import os
import requests
import zipfile
from io import BytesIO
from datetime import datetime
from .validator import Validator
from .file_manager import FileManager
from .link_generator import LinkGenerator
from .utils import wait_random_time
from .config import *

class SECDatasetDownloader:
    """
    A class responsible for downloading SEC financial datasets.

    Attributes:
    - identified (bool): Whether the user has been identified.
    - headers (dict): HTTP headers for requests.
    - start_year (int): The starting year for available data.
    - current_year (int): The current year.
    - current_month (int): The current month.
    """

    def __init__(self):
        self.identified = False
        self.headers = None
        self.start_year = 2009
        self.current_year = datetime.today().year
        self.current_month = datetime.today().month
        self.validator = Validator()
        self.file_manager = FileManager()
        self.link_generator = LinkGenerator()

    def set_identity(self, email: str) -> None:
        """
        Identifies the user with an email address.

        :param email: User email.
        :raises ValueError: If the email is invalid.
        """
        self.validator.validate_email(email)
        self.headers = { "User-Agent": USER_AGENT_TEMPLATE.format(email=email) }
        self.identified = True
        print(f"🔑 User identified as {email}")

    def is_identified(self) -> bool:
        """
        Checks if the user has been identified.

        :return: True if identified, False otherwise.
        """
        return self.identified
    
    def get_historical_data(self, base_folder: str = "data") -> None:
        """
        Downloads all available historical data.
        """
        for year in range(self.start_year, self.current_year + 1):
            self.get_year_data(year, base_folder)

    def get_year_data(self, year: int, base_folder: str = "data") -> None:
        """
        Downloads all available data for a specific year.
        
        :param base_folder: The base directory for storing the downloaded data.
        :param year: The year for which data should be downloaded.
        :raises ValueError: If the user is not identified or the year is invalid.
        """
        self.validator.validate_year(year)
        self.validator.ensure_identification(self.identified)

        year_folder = self.file_manager.create_year_folder(year, base_folder)

        if year < self.current_year - 1:
            self._download_by_quarters(year, year_folder)
        else:
            self._download_by_months(year, year_folder)

    def _download_by_quarters(self, year: int, year_folder: str) -> None:
        """
        Downloads data organized by quarters.

        :param year: The year for which quarterly data is downloaded.
        :param year_folder: The base directory for storing the downloaded data.
        """
        for url, quarter in self.link_generator.generate_quarter_links(year):
            folder_name = os.path.join(year_folder, quarter)
            self._process_download(url, folder_name)

    def _download_by_months(self, year: int, year_folder: str) -> None:
        """
        Downloads data organized by months.

        :param year: The year for which monthly data is downloaded.
        :param year_folder: The base directory for storing the downloaded data.
        """
        for url, month in self.link_generator.generate_month_links(year):
            folder_name = os.path.join(year_folder, month)
            if self.validator.is_future_data(year, month):
                continue
            self._process_download(url, folder_name)

    def _process_download(self, url: str, folder_name: str) -> None:
        """
        Handles the downloading and extraction of data.

        :param url: The URL of the data to be downloaded.
        :param folder_name: The folder where the downloaded data will be stored.
        """
        if os.path.exists(folder_name):
            print(f"✅ {folder_name} already exists, skipping download.")
            return

        print(f"🔄 Attempting to download: {url}")
        self._download_and_unzip(url, folder_name)
        wait_random_time()

    def _download_and_unzip(self, url: str, extract_to: str) -> bool:
        """
        Downloads and extracts a ZIP file from the SEC.

        :param url: URL of the ZIP file.
        :param extract_to: Destination folder for extraction.
        :return: True if successful, False otherwise.
        """
        with requests.Session() as session:
            session.headers.update(self.headers)

            try:
                print(f"🔄 Downloading: {url}")
                response = session.get(url, timeout=30)

                if response.status_code == 404:
                    print(f"❌ Not available: {url}")
                    return False

                response.raise_for_status()
                os.makedirs(extract_to, exist_ok=True)

                with zipfile.ZipFile(BytesIO(response.content)) as zip_file:
                    zip_file.extractall(path=extract_to)

                print(f"✅ Downloaded and extracted to {extract_to}")
                return True

            except requests.exceptions.RequestException as e:
                print(f"⛔ Error downloading {url}: {e}")
                return False
