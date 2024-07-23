from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
 
db = SQLAlchemy()
 
class BusInfo(db.Model):
    __tablename__ = 'BusInfo'
    busNumber = db.Column(db.Integer, primary_key=True)
    busSource = db.Column(db.String, nullable=False)
    busDestination= db.Column(db.String, nullable=False)
    arrivalTime = db.Column(db.String, nullable=False)
    remainingSeats = db.Column(db.Integer, nullable=False, default = 40)
    fare = db.Column(db.Integer, nullable=False, default = 200)
 
    def __repr__(self):
        return f"{self.busNumber}, {self.busSource}, {self.busDestination}, {self.arrivalTime}, {self.remainingSeats}, {self.fare}"
 
 
class TicketInfo(db.Model):
    __tablename__ = 'TicketInfo'
    ticketId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    busNumber = db.Column(db.ForeignKey('BusInfo.busNumber'), nullable=False)
    phoneNumber = db.Column(db.ForeignKey('UserInfo.phoneNumber'), unique=True, nullable=False)
    ticketQuantity = db.Column(db.Integer, nullable=False)
    seatNumber = db.Column(db.Integer, nullable=False)
 
    def __repr__(self):
        return f"{self.ticketId}, {self.busNumber}, {self.phoneNumber}, {self.ticketQuantity}, {self.seatNumber}"
 
    
class UserInfo(db.Model):
    __tablename__ = 'UserInfo'
    userName = db.Column(db.Integer, nullable=False)
    phoneNumber = db.Column(db.Integer, primary_key=True)
    emailId = db.Column(db.String, unique=True, nullable=False)
    ticketId = db.Column(db.ForeignKey('TicketInfo.ticketId'), nullable=False)
 
    def __repr__(self):
        return f"{self.userName}, {self.phoneNumber}, {self.emailId}, {self.ticketId}"