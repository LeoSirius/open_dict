import requests
from bs4 import BeautifulSoup

word = {
    'phonetic':[],
    'desc': [
        {
        'quality':'n',
        'means':['','', ...],
        }
    ]
}


def list_segs(soup):
    return soup.findAll('div', {'class':'each_seg'})

def get_quality(seg):
    quality_soup = seg.find('div', {'class': 'pos'})
    return quality_soup.get_text() if quality_soup else ''

def get_desc_list(seg):
    desc_list = seg.findAll('span', {'class': 'bil'})
    return [desc.get_text() for desc in desc_list]

def word_scraper(word):
    url = "https://cn.bing.com/dict/search?q=" + word#in situ" # + "&qs=n&form=Z9LH5&sp=-1&pq=" + str(
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")

    segs = list_segs(soup)  # each seg is a quality

    if not segs:
        print('no mean')

    word_desc_results = []
    for seg in segs:
        quality = get_quality(seg)
        desc_list = get_desc_list(seg)
        word_desc_result = {
            'quality': quality,
            'desc_list': desc_list,
        }
        word_desc_results.append(word_desc_result)
    print('word_desc_results = {}'.format(word_desc_results))
    return word_desc_results

    # print('li_pos ')

    # qualities = get_quality(li_pos)
    # print(qualities)
# voice:
# http://dict.youdao.com/dictvoice?audio=word

if __name__ == '__main__':
    try:
        word_scraper('hare')
    except Exception as e:
        print('E = {}'.format(e))





