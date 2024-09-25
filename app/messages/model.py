from app import db

class Messages(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    send_date = db.Column(db.DateTime, nullable=False)
    sent_by = db.Column(db.String, nullable=False)
    documents = db.Column(db.JSON, nullable=True)
    masked_content = db.Column(db.String, nullable=True)

    def __repr__(self):
        return f"<Messages {self.id}>"

    # Convert object to dictionary (useful for JSON serialization)
    def to_dict(self):
        return {
            'id': self.id,
            'chat_id': self.chat_id,
            'content': self.content,
            'send_date': self.send_date,
            'sent_by': self.sent_by,
            'documents': self.documents,
            'masked_content': self.masked_content
        }
