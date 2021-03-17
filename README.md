# Budgie Budget Tacker
![Screenshot 2021-03-17 at 11 30 12](https://user-images.githubusercontent.com/69347343/111462382-487b4300-8716-11eb-8643-42bd0da9e1bf.png)
![Screenshot 2021-03-17 at 11 30 33](https://user-images.githubusercontent.com/69347343/111462706-a871e980-8716-11eb-80bf-d6ca932b93d0.png)

Don't be a birdbrain - let Budgie help you budget! A fullstack app to allow a user to track their spending, built over 5 days using Python, Flask and PostgreSQL.

## The Brief

### MVP

* The app should allow the user to create and edit merchants, e.g. Tesco, Amazon, ScotRail
* The app should allow the user to create and edit tags for their spending, e.g. groceries, entertainment, transport
* The user should be able to assign tags and merchants to a transaction, as well as an amount spent on each transaction.
* The app should display all the transactions a user has made in a single view, with each transaction's amount, merchant and tag, and a total for all transactions.

### Design
It was important to me to make the design responsive and mobile-friendly, as I felt like I would be most likely to use it on my phone, so I used a number of CSS media queries to stop things crashing into each other at smaller screen sizes.

![Screenshot 2021-03-17 at 11 31 32](https://user-images.githubusercontent.com/69347343/111462859-d1927a00-8716-11eb-9993-b99a8b108f6c.png)
![Screenshot 2021-03-17 at 11 32 13](https://user-images.githubusercontent.com/69347343/111462862-d2c3a700-8716-11eb-9135-07e2c8dfa8ba.png)

I am also keenly aware that personal finance is something people feel a lot of anxiety about, so I used calming colours, and tried to introduce an element of whimsy with the titular Budgie, in an effort to make budgeting fun!

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
cd budgie
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
Follow the link to localhost:5000 to view the app in the browser

