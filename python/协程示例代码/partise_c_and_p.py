import asyncio
import random
import time

async def consumer(queue, id):
    # 无限循环的消费者
    while True:
        # 每次从队列中
        val = await queue.get()
        print(f"{id} get a val: {val}")
        await asyncio.sleep(1)

async def producer(queue, id):
    for i in range(5):
        val = random.randint(1,10)
        await queue.put(val)
        print(f"{id} put a val: {val}")
        await asyncio.sleep(1) 

async def main():
    queue = asyncio.Queue()

    consumer_1 = asyncio.create_task(consumer(queue, 'consumer_1')) 	# create a task with a callback function to check queue for items
    consumer_2 = asyncio.create_task(consumer(queue, 'consumer_2')) 	# create a task with a callback function to check

    producer_1 = asyncio.create_task(producer(queue, 'producer_1')) 	# create a task with a callback
    producer_2 = asyncio.create_task(producer(queue, 'producer_2')) 	# task with a callback function to check queue

    await asyncio.sleep(10)
    consumer_1.cancel()
    consumer_2.cancel()

    await asyncio.gather(producer_1,producer_2,consumer_1,consumer_2, return_exceptions=True) # run everything in parallel


start_time = time.time()
asyncio.run(main())
end_time = time.time()
total_time = end_time - start_time
print("总共用时：", total_time, "秒")
