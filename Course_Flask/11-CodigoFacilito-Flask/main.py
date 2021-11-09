from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    name = 'Codi'
    course = 'Python Web'
    is_premium = False
    courses = ['Python', 'Ruby', 'Js', 'Java']

    return render_template('index.html', username=name,
                           course_name=course,
                           is_premium=is_premium,
                           courses=courses)


# Creacion de url con parametros <parametro>
@app.route('/usuario/<last_name>/<name>/<int:age>')
def usuario(last_name, name, age):
    return 'Hola' + last_name + '' + name + '' + str(age)


if __name__ == '__main__':
    app.run(debug=True, port=9000)
