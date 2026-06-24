from time import ctime, time, process_time
import asyncio
import os
import threading
import psutil

# ฟังก์ชันลองทำงานแบบ Asyncynchronous
async def make_coffee(customer_name):

    # 1. ดู Process ID และ Thread ID (ยังคงเหมือนเดิมเสมอในทุก Task)
    pid = os.getpid()
    thread_id = threading.current_thread().native_id

    # 2. ดูข้อมูล Task ปัจจุบันของ asyncio
    current_task = asyncio.current_task()
    task_name = current_task.get_name()  # ชื่อ Task

    # ใน Python 3.12+ สามารถใช้หา Unique ID ของ Task ได้ผ่าน id(current_task)
    task_id = id(current_task)

    print(
        f"[{ctime()}] [PID: {pid}] [TID: {thread_id}] "
        f"[Async Task ID: {task_id}] [Task Name: {task_name}] "
        f"กำลังชงกาแฟให้ ลูกค้า {customer_name}..."
    )

    sum(i * i for i in range(1000000))  # จำลองงานคำนวณ (CPU-bound) เล็กน้อย และรอ 5 วินาที

    # หยุดงาน (Non-blocking Wait)
    await asyncio.sleep(5)

    print(
        f"[{ctime()}] [PID: {pid}] [TID: {thread_id}] "
        f"[Async Task ID: {task_id}] [Task Name: {task_name}] "
        f"ลูกค้า {customer_name}: ได้รับกาแฟแล้ว!"
    )


async def main():

    queue = ['A', 'B', 'C']

    main_pid = os.getpid()
    main_tid = threading.current_thread().native_id

    print(
        f"[{ctime()}] [Main PID: {main_pid}] [Main TID: {main_tid}] "
        f"=== เริ่มระบบร้านกาแฟแบบ asyncio ==="
    )

    start_time = time()
    start_cpu = process_time()

    tasks = []

    for customer in queue:

        # สร้าง Coroutine
        coro = make_coffee(customer)

        # แปลง Coroutine เป็น Task เพื่อให้ Event Loop บริหารและสลับรันได้
        task = asyncio.create_task(
            coro,
            name=f"Task-{customer}"
        )

        tasks.append(task)

    # รอให้ทำงานพร้อมกัน
    await asyncio.gather(*tasks)

    duration = time() - start_time
    cpu_duration = process_time() - start_cpu

    process = psutil.Process(os.getpid())
    mem_mb = process.memory_info().rss / (1024 * 1024)

    print("\n[ข้อมูล Asyncio]")
    print(f"เวลาที่ใช้จริง (Wall Time): {duration:.2f} วินาที")
    print(f"เวลาที่ CPU ใช้งานสะสมจริง (CPU Time): {cpu_duration:.4f} วินาที")
    print(f"หน่วยความจำ Memory (RAM) ที่ใช้: {mem_mb:.2f} MB")


if __name__ == "__main__":
    asyncio.run(main())