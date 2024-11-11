from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum
from datetime import datetime

db = SQLAlchemy()

class JobPosting(db.Model):
    __tablename__ = 'job_postings'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    responsibilities = db.Column(db.Text, nullable=False)
    requirements = db.Column(db.Text, nullable=False)
    application_method = db.Column(Enum('email', 'website', name='application_method_enum'), nullable=False)
    application_details = db.Column(db.String(200), nullable=False)  # stores email or website URL
    posted_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    deadline = db.Column(db.DateTime, nullable=False)
    
    def __repr__(self):
        return f"<JobPosting {self.title}>"
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "responsibilities": self.responsibilities,
            "requirements": self.requirements,
            "application_method": self.application_method,
            "application_details": self.application_details,
            "posted_date": self.posted_date.isoformat(),
            "deadline": self.deadline.isoformat(),
        }
