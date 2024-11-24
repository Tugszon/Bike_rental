import json
import datetime
import smtplib
import os

def rent_bike(customer_name:str, rental_duration:int):
    price = calculate_cost(rental_duration)
    rental = {
            customer_name :{
            "długość wynajmu" : rental_duration,
            "cena" : price
            }
        }
    save_rental(rental)

def calculate_cost(rental_duration:int) ->str:
    return f"{10+(rental_duration-1)*5}zł"

def save_rental(rental:dict):
    if os.path.exists("data/rentals.json"):
        with open("data/rentals.json", encoding="utf-8") as f:
            data = json.load(f)

        data.update(rental)
        with open("data/rentals.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)

    else:
        with open("data/rentals.json", "w", encoding="utf-8") as f:
            json.dump(rental, f, ensure_ascii=False)

def load_rentals():
    with open ("data/rentals.json", encoding="utf-8") as f:
        print(json.load(f))

# def cancel_rental(customer_name):
#     None

# def send_rental_invoice_email(customer_email, rental_details):
#     None

# def generate_daily_report():
#     None

def main(n):
    while n != "exit":
        n = str(input("podaj co chcesz zrobić: "))
        match n:
            case "rent":
                rental_duraction = int(input("Ilość godzin: "))
                if rental_duraction == 0:
                    print("Podaj odpowiedznią ilość godzin")
                    n = "rent"
                else:
                    customer_name = str(input("podaj imię klienta: "))
                    rent_bike(customer_name, rental_duraction)
            case "load":
                load_rentals()

            case _:
                print("Podaj odpowiednią instrukcję")

main(0)