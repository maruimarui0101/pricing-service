from models.item import Item

url = "https://www.amazon.co.uk/BYD-Procedural-Mask-Sterile-Masks/dp/B087QRRGL3?pd_rd_w=vSW3s&pf_rd_p=243fcdf9-2970-4b50-8a21-b929733c8b37&pf_rd_r=P2AZAS8QR4XTG926PKBX&pd_rd_r=d1cea3f6-d93a-46ad-902b-60929896c245&pd_rd_wg=mDUjc"
url2 = "https://www.johnlewis.com/tinc-gifts-gadgets-stationery-advent-calendar-2020/p5027086"
tag_name = "span"
query = {"class": "a-size-medium a-color-price"}

item = Item(url=url, tag_name=tag_name, query=query)

price = item.load_price()
print(price)


