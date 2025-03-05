import os

class FileManager:
    def __init__(self):
        """Initializes file manager with a base folder"""

    def create_year_folder(self, year: int, base_folder: str = "data") -> str:
        """
        Creates a directory for storing data of the given year.

        :param year: The year for which the folder is created.
        :return: The path of the created folder.
        """
        year_folder = os.path.join(base_folder, str(year))
        os.makedirs(year_folder, exist_ok=True)
        return year_folder
