from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/index', methods=['get', 'post'])
def index():
    imt = 0
    if request.method == 'GET':
        m = request.args.get('p')
        h = request.args.get('q')
    if h and m:
        if h.isdigit() and m.isdigit():
            imt = int(m)/(int(h)/100)**2
        else:
            imt = -1
    return render_template('index.html', imt=round(imt,2))


@app.route('/trap')
def trap():
    return render_template('trap.html')


app.run(debug=True)
