from bs4 import BeautifulSoup
import requests

import sys
colect_so_xo = []
html = requests.get("http://ketqua.net/")
soup = BeautifulSoup(html.text, 'html.parser')
so_xo_doc = soup.tbody

for number in so_xo_doc.find_all("td"):
    colect_so_xo.append(str(number.string))
while "None" in colect_so_xo:
    colect_so_xo.remove("None")
counts_win = 0
for your_number in sys.argv[1:]:
    if len(your_number) == 2:
        for number_xoso in colect_so_xo:
            if your_number == number_xoso[-2:]:
                print("{} của bạn đã trúng".format(your_number))
                counts_win += 1
    else:
        print("{} ko hợp lệ nhập số có 2 chữ số".format(your_number))
if counts_win == 0:
    print("Xổ số hôm nay là :")
    for number in colect_so_xo:
        print(number)
