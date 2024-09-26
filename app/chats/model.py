from app import db

class Chats(db.Model):
    __tablename__ = 'chats'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    session_id = db.Column(db.String, nullable=True)
    created_at = db.Column(db.DateTime, nullable=True)
    model_name = db.Column(db.String, nullable=True)

    def __repr__(self):
        return f"<Chats {self.id}>"

    # Convert object to dictionary (useful for JSON serialization)
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'session_id': self.session_id,
            'created_at': self.created_at,
            'model_name': self.model_name
        }
