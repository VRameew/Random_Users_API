from faker import Faker

fake = Faker(['ru_RU'])

def generate_user(integer: int):
    """   This function takes integet, start cycle for numb of Integer
    iterations. In iterations generates random users data
    and saved in dictionary.    """
    i = 0
    data = {
            "quantity": integer,
            "users": [],
            }
    while i < integer:
        gender = fake.random_element(['Male', 'Female'])
        age = fake.random_int(min=14, max=85)
        FIO = fake.name_male() if gender == 'Male' else fake.name_female()
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
        data["users"].append(user_data)
        i = i + 1

    return data
