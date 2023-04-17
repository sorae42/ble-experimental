import sys
import asyncio
import time

from bleak import BleakClient

ADDRESS = "A1379F49-AA6C-D07E-5B6B-C7971F54AC85"
GENERAL_CHAR = "0000ee02-0000-1000-8000-00805f9b34fb"
STEP = 16
DELAY = 42

def toRGB(c, a):
    return bytearray([0x69, 0x96, 0x5, 0x2, c[0], c[1], c[2], a])

def calcTime(s):
    time_obj = time.gmtime(s)
    return time.strftime("%H:%M:%S", time_obj)

async def main(address):
    print("ok wait")
    async with BleakClient(address) as client:
        total = STEP * DELAY
        print("seconds: " + str(total))
        for i in range(STEP, -1, -1):
            color = [i, 0, round(i/2)]
            alpha = 0
            converted = toRGB(color, alpha)
            print(color)
            await client.write_gatt_char(GENERAL_CHAR, converted)
            print("SET ok: " + str(i))
            for j in range(DELAY, 0, -1):
                total = total - 1
                print("\r" + str(j) + "s until next jump ( " + calcTime(total) + " til finish)               ", end="") 
                time.sleep(1)


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1] if len(sys.argv) == 2 else ADDRESS))
