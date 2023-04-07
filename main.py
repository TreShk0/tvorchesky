#Импорт необходимых модулей
import pandas as pd
import smtplib

#Создание датафрейма table
table = pd.read_csv('dataset.csv', delimiter=',')
#Группировка и создание результирующей таблицы, сохранение ее в файл
result = table.groupby(['platform', 'event']).size()
result.to_csv('result.csv', sep=',')


smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()

smtpObj.login('login', 'password')

smtpObj.sendmail("treshkobattle@gmai.com","tr3shk0@yandex.ru","test")

smtpObj.quit()