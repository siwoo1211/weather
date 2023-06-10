import tkinter as tk
import json

def 날씨정보불러오기():
    content = {}
    ...
    return content

def 사진바꾸기(imageBoxLabel:tk.Label, 날씨):
    if 날씨 == "맑음":
        이미지경로 = "이미지/맑음.png"
    elif 날씨 == "흐림":
        이미지경로 = "이미지/흐림.png"
        
    imageBox = tk.PhotoImage(file=이미지경로)
    imageBoxLabel.configure(image=imageBox)
    imageBoxLabel.image = imageBox

def selectionAction(city_select, date_select, imgLabel, 온도Label):
    data = dict()
    data = json.loads(open("data.json", encoding="utf8").read())
    # print(data)
    # print(city_select.get(), date_select.get())
    cs = city_select.get()
    ds = date_select.get()
    도시의날씨정보 = data[cs]
    도시의날씨정보 = 도시의날씨정보[ds]
    날씨 = 도시의날씨정보["날씨"]
    print(날씨)
    온도Label.configure(text=f"온도: {도시의날씨정보['온도']}")
    사진바꾸기(imgLabel, 날씨)
    
    
    # 날씨정보 = 날씨정보불러오기(city_select.get(), date_select.get())
    # 사진바꾸기(날씨정보)