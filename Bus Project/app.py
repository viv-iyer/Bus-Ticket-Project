from flask import Flask, render_template, request, redirect, send_from_directory, url_for
from model import db, TicketInfo, UserInfo, BusInfo
# from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# import db_query
 
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
 
 
 
@app.route('/', methods =["POST"])
def book_ticket():
    userName = request.form["userName"]
    phoneNumber = request.form["phoneNumber"]
    emailId = request.form["emailId"]
    ticketQuantity = int(request.form["ticketQuantity"])
    busNumber = int(request.form["busNumber"])
 
    # Create UserInfo entry
    userInfo = UserInfo.query.filter_by(phoneNumber=phoneNumber).first()
 
    # Create TicketInfo entry
    ticketInfo = TicketInfo(phoneNumber=phoneNumber, busNumber=busNumber, ticketQuantity=ticketQuantity, seatNumber=1)  # Assuming seatNumber is handled elsewhere
    db.session.add(ticketInfo)
 
    # changing remaining tickets in BusInfo table
    busInfo = BusInfo.query.filter_by(busNumber=busNumber).first()
    busInfo.remainingSeats -= ticketQuantity
    db.session.commit()
    
    return redirect(url_for('ticket_details', ticketId=ticketInfo.ticketId))
 
@app.route('/ticket/<int:ticketId>')
def ticket_details(ticketId):
    ticket = TicketInfo.query.get(ticketId)
    bus = BusInfo.query.filter_by(busNumber=ticket.busNumber).first()
    return render_template("ticket.html", ticket=ticket, bus=bus)
 
@app.route('/cancel/<int:ticketId>', methods=["POST"])
def cancel_ticket(ticketId):
    ticket = TicketInfo.query.get(ticketId)
    if ticket:
        busInfo = BusInfo.query.filter_by(busNumber=ticket.busNumber).first()
        busInfo.remainingSeats += ticket.ticketQuantity
        db.session.delete(ticket)
        db.session.commit()
    return redirect(url_for('home'))
 
if __name__ == "__main__":
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)