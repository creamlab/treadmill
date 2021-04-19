import ni_reader as ni
import sound_player as so
import sound_player_frequencies as sop
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
# ni_reader=ni.NIReader(date,'config/config_nireader_real.p') # à utiliser sur place
ni_reader=ni.NIReader(date,'config/config_nireader_simulated.py') #à utiliser pour simulation
# sound_player=so.SoundPlayer(date,'config/config_sound_player.py')
sound_player_frequencies=sop.SoundPlayerFrequencies(date, 'config/config_sound_player_frequencies.py')

def start():
	time_start=time.time()
	ni_reader.set_participant(text_field.get())
	# sound_player.set_participant(text_field.get())
	sound_player_frequencies.set_participant(text_field.get())
	ni_reader.start_acquisition(time_start)
	# sound_player.set_start_time(time_start)
	# sound_player.start()
	sound_player_frequencies.set_start_time(time_start)
	sound_player_frequencies.start()

def stop():
	ni_reader.stop_acquisition()
	# sound_player.stop_playing()
	sound_player_frequencies.stop_playing()
button_Start.config(command = start)
button_Stop.config(command = stop)


# start GUI
window.mainloop()





