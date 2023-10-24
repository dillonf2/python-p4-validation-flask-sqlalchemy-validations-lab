from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

    @validates('name')
    def validate_author(self, key, address):
        if address == '':
            raise ValueError("Authors must have a name.")
        return address

    @validates('phone_number')
    def validate_phone_number(self, key, address):
        if len(address) != 10:
            raise ValueError("Phone numbers must be 10 digits long.")
        return address

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'

    @validates('title')
    def validate_title(self, key, title):
        if title == '':
            raise ValueError("Posts must have a title.")

        clickbait_keywords = ["Won't Believe", "Secret", "Top", "Guess"]
        if not any(keyword in title for keyword in clickbait_keywords):
            raise ValueError("Title must contain at least one clickbait keyword.")
        return title
        
    @validates('content')
    def validate_content(self, key, address):
        if len(address) < 250:
            raise ValueError("Content must be at least 250 characters long.")
        return address

    @validates('summary')
    def validate_summary(self, key, summary):
        if len(summary) >= 250:
            raise ValueError("Post summaries must be shorter than 250 characters.")
        return summary
    
    @validates('category')
    def validate_category(self, key, address):
        if address != "Fiction" and address != "Non-Fiction":
            raise ValueError("Post category must be either Fiction or Non-Fiction.")
        return address

