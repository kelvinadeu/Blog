from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required
from ..models import User,Blogs
from .forms import AddBlogForm
from .. import db
from ..request import *

@main.route('/')
def index():

    today =get_single('random')
    print(today)

    return render_template('index.html', title=title,today = today)

@main.route('/new_blog', methods = ['GET','POST'])
@login_required
def new_blog():
	form = BlogForm()
	if form.validate_on_submit():
		blog = Blog(post=form.post.data,body=form.body.data)
		blog.save_blog()
		return redirect(url_for('main.index'))
	return render_template('new_blog.html',form=form)

@main.route('/view_blogs', methods = ['GET','POST'])
def view_blogs():

	first=Blog.query.limit(1).all()

	return render_template('view_blogs.html',first=first)
