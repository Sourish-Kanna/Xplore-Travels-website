import sqlite3

def create():
    conn = sqlite3.connect("static/GST Travels.db")
    cur = conn.cursor() 
    cur.execute("CREATE TABLE IF NOT EXISTS city( cid char(3) primary key, city varchar(50) );")
    cur.execute("CREATE TABLE IF NOT EXISTS tag( tid char(3) primary key, tag varchar(50) );")
    cur.execute("CREATE TABLE IF NOT EXISTS find( cid char(3) REFERENCES city(cid), tid char(3) REFERENCES tag(tid));")
    cur.execute("""CREATE TABLE IF NOT EXISTS destination(cid char(3) REFERENCES city(cid),Budget int,SightSeeing varchar(50),byroad varchar(50),
                byrail varchar(50),byair varchar(50),Hotels5star varchar(50),Hotels3star varchar(50),Hotels1star varchar(50),
                Restaurents5star varchar(50),Restaurents3star varchar(50),Restaurents1star varchar(50),NearbySights varchar(50));""")
    conn.commit()
    conn.close()

def insert_preset():
    conn = sqlite3.connect("static/GST Travels.db")
    cur = conn.cursor() 
    cur.execute("""INSERT INTO tag VALUES('T01',"Beach Holidays"),('T02',"Adventure Tour"),('T03',"Cultural Experience"),
                ('T04',"Wildlife Safaries"),('T05',"Mountain Expeditions"),('T06',"Urban Exploration"),('T07',"Wellness Retreats"),
                ('T08',"Historical Journeys"),('T09',"Eco Tourism"),('T10',"Road Trips"),('T11',"Pilgrimage");""")
    conn.commit()
    cur.execute("""INSERT INTO city VALUES('C01',"Goa"),('C02',"Kovalam (Kerala)"),('C03',"Andaman and Nicobar Islands"),('C04',"Manali (Himachal Pradesh)"),
                ('C05',"Rishikesh (Uttarakhand)"),('C06',"Leh (Ladakh)"),('C07',"Jaipur (Rajasthan)"),('C08',"Varanasi (Uttar Pradesh)"),
                ('C09',"Kolkata (West Bengal)"),('C10',"Ranthambore (Rajasthan)"),('C11',"Jim Corbett (Uttarakhand)"),('C12',"Kanha (Madhya Pradesh)"),
                ('C13',"Darjeeling (West Bengal)"),('C14',"Mumbai (Maharashtra)"),('C15',"Delhi"),('C16',"Kerala"),('C17',"Tirupati (Andhra Pradesh)"),
                ('C18',"Agra (Uttar Pradesh)"),('C19',"Munnar (Kerala)"),('C20',"Coorg/Kodagu (Karnataka)"),('C21',"Bangalore (Karnataka)"),
                ('C22',"Haridwar (Uttarakhand)");""")
    conn.commit()
    cur.execute("""INSERT INTO find VALUES('C01',"T01"),('C02',"T01"),('C03',"T01"),('C04',"T02"),('C05',"T02"),('C06',"T02"),
                ('C07',"T03"),('C08',"T03"),('C09',"T03"),('C10',"T04"),('C11',"T04"),('C12',"T04"),('C06',"T05"),('C04',"T05"),('C13',"T05"),
                ('C14',"T06"),('C15',"T06"),('C09',"T06"),('C05',"T07"),('C01',"T07"),('C16',"T07"),('C07',"T08"),('C08',"T08"),('C18',"T08"),
                ('C19',"T09"),('C10',"T09"),('C20',"T09"),('C06',"T10"),('C21',"T10"),('C07',"T10"),('C08',"T11"),('C22',"T11"),('C17',"T11");""")
    conn.commit()
    conn.close()

def insert_tag(tup):
    conn = sqlite3.connect("static/GST Travels.db")
    cur = conn.cursor() 
    tid,tag = tup
    cur.execute(f"INSERT INTO tag VALUES('{tid}','{tag}');")
    conn.commit()
    conn.close()

def insert_city(tup):
    conn = sqlite3.connect("static/GST Travels.db")
    cur = conn.cursor() 
    cid,city = tup
    cur.execute(f"INSERT INTO city VALUES('{cid}','{city}');")
    conn.commit()
    conn.close()

def insert_find(tup):
    conn = sqlite3.connect("static/GST Travels.db")
    cur = conn.cursor() 
    cid,tid = tup
    cur.execute(f"INSERT INTO find VALUES('{cid}','{tid}');")
    conn.commit()
    conn.close()

def gettags():
    conn = sqlite3.connect("static/GST Travels.db")
    cur = conn.cursor() 
    cur.execute("select tag from tag")
    value = []
    lis = cur.fetchall()
    val = len(lis)
    for _ in range(val):
        value.append(lis[_][0])
    conn.close()
    return tuple(value)

def getcitys(tag):
    conn = sqlite3.connect("static/GST Travels.db")
    cur = conn.cursor() 
    cur.execute(f"select tid from tag where tag='{tag}'")
    tid = cur.fetchone()[0]
    cur.execute(f"select city from city where cid in (select cid from find where tid='{tid}');")
    value = []
    lis = cur.fetchall()
    val = len(lis)
    for _ in range(val):
        value.append(lis[_][0])
    conn.close()
    return tuple(value)

def prestart():
    create()
    insert_preset()

try:
    conn = sqlite3.connect("static/GST Travels.db")
    cur = conn.cursor() 
    cur.execute("select tag from tag")
    conn.close()
except sqlite3.OperationalError:
    prestart()

if __name__ == "__main__":
    conn = sqlite3.connect("static/GST Travels.db")
    cur = conn.cursor() 
    for i in cur.execute("select * from city").fetchall():
        print(i[1])
    conn.close()