from flask import Blueprint, render_template

views_bp = Blueprint('views', __name__) #initialize blueprint

# Responsible for routing and connecting backend and frontend.
# in home.html line 11, you could see being used 'views.extract'
@views_bp.route('/') 
def home():
    return render_template('home.html')
