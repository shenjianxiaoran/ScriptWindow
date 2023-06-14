import requests
from bs4 import BeautifulSoup
import time

def main():
    url = 'https://movie.douban.com/cinema/later/beijing/'
    init_page = requests.get(url).content
    print(init_page)
    init_soup =  BeautifulSoup(init_page, 'lxml') 

    all_movies = init_soup.find('div', id="showing-soon")
    print(all_movies)
    for each_movie in all_movies.find_all('div', class_='item'):
        all_a_tag = each_movie.find_all('a')
        all_li_tag = each_movie.find_all('li')

        movie_name = all_a_tag[1].text
        url_to_fetch = all_a_tag[1]['href']
        movie_date = all_li_tag[0].text

        response_item = requests.get(url_to_fetch).content
        soup_item = BeautifulSoup(response_item, 'lxml')
        img_tag = soup_item.find('img')
        print(f"{movie_name} {movie_date} {img_tag['src']}")

start_time = time.time()
main()
end_time = time.time()
total_time = end_time - start_time
print("总共用时：", total_time, "秒")