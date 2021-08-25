from flask import Flask, render_template, session, redirect, request
from flask_socketio import SocketIO, emit, join_room, leave_room, rooms

app = Flask(__name__)
app.config['SECRET_KEY'] = 'pwsadwda'

socket_io = SocketIO(app)

pw = {
    'awsdawd':'A-14'
}

@app.route('/')
def f1():
    if 'login' in session:
        return render_template('main.html')
    else:
        return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    pwin = request.form['PW']
    if pwin in pw:
        session['login'] = True
        session['BID'] = pw[pwin]
        return redirect('/')
    else:
        return render_template('index.html', msg='비밀번호가 일치하지 않습니다.')


if __name__ == '__main__':
    socket_io.run(app, host='0.0.0.0', port=80, debug=True)