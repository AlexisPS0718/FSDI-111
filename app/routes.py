from flask import Flask         # From the flask module import the Flask Class

app = Flask(__name__)            # Create an instance of Flask (now an object)

@app.get("/")                    # Flask decorator thtat allows us to define routes. @ = decorator
def index():                     # View function = function wrapped inside a Flask decorator
    me = {                       # Python dictionary (key-value pairs)
      "first_name": "Alexis",
      "last_name": "GPL",
      "hobbies": "Videogames",
      "is_online": True
    }
    return me                    # Returning a dictionary in Flask converts it to JSON