import tkinter as tk
import math
import json
import sys
import pandas as pd
import requests
import matplotlib.pyplot as plt

def calculate_coronavirus_number_display():
    countryCode = str(country_entry.get())
    URL = "https://api.thevirustracker.com/free-api?countryTimeline="

    res = requests.get(URL + countryCode)
    arr = res.json()
    items = arr['timelineitems'][0]
    dates = list(items.keys())
    dates.remove(dates[-1])
    caseCount = [(items[key]['total_cases']) for key in items if key != 'stat']

    x = dates
    y = caseCount
    plt.plot(x, y)
    plt.xlabel('date')
    plt.ylabel('case')
    plt.show()



window = tk.Tk()
window.title('Coronavirus App')
window.geometry('400x200')
window.configure(background='white')


header_label = tk.Label(window, text='新冠肺炎國家')
header_label.pack()

country_frame = tk.Frame(window)
country_frame.pack(side=tk.TOP)
country_label = tk.Label(country_frame, text='國家代碼')
country_label.pack(side=tk.LEFT)
country_entry = tk.Entry(country_frame)
country_entry.pack(side=tk.LEFT)

result_label = tk.Label(window)
result_label.pack()

calculate_btn = tk.Button(window, text='好手氣', command=calculate_coronavirus_number_display)
calculate_btn.pack()

window.mainloop()
