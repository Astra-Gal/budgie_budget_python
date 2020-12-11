from app.db.run_sql import run_sql

from app.models.merchant import Merchant
from app.models.tag import Tag
from app.models.transaction import Transaction


# save
def save(merchant):
    sql = "INSERT INTO merchants (name) VALUES (%s) RETURNING id"
    values = [merchant.name]
    results = run_sql(sql, values)
    merchant.id = results[0]['id']
    return merchant


# select_all

# select(id)

# edit merchant - UPDATE merchants SET name = (?? %s ??) WHERE name = (?? %s ??) 

# delete_all

# delete(id)