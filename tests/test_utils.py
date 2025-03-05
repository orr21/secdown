from secdown.utils import wait_random_time
import time

def test_wait_random_time():
    start = time.time()
    wait_random_time()
    end = time.time()
    assert 5 <= (end - start) <= 15