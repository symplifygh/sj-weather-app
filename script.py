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


response = requests.get("https://weather.com/en-IN/weather/today/l/dae948ef8d2a2af0eb0f8a324707e94e27ac445550ccbd9d75a3f98f9d765371")

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    spans = soup.find_all("span", class_="CurrentConditions--tempValue--MHmYY")
    temperature = spans[0].string
    # breakpoint()
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(HTML_TEMPLATE.format(temperature))
    
else:
    print("Request Failed")
