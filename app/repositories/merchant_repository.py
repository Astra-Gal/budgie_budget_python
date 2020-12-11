from app.db.run_sql import run_sql

from app.models.merchant import Merchant
# from app.models.tag import Tag
# from app.models.transaction import Transaction


# save a merchant
def save(merchant):
    sql = "INSERT INTO merchants (name) VALUES (%s) RETURNING id"
    values = [merchant.name]
    results = run_sql(sql, values)
    merchant.id = results[0]['id']
    return merchant

# edit a merchant
def update(merchant):
    sql = "UPDATE merchants SET (name) = (%s) WHERE id = %s"
    values = [merchant.name, merchant.id]
    run_sql(sql, values)


# select_all
def select_all():
    merchants = []

    sql = "SELECT * FROM merchants"
    results = run_sql(sql)
    for row in results:
        merchant = Merchant(row['name'], row['id'])
        merchants.append(merchant)
    return merchants

# select(id)
def select(id):
    merchant = None
    sql = "SELECT * FROM merchants WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        merchant = Merchant(result['name'], result['id'])
    return merchant


# delete_all
def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)

# delete(id)
def delete(id):
    sql = "DELETE FROM merchants WHERE id = %s"
    values = [id]
    run_sql(sql, values)