from flask import Flask, request, redirect
import cgi
import os
import jinja2


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_dir),
    autoescape=True
)

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    template = jinja_env.get_template('index.html')
    return template.render()


@app.route("/movies", methods=['POST'])
def validate():
    user_name = request.form['username']
    username_error = ""

    pass_word = request.form['password']
    password_error = ""

    verify_password = request.form['verified']
    verified_error = ""

    e_mail = request.form['email']
    email_error = ""

    count = 0
    count_dots = 0

    template = jinja_env.get_template('index.html')

    if len(user_name) < 6:
        username_error = "User name MUST be greater than 6 characters!"
    for letter in user_name:
        if not letter.isalpha():
            username_error = "Username CANNOT contain spaces!"

    if len(pass_word) < 3 or len(pass_word) > 20:
        password_error = "Password MUST be greater than 20 characters (less than 20)!"
    for letter in pass_word:
        if not letter.isalpha():
            password_error = "Password CANNOT contain spaces!"
    if pass_word != verify_password:
        verified_error = "Both passwords MUST be identical!"

    if len(e_mail) > 0:

        for letter in e_mail:
            if letter == "@":
                count += 1
            if letter == ".":
                count_dots += 1
        if count != 1 or count_dots != 1:
            email_error = "Sorry! This is not a valid email!"

    if not password_error and not verified_error and not username_error and not email_error:
        name = user_name
        return redirect('/welcome?name={0}'.format(name))

    return template.render(name=user_name,
                           password=pass_word,
                           pwd=verify_password,
                           email=e_mail,
                           username_error=username_error,
                           password_error=password_error,
                           verified_error=verified_error,
                           email_error=email_error
                           )


@app.route('/welcome')
def welcome():
    name = request.args.get('name')
    return '<h1> Welcome, {0}! Are you ready for your next adventure? <h1>'.format(name)


app.run()
