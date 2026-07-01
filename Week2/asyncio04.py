# Program 4: The await Keyword
# Concept: Pausing a coroutine to let another operation finish using await.
import asyncio
from time import ctime

async def main():
    print(f"{ctime()} -> Task 1: Started")
    
    await asyncio.sleep(1)  # Simulate a long-running operation
    
    print(f"{ctime()} -> Task 1: Finished")

if __name__ == "__main__":
    asyncio.run(main())
