import sqlite3

# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('example.db')

# cursor object
cursor_obj = connection_obj.cursor()

# Drop the GEEK table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS users")

# Creating table username, password_nam, firstname, lastname, email
table = """ CREATE TABLE users (
			username VARCHAR(255) NOT NULL,
            password_nam VARCHAR(255) NOT NULL,
			firstname CHAR(25) NOT NULL,
			lastname CHAR(25),
			email VARCHAR(255) NOT NULL
		); """

cursor_obj.execute(table)

print("Table is Ready")

# Close the connection
connection_obj.close()



"""create table users (username text, password_nam text, firstname text, lastname text, email text);

create table households(HSHD_NUM int,L text ,AGE_RANGE text,MARITAL text,INCOME_RANGE text,HOMEOWNER text,HSHD_COMPOSITION text,HH_SIZE text,CHILDREN text);

create table transactions(BASKET_NUM int,HSHD_NUM int,PURCHASE_ text,PRODUCT_NUM int,SPEND int,UNITS int,STORE_R text,WEEK_NUM int,YEAR_NUM int);

create table products(PRODUCT_NUM int,DEPARTMENT text,COMMODITY text,BRAND_TY text,NATURAL_ORGANIC_FLAG text);

insert into users values('Srikrithi13', 'qwerty789', 'Sri Krithi', 'Alla', 'srikrikthialla@gmail.com');"""
