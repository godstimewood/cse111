# I added a code to ask the user if want to buy the tire,
# and stores their phone number in the volume.txt file if they say "yes".

import math
from datetime import datetime

width = int(input("Enter the width of the tire in mm (ex 205:) "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60:) "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15:) "))

volume = (math.pi * (width ** 2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) /10000000000
volume_rounded = round(volume, 2)

print(f"The approximate volume is {volume_rounded} litres")

current_date = datetime.now().strftime("%Y-%m-%d")

buy_tire = input("Would you like to buy tires with these diamensions? (yes/no): ").strip().lower()
phone_number = ""

if buy_tire == "yes":
    phone_number = input("Please enter your phone number: ").strip()

with open("volumes.txt", "at") as file:
    if phone_number:
        file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume_rounded}, {phone_number}\n")
    else:
        file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume_rounded}\n")