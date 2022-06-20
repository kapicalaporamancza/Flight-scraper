import smtplib
import ssl
from email.message import EmailMessage

def sender(subject, attach):		
	email_sender = 'jezyki.skryptowe.260468@gmail.com'
	email_password = 'vfwhbrpvgxondsuu'
	email_receiver = 'kapicalaporamancza@gmail.com'

	body = "Wyniki twojego zapytania znajdują się w załączniku."

	em = EmailMessage()
	em['From'] = email_sender
	em['To'] = email_receiver
	em['Subject'] = subject
	em.set_content(body)

	with open(attach, 'rb') as content_file:
		content = content_file.read()
		em.add_attachment(content, maintype='application', subtype='xlsx', filename=attach)
	
	context = ssl.create_default_context()

	with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
		smtp.login(email_sender, email_password)
		smtp.sendmail(email_sender, email_receiver, em.as_string())