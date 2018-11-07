import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("sharkpandi@gmail.com","sankara@2709")
msg="Sent from my desktop"
server.sendmail("sharkpandi@gmail.com","sankara@2709",msg)
server.quit()
