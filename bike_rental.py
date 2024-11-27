import json
import datetime
import smtplib
import os

history = {}

def rent_bike(customer_name:str, rental_duration:int) ->dict:
    price = calculate_cost(rental_duration)
    rental = {
            customer_name :{
            "długość wynajmu" : rental_duration,
            "cena" : price
            }
        }
    rentalh = {
            customer_name :{
                "długość wynajmu" : rental_duration,
                "cena" : price,
                "Status" : "Dodano"
                } 
        }
    history.update(rentalh)
    save_rental(rental)
    return f"Dziękujemu {customer_name} za zarezerwowanie roweru na {rental_duration} godzin."

def calculate_cost(rental_duration:int) ->str:
    return f"{10+(rental_duration-1)*5}zł"


def save_rental(rental:dict) ->dict:
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

def cancel_rental(customer_name:str) ->dict:
    with open("data/rentals.json", encoding="utf-8") as f:
            data = json.load(f)
    if customer_name in data:
        cancelh = {
                customer_name : {
                    "status" : "Anulowano"
                    }
            }
        history.update(cancelh)
        del data[customer_name]
        print("Rezerwacja została pomyślnie anulowana")
        with open("data/rentals.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)
    else:
        print("Podana rezerwacja nie istnieje")
    
def send_rental_invoice_email(customer_email:str, rental_details:str):
    from email.message import EmailMessage

    msg= EmailMessage()
    msg.set_content("Dokonano rezerwacji")
    msg["Subject"]="Rental Bike"
    msg["From"]="Rental Bike Corporation"
    msg["To"]=""

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("", "")
    server.send_message(msg)
    server.quit

def generate_daily_report():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    with open(f"data/daily_report_{current_date}.json", "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False)

def main(n):
    while n != "exit":
        n = str(input("podaj co chcesz zrobić: "))
        match n:
            case "rent":
                rental_duraction = int(input("Ilość godzin: "))
                if rental_duraction == 0:
                    print("Podaj odpowiedznią ilość godzin")
                else:
                    customer_name = str(input("podaj imię klienta: "))
                    customer_email = str(input("Podaj Email: "))
                    rental_details = rent_bike(customer_name, rental_duraction)
                    send_rental_invoice_email(customer_email,rental_details)
            case "load":
                load_rentals()
            case "cancel":
                if os.path.exists("data/rentals.json"):
                    customer_name = str(input("Podaj imię klienta: "))
                    cancel_rental(customer_name)
                else:
                    print("Obecnie nie ma żadnych rezerwacji")
            case _:
                print("Podaj odpowiednią instrukcję")
    else:
        print("Dowidzenia")
        generate_daily_report()

main(0)