from app import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextField, TextAreaField
from wtforms.validators import DataRequired, Length
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect(app)

class ContactForm(FlaskForm):
    name = StringField('Name:',validators=[DataRequired()])
    email = StringField('Email:',validators=[DataRequired()])
    subject = StringField('Subject:',validators=[DataRequired()])
    msg = TextAreaField('Message:', [DataRequired(),Length(min=9, message=('Your message is too short.'))])
    submit = SubmitField('Submit')
'''
<div>
<label for="name">Full Name:</label>
<input type="text" id="name" name="full_name" />
</div>
<div>
<label for="mail">E-mail:</label>
<input type="email" id="mail" name="email" />
</div>
<div>
<label for="subject">Subject:</label>
<input type="text" id="subject" name="subject" />
</div>
<div>
<label for="msg">Message:</label>
<textarea id="msg" name="message"></textarea>
</div>
'''

