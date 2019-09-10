
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

fromaddr = "ankushbanik1234@gmail.com"
toaddr = "ankushbanik123@gmail.com" 
# toCC = "ghi@gmail.com,jkl@hotmail.com,mnopq@yahoo.com" # Write all the email ids that you want to be present in CC, separated by commas.
#toBCC = "ghi@gmail.com,jkl@hotmail.com,mnopq@yahoo.com" # Use this, if need be
toaddrs = [toaddr]  + toCC.split(",") # +toBCC.split(",")

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
# msg['CC'] = toCC
#msg['BCC'] = toBCC
msg['Subject'] = "Give your static subject here "
body = '''Dear Mr. XYZ,
This is a sample code to send email.
Thanks,
Python
'''
msg.attach(MIMEText(body, 'plain'))

filename = "File that should be attached.txt"
f = file(filename)
attachment = MIMEText(f.read())
attachment.add_header('Content-Disposition', 'attachment', filename=filename)           
msg.attach(attachment)


import smtplib
#Simple Mail Transfer Protocol (SMTP) is a protocol,
# which handles sending e-mail and routing e-mail between mail servers.

#Python provides smtplib module, which defines an SMTP client session object that can be used to send mail 
# to any Internet machine with an SMTP or ESMTP listener daemon.

server = smtplib.SMTP(host='smtp.gmail.com', port=587) # to use any other host, check for their host name and its respective port number from internet
server.ehlo()
server.starttls()
server.ehlo()
server.login("ankushbanik12342gmail.com", "dashing boy")#Give your id and pwd here
text = msg.as_string()
server.sendmail(fromaddr, toaddrs, text)
server.quit()