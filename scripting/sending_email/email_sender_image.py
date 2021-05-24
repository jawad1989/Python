""" turn on before sending email
https://support.google.com/accounts/answer/6010255"""

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from string import Template
from pathlib import Path

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


html = Template(Path('index.html').read_text())#.substitute(name='Jawad')


# Update line 10, 18
email            = MIMEMultipart('alternative')
email['from']    = 'sender'
email['to']      = 'receiver@gmail.com'
email['subject'] = "you won 300 dollars"


text = MIMEText('<p>Hi this is test message</p> <img src="cid:image1">', 'html')
email.attach(text)

image = MIMEImage(open('pikachu.jpg', 'rb').read())

# Define the image's ID as referenced in the HTML body above
image.add_header('Content-ID', '<image1>')
email.attach(image)


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('sender@gmail.com','pasword')
    smtp.send_message(email)
    print('email sent')
