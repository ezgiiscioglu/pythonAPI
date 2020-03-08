import requests
from bs4 import BeautifulSoup


try:
    #  Price list
    URL="https://www.cars.com/for-sale/searchresults.action/?dealerType=localOnly&mkId=20005&page=1&perPage=50&searchSource=GN_REFINEMENT&sort=relevance&zc=90006"

    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    brand=[]
    model=list()
    year=list()
    cars=soup.find_all("h2",attrs={"class":"listing-row__title"})
    car_list=list()
    for item in cars:
        temp=(str(item.text).strip().split())
        brand.append(temp[1])
        model.append(temp[2:])
        year.append(temp[0])
    print(len(car_list)) 

    print("##################################################################")
    print(brand)
    print("##################################################################")
    print(model)
    print("##################################################################")
    print(year)
    print("##################################################################")



    prices=soup.find_all("span",attrs={"class":"listing-row__price"})
    prices_list=list()
    for item in prices:
        prices_list.append(str(item.text.split("$")[1]).strip())
    print(prices_list) 

    print("##################################################################")
    
    
    externelColorList=list()
    externalColors=soup.find_all(class_="listing-row__meta")
    for item in externalColors:
        externalColorItems = item.find_all('li')
        temp=((externalColorItems[0].contents[2].strip()))
        externelColorList.append(temp)
    print(externelColorList)

    print("##################################################################")
    internalColorsList=list()
    internalColors = soup.find_all(class_='listing-row__meta')
    for internal_color in internalColors:
        internalColorItems = internal_color.find_all('li')
        temp=(internalColorItems[1].contents[2].strip())
        internalColorsList.append(temp)
    print(internalColorsList)

    print("##################################################################")

    transmissionsList=list()
    transmissions = soup.find_all(class_='listing-row__meta')
    for transmission in transmissions:
        transmission_items = transmission.find_all('li')
        temp=(transmission_items[2].contents[2].strip())
        transmissionsList.append(temp)
    print(transmissionsList)

    print("##################################################################")

    contact_List=[]
    contact_number_list = soup.find_all(class_='listing-row__dealer')
    for contact_number in contact_number_list:
        contact_number_list_items = contact_number.find(class_='listing-row__phone')
        if contact_number_list_items!=None:
            number=contact_number_list_items.find_all('span')
            contact_List.append(number[len(number)-1].contents[0])
        else:
            contact_List.append("")
            
    print(contact_List)

    print("##################################################################")
    for x in range(len(contact_List)-1):
        myobj = {'year': year[x],'model':str(brand[x])+" "+str(model[x]),'extcolor':externelColorList[x],'intcolor':internalColorsList[x],'transmission':transmissionsList[x],'price':prices_list[x],'contact':contact_List[x]}
        requests.post("http://127.0.0.1:5000/add", data = myobj)

except requests.exceptions.RequestException as e: 
    print(e)
