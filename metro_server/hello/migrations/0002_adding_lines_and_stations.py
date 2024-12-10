from django.db import migrations

from hello.models import StationModel


def add_lines_and_stations(apps, schema_editor):

    LineModel = apps.get_model('hello', 'LineModel')
    StationModel = apps.get_model('hello', 'StationModel')

    lines = [
        {"name": "Сокольническая",
         "color": int(0xFFCC0000),
         "stations": [
             "Бульвар Рокоссовского", "Черкизовская", "Преображенская площадь",
             "Сокольники", "Красносельская",
             "Комсомольская", "Красные Ворота", "Чистые пруды", "Лубянка",
             "Охотный Ряд", "Библиотека имени Ленина",
             "Кропоткинская", "Парк культуры", "Фрунзенская", "Спортивная",
             "Воробьёвы горы", "Университет",
             "Проспект Вернадского", "Юго-Западная", "Тропарёво", "Румянцево",
             "Саларьево", "Филатов Луг",
             "Прокшино", "Ольховая", "Новомосковская", "Потапово"
         ]},
        {"name": "Замоскворецкая",
         "color": int(0xFF008000),
         "stations": [
             "Ховрино", "Беломорская", "Речной вокзал", "Водный стадион",
             "Войковская", "Сокол", "Аэропорт",
             "Динамо", "Белорусская", "Маяковская", "Тверская", "Театральная",
             "Новокузнецкая", "Павелецкая",
             "Автозаводская", "Технопарк", "Коломенская", "Каширская",
             "Кантемировская", "Царицыно", "Орехово",
             "Домодедовская", "Красногвардейская", "Алма-Атинская"
         ]},
        {"name": "Арбатско-Покровская", "color": int(0xFF0096FF), "stations": []},
        {"name": "Филёвская", "color": int(0xFF89CFF0), "stations": []},
        {"name": "Кольцевая", "color": int(0xFF8B4513), "stations": []},
        {"name": "Калужско-Рижская", "color": int(0xFFFFA500), "stations": []},
        {"name": "Таганско-Краснопресненская", "color": int(0xFFA000A0), "stations": []},
        {"name": "Калининская", "color": int(0xAAFFFF00), "stations": []},
        {"name": "Серпуховско-Тимирязевская", "color": int(0xFF808080), "stations": []},
        {"name": "Люблинско-Дмитровская", "color": int(0xFF90EE90), "stations": []},
        {"name": "Каховская", "color": int(0xFF96DED1), "stations": []},
        {"name": "Бутовская", "color": int(0xFFB0E0E6), "stations": []},
    ]

    for ind, line in enumerate(lines, start=1):
        line_instance = LineModel(num=ind, name=line["name"], color=line["color"])
        line_instance.save()
        for i, station_name in enumerate(line["stations"], start=1):
            station_instance = StationModel(num=i, name=station_name, line=line_instance)
            station_instance.save()


class Migration(migrations.Migration):
    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_lines_and_stations),
    ]
