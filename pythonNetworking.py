import smtplib
from email.mime.text import MIMEText


# smtpObj = smtplib.SMTP('smtp-relay.sendinblue.com', 587)

# smtpObj.login('schoolofiris@gmail.com', 'wOnxApCs7m4zKvSB')


# message = MIMEText('This is the message body')
# message['From'] = 'schoolofiris@gmail.com'
# message['To'] = 'schoolofiris@gmail.com'
# message['Subject'] = 'This is the subject'

with smtplib.SMTP('smtp-relay.sendinblue.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login('schoolofiris@gmail.com','wOnxApCs7m4zKvSB')

    subject = 'grab dinner this weekend'
    body = 'how about 6pm?'
    msg = subject + body

    smtp.sendmail('schoolofiris@gmail.com', 'mohammedirisa@gmail.com', msg)
