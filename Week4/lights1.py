import asyncio
import aiohttp
import time

STUDENT_ID = "6710301023"
BASE_URL = "http://172.16.2.117:8088"

async def turn_on_light(session, light_id):
    url = f"{BASE_URL}/api/{STUDENT_ID}/lights/{light_id}"
    async with session.post(url, json={"status": "ON"}) as resp:
        data = await resp.json()
        print(f"{light_id} -> {data['current_status']}")

async def main():
    # เริ่มจับเวลา
    start_time = time.perf_counter()

    async with aiohttp.ClientSession() as session:
        # รอทีละดวง เรียงตามลำดับ 1 -> 2 -> 3 -> 4
        await turn_on_light(session, "light_1")
        await turn_on_light(session, "light_2")
        await turn_on_light(session, "light_3")
        await turn_on_light(session, "light_4")

    # หยุดจับเวลา
    end_time = time.perf_counter()
    total_time = end_time - start_time

    print(f"\nเวลารวมในการเปิดไฟทั้งหมด: {total_time:.2f} วินาที")

asyncio.run(main())