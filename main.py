from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs = [{
  'id': 1,
  'title': "Data Analyst",
  'location': "Delhi, India",
  'salary': 'Rs. 12,22,223'
}, {
  'id': 2,
  'title': "Data Engineer",
  'location': "Hyderabad, India",
  'salary': 'Rs. 12,00,00'
}, {
  'id': 3,
  'title': "Data Scientist",
  'location': "Bangalore, India",
  'salary': 'Rs. 15,22,223'
}, {
  'id': 4,
  'title': "Business Analyst",
  'location': "Delhi, India",
  'salary': 'Rs. 32,22,223'
}]

@app.route('/')
def hello_world():
  return render_template('hello.html', jobs=jobs)

@app.route('/api/jobs')
def job_list():
  return jsonify(jobs)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
