#Hakim Al Ghifari

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user = input ("Masukkan email pengguna : ")
email_password = input("Masukkan Password : ") 
email_send=input("Masukkan email tujuan: ")
           
subject = input ("Subject email : ") 

msg = MIMEMultipart()
msg['From'] =  email_user
msg['To'] = email_send
msg['Subject'] = subject


tambahan = int(input("Pilih 1 jika ingin attach file atau pilih 0 jika tidak : "))

if tambahan ==0:
  print("Tidak memilih attachment")
  body = input("Isi pesan email : ")  
  msg.attach(MIMEText (body,'plain'))
elif tambahan ==1: 
  filename = input("Masukkan nama file beserta formatnya : ")  #seperti gambar.jpg atau document.txt
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
print("email berhasil dikirim!")

server.quit()
