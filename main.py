import requests
from bs4 import BeautifulSoup
url = 'https://www.letsallfollowback.com/add.php' 
def scrape():
    response = requests.get(url , headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(response.text , 'html.parser')
    print(response.status_code)
    print(response.text)
    data= {'nameField': 'Memes_Dispenser' , 'twitField': '@Memes_Dispenser' , 'submitform': 1 }
    response = requests.post(url , data=data , headers={'User-Agent': 'Mozilla/5.0'})
    print(response.text)
    print(response.status_code)
scrape()
