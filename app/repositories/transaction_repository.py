from app.db.run_sql import run_sql

from app.models.transaction import Transaction
from app.models.merchant import Merchant
from app.models.tag import Tag
import app.repositories.merchant_repository as merchant_repository
import app.repositories.tag_repository as tag_repository



# save
def save(transaction):
    sql = "INSERT INTO transactions (amount, merchant_id, tag_id) VALUES (%s, %s, %s) RETURNING id"
    values = [transaction.amount, transaction.merchant.id, transaction.tag.id]
    results = run_sql(sql, values)
    transaction.id = results[0]['id']
    return transaction

# select_all
def select_all():
    transactions = []

    sql = "SELECT * FROM transactions"
    results = run_sql(sql)

    for row in results:
        merchant = merchant_repository.select(row['merchant_id'])
        tag = tag_repository.select(row['tag_id'])
        transaction = Transaction(row['amount'], merchant, tag, row['id'])
        transactions.append(transaction)
    return transactions

# select(id)

# edit 

# delete_all

# delete(id)