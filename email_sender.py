import os
import smtplib
from email.message import EmailMessage
import imghdr
with open('emails.txt','r') as f:
    email_list = f.read().split(', ')
USER_ADRESS = os.environ.get('USER_EMAIL')
USER_PASSWORD = os.environ.get('USER_PASSWORD')
emails = ['facu_javi_du@gmail.com',"example@gmail.com"]
with open('Facundo_Duran_CV.pdf','rb') as f:
                file_data = f.read()
                file_name = f.name
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(USER_ADRESS, USER_PASSWORD)
        for email in emails:
            msg = EmailMessage()
            msg['Subject'] = "Python Developer"
            msg['From'] = USER_ADRESS
            msg.set_content('¡Hola! ¿Como estás?'
                            + '\n'
                            + 'Mi nombre es Facundo Duran, Desarrollador Python con casi un año de experiencia en Data Engineering'
                            + '\n'
                            + 'Trabajo en todo tipo de procesos ETL y automatizaciones de todo tipo. Hablando de automatizaciones, este proceso es un proceso automatizado. Soy un robot Bip Bop.'
                            + 'Utilizando mis habilidades para obtener datos obtuve tu propuesta desde la pagina de python.org.ar'
                            )
            msg.add_attachment(file_data, maintype='application',subtype='octet-stream',filename=file_name)
            msg['To'] = email
            smtp.send_message(msg)