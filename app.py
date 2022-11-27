from flask import Flask
app = Flask(__name__)



@app.route("/")
def hello():
   print (request.headers)
   return "Welcome Flask APP"



if __name__ == "__main__":
   app.run()

