from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db_with_id, add_application_to_db

app = Flask(__name__)


@app.route('/')
def hello_world():
  jobs = load_jobs_from_db()
  return render_template('hello.html', jobs=jobs)


@app.route('/api/jobs')
def job_list():
  jobs = load_jobs_from_db()
  return jsonify(jobs)


@app.route('/job/<id>')
def show_job(id):
  job = load_job_from_db_with_id(id)
  if not job:
    return "Not Found", 404
  return render_template('jobpage.html', job=job)


@app.route('/job/<id>/apply', methods=['post'])
def apply_to_job(id):
  data = request.form
  job = load_job_from_db_with_id(id)
  #Store data into database
  add_application_to_db(id, data)
  return render_template('applicationSubmitted.html', application=data, job=job)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
