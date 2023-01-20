from utils.test_functions import test_flow
from multiprocessing import Pool
import time, os, os.path
from dotenv import load_dotenv

if __name__ == '__main__':
    """End-to-end test.
    The goal is to simulate what a real user
    scenario looks like from start to finish.
    The test is running until the number of files downloaded by all user will be at least 20.
    Users are randomly choosing among four video files with different duration time (30, 60, 105, 210 seconds).
    """
    load_dotenv()
    start = time.time()

    while len([name for name in os.listdir('mp3s')]) < 25:
        with Pool() as pool:
            users = [
                ('notification.converter.bot@gmail.com', os.getenv('PASS_1'), os.getenv('GMAIL_PASS_1')),
                ('johnsmith.app11@gmail.com', os.getenv('PASS_2'), os.getenv('GMAIL_PASS_2')),
                ('projektum2022@gmail.com', os.getenv('PASS_3'), os.getenv('GMAIL_PASS_3'))
                ]
            pool.starmap(test_flow, users)

    test_time = time.time() - start
    print(f'Test time: {test_time}s')
