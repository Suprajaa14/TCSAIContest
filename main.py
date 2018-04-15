import csv
import pandas as pd
from textblob import TextBlob
myFile = open('output.csv', 'w')
with myFile:
        myFields = ['id', 'is_duplicate']
        writer = csv.DictWriter(myFile, fieldnames=myFields)    
        writer.writeheader()

def write2csv(row,is_duplicate) :
    myFile = open('output.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        mydata = [row,is_duplicate]
        writer.writerows(mydata)
    
    
    
ifile  = open('train.csv', "r",encoding="utf8")
read = csv.reader(ifile)


for row in read :
    
    question1 = row[3]
    question2 = row[4]
    q1 = TextBlob(question1)
    q2 = TextBlob(question2)
    q1_nouns = q1.noun_phrases
    q2_nouns = q2.noun_phrases
    len_q1_nouns = len(q1_nouns)
    len_q2_nouns = len(q2_nouns)
    a = str(len_q1_nouns)
    b = str(len_q2_nouns)
    if a > b :
        for ele1 in q1_nouns :
            for ele2 in q2_nouns :
                if ele1 == ele2 :
                  
                    write2csv(row[0],"1")
                else :
                   
                    write2csv(row[0],"0")

    else :
        for ele2 in q2_nouns :
            for ele1 in q1_nouns :
                if ele2 == ele1 :
                  
                    write2csv(row[0],"1")
                      
                else:
                  
                    write2csv(row[0],"0")
                     

    

                            
            

                    
