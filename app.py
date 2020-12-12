from flask import Flask, Blueprint, render_template, redirect, request, url_for

from budgie.controllers.merchants_controller import merchants_blueprint


app = Flask(__name__)

app.register_blueprint(merchants_blueprint)

# import blueprint stuff

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)