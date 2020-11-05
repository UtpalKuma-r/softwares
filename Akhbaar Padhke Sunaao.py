import requests


def speak(str):
      from win32com.client import Dispatch
      speak=Dispatch("SAPI.SpVoice")
      speak.Speak(str)


r = requests.get("http://newsapi.org/v2/top-headlines?country=in&language=en&sortBy=top&apiKey=<\\\\\\\\apiKey////////>")
res = r.json()
articles = res["articles"]


speak("while i am reading headlines you can click the links i am printing to know more about them")
for i in range(0,10):
    dic = articles[i]
    news = dic["title"]
    newsUrl = dic["url"]
    newsNumber = i+1
    print(f"News: {newsNumber}\n {newsUrl}\n")
    speak(f"news {str(newsNumber)}, {news}")
speak("Thats it for now, thank you")