import requests
from bs4 import BeautifulSoup

url = "https://www.thehindu.com/news/national/andhra-pradesh/"
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
headlines = soup.find_all("h2")

with open("C:/Users/akhip/headlines.txt", "w", encoding="utf-8") as f:
    f.write("📰 Latest News Headlines\n\n")
    for i, h in enumerate(headlines[:10], 1):
        title = h.get_text(strip=True)
        f.write(f"{i}. {title}\n")

print("✅ Headlines saved to headlines.txt")