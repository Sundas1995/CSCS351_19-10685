from selenium import webdriver

web = webdriver.Chrome()
web.get('http://automationpractice.com/index.php')


searchName = "Printed Summer Dress"
Search = web.find_element_by_xpath('//*[@id="search_query_top"]')
Search.send_keys(searchName)


Submit = web.find_element_by_xpath('//*[@id="searchbox"]/button')
Submit.click()

img = web.find_element_by_xpath('//*[@id="center_column"]/ul/li[1]/div/div[1]/div/a[1]/img')
img.click()