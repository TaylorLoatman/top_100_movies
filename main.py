from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/TaylorLoatman/chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get('https://www.empireonline.com/movies/features/best-movies-2/')

movie_list = driver.find_elements(By.CSS_SELECTOR, '.block-item h3')
movie_list.reverse()
for movie in movie_list:
    print(movie.text)


driver.quit()




