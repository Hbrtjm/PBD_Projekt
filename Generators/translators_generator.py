import random
import faker
import csv

fake = faker.Faker('pl_PL')

polish_voivodeships = [
    "Dolnośląskie", "Kujawsko-Pomorskie", "Lubelskie", "Lubuskie", 
    "Łódzkie", "Małopolskie", "Mazowieckie", "Opolskie", 
    "Podkarpackie", "Podlaskie", "Pomorskie", "Śląskie", 
    "Świętokrzyskie", "Warmińsko-Mazurskie", "Wielkopolskie", "Zachodniopomorskie"
]

roles = [ "CEO", "CTO", "Lecturer", "Dean", "PRODean", "NoobDean", "DeansSecretary"]

languages = ["English","Polish","German","French","Esperanto"]

data = []

N = None

with open("samples_amount.txt","r") as infile:
    N = int(infile.read())

for _ in range(N):
    row = {
        "FirstName": fake.first_name(),
        "LastName": fake.last_name(),
        "Phone": fake.phone_number().replace('+48','').replace(' ',''),
        "HireDate": fake.date_between(start_date='-10y', end_date='today'),
        "Agreement": 1,
        "Languages": ','.join(random.sample(languages,random.randint(2,len(languages)-1))),
        "StreetName": fake.street_name(),
        "Region": random.choice(polish_voivodeships),  # Randomly pick a Polish voivodeship
        "CityName": fake.city(),
        "CountryName": "Poland",  # Assuming all data is in Poland for consistency
    }
    data.append(row)
    
# Write to CSV format
output_file_path = 'Translators.csv'
with open(output_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

output_file_path