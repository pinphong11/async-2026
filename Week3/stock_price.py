# Assignment 2: The Stock Price Race (ระบบแข่งดึงข้อมูลราคาหุ้น) - Mock Version
# ใช้ asyncio.wait() พร้อม return_when=FIRST_COMPLETED เท่านั้น ตามสเปก
import asyncio
from time import ctime


async def fetch_stock_price(server_name, delay):
    # จำลองความหน่วงของแต่ละเซิร์ฟเวอร์
    await asyncio.sleep(delay)
    return f"[{server_name}] Price: 150 USD"


async def main():
    # สร้าง Task พร้อมกัน 3 ตัวสำหรับ 3 เซิร์ฟเวอร์
    tasks = {
        asyncio.create_task(fetch_stock_price("Alpha", 3.0)),
        asyncio.create_task(fetch_stock_price("Beta", 0.8)),
        asyncio.create_task(fetch_stock_price("Gamma", 1.5)),
    }

    # แข่งกัน ใครเสร็จก่อนถือว่าชนะ (FIRST_COMPLETED)
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    # แสดงผลลัพธ์ของผู้ชนะ
    winner = list(done)[0]
    print(f"{ctime()} Winner Server Result: {winner.result()}")

    # ยกเลิก Task ที่เหลือ (ยัง pending อยู่) ทั้งหมด ป้องกัน Memory Leak
    for pending_task in pending:
        pending_task.cancel()

    # รอให้การ cancel เสร็จสมบูรณ์ก่อนจบโปรแกรม
    if pending:
        await asyncio.gather(*pending, return_exceptions=True)

    print(f"{ctime()} Cleanup complete. Cancelled {len(pending)} pending task(s).")


if __name__ == "__main__":
    asyncio.run(main())