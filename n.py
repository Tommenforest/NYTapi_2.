import requests



sivunumero = 0
while (sivunumero < 100):
    sivunumero = sivunumero + 1
    response = requests.get("https://api.nytimes.com/svc/search/v2/articlesearch.json?q=Trump+foreign+policy&"
    "page={}&begin_date=20150101&end_date=20191120&api-key=2L6CJGmGCgR9YuwGKt7BOAXGpF4sf2pC" .format(sivunumero))
    print(response.json())
    file = open("tulos2.json", "a")
    file.write(str(response.content))
    file.close()