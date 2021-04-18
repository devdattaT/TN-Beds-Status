from bs4 import BeautifulSoup
import csv
import time

#get the row as a List
def rowgetDataText(tr, coltag='td'): # td (data) or th (header)       
        return [td.get_text(strip=True) for td in tr.find_all(coltag)]  


def getFileName():
    timestr = time.strftime("%Y%m%d-%H%M%S")
    extension = "_output.csv"
    file_name =  timestr + extension
    return file_name



bs = BeautifulSoup(open('beds.html', encoding="utf8"), 'html.parser')

#print(bs.prettify())

table = bs.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="dtBasicExample") 
rows = table.findAll(lambda tag: tag.name=='tr')


list_table = []
headers = ['District', 'Institution','Covid Beds-Total','Covid Beds-Occupied','Covid Beds-Vacant',
'OXYGEN SUPPORTED BEDS-Total','OXYGEN SUPPORTED BEDS-Occupied','OXYGEN SUPPORTED BEDS-Vacant',
'Non-OXYGEN SUPPORTED BEDS-Total','Non-OXYGEN SUPPORTED BEDS-Occupied','Non-OXYGEN SUPPORTED BEDS-Vacant',
'ICU BEDS-Total','ICU BEDS-Occupied','ICU BEDS-Vacant',
'VENTILATOR-Total','VENTILATOR-Occupied','VENTILATOR-Vacant','Last Updated', 'Remarks']
list_table.append(headers)

for r in rows:
    #get row as list
    row_as_List = rowgetDataText(r)
    # if row has data
    if(len(row_as_List) > 0):
        list_table.append(row_as_List)
    
#Make output  file name
outputFileName = getFileName()

with open(outputFileName, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(list_table)