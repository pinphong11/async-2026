import asyncio
from time import sleep, ctime, time

#Greting synchronous 
def greet_dinners(customer):
    print(f"ctime: {ctime()} - Hello {customer}, welcome to our restaurant!")
    sleep(1)  # Simulate a delay
    print(f"ctime: {ctime()} - How are you today, {customer},...Done")

#Do order
def do_order(customer):
    print(f"ctime: {ctime()} - Taking order from {customer}...")
    sleep(1)  # Simulate a delay
    print(f"ctime: {ctime()} - Taking order from {customer}...Done")

#Do cooking
def do_cooking(customer):
    print(f"ctime: {ctime()} - Cooking for {customer}...")
    sleep(1)  # Simulate a delay
    print(f"ctime: {ctime()} - Cooking for {customer}...Done")

def mini_bar(customer):
    print(f"ctime: {ctime()} - Preparing drinks for {customer}...")
    sleep(1)  # Simulate a delay
    print(f"ctime: {ctime()} - Preparing drinks for {customer}...Done")

if __name__ == "__main__":
    customers = ["Alice", "Bob", "Charlie"]
    start_time = time()

    for customer in customers:
        greet_dinners(customer)
        do_order(customer)
        do_cooking(customer)
        mini_bar(customer)    

    duration = time() - start_time
    print(f"Finish cooking in: {duration:.2f} seconds")    