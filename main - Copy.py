import sqlite3
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE Twitters
                  (username text, phone text, popular_tweet text, 
                   number_follower number, retweet text) 
               """)
cursor.execute("Insert Into Twitters Values('@sidharth', '911', 'eating rajmachawal', 200, '@alia' ) ")
#single
Twitters = [('@sharukh', '912', 'launching rolex', 2000, '@salman' ), ('@tendulkar', '981', 'India vs. Pak Today', 3012, '@dhoni' ),
	       ('@yogiadityanath', '919', 'romeo squad', 129, '@modi' ), ('@modi', '916', 'GST Coming', 1120, '@Startup India' ),
	        ('@obama', '101', 'President Retires', 4200, '@USA_Biggest Economy' )]
cursor.executemany("INSERT INTO Twitters VALUES (?,?,?,?,?)", Twitters)
conn.commit()
#multiple

sql = "SELECT * FROM Twitters"
cursor.execute(sql)
print (cursor.fetchall())
#fetch
 
sql = """
DELETE FROM Twitters
WHERE popular_tweet = 'GST Coming' """
cursor.execute(sql)
#delete

sql = "SELECT * FROM Twitters"
cursor.execute(sql)
print (cursor.fetchall())
#fetch

print ("\nHere's a listing of all the records in the table:\n"
for row in cursor.execute("SELECT rowid, * FROM Twitters ORDER BY username"):
    print(row)
#print tuple

sql = """
UPDATE Twitters
SET retweet ='@Captain_dhoni'
WHERE username = '@tendulkar'
"""
cursor.execute(sql)
conn.commit()
#Update

sql = "SELECT * FROM Twitters"
cursor.execute(sql)
print (cursor.fetchall())
#check update








