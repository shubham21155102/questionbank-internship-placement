import sqlite3
#Open database
conn = sqlite3.connect('intern.db')
#Create table
c = conn.cursor()
c.execute('''CREATE TABLE company
                (companyname text, examtype text, questionname text, questionlink text, year text)''')
#Insert a row of data
c.execute("INSERT INTO company VALUES ('Google', 'Coding', 'Find the Duplicate Number', 'https://leetcode.com/problems/find-the-duplicate-number/', '2020')")
c.execute("INSERT INTO company VALUES ('Google', 'Coding', 'Find the Duplicate Number', 'https://leetcode.com/problems/find-the-duplicate-number/', '2020')")
c.execute("INSERT INTO company VALUES ('Google', 'Coding', 'Find the Duplicate Number', 'https://leetcode.com/problems/find-the-duplicate-number/', '2020')")
conn.close()