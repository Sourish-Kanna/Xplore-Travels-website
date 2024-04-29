import sqlite3
import re

def create():
    conn = sqlite3.connect("static/GST Travels.db")
    cur = conn.cursor() 
    cur.execute("CREATE TABLE IF NOT EXISTS city( cid char(3) primary key, city varchar(50) );")
    cur.execute("CREATE TABLE IF NOT EXISTS tag( tid char(3) primary key, tag varchar(50) );")
    cur.execute("CREATE TABLE IF NOT EXISTS find( cid char(3) REFERENCES city(cid), tid char(3) REFERENCES tag(tid));")
    cur.execute("""CREATE TABLE IF NOT EXISTS destination(cid char(3) REFERENCES city(cid),Budget int,SightSeeing varchar(200),byroad varchar(200),
                byrail varchar(200),byair varchar(200),Hotels5star varchar(200),Hotels3star varchar(200),Hotels1star varchar(200),
                Restaurents5star varchar(200),Restaurents3star varchar(200),Restaurents1star varchar(200),NearbySights varchar(200));""")
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
                ('C18',"Agra (Uttar Pradesh)"),('C19',"Munnar (Kerala)"),('C20',"Coorg (Karnataka)"),('C21',"Bangalore (Karnataka)"),
                ('C22',"Haridwar (Uttarakhand)");""")
    conn.commit()
    cur.execute("""INSERT INTO find VALUES('C01',"T01"),('C02',"T01"),('C03',"T01"),('C04',"T02"),('C05',"T02"),('C06',"T02"),
                ('C07',"T03"),('C08',"T03"),('C09',"T03"),('C10',"T04"),('C11',"T04"),('C12',"T04"),('C06',"T05"),('C04',"T05"),('C13',"T05"),
                ('C14',"T06"),('C15',"T06"),('C09',"T06"),('C05',"T07"),('C01',"T07"),('C16',"T07"),('C07',"T08"),('C08',"T08"),('C18',"T08"),
                ('C19',"T09"),('C10',"T09"),('C20',"T09"),('C06',"T10"),('C21',"T10"),('C07',"T10"),('C08',"T11"),('C22',"T11"),('C17',"T11");""")
    conn.commit()
    cur.execute("""INSERT INTO DESTINATION VALUES
                ('C12', 1500, 'Kanha Museum', 'national and state highways', 'Gondia and Jabalpur', 'Jabalpur Airport (JLR) and Raipur Airport (RPR)', 'Club Mahindra Resort - Kanha', 'Kanha Kiskindha Resort', 'Waghoba Resort', 'Hotel Kanha', 'Kamlesh Dhaba', 'Ratnahi Dhaba', 'Jabalpur'),
                ('C16', 6000, 'Kovalam Beach', 'National Highways 17, 47 and 49', 'Thiruvananthapuram Central', 'Cochin International Airport (COK) in Kochi', 'Malabar Junction', 'Fort House Hotel', 'History & Terrace Grill Restaurant', 'Villa Maya', 'Aiswarya Hotel', 'Rich Boat', 'Periyar National Park'),
                ('C02', 2500, 'Vizhinjam Lighthouse', 'Kerala State Road Transportation Services', 'Trivandrum central railways', 'Trivandrum International Airport', 'The Leela Kovalam', 'Maharaju Palace', 'Hotel Dreams', 'Jasmine Bay Restaurant', '3rd Rock Restaurant', 'The Cafe’s Studio', 'Samudra Beach Park'),
                ('C05', 4000, 'Ram jhula', 'regular bus services from Delhi, Haridwar and Dehradun', 'Haridwar Junction railway station', 'Jolly Grant Airport in Dehradun', 'Veda5 Ayurveda & Yoga Retreat', 'Aroma By Taste', 'One 2 One Punjabi Restaurant', 'B2L Hills', 'Shivansh Inn Resort', 'Hotel Madhu Sudan', 'Parmarth Niketan Ashram'),
                ('C08', 1500, 'Assi Ghat', 'National Highway 2', 'Varanasi Junction and Kashi Junction', 'Lal Bahadur Shastri International Airport (VNS)', 'Taj Ganges', 'Hotel Regency', 'Ganga Fuji Homes And Hostel', 'Canton Royale Restaurant', 'Blue Salt Restaurant', 'Tanish Dining and Cafe', 'Bharath Mata Mandir'),
                ('C15', 6000, 'Qutub Minar', 'Interstate Bus Terminals (ISBT) at Anand Vihar, Kashmiri Gate and Sarai Kale Khan', 'New Delhi Railway Station (NDLS), Old Delhi Railway Station (DLI), Hazrat Nizamuddin Railway Station (NZM) and Anand Vihar Railway Terminal (ANVT)', 'Indira Gandhi International Airport (IGI)', 'Country Inn and Suites by Radisson, Sahibabad', 'Hotel Ocean View', 'Hotel Asian Blue Delhi', 'Spice Art', 'The Great Kabab Factory', 'Edesia, Crowne Plaza New Delhi Okhla', 'Agra'),
                ('C13', 6000, 'Tiger Hill Observation Deck', 'Tenzing Norgay Central Bus Terminus at Siliguri', 'New Jalpaiguri', 'Bagdogra', 'Sterling Darjeeling', 'Viceroy Hotel', 'Summit Montana Suites & Spa', 'Grains By Udaan Nirvana, Darjeeling', 'Hotel Lunnar', 'The Junction', 'Siliguri'),
                ('C09', 6000, 'Victoria Memorial Hall', 'national highways', 'Howrah and Sealdah', 'Netaji Subhash Chandra Bose International Airport or Kolkata Airport', 'Taj City Centre New Town, Kolkata', 'Hotel De Sovrani', 'Metropole Hotel', 'Avartana', 'Social Kitchen', 'Aromas', 'darjeeling'),
                ('C10', 6000, 'Ranthambore wildlife sanctuary', 'national highways', 'Sawai Madhopur Railway Station and Jaipur Railway Station', 'Jaipur International Airport', 'The Kipling Lodge - Nature Kalp', 'RTDC Hotel Vinayak', 'Hotel Panthera Tigiris', 'Fateh''s Café', 'Manisha Restaurant', 'Food Corner', 'jaipur'),
                ('C14', 6000, 'Dhobi Ghat', 'Mumbai Central Bus Station', 'Chhatrapati Shivaji Terminus, Mumbai Central Station', 'Chhatrapati Shivaji International Airport', 'The Fern Residency, Mumbai, Chembur', 'Hotel Residency Fort', 'Ginger Mumbai, Goregaon', 'The Earth Plate', 'Tuskers - Vegetarian Dining & Bar', 'Tanatan Shivaji Park', 'pune'),
                ('C11', 10000, 'jim corbet wildlife sanctuary', 'National Highway 121', 'Ramnagar Railway Station', 'Pantnagar Airport (PGH)', 'Taj Corbett Resort and Spa', 'Hotel Corbett Bunglow', 'Waghoba Resort', 'Jungle Grill', 'Gurney House', 'Aromas', 'Rishikesh'),
                ('C19', 10000, 'Munnar Rose Garden', 'Munnar-Bodimettu Highway', 'Aluwa Railway Station', 'Cochin International Airport', 'The Panaromic Getaway', 'Kurinji Wanderlust Resort', 'MSP Amma Cottage', 'Munnar pure vegetarian', 'Rainbow pure vegetarian', 'Munnar cafe', 'Kodaikanal'),
                ('C17', 10000, 'tirumala', 'National Highway 140', 'Tirupati railway station', 'Tirupati International Airport', 'Taj Tirupati', 'Padma Homestay', 'Hotel woodside prestige', 'hotel bliss', 'cafe paprika', 'hotel Tirupati', 'ISKON TIRUPATI'),
                ('C20', 10000, 'Abbey falls', 'Mysore-Madikeri Economic Corridor', 'Mysore railway station', 'Mangalore International Airport', 'The Tamara', 'Whispering Woods', 'hotel Coorg', 'Green Cardamom', 'Silver Oaks', 'Coorg hotels', 'Brahmagiri'),
                ('C22', 10000, 'Ganga Aarti', 'National Highway 58', 'Haridwar Jn (HW)', 'Jolly Grant Airport', 'Ambrosia Sarovar', 'Hotel Le ROI', 'the foodloft', 'Hoshiyar puri', 'the patio', 'Hotel Haridiwar', 'Dehradun'),
                ('C18', 5000, 'agra fort', 'yamuna expressway national highway 19', 'Gatimaan express from delhi to agra', 'kheria airport and indira gandhi airport', 'hotel oberoi amarvilas', 'hotel taj resorts', 'hotel kamal', 'peshawari resto', 'dasaprakash resto', 'joney''s place resto', 'mathura'),
                ('C01', 5000, 'dudhsagar falls', 'mumbai expressway highway', 'madgoan express', 'dabolim airport', 'taj exotica resort', 'acron waterfront resort', 'the business hotel', 'gunpowder', 'fisherman wharf', 'souza lobo', 'panaji'),
                ('C03', 5000, 'ross island', 'not feasible', 'not feasible', 'veer savarkar international airport', 'taj exotica resort', 'sea shell resort', 'haywizz', 'new lighthouse restaurant', 'icy spicy', 'anju coco', 'Havelock island'),
                ('C21', 5000, 'lalbagh botanical garden', 'national highways', 'bengaluru railway station', 'kempegowda international airport', 'the leela palace', 'taj MG road', 'treebo trend edge', 'karavalli', 'MTR mavalli', 'koshy''s resto', 'mysore'),
                ('C06', 5000, 'pangong lake', 'srinagar and manali highways', 'not feasible', 'kushok bakula rimpochee airport', 'the grand dragon ladakh', 'hotel ladakh palace', 'hotel asia', 'tibetan kitchen', 'gesmo resto', 'bon appetit', 'none due to remote location'),
                ('C04', 6000, 'Solang Valley', 'Chandigarh and Shimla National Highway', 'Joginder Railway Station', 'Bhuntar Airport', 'The Himalayan Resort', 'Hotel Snow Park', 'Manali Heights', 'Johnson''s Cafe and Restaurant', 'Chopsticks Resto', 'Cafe 1947', 'Kullu'),
                ('C07', 6000, 'Hawa Mahal and Amber Fort', 'Udaipur National Highways', 'Jaipur Junction', 'Jaipur International Airport', 'The Rambagh Palace', 'Hotel Pearl Palace', 'Hotel Ratnawali', 'Suvarna Mahal', 'Laxmi Misthan Bhandar', 'Peacock Rooftop Restaurant', 'Agra');
                """)
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
    cur.execute(f"SELECT city.city FROM city JOIN find ON city.cid = find.cid JOIN tag ON find.tid = tag.tid WHERE tag.tag = '{tag}';")
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

def get_destination_info(city_name):
    conn = sqlite3.connect("static/GST Travels.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT cid FROM city WHERE city ='{city_name}'")
    city_id = cursor.fetchone()
    cursor.execute(f"SELECT * FROM DESTINATION WHERE cid='{city_id[0]}'")
    data = cursor.fetchone()
    city = re.sub(r'\(.*?\)', '', city_name).strip()
    info = {
        'How to Reach': {
            'By Road': data[3],
            'By Air': data[5],
            'By Rail': data[4]
        },
        f'Our choice of Hotels in {city}': {
            '5⭐': data[6],
            '3⭐': data[7],
            '2⭐': data[8]
        },
        f'Our choice of Restaurants in {city}': {
            '5⭐': data[9],
            '3⭐': data[10],
            '2⭐': data[11]
        },
        f'Our choice of Sightseeing Places in {city}': data[2],
        f'Our choice of Places to Visit Near {city}': data[12]
    }
    conn.close()
    return info

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