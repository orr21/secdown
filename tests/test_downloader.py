import pytest
from secdown.downloader import SECDatasetDownloader

@pytest.fixture
def downloader():
    return SECDatasetDownloader()

def test_set_identity(downloader):
    downloader.set_identity("test@example.com")
    assert downloader.is_identified() is True

def test_set_identity_invalid_email(downloader):
    with pytest.raises(ValueError, match="Invalid email format."):
        downloader.set_identity("invalid-email")

def test_get_year_data_without_identification(downloader):
    with pytest.raises(ValueError, match="User must be identified before downloading data."):
        downloader.get_year_data(2021)
