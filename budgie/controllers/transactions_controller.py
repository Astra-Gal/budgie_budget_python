import pdb
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
    tags = tag_repository.select_all()
    merchants = merchant_repository.select_all()
    total_transactions = transaction_repository.total_transactions()
    return render_template("transactions/index.html", transactions=transactions, total_transactions=total_transactions, merchants=merchants, tags=tags)

# show a particular transaction in more detail
@transactions_blueprint.route("/transactions/<id>")
def show(id):
    transaction = transaction_repository.select(id)
    merchant = transaction_repository.merchant(transaction)
    tag = transaction_repository.tag(transaction)
    return render_template("transactions/show.html", transaction=transaction, merchant=merchant, tag=tag)

# ADD - make a new transaction
@transactions_blueprint.route("/transactions/new")
def new():
    merchants = merchant_repository.select_all()
    tags = tag_repository.select_all()
    return render_template("transactions/new.html", merchants=merchants, tags=tags)

# CREATE - add a new transaction 
@transactions_blueprint.route("/transactions", methods =['POST'])
def create_transaction():
    amount = float(request.form['amount'])
    tag = tag_repository.select(request.form['tag'])
    merchant = merchant_repository.select(request.form['merchant'])
    transaction = Transaction(amount, merchant, tag)
    transaction_repository.save(transaction)
    return redirect('/transactions')

#EDIT - GET '/transactions/<id>/edit'
@transactions_blueprint.route("/transactions/<id>/edit")
def edit_transaction(id):
    transaction = transaction_repository.select(id)
    tags = tag_repository.select_all()
    merchants = merchant_repository.select_all()
    return render_template('transactions/edit.html', transaction=transaction, tags=tags, merchants=merchants)

# UPDATE - PUT the values from the form on edit back in '/transactions/<id>'
@transactions_blueprint.route("/transactions/<id>", methods=['POST'])
def update_transaction(id):
    amount = float(request.form['amount']) * 100
    tag = tag_repository.select(request.form['tag'])
    merchant = merchant_repository.select(request.form['merchant'])
    transaction = Transaction(amount, merchant, tag, id)
    transaction_repository.update(transaction)
    return redirect('/transactions')