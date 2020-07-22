import re
import requests 

class site:
    
    def __init__(self, url, user_agent):
        self.url = url
        self.user_agent = user_agent

    def scraper(self):
        headers = {'User-Agent': self.user_agent}
        response = requests.get(self.url,headers=headers)
        content = response.text
        return content

    def get_trending(self):
        trendlist = []
        data = self.scraper()
        sort_trending = re.compile(r"""(class="pos">)(.*?)(<\/a><div class="desc">)""") 
        clean_trending = re.compile(r"""(\/">)(.*?)($)""")
        trend_one = re.findall(sort_trending,data)
        for item in trend_one:
            clean = re.findall(clean_trending,item[1])
            trendlist.append(clean[0][1])
        return trendlist

    def get_hashtags(self):
        taglist = []
        data = self.scraper()
        sort_tags = re.compile(r"""(class="pos">)(.*?)(<\/a><\/td><td)""") 
        clean_tags = re.compile(r"""(\/">)(.*?)($)""")
        tag_one = re.findall(sort_tags,data)
        for item in tag_one:
            clean = re.findall(clean_tags,item[1])
            taglist.append(clean[0][1])
        return taglist

class twima_ui:

    def __init__(self):
        pass
    
    def main_menu(self):
        print("\n")
        print(24*'-', " Welcome to Twima", 24*'-', "\n") 
        print(12*' ',"The API-less Twitter manipulator by @Polo-Sec", "\n")
        print("1 - View currently trending [worldwide]")
        print("2 - View currently trending [by country]")
        print("Q - Quit")

    def get_input(self):
        print("\n")
        user_input = input("> ")
        print("\n")
        return user_input

    def set_user_agent(self):
        available_user_agents = [
                'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
                ]
        print("Select User Agent")
        print("\n", "1. Firefox", "\n", "2. Chrome", "\n", "3. Safari")
        choice = int(self.get_input())
        user_agent = available_user_agents[choice-1]
        return user_agent
    
    def set_source(self):
        sources = [
                'https://getdaytrends.com'
                ]
        print("Select Data Source")
        print("\n", "1. Get Day Trends [https://getdaytrends.com]")
        choice = int(self.get_input())
        source = sources[choice-1]
        return source

    def set_location(self,user_agent,url):
        headers = {'User-Agent': user_agent}
        print("Please enter the country")
        country = self.get_input()
        country = country.replace(' ','-').lower()
        print("Would you like to specify a city? [Y/N]")
        city_choice = self.get_input()
        if city_choice == "Y":
            print("Please enter the City")
            city = self.get_input()
            city = city.replace(' ','-').lower()
            response = requests.get(url+'/'+country+'/'+city,headers=headers)
            print(response)
        else: 
            response = requests.get(url+'/'+country,headers=headers)
            print(response)

            



#daytrends = site('https://getdaytrends.com/','Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0')

#for item in daytrends.get_trending():
#    print(item,'\n')
#for item in daytrends.get_hashtags():
#    print(item,'\n')

