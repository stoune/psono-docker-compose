#!/usr/bin/env python
# -*- coding: utf-8 -*-

### Script to debugging email send

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body, to_email, from_email, smtp_server, smtp_port, smtp_user, smtp_password):
    # Створення об'єкта повідомлення
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Додавання тіла повідомлення
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Підключення до SMTP сервера з використанням SSL
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Start TLS
            server.login(smtp_user, smtp_password)  # Вхід на сервер
            server.send_message(msg)  # Відправка повідомлення
            print("Email sent successfully")

    except Exception as e:
        print(f"Failed to send email: {e}")

def print_env_var_absent_exit(env_var: str):
    if not os.environ.get(env_var):
        print(f"{env_var} not defined. Script aborted.")
        exit(1)

def main():
    # Використання функції send_email
    # Returns `None` if the key doesn't exist
    print_env_var_absent_exit("PSONO_EMAIL_HOST")
    email_host = os.environ.get("PSONO_EMAIL_HOST")
    # email_host = 'mailserver'
    print(f"EMAIL_HOST : {email_host}") 
    print_env_var_absent_exit("PSONO_EMAIL_PORT")
    email_port = os.environ.get("PSONO_EMAIL_PORT")
    print(f"EMAIL_PORT : {email_port}") 
    # print_env_var_absent_exit("EMAIL_HOST_USER")
    smtp_user = os.environ.get("PSONO_EMAIL_HOST_USER")
    # print_env_var_absent_exit("EMAIL_HOST_PASSWORD")
    smtp_password = os.environ.get("PSONO_EMAIL_HOST_PASSWORD")
    print_env_var_absent_exit("PSONO_EMAIL_USE_TLS")
    print_env_var_absent_exit("PSONO_EMAIL_USE_SSL")
    print_env_var_absent_exit("PSONO_EMAIL_FROM")
    email_from = os.environ.get("PSONO_EMAIL_FROM")
    
    send_email(
        subject="Тема листа",
        body="Текст листа",
        to_email="recipient@example.com",
        from_email=email_from,
        smtp_server=email_host,
        smtp_port=email_port,
        smtp_user=smtp_user,
        smtp_password=smtp_password
    )

if __name__ == "__main__":
    main()