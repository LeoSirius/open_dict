import requests
from bs4 import BeautifulSoup


def word_scraper(word):
    url = "https://cn.bing.com/dict/search?q=" + word
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")

    lis_soup = soup.select('div.qdef ul li')
    meanings = []
    for item in lis_soup:
        pos = item.select_one('span.pos').text
        meaning = item.select_one('span.b_regtxt span').text
        one_meaning = {
            'pos':pos,
            'meaning':meaning
        }
        meanings.append(one_meaning)

    return meanings


if __name__ == '__main__':
    try:
        word_scraper('topaz')
    except Exception as e:
        print('E = {}'.format(e))
