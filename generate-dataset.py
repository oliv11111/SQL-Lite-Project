import csv
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Define the number of customers
num_customers = 10

# Create a list to hold customer data
customers = []

# Generate customer data
for _ in range(num_customers):
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = f"{first_name.lower()}.{last_name.lower()}@example.com"  # Create email in the desired format
    customers.append({
        "first_name": first_name,
        "last_name": last_name,
        "gender": random.choice(["M", "F"]),
        "dob": fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d'),
        "email": email,
        "phone_number": fake.phone_number(),
        "address": fake.street_address(),
        "city": fake.city(),
        "state": fake.state_abbr(),
    })

# Specify the CSV file name
csv_file = 'customers.csv'

# Write the customer data to a CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=customers[0].keys())
    writer.writeheader()  # Write the header
    writer.writerows(customers)  # Write the customer data

print(f"Generated {num_customers} customer entries and saved to {csv_file}.")
