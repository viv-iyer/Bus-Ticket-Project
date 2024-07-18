from flask import Flask, render_template, request, redirect, send_from_directory
from model import db, TicketInfo, UserInfo, BusInfo
# from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ticket.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def hello_world():
    return render_template("index.html")
    

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    # app.run(debug=True)


