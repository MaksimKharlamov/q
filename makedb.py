import datetime

from data import db_session
from data.jobs import Job
from data.users import User

db_session.global_init("db/mars_explorers.db")
db_sess = db_session.create_session()
u1 = User(name="Ridley", surname="Scott",
          age=21, position="captain",
          speciality="engineer", address="module_1",
          email="1@ya.ru", hashed_password="password1")

u2 = User(name="John", surname="Bryan",
          age=52, position="officer",
          speciality="biologist", address="module_2",
          email="2@ya.ru", hashed_password="password2")

u3 = User(name="Ryan", surname="Ingram",
          age=24, position="sergeant",
          speciality="chemist", address="module_3",
          email="3@ya.ru", hashed_password="password3")

u4 = User(name="Mark", surname="Howard",
          age=37, position="major",
          speciality="physicist", address="module_4",
          email="4@ya.ru", hashed_password="password4")

j1 = Job(team_leader=1, job="Deployment of residential modules 1 and 2",
         work_size=15, collaborators="2, 3",
         start_date=datetime.datetime.now(), is_finished=False)

j2 = Job(team_leader=2, job="Exploration of mineral resources",
         work_size=15, collaborators="4, 3",
         start_date=datetime.datetime.now(), is_finished=False)

j3 = Job(team_leader=3, job="Development of a management system",
         work_size=25, collaborators="5",
         start_date=datetime.datetime.now(), is_finished=False)

db_sess.add(u1)
db_sess.add(u2)
db_sess.add(u3)
db_sess.add(u4)
db_sess.add(j1)
db_sess.add(j2)
db_sess.add(j3)
db_sess.commit()
