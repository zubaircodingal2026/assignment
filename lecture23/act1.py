#blueprint of hotel
class HotelBusiness:
    #properties of hotelbusiness class
    name = "Taj bangla"
    floor = "20"
    price_night = "10,000rs"
    print(f"this is a HotelBusiness Blueprint")
    
    
#object of HotelBusiness class
Taj_kolkata = HotelBusiness()
Taj_mumbai = HotelBusiness()
Taj_dhaka = HotelBusiness()

#Accessing properties of HotelBusiness class using its objects
print(Taj_dhaka.name)
print(Taj_dhaka.floor)
print(Taj_dhaka.price_night)
