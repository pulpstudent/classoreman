import requests
from bs4 import BeautifulSoup as bs 
import time


update_url = 'https://api.telegram.org/bot6453932148:AAFeB8vjo2ly_UCWlAaDHgS3VhQpvfDdAQ4/sendPhoto'
parameters = {
      "chat_id" : "-1001658066382" ,
      "photo" : "https://gameato.ir/wp-content/uploads/2022/11/مگ.png" ,
      "caption" : "\n" + "\n" + "Changes : " + "\n" + "WTF" + "\n" + "#ggdevs"
}

# define letter_dic
letter_dic = {}

time.sleep(10)

while True : 
    # night_sleep
    time.sleep(43200)

    # define list 
    pic_list = []

    counter = 1
    while counter % 7 != 0  : 
        r = requests.get("https://divar.ir/s/tehran/game-consoles?goods-business-type=personal&price=1000000-")
        soup = bs(r.text , "html.parser")

        # picture
        pic_soup = soup.find("div" ,class_= "browse-post-list-f3858").find_all("picture")

        # title
        title_soup = soup.find("div" ,class_= "browse-post-list-f3858").find_all("h2")
        title_numb = -1

        # create title_list for each loap 
        title_list = []

        for i in title_soup : 
            title = i.text
            title_list.append(title)

        # append letter_dic   
        for i in title_list : 
            title = i
            letters = title.split()
            for letter in letters :
                if len(letter) > 3 : 
                    if letter in letter_dic : 
                        letter_dic[letter] += 1 
                    else : 
                        letter_dic[letter] = 1
                else : 
                    a = 0 

        # extract data 
        for i in pic_soup :

            # increas title_numb 
            title_numb += 1 

            # pic
            x = i.find("img")
            src = x.get("data-src")
            if src in pic_list : 
                a = 0 
            else:
                pic_list.append(src)

                ## pic_link
                pic_link = src
                
            ## title 
            title = title_list[title_numb]

            # star
            letters = title.split()
            
            pi1 = 0 
            pi2 = 0 
            
            # pi2 
            for j in letter_dic : 
                pi2 += letter_dic[j]
            
            # pi1 
            for letter in letters : 
                pi1 += letter_dic[letter]

            ## star 
            star = ( pi1 / pi2 ) // 3     

            ### run 
            update_url = 'https://api.telegram.org/bot6453932148:AAFeB8vjo2ly_UCWlAaDHgS3VhQpvfDdAQ4/sendPhoto'
            parameters = {
                "chat_id" : "-1001658066382" ,
                "photo" : pic_link ,
                "caption" : "\n" + "\n" + title + "\n" + star + "\n" 
            }

            resp_update = requests.get(update_url, data= parameters)
            print(resp_update.text)

            # breath_sleep
            time.sleep(10)

        counter += 1
        # main_sleep
        time.sleep(7200)
                
   
