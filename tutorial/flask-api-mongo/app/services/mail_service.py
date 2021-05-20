from threading import Thread
from flask_mail import Mail, Message
from resources.errors import InternalServerError

mail = Mail(app=None)
app = None


def initialize_mail_service(appiclation):
    global mail
    global app
    mail = Mail(app=appiclation)
    app = appiclation


def send_async_email(app, msg, mail):
    with app.app_context():
        try:
            mail.send(msg)
        except ConnectionRefusedError:
            raise InternalServerError("[MAIL SERVER] not working")


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(app, msg, mail)).start()
