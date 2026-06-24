from time import sleep, ctime, time, process_time
import os
import threading
import psutil


# ฟังก์ชันจำลองการทำกาแฟให้ลูกค้า 1 คนแบบซิงโครนัส
def make_coffee(customer_name):
    #ดึง PID และ THREAD ID ออกมาดู
    pid = os.getpid()
    thread_id = threading.current_thread().native_id
    thread_name = threading.current_thread().name

    print(f"{ctime()} | [PID: {pid}] [TID: {thread_id}] [Thread Name: {thread_name}] กำลังชงกาแฟให้ลูกค้า {customer_name}...")
    sum(i * i for i in range(10000000))  # จำลองงานคำณวนหนัก (CPU-bound) เล็กน้อย และรอเวลา 5 วินาที
    sleep(5) #บล็อกการทำงานของ Thread ปัจจุบัน 5 วินาที
    print(f"{ctime()} | [PID: {pid}] [TID: {thread_id}] [Thread Name: {thread_name}] ลูกค้า {customer_name}: ได้รับกาแฟแล้ว!")

def main():
    queue = ['A', 'B', 'C']
    main_pid = os.getpid()
    main_tid = threading.current_thread().native_id

    print(f"{ctime()} | [Main PID: {main_pid}] [Main TID: {main_tid}] === เริ่มต้นการทำงานของร้านกาแฟแบบ Synchronous ===")
    start_time = time()
    start_cpu = process_time() #เริ่มต้นจับเวลา CPU
    
    #ลูปทำงานตามลำดับคิวเดี่ยวทีละคน
    for customer in queue:
        make_coffee(customer)

    duration = time() - start_time 
    cpu_duration = process_time() - start_cpu 

    #ใช้ psutil ดึงขค่าการกิน RAM
    process = psutil.process(os.getpid())
    mem_mb = process.memory_info().rss / (1024 * 1024)

    print(f"[สรุปผล synchronous]" )
    print(f" เวลาในการทำงานทั้งหมด: {duration:.2f} วินาที")
    print(f" เวลา CPU ที่ใช้ (CPU time): {cpu_duration:0.4f} วินาที")
    print(f" ความจุหน่วยความจำที่ใช้: {mem_mb:.2f} MB")

if __name__ == "__main__":
    main()
