from flask import Flask, render_template, redirect
from flask import request
from collections.abc import Mapping
from get_data import get_content

app = Flask(__name__)



# załadowanie strony z obrazkiem oraz nazwą dania
@app.route('/',methods=['GET'])
def show_index():
    print("ładuję stronę")
    new_data = get_content()
    image = new_data.get('image_key')
    title = new_data.get('name_key')

    return render_template("index.html", user_image= image,  name_of_dish= title )

# dodanie slider'a do strony oraz pobieranie jego wartości po wprowadzeniu przez użytkownika
@app.route("/submit",methods=['GET'])
def formback():
    default_value = '0'
    data = request.args.get("slider",default_value)
    print('pobrane od użytkownika:', data)

    #tu chyba do game mechanizm będzie wszystki napierdalane

    slider_value = data  # Zaktualizuj wartość pola "slider"

    return slider_value  # Zwróć wartość pola "slider"


@app.route("/modal",methods=['GET','POST'])
def modal():
    #tu wait na zamknięcie tego modala
    print("jest modal")
    return show_index()

#główna pętla programu
if __name__ == "__main__":
    app.run(debug=True)

# https://www.jitsejan.com/python-and-javascript-in-flask
