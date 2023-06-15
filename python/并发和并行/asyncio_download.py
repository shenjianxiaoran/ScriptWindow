
import asyncio
import time
import aiohttp

async def download_one(url):
    async with aiohttp.ClientSession() as session:    # 创建session对象，可以在任何环境中使用。 这
        async with session.get(url) as resp:
            print('Read {} from {}'.format(resp.content_length, url))
    
async def download_all(sites):
    tasks = [asyncio.create_task(download_one(site)) for site in sites]
    await asyncio.gather(*tasks)


def main():
    sites = [
        'https://encyclopedia.thefreedictionary.com/wiki/Portal:Arts',
        'https://encyclopedia.thefreedictionary.com/wiki/Portal:History',
        'https://encyclopedia.thefreedictionary.com/wiki/Portal:Society',
        'https://encyclopedia.thefreedictionary.com/wiki/Portal:Biography',
        'https://encyclopedia.thefreedictionary.com/wiki/Portal:Mathematics',
        'https://encyclopedia.thefreedictionary.com/wiki/Portal:Technology',
        'https://encyclopedia.thefreedictionary.com/wiki/Portal:Geography',
        'https://encyclopedia.thefreedictionary.com/wiki/Portal:Science',
        'https://encyclopedia.thefreedictionary.com/wiki/Computer_science',
        'https://encyclopedia.thefreedictionary.com/wiki/Python_(programming_language)',
        'https://encyclopedia.thefreedictionary.com/wiki/Java_(programming_language)',
        'https://encyclopedia.thefreedictionary.com/wiki/PHP',
        'https://encyclopedia.thefreedictionary.com/wiki/Node.js',
        'https://encyclopedia.thefreedictionary.com/wiki/The_C_Programming_Language',
        'https://encyclopedia.thefreedictionary.com/wiki/Go_(programming_language)'
    ]
    start_time = time.perf_counter()
    # asyncio.run(download_all(sites))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(download_all(sites))
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))
    
if __name__ == '__main__':
    main()
