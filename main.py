from twima import twima_front
from twima import site

twima_instance = twima_front()

twima_instance.main_menu()
menu_choice = twima_instance.get_input()
if menu_choice == "Q":
    exit()
elif menu_choice == "1":
    user_agent = twima_instance.set_user_agent()
    source = twima_instance.set_source()
    site_data = site(source,user_agent)
    print("Trending Topics")
    print(site_data.get_trending(),"\n")
    print("Trending Hashtags")
    print(site_data.get_hashtags(),"\n")
elif menu_choice == "2":
    user_agent = twima_instance.set_user_agent()
    source = twima_instance.set_source()
    loc_url = twima_instance.set_location(user_agent,source)
    site_data = site(loc_url,user_agent)
    print("Trending Topics")
    print(site_data.get_trending(),"\n")
    print("Trending Hashtags")
    print(site_data.get_hashtags(),"\n")
 
