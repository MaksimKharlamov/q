from flask import *

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template("base.html", title=title)


@app.route('/training/<prof>')
def training(prof):
    if 'инженер' in prof or 'строитель' in prof:
        return render_template('engineer.html')
    return render_template('science.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
