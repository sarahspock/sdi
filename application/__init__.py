from flask import Flask, redirect, render_template

app = Flask(__name__)

# Import a module / component using its blueprint handler variable
from mod_front.controllers import mod_front as front_module

app.register_blueprint(front_module)

@app.route('/')
def template_location():
    return render_template('front.html')
