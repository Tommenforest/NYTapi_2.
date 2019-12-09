import requests

count = 1
while(count < 11):
    response = requests.get("https://api.nytimes.com/svc/search/v2/articlesearch.json?q=Trump+foreign+policy&"
    "page=3&begin_date=20150101&end_date=20191120&api-key=2L6CJGmGCgR9YuwGKt7BOAXGpF4sf2pC")
    print(response.json())
    file = open("tulos2.json", "a")
    file.write(str(response.content))
    file.close()
    count = count + 1
print("loppukuitti")