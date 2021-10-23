# -*- encoding: utf-8 -*-
import smtplib
import socket
from getpass import getpass

mail = smtplib.SMTP("smtp.gmail.com", 587)
mail.ehlo()
mail.starttls()

print("[+] 1 - Tek Kullanıcıya Mesaj Gönder" + "\n" + "[+] 2 - Toplu Mesaj Gönder")
secenek = int(input("[+] Lütfen yapmak istediğiniz işlemi seçiniz: "))

if secenek == 1:

     content = input("[+] Lütfen Göndermek İstediğiniz Mesajı Giriniz:"))
     emailadresi = input("[+] Lütfen Email Adresinizi Giriniz:"))
     sifre = getpass("[+] Lütfen Şifrenizi Giriniz:"))
     mail_kimden = input("[+] Lütfen Hangi Email Adresinden Mail Göndereceğinizi Giriniz:"))
     mail_kime = input("[+] Lütfen Hangi Email Adresine Mail Göndereceğinizi Giriniz:"))

     mail.login(emailadresi,sifre)
     mail.sendmail(mail_kimden , mail_kime,content)
     
if secenek == 2:

    emailadres_list = input("[+] Lütfen Email Adreslerinin Bulunduğu Text Uzantılı Dosyanın Dizinini Giriniz:"))
    emailadres_list = open(emailadres_list,"r")
    content = input("[+] Lütfen Göndermek İstediğiniz Mesajı Giriniz:"))
    mail_kimden = input("[+] Lütfen Hangi Email Adresinden Mail Göndereceğinizi Giriniz:"))

    for email in emailadres_list:
      try:
          mail.sendmail(mail_kimden,emailadres_list)
          print("[+] Mailler gönderildi!")
          break
      except smtplib.SMTPConnectError :
          print("[+] Bağlantı Hatası")
    emailadres_list.close()
else :
   print("[+] Yanlış seçim yaptınız!")

