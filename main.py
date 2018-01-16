from flask import Flask
from object_size import obj_size
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, DaoDear!'

@app.route('/view')
def size():
  #return "It's me"
  obj = obj_size("./images/example_01.png", 0.955)
  return obj.compute()

if __name__ == '__main__':
  app.run()
