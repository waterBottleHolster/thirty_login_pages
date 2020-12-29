from flask import render_template, session, redirect, url_for
from . import main
from .forms import PostForm
from .. import db
from ..models import Post
from flask_login import login_required, current_user

@main.route('/')
@login_required
def index():
    return render_template('index.html')

@main.route('/cash_flow')
@login_required
def cash_flow():
    return render_template('cash_flow.html')