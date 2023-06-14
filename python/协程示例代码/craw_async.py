import asyncio
import aiohttp
import time
from bs4 import BeautifulSoup

async def fetch_content(url):
    async with aiohttp.ClientSession(
        headers=header, connector=aiohttp.TCPConnector(ssl=False)
    ) as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    url = "https://movie.douban.com/cinema/later/beijing/"
    init_page = await fetch_content(url)
    print(init_page)
    init_soup =  BeautifulSoup(init_page, 'lxml') 

    movie_names, urls_to_fetch, movie_dates = [], [], []

    all_movies = init_soup.find('div', id="showing-soon")
    for each_movie in all_movies.find_all('div', class_='item'):
        all_a_tag = each_movie.find_all('a')
        all_li_tag = each_movie.find_all('li')

        movie_names.append(all_a_tag[1].text)
        urls_to_fetch.append(all_a_tag[1]['href'])
        movie_dates.append(all_li_tag[0].text)
    
    tasks = [fetch_content(url) for url in urls_to_fetch]
    pages = await asyncio.gather(*tasks) # pages = [page1, page2,...] 或 pages = await [fetch_content

    for movie_name, movie_date, page in zip(movie_names, movie_dates, pages):
        soup_item = BeautifulSoup(page, 'lxml')
        img_tag = soup_item.find('img')
        print(f"{movie_name} {movie_date} {img_tag['src']}")


start_time = time.time()
asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
end_time = time.time()
total_time = end_time - start_time
print("总共用时：", total_time, "秒")