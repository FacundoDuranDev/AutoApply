import os
import smtplib
from email.message import EmailMessage
import imghdr
with open('emails.txt','r') as f:
    email_list = f.read().split(', ')
USER_ADRESS = os.environ.get('USER_EMAIL')
USER_PASSWORD = os.environ.get('USER_PASSWORD')
with open('Facundo_Duran_CV.pdf','rb') as f:
                file_data = f.read()
                file_name = f.name
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(USER_ADRESS, USER_PASSWORD)
        for email in email_list:
            msg = EmailMessage()
            msg['Subject'] = "Python Developer"
            msg['From'] = USER_ADRESS
            msg.set_content('¡Hola! ¿Como estás?\nMi nombre es Facundo Duran, soy un desarrollador de Python con casi un año de experiencia como Data Engineer.\nActualmente me desempeño como WebScraper en BB-Business Bureau, automatizando procesos ETL para la obtención de datos utiles en el mundo del entretenimiento. Tengo un nivel de Inglés lo suficientemente alto como para mantener conversaciones fluidas. Me apasiona la automatización de procesos manuales, de hecho, ahora mismo soy un robot... ¡Bip Bop! Cree un proyecto que recopila los datos de https://www.python.org.ar/trabajo/ para obtener todos los mails, ¡incluyendo el tuyo!\nPuedes ver el codigo de mi proyecto en https://github.com/FacundoDuranDev/AutoApply si te interesa.\nTe adjunto mi CV actualizado en inglés junto con este correo.\nMuchas gracias por tu tiempo de lectural *Inserte sonidos de Arturito* Espero que mi acercamiento no te parezca demasiado extraño, pero me pareció divertido hacer este proyecto de un día para tener más oportunidades.'
                            )
            msg.add_attachment(file_data, maintype='application',subtype='octet-stream',filename=file_name)
            msg['To'] = email
            smtp.send_message(msg)