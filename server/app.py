from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_migrate import Migrate

app = Flask(__name__)
CORS(app)


app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:password@localhost:5432/job_app"


from models import db, JobPosting
migrate = Migrate(app, db)
db.init_app(app)

@app.route('/get_jobpostings', methods=['GET'])
def get_jobpostings():
    jobs = JobPosting.query.all()
    jobs_list = [job.to_dict() for job in jobs]
    return jsonify(jobs_list), 201

@app.route('/job/<int:job_id>', methods=['GET'])
def get_job_id(job_id):
    job = JobPosting.query.get(job_id)
    if not job:
        return jsonify({'error': 'Job not found'}), 404
    return jsonify(job.to_dict()), 201

if __name__  == '__main__':
    app.run(debug = True)