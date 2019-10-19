import datetime

import csv
import shutil
from tempfile import NamedTemporaryFile
import re


infodatabase = 'infodatabase.csv'
temp_file = NamedTemporaryFile(delete=False, mode='a')



def editInfo(uid=None, name=None, email=None, itemBought=None, itemAmount=None, date=None):
    #temp_file = NamedTemporaryFile(delete=False)
    with open(infodatabase, "r") as csvfile, temp_file:
        reader = csv.DictReader(csvfile)
        fieldnames = ['id', 'name', 'email', 'item bought', 'item amount', 'date', 'message']
        writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
        writer.writeheader()
        #print(writer)
        for row in reader:
            if row['id'] is not None and int(row.get('id')) == int(uid):
                if name is not None:
                    row['name'] = name
                elif email is not None:
                    row['email'] = email
                elif itemBought is not None:
                    row['item bought'] = itemBought
                elif itemAmount is not None:
                    row['item amount'] = itemAmount
                elif date is not None:
                    row['date'] = date        
            else:
                pass
            writer.writerow(row)
            
        shutil.move(temp_file.name, infodatabase)
        return True
    return False

editInfo(uid='1', name='ssss')
