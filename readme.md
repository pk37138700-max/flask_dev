pip install flask     -flask install

create a file  app.py


create one static folder for css

create one templates folder for html files 


in app.py 

import flask
 
 app = Flask(__name__)


 create route 

@app.route('/')
def index():
    return render_template('index.html')

    @app.route('/home')
def home():
    return render_template('home.html')




link with html and css
   <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">




connect python and mysql 
pip install flask mysql-connector-python



