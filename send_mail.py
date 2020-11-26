import smtplib
from email.mime.multipart import MIMEMultipart  # Многокомпонентный объект
from email.mime.text import MIMEText  # Текст/HTML
from dictin import form_messege
from form_messege_head import form_messege_h
from addr_config import addr_f, addr_t, addr_f_password


def send_messege(h, a):
    msg = MIMEMultipart()
    msg['From'] = addr_f
    msg['To'] = addr_t
    msg['Subject'] = 'Test'
    body = form_messege_h(h) + form_messege(a)
    msg.attach(MIMEText(body, 'plain'))

    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login(addr_f, addr_f_password)
    s.send_message(msg)
    s.quit()

