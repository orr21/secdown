import time
import random

def wait_random_time() -> None:
    """Introduces a random delay to avoid rate limiting"""
    time.sleep(random.uniform(5, 15))
