import pytest
from secdown.validator import Validator

@pytest.fixture
def validator():
    return Validator()

def test_validate_year_valid(validator):
    validator.validate_year(2015)

def test_validate_year_below_minimum(validator):
    with pytest.raises(ValueError, match="Year cannot be less than 2009."):
        validator.validate_year(2008)

def test_validate_year_above_maximum(validator):
    with pytest.raises(ValueError, match="Year cannot be greater than the current year"):
        validator.validate_year(2026)

def test_ensure_identification(validator):
    with pytest.raises(ValueError, match="User must be identified before downloading data."):
        validator.ensure_identification(False)

def test_validate_email_valid(validator):
    validator.validate_email("test@example.com")

def test_validate_email_invalid(validator):
    with pytest.raises(ValueError, match="Invalid email format."):
        validator.validate_email("invalid-email")

def test_is_future_data(validator):
    assert validator.is_future_data(2025, "12") is True
    assert validator.is_future_data(2024, "10") is False
