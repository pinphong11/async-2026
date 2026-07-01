# Program 6: Creating a Concurrent Task
# Concept: Wrapping a coroutine inside asyncio.create_task() to schedule it to run in the background.

import asyncio
from time import time,ctime

async def cook_spaghtti(customer):
    print(f"{ctime()} | Cooking spaghetti for {customer}...")
    await asyncio.sleep(1)  # Simulate a delay of 1 second
    print(f"{ctime()} | Finished cooking spaghetti for {customer}.")
    
async def main():
    start_time = time()
    
    # Create a task for cooking spaghetti for Alice
    task_a = asyncio.create_task(cook_spaghtti("Alice")) #สร้าง task1 ขึ้นมาเพื่อให้ทำงานแบบ Async
    
    # Create a task for cooking spaghetti for Bob
    # task2 = asyncio.create_task(cook_spaghtti("Bob"))
    
    # Wait for both tasks to complete
    await task1  #สำคัญ เพราะทำให้เป็น Async
    # await task2
    
    print(f"Total Time: {time() - start:.2f} seconds")
    
if __name__ == "__main__":
    asyncio.run(main())  # Run the main coroutine using the event loop