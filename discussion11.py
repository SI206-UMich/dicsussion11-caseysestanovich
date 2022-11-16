import unittest
import sqlite3
import json
import os
# starter code

# Create Database
def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name) # creates a connection
    cur = conn.cursor() #create a cursor from connection
    return cur, conn


# Creates list of species ID's and numbers
def create_species_table(cur, conn):

    species = ["Rabbit",
    "Dog",
    "Cat",
    "Boa Constrictor",
    "Chinchilla",
    "Hamster",
    "Cobra",
    "Parrot",
    "Shark",
    "Goldfish",
    "Gerbil",
    "Llama",
    "Hare"
    ]

    cur.execute("DROP TABLE IF EXISTS Species")
    cur.execute("CREATE TABLE Species (id INTEGER PRIMARY KEY, title TEXT)")
    for i in range(len(species)):
        cur.execute("INSERT INTO Species (id,title) VALUES (?,?)",(i,species[i]))
    conn.commit()

# TASK 1
# CREATE TABLE FOR PATIENTS IN DATABASE
def create_patients_table(cur, conn):
    cur.execute('drop table if exists Patients')
    cur.execute("create table Species (pet_id INTEGER PRIMARY KEY, name TEXT, species_id NUMBER, age INTEGER, cuteness INTEGER, aggressiveness NUMBER)")
    conn.commit()


# ADD FLUFFLE TO THE TABLE
def add_fluffle(cur, conn):
    cur.execute('insert into Patients (pet_id, name, species_id, age, cuteness, aggressiveness) values (?,?,?,?,?,?)', (0,"Fluffle", 0, 3, 90, 100))
    conn.commit()

# TASK 2
# CODE TO ADD JSON TO THE TABLE
# ASSUME TABLE ALREADY EXISTS
def add_pets_from_json(filename, cur, conn):
    
    # WE GAVE YOU THIS TO READ IN DATA
    f = open(filename)
    file_data = f.read()
    f.close()
    json_data = json.loads(file_data)

    # THE REST IS UP TO YOU
    for i in range(len(json_data)):
        cur.execute("insert into Patients (pet_id, name, species_id, age, cuteness, aggressiveness) values (?,?,?,?,?,?)",(i, json_data['name'][i],json_data['species_id'][i], json_data['age'][i], json_data['cuteness'][i], json_data['aggressiveness'][i] ))
    conn.commit()


# TASK 3
# CODE TO OUTPUT NON-AGGRESSIVE PETS
def non_aggressive_pets(aggressiveness, cur, conn):
    un_an = ()
    for i in range(len(aggressiveness)):
        if aggressiveness[i] <= 10:
            un_an += cur.execute('insert into Patients')
        conn.commit()


def main():
    # SETUP DATABASE AND TABLE
    cur, conn = setUpDatabase('animal_hospital.db')
    create_species_table(cur, conn)

    create_patients_table(cur, conn)
    add_fluffle(cur, conn)
    add_pets_from_json('pets.json', cur, conn)
    ls = (non_aggressive_pets(10, cur, conn))
    print(ls)
    
    
if __name__ == "__main__":
    main()

