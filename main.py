import requests

# update
# https://api.telegram.org/bot6453932148:AAFeB8vjo2ly_UCWlAaDHgS3VhQpvfDdAQ4/getUpdates 

# id_main = -1001548874589
# id_test = -1001658066382

update_url = 'https://api.telegram.org/bot6453932148:AAFeB8vjo2ly_UCWlAaDHgS3VhQpvfDdAQ4/sendPhoto'
parameters = {
      "chat_id" : "-1001658066382" ,
      "photo" : "https://gameato.ir/wp-content/uploads/2022/11/مگ.png" ,
      "caption" : "\n" + "\n" + "Changes : " + "\n" + "1.RUN" + "\n" + "#ggdevs"
 }

resp_update = requests.get(update_url, data= parameters)
print(resp_update.text)


from bs4 import BeautifulSoup as bs 
import time
import random


db_emoji_1 = { 0 : "📍" , 1 : "🖋️" , 2 : "📌" , 3 : "🧷" , 4 : "⭕️" , 5 : "🌀" , 6 : "🔷" , 7 : "🔶" , 8 : "🔔" , 9 : "💬" , 10 : "🟡" , 11 : "🔵" , 12 : "🟢"}
db_emoji_2 = { 0 : "🔍" , 1 : "👨‍💻" , 2 : "🔥" , 3 : "🎯" , 4 : "💣" , 5 : "📌" , 6 : "🔰" , 7 : "🌀" , 8 : "🟣" , 9 : "⭕️" , 10 : "" , 11 : "" , 12 : ""}
db_cta_z = { 0 : "💬نظر شما در این مورد چیه؟" , 1 : "💬نظرتو کامنت کن برامون" , 2 : "💬نظرتو کامنت کن" , 3 : "💬نظرتو چیه؟ کامنتش کن" , 4 : "" , 5 : "" , 6 : "" , 7 : "" , 8 : "" , 9 : "" , 10 : "" , 11 : "" , 12 : "" , 13 : "" , 14 : "" , 15 : "" , 16 : "" , 17 : ""}
counter0 = 0

time.sleep(60)


while True : 
    r = requests.get("https://digiato.com/topic/science")
    soup = bs(r.text , "html.parser")
    article_links = soup.find("div" , class_="todaysNewsList").find_all("a")
    urls = [link["href"] for link in article_links]
    counter = 0 
    for iurl in urls :
        counter += 1
        if counter == 2 : 
            article_url = iurl


    # image_link 
    r = requests.get(article_url)
    soup = bs(r.text , "html.parser")
    image_links = soup.find("div" , class_="dailyNewsPageHead__picture")
    image_links = str(image_links)
    i_counter = 0 
    g_counter = 0 
    for letter in image_links:
        if letter == "\"" : 
            i_counter += 1
            g_counter += 1
            if i_counter == 15 : 
                a = g_counter
            elif i_counter == 16 : 
                b = g_counter
            else : 
                pi = 3.14 
        else : 
            g_counter += 1 
    image_link = image_links[a : b-1]

    # title 
    r = requests.get(article_url)
    soup = bs(r.text , "html.parser")
    title = soup.find("h1" , class_="dailyNewsPageHead__description--title").text

    # description 
    r = requests.get(article_url)
    soup = bs(r.text , "html.parser")
    description = soup.find("div" , class_="articlePost").find("p").text


    #run
    emoji_1 = db_emoji_1[random.randint(0,12)]
    emoji_2 = db_emoji_2[random.randint(0,12)]
    cta_z = db_cta_z[random.randint(0,17)]



    update_url = 'https://api.telegram.org/bot6453932148:AAFeB8vjo2ly_UCWlAaDHgS3VhQpvfDdAQ4/sendPhoto'
    parameters = {
        "chat_id" : "-1001548874589" ,
        "photo" : image_link ,
        "caption" : emoji_1 + title + "\n" + "\n" + emoji_2 + description + "\n" + "\n" + cta_z + "\n" +"#خارج_از_کنکور" + "\n" + "---------------" + "\n" + "🆔@classoreman" + "\n" + "🌐classoreman.com" 
    }

    if counter0 > 0 : 
        resp_update = requests.get(update_url, data= parameters)
        print(resp_update.text)
        counter0 += 1 
    else : 
        counter0 += 1 



    time.sleep(86400)
