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


@app.route('/distribution')
def distribution():
    staff = [
        "Ридли Скотт",
        "Энди Уир",
        "Марк Уотни",
        "Венката Капур",
        "Тедди Сандерс",
        "Шон Бин",
    ]
    return render_template("staff.html", staff=staff)


@app.route('/table/<sex>/<age>')
def table(sex, age):
    images = ["https://img.razrisyika.ru/img/60/1200/237793-udivitelnye-raskraski-prishelcev-dlya-detey.jpg",
              "https://narisyu.cdnbro.com/posts/724536-monstrik-raskraska-36.jpg",
              "https://coloringpagesonly.com/wp-content/uploads/2021/12/Aliens-Toy-Story-Drawing.png",
              "https://raskrasil.com/wp-content/uploads/Raskrasil.com-Alien-8-631x900.jpg"]
    index = 0
    colors = ["#55f", "#f55", "#00f", "#f00"]
    if int(age) > 21:
        index += 2
    if sex == "female":
        index += 1
    return render_template("table.html", color=colors[index], image=images[index])


@app.route('/astronaut_selection')
def form():
    return render_template('form.html')


@app.route('/answer', methods=['POST', 'GET'])
@app.route('/auto_answer', methods=['POST', 'GET'])
def answer():
    d = {}
    d['title'] = "Анкета"
    d['name'] = request.form['name']
    d['surname'] = request.form['surname']
    d['education'] = request.form['education']
    d['profession'] = request.form['profession']
    d['sex'] = request.form['sex']
    d['motivation'] = request.form['motivation']
    d['ready'] = True if request.form.get('ready', 0) else False
    return render_template("auto_answer.html", **d)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
