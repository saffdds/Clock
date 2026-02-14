import time
import os

while True:
    print(f"Time: {time.strftime('%H:%M:%S') }", end="\r")
    time.sleep(1)