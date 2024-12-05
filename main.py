from flask import Flask
from sql_practise import add_post, delete_post, update_post, get_posts

# создание обьекта Flask / приложения

app = Flask(__name__)


# global variables
weather = {"astana": -10.3, "almaty": -6.3, "vienna": 0}
todos = []


@app.route("/")
def welcome():
    return "Это мое первое API"


@app.route("/name")
def name():
    return "Привет, Aitbek"


@app.route("/todos/new/<title>")
def append_title(title):
    todos.append(title)
    return f"Title: '{title}' succesfully has been append to list todos"


@app.route("/todos")
def return_todos():
    return todos


@app.route("/city/<city_name>")
def weather_by_city(city_name):
    for i in weather:
        if i == city_name.lower():
            return f"Твой город: {city_name} \n Температура твоего города в C: {weather[i]}"
    return "Твой город не найден"


@app.route("/todos/remove/<index>")
def remove_element_of_todos(index):
    if (len(todos) < (int(index) + 1)) or (int(index) < -len(todos)):
        return "Индекс не найден сорри"
    del todos[int(index)]
    return todos


# @app.route("/todos/remove/<index>")
# def remove_element_of_todos(index):
#     if todos.pop(int(index)) == -1:
#         return "Error"
#     return todos


@app.route("/posts/add/<posts_title>/<posts_content>")
def add_new_post(posts_title, posts_content):
    return add_post(posts_title, posts_content)


@app.route("/posts")
def get_all_posts():
    return get_posts()


@app.route("/posts/delete/<posts_id>")
def delete_post_by_id(posts_id):
    return delete_post(posts_id)


@app.route("/posts/update/<posts_id>/<new_title>/<new_content>")
def update_postf(posts_id, new_title, new_content):
    return update_post(posts_id, new_title, new_content)


if __name__ == "__main__":
    app.run(port=5102, host="0.0.0.0", debug=True)
