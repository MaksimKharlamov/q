from flask import *
from flask_login import *

from data import db_session
from data.jobs import Job
from data.loginform import LoginForm
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandex_lyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)
db_session.global_init('db/mars_explorers.db')


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/')
def q():
    db_sess = db_session.create_session()
    data = db_sess.query(Job).all()
    jobs = []
    for i in data:
        job = [''] * 6
        job[-1] = i.id
        job[0] = i.job
        leader = db_sess.query(User).filter(User.id == i.team_leader).first()
        job[1] = leader.surname + ' ' + leader.name
        job[2] = f"{i.work_size} hours"
        job[3] = i.collaborators
        job[4] = "Is " + ("not " if not i.is_finished else '') + "finished"
        jobs.append(job)
    print(jobs)
    return render_template('jobs.html', jobs=jobs)


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


def main():
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
