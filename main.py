
# pip install plyer
# pip install bs4


from plyer import notification
import requests
from bs4 import BeautifulSoup 

def notifyMe(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "Images\\icon.ico",
        timeout = 10
    )

def getData(url):
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
    # notifyMe("Notification","Testing Notification")
    myHTMLData = getData('https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Pakistan')
    # print(myHTMLData)
    soup = BeautifulSoup(myHTMLData, 'html.parser')
    # print(soup.prettify()) 
    myDataStr = ""
    for tr in soup.find_all('tbody')[3].find_all('tr'):
        myDataStr += tr.get_text()
    myDataStr = myDataStr[1:]    
    itemList =  myDataStr.split("\n\n")    
    # print(itemList)
    proviences = ['\xa0Sindh', '\xa0Punjab']
    # proviences = proviences[3:]

    for item in itemList[0:22]:
        dataList = item.split('\n')
    d =  dataList[0] 
    print(d)   
        # print(type(dataList))   
        # print(len(dataList)) 
        # title = "Cases of Covid-19 in Pakistan"
        # message = f" Provience : {dataList[0]} \n Cases : {dataList[1]}\n Deaths : {dataList[2]} \n Recoveries : {dataList[3]} \n Active Cases : {dataList[4]} \n Cases / 1M. People : {dataList[5]} "
        
        # if dataList[0] in proviences:
        #     notifyMe(title,message)
        #     print(dataList)    
