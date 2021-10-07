from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return "<h1>Hello World!</h1>"

@app.route('/information')
def info():
    return '<h1>Welcomer of Information!</h1>'

@app.route('/puppy/<name>')
def puppy(name):
  return '<h1>Upper case: {}</h1>'.format(name.upper())


if __name__ == '__main__':
  #para activar va run(debug=True)
  app.run()