from tkinter import *
from tkinter import Scrollbar
from bs4 import BeautifulSoup
import requests
import webbrowser

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
# import manan as m
flipkart=''
ebay=''
croma=''
amazon=''
olx=''

def flipkart(name = ""):
    try:
        global flipkart
        name1 = name.replace(" ","+")   #iphone x  -> iphone+x
        flipkart=f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'
        res = requests.get(f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off',headers=headers)

        soup = BeautifulSoup(res.text,'html.parser')
        flipkart_name = soup.select('._4rR01T')[0].getText().strip()  ### New Class For Product Name
        flipkart_name = flipkart_name.upper()
        if name.upper() in flipkart_name:
            flipkart_price = soup.select('._30jeq3 _1_WHN1')[0].getText().strip()  ### New Class For Product Price
            flipkart_name = soup.select('._4rR01T')[0].getText().strip()

            return f"{flipkart_name}\nPrise : {flipkart_price}\n"
        else:

            flipkart_price='           Product Not Found'
        return flipkart_price
    except:

        flipkart_price= '           Product Not Found'
    return flipkart_price

def ebay(name):
    try:
        global ebay
        name1 = name.replace(" ","+")
        ebay=f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw={name1}&_sacat=0'
        res = requests.get(f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw={name1}&_sacat=0',headers=headers)

        soup = BeautifulSoup(res.text,'html.parser')
        length = soup.select('.s-item__price')
        ebay_page_length=int(len(length))
        for i in range (0,ebay_page_length):
            info = soup.select('.SECONDARY_INFO')[i].getText().strip()
            info = info.upper()
            if info=='BRAND NEW':
                ebay_name = soup.select('.s-item__title')[i].getText().strip()
                name=name.upper()
                ebay_name=ebay_name.upper()
                if name in ebay_name[:25]:
                    ebay_price = soup.select('.s-item__price')[i].getText().strip()
                    ebay_name = soup.select('.s-item__title')[i].getText().strip()

                    ebay_price = ebay_price.replace("INR","₹")

                    ebay_price=ebay_price[0:14]
                    break
                    return f"{ebay_name}\nPrise : {ebay_price}\n"

                else:
                    i+=1
                    i=int(i)
                    if i==ebay_page_length:

                        ebay_price = '           Product Not Found'
                        break

        return f"{ebay_name}\nPrise : {ebay_price}\n"
    except:

        ebay_price = '           Product Not Found'
    return ebay_price

def croma(name):
    try:
        global croma
        name1 = name.replace(" ","+")
        croma=f'https://www.croma.com/search/?text={name1}'
        res = requests.get(f'https://www.croma.com/search/?text={name1}',headers=headers)

        soup = BeautifulSoup(res.text,'html.parser')
        croma_name = soup.select('h3')

        croma_page_length = int( len(croma_name))
        for i in range (0,croma_page_length):
            name = name.upper()
            croma_name = soup.select('h3')[i].getText().strip().upper()
            if name in croma_name.upper()[:25]:
                croma_name = soup.select('h3')[i].getText().strip().upper()
                croma_price = soup.select('.pdpPrice')[i].getText().strip()

                break
            else:
                i+=1
                i=int(i)
                if i==croma_page_length:

                    croma_price = '           Product Not Found'
                    break

        return f"{croma_name}\nPrise : {croma_price}\n"
    except:

        croma_price = '           Product Not Found'
    return croma_price

def amazon(name):
    try:
        global amazon
        name1 = name.replace(" ","-")
        name2 = name.replace(" ","+")
        amazon=f'https://www.amazon.in/{name1}/s?k={name2}'
        res = requests.get(f'https://www.amazon.in/{name1}/s?k={name2}',headers=headers)

        soup = BeautifulSoup(res.text,'html.parser')
        amazon_page = soup.select('.a-size-large product-title-word-break')
        amazon_page_length = int(len(amazon_page))
        for i in range(0,amazon_page_length):
            name = name.upper()
            amazon_name = soup.select('.a-size-large product-title-word-break')[i].getText().strip().upper()
            if name in amazon_name[0:20]:
                amazon_name = soup.select('.a-size-large product-title-word-break')[i].getText().strip().upper()
                amazon_price = soup.select('.a-price-whole')[i].getText().strip().upper()

                break
            else:
                i+=1
                i=int(i)
                if i==amazon_page_length:

                    amazon_price = '           Product Not Found'
                    break
        return f"{amazon_name}\nPrise : {amazon_price}\n"
    except:

        amazon_price = '           Product Not Found'
    return amazon_price


def olx(name):
    try:
        global olx
        name1 = name.replace(" ","-")
        olx=f'https://www.olx.in/items/q-{name1}?isSearchCall=true'
        res = requests.get(f'https://www.olx.in/items/q-{name1}?isSearchCall=true',headers=headers)

        soup = BeautifulSoup(res.text,'html.parser')
        olx_name = soup.select('._2tW1I')
        olx_page_length = len(olx_name)
        for i in range(0,olx_page_length):
            olx_name = soup.select('._2tW1I')[i].getText().strip()
            name = name.upper()
            olx_name = olx_name.upper()
            if name in olx_name:
                olx_price = soup.select('._89yzn')[i].getText().strip()
                olx_name = soup.select('._2tW1I')[i].getText().strip()
                olx_loc = soup.select('.tjgMj')[i].getText().strip()
                try:
                    label = soup.select('._2Vp0i span')[i].getText().strip()
                except:
                    label = "OLD"

                break
            else:
                i+=1
                i=int(i)
                if i==olx_page_length:

                    olx_price = '           Product Not Found'
                    break
        return f"{olx_name}\nPrise : {olx_price}\n"
    except:

        olx_price = '           Product Not Found'
    return olx_price

def convert(a):
    b=a.replace(" ",'')
    c=b.replace("INR",'')
    d=c.replace(",",'')
    f=d.replace("₹",'')
    g=int(float(f))
    return g


def urls():
    global flipkart
    global ebay
    global croma
    global amazon
    global olx
    return f"{flipkart}\n\n\n{ebay}\n\n\n{croma}\n\n\n{amazon}\n\n\n{olx}"



def open_url(event):
        global flipkart
        global ebay
        global croma
        global amazon
        global olx
        webbrowser.open_new(flipkart)
        webbrowser.open_new(ebay)
        webbrowser.open_new(croma)
        webbrowser.open_new(amazon)
        webbrowser.open_new(olx)

def search():
    box1.insert(1.0,"Loding...")
    box2.insert(1.0,"Loding...")
    box3.insert(1.0,"Loding...")
    box4.insert(1.0,"Loding...")
    box5.insert(1.0,"Loding...")
    box6.insert(1.0,"Loding...")


    search_button.place_forget()


    box1.delete(1.0,"end")
    box2.delete(1.0,"end")
    box3.delete(1.0,"end")
    box4.delete(1.0,"end")
    box5.delete(1.0,"end")
    box6.delete(1.0,"end")

    t1=flipkart(product_name.get())
    box1.insert(1.0,t1)

    t2=ebay(product_name.get())
    box2.insert(1.0,t2)

    t3=croma(product_name.get())
    box3.insert(1.0,t3)

    t4=amazon(product_name.get())
    box4.insert(1.0,t4)

    t5=olx(product_name.get())
    box5.insert(1.0,t5)

    t6 = urls()
    box6.insert(1.0,t6)


window = Tk()
window.wm_title("Prise comparison extinction")
window.minsize(1500,700)

lable_one =  Label(window, text="Enter Product Name :", font=("courier", 10))
lable_one.place(relx=0.2, rely=0.1, anchor="center")

product_name =  StringVar()
product_name_entry =  Entry(window, textvariable=product_name, width=50)
product_name_entry.place(relx=0.5, rely=0.1, anchor="center")

search_button =  Button(window, text="Search", width=12, command= search)
search_button.place(relx=0.5, rely=0.2, anchor="center")


l1 =  Label(window, text="flipkart", font=("courier", 20))
l2 =  Label(window, text="ebay", font=("courier", 20))
l3 =  Label(window, text="croma", font=("courier", 20))
l4 =  Label(window, text="amazon", font=("courier", 20))
l5 =  Label(window, text="olx", font=("courier", 20))
l6 =  Label(window, text="All urls", font=("courier", 20))
l8 =  Label(window, text="Loding.....", font=("courier", 30))

l1.place(relx=0.1, rely=0.3, anchor="center")
l2.place(relx=0.5, rely=0.3, anchor="center")
l3.place(relx=0.8, rely=0.3, anchor="center")
l4.place(relx=0.1, rely=0.6, anchor="center")
l5.place(relx=0.5, rely=0.6, anchor="center")
l6.place(relx=0.8, rely=0.6, anchor="center")

scrollbar = Scrollbar(window)
box1 =  Text(window, height=7, width=50, yscrollcommand=scrollbar.set)

box2 =  Text(window, height=7, width=50, yscrollcommand=scrollbar.set)

box3 =  Text(window, height=7, width=50, yscrollcommand=scrollbar.set)

box4 =  Text(window, height=7, width=50, yscrollcommand=scrollbar.set)

box5 =  Text(window, height=7, width=50, yscrollcommand=scrollbar.set)


box1.place(relx=0.2, rely=0.4, anchor="center")
box2.place(relx=0.5, rely=0.4, anchor="center")
box3.place(relx=0.8, rely=0.4, anchor="center")
box4.place(relx=0.2, rely=0.7, anchor="center")
box5.place(relx=0.5, rely=0.7, anchor="center")

box6 =  Text(window, height=15, width=50, yscrollcommand=scrollbar.set, fg="blue", cursor="hand2")
box6.place(relx=0.8, rely=0.8, anchor="center")
box6.bind("<Button-1>", open_url)


window.mainloop()