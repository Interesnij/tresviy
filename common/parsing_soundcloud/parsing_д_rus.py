
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

д_rus_list_1 = [
"Д Артаньян и три мушкетёра",
"Д503",
"Давид Бинтсене и Витя Исаев",
"Давинчи (The Davincies)",
"Дадаш & H1GH",
"Дайвер",
"Дайкири",
"ДаКи",
"Дакота",
"Дале feat. Katya Tu",
"Дали",
"Дальний Свет",
"Дамбо",
"Дан Розин",
"Дана Борисова",
"Дана Релли",
"Дана Соколова",
"Даниил Блёскин feat. Pompey",
"Даниил Данилевский",
"Даниил Иванов",
"Даниил Орловский",
"Даниил Рувинский",
"Даниил Сири feat. Зомб",
"Даниил Сорокин",
"Данил Бойко",
"Данил Брест (Кудрянов)",
"Данил Буранов",
"Данила Краснов",
"Даниэль Гарунов",
"Данко",
"Дантес",
"Дантес и Олейник",
"Даня Nill",
"Даня Nill & Зомб",
"Даня Вайнер",
"Дари Черная",
"Дари Чёрная feat. Deels",
"Дарина Жудова",
"Дарина Иванова",
"Дарина Кройтор",
"Дарья Ануфриева",
"Дарья Бутарева",
"Дарья Гончарова",
"Дарья Кумпаньенко",
"Дарья Медовая",
"Дарья Покровская",
"Дарья Рассвет feat. Bengalsky",
"Дарья Шейк",
"Дарья Явуз",
"Дарья Ярцева",
"Дато",
"Даша Астафьева",
"Даша Баскакова",
"Даша Волосевич",
"Даша Данилова",
"Даша Дубовицкая",
"Даша Зеброва",
"Даша Клюкина",
"Даша Монас",
"Даша Русакова",
"Даша Столбова",
"Даша Суворова",
"Даша Судакова",
"Даша Шерман",
"Даша Шульц",
"Даяна",
"Два Океана",
"Дварняги",
"Две Столицы feat. Sal One",
"Две стороны одной медали",
"Двенадцать стульев",
"Двойной Коктейль",
"Двойной удар",
"Дворецкая",
"ДДТ",]

д_rus_list_2 = [
"Дебош",
"ДеЛайла",
"Дельфин",
"Демидыч",
"Демо",
"Демо & Love T",
"Ден Вильнер",
"Денис Kore",
"Денис Rasko",
"Денис RiDer",
"Денис Алборов",
"Денис Барканов",
"Денис Белик",
"Денис Жатвинский",
"Денис Клявер",
"Денис Копытов",
"Денис Косякин",
"Денис Кочержук",
"Денис Лирик",
"Денис Лис",
"Денис Любимов",
"Денис Майданов",
"Денис Мусаев",
"Денис Надёжин",
"Денис Океан",
"Денис Повалий",
"Денис Реконвальд",
"Денис Сарин",
"Денис Симуков",
"Денис Стрельцов",
"Денис Филимонов",
"Денис Шевченко",
"День Ангела",
"День Независимости (DN)",
"Дети Капитана Гранта",
"Дети Фристайла",
"Детская Студия Дельфин",
"Детский Хор",
"Децл",
"Джама",
"Джамала",
"Джамар",
"Джанго",
"Джани Радари",
"Джаникс",
"Джаникс и Олия",
"Джарахов",
"Джаро",
"Джастик",
"Джая Миядзаки",
"ДжеNифер",
"Джей Ди",
"Джей Мар",
"Джейн",
"Джейхун Пирвердиев",
"Джемма",
"Дженаро",
"Дженнет",
"Джентльмены удачи",
"ДЖЕТЭ",
"Джи Арт & DJ.Gor",
"Джи Вилкс",
"ДжиАш",
"ДжиБо feat. Лёша Свик & Oleg LeeReeK",
"Джиган",
"Джиган (Geegun)",
"Джизус",
"Джим aka Pello & Dizzy, Вадим Свой",
"Джино",
"Джинсовые Мальчики",
"Джиос",
"Джоззиo",
"Джокеры",
"Джокеры feat. Ost1n",
"Джон Сергей Тихоненко",]

