# stock_price_httpx.py
# Assignment 3: Concurrency Racing บนระบบเครือข่ายจริงร่วมกับ httpx + FastAPI Mock Server
import asyncio
import httpx
from time import ctime


async def fetch_stock_price(server_name: str):
    """
    เชื่อมต่อ Mock Server ผ่านระบบเครือข่ายจริงด้วย httpx.AsyncClient
    (เป็น async ทำให้ไม่ Block Event Loop ระหว่างรอ response)
    """
    url = f"http://127.0.0.1:8088/price/{server_name}"  # เปลี่ยนเป็น IP/host จริงของเซิร์ฟเวอร์อาจารย์

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        return f"[{data['server']}] Price: {data['price_usd']} USD"


async def main():
    servers = ["Alpha", "Beta", "Gamma"]

    # แตก Task ยิงคำขอไปทั้ง 3 เซิร์ฟเวอร์พร้อมกัน
    tasks = {asyncio.create_task(fetch_stock_price(name)) for name in servers}

    # รอจนกว่าจะมีตัวใดตัวหนึ่งเสร็จก่อน (racing)
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    # แสดงผลลัพธ์ของผู้ชนะ
    winner = list(done)[0]
    print(f"{ctime()} Winner Server Result: {winner.result()}")

    # ปิดกั้น/ยกเลิก Task ที่ยัง pending อยู่ทันที
    for pending_task in pending:
        pending_task.cancel()

    if pending:
        await asyncio.gather(*pending, return_exceptions=True)

    print(f"{ctime()} Cleanup complete. Cancelled {len(pending)} pending connection(s).")


if __name__ == "__main__":
    asyncio.run(main())