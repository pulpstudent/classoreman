import requests
from bs4 import BeautifulSoup as bs 
import time



while True : 
    # night_sleep
    time.sleep(1)
    main_dic = []
    counter = 1
    while counter % 5 != 0  : 
        r = requests.get("https://divar.ir/s/tehran/game-consoles?goods-business-type=personal&price=1000000-")
        soup = bs(r.text , "html.parser")
        product_soup = soup.find("div" ,class_= "browse-post-list-f3858").find_all("picture")
        for i in product_soup :
            x = i.find("img")
            srcs = x.get("data-src")
            if srcs in main_dic : 
                a = 0 
            else:
                main_dic.append(srcs)
        counter += 1
        for link in main_dic : 
            update_url = 'https://api.telegram.org/bot6453932148:AAFeB8vjo2ly_UCWlAaDHgS3VhQpvfDdAQ4/sendPhoto'
            parameters = {
                "chat_id" : "-1001658066382" ,
                "photo" : link ,
                "caption" : "\n" + "\n" + "Changes : " + "\n" + "1.RUN2.2" + "\n" + "#ggdevs"
            }

            resp_update = requests.get(update_url, data= parameters)
            print(resp_update.text)
            
            # breath_sleep
            time.sleep(10)
        # main_sleep
        time.sleep(20)
                
