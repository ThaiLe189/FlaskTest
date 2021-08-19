from flask import Flask, render_template
from flask_cors import CORS, cross_origin
from flask import request

# khởi tạo flask server backend
app = Flask(__name__)

# CORS cho phép domain khác gọi
# Apply Flask CORS
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# url phải truyền tham sooskhi dùng get: http://127.0.0.1/add?a=10&b=5
@app.route('/add_use_get', methods=['POST','GET'])
@cross_origin(origin='*')
def add_use_get():

    a = request.args.get('a')
    b = request.args.get('b')

    return str(int(a)+int(b))

# Dùng post
@app.route('/add_use_post', methods=['POST'])
@cross_origin(origin='*')
def add_use_post():
    
    a = request.form['a']
    b = request.form['b']

    return str(int(a)+int(b))


@app.route('/')
def home():

    return render_template('index.html')

# start backend
if __name__ == '__main__':
    app.run(host='127.0.0.1', port='80')