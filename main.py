#Импорт необходимых модулей
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


#Создание датафрейма table
table = pd.read_csv('dataset.csv', delimiter=',')
#Группировка и создание результирующей таблицы, сохранение ее в файл
result = table.groupby(['platform', 'event']).size()
result.to_csv('result.csv', sep=',')

def SendMessage(to_adress):
    try:
        msg = MIMEMultipart()
        msg['From'] = 'tvorcheskiRGF@yandex.ru'
        msg['To'] = to_adress
        msg['Subject'] = 'Отправка результатов творческого проекта'
        message = 'К этому сообщению прикреплен csv файл - результат обработки датасета'
        msg.attach(MIMEText(message))
        filename='result.csv'
        fp=open(filename,'rb')
        att = MIMEApplication(fp.read(),_subtype="csv")
        fp.close()
        att.add_header('Content-Disposition','attachment',filename=filename)
        msg.attach(att)
        mail = smtplib.SMTP('smtp.yandex.ru',587)
        mail.set_debuglevel(True)
        mail.starttls()
        mail.login('tvorcheskiRGF@yandex.ru', 'wwfdpcikojevhvuk')
        mail.sendmail("tvorcheskiRGF@yandex.ru",to_adress,msg.as_string())
        mail.quit()
        print("Результаты отправлены")
    except smtplib.SMTPException:
        print("Не удалось отправить письмо, что-то пошло не так")

to_adress = input("Введите адрес получателя: ")
SendMessage(to_adress)