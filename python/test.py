from faker import Faker

fake = Faker()

country = fake.country()
state = fake.state()
print(country)
