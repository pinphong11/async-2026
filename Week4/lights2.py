import asyncio
import aiohttp
import time

student_id = "6710301023"
base_url = "http://172.16.2.117:8088"

lights = [
    ("light_1", 0.5),
    ("light_2", 1.2),
    ("light_3", 2.0),
    ("light_4", 0.8)
]

async def control_light(session, light_id):
    async with session.post(
        f"{base_url}/api/{student_id}/lights/{light_id}",
        json={"status": "ON"}
    ) as response:
        result = await response.json()
        print(result)

async def main():
    start_time = time.perf_counter()   # เริ่มจับเวลา

    async with aiohttp.ClientSession() as session:
        # เรียงตาม delay จากน้อยไปมาก
        for light_id, delay in sorted(lights, key=lambda x: x[1]):
            await control_light(session, light_id)

    end_time = time.perf_counter()     # หยุดจับเวลา
    total_time = end_time - start_time

    print(f"\nเวลารวมในการเปิดไฟทั้งหมด: {total_time:.2f} วินาที")

asyncio.run(main())