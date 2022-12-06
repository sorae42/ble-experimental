import sys
import asyncio

from bleak import BleakClient

ADDRESS = "022481EE-AD90-A4E7-DB74-95A825543696"
GENERAL_CHAR = "0000ee02-0000-1000-8000-00805f9b34fb"

def toRGB(c, a):
    return bytearray([0x69, 0x96, 0x5, 0x2, c[0], c[1], c[2], a])

async def main(address):
    print("ok wait")
    async with BleakClient(address) as client:
        while True:
            print("rgb enter")
            a = int(input())
            b = int(input())
            c = int(input())
            color = [a, b, c]
            alpha = 0xFF
            converted = toRGB(color, alpha)
            print(color)
            await client.write_gatt_char(GENERAL_CHAR, converted)

if __name__ == "__main__":
    asyncio.run(main(sys.argv[1] if len(sys.argv) == 2 else ADDRESS))