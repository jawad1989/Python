""" turn on before sending email
https://support.google.com/accounts/answer/6010255"""

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('index.html').read_text())#.substitute(name='Jawad')


# Update line 10, 18
email            = EmailMessage()
email['from']    = 'sender'
email['to']      = 'receiver@gmail.com'
email['subject'] = "you won 300 dollars"

email.set_content(html.substitute({'name' : 'Jawad', 'dollars' : '200'}),'html')
print(email)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('sender@gmail.com','pasword')
    smtp.send_message(email)
    print('email sent')
