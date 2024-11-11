from datetime import datetime, timedelta
from models import db, JobPosting

# Sample job data
jobs = [
    JobPosting(
        title="Software Engineer",
        responsibilities="Develop and maintain software applications.",
        requirements="3+ years of experience in software development. Knowledge of Python and Flask.",
        application_method="email",
        application_details="jobs@techcompany.com",
        posted_date=datetime.utcnow(),
        deadline=datetime.utcnow() + timedelta(days=30)
    ),
    JobPosting(
        title="Data Analyst",
        responsibilities="Analyze data trends and create reports.",
        requirements="2+ years of experience in data analysis. Proficiency in SQL and Excel.",
        application_method="website",
        application_details="https://techcompany.com/careers",
        posted_date=datetime.utcnow(),
        deadline=datetime.utcnow() + timedelta(days=45)
    ),
    JobPosting(
        title="Product Manager",
        responsibilities="Manage product lifecycle and coordinate with cross-functional teams.",
        requirements="Experience in product management and agile methodologies.",
        application_method="email",
        application_details="careers@innovate.com",
        posted_date=datetime.utcnow(),
        deadline=datetime.utcnow() + timedelta(days=60)
    ),
    JobPosting(
        title="UX/UI Designer",
        responsibilities="Design user interfaces and improve user experience.",
        requirements="Portfolio of previous UX/UI design work. Familiarity with Figma and Sketch.",
        application_method="website",
        application_details="https://innovate.com/jobs",
        posted_date=datetime.utcnow(),
        deadline=datetime.utcnow() + timedelta(days=30)
    ),
    JobPosting(
        title="Project Coordinator",
        responsibilities="Coordinate projects and assist project managers.",
        requirements="Organizational skills and experience in project management.",
        application_method="email",
        application_details="hr@companysolutions.com",
        posted_date=datetime.utcnow(),
        deadline=datetime.utcnow() + timedelta(days=20)
    ),
    JobPosting(
        title="Marketing Specialist",
        responsibilities="Develop and implement marketing campaigns.",
        requirements="2+ years of experience in marketing and content creation.",
        application_method="website",
        application_details="https://companysolutions.com/jobs",
        posted_date=datetime.utcnow(),
        deadline=datetime.utcnow() + timedelta(days=40)
    ),
    JobPosting(
        title="Sales Representative",
        responsibilities="Sell products and services to potential clients.",
        requirements="Experience in sales and excellent communication skills.",
        application_method="email",
        application_details="sales@retailco.com",
        posted_date=datetime.utcnow(),
        deadline=datetime.utcnow() + timedelta(days=15)
    ),
    JobPosting(
        title="Customer Service Associate",
        responsibilities="Assist customers with inquiries and resolve issues.",
        requirements="Strong communication skills and experience in customer service.",
        application_method="website",
        application_details="https://retailco.com/careers",
        posted_date=datetime.utcnow(),
        deadline=datetime.utcnow() + timedelta(days=25)
    ),
    JobPosting(
        title="Network Engineer",
        responsibilities="Manage network infrastructure and troubleshoot issues.",
        requirements="Experience with network protocols and security.",
        application_method="email",
        application_details="jobs@technetwork.com",
        posted_date=datetime.utcnow(),
        deadline=datetime.utcnow() + timedelta(days=35)
    ),
    JobPosting(
        title="Content Writer",
        responsibilities="Write articles, blogs, and content for the website.",
        requirements="Proficiency in English and experience in content creation.",
        application_method="website",
        application_details="https://contentco.com/jobs",
        posted_date=datetime.utcnow(),
        deadline=datetime.utcnow() + timedelta(days=50)
    )
]

# Function to seed the database
def seed_jobs():
    db.session.bulk_save_objects(jobs)
    db.session.commit()
    print("Database has been seeded with job postings.")

# Run the seeding function
if __name__ == "__main__":
    from app import app  # Assuming the main app file is named app.py
    with app.app_context():
        seed_jobs()
