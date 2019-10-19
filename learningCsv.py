import csv


################################
#####
#####  WRITING DATA TO CSV FLE..
#####
################################

'''
with open("infobase.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title", "Description"])
    writer.writerow(["HTML", "Mark-up Language"])
    writer.writerow(["CSS", "Styling language"])
    writer.writerow(["Javascript", "Language that provides software interactivity"])
    writer.writerow(["Python", "It's a scripting language (OOP)"])
    print("File Overwritten")
'''

'''
with open("infobase.csv", "a", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["C#", "Object Oriented Programming Language"])
    writer.writerow(["C", "Programming language"])
    writer.writerow(["Java", "Object Oriented Programming Language"])
    writer.writerow(["Perl", "It's a scripting language"])
    print("File appended")
'''

################################
#####
#####  READING DATA FROM CSV FLE
#####
################################

'''
with open("infobase.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row) # we can do: print(row[0])
'''        


#######################
#####
##### USING DICTWRITER
#####
#######################


with open("infobase.csv", "w", newline='') as csvfile:
    fieldnames = ["title", "Description"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, restval=None, extrasaction='raise')
    writer.writeheader()
    writer.writerow({"title":"HTML", "Description":"Mark-up Language"})
    writer.writerow({"title":"CSS", "Description":"Styling language"})
    writer.writerow({"title":"Javascript", "Description":"Language that provides software interactivity"})
    writer.writerow({"title":"Python", "Description":"It's a scripting language (OOP)"})
    print("File Overwritten")
    

#######################
#####
##### USING DICTREADER
#####
#######################

with open("infobase.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['title']) # or print(row['title'])














        
