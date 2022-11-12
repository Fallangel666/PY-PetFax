from flask import ( Blueprint, render_template, request ) 

bp = Blueprint('fact',
                __name__, 
                url_prefix="/facts")

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form)
    else:
        return 'Fact index works'   

@bp.route('/new')
def new():
    return render_template('facts/index.html')