import smtplib
import socket
import sys


class Mailit:

 def __init__(self, emailid, password, to, sub, msgbody):
    try:
        smtpserver = smtplib.SMTP('smtp.gmail.com', 587)

        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo()
        try:
            smtpserver.login(emailid, password)
        except smtplib.SMTPException:
           print('authentication failed \n')
    except (socket.gaierror, socket.error, socket.herror, smtplib.SMTPException):
        print(' connection to gmail failed ' + '\n')
        sys.exit(1)

    header = to + '\n' + emailid + '\n' + sub + '\n'
    msg = header + '\n' + msgbody

    try:
        smtpserver.sendmail(emailid, to, msg)
    except smtplib.SMTPException:
        print('email could not be sent')
        smtpserver.close()
        sys.exit(1)

    print(' email sent successfully ')
    smtpserver.close()
    sys.exit(1)


obj = Mailit("swetasoorya@gmail.com", "ilovemymom*", "pkspgtchem@gmail.com", "yee", "mail from python")

