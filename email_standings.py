#!/usr/bin/python3 

import smtplib
from email.mime.text import MIMEText
import sys
import datetime

today = datetime.date.today()

try:
    s = smtplib.SMTP('smtp.bob.com', 587)
    s.starttls()
    s.login("USER", "PASSWD")
    s.set_debuglevel(0)

    msg = MIMEText("""TEST TEST \n TEST TEST""")

    sender = 'send1@bob.com'

    recipients = ['user1@bob.com', 'user2@bob.com']

    msg['Subject'] = "BB POOL " + str(today)

    msg['From'] = sender

    msg['To'] = ", ".join(recipients)
 
    s.sendmail(sender, recipients, msg.as_string())

except Exception as err:
    pirnt(err)
    sys.exit(1)
