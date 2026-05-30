temperature = 30
is_raining = False
if temperature > 30:
    print("Сегодня очень жарко. Оставайтесь в помещении.")
elif 20 <= temperature <= 30:
    if is_raining:
        print("Тепло, но идет дождь. Возьмите зонт.")
    else:
        print("Тепло и солнечно. Отличная погода для прогулки.")
elif 10 <= temperature < 20:
        print("Прохладно. Наденьте куртку.")
else:
        print("Холодно. Одевайтесь тепле.")