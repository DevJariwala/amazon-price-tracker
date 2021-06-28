import requests
from bs4 import BeautifulSoup
import lxml

# url = 'https://www.amazon.in/dp/B08GY3PZQF/ref=s9_acsd_al_bw_c2_x_0_i?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-4&pf_rd_r=KQ7KZ99WR8AERQ6NXR0F&pf_rd_t=101&pf_rd_p=1788fcc0-6d04-4070-a9f6-391682f0650f&pf_rd_i=26264490031'
# url='https://www.amazon.in/Oppo-Fantasy-Storage-Additional-Exchange/dp/B08444SXZ6?ref_=Oct_DLandingS_D_4d1bdad4_60&smid=A14CZOWI0VEHLG'
def get_link_data(url):
    header = {
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36",
        'Accept_Language':'en-GB,en-US;q=0.9,en;q=0.8'
    }


    respons = requests.get(url,headers=header)

    soup = BeautifulSoup(respons.text,'lxml')
   
   

    name = soup.select_one(selector='#productTitle')
    name=name.getText()
    name=name.strip()  #remove extra spaces
    # print(name)
    
    
    try:
        price = soup.select_one(selector="#priceblock_ourprice").getText()
    except:
        price = soup.select_one(selector="#priceblock_dealprice").getText()

   
    price = price[2:].strip()
    price = price.split(',')
    realPrice=''
    for p in price:
        realPrice=realPrice+p

    realPrice=float(realPrice)
    # print(price)
    # print(realPrice)
    return name,realPrice

# print(get_link_data(url))