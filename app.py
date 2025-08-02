from flask import request, Flask, render_template
from webbrowser import open as surfweb

app = Flask(__name__)
def do_the_login(name):
    exec(name)
    print("hrhrh")

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)

@app.route('/copycode', methods=['GET', 'POST'])
def copycode(name=None):
    if request.method == 'POST':
        return do_the_login(name)
    else:
        return render_template('copycode.html')

@app.route('/executecommande', methods=['GET', 'POST'])
def executecommande(name=None):
    if request.method == 'POST':
        return do_the_login(name)
    else:
        return render_template('executecommande.html')

@app.route('/callapis', methods=['GET', 'POST'])
def callapis(name=None):
    if request.method == 'POST':
        return do_the_login(name)
    else:
        return render_template('callapis.html')

@app.route('/navigateweb', methods=['GET', 'POST'])
def navigateweb(name=None):
    if request.method == 'POST':
        surfweb(name)
    else:
        return render_template('navigateweb.html')

@app.route('/editcode', methods=['GET', 'POST'])
def editcode(name=None):
    if request.method == 'POST':
        return do_the_login(name)
    else:
        return render_template('editcode.html')

@app.route('/')
def openhands(name=None):
    return render_template('openhands.html')
