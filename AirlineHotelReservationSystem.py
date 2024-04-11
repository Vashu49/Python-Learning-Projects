#!/usr/bin/env python
# coding: utf-8

# In[1]:


class ReservationSystem:
    def __init__(self):
        self.airline_seats = {'first_class': 10, 'coach': 50}
        self.hotel_rooms = {'standard': 20, 'penthouse_suite': 5}
    
    def display_available_seats(self):
        print("\nAirline Seats Available:")
        for seat_type, count in self.airline_seats.items():
            print(f"{seat_type}: {count}")
    
    def display_available_rooms(self):
        print("\nHotel Rooms Available:")
        for room_type, count in self.hotel_rooms.items():
            print(f"{room_type}: {count}")
    
    def book_airline_seat(self, seat_type):
        if seat_type not in self.airline_seats or self.airline_seats[seat_type] == 0:
            print(f"Sorry, {seat_type} is not available.")
            return
        
        self.airline_seats[seat_type] -= 1
        print(f"Successfully booked {seat_type} seat.")
    
    def book_hotel_room(self, room_type):
        if room_type not in self.hotel_rooms or self.hotel_rooms[room_type] == 0:
            print(f"Sorry, {room_type} is not available.")
            return
        
        self.hotel_rooms[room_type] -= 1
        print(f"Successfully booked {room_type} room.")
    
    def cancel_airline_seat(self, seat_type):
        if seat_type not in self.airline_seats or self.airline_seats[seat_type] == 10:
            print(f"No booking found for {seat_type}.")
            return
        
        self.airline_seats[seat_type] += 1
        print(f"Successfully canceled {seat_type} seat.")
    
    def cancel_hotel_room(self, room_type):
        if room_type not in self.hotel_rooms or self.hotel_rooms[room_type] == 20:
            print(f"No booking found for {room_type}.")
            return
        
        self.hotel_rooms[room_type] += 1
        print(f"Successfully canceled {room_type} room.")

if __name__ == "__main__":
    system = ReservationSystem()
    
    while True:
        print("\nMenu:")
        print("1. Display available airline seats")
        print("2. Display available hotel rooms")
        print("3. Book airline seat")
        print("4. Book hotel room")
        print("5. Cancel airline seat")
        print("6. Cancel hotel room")
        print("7. Exit")
        
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            system.display_available_seats()
        elif choice == '2':
            system.display_available_rooms()
        elif choice == '3':
            seat_type = input("Enter seat type (first_class/coach): ")
            system.book_airline_seat(seat_type)
        elif choice == '4':
            room_type = input("Enter room type (standard/penthouse_suite): ")
            system.book_hotel_room(room_type)
        elif choice == '5':
            seat_type = input("Enter seat type to cancel (first_class/coach): ")
            system.cancel_airline_seat(seat_type)
        elif choice == '6':
            room_type = input("Enter room type to cancel (standard/penthouse_suite): ")
            system.cancel_hotel_room(room_type)
        elif choice == '7':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# In[2]:


class ReservationSystem:
    def __init__(self):
        # Initialize the available airline seats and hotel rooms
        self.airline_seats = {'first_class': 10, 'coach': 50}
        self.hotel_rooms = {'standard': 20, 'penthouse_suite': 5}
        
        # Define the rates for each section
        self.airline_rates = {'first_class': 500, 'coach': 200}
        self.hotel_rates = {'standard': 100, 'penthouse_suite': 500}
    
    def display_available_seats(self):
        print("\nAirline Seats Available:")
        for seat_type, count in self.airline_seats.items():
            print(f"{seat_type.capitalize()}: {count} seats - ${self.airline_rates[seat_type]} per seat")
    
    def display_available_rooms(self):
        print("\nHotel Rooms Available:")
        for room_type, count in self.hotel_rooms.items():
            print(f"{room_type.capitalize()}: {count} rooms - ${self.hotel_rates[room_type]} per night")
    
    def book_airline_seat(self, seat_type):
        if seat_type not in self.airline_seats or self.airline_seats[seat_type] == 0:
            print(f"Sorry, {seat_type} is not available.")
            return
        
        self.airline_seats[seat_type] -= 1
        print(f"Successfully booked {seat_type} seat for ${self.airline_rates[seat_type]}.")
    
    def book_hotel_room(self, room_type):
        if room_type not in self.hotel_rooms or self.hotel_rooms[room_type] == 0:
            print(f"Sorry, {room_type} is not available.")
            return
        
        self.hotel_rooms[room_type] -= 1
        print(f"Successfully booked {room_type} room for ${self.hotel_rates[room_type]} per night.")
    
    def cancel_airline_seat(self, seat_type):
        if seat_type not in self.airline_seats:
            print(f"No booking found for {seat_type}.")
            return
        
        self.airline_seats[seat_type] += 1
        print(f"Successfully canceled {seat_type} seat.")
    
    def cancel_hotel_room(self, room_type):
        if room_type not in self.hotel_rooms:
            print(f"No booking found for {room_type}.")
            return
        
        self.hotel_rooms[room_type] += 1
        print(f"Successfully canceled {room_type} room.")

if __name__ == "__main__":
    system = ReservationSystem()
    
    while True:
        print("\nMenu:")
        print("1. Display available airline seats")
        print("2. Display available hotel rooms")
        print("3. Book airline seat")
        print("4. Book hotel room")
        print("5. Cancel airline seat")
        print("6. Cancel hotel room")
        print("7. Exit")
        
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            system.display_available_seats()
        elif choice == '2':
            system.display_available_rooms()
        elif choice == '3':
            seat_type = input("Enter seat type (first_class/coach): ").lower()
            system.book_airline_seat(seat_type)
        elif choice == '4':
            room_type = input("Enter room type (standard/penthouse_suite): ").lower()
            system.book_hotel_room(room_type)
        elif choice == '5':
            seat_type = input("Enter seat type to cancel (first_class/coach): ").lower()
            system.cancel_airline_seat(seat_type)
        elif choice == '6':
            room_type = input("Enter room type to cancel (standard/penthouse_suite): ").lower()
            system.cancel_hotel_room(room_type)
        elif choice == '7':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# In[ ]:




