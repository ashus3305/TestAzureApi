import flask


# Initializing flask app
app = flask.Flask(__name__)
# Adding cors to flask


# Controller-1
@app.route("/home")
def home():
    return "This is a demo api"



# Running the api
if __name__ == '__main__':
    app.run()
