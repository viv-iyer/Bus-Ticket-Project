from app import db, app
from model import BusInfo, UserInfo, TicketInfo
from datetime import datetime


def list_all_users():
    users = UserInfo.query.all()
    return users

def list_all_buses():
    buses = BusInfo.query.all()
    return buses

def list_all_ticket():
    tickets = TicketInfo.query.all()
    return tickets

def add_bus(bus):
    buss = BusInfo(**bus)
    db.session.add(buss)
    db.session.commit()
    return list_all_buses()

def add_ticket(ticket):
    ticket = TicketInfo(**ticket)
    db.session.add(ticket)
    db.session.commit()
    return list_all_ticket()

def add_user(user):
    # user = UserInfo(**user)
    db.session.add(UserInfo(**user))
    db.session.commit()
    return list_all_users()


if __name__ == "__main__":
    with app.app_context():
        # initialise_db()
        users = [{"userName": "JJ", "phoneNumber": "9865253278", "emailId": "abc@gmail.com", "ticketId":"33"}]
        tickets = [{"ticketId":"33", "busNumber":"4", "phoneNumber": "9865253278", "ticketQuantity":"3"}]
        buss = [{"busNumber":"4", "busSource":"Mumbai","busDestination":"Pune"}]

        # for user in users:
        #     print(add_user(user))

        # for ticket in tickets:
        #     print(add_ticket(ticket))

        # for bus in buss:
        #     print(add_bus(bus))

        print(list_all_buses())
        print(list_all_ticket())
        print(list_all_users())



        

