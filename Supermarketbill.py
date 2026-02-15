from datetime import datetime

name=input("Enter Your Name:")
Lists='''
Rice 20/kg
sugar 40/kg
wheat 30/kg
oil Rs 80/liter
paneer Rs 110/kg
Maggi 50/kg
Boost 90/each
colgate 85/each
'''
print(Lists)

#declaration
price=0
pricelist=[]
totalprice=0
ilist=[]
qlist=[]
plist=[]

#rates for items
items={'rice':20,
       'sugar':40,
       'wheat':30,
        'oil':80,
        'paneer':110,
        'Maggi':50,
        'Boost': 90,
        'colgate':85
        }
option=int(input("for list of items press 1:"))
if option==1:
    print(Lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or press 2 for exit:"))
    if inp1==2:
       break
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("Enter your quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
           #for multiple values
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("Sorry you entered item is not available:")
    else:
        print("You entered wrong number:")

    inp=input("Do you want to bill your items yes or no:")
    if inp=='yes':
       pass
       if finalamount!=0:
           print(25*"=","KeMa Supermarket",25*"=")
           print(28*" ","Ibrahimpatnam")
           print("Name:",name,30* " ","Date:",datetime.now())
           print(75*"-")
           print("sno",8*" ",'items',8*" ",'quantity',3*" ",'price')
           for i in range(len(pricelist)):
              print(i,8*' ',5*' ',ilist[i],3*' ',qlist[i],8*"",plist[i])
              print(75*"-")
              print(50*" ",'Totalamount:''Rs',totalprice)
              print("gst amount", 50*" ",'Rs',gst)
              print(75*"-")
              print(50*" ",'finalamount:','Rs',finalamount)
              print(75*"-")
              print(50*" ","Thanks for visiting")
              print(75*"-")


              


