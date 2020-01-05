# -*- coding: utf-8 -*-
from locale import *
import sys,os

project_dir = '../../tr/tr/'

sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import django
django.setup()

import soundcloud
from music.models import *
from datetime import datetime, date, time


client = soundcloud.Client(client_id='dce5652caa1b66331903493735ddd64d')
page_size = 200
genres_list = SounGenres.objects.values('name')
genres_list_names = [name['name'] for name in genres_list]
a_rus_list = [
'Агата Кристи',
'Аквариум',
'А-Лексий',
'А-мега and Блестящие',
'А-Студио',
'А.Р.М.И.Я',
'А.Т & Диана Видякина',
'Абдулкарим Каримов',
'Абир Касенов',
'АБРОSIM',
'Абсамат Абсаматов',
'Авейра',
'Авет Маркарян',
'Авиатор',
'Авраам Руссо',
'Автобус',
'Агата Кристи',
'Агент Смит',
'АгузароваЖанна',
'Агутин Леонид',
'Ада Якушева',
'Адам Риф',
'Адаптация',
'Адвайта',
'Аддис Абеба',
'Аделина Шарипова',
'Аделя Изтелеуова',
'Адильхан Бамматказиев',
'Адис Бек',
'Адлер Коцба',
'Адрей Царь',
'Адреналин',
'АЖУР',
'Азам Азизов',
'Азамат Биштов',
'Азамат Исенгазин',
'Азат Аветян',
'Азбука Хит',
'Азиза',
'Аида Ведищева',
'Аида Евдокимова',
'Аида Николайчук',
'Ай-Q',
'Ай-Ман',
'Айва',
'Айдамир Мугу',
'Айдамир Эльдаров',
'Айжан',
'Айки Душевный',
'Musique',
'Айкью',
'Айла (i-La)',
'Айлин',
'Айна Вильберг',
'Айрэн',
'Академия',
'Аквамарин',
'Аквариум',
'Акела',
'Аким',
'Акула',
'Алабама',
'Алан Музаев',
'Алан Черкасов',
'Алгоритм',
'Алевтина',
'Алевтина Бердникова',
'Алекс Балыков',
'Алекс Блинов',
'Алекс Гришин',
'Алекс Индиго',
'Алекс Малиновский',
'Алекc Тумм',
'Алекс Ческис',
'Алекс Юлдашев',
'Алекса Астер',
'Алекса Пол',
'Александр Dei-Russ',
'Александр Абдулов',
'Александр Айвазов',
'Александр Альтергот',
'Александр Андрианов',
'Александр Антонов',
'Александр Асташенок',
'Александр Бабенко',
'Александр Бакин',
'Александр Балбус',
'Александр Балыков',
'Александр Барыкин',
'Александр Бахтеев',
'Александр Белов',
'Александр Березиков',
'Александр Бешеный',
'Александр Блик',
'Александр Боборыкин',
'Александр Бон',
'Александр Борисов',
'Александр Буйнов',
'Александр Буйнов & Сергей Коньков',
'Александр Вервайн',
'Александр Вертинский',
'Александр Вестов',
'Александр Ворошило',
'Александр Галич',
'Александр Головин',
'Александр Городницкий',
'Александр Гудков',
'Александр Гужов',
'Александр Гужов и Николай Зайцев'
'Александр Дадали',
'Александр Дамаскин',
'Александр Данцевич',
'Александр Демидов и Би-2',
'Александр Денисов',
'Александр Деринг',
'Александр Добронравов',
'Александр Добрынин',
'Александр Дольский',
'Александр Доля',
'Александр Дулов',
'Александр Думлер',
'Александр Дюмин',
'Александр Евграфов',
'Александр Егоров',
'Александр Еловских',
'Александр Еловских & Маргарита Позоян',
'Александр Ермолов',
'Александр Жвакин',
'Александр Забазный',
'Александр Звинцов',
'Александр Звинцов и Виталий Гордей',
'Александр и Елена Альтергот',
'Александр и Устинья Малинины',
'Александр Иванов',
'Александр Казак',
'Александр Казанцев (Сотник)',
'Александр Кальянов',
'Александр Кварта',
'Александр Келеберда',
'Александр Киреев',
'Александр Кирсс',
'Александр Киршанов',
'Александр Климм',
'Александр Кнут',
'Александр Коган',
'Александр Коновалов',
'Александр Константинов',
'Александр Корецкий',
'Александр Королёв',
'Александр Кравцов',
'Александр Кривошапко',
'Александр Куданов',
'Александр Кузнецов',
'Александр Кулаев',
'Александр Куликов',
'Александр Куликов (Группа А-рай)',
'Александр Курган',
'Александр Курган и Саша Сирень',
'Александр Курилов',
'Александр Кутиков',
'Александр Кэтлин',
'Александр Леньков',
'Александр Леонидов',
'Александр Лир',
'Александр Литвинов',
'Александр Ломинский',
'Александр Ломинский & Афина',
'Александр Ломинский & Любовь Шепилова',
'Александр Ломинский и Алена Водонаева',
'Александр Ломинский и Татьяна Буланова',
'Александр Ломия (Jambazi)',
'Александр Ломия (Jambazi) & Aragvi Project',
'Александр Малинин',
'Александр Мамошин',
'Александр Марцинкевич',
'Александр Маршал',
'Александр Матвеев',
'Александр Милкин',
'Александр Мирский',
'Александр Назаров',
'Александр Нефедов',
'Александр Новгородцев',
'Александр Новиков',
'Александр Овчаренко',
'Александр Олешко',
'Александр Павлик',
'Александр Павлик и Лидия Скорубская',
'Александр Пенкин',
'Александр Побединский',
'Александр Подболотов',
'Александр Поддубный',
'Александр Пушной',
'Александр Разгуляев',
'Александр Розенбаум',
'Александр Рубан',
'Александр Рыбак',
'Александр Савинов',
'Александр Савченко',
'Александр Самсон',
'Александр Свириденко',
'Александр Сергеев',
'Александр Серов',
'Александр Сизов',
'Александр Скворцов',
'Александр Солодуха',
'Александр Сотник',
'Александр Суханов',
'Александр Сыров',
'Александр Тайчер',
'Александр Талин',
'Александр Тищенко',
'Александр Ткаченко',
'Александр Туралин',
'Александр Тюрин',
'Александр Ф. Скляр',
'Александр Федорков',
'Александр Филин',
'Александр Хамуев',
'Александр Хвыля',
'Александр Хочинский',
'Александр Черкасов',
'Александр Чусовитин',
'Александр Шапиро',
'Александр Шахов',
'Александр Шевченко',
'Александр Шоуа',
'Александр Шустерман',
'Александр Щиголев',
'Александр Юрпалов',
'Александр Ягья',
'Александр Яковлев',
'Александр Яременко',
'Александр Яшин',
'Александра Абрамейцева',
'Александра Белякова',
'Александра Белякова & Александр Панайотов',
'Александра Бозон',
'Александра Воробьева',
'Александра Дядюн',
'Александра Муканова',
'Александра Павлюк',
'Александра Савельева',
'Александра Серёжникова',
'Александра Скородумова',
'Алексей Башкиров',
'Алексей Белов',
'Алексей Белов и Ольга Кормухина',
'Алексей Большой',
'Алексей Большой и RiffMaster',
'Алексей Босота',
'Алексей Брытков (АлЁшка)',
'Алексей Брянцев',
'Алексей Брянцев и Елена Касьянова',
'Алексей Булыженский',
'Алексей Воробьев',
'Алексей Глызин',
'Алексей Гоман',
'Алексей Гоман И Naomi',
'Алексей Гонт',
'Алексей Данькин',
'Алексей Двин',
'Алексей Дидуров',
'Алексей Елистратов',
'Алексей Кабанов',
'Алексей Калдышкин',
'Алексей Князев',
'Алексей Корзин',
'Алексей Коробейников',
'Алексей Кубин',
'Алексей Кудрявцев',
'Алексей Куимов',
'Алексей Кумшатский',
'Алексей Леджер',
'Алексей Лосихин',
'Алексей Малахов',
'Алексей Матиас',
'Алексей Матов',
'Алексей Новиков',
'Алексей Ордынский',
'Алексей Плотников',
'Алексей Пономарев',
'Алексей Потехин',
'Алексей Раджабов',
'Алексей Раздобудько',
'Алексей Романюта',
'Алексей Рыбников',
'Алексей Рябоволик',
'Алексей Сагаловский',
'Алексей Сапрыкин',
'Алексей Семиврагов',
'Алексей Созонов',
'Алексей Стёпин',
'Алексей Стефанов',
'Алексей Сулима',
'Алексей Тамразов',
'Алексей Тэн',
'Алексей Фёдоров',
'Алексей Хворостян',
'Алексей Хлестов',
'Алексей Черфас',
'Алексей Чумаков',
'Алексей Шедько',
'Алексин',
'Алексин и Оксана Почепа',
'Алексия',
'Ален Самыкенов',
'Ален Сафарян',
'Алёна Roxis',
'Алена Андерс',
'Алёна Апина',
'Алёна Апина feat. DJ Vini',
'Алёна Бурхат',
'Алёна Валенсия',
'Алена Васильева',
'Алена Винницкая',
'Алена Водонаева и GуссиЛебеди',
'Алёна Высотская',
'Алёна Высоцкая',
'Алёна Герасимова',
'Алёна Герасимова (Макаровна)',
'Алёна Денисова',
'Алёна Жданова',
'Алёна Корольчук',
'Алёна Кошкина',
'Алена Кравец',
'Алёна Кухарёнок',
'Алена Ланская',
'Алёна Мальцева и Ярмарка',
'Алена Маринина',
'Алёна Мордяхина',
'Алена Осадчая',
'Алена Павленко',
'Алена Пак',
'Алёна Петровская',
'Алёна Рай и Денис Яковлев',
'Алёна Райс',
'Алена Свиридова',
'Алена Свиридова & Олеся Халме',
'Алёна Свиридова feat. Фёдор Фомин',
'Алёна Скок',
'Алена Уколова',
'Алёна Шарапова',
'Алёна Швец',
'Алёна, Ася И Чехов',
'Алеся',
'Алеся Боярских',
'Алеся Висич',
'Алеся Жинь и Сергей Смирный',
'Алеся Кирпа',
'Алеся Муха',
'Алехно Руслан',
'Алёша Пальцев',
'Алиана Устиненко',
'Алибек Саликов & Дмитрий Романов',
'Алиби',
'Алик Бендерский',
'Алик Довлатбекян',
'Алик Кумык',
'Алик Майт',
'Алим Зульпикаров',
'Алим Тайга feat. Hamwake',
'Алина',
'Алина Артц',
'Алина Астровская',
'Алина Башкина',
'Алина Верипя',
'Алина Виардо',
'Алина Высоцкая',
'Алина Грин',
'Алина Гросу',
'Алина Делисс',
'Алина Дубинина',
'Алина Захарова',
'Алина Кабаева',
'Алина Колтышева',
'Алина Крочева',
'Алина Палий',
'Алина Ромашкина',
'Алина Ростовская',
'Алина Ян',
'Алира',
'Алиса',
'Алиса Агамалова',
'Алиса В Стране Чудес',
'Алиса Вокс',
'Алиса Вокс & Феликс Бондарев',
'Алиса Данелия',
'Алиса Кожикина',
'Алиса Кожикина и Кирилл Скрипник',
'Алиса Милош',
'Алиса Мон',
'Алиса Мон & Константин Бубнов',
'Алиса Савинская',
'Алиса Салтыкова',
'Алиса Супронова',
'Алиса Франка',
'Алиса Фрейндлих',
'Алисия',
'Алисия & Master Spensor',
'Алисия & Влад Корса',
'Алисия & Павел Есенин и Hi-Fi',
'Алиш',
'Алла Баянова',
'Алла Горбачёва',
'Алла Дин',
'Алла Земскова',
'Алла Канти',
'Алла Костина feat. Total',
'Алла Медведева',
'Алла Нестерова',
'Алла Попова',
'Алла Пугачёва',
'Алладин',
'Аллан Камилов',
'Алмас Багратиони',
'Алмас Бекботаев feat. Slimz',
'АлоэВера',
'АлСми',
'Алсу',
'Алтайский',
'Аль Хоон',
'Альберт Асадуллин',
'Альберт Ибраев',
'Альберт Комаров',
'Альберт Салтыков',
'Альберт Салтыков и Виталий Котиц',
'Альберт Элоян',
'Альбина',
'Альбина Джанабаева',
'Альфа',
'Альяна feat. J-Vince & JDVX',
'Аля Гарсиа',
'Аля Кудряшева',
'Аля Райтер feat. Nebesno',
'Аматори',
'Амаяк Багдасарян',
'Амбери',
'Амега',
'Амели На Мели',
'Амид Салимов',
'Амилио',
'Амир Гильдерман',
'Ананасик',
'Анар feat. Алиса Мон',
'Анастасия',
'Анастасия Алентьева',
'Анастасия Анисимова',
'Анастасия Бородина',
'Анастасия Брухтий',
'Анастасия Варнавская',
'Анастасия Винникова',
'Анастасия Волочкова',
'Анастасия Главатских',
'Анастасия Гладилина',
'Анастасия Гончар',
'Анастасия Гринина',
'Анастасия Зудова',
'Анастасия и Валерий Желенок',
'Анастасия Карпова',
'Анастасия Ковалева',
'Анастасия Кожевникова',
'Анастасия Коновалова',
'Анастасия Мандрыкина',
'Анастасия Морозова',
'Анастасия Некрасова',
'Анастасия Петрик',
'Анастасия Приходько',
'Анастасия Приходько и Давид Каландадзе',
'Анастасия Ричманд',
'Анастасия Рэй',
'Анастасия Сандрова',
'Анастасия Сисаури',
'Анастасия Спиридонова',
'Анастасия Стоцкая',
'Анастасия Стоцкая и Николай Задерей',
'Анастасия Тиханович',
'Анастасия Трианна',
'Анастасия Царькова',
'Анастасия Чагина',
'Анастасия Шевченко',
'Анатолий Беляев',
'Анатолий Вишняков',
'Анатолий Волков',
'Анатолий Жих',
'Анатолий Загот',
'Анатолий Киреев',
'Анатолий Корж',
'Анатолий Могилевский',
'Анатолий Мякушкин',
'Анатолий Мякушкин и Татьяна Чубарова',
'Анатолий Писарев',
'Анатолий Полотно',
'Анатолий Тукиш',
'Анатолий Ушанов',
'Ангел А',
'Ангелина Власова',
'Ангелина Завальская',
'Ангелина Завальская & Gladushevskyy',
'Ангелина Каплан',
'Ангелина Рай',
'Ангелина Сергеева',
'Ангелина Шалимова',
'Ангелина Шикова',
'АнгелиЯ',
'Ангелы и Демоны',
'Ангина',
'Андей Забродин',
'Андреи? Али',
'Андрей Kosh',
'Андрей Авдеев',
'Андрей Адаричев',
'Андрей Андреев',
'Андрей Арзуманян',
'Андрей Арсентьев feat. Лев Тимашов',
'Андрей Артемьев',
'Андрей Бандера',
'Андрей Батт',
'Андрей Бельгиец',
'Андрей Бирюков',
'Андрей Бирюков & Аделя Изтелеуова',
'Андрей Бойко',
'Андрей Бородин',
'Андрей Бриг',
'Андрей Брукс',
'Андрей Вайсман',
'Андрей Васильев',
'Андрей Вертузaев',
'Андрей Вертузаев',
'Андрей Весенин',
'Андрей Ветер',
'Андрей Витвитский',
'Андрей Волянский',
'Андрей Вранской',
'Андрей Гамбург',
'Андрей Гражданкин',
'Андрей Григорьев',
'Андрей Гризли',
'Андрей Губин',
'Андрей Державин',
'Андрей Детистов',
'Андрей Драгунов',
'Андрей Дубов',
'Андрей Дубровин',
'Андрей Евсеев',
'Андрей Егоров',
'Андрей Жарков',
'Андрей Забродин',
'Андрей Запал',
'Андрей Иванцов',
'Андрей Иголкин',
'Андрей Иноземцев',
'Андрей Калинин',
'Андрей Карат',
'Андрей Карат и Елена Тишкова',
'Андрей Каргин',
'Андрей Карельский',
'Андрей Картавцев (ВерсиА)',
'Андрей Керченский',
'Андрей Климнюк',
'Андрей Князь',
'Андрей Ковалев',
'Андрей Ковалев и Любаша',
'Андрей Ковалёв и Юлия Митюнина',
'Андрей Козловский',
'Андрей Копылов',
'Андрей Кравченко',
'Андрей Ксешинский',
'Андрей Курбатов',
'Андрей Леницкий',
'Андрей Лиранов',
'Андрей Макаревич',
'Андрей Мамаев',
'Андрей Манухин',
'Андрей Мисин',
'Андрей Морган',
'Андрей Наволоцкий',
'Андрей Никольский',
'Андрей Ноткин',
'Андрей Опейкин',
'Андрей Орельский',
'Андрей Острякоff',
'Андрей Павлович',
'Андрей Поливцев',
'Андрей Приклонский',
'Андрей Резников',
'Андрей Рогаткин',
'Андрей Романов',
'Андрей Ростов',
'Андрей Рубежов',
'Андрей Рыбаков',
'Андрей Спасенников',
'Андрей Стрелков',
'Андрей Таныч',
'Андрей Тарасов',
'Андрей Тихонов',
'Андрей Токарев',
'Андрей Томин',
'Андрей Усманов',
'Андрей Храмов',
'Андрей Черных',
'Андрей Широков',
'Андрей Шпехт',
'Андрей Яблонев',
'Андрей Язвинский',
'Андрей Язвинский и Наталья Язвинская',
'Андрей Якиманский',
'Андрей Янкин',
'Андрій Князь',
'Андрій Лемішка & Ярина Романів',
'Андрій Лучан',
'Андрій Хливнюк і Джамала',
'Анет Сай',
'Анжелика',
'Анжелика Агурбаш',
'Анжелика Ахмедова',
'Анжелика  Варум',
'Анжелика Галь',
'Анжелика Начесова',
'Анжелика Пушнова',
'Анжелика Рута',
'Анжелика Саурская',
'Анжелика Султанова',
'Анжелика Ютт',
'Ани Варданян',
'Ани Лорак',
'Аника',
'Аника Далински',
'Анилла',
'АнимациЯ',
'Анита Цой',
'Анна Антоник',
'Анна Артеменко',
'Анна Барабошина',
'Анна Белкина',
'Анна Бершадская',
'Анна Боронина',
'Анна Бэйс',
'Анна Власова',
'Анна Волошина',
'Анна Ворфоломеева',
'Анна Галкина',
'Анна Герман',
'Анна Грачевская',
'Анна Гуричева',
'Анна Диди',
'Анна Добрыднева',
'Анна Дуванова',
'Анна Завальская',
'Анна Калашникова',
'Анна Козырь',
'Анна Кольцова',
'Анна Корнильева',
'Анна Кришталь',
'Анна Леонова',
'Анна Маковецкая',
'Анна Малышева и Мята',
'Анна Марти',
'Анна Морс',
'Анна Плетнёва',
'Анна Резникова',
'Анна Ричч',
'Анна Ряпасова',
'Анна Савва',
'Анна Седакова',
'Анна Седокова',
'Анна Семенович',
'Анна Сингаевская',
'Анна Стассия',
'Анна Твердоступ',
'Анна Темнякова',
'Анна Тинс',
'Анна Уайборн',
'Анна Филипчук',
'Анна Шаркунова',
'Анна Швец',
'Анна Шульгина',
'Анна Якубук',
'Анна Ярчинская',
'Анна-Мария',
'Анне Вески',
'Аннет & Bizaro',
'Анора',
'Ансамбль Дружба',
'Ансамбль Им. А. Александрова',
'АнтипА',
'Антитела',
'Антон Азаров',
'Антон Балков',
'Антон Беляев',
'Антон Вирта',
'Антон Данюшин',
'Антон Зацепин',
'Антон Климик',
'Антон Лаврентьев',
'Антон Макарский',
'Антон Небо',
'Антон Новицкий',
'Антон Ньюмарк',
'Антон Рикс',
'Антон Семенов',
'Антон Степанов',
'Антон Широков',
'Антонина Громова',
'Антонио Вивальди',
'Антоха Копоть',
'Ануш',
'Анфиса Чехова',
'Анюта Ильина',
'Анюта Славская',
'Аня Воробей',
'Аня Добрыднева',
'Аня Жулина',
'Аня Мун',
'Аня Нилова',
'Аня Руднева',
'Аня Стрекоза',
'Аня Ткаченко',
'Аня Шаркунова',
'Аня Эйтманн',
'Апм',
'Аполлинария',
'Апп Краснознаменного Округа',
'Ара Мартиросян',
'Арам Хачатурян',
'Арамис',
'Арбат New',
'Арвид',
'Аревик Багдасарян и T-Killah',
'Ариадна',
'Ариана',
'Арина Бережная',
'Арина Войт',
'Арина Данилова',
'Арина Данилова feat. HARU',
'Арина Домски',
'Арина и Размер Project',
'Арина Эймер',
'Аритмия',
'Ария',
'Аркадиас',
'Аркадий Войтюк',
'Аркадий Грек',
'Аркадий Дар',
'Аркадий Духин',
'Аркадий Кобяков',
'Аркадий Северный',
'Аркадий Стародубцев',
'Аркадий Хоралов',
'Аркан',
'Арктида',
'Арлин',
'Арман Алматинский',
'Арсен Акопян',
'Арсен Гитинов',
'Арсен Мирзоян',
'Арсен Шавлюк',
'Арсений Бородин',
'Арсений Лавкут',
'Арманта',
'АрматА',
'Армен Багдасарян',
'Армен Захарян',
'Армия',
'Арсен Акопян',
'Арсен Гитинов',
'Арсен Шавлюк',
'Арсений Бородин',
'Арсений Лавкут',
'Артем Артемьев',
'Артем Баринов',
'Артем Бизин',
'Артём Будзинский',
'Артем Грачёв',
'Артём Душевный',
'Артем Еременко',
'Артем Иванов'
'Артем Каменский',
'Артем Качер',
'Артем Кинг',
'Артем Кондратюк',
'Артём Коржуков',
'Артем Лоик',
'Артем Мех',
'Артем Михаленко',
'Артём Неизвестный',
'Артём Нечипоренко',
'Артём Никитин',
'Артем Орлов',
'Артём Пивоваров',
'Артём Попов',
'Артём Симонов',
'Артём Сорока',
'Артём Татищевский',
'Артём Туркин',
'Артем Угловский',
'Артём Угляров',
'Артём Укропов',
'Артем Шалимов',
'Артерия',
'Артур feat. Сабрина',
'Артур Алибердов',
'Артур Аржаков',
'Артур Боссо',
'Артур Бэст',
'Артур Вишенков',
'Артур Геладов',
'Артур Железняк',
'Артур Иванов',
'Артур Капишев',
'Артур Карецкий',
'Артур Кусимов',
'Артур Лабор',
'Артур Манташев feat. Samoel',
'Артур Ратнер',
'Артур Толепов',
'Артур Толмасов',
'Артур Тринёв',
'Артур Урванцев',
'Артур Халатов',
'Артур Эйзен',
'Артуро Сафин & Dramma',
'АСер feat. Даша Явуз',
'Асия',
'Аскер Седой',
'Аслан',
'Аслан Гусейнов',
'Аслан и Марина',
'Аслан Кятов',
'Аслан Махов',
'АССА',
'Ассаи',
'Ассаи feat. Иван Дорн',
'Ассия Ахат',
'Ассоль feat. Artik',
'Ассорти',
'Ассорти & Евгений Анишко',
'Астемир',
'Астемир Апанасов',
'Асферикс',
'Асхат',
'Ася Желнова',
'Ася Пивоварова',
'Ася Тлекова',
'Атаманка',
'Атмосфера',
'Атома DBR',
'Атри',
'Аукцыон',
'Аура',
'Аферистки',
'Афина',
'Афродита',
'Аффекты',
'Аффинаж',
'Ах, водевиль водевиль',
'Ахи-Вздохи',
'Ахлям Газалиев',
'Ахонькоvа',
'Аш',
]

