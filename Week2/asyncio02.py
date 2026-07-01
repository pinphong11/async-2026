# Program 2: The Coroutine Object
# Concept: Seeing that calling an async def function creates an "Object" but does not execute it yet.

import asyncio

async def greet():
    print("Hello ")
#Calling the async def function creates a coroutine object but does not execute it yet.
coro_obj = greet()

print(type(coro_obj))

coro_obj.close()  # Close the coroutine object to avoid warnings about unawaited coroutines