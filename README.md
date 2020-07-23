# twiglet
A project written to easily retrieve Twitter data, namely trending topics and hashtags without the use of the Twitter API

## Details 
Twitter does provide an API in order to access statistics, data and tweets. However this requires a validated developer account. This project gets around that limitation by retrieving and sorting data from third party scrapers and provides easy methods (as outlined in main.py) to retrieve that information / integrate it into another Python project. 
	
## Details 
This package assumes a Python3 environment, with requirements listed in the "requirements.txt" file for PIP3, you can run the following to get the dependancies. 

```
pip3 install -r requirements.txt
```
## Components
- **twiglet:** A manager class to help provide options for, and a basic CLI to, an instance of site. 
- **site:** Gets tweet trending data from the selected source and reformats it.

## Examples of python usage
- Get trending topics and hashtags worldwide.
``` python
    user_agent = twiglet.set_user_agent()
    source = twiglet.set_source()
    site_data = site(source,user_agent)
    
    print("Trending Topics")
    print(site_data.get_trending(),"\n")
    print("Trending Hashtags")
    print(site_data.get_hashtags(),"\n")
```    
- Further example of basic CLI interface for fetching trends implemented in main.py
