import requests
from bs4 import BeautifulSoup

titles = []
foods= []
feedbacks = []
discounts = []
deliverys = []

page=1
while True:
        result = requests.get(f"https://www.talabat.com/egypt/restaurants/7771/downtown-tahrir?page={page}")


        src = result.content
        #print(src)

        soup = BeautifulSoup(src, "lxml")
        title = soup.find_all("h2", {"class":"f-18 truncate"})
        food = soup.find_all("span", {"class":"f-14"})
        feedback = soup.find_all("div", {"class":"ml-1 undefined"})
        delivery = soup.find_all("span", {"class":"mr-2"})
        discount = soup.find_all("span", {"class":"f-14 f-500"})



        for i in range(len(title)):
            titles.append(title[i].text)
            foods.append(food[i].text)
            deliverys.append(delivery[i].text)
        for j in range(len(feedback)):
            feedbacks.append(feedback[j].text)
        for o in range(len(discount)):
            discounts.append(discount[o].text)
        if page >19:
         break
        page+=1

print(titles)
print(foods)
print(feedbacks)
print(discounts)
print(deliverys)




