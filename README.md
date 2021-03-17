# Budgie Budget Tacker

Don't be a birdbrain - let Budgie help you budget! A fullstack app to allow a user to track their spending, built over 5 days using Python, Flask and PostgreSQL.

## The Brief

### MVP

* The app should allow the user to create and edit merchants, e.g. Tesco, Amazon, ScotRail
* The app should allow the user to create and edit tags for their spending, e.g. groceries, entertainment, transport
* The user should be able to assign tags and merchants to a transaction, as well as an amount spent on each transaction.
* The app should display all the transactions a user has made in a single view, with each transaction's amount, merchant and tag, and a total for all transactions.

## Future Directions
This was my first fullstack app, and I feel like I've learned a lot since making it. If I were to make Budgie 2.0, I would like to include:
* Data visualisation to show what proportion of a user's budget is going on what
* More active means of goal setting
* Sending alerts/notifications when a user is close to their monthly spending targets

------------

##   How to run
Budgie runs on Flask, and uses psycopg2 for connections to the PostgreSQL database.
### Install Flask
```zsh
pip3 install flask
```
### Install psycopg2
```zsh
pip3 install psycopg2
```
### Database set up
SQL queries can be found in db/budgie_budget.sql to create the tables in the database
```zsh
createdb budgie
psql -d budgie -f budgie/db/budgie_budget.sql
```
To populate the database:
```zsh
python3 console.py
```
### To run the app
```zsh
flask run
```
The app will be running in the browser on localhost:5000

