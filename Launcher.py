import ni_reader as ni
import sound_player as so
from datetime import datetime
import time
import tkinter as tk

# current date
date=datetime.now().strftime('%y_%m_%d_%H_%M')

# create GUI
window = tk.Tk()
label = tk.Label(text="Data collecting tool",width=30,height=10)
label.pack()
participant = tk.Label(text="Participant")
participant.pack()
text_field = tk.Entry()
text_field.pack()
button_Start = tk.Button(text="Start",width=25,height=5,)
button_Start.pack()
button_Stop = tk.Button(text="Stop",width=25,height=5,)
button_Stop.pack()

# NI GUI methods
ni_reader=ni.NIReader(date)
sound_player=so.SoundPlayer(date)
def start():
	time_start=time.time()
	ni_reader.set_participant(text_field.get())
	sound_player.set_participant(text_field.get())
	ni_reader.start_acquisition(time_start)
	sound_player.start_playing(time_start)

def stop():
	ni_reader.stop_acquisition()
button_Start.config(command = start)
button_Stop.config(command = stop)


# start GUI
window.mainloop()





