import csv

##################################
#####
#####  USING A METHOD TO ADD DATA TO A CSV FILE..
#####
###################################

def getLength (filePath):
    with open(filePath, 'r') as csvfile:
        reader = csv.reader(csvfile)
        readerList = list(reader)
        return len(readerList)


def addUser (filePath, userName, email):
    fieldnames=['ID', 'Name', 'Email']
    with open(filePath, 'a', newline='') as csvfile:
        uid = getLength(filePath)
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({
            'ID': uid,
            'Name': userName,
            'Email': email, })
        return


with open('hungryData.csv', 'w', newline='') as csvfile:
    fieldnames=['ID', 'Name', 'Email']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
addUser('hungryData.csv', 'Ishaq Alimam', 'ishaqalimam@gmail.com')
addUser('hungryData.csv', 'Ishaq Muhammed', 'ishaqmuhammed191@gmail.com')
print('Done')

            
    
