import smtplib, ssl
import getpass

smtp_server = 'smtp.mail.yahoo.com'
port = 587
sender_email = 'bauer.david@att.net'
receiver_email = 'mathew.sommers@ge.com'
password = getpass.getpass(prompt='Type password and press enter: ', stream=None)
message = """\
Subject: Hulllooo!

This message was sent from Python, Dude!"""


# Create a secure SSL context
context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)


# Try to log into server and send email
# try:
#     server = smtplib.SMTP(smtp_server, port)
#     print(server.help())
#     # server.ehlo()
#     # server.starttls(context=context)
#     # server.ehlo()
#     # server.login(sender_email, password)
#     # server.sendmail(sender_email, receiver_email, message)
# except Exception as e:
#     print(e)
# finally:
#     server.quit()