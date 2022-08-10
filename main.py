from selenium import webdriver
from selenium.webdriver.common.by import By

# получаем ссылки на каждый телефон
# list = []
# for i in range(1, 5, 1):
#     url = f'https://catalog.onliner.by/mobile?mobile_type%5B0%5D=smartphone&mobile_type%5Boperation%5D=union&page={i}'
#     # print(url)
#
#     driver = webdriver.Chrome()
#     driver.get(url)
#     d = driver.find_elements(By.XPATH, ".//div[@class='schema-product__title']/a[@class='js-product-title-link']")
#     for el in d:
#         gg = el.get_attribute('href')
#         list.append(gg)
#         # print(gg)
#
#
# with open('href.txt', 'w') as file:
#     for line in list:
#         file.write(f'{line}\n')

# c каждой ссылки получаем цены телефона
with open('href.txt', 'r') as file:
    l = [line.strip() for line in file]
    print(l)

    for el in l:
        driver = webdriver.Chrome()
        driver.get(el)
        d = driver.find_elements(By.XPATH, ".//div[@class='product-aside__offers-part product-aside__offers-part_1']")
        for i in d:
            gg = i.text
            print(gg)

