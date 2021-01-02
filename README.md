# Budget-Budgie-Python-Project
### Spending Tracker

Build an app that allows a user to track their spending.

#### MVP

* The app should allow the user to create and edit merchants, e.g. Tesco, Amazon, ScotRail
* The app should allow the user to create and edit tags for their spending, e.g. groceries, entertainment, transport
* The user should be able to assign tags and merchants to a transaction, as well as an amount spent on each transaction.
* The app should display all the transactions a user has made in a single view, with each transaction's amount, merchant and tag, and a total for all transactions.

####   HOW TO OPEN THIS APP

* to make sure you haven't already got a database called budgie, do 'dropdb budgie' then 'createdb budgie'
* run command 'psql -d budgie -f budgie/db/budgie_budget.sql' to create tables in the database
* run command 'python3 console.py' to populate the database
* after making sure flask is installed, run command 'flask run', and follow the link to the local host.
