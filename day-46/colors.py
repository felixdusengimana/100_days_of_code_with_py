from bs4 import BeautifulSoup
import requests

W3_MAIN_URL = "https://www.w3schools.com/colors/colors_names.asp"

webpage_html = requests.get(W3_MAIN_URL).text
soup = BeautifulSoup(webpage_html, 'html.parser')

color_names = soup.find_all(class_="colornamespan")
hex_code = soup.find_all(class_="colorhexspan")


for i in range(0, len(color_names)):
    print(f"<p>{i+1}. {color_names[i].text}: <b>{hex_code[i].text}</b></p>")

if __name__ == "__main__":
    pass
