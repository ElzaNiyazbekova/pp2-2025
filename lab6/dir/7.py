# with open("/Users/elzaniyazbekova/Desktop/pp2/lab6/dir/m.txt", "r") as source_file:
#     c= source_file.read()

# with open("/Users/elzaniyazbekova/Desktop/pp2/lab6/dir/r.txt", "w") as destination_file:
#     destination_file.write(c)




import psycopg2, csv


# db = psycopg2.connect(dbname='lab10', user='postgres', password='12345', host='5432')
db = psycopg2.connect(
    dbname='phonebook',
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
    INSERT INTO phonebook (person_name, phone_number) 
    VALUES
        ('John', '12345678901'),
        ('Jane', '19876543210'),
        ('Mike', '56789012345');

""")


print(''' What do you want?
      "1" if you want to add a new contact or update existing
      "2" if you want to add contacts from .csv file
      "3" if you want to change name or phone of contact
      "0" if you want to see the whole table contacts
      "4" if you want to see first N contacts
      "5" if you want to see all phones of contacts
        
      "6" if you want to change name or phone of contact
      "7" if you want to add many contacts by list
      "8" if you want to see contacts with pagination (LIMIT and OFFSET)
      "9" if you want to delete contact by name or phone''')

req = input("Enter")
if req=='1':
    n = input("Enter name")
    p = input("enter p")
    sql = """
        INSERT INTO phonebook VALUES(%s, %s);"""
    current.execute(sql,(n, p))
    
elif req=='2':
    sql = """
        INSERT INTO phonebook VALUES(%s, %s) returning *;"""
    re = []
    with open ('/Users/elzaniyazbekova/Desktop/pp2/lab10/p_b.csv') as f:
        reader = csv.reader(f, delimiter=',')
        for r in reader:
            current.execute(sql, r)
            re.append(current.fetchone())
        print(re, "added")
elif req=='3':
    w = input("Name or phone")
    if w =='name'

elif req =='5':
    sql = """
        SELECT phone_number FROM phonebook;"""
    current.execute(sql)
    res = current.fetchall()
    for i in range(len(res)):
        print(res[i][0])
elif req=='6':
    w = input("Name or phone")
    if w =='name':
        y = input("p_n")
        x = input("name")
    sql = """"
        UPDATE phonebook SET person_name=%s WHERE phobe_number=%s;
    """
    current.execute(sql(y, x))
    print("updates")
elif req=='7':
    contact = input("list")
    cont = []
    for tup in contact.split('),('):
        tup = tup.replace(')','').replace('(', '')
        cont.append(tuple(tup.split(',')))
    print(cont)
    sql = """
        INSERT INTO phonebook VALUES(%s, %s)"""
    
    for i in range(len(cont)):
        current.execute(sql, (cont[i][0], cont))