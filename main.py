#Импорт необходимых модулей
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#Создание датафрейма table
table = pd.read_csv('dataset.csv', delimiter=',')
#Группировка и создание результирующей таблицы, сохранение ее в файл
result = table.groupby(['platform', 'event']).size()
result.to_csv('result.csv', sep=',')



msg = MIMEMultipart()
msg['From'] = 'tvorcheskiRGF@yandex.ru'
msg['To'] = 'tr3shk0@yandex.ru'
msg['Subject'] = 'Тест скрипта SMTP'
message = 'Тестовое сообщение для отправки через скрипт'
msg.attach(MIMEText(message))


mail = smtplib.SMTP('smtp.yandex.ru',587)
mail.set_debuglevel(True)

mail.starttls()

mail.login('tvorcheskiRGF@yandex.ru', 'wwfdpcikojevhvuk')

mail.sendmail("tvorcheskiRGF@yandex.ru","tr3shk0@yandex.ru",msg.as_string())

mail.quit()