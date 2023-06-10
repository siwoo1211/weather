import tkinter as tk
from tkinter import ttk
from actions import selectionAction, 사진바꾸기
  



def main():
    # Creating tkinter window
    window = tk.Tk()
    window.geometry('350x550')
    # Label
    ttk.Label(window, text = "City :", 
            font = ("Times New Roman", 10)).grid(column = 0, 
            row = 15, padx = 10, pady = 25)
    ttk.Label(window, text = "Date :", 
            font = ("Times New Roman", 10)).grid(column = 0, 
            row = 30, padx = 10, pady = 25)

    imageBox = tk.PhotoImage(file="이미지/흐림.png")   
    imageLabel = ttk.Label(window, image=imageBox)
    imageLabel.grid(row=0,column=1)

    n1, n2 = tk.StringVar(), tk.StringVar()
    city_select = ttk.Combobox(window, width = 27, 
                                textvariable = n1)
    city_select['values'] = ('서울', '세종시', '대구')
    city_select.grid(column = 1, row = 15)

    date_select = ttk.Combobox(window, width = 27, 
                                textvariable = n2)
    date_select['values'] = ('2023-01-01', '2023-01-02', '2023-01-03')
    date_select.grid(column = 1, row = 30)
    
    city_select.current(1) 
    date_select.current(1) 

    온도Label = ttk.Label(window, text = "온도 :")
    온도Label.grid(column = 0, row = 65, padx = 10, pady = 25)
    
    buttonAction = lambda : selectionAction(city_select, date_select, imageLabel, 온도Label)

    button = ttk.Button(window, text="선택", command=buttonAction)
    button.grid(row=35, column=1)
    
    
    window.mainloop()

if __name__=="__main__":
    main()