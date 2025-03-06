from flask import Flask ,render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime,timezone

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///chat.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Chat(db.Model):
    idd = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(300), nullable=False)


    def __repr__(self) -> str:
        return f"{self.title} - {self.content}"



@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        chat = Chat(title=title, content=content)
        db.session.add(chat)
        db.session.commit()
    allchat=Chat.query.all()
    return render_template('index.html',allchat=allchat)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="192.168.1.4",debug=True, port=80)
