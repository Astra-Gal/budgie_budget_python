from app.db.run_sql import run_sql

from app.models.transaction import Transaction
from app.models.merchant import Merchant
from app.models.tag import Tag
import app.repositories.merchant_repository
import app.repositories.tag_repository



# save
def save(transaction):
    sql = "INSERT INTO transactions (amount, merchant_id, tag_id) VALUES (%s, %s, %s) RETURNING id"
    values = [transaction.amount, transaction.merchant.id, transaction.tag.id]
    results = run_sql(sql, values)
    transaction.id = results[0]['id']
    return transaction

# select_all

# select(id)

# edit 

# delete_all

# delete(id)