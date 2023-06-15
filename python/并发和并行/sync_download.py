
import requests
import time

def download_one(url):
    resp = requests.get(url)
    print('Read {} from {}'.format(len(resp.content), url))
    
def download_all(sites):
    for site in sites:
        download_one(site)

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
    download_all(sites)
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))
    
if __name__ == '__main__':
    main()
