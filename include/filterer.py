import requests
from colored import fg

green = fg('green')
red = fg('red')
yellow = fg('yellow')

class Filterer:
    def __init__(self, url:str, fuzzText: str):
        self.url = url
        self.query = url[url.find("?")+1:url.find("=")]
        self.fuzzText = fuzzText


    def get_data(self) -> bool:
        response = requests.get(self.url)
        if(response.status_code == 200):
             return self.check_fuzz(response.text)
        else: 
            print(red + "Eliminated : " ,self.url, " with status code : ", response.status_code)
            return False
    
    def check_fuzz(self, responseText:str) -> bool:
        if self.fuzzText in responseText:
            print(green + "Text Reflected with query : ", self.url)
            return True

            # call selenium here.
        else:
            # print(yellow + "Text not reflected with query : ", self.query)
            return False