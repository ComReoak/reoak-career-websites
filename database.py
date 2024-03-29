from sqlalchemy import create_engine, text
import os

db_connection_string = my_secret = os.environ['SECRET_DB_CONNECTION_CODE']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
    return jobs


def load_job_from_db_with_id(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs where id= :val"),
                          {'val': id})
    job_row = result.all()

    if len(job_row) == 0:
      return None
    else:
      return job_row[0]._asdict()


def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    pass
