from config import db, app
    
class NoteData(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    note = db.Column(db.Text, unique=False, nullable=False)

    def to_json(self):
        return {
            "ID": self.id,
            "noteData": self.note,
        }