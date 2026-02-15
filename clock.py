import time
import os
import datetime

while True:
    adesso = datetime.datetime.now()
    print(f"deta: {adesso.strftime('%d/%m/%Y')} | Ora: {adesso.strftime('%H:%M:%S')}", end="\r")
    time.sleep(1)