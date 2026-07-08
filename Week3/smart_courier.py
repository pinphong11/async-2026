# Assignment 1: The Smart Courier System (ระบบส่งพัสดุด่วน)
import asyncio
from time import ctime


async def delivery_task(package_id, duration):
    # เริ่มส่งพัสดุ พิมพ์ข้อความแจ้งเริ่มงาน
    print(f"{ctime()} Courier: Starting delivery of package {package_id} (ETA {duration}s)...")
    try:
        # จำลองเวลาที่ใช้ในการส่งของ
        await asyncio.sleep(duration)
        print(f"{ctime()} Courier: Package {package_id} arrived at destination!")
        return f"Package {package_id} Delivered!"
    except asyncio.CancelledError:
        # ดักจับตอนถูกยกเลิกงานกลางคัน
        print(f"{ctime()} Delivery Canceled! Returning package to warehouse.")
        raise  # ต้อง raise ต่อ ไม่งั้น Task จะไม่ถูกมาร์คว่า cancelled จริง


async def main():
    # สร้าง Task จาก delivery_task พร้อมตั้งชื่อ Task
    task = asyncio.create_task(delivery_task(package_id="P001", duration=5.0))
    task.set_name("Express-Courier")

    # จำลองว่าเวลาผ่านไป 2 วินาทีระหว่างพัสดุกำลังเดินทาง
    await asyncio.sleep(2.0)

    # ตรวจสอบสถานะ + พิมพ์ชื่อ Task ปัจจุบัน
    print(f"{ctime()} Main: Checking on task '{task.get_name()}' -> Done? {task.done()}")

    if not task.done():
        # ถ้ายังไม่เสร็จ (นานเกินไป) ให้ยกเลิกงานทันที
        print(f"{ctime()} Main: Delivery is taking too long! Cancelling '{task.get_name()}' now.")
        task.cancel()

    try:
        await task  # await task ที่ถูก cancel จะ raise CancelledError ออกมาที่นี่
    except asyncio.CancelledError:
        print(f"{ctime()} Main: Confirmed task was cancelled from the caller side.")

    # ตรวจสอบสถานะ .cancelled() ว่าเป็น True หรือไม่
    print(f"{ctime()} Main: Is task cancelled? {task.cancelled()}")


if __name__ == "__main__":
    asyncio.run(main())