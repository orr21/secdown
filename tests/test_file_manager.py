import os
import shutil
import pytest
from secdown.file_manager import FileManager

@pytest.fixture
def file_manager():
    return FileManager()

def test_create_year_folder(file_manager):
    folder = file_manager.create_year_folder(2020, "test_data")
    assert os.path.exists(folder)
    shutil.rmtree("test_data")
