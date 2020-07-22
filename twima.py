import re
import requests 

class site:
    
    def __init__(self, url, user_agent):
        self.url = url
        self.user_agent = user_agent

    def scraper(self):
        headers = {'User-Agent': self.user_agent}
        print()
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

#daytrends = site('https://getdaytrends.com/','Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0')

#for item in daytrends.get_trending():
#    print(item,'\n')
#for item in daytrends.get_hashtags():
#    print(item,'\n')

