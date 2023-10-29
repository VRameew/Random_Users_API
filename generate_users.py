from faker import Faker

fake = Faker(['ru_RU'])

def generate_user():
    gender = fake.random_element(['M', 'F'])
    age = age = fake.random_int(min=14, max=85)
    FIO = fake.name() if gender == 'M' else fake.first_name_female()
    address = fake.address()
    email = fake.email()
    login = fake.user_name()

    user_data = {
        'gender': gender,
        'age': age,
        'f_i_o': FIO,
        'address': address,
        'email': email,
        'login': login
    }

    return user_data
