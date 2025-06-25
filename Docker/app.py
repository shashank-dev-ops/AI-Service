import flask, flask.views
from flask import views

app = flask.Flask(__name__)

class View(flask.views.MethodView):
    def get(self):
        return "Hello from Python!"

app.add_url_rule('/', view_func=View.as_view('main'))

app.debug = True
app.run(port=30001)