from flask import Flask, Blueprint, render_template, redirect, request, url_for

from budgie.controllers.merchants_controller import merchants_blueprint
from budgie.controllers.transactions_controller import transactions_blueprint
from budgie.controllers.tags_controller import tags_blueprint

app = Flask(__name__, template_folder='budgie/templates', static_folder='budgie/static')

app.register_blueprint(merchants_blueprint)
app.register_blueprint(transactions_blueprint)
app.register_blueprint(tags_blueprint)

# import blueprint stuff

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)