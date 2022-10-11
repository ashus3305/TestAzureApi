import flask


# Initializing flask app
app = flask.Flask(__name__)
# Adding cors to flask


# Controller-1
@app.route("/")
def default():
    return "This is a demo api"
@app.route("/home", methods=['GET'])
def home():
    return "welcome to home"



# Running the api
#if __name__ == '__main__':
    #app.run()
