import pdb
from app.models.merchant import Merchant 
from app.models.tag import Tag
from app.models.transaction import Transaction

import app.repositories.merchant_repository as merchant_repository
import app.repositories.tag_repository as tag_repository
import app.repositories.transaction_repository as transaction_repository


merchant_repository.delete_all()
tag_repository.delete_all()

merchant_1 = Merchant("Sainsbury")
merchant_repository.save(merchant_1)

tag_1 = Tag("Groceries")
tag_repository.save(tag_1)

transaction_1 = Transaction