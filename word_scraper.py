import requests
from bs4 import BeautifulSoup

# word_document = {
#     "_id": ...,
#     'name': ...,
#     'mtime': ..., # timestamp
#     'lang_code': ..., # EN, ZH, JP ...
#     'meanings': [
#         {
#             'pos': 'v.',     # parts of speach
#             'meaning': '...', 
#         }
#     ]
# }


def word_scraper(word):
    url = "https://cn.bing.com/dict/search?q=" + word#in situ" # + "&qs=n&form=Z9LH5&sp=-1&pq=" + str(
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")

    lis_soup = soup.select('div.qdef ul li')
    meanings = []
    for item in lis_soup:
        pos = item.select_one('span.pos').text
        meaning = item.select_one('span.b_regtxt span').text
        print('pos = {}'.format(pos))
        print('meanning = {}'.format(meaning))
        one_meaning = {
            'pos':pos,
            'meaning':meaning
        }
        meanings.append(one_meaning)

    print('meanings = {}'.format(meanings))
    return meanings


if __name__ == '__main__':
    try:
        word_scraper('topaz')
    except Exception as e:
        print('E = {}'.format(e))
