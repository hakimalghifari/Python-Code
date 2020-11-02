#Hakim Al Ghifari

import getpass
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user = input ("Please enter user email : ")
email_password = getpass.getpass()         
print("Password correct!")               
email_send = input("Please enter recepient email : ")

subject = input ("Subject email : ") 

msg = MIMEMultipart()
msg['From'] =  email_user
msg['To'] = email_send
msg['Subject'] = subject

body = input("Write the message : ")  
msg.attach(MIMEText (body,'plain'))



tambahan = int(input("Choose 1 if you want to attach file or choose 0 to not attach : "))
if tambahan ==0:
  print("Not Choosing attachment")

elif tambahan ==1: 
  filename = input("Enter file name with the format : ")  #format ex, .jpg, pdf, txt etc & must be in the same folder with your .py code
  attachment = open(filename, 'rb')
  part = MIMEBase('application','octet-stream')
  part.set_payload((attachment).read())
  encoders.encode_base64(part)
  part.add_header('Content-Disposition', "attachment; filename= "+ filename)
  msg.attach(part)

text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_user, email_password)
server.sendmail(email_user, email_send, text)
print("email sent!")

server.quit()
