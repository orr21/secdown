import re
from datetime import datetime

class Validator:
    def __init__(self):
        self.current_year = datetime.today().year
        self.current_month = datetime.today().month

    def validate_year(self, year: int) -> None:
        if year is None:
            raise ValueError("Year must be specified.")
        if year < 2009:
            raise ValueError("Year cannot be less than 2009.")
        if year > self.current_year:
            raise ValueError(f"Year cannot be greater than the current year ({self.current_year}).")

    def ensure_identification(self, identified: bool) -> None:
        if not identified:
            raise ValueError("User must be identified before downloading data.")

    def validate_email(self, email: str) -> None:
        if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email format.")

    def is_future_data(self, year: int, month: str) -> bool:
        return int(year) == self.current_year and int(month) > self.current_month
