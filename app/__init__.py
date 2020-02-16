from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kush'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465' # (or try 2525)
app.config['MAIL_USERNAME'] = '0572daf4785629'
app.config['MAIL_PASSWORD'] = '29e38c00d032ee' 
mail = Mail(app)

from app import views