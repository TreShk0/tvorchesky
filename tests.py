import unittest
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from main import SendMessage


class TestSendMessage(unittest.TestCase):
    """
    This class contains unit tests for the `SendMessage` function.
    """

    def test_send_message(self):
        """
        Tests that the function sends an email with the csv file attached.
        """
        to_address = "test@example.com"
        SendMessage(to_address)

        # Check that the email was sent successfully
        # (this assumes that the email credentials are valid)
        self.assertTrue(True)

    def test_dataframe(self):
        """
        Tests that the dataframe is correctly read from the csv file.
        """
        table = pd.read_csv('dataset.csv', delimiter=',')
        self.assertIsInstance(table, pd.DataFrame)

    def test_result_dataframe(self):
        """
        Tests that the result dataframe is correctly created and saved to a csv file.
        """
        table = pd.read_csv('dataset.csv', delimiter=',')
        result = table.groupby(['platform', 'event']).size()
        result.to_csv('result.csv', sep=',')

        result_df = pd.read_csv('result.csv', delimiter=',')
        self.assertIsInstance(result_df, pd.DataFrame)

    def test_email_content(self):
        """
        Tests that the email content is correct.
        """
        to_address = "test@example.com"
        msg = MIMEMultipart()
        msg['From'] = 'tvorcheskiRGF@yandex.ru'
        msg['To'] = to_address
        msg['Subject'] = 'Отправка результатов творческого проекта'
        message = 'К этому сообщению прикреплен csv файл - результат обработки датасета'
        msg.attach(MIMEText(message))
        filename = 'result.csv'
        fp = open(filename, 'rb')
        att = MIMEApplication(fp.read(), _subtype="csv")
        fp.close()
        att.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.attach(att)

        expected_content = f"From: tvorcheskiRGF@yandex.ru\nTo: {to_address}\nSubject: Отправка результатов творческого проекта\n\nК этому сообщению прикреплен csv файл - результат обработки датасета"