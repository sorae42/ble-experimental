import sys
import asyncio
import time
from random import randint

from bleak import BleakClient

ADDRESS = "022481EE-AD90-A4E7-DB74-95A825543696"
GENERAL_CHAR = "0000ee02-0000-1000-8000-00805f9b34fb"

def modify(a, b, c, d, rgb, alpha):
    return bytearray([a, b, c, d, rgb[0], rgb[1], rgb[2], alpha])
    
def calcTime(s):
    min, sec = divmod(s, 60)
    hour, min = divmod(min, 60)
    return '%d:%02d:%02d' % (hour, min, sec)
    
def rand():
    return randint(0,255)

CLOCK = 0.0121

async def main(address):
    print("[INFO] initializing test...")
    async with BleakClient(address) as client:
        test_num = 0
        while True:
            test_num = test_num + 1
            print("\r[INFO] test #" + str(test_num) + " in progress!!               ")
            for i in range(255, -1, -1):
                #color = [rand(), rand(), rand()]
                color = [i, i, i]
                alpha = 255
                a = 0x69
                b = 0x96
                c = 0x5
                d = 0x2
                converted = modify(a, b, c, d, color, alpha)
                await client.write_gatt_char(GENERAL_CHAR, converted)
                print("\rclock: " + str(CLOCK) + "s - PROGRESS set OK: " + str(i) + "   ", end="")
                time.sleep(CLOCK)
            print("\rtest OK... ^C to conclude the test", end="")
            time.sleep(2)

if __name__ == "__main__":
    asyncio.run(main(sys.argv[1] if len(sys.argv) == 2 else ADDRESS))