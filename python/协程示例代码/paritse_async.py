# 简单的协程改造
import asyncio
import time

async def crawl_page(url):
    print(f'crawling {url}')
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)  # await asyncio.sleep() 函数的返回值是一个任务队列
    print(f'OK {url}')

async def main(urls):  # main coroutine 创建任务队列并执行队列中的任务（可以是任务
    
    # ----------------------------------------------------------------
    # 如果按以下方式写，就是等待每次执行完毕再进行下一次执行，等于同步代码
    # for url in urls:
    #     await crawl_page(url)  
    # ----------------------------------------------------------------
    
    # 创建任务，注意，当创建create_task时，任务就已经开始执行了
    tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
    
    # 异步等待3秒后，取消掉第四个任务
    # 注意，如果休息时间超过执行时间，此时在这之后调用cancel是无效的，因为已经执行完了
    await asyncio.sleep(3)
    tasks[3].cancel()
    
    # 如果不设置return_exceptions=True，那么并发途中产生的报错会抛出，并且停止其余所有的执行
    # 设置return_exceptions=True，异常会在res中存储
    res = await asyncio.gather(*tasks, return_exceptions=True)  
    print(res)
    
    # 也可以for循环等待所有task,如下
    # for task in tasks:
    #     await task

start_time = time.time()
asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
end_time = time.time()
total_time = end_time - start_time
print("总共用时：", total_time, "秒")
