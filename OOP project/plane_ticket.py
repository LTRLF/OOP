
class Controller:
    def __init__(self,name):
        self.__name = name
        self.__user_list = []
        self.__guest_list = []
        self.__promocode_list = []
        self.__flight_list = []
        self.__flightinstance_list = []
        self.__admin_list = []
        self.__airport_list = []

    def search_flight(self,departure,destination,date,total_passenger,promocode = None):
        pass
    def add_admin(self,admin):
        self.__admin_list.append(admin)


class Promocode:
    def __init__(self,code,genre):
     self.__code = code
     self.__genre = genre
     self.__exprire_date = None


class Admin:
    def __init__(self,admin_id):
        self.__admin_id 

    def add_flight(self):
        pass
    def add_promocode(self):
        pass

class Guest:
    def __init__(self,guest_id):
        self.__guest_id = guest_id

class User(Guest):
    def __init__(self,email,user_id,):
        self.__email = email
        self.__user_id = user_id
        self.__booking_list = []

class Booking:
    def __init__(self,booking_no,destination,departure,departure_date_time,arriving_date_time):
        self.__booking_no = booking_no
        self.__passenger_list = []
        self.__destination = destination
        self.__departure = departure
        self.__departure_date_time = departure_date_time
        self.__arriving_date_time = arriving_date_time
        self.__booking_status = None
        self.__payment = None 

    def update_booking_status(self):
        pass
    
    def update_payment(self):
        pass

class Payment:
    def __init__(self,user_id,amount,transaction_id,payment_genre,payment_status):
        self.__user_id = user_id
        self.__amount = amount
        self.__transaction_id = transaction_id
        self.__payment_genre = payment_genre
        self.__payment_status = payment_status

class MobileBanking(Payment):
    def __init__ (self,account):
        self.__account = account
    
    def paid_by_mobilebanking(self):
        pass
    
class Card(Payment):
    def __init__ (self,card_no):
        self.__card_no = card_no

    def paid_by_card(self):
        pass

class CreditCard(Card):
    def __init__ (self,card_limit):
        self.__card_limit = card_limit

class DebitCard(Card):
    def __init__ (self,balance):
        self.__balance = balance   

class Passenger:
    def __init__(self,gender,tel_no,name,birth_date,citizen_id,boardingpass):
        self.__gender = gender
        self.__tel_no = tel_no
        self.__name = name
        self.__birth_date = birth_date
        self.__citizen_id = citizen_id
        self.__boardingpass = boardingpass

class Boardingpass:
    def __init__(self,destination,departure,departure_date_time,arriving_date_time,gate,flight_no):
        self.__destination = destination
        self.__departure = departure
        self.__departure_date_time = departure_date_time
        self.__arriving_date_time = arriving_date_time
        self.__gate = gate
        self.__flight_no = flight_no
        self.__luggage_list = []

class Luggage:
    def __init__(self,package,luggage_id):
        self.__owner = None
        self.__package = package
        self.__luggage_id = luggage_id
    
class Airport:
    def __init__(self,name):
        self.__name = name
        self.__current_airplane_list = []

    def get_current_airplane(self):
        return self.__current_airplane_list

class Flight:
    def __init__(self,departure,destination,flight_no):
        self.__departure = departure
        self.__destination = destination
        self.__flight_no = flight_no

class Flightinstance(Flight):
    def __init__(self,flight_instance_no,departure_date_time,destination_date_time,airplane,gate,remain_seat):
        self.__flight_instance_no = flight_instance_no
        self.__departure_date_time = departure_date_time
        self.__destination_date_time = destination_date_time
        self.__airplane = airplane
        self.__gate = gate
        self.__remain_seat = remain_seat

    def seat_update(self):
        pass

class Airplane:
    def __init__(self,airplane_id,total_seat):
        self.__airplane_id = airplane_id
        self.__total_seat = total_seat

class Seat:
    def __init__(self,row,column,seat_genre,price):
        self.__row = row
        self.__column = column
        self.__seat_genre = seat_genre
        self.__price = price

class ShowSeat(Seat):
    def __init__(self,seat_no):
        self.__seat_no = seat_no
        self.__is_available = True