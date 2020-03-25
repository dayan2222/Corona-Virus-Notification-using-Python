
# pip install plyer
# pip install bs4


from plyer import notification
import requests
from bs4 import BeautifulSoup 

def notifyMe(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = None,
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
    for tr in soup.find_all('tbody')[4].find_all('tr'):
        myDataStr += tr.get_text()
    # print(myDataStr)
    myDataStr = myDataStr[1:] 
    # print(myDataStr)
    itemList =  myDataStr.split("\n\n")    
    # print(itemList)

    title = "Cases of Covid-19 in Pakistan"
    message = f" Provience : {itemList[0]} \n Cases : {itemList[1]}\n Deaths : {itemList[2]} \n Recoveries : {itemList[3]} \n Active Cases : {itemList[4]} \n Cases / 1M. People : {itemList[5]} "
    proviences = ['\xa0Sindh', '\xa0Punjab']    
    for item in itemList[0:22]:
        dataList = item.split('\n')
        if dataList[0] in proviences:
            notifyMe(title,message)
