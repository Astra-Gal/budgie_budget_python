import pdb
from budgie.models.merchant import Merchant 
from budgie.models.tag import Tag
from budgie.models.transaction import Transaction

import budgie.repositories.merchant_repository as merchant_repository
import budgie.repositories.tag_repository as tag_repository
import budgie.repositories.transaction_repository as transaction_repository

transaction_repository.delete_all()
merchant_repository.delete_all()
tag_repository.delete_all()

# merchants
merchant_1 = Merchant("Sainsbury")
merchant_repository.save(merchant_1)

merchant_2 = Merchant("Boots")
merchant_repository.save(merchant_2)

merchant_3 = Merchant("Amazon")
merchant_repository.save(merchant_3)

merchant_4 = Merchant("Landlord")
merchant_repository.save(merchant_4)

merchant_5 = Merchant("giffgaff")
merchant_repository.save(merchant_5)

merchant_6 = Merchant("Kathy Knits")
merchant_repository.save(merchant_6)



# tags
tag_1 = Tag("Groceries")
tag_repository.save(tag_1)

tag_2 = Tag("Entertaiment")
tag_repository.save(tag_2)

tag_3 = Tag("Travel")
tag_repository.save(tag_3)

tag_4 = Tag("Transport")
tag_repository.save(tag_4)

tag_5 = Tag("Bills")
tag_repository.save(tag_5)

tag_6 = Tag("Technology")
tag_repository.save(tag_6)

tag_7 = Tag("Rent")
tag_repository.save(tag_7)

tag_8 = Tag("Beauty")
tag_repository.save(tag_8)

tag_9 = Tag("Hobbies")
tag_repository.save(tag_9)



# transactions
transaction_1 = Transaction(15.84, merchant_1, tag_1)
transaction_repository.save(transaction_1)

transaction_2 = Transaction(30.49, merchant_2, tag_2)
transaction_repository.save(transaction_2)

transaction_3 = Transaction(28.70, merchant_3, tag_3)
transaction_repository.save(transaction_3)

transaction_4 = Transaction(570.00, merchant_4, tag_7)
transaction_repository.save(transaction_4)

transaction_5 = Transaction(25.99, merchant_5, tag_5)
transaction_repository.save(transaction_5)

transaction_6 = Transaction(17.80, merchant_3, tag_2)
transaction_repository.save(transaction_6)

transaction_7 = Transaction(12.34, merchant_3, tag_6)
transaction_repository.save(transaction_7)

transaction_8 = Transaction(22.46, merchant_1, tag_8)
transaction_repository.save(transaction_8)
