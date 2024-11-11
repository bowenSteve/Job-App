from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_migrate import Migrate

app = Flask(__name__)
CORS(app)


app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:password@localhost:5432/job_app"


from models import db, JobPosting
migrate = Migrate(app, db)
db.init_app(app)

@app.route('/get_jobpostings', methods=['POST'])
def get_jobpostings():
    jobs = JobPosting.query.all()
    jobs_list = [job.to_dict() for job in jobs]
    return jsonify(jobs_list)



if __name__  == '__main__':
    app.run(debug = True)