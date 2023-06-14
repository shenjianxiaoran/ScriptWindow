
import time

def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    time.sleep(sleep_time)
    print('OK {}'.format(url))

def main(urls):
    for url in urls:
        crawl_page(url)

start_time = time.time()
main(['url_1', 'url_2', 'url_3', 'url_4'])
end_time = time.time()
total_time = end_time - start_time
print("总共用时：", total_time, "秒")

