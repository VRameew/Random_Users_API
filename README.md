# Code README

This repository contains code for generating fake user data using the Faker library, and saving the generated data to a PostgreSQL database using SQLAlchemy ORM.

## Files

- main.py: This file contains the main FastAPI application that exposes an API endpoint /api/{integer}. When a POST request is made to this endpoint with an integer value, it generates fake user data using the generate_user function from generate_users.py and saves the data to the database using the save_users_data function from SQL_ORM_API.py. The generated data is returned as the response.

- generate_users.py: This file contains the generate_user function that generates fake user data using the Faker library. It takes an integer parameter integer that specifies the number of users to generate. The function creates a dictionary with the quantity of users and a list of user data. The user data includes gender, age, full name (FIO), address, email, and login. The function uses a while loop to generate the specified number of users and appends them to the list.

- SQL_ORM_API.py: This file contains the SQLAlchemy ORM code for saving the generated user data to a PostgreSQL database. It defines a UserData class that represents the table structure for storing user data. The file also includes functions for creating the table, retrieving the last ID of the requestion, and saving the user data to the database.

- test_main.py: This file contains unit tests for the main.py file. It uses the TestClient class from the fastapi.testclient module to test the API endpoint /api/{integer}. The test_response_question function generates fake user data using the generate_user function and mocks the save_users_data function. It then makes a POST request to the endpoint and asserts that the response status code is 200 (OK) and the response body matches the generated user data.

## Docker Compose

To run the application using Docker Compose, follow these steps:

1. Install Docker and Docker Compose if you haven't already.

2. Clone the repository to your local machine.

3. Navigate to the project directory.

4. Build the Docker image by running the following command:

   
   docker-compose build
   

5. Start the application by running the following command:

   
   docker-compose up
   

6. The FastAPI application will be running on http://localhost:8448.

7. Make a POST request to http://localhost:8448/api/{integer} where {integer} is the number of users you want to generate. The generated user data will be saved to the database and returned as the response.

Note: Ensure that you have Docker and Docker Compose installed and running on your machine.

## EXAMPLE

 - Example POST request: http://localhost:8448/api/5
 - Answer:   

{
    "quantity": 5,
    "users": [
        {
            "gender": "Female",
            "age": 35,
            "f_i_o": "Евфросиния Эдуардовна Аксенова",
            "address": "клх Асино, ул. Лермонтова, д. 9/3 стр. 5/1, 511407",
            "email": "sidor40@example.net",
            "login": "gedeon50"
        },
        {
            "gender": "Male",
            "age": 57,
            "f_i_o": "Силантий Филиппович Дроздов",
            "address": "клх Ревда (Сверд.), ул. Саратовская, д. 103, 166621",
            "email": "hariton08@example.net",
            "login": "makarzhukov"
        },
        {
            "gender": "Female",
            "age": 37,
            "f_i_o": "Копылова Оксана Леонидовна",
            "address": "д. Нефедова, пер. Ореховый, д. 6 к. 38, 174660",
            "email": "longinsmirnov@example.org",
            "login": "ovchinnikovfeliks"
        },
        {
            "gender": "Female",
            "age": 56,
            "f_i_o": "Майя Харитоновна Рогова",
            "address": "с. Каменномостский, пер. Отрадный, д. 74 стр. 220, 841351",
            "email": "dmitrievigor@example.com",
            "login": "luchezar2009"
        },
        {
            "gender": "Female",
            "age": 29,
            "f_i_o": "Силина Ульяна Болеславовна",
            "address": "с. Новгород Великий, ш. Мира, д. 5, 126868",
            "email": "zbeljaev@example.net",
            "login": "cpoljakova"
        }
    ]
}

## Dependencies

- FastAPI
- Faker
- SQLAlchemy
- psycopg2
- Pytest
