from api.mana.models import Mana, Episode
from bs4 import BeautifulSoup
import requests


def post_episode_list():
    title = "다가시카시"

    mana = Mana.objects.filter(title=title).first()
    req = requests.get(mana.get_link())
    soup = BeautifulSoup(req.content, 'html.parser')

    episodes = soup.find("div", class_="chapter-list").find_all("a")
    episodes = list(reversed(episodes))

    order = Episode.objects.filter(mana=mana).order_by('-order').first()
    if order is None:
        order = 0
    else:
        order = order.order

    for episode in episodes:
        order += 1
        link = episode['href']
        episode_title = episode.find("div", class_="title").find(text=True, recursive=False)
        episode_title = episode_title.replace("\n", "").replace("\t", "").replace(title, title + " ")

        Episode(title=episode_title, link=link, order=order, status='X', mana=mana).save()
