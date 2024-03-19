import random
import smtplib
from email.mime.text import MIMEText

try:
    otp = ''.join([str(random.randint(0, 9)) for i in range(4)])

    msg = MIMEText('Hello, your otp is: ' + str(otp))

    msg['Subject'] = 'Your OTP'
    msg['From'] = 'email-1@gmail.com’
    msg['To'] = 'email-2@gmail.com'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login('email-1@gmail.com', 'email-1_app_password’)

    server.sendmail('email-1@gmail.com', 'email-2@gmail.com', msg.as_string())

    server.quit()

    print("Email sent successfully!")
except Exception as e:
    print("An error occurred:", e)
