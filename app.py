from flask import Flask, render_template, redirect, request, url_for
from flask import Blueprint

# import controller stuff

app = Flask(__name__)

# import blueprint stuff

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)