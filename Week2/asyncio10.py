# Program 10: Extracting Return Values from Tasks
# Concept: Accessing returned results from completed Task objects using .result() or direct assignment.

import asyncio

async def calculate_bill(customer, base_price):
    print(f"Calculating bill for {customer}...")
    await asyncio.sleep(1)  # Simulate a delay of 1 second
    total = base_price * 1.07  # Adding a 7% tax
    print(f"Total bill for {customer}: ${total:.2f}")
    return total

async def main():
    # Create tasks for calculating bills for two customers
    task1 = asyncio.create_task(calculate_bill("Alice", 50))
    task2 = asyncio.create_task(calculate_bill("Bob", 75))

    # Wait for both tasks to complete and get their results
    total1 = await task1
    total2 = await task2

    print(f"Final Total for Alice: ${total1:.2f}")
    print(f"Final Total for Bob: ${total2:.2f}")

if __name__ == "__main__":
    asyncio.run(main())  # Run the main coroutine using the event loop