litera = SoundSymbol.objects.get(name="А")

count = 0
all_track_playlist = SoundList.objects.get(id=2)

for tag in a_rus_list:
    tracks = client.get('/tracks', q=tag, limit=page_size, linked_partitioning=1)
    if tracks:
        for track in tracks.collection:
            created_at = track.created_at
            created_at = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
            try:
                SoundParsing.objects.get(id=track.id)
            except:
                try:
                    self_tag = SoundTagsList.objects.get(name=tag, symbol=litera)
                except:
                    self_tag = SoundTagsList.objects.create(name=tag, symbol=litera)
                if track.genre and track.release_year and track.duration > 90000 and track.genre in genres_list_names:
                    genre =SounGenres.objects.get(name=track.genre.replace("'", '') )
                    new_track = SoundParsing.objects.create(id=track.id, tag=self_tag, artwork_url=track.artwork_url, created_at=created_at, duration=track.duration, genre=genre, stream_url=track.stream_url, title=track.title, uri=track.uri, release_year=track.release_year)
                    all_track_playlist.track.add(new_track)
                count = count + 1
        while tracks.next_href != None and count < 1000:
            tracks = client.get(tracks.next_href, limit=page_size, linked_partitioning=1)
            for track in tracks.collection:
                created_at = track.created_at
                created_at = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
                try:
                    SoundParsing.objects.get(id=track.id)
                except:
                    self_tag = SoundTags.objects.get(name=tag, symbol=litera)
                    if track.genre and track.release_year and track.duration > 90000 and track.genre in genres_list_names:
                        genre =SounGenres.objects.get(name=track.genre.replace("'", '') )
                        new_track = SoundParsing.objects.create(id=track.id, tag=self_tag, artwork_url=track.artwork_url, created_at=created_at, duration=track.duration, genre=genre, stream_url=track.stream_url, title=track.title, uri=track.uri, release_year=track.release_year)
                        all_track_playlist.track.add(new_track)
                    count = count + 1
