# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_details(
    name=input("Enter your name"),
    surname=input("Enter your surname"),
    birthyear=input("Enter your birth year"),
    city=input("Enter the city of residence"),
    email=input("Enter your email"),
    phone=input("Enter your phone")
):
    print(f"User's details: Name- {name},Surname- {surname}, "
          f"Year of birth- {birthyear}, City of residence- {city},"
          f"Email- {email}, Phone- {phone}.")

print(user_details())

