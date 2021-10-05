import smtplib

def notify(sender: str, password: str, destination: str, message: str):
  try:  
    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.login(sender, password)
    mailserver.sendmail(sender, destination, message.as_string())
    mailserver.close()
  except Exception as e:  
    print(e)