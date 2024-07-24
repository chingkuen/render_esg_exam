from extensions import db

class Question(db.Model):
    __tablename__ = 'question_db'
    id = db.Column(db.Integer, primary_key=True)
    question_name = db.Column(db.String(255), nullable=False)
    question_chapter = db.Column(db.String(255), nullable=False)
    question_level = db.Column(db.String(255), nullable=False)
    question_type = db.Column(db.String(255), nullable=False)
    answer = db.Column(db.String(255), nullable=False)
    option_a = db.Column(db.String(255), nullable=False)
    option_b = db.Column(db.String(255), nullable=False)
    option_c = db.Column(db.String(255), nullable=False)
    option_d = db.Column(db.String(255), nullable=False)
    answer_detail = db.Column(db.String(255))
    
