# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
def my_user(name, surname, birth_year, city, email, tel):
    return f"Имя: {name}, Фамилия: {surname}, Год рождения: {birth_year}, Город проживания: {city}, e-mail: {email}, телефон: {tel}"

params = {"name": "Olga",
          "surname": "Levshina",
          "birth_year": "1985",
          "city": "Moscow",
          "email": "levshina@mail.ru",
          "tel": "89269999999"}

print(my_user(**params))

