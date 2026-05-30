try:
    file = open ('example.txt', 'r')
    content = file.read()
    print (content)
except FileNotFoundError as e:
    print ("Файл не найден. Пожалуйста, проверьте имя файла и попробуйте снова.")
finally:
    file.close()
    print ("Файл закрыт.")
