#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys
import glob
import time
import csv
from PIL import Image

number_files = len(glob.glob1('.',"*.jpg"))
today = time.strftime("%Y-%m-%d")
time_now = time.strftime("%H:%M:%S")
size = 800, 600

term_list = {
    "Донстрой" : "10.1.255.5",
    "Остров мечты 4 эт" : "10.1.255.9",
    "ПЭК" : "10.1.255.10",
    "РосТех" : "10.1.255.12",
    "Замочек (неттоп)" : "10.1.255.13",
    "Офис" : "10.1.255.16",
    "Технополис" : "10.1.255.17",
    "РосЭлектроника" : "10.1.255.20",
    "Дом.рф 4 эт" : "10.1.255.22",
    "Дом.рф 5 эт" : "10.1.255.23",
    "Дом.рф Автозаводская" : "10.1.255.31",
    "Евразийский Банк" : "10.1.255.33",
    "Росэксим" : "10.1.255.38",
    "МатчПоинт 3й подъезд" : "10.1.255.42",
    "Технополис 1 эт." : "10.1.255.45",
    "Локомотив ЮГ2" : "10.1.255.47",
    "Просвещение, 5 этаж" : "10.1.255.49",
    "МатчПоинт 4й подъезд" : "10.1.255.52",
    "Транслом" : "10.1.255.53",
    "Кушман" : "10.1.255.54",
    "МПО Румянцева" : "10.1.255.55",
    "Про Город" : "10.1.255.56",
    "RussiaToday_1 (лестница)" : "10.1.255.57",
    "RussiaToday_2" : "10.1.255.58",
    "БЦ Матрешки" : "10.1.255.61",
    "Учебный центр ВЭБ.РФ" : "10.1.255.64",
    "ЖК Октябрьское поле 30" : "10.1.255.69",
    "Главстрой" : "10.1.255.71",
    "Бинергия" : "10.1.255.75",
    "Такеда" : "10.1.255.76",
    "ГАУ Медиацентр" : "10.1.255.77",
    "ВСК" : "10.1.255.78",
    "Почта России 3 этаж" : "10.1.255.82",
    "НПП Торий" : "10.1.255.83",
    "АТОН" : "10.1.255.85",
    "ЖК Символ" : "10.1.255.86",
    "ЖК Лайнер" : "10.1.255.87",
    "Иммо Сервис" : "10.1.255.88",
    "НСК царская площадь" : "10.1.255.89",
    "Специальный депозитарий" : "10.1.255.92",
    "Новиком, Б.Полянка" : "10.1.255.93",
    "Балчуг Space1" : "10.1.255.96",
    "ИЭК Инвест" : "10.1.255.98",
    "ГПМ Радио" : "10.1.255.100",
    "ЖК Октябрьское поле 30А" : "10.1.255.101",
    "ЭКСМО, Зорге 1с1" : "10.1.255.102",
    "INFOWATCH" : "10.1.255.103",
    "RRC Крекшино" : "10.1.255.104",
    "Новикомбанк Профсоюзная" : "10.1.255.105",
    "Ресо Лизинг" : "10.1.255.106",
    "ПРО.Мед.Цс" : "10.1.255.107",
    "Ростех Гоголевский" : "10.1.255.111",
    "Банк Дом РФ, ул. Перова Поля" : "10.1.255.114",
    "Эксмо 8 этаж" : "10.1.255.115",
    "RRC Обручева" : "10.1.255.125",
    "ГПМ Радио, Даймонд Холл" : "10.1.255.126",
    "Артикон" : "10.1.255.131",
    "Ростелеком Вятская 35" : "10.1.255.132",
    "Ростелеком Никитский 7" : "10.1.255.133",
    "Иркут Жуковский (white)" : "10.1.255.141",
    "БЦ Ярд" : "10.1.255.143",
    "БЦ Солид Кама(white)" : "10.1.255.144",
    "ИЦ текстильной и легкой промышленности" : "10.1.255.145",
    "ООО Гарант (msi)" : "10.1.255.146",
    "МПО Румянцева (Заводской корпус)(white)" : "10.1.255.149",
    "Онланта Проходная" : "10.1.255.150",
    "Онланта 4 этаж(white)" : "10.1.255.151",
    "Олимпроект" : "10.1.255.153",
    "Технополис 13корп 1 этаж" : "10.1.255.155",
    "Спич" : "10.1.255.156",
    "Дом.рф 5 эт 2я точка" : "10.1.255.159",
    "ЭМЗ Мясищева" : "10.1.255.163",
    "ЭирТранс" : "10.1.255.165",
    "ДИАСОФТ" : "10.1.255.166",
    "Фазотрон" : "10.1.255.167",
    "БЦ Ренова" : "10.1.255.168",
    "Гинцветмет" : "10.1.255.169",
    "СТС Медиа(white)" : "10.1.255.171",
    "Русагро" : "10.1.255.174",
    "ПАО ИЛ" : "10.1.255.175",
    "АО ГЛОНАСС" : "10.1.255.176",
    "СМП Страхование Ватин" : "10.1.255.177",
    "Атомтехэнерго" : "10.1.255.178",
    "Мегафон" : "10.1.255.179",
    "Миль и Камов (white)" : "10.1.255.180",
    "Фонд Реформ ЖКХ" : "10.1.255.181",
    "Этажи" : "10.1.255.182",
    "Work'N'Soda" : "10.1.255.183",
    "Энергосеть" : "10.1.255.185",
    "ЖК БАЛТИЙСКАЯ 15" : "10.1.255.187",
    "Office Less" : "10.1.255.188",
    "ДРТ1 2эт mini" : "10.1.255.189",
    "БЦ Скайлайт mail.ru, vk 4эт." : "10.1.255.190",
    "ПАО ИЛ NEW 7эт." : "10.1.255.194",
    "Новикомбанк Полянка 2эт" : "10.1.255.195",
    "Ботаника 24" : "10.1.255.196",
    "БЦ Wall Street" : "10.1.255.197",
    "Huawei" : "10.1.255.198",
    "СТС медиа БЦ Монарх" : "10.1.255.199",
    "Автобантранс" : "10.1.255.200",
    "ФК Пульс" : "10.1.255.201",
    "Дзен Платформа" : "10.1.255.202",
    "Линк Групп " : "10.1.255.203",
    "Желдорпроект" : "10.1.255.205",
    "Сбер Здоровье" : "10.1.255.206",
    "Москвариум " : "10.1.255.208",
    "Авито " : "10.1.255.209",
    "РеТрейдинг " : "10.1.255.210",
    "Девелоника Mini" : "10.1.255.211",
    "Лэтуаль " : "10.1.255.213",
    "ВТБ Лизинг 27Ас1" : "10.1.255.214",
    "ВТБ Лизинг 18с1" : "10.1.255.215",
    "Норси Транс центр.офис" : "10.1.255.216",
    "РеТрейдинг-2" : "10.1.255.218",
    "Динамо-Москва Mini" : "10.1.255.219",
    "НРК РОСТ" : "10.1.255.220",
    "Биокард Логистик" : "10.1.255.221",
    "Честный знак" : "10.1.255.222",
    "Стройконтинент " : "10.1.255.223",
    "Новосталь-М" : "10.1.255.225",
    "М Видео к.20" : "10.1.255.226",
    "М Видео к.10" : "10.1.255.227",
    "М Видео к.5" : "10.1.255.228",
    "ГК Самолет" : "10.1.255.229",
    "Президент Сервис" : "10.1.255.231",
    "Экостандарт (MSI)" : "10.1.255.232",
    "Маркс Групп" : "10.1.255.235",
    "Норси Транс Mini" : "10.1.255.236",
    "НИИАА" : "10.1.255.240",
    "ИнтерУрок" : "10.1.255.241",
    "Яндекс, Лотте плаза" : "10.1.255.245",
    "Яндекс, Аврора" : "10.1.255.246",
    "РЖД строй" : "10.1.255.247",
    "Склад-sale" : "10.1.255.248",
    "Мани Мен 13эт" : "10.1.255.249",
    "Мани Мен 9 эт" : "10.1.255.250",
    "Ральф Рингер" : "10.1.255.253",
    "ВИК Групп" : "10.1.255.254",
    "Тинькофф" : "10.1.2.55",
    "БЦ Джаз" : "10.1.2.57",
    "НАМИ" : "10.1.2.61",
    "SRG" : "10.1.2.62",
    "РЖД Щербинка университет" : "10.1.2.63",
    "СТС Медиа Даниловская мануфактура" : "10.1.2.64",
    "Миль и Камов 2 точка" : "10.1.2.65",
    "Фрезарт" : "10.1.2.66",
    "Кронштадт 1эт" : "10.1.2.67",
    "Кронштадт 2эт" : "10.1.2.68",
    "Терра Линк" : "10.1.2.69",
    "Easy Media mini" : "10.1.2.70",
    "Игроник" : "10.1.2.71",
    "Ункомтех Mini" : "10.1.2.72",
    "РОССТ" : "10.1.2.73",
    "Инвитро" : "10.1.2.74",
    "МВидео 20 корпус 5 этаж." : "10.1.2.75",
    "Салым Петролеум Кухня" : "10.1.2.76",
    "Салым Петролеум Ресепшен" : "10.1.2.77",
    "Икар" : "10.1.2.78",
    "Феско Новокузнецкая" : "10.1.2.79",
    "Феско Толмачевский" : "10.1.2.80",
    "Феско Б. Татарская" : "10.1.2.81",
    "БЦ Ринко Плаза" : "10.1.2.86",
    "Москабельмет " : "10.1.2.87",
    "Позитив Технолоджис" : "10.1.2.88",
    "Элвис " : "10.1.2.89",
    "Коворкинг Smart Yard" : "10.1.2.90",
    "ДРТ1 3эт. mini" : "10.1.2.91",
    "ДРТ1 8эт" : "10.1.2.92",
    "НИИМЭ" : "10.1.2.93",
    "Стоун Лизинг" : "10.1.2.94",
    "Ростех Летная Резиденс" : "10.1.2.95",
    "ПАО Банк Траст" : "10.1.2.96",
    "Т-1" : "10.1.2.97",
    "Киностудия имени Горького" : "10.1.2.98",
    "Блэк Стар" : "10.1.2.99",
    "Кофейный дом ХОРСЪ" : "10.1.3.0",
    "Оберон" : "10.1.3.1",
    "ОЗК" : "10.1.3.2",
    "СО ЕЭС" : "10.1.3.3",
    "Ренессанс Страхование" : "10.1.3.4",
    "Городской методический центр" : "10.1.3.5",
    "РЖД Щербинка  mini." : "10.1.3.6",
    "Ростелеком Вернадского" : "10.1.3.7",
    "ВТБ Факторинг" : "10.1.3.8",
    "Бест доктор" : "10.1.3.9",
    "БЦ Оазис" : "10.1.3.10",
    "Локотех Гончарный" : "10.1.3.11",
    "Локотех Земляной Вал" : "10.1.3.12",
    "Лоция - Ингосстрах жизнь" : "10.1.3.13",
    "Коворкинг Фабрика" : "10.1.3.14",
    "Фармстандарт" : "10.1.3.15",
    "Коворкинг Office Less Полянка" : "10.1.3.16",
    "Тинькофф Хуторская 1эт" : "10.1.3.17",
    "Тинькофф Хуторская 2эт" : "10.1.3.18",
    "Тинькофф Хуторская 3эт" : "10.1.3.19",
    "Тинькофф Хуторская 6эт" : "10.1.3.20",
    "Мосгоризберком" : "10.1.3.21",
    "Дирекция тяги филиал РЖД" : "10.1.3.22",
    "Детский мир" : "10.1.3.23",
    "Чубакка" : "10.1.3.24",
    "ex------Склад - sale" : "10.1.255.8",
    "Тестовый Гронет" : "10.1.255.6"
}

