# id_main = -1001548874589
# id_test = -1001658066382
import requests

update_url = 'https://api.telegram.org/bot6453932148:AAFeB8vjo2ly_UCWlAaDHgS3VhQpvfDdAQ4/sendPhoto'
parameters = {
      "chat_id" : "-1001658066382" ,
      "photo" : "" ,
      "caption" : "\n" + "\n" + "Changes : " + "\n" + "1.RUN2.2" + "\n" + "#ggdevs"
}

resp_update = requests.get(update_url, data= parameters)
print(resp_update.text)

