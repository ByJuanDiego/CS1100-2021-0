"""
from time import localtime, strftime, sleep

while True:
    hora_local = localtime()
    result = strftime("%I:%M:%S %p", hora_local)
    print(result)
    sleep(1)"""
import time

while True:
    hora_local = time.localtime()
    result = time.strftime("%I:%M:%S %p", hora_local)
    print(result)
    time.sleep(1)
