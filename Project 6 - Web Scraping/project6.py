from bs4 import BeautifulSoup
import requests
from unidecode import unidecode

# This was a prompt from lab, which I could not get to during lab hours
# because I was out of time.
# I wanted to see if I could do it.
# The biggest challenge was wading through the entire timeline and seeing all
# the possible ways in which a row could appear
# Some had no dates, some had no years
# But there couldn't be a row without an event, so that's what I decided to loop through.
# That step took me a long while because there was just so much stuff to look through
# The next biggest challenge was figuring out how to structure the dictionary in which I would put the data,
# and also the rows with missing years.

# wikipedia roman history
url = "https://en.wikipedia.org/wiki/Timeline_of_Roman_history"
source_code = requests.get(url).text
parsed_code = BeautifulSoup(source_code, "html.parser")

tables = parsed_code.find_all("table", class_="wikitable")

rome_history_dict = {} # {year : [ [date, event ], [date, event] etc.] }
for table in tables:
    rows = table.find_all("tr")
    
    year = ""
    for row in rows:
        all_td = row.find_all("td")
        
        one_row = []
        for td in all_td:
            one_row.append(td)
            
        if len(one_row) == 3:
            year = unidecode(one_row[0].text)
            rome_history_dict[year] = []
            
            date = one_row[1].text
            if one_row[1].text == "":
                date = "N/A"
        
            event = one_row[2].text.strip()
            #print("ONE", year, date, event)
        
        
        elif len(one_row) == 2:
            date = one_row[0].text
            
            if one_row[1].text == "":
                date = "N/A"
        
            event = one_row[1].text.strip()
            #print("TWO", year, date, event)
        
        else:
            continue
        
        rome_history_dict[year].append([date, event])
        

for key in rome_history_dict:
    print("Year: ", key)
    for event in rome_history_dict[key]:
        print(f"Date: {event[0]}\n{event[1]}\n")
    print("=============================")
    


