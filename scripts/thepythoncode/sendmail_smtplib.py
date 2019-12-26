# https://www.thepythoncode.com/article/sending-emails-in-python-smtplib

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# your credentials
email = "email@example.com"
password = "password"

# the sender's email
FROM = "from@example.com"
# the receiver's email
TO = "to@example.com"
# the subject of the email (subject)
subject = "Just a subject"

# initialize the msg we wanna send
msg = MIMEMultipart()
# set the sender's email
msg["From"] = FROM
# set the receiver's email
msg["To"] = TO
# set the subject
msg["Subject"] = subject
