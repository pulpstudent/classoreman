# id_main = -1001548874589
# id_test = -1001658066382
import requests

update_url = 'https://api.telegram.org/bot6453932148:AAFeB8vjo2ly_UCWlAaDHgS3VhQpvfDdAQ4/sendMessage'
parameters = {
      "chat_id" : "-1001658066382" ,
      "text" : "https://divar.ir/v/پژو-206-تیپ-۲-مدل-۱۳۸۲_سواری-و-وانت_تهران_مرزداران_دیوار/QZNVFHCZ" ,
      "parse_mode" : "markdown"
}

resp_update = requests.get(update_url, data= parameters)
print(resp_update.text)

