from twiglet import twiglet
from twiglet import site

twiglet = twiglet()

twiglet.main_menu()
menu_choice = twiglet.get_input()
if menu_choice == "Q":
    exit()
elif menu_choice == "1":
    user_agent = twiglet.set_user_agent()
    source = twiglet.set_source()
    site_data = site(source,user_agent)
    print("Trending Topics")
    print(site_data.get_trending(),"\n")
    print("Trending Hashtags")
    print(site_data.get_hashtags(),"\n")
elif menu_choice == "2":
    user_agent = twiglet.set_user_agent()
    source = twiglet.set_source()
    loc_url = twiglet.set_location(user_agent,source)
    site_data = site(loc_url,user_agent)
    print("Trending Topics")
    print(site_data.get_trending(),"\n")
    print("Trending Hashtags")
    print(site_data.get_hashtags(),"\n")
 
