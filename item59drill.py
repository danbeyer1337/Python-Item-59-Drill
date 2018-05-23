import sqlite3

peopleValues = (
('Jean-Baptiste Zorg', 'Human', 122),
(' Korben Dallas', 'Meat Popsicle', 100),
("Ak'not", ' Mangalore', -5)
)

with sqlite3.connect(':memory:') as connection:
    c = connection.cursor()

    c.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)")
    c.executemany("INSERT INTO Roster VALUES(?, ?, ?)",peopleValues)

#updates the Species of Korben Dallas to be Human
    c.execute("UPDATE Roster SET Species = 'Human' WHERE Species = 'Meat Popsicle'")
    for row in c.fetchall():
        print(row)
#select all the names and IQs of everyone in the table who is classified as Human
    c.execute("SELECT Name, IQ FROM Roster WHERE Species = 'Human'")
    for row in c.fetchall():
        print(row)

    

    
