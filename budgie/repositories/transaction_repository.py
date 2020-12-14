import pdb
from budgie.db.run_sql import run_sql

from budgie.models.transaction import Transaction
from budgie.models.merchant import Merchant
from budgie.models.tag import Tag
import budgie.repositories.merchant_repository as merchant_repository
import budgie.repositories.tag_repository as tag_repository



# save
def save(transaction):
    transaction.convert_to_pennies()
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
        merchant = merchant_repository.select(result['merchant_id'])
        tag = tag_repository.select(result['tag_id'])
        transaction = Transaction(result['amount'], merchant, tag, result['id'])
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
    result = run_sql(sql)
    # pdb.set_trace()
    total_as_pennies = result[0][0]
    return total_as_pennies / 100

    


# get total of all transactions for a particular merchant
def total_transactions_by_merchant():
    sql = "SELECT merchant_id, SUM (amount) AS totals FROM transactions GROUP BY merchant_id ORDER BY totals DESC"
    totals = run_sql(sql)
    return totals


# get total of all transactions for a particular tag
def total_transactions_by_tag():
    sql = "SELECT tag_id, SUM (amount) AS totals FROM transactions GROUP BY tag_id ORDER BY totals DESC"
    totals = run_sql(sql)
    return totals