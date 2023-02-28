import requests
from bs4 import BeautifulSoup

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" />
    <title>Weather App</title>
</head>
<body>
    <h1>Temperature: {}</h1>
</body>
</html>
'''


response = requests.get("https://weather.com/en-IN/weather/today/l/7df684d64bef23f80b45fb8005de7a411d1fde0976ef68d6957ea74b18b54bad")

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    spans = soup.find_all("span", class_="CurrentConditions--tempValue--MHmYY")
    temperature = spans[0].string
    # breakpoint()
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(HTML_TEMPLATE.format(temperature))
    
else:
    print("Request Failed")
