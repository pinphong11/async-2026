import asyncio
import time


async def greet_customer(name: str) -> None:
    print(f"{time.ctime()} Greeting for {name} ...")
    await asyncio.sleep(1)
    print(f"{time.ctime()} Greeting for {name} ...Done!")


async def take_order(name: str) -> None:
    print(f"{time.ctime()} [{name}] Taking Order ...")
    await asyncio.sleep(1)
    print(f"{time.ctime()} [{name}] Taking Order ...Done!")


async def cook_spaghetti(name: str) -> None:
    print(f"{time.ctime()} [{name}] Cooking Spaghetti ...")
    await asyncio.sleep(1)
    print(f"{time.ctime()} [{name}] Cooking Spaghetti ...Done!")


async def manage_bar(name: str) -> None:
    print(f"{time.ctime()} [{name}] Manage Bar for Drink ...")
    await asyncio.sleep(1)
    print(f"{time.ctime()} [{name}] Manage Bar for Drink ...Done!")


async def serve_customer(name: str) -> None:
    """งานอิสระของแต่ละโต๊ะ: สั่งอาหาร -> ทำอาหาร -> ทำเครื่องดื่ม -> เสิร์ฟ"""
    await take_order(name)
    await cook_spaghetti(name)
    await manage_bar(name)
    print(f"{time.ctime()} [{name}] All served!")


async def main() -> None:
    start = time.perf_counter()

    customers = ["Customer-A", "Customer-B", "Customer-C"]
    tasks = ["Task-A", "Task-B", "Task-C"]

    # 1) ต้อนรับลูกค้าทีละคน (sequential)
    for customer in customers:
        await greet_customer(customer)

    print()
    print(f"{time.ctime()} --- All customers greeted. Scheduling independent Async Tasks! ---")
    print()

    # 2) สร้าง Task อิสระให้รันพร้อมกันสำหรับแต่ละโต๊ะ (concurrent)
    await asyncio.gather(*(serve_customer(t) for t in tasks))

    elapsed = time.perf_counter() - start
    print()
    print(f"{time.ctime()} Finished Entire Restaurant Operation in {elapsed:.2f} seconds.")


if __name__ == "__main__":
    asyncio.run(main())