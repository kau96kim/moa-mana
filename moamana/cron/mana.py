from api.mana.models import Mana
from multiprocessing import Pool
from bs4 import BeautifulSoup
from api.models import Url
import itertools
import requests


url = Url.objects.get(id=1).link


def get_page_list():
    req = requests.get(f"{url}/bbs/page.php?hid=manga_list")
    soup = BeautifulSoup(req.content, 'html.parser')

    last_page = soup.find("i", class_="fa-angle-double-right").parent['href']
    last_page = int(last_page[last_page.index("(")+1:last_page.index(")")]) + 1
    page_list = list(range(0, last_page))

    return page_list


def get_mana_list(page):
    mana_list = []

    req = requests.get(f"{url}/bbs/page.php?hid=manga_list&page={page}")
    soup = BeautifulSoup(req.content, 'html.parser')
    manas = soup.select("div.manga-subject > a")

    for mana in manas:
        link = mana['href']
        title = mana.text.replace("\n", "").replace("\t", "")
        mana_list.append({'title': title, 'link': link})

    return mana_list


def post_mana_list():
    try:
        pool = Pool(processes=8)

        title_list = pool.map(get_mana_list, get_page_list())
        mana_list = list(itertools.chain.from_iterable(title_list))

        for mana in mana_list:
            Mana(title=mana['title'], link=mana['link']).save()

    except Exception as e:
        print(e)


