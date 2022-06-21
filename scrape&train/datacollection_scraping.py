from selenium import webdriver
from selenium.webdriver.chrome.options import Options


ops = Options()
ops.add_argument("--headless")
driver = webdriver.Chrome(
    executable_path="scrape&train/chromedriver.exe", options=ops)
driver.get("https://b2gdevs.github.io/MLIntro/heart-disease.html")
age_elements = driver.find_element_by_class_name("patient-age")
sex_elements = driver.find_element_by_class_name("patient-sex")


print("age_elements")
for i in range(len(age_elements)-1):
    print(int(age_elements[i].text))

print("sex_elements")
for i in range(len(sex_elements)-1):
    print(int(sex_elements[i].text))
