


import psycopg2, csv


# db = psycopg2.connect(dbname='lab10', user='postgres', password='12345', host='5432')
db = psycopg2.connect(
    dbname='lab10',
    user='postgres',
    password='12345',
    host='localhost',  # Или '127.0.0.1'
    port='5432'
)

current=db.cursor()
current.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        person_name VARCHAR(50),
        phone_number VARCHAR(20)
    );
""")


print(''' What do you want?
      "1" if you want to add a new contact or update existing
      "2" if you want to add contacts from .csv file
      "3" if you want to change name or phone of contact
      "0" if you want to see the whole table contacts
      "4" if you want to see first N contacts''')

req = input("Enter the number ")
if req =='1':
    n = input("Enter name ")
    p = input("Enter phone")
    sql="""
        INSERT INTO phonebook VALUES(%s, %s);
    """
    current.execute(sql,(n, p))

elif req=='2':
    sql="""
        INSERT INTO phonebook VALUES(%s, %s) returning *;
    """
    re = []
    with open ('/Users/elzaniyazbekova/Desktop/pp2/lab10/p_b.csv') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            current.execute(sql, row)
            re.append(current.fetchone())
        print(re, "has been added")
elif req=='3':
    w = input("Name or phone")
    if w=='name':
        x = input("Enter new p_n")
        y = input("Enter the new name")
        sql = """
            UPDATE phonebook SET person_name = %s WHERE phone_number = %s;
        """


        current.execute(sql, (y, x))
        print("has been updated")

elif req=='4':
    x = input("Enter the number of contacts")
    sql = """
        SELECT * FROM phonebook;"""
    current.execute(sql)
    re = current.fetchmany(int(x))

    print("has been added")
    for i in range(len(re)):
        print('{0:20}{1:20}'.format(re[i][0], re[i][1]))
    
elif req == '0':
    sql = """
        SELECT * FROM phonebook
    """
    current.execute(sql)
    results = current.fetchall()
    print('''PHONEBOOK
=========================================
NAME                PHONE
=========================================''')
    for i in range(len(results)):
        print('{0:20}{1:20}'.format(results[i][0], results[i][1]))    

else:
    print("Request is unidentified")

current.close()
db.commit()
db.close()