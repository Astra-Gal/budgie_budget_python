import pdb
from app.models.merchant import Merchant 

import app.repositories.merchant_repository as merchant_repository

merchant_1 = Merchant("Sainsbury")
merchant_repository.save(merchant_1)