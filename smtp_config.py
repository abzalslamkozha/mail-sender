import smtplib
from settings import EMAIL_HOST_PASSWORD, EMAIL_PORT, EMAIL_HOST, EMAIL_HOST_USER
from schemas import Message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_connection = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
smtp_connection.starttls()
smtp_connection.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)


def send_email(message: Message):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_HOST_USER
        msg['To'] = message.to
        msg['Subject'] = message.subject

        msg.attach(MIMEText(message.message, 'plain'))

        smtp_connection.sendmail(EMAIL_HOST_USER, message.to, msg.as_string())

        return "success"

    except Exception as e:
        return e
