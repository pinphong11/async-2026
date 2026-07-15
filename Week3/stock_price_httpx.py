# Assignment 3: Stock Price Race (Live FastAPI + HTTPX) (10 คะแนน)
# Objective: ประยุกต์ใช้ Concurrency บนระบบเครือข่ายจำลองจริงร่วมกับ httpx
#
# ก่อนรันไฟล์นี้ ต้องเปิด Mock Server ก่อนในอีก Terminal หนึ่ง:
#   uvicorn stock_api:app --reload --port 8088

import asyncio
import httpx
from time import ctime

# ตั้งค่า Base URL ของ Mock Server (รันอยู่บนเครื่องเดียวกัน -> ใช้ 127.0.0.1)
BASE_URL = "http://127.0.0.1:8088"


# ──────────────────────────────────────────────
# ฟังก์ชันเชื่อมต่อ Mock Server ผ่านระบบเครือข่ายจริง
# ──────────────────────────────────────────────
async def fetch_stock_price(server_name: str):
    """
    เชื่อมต่อไปยัง Stock Price API Server ของอาจารย์ (FastAPI, พอร์ต 8088)
    - ห้ามรับพารามิเตอร์ delay (latency เกิดขึ้นจริงที่ฝั่ง Server แล้ว)
    - ใช้ httpx.AsyncClient() แบบ async with เพื่อไม่ Block Event Loop
    - แปลง JSON ที่ได้ (server, price_usd) มาจัดฟอร์แมตเป็นข้อความ
    """
    url = f"{BASE_URL}/price/{server_name}"
    print(f"{ctime()} [{server_name}] กำลังเชื่อมต่อ {url} ...")

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        print(f"{ctime()} [{server_name}] ได้รับข้อมูลจาก Server แล้ว!")
        return f"[{data['server']}] Price: {data['price_usd']} USD"


# ──────────────────────────────────────────────
# ฟังก์ชันหลัก: Concurrency Racing
# ──────────────────────────────────────────────
async def main():
    print(f"{ctime()} {'='*55}")
    print(f"{ctime()} [Main] === Stock Price Race (Live Network) เริ่มการแข่งขัน ===")
    print(f"{ctime()} {'='*55}\n")

    # แปลงคอรูทีนของทั้ง 3 สาขาให้เป็น asyncio.Task เพื่อส่งเข้าคิวรันพร้อมกัน
    tasks = {
        asyncio.create_task(fetch_stock_price("alpha"), name="Alpha"),
        asyncio.create_task(fetch_stock_price("beta"), name="Beta"),
        asyncio.create_task(fetch_stock_price("gamma"), name="Gamma"),
    }

    print(f"{ctime()} [Main] ส่ง Task ทั้ง 3 สาขาเข้าคิว Event Loop พร้อมกันแล้ว\n")

    # ใช้ asyncio.wait() + FIRST_COMPLETED เพื่อดีดตัวออกทันที
    # เมื่อมีเซิร์ฟเวอร์ตัวแรกส่งข้อมูลกลับมาสำเร็จ
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    # แสดงผลลัพธ์ของเซิร์ฟเวอร์ที่ชนะการแข่งขัน
    winner_task = done.pop()
    print(f"\n{ctime()} [Main] ─── ผลการแข่งขัน ───")
    print(f"{ctime()} [Main] เซิร์ฟเวอร์ที่ชนะ (เร็วที่สุด): {winner_task.get_name()}")
    print(f"{ctime()} [Main] ผลลัพธ์ที่ได้: {winner_task.result()}")

    # [สำคัญมาก - Anti-Memory Leak]
    # วนลูปดึงงานที่ยังค้างอยู่ใน pending มาสั่งยกเลิกทิ้งให้หมดสิ้น
    # เพื่อตัดสัญญาณ Network Request ที่ยังวิ่งค้างอยู่บนระบบเครือข่าย
    print(f"\n{ctime()} [Main] ─── ล้างระบบ (Anti-Memory Leak) ───")
    for ongoing_task in pending:
        print(f"{ctime()} [Main] ยกเลิก Network Request ที่ยังค้างอยู่: {ongoing_task.get_name()}")
        ongoing_task.cancel()

    # yield ให้ Event Loop ประมวลผลการ cancel ให้เสร็จสมบูรณ์ก่อนจบโปรแกรม
    await asyncio.gather(*pending, return_exceptions=True)

    print(f"\n{ctime()} [Main] ล้างระบบเสร็จสิ้น — Request ที่เหลือถูกยกเลิกทั้งหมดแล้ว")
    print(f"{ctime()} {'='*55}")


if __name__ == "__main__":
    asyncio.run(main())