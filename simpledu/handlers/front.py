from flask import Blueprint,render_template
from simpledu.models import Course
from simpledu.forms import LoginForm,RegisterForm
from flask import request,current_app

front=Blueprint('front',__name__)

@front.route('/')
def index():
    page=request.args.get('page',default=1,type=int)
    pagination=Course.query.paginate(
            page=page,
            per_page=current_app.config['INDEX_PER_PAGE'],
            error_out=False)
    return render_template('index.html',pagination=pagination)
@front.route('/login')
def login():
    form=LoginForm()
    return render_template('login.html',form=form)

@front.route('/register')
def register():
    form=RegisterForm()
    return render_template('register.html',form=form)
