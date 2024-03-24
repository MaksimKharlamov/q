import flask
from flask import jsonify, request, make_response

from . import db_session
from .jobs import Job

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Job).all()
    return jsonify({'jobs': [item.to_dict() for item in jobs]})


@blueprint.route('/api/jobs/<job_id>')
def get_job(job_id):
    db_sess = db_session.create_session()
    try:
        job = db_sess.query(Job).get(job_id)
        return jsonify(job.to_dict())
    except Exception as e:
        return "неверный параметр"


@blueprint.route('/api/jobs', methods=['POST'])
def create_job():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in
                 ['team_leader', 'job', 'work_size', 'collaborators', 'is_finished']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    db_sess = db_session.create_session()
    job = Job(
        team_leader=request.json['team_leader'],
        job=request.json['job'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators'],
        is_finished=request.json['is_finished'],
    )
    db_sess.add(job)
    db_sess.commit()
    return jsonify({'id': job.id})


@blueprint.route('/api/jobs/<job_id>', methods=['DELETE'])
def delete_news(job_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Job).get(job_id)
    if not job:
        return make_response(jsonify({'error': 'Not found'}), 404)
    db_sess.delete(job)
    db_sess.commit()
    return jsonify({'success': 'OK'})
