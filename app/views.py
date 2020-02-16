"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for, flash
from app.forms import ContactForm

from app import mail
from flask_mail import Message 


###
# Routing for your application.
###

@app.route('/', methods=['GET','POST'])
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/contact', methods=['POST','GET'])
def contact():
    """Render the website's contact page."""
    form = ContactForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            flash('Your email was successfully sent.')
            return redirect(url_for('.home'))
    return render_template('contact.html', form=form)


###
# The functions below should be applicable to all Flask apps.
###

@app.route("/")
def index():
    msg = Message("Info3180",
                sender=("Jelani Bryan-Hall","jelanikush@gmail.com"), 
                recipients=["info3180lab@gmail.com"])
    msg.body = 'This is the body of the message. Hello how are you?'
    mail.send(msg)

# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
