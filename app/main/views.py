from flask import render_template
from . import main





@main.route('/')
def index():

    title = 'Home Page - Welcome to Adeu blogs,your daily inspiration'

    new_single= get_single('general')
    return render_template('index.html',title=title)
