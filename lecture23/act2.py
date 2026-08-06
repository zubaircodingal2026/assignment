import random

class HotelBusiness:
    # Create Constructor (special method )
    def __init__(self, name, floors, price_night):
        self.name = name
        self.floors = floors
        self.price_night = price_night

    # custom methods
    def calculate_cost(self, days):
        return days * self.price_night

    def displayBookingDetails(self, days):
        self.total_price = self.calculate_cost(days) 
        print("Your booking is confirmed..")
        print("Here are the details of your booking...")
        print("#" * 30)
        print(f"\nHotel Name   : {self.name}")
        print(f"Floor Number : {random.randint(1, int(self.floors))}") 
        print(f"Total Price  : ₹{self.total_price}") 


# Create the hotel object
hotel_dhaka = HotelBusiness("Dhaka Taj Hotel", 20, 10000)

# Take the number of days from the user
try:
    print("\nWelcome to Taj Group of Hotels...")
    print("*" * 30)
    user_days = int(input("Enter the number of days you want to stay: "))
    
    # Pass the user input into the method
    hotel_dhaka.displayBookingDetails(user_days)
except ValueError:
    print("Please enter a valid whole number for the days.")
