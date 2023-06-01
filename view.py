from tqdm import tqdm
import time as t


def message(message):
    print(message)

def progressbar():
    for i in tqdm(range(100), desc="Loading..."):
        t.sleep(0.05)