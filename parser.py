import csv
import json
import collections
import itertools
from _ast import Num



def csvFinder():
    companyList = set()
    
    word = ""
    delim = ","
    counter = 0
    header = ""
    headCount = 0
    topDict = {}
    
    with open("jsonParse.txt","w") as wJson:
        with open("ratings_report.csv","r") as readCsv:
            readCsv.strip()
            for line in readCsv:
                
                if counter == 0:
                    for c in line:
                        header += c
                        if c == ",":
                            header = header.replace(",","")
                            headCount += 1
                            topDict[header]= headCount
                            header = ""
                            continue
                        
                            
                            
                        
                for c in line:
                    word = word + c
                    if c == ",":
                        word = word.replace(",","")
                        companyList.add(word)
                        word = ""
                        break
                counter +=1
                
    print companyList        
    
def csvTest():
    with open("jsonParse.txt","w") as wJson:
        with open("ratings_report.csv","r") as readCsv:
            sr = csv.reader(readCsv, delimiter=",",quotechar='"')
            
            allRows = (row for row in sr)
            firstRow= list(allRows.next())
            counter = 0
            firstDict ={}
            for e in firstRow: 
                firstDict[e]=counter
                counter+=1
                
            
            
            

            compList = {row[0] for row in sr}
            bbid = {row[1] for row in sr}
            
            #compList = list(compList)
                   
            it1 = (e for e in compList)
            it2 = (e for e in bbid)
                        
            lst = list(it1)
            lst2 = list(it2)
            trueZip={}
            lst3=itertools.izip(lst,lst2)
            for e in lst3:
                print e
            print trueZip
            a = [1,2,3]
            b = [4,5,6]
            for x,y in zip(a,b):
                print x,y
#             while True:
#                 try:
#                     x= it1.next()
#                     y = it2.next()
#                     print x,y
#                     break
#                 except StopIteration:
#                     pass
#                 break

            for row in sr:
                temp = ",".join(row)
                wJson.write(temp+"\n")
                temp=""
    #print compList
    
    
if __name__ == '__main__':
    csvTest()
