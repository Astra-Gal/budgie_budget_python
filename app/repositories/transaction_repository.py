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
def select(id):
    transaction = None
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        transaction = Transaction(result['amount'], result['merchant.id'], result['tag.id'], result['id'])
    return transaction

# edit 
def update(transaction):
    sql = "UPDATE transactions SET (amount, merchant_id, tag_id) = (%s, %s, %s) WHERE id = %s"
    values = [transaction.amount, transaction.merchant.id, transaction.tag.id, transaction.id]
    run_sql(sql, values)

# delete_all
def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)

# delete(id)
def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def merchant(transaction):
    sql = "SELECT * FROM merchants WHERE id = %s"
    values = [transaction.merchant.id]
    results = run_sql(sql, values)[0]
    merchant = Merchant(results['name'], results['id'])
    return merchant

def tag(transaction):
    sql = "SELECT * FROM tags WHERE id = %s"
    values = [transaction.tag.id]
    results = run_sql(sql, values)[0]
    tag = Tag(results['category'], results['id'])
    return tag

# get total for all transactions
def total_transactions():
    sql = "SELECT SUM (amount) FROM transactions"
    total = run_sql(sql)
    return total