д_rus_list_3 = [
"ДжониДжейн",
"Джонни C4",
"Джонни Фунт",
"Джоя",
"Дзідзьо",
"Ди-Бронкс",
"Ди-Кей",
"ДИF feat. Call Of Beat",
"Диана",
"Диана Громова",
"Диана Гурцкая",
"Диана Даре",
"Диана Завидова",
"Диана Норден",
"Диана Прошкина",
"Диана Сладкая",
"Диана Тагиева",
"Диана Тайманова",
"Диана Хитарова",
"Диана Шарапова",
"Диана Шимановская",
"Дибир Абаев",
"Диверсанты",
"ДиВойс",
"Дигори Кёрк",
"Диджей Жиро",
"Дидо",
"Дидо Каримов",
"Дидюля",
"Дилайс",
"Дилара Рафаэлли",
"Дилемма",
"Дилеон",
"Дилижанс",
"Дилэй",
"Диля Даль",
"Дима Prosto",
"Дима Адаев",
"Дима Бикбаев",
"Дима Билан",
"Дима Бриз",
"Дима Бушмелев",
"Дима Вебер",
"Дима Власкин",
"Дима Воронежский",
"Дима Горичев",
"Дима Дембицкий",
"Дима Догма",
"Дима Жгучий",
"Дима Каднай",
"Дима Казанский",
"Дима Каминский",
"Дима Карташов",
"Дима Квант feat. Акайс",
"Дима Климашенко и Саша Рей",
"Дима Коляденко",
"Дима Корсо",
"Дима Кузьмин",
"Дима Лорен",
"Дима Масюченко feat. Энвер Каримов",
"Дима Миленин",
"Дима Мирон",
"Дима Монатик",
"Дима Никонович",
"Дима Скалозубов",
"Дима Татами",
"Дима Тихонов",
"Дима Уникал",
"Дина Гарипова",
"Дина Грехова & Eugene Star",
"Динама",
"Динамик",
"Динамит",
"Динара Harley",
"ДинаЯ",]

д_rus_list_4 = [
"Диня Фарт",
"ДиО.Фильмы",
"Дипсай",
"Дисайд",
"Дискомафия",
"Дискотека Авария",
"Дискотека Гараж",
"Діля feat. Астарта",
"Дмитриев Михаил",
"Дмитрий Андреев",
"Дмитрий Андриец",
"Дмитрий Бикбаев",
"Дмитрий Быковский",
"Дмитрий Вешнев",
"Дмитрий Геттс",
"Дмитрий Голубев",
"Дмитрий Дан",
"Дмитрий Данилин",
"Дмитрий Донской",
"Дмитрий Дюмин",
"Дмитрий Ермак & Наталия Быстрова",
"Дмитрий Казанцев",
"Дмитрий Калугин",
"Дмитрий Каминский",
"Дмитрий Каннуников",
"Дмитрий Касаткин",
"Дмитрий Климашенко",
"Дмитрий Колдун",
"Дмитрий Колобов",
"Дмитрий Константинов",
"Дмитрий Королёв",
"Дмитрий Король",
"Дмитрий Кохановский",
"Дмитрий Кубасов",
"Дмитрий Курилов",
"Дмитрий Логинов",
"Дмитрий Маликов",
"Дмитрий Митин",
"Дмитрий Недоспелов",
"Дмитрий Несветайло",
"Дмитрий Нестеров",
"Дмитрий Осипов",
"Дмитрий Первушин",
"Дмитрий Полторацкий",
"Дмитрий Попов",
"Дмитрий Прасковин",
"Дмитрий Прасковьин",
"Дмитрий Прянов",
"Дмитрий Родонов",
"Дмитрий Романов",
"Дмитрий Ромм",
"Дмитрий Соловей",
"Дмитрий Соснин",
"Дмитрий Стрельцов feat. Екатерина Петрова",
"Дмитрий Сулей",
"Дмитрий Суслов",
"Дмитрий Сысоев",
"Дмитрий Тарасов",
"Дмитрий Тищенко feat. Наташа Турбина",
"Дмитрий Треликовский",
"Дмитрий Фомин",
"Дмитрий Харатьян",
"Дмитрий Хворостовский",
"Дмитрий Хмелёв",
"Дмитрий Шестаков",
"Дмитрий Юрич",
"Дмитро Камінський",
"Дмитро Шуров",
"До Минор",
"Доберман",
"Добрые Молодцы",
"Добрый Дми feat. Bachu",
"Добрый Шубинъ",
"Доза Радости",
"Доктор Александров",]

д_rus_list_5 = [
"Доктор Ватсон",
"Доминик Джокер",
"Доминика",
"Дорогая Моя Столица",
"Достояние республики",
"Достучаться До Небес",
"Драгни",
"Дракон Пита",
"Дракоша Тоша",
"Дракула",
"Дрей Сонгз",
"Дроби",
"Дрозды",
"Друга Ріка",
"Другая Погода",
"Другие правила",
"ДрузьЯ",
"Дунаевский Orchestra",
"Душа",
"Дуэнья",
"Дуэт L",
"Дуэт Алмас",
"Дуэт Золото",
"Дуэт Лето",
"Дуэт Не Уходи",
"Дуэт Пара Лель",
"Дуэт Полвторого (Алексей Хомчик, Юрий Лобиков)",
"Дуэт Учитель Танцев",
"Дуэт Эскиз",
"Дэвид Бэк",
"Дэн Дэмкив",
"Дэн Ясюк",
"Дэя",
"Дюна",
"Дядя Ru",
"Дядя Жора",
"ДяДя Потап",
]



litera = SoundSymbol.objects.get(name="Д")

count = 0

for tag in д_rus_list_1:
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
