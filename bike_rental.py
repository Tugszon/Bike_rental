import json
import datetime
import smtplib
import os

# def rent_bike(customer_name:str, rental_duration:int):

def calculate_cost(rental_duration:int) ->str:
    return f"{10+(rental_duration-1)*5}zł"

# def save_rental(rental):
#     json.dumps(x)

# def load_rentals():
#     None

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
                customer_name = input("podaj imię klienta: ")
            case _:
                print("Podaj odpowiednią instrukcję")

main(0)