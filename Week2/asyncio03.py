# Program 3: The Event Loop (asyncio.run)
# Concept: Using the Event Loop to actually execute a Coroutine Object.
import asyncio

async def greet():
    print("Hello from the Event Loop! ")

if __name__ == "__main__":
    coro_obj = greet()  # Create a coroutine object

    asyncio.run(coro_obj)  # Run the coroutine object using the event loop  
    