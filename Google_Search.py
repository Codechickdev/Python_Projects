from selenium import webdriver

search_string = input("Enter the word to search: ")
search_string = search_string.replace(' ', "+")

path = "Enter the path of chorme driver"

web = webdriver.Chrome(path)

for i in range(1):
    match_ele = web.get("https://www.google.com/search?q=' " + search_string + "&start=" + str(i))
