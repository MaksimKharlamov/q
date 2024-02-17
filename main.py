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


@app.route('/list_prof/<q>')
def list_prof(q):
    if q not in ('ol', 'ul'):
        return render_template('error.html')
    prof_list = [
        "инженер-исследователь",
        "пилот",
        "строитель",
        "экзобиолог",
        "врач",
        "инженер по терраформированию",
        "климатолог",
        "специалист по радиационной защите",
        "астрогеолог",
        "гляциолог",
        "инженер жизнеобеспечения",
        "метеоролог",
        "оператор марсохода",
        "киберинженер",
        "штурман",
        "пилот дронов",
    ]
    return render_template('list.html', prof=prof_list, q=q)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
