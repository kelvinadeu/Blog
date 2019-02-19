from flask import render_template
from . import main
from app.request import get_single




@main.route('/')
def index():

    title = 'Home Page - Welcome to Adeu blogs,your daily inspiration'
    new_single= get_single()
    return render_template('index.html',title=title,new_single=new_single)
