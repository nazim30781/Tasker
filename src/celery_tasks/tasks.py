from celery import Celery
import smtplib
from email.message import EmailMessage

from ..config import SMTP_PASS, SMTP_USER
from ..logger import logger

celery = Celery("tasks", broker="redis://localhost:6379")

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465

def get_email():
    email = EmailMessage()
    email['Subject'] = "Task"
    email['From'] = SMTP_USER
    email['To'] = SMTP_USER

    return email


@celery.task
def send_email():
    email = get_email()
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(email)
