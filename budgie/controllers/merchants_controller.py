from flask import Flask, render_template, request, redirect
from flask import Blueprint

from budgie.models.merchant import Merchant
import budgie.repositories.merchant_repository as merchant_repository

merchants_blueprint = Blueprint("merchants", __name__)

# show all merchants
@merchants_blueprint.route("/merchants")
def merchants():
    merchants = merchant_repository.select_all()
    return render_template("merchants/index.html", merchants=merchants)

# show all the tags a merchant has been assigned
@merchants_blueprint.route("/merchants/<id>")
def show(id):
    merchant = merchant_repository.select(id)
    tags = merchant_repository.tags(merchant)
    return render_template("merchants/show.html", merchant=merchant, tags=tags)

# ADD - where the form for a new tag lives
@merchants_blueprint.route("/merchants/new")
def new():
    return render_template("merchants/new.html")

# CREATE - add a new merchant
@merchants_blueprint.route("/merchants", methods=['POST'])
def create_merchant():
    name = request.form['name']
    merchant = Merchant(name)
    merchant_repository.save(merchant)
    return redirect('/merchants')