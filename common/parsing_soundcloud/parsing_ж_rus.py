
# -*- coding: utf-8 -*-
from locale import *
import sys,os

project_dir = '../tr/tr/'

sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import django
django.setup()

import soundcloud
from music.models import *
from datetime import datetime, date, time


client = soundcloud.Client(client_id='dce5652caa1b66331903493735ddd64d')
page_size = 200
genres_list = SoundGenres.objects.values('name')
genres_list_names = [name['name'] for name in genres_list]

ж_rus_list_1 = [
"Жак Энтони",
"Жаман (Восточный Округ)",
"Жамки feat. Руставели (Многоточие)",
"Жан & Rimsky",
"Жан & Rimsky feat. Kathy Soul",
"Жан Батист Люлли",
"Жанна Агузарова",
"Жанна Бичевcкая",
"Жанна Бичевская",
"Жанна Прохорихина",
"Жанна Рождественская",
"Жанна Фриске",
"Жанна Швец",
"Жара (Песочные Люди)",
"Жека (Григорьев Евгений)",
"Жека (Евгений Григорьев)",
"Жека Баянист",
"Жека и Светлана Питерская",
"Жека РАС ТУ (Кто ТАМ?)",
"Жека Соловей",
"Желтая Ветка",
"Жемчуг",
"Жемчужина",
"Женя Mad",
"Женя Python",
"Женя Reyn feat. Влад Крик",
"Женя Ангел",
"Женя Белоусов",]

ж_rus_list_2 = [
"Женя Бриз",
"Женя Вилль",
"Женя Вилль feat. Коля Крик",
"Женя Герасимчук",
"Женя Герасимчук и Дима Карташов",
"Женя Дэп",
"Женя Жакет",
"Женя Забытый & Вова Ванэс",
"Женя Индиго",
"Женя Ким",
"Женя Коннов",
"Женя Латышев",
"Женя Любич",
"Женя Максимова",
"Женя Малахова",
"Женя Мильковский",
"Женя Нева, Nekby, Валиум",
"Женя Отрадная",
"Женя Поликарпова",
"Женя Рэй",
"Женя Рябцева & Gurude",
"Женя Семёнов",
"Женя Толочный",
"Женя Тополь",
"Женя Фокин",
"Женя Шевченко",
"Женя Юдина",
"ЖеняNOrm",
"Жестокий романс",
"Жин-Жин",
"Жора Затонский",
"Жора Камский",
"Жорик Иванов",
"Жуки",
"Жулики",
"Журга",
]

litera = SoundSymbol.objects.get(name="Ж")

count = 0

for tag in ж_rus_list_1:
    tracks = client.get('/tracks', q=tag, limit=page_size, linked_partitioning=1)
    if tracks:
        for track in tracks.collection:
            created_at = track.created_at
            created_at = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
            try:
                SoundParsing.objects.get(id=track.id)
            except:
                if track.genre and track.release_year and track.duration > 90000 and track.genre in genres_list_names:
                    try:
                        self_tag = SoundTags.objects.get(name=tag, symbol=litera)
                    except:
                        self_tag = SoundTags.objects.create(name=tag, symbol=litera)
                    genre =SoundGenres.objects.get(name=track.genre.replace("'", '') )
                    new_track = SoundParsing.objects.create(id=track.id, tag=self_tag, artwork_url=track.artwork_url, created_at=created_at, duration=track.duration, genre=genre, stream_url=track.stream_url, title=track.title, uri=track.uri, release_year=track.release_year)
                count = count + 1
        while tracks.next_href != None and count < 2000:
            tracks = client.get(tracks.next_href, limit=page_size, linked_partitioning=1)
            for track in tracks.collection:
                created_at = track.created_at
                created_at = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
                try:
                    SoundParsing.objects.get(id=track.id)
                except:
                    if track.genre and track.release_year and track.duration > 90000 and track.genre in genres_list_names:
                        try:
                            self_tag = SoundTags.objects.get(name=tag, symbol=litera)
                        except:
                            self_tag = SoundTags.objects.create(name=tag, symbol=litera)
                        genre =SoundGenres.objects.get(name=track.genre.replace("'", '') )
                        new_track = SoundParsing.objects.create(id=track.id, tag=self_tag, artwork_url=track.artwork_url, created_at=created_at, duration=track.duration, genre=genre, stream_url=track.stream_url, title=track.title, uri=track.uri, release_year=track.release_year)
                    count = count + 1
