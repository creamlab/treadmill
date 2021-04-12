import module_acquisition as mo
from datetime import datetime
import time
import tkinter as tk



date=str(datetime.now())
date=date.replace(':','-')
date=date.replace(' ','_')
date=date[:-7]
window = tk.Tk()
label = tk.Label(text="Data collecting tool",width=30,height=10)
label.pack()
individu = tk.Label(text="individu")
entry = tk.Entry()
individu.pack()
entry.pack()
button_Start = tk.Button(text="Start",width=25,height=5,)
button_Start.pack()
button_Stop = tk.Button(text="Stop",width=25,height=5,)
button_Stop.pack()
information = tk.Label()
information.pack()
data_samples=mo.data_acquisitor(entry,date)

def start():
	global button_Start
	data_samples.start_acquisition()

def stop():
	global button_Stop
	data_samples.stop_acquisition()

button_Start.config(command = start)
button_Stop.config(command = stop)
window.mainloop()





