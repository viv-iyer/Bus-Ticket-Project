from flask import Flask, render_template, request, redirect, send_from_directory
from model import db, TicketInfo, UserInfo, BusInfo
# from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import db_query

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ticket.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def home():
    busInfo = BusInfo.query.all()
    print(busInfo)
    return render_template("index.html", busInfo = busInfo)



@app.route('/book', methods =["POST"])
def book_ticket():
    userName = request.form["userName"]
    phoneNumber = request.form["phoneNumber"]
    emailId = request.form["emailId"]
    ticketQuantity = request.form["ticketQuantity"]
    busNumber = request.form["busNumber"]

    ticketInfo = TicketInfo( phoneNumber=phoneNumber, busNumber=busNumber, ticketQuantity=ticketQuantity)

    # add ticket to DB
    ticketId = db_query.add_ticket(ticket=ticketInfo)

    # adding user 
    userInfo = UserInfo(userName=userName, phoneNumber=phoneNumber, emailId=emailId, ticketId=ticketId)

    db_query.add_user(userInfo)

    # changing remaining tickets in BusInfo table
    busInfo = BusInfo.query.filter_by(busNumber=busNumber).first()
    busInfo.remainingTickets = busInfo.remainingTickets - ticketQuantity
    db.session.commit()
    # return redirect("/")


    return render_template("index.html", TicketInfo)









    


if __name__ == "__main__":
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)


