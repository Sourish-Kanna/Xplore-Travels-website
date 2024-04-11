import sqlite3
import dbms

def city_ID():
    demodb = sqlite3.connect("static/GST Travels.db")
    SuppID:str = "C00"
    cursor = demodb.cursor()
    cursor.execute(f"SELECT cid FROM city;")
    for i in cursor:
        if not bool(i):
            SuppID = 'C00'
        else:
            SuppID = max(i)
    demodb.close()

    try:
        if SuppID[-1] == '9':
            pass
    except:
        SuppID = 'C00'

    if SuppID[-1] == '9':
        b = str(int(SuppID[-2]) + 1)
        SuppID = 'C' + b + "0"
    elif SuppID[-1] != '9':
        a = str(int(SuppID[-1]) + 1)
        b = str(int(SuppID[-2]))
        SuppID = 'C' + b + a
    return SuppID

def tag_ID():
    demodb = sqlite3.connect("static/GST Travels.db")
    SuppID:str = "T00"
    cursor = demodb.cursor()
    cursor.execute(f"SELECT tid FROM tag;")
    for i in cursor:
        if not bool(i):
            SuppID = 'T00'
        else:
            SuppID = max(i)
    demodb.close()

    try:
        if SuppID[-1] == '9':
            pass
    except:
        SuppID = 'T00'

    if SuppID[-1] == '9':
        b = str(int(SuppID[-2]) + 1)
        SuppID = 'T' + b + "0"
    elif SuppID[-1] != '9':
        a = str(int(SuppID[-1]) + 1)
        b = str(int(SuppID[-2]))
        SuppID = 'T' + b + a
    return SuppID

def devstart():
    cid = city_ID()
    city = input("Enter City name: ")
    tag = input("Enter tags: ").split()
    tup1 = (cid,city)
    dbms.insert_city(tup1)
    for i in range(len(tag)):
        tid = tag_ID()
        dbms.insert_tag((tid,i))
        dbms.insert_find((cid,tid))

if __name__ == "__main__":
    devstart()