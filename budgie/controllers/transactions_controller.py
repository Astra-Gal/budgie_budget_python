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
    total_transactions = transaction_repository.total_transactions()
    return render_template("transactions/index.html", transactions=transactions, total_transactions=total_transactions)

# show a particular transaction in more detail
@transactions_blueprint.route("/transactions/<id>")
def show(id):
    transaction = transaction_repository.select(id)
    merchant = transaction_repository.merchant(transaction)
    tag = transaction_repository.tag(transaction)
    return render_template("transactions/show.html", transaction=transaction, merchant=merchant, tag=tag)

# add a new transaction