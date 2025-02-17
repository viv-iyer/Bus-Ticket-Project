from app import db, app
from model import BusInfo, UserInfo, TicketInfo
from datetime import datetime
 
def list_all_users():
    users = UserInfo.query.all()
    return users
 
def list_all_buses():
    buses = BusInfo.query.all()
    return buses
 
def list_all_tickets():
    tickets = TicketInfo.query.all()
    return tickets
 
def add_bus(bus):
    buses = BusInfo(**bus)
    db.session.add(buses)
    db.session.commit()
    return list_all_buses()
 
def add_ticket(ticket):
    ticket = TicketInfo(**ticket)
    db.session.add(ticket)
    db.session.commit()
    return list_all_tickets
 
def add_user(user):
    user = UserInfo(**user)
    db.session.add(user)
    db.session.commit()
    return list_all_users
 
def get_by_ticket_no(ticketId):
    return db.session.get(TicketInfo, ticketId)
 
def delete_ticket(ticketId):
    ticket = get_by_ticket_no(ticketId)
    db.session.delete(ticket)
    db.session.commit()
 
if __name__ == "__main__":
    with app.app_context():
        # initialise_db()
        users = [{"userName": "John", "phoneNumber": "9865253278", "emailId": "abc@gmail.com", "ticketId":"1"}]
        tickets = [{"busNumber":"1", "phoneNumber": "9865253270", "ticketQuantity":"1", "seatNumber":"5"}]
        buses = [{"busNumber":"1", "busSource":"Mumbai","busDestination":"Pune", "remainingSeats":"45", "arrivalTime":"9 AM"}, {"busNumber":"2", "busSource":"Mumbai","busDestination":"Pune", "remainingSeats":"45", "arrivalTime":"5 PM"}, {"busNumber":"3", "busSource":"Pune","busDestination":"Mumbai", "remainingSeats":"45", "arrivalTime":"9 AM"}, {"busNumber":"4", "busSource":"Pune","busDestination":"Mumbai", "remainingSeats":"45", "arrivalTime":"5 PM"}]
 
        # for user in users:
        #     print(add_user(user))
 
        # for ticket in tickets:
        #     print(add_ticket(ticket))
 
        for bus in buses:
            print(add_bus(bus))
 
        # delete_ticket(33)
 
        
 
        # print(list_all_buses())
        # print(list_all_tickets())
        # print(list_all_users())