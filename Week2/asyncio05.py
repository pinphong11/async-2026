# Program 5: Sequential Execution (The Wrong Way)
# Concept: Showing that simply awaiting one after another is still sequential (Synchronous behavior).
import asyncio
from time import time, ctime

async def sever_customer(name):
    print(f"{ctime()} -> Cooking for {name}...")
    await asyncio.sleep(1)  # Simulate a long-running operation
    print(f"{ctime()} -> served {name}!")

async def main():
    start = time()
    # If you await them one by one, they still run sequentially!!
    await sever_customer("A")
    await sever_customer("B")

    print(f"Total time: {time() - start:0.2f} seconds") #will be 
if __name__ == "__main__":
    asyncio.run(main())   