from django.db import migrations, models

def add_lines_and_stations(apps, schema_editor):
    Line = apps.get_model("hello", "LineModel")
    Station = apps.get_model("hello", "StationModel")

    lines = [
        {"name": "Сокольническая", "color": 0xFFCC0000, "stations": [
            "Бульвар Рокоссовского", "Черкизовская", "Преображенская площадь", "Сокольники", "Красносельская",
            "Комсомольская", "Красные Ворота", "Чистые пруды", "Лубянка", "Охотный Ряд", "Библиотека имени Ленина",
            "Кропоткинская", "Парк культуры", "Фрунзенская", "Спортивная", "Воробьёвы горы", "Университет",
            "Проспект Вернадского", "Юго-Западная", "Тропарёво", "Румянцево", "Саларьево", "Филатов Луг",
            "Прокшино", "Ольховая", "Новомосковская", "Потапово"
        ]},
        {"name": "Замоскворецкая", "color": 0xFF008000, "stations": [
            "Ховрино", "Беломорская", "Речной вокзал", "Водный стадион", "Войковская", "Сокол", "Аэропорт",
            "Динамо", "Белорусская", "Маяковская", "Тверская", "Театральная", "Новокузнецкая", "Павелецкая",
            "Автозаводская", "Технопарк", "Коломенская", "Каширская", "Кантемировская", "Царицыно", "Орехово",
            "Домодедовская", "Красногвардейская", "Алма-Атинская"
        ]},
        {"name": "Арбатско-Покровская", "color": 0xFF0096FF, "stations": []},
        {"name": "Филёвская", "color": 0xFF89CFF0, "stations": []},
        {"name": "Кольцевая", "color": 0xFF8B4513, "stations": []},
        {"name": "Калужско-Рижская", "color": 0xFFFFA500, "stations": []},
        {"name": "Таганско-Краснопресненская", "color": 0xFFA000A0, "stations": []},
        {"name": "Калининская", "color": 0xAAFFFF00, "stations": []},
        {"name": "Серпуховско-Тимирязевская", "color": 0xFF808080, "stations": []},
        {"name": "Люблинско-Дмитровская", "color": 0xFF90EE90, "stations": []},
        {"name": "Каховская", "color": 0xFF96DED1, "stations": []},
        {"name": "Бутовская", "color": 0xFFB0E0E6, "stations": []},
    ]

    for line in lines:
        line_instance = Line(name=line["name"], color=line["color"])
        line_instance.save()
        for i in range(len(line["stations"])):
            station_instance = Station(num = i + 1, name=line["stations"][i - 1], line=line_instance)
            station_instance.save()

class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_linemodel_color_linemodel_name_alter_usermodel_email_and_more'),
    ]

    operations = [
        migrations.RunPython(add_lines_and_stations)
    ]