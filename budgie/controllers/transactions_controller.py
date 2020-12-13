from flask import Flask, render_template, request, redirect
from flask import Blueprint

from budgie.models.transaction import Transaction
from budgie.models.merchant import Merchant
from budgie.models.tag import Tag

import budgie.repositories.transaction_repository as transaction_repository
import budgie.repositories.merchant_repository as merchant_repository
import budgie.repositories.tag_repository as tag_repository

transactions_blueprint = Blueprint("transactions", __name__)

# show all transactions
@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    return render_template("transactions/index.html", transactions=transactions)

