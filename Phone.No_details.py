import phonenumbers
from phonenumbers import timezone,geocoder,carrier  

Ph_No = input("Enter your Phone No,with +__  : ")

phone = phonenumbers.parse(Ph_No)
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_valid_number(phone , "en")  #en is used for the language english
registration = geocoder.description_for_number(phone,"en")

print(phone)
print(time)
print(car)
print(registration)

print("---Details Captured---")
print("HELLO WORLD")