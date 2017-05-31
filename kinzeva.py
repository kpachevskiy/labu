# coding=utf-8
from time import strftime, gmtime
import  urllib2 , os , csv
import pandas as pd
if not os.path.isdir("data"):
    os.makedirs("data")
nomer=27
pdict={1:'Vinnytsya',2:'Volyn',3:"Dnipropetrovs'k",4:"Donets'k",5:'Zhytomyr',6:'Transcarpathia',7:'Zaporizhzhya',8:"Ivano-Frankivs'k",9:'Kiev',10:'Kirovohrad',
      11:"Luhans'k",12:"L'viv",13:'Mykolayiv',14:'Odessa',15:'Poltava',16:'Rivne',17:'Sumy',18:"Ternopil'",19:'Kharkiv',20:'Kherson',21:"Khmel'nyts'kyy",
      22:'Cherkasy',23:'Chernivtsi',24:'Chernihiv',25:'Crimea',26:"Sevastopol'"}
zdict={}
def zavant(nomer):
    vhi_url = urllib2.urlopen("https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_provinceData.php?country=UKR&provinceID=%s&year1=1981&year2=2017&type=Mean" %(nomer))
    nazva= 'vhi_id_%s%s.csv' %(nomer,strftime('_%d-%m-%Y_%H-%M', gmtime()))
    out = open('data/%s' %(nazva),'wb')
    out.write(vhi_url.read().replace('<br><tt><pre>year,week,, provinceID, SMN,SMT,VCI,TCI,VHI','\nyear,week,SMN,SMT,VCI,TCI,VHI').replace(',', ' ').replace('   ', ' ').replace('  ', ' ').replace(' ',',').replace('</pre></tt>',''))
    out.close()
    csv_data = csv.reader(file('data/%s' %(nazva)))
    for row in csv_data:
        zdict[row[6]]=nomer
        break 
    print "VHI �%s for %s is downloaded..." %(nomer,row[6])
fdict = {}    
def frame(filedir):
    i=0
    
    for filename in os.listdir(filedir):
        if filename.endswith('.csv'):
            if i<len(zdict):
                df = pd.read_csv('%s%s' %(filedir,filename), index_col=False, header=1)
                fdict[zdict.keys()[i]] = df
            i+=1
    #return fdict.keys()
def dani(num):
    print pdict[num]
    return fdict[pdict[num]]
def rik(year,num):
        df=dani(num)
        print df[(df['year']==year)]
        print ('max & min')
        print df[(df['VHI']==max(df['VHI']))]
        print df[(df['VHI']==min(df['VHI']))]
def pos(num):
        da=dani(num)
        df=list(da['VHI'])
        dk=list(da['week'])
        dm=list(da['year'])
        i=0
        while i < len(df):
                if df[i]<=15:
                        print df[i],dk[i],dm[i]
                i+=1
def pom(num):
        da=dani(num)
        df=list(da['VHI'])
        dk=list(da['week'])
        dm=list(da['year'])
        i=0
        while i < len(df):
                if df[i]<=35:
                        print df[i],dk[i],dm[i]
                i+=1

def main():
    for index in range(0, nomer):
        zavant(index+1)
if __name__ == "__main__":
    main()