def match_name(jpg):
        for hostname,ip in term_list.items():
                if ip == jpg:
                        return(hostname)

html = """<!DOCTYPE html>
<html>
<head>
<style>
div.gallery {
  border: 1px solid #ccc;
}

div.gallery:hover {
  border: 1px solid #777;
}

div.gallery img {
  width: 100%;
  height: auto;
}

div.desc {
  padding: 15px;
  text-align: center;
}

* {
  box-sizing: border-box;
}

.responsive {
  padding: 0 6px;
  float: left;
  width: 24.99999%;
}

@media only screen and (max-width: 700px) {
  .responsive {
    width: 49.99999%;
    margin: 6px 0;
  }
}

@media only screen and (max-width: 500px) {
  .responsive {
    width: 100%;
  }
}

.clearfix:after {
  content: "";
  display: table;
  clear: both;
}
</style>
</head>
<body>

<h2>"""
html += f"<center><b>Всего терминалов опрошено:  {str(number_files)}</b>"
html += f"<center><b>Дата обновления информации: {today} </b>"
html += f"<center><b>Время обновления информации: {time_now} </b>"
html += f"<center><b>-------</b>"
html += """</h2>
<h4>test_env</h4>
"""


for infile in glob.glob("*.jpg"):
    if os.stat(infile).st_size != 0:
      outfile = os.path.splitext(infile)[0] + ".mini.jpg"
      if infile != outfile:
        im = Image.open(infile)
        im2 = im.resize((size),resample=Image.BICUBIC)
        im2.save(outfile, "JPEG")


for file in glob.glob("*.mini.jpg"):
    ip = file.rstrip(".mini.jpg")
    hostname = match_name(ip)
    #print(ip + hostname)
    html += f"""<div class="responsive">
  <div class="gallery">
    <a target="_blank" href="{file}">
      <img src="{file}" alt="{file}" width="600" height="400">
    </a>
    <div class="desc">{file} <p style="color:#FF0000";><big><big>{hostname}</big></big></p></div>
  </div>
</div>
"""

html +="""
<div class="clearfix"></div>

<div style="padding:6px;">
  <p> </p>
</div>

</body>
</html>
"""
with open("test.html", "w", encoding="WINDOWS-1251") as outputfile:
        outputfile.write(html)
