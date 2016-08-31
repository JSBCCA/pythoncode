import sqlite3
con = sqlite3.connect('census.db')
cur = con.cursor()
cur.execute(
    'CREATE TABLE Capitals(Province TEXT, Capital TEXT, Population INTEGER)')

countries = [("Newfoundland and Labrador", "St. John's", 512930),
             ("Prince Edward Island", "Charlottetown", 135294),
             ("Nova Scotia", "Halifax", 908007),
             ("New Brunswick", "Fredericton", 729498),
             ("Quebec", "Quebec City", 7237479),
             ("Ontario", "Toronto", 11410046),
             ("Manitoba", "Winnipeg", 1119583),
             ("Saskatchewman", "Regina", 978933),
             ("Alberta", "Edmonton", 2974807),
             ("British Columbia", "Victoria", 3907738),
             ("Yukon Territory", "Whitehorse", 28674),
             ("Northwest Territories", "Yellowknife", 37360),
             ("Nunavut", "Iqaluit", 26745)]
for c in countries:
    cur.execute('INSERT INTO Capitals VALUES (?, ?, ?)', (c[0], c[1], c[2]))

con.commit()

cur.execute('SELECT Province, Capital, Population FROM Capitals')

cur.fetchall()
