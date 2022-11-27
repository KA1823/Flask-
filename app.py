<<<<<<< HEAD
from flask import Flask, request
app = Flask(__name__)



@app.route("/")
def hello():
   print (request.headers)
   return "Welcome Flask APP"



if __name__ == "__main__":
   app.run()
=======
# from flask import Flask
# # request
# app = Flask(__name__)



# @app.route("/")
# def hello():
#    # print (request.headers)
#    return "Welcome Flask APP"



# # if __name__ == "__main__":
# #    app.run()
>>>>>>> d0070eb8fc2caa619b3236e1b8ba4a5f99cb3a58

