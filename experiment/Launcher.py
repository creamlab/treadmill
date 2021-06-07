import ni_reader as ni
import sound_player as so
from datetime import datetime
import time
import tkinter as tk
import metronome as m
import weight_reader as wei
import random
import copy_file as cf

# current date
date=datetime.now().strftime('%y_%m_%d_%H_%M')
	
# create GUI
window = tk.Tk()
label = tk.Label(text="Data collecting tool",width=30,height=10)
label.grid(row=1,column=0)

participant = tk.Label(text="Participant")
participant.grid(row=2,column=0)

text_field = tk.Entry()
text_field.grid(row=3,column=0)

button_weight_left = tk.Button(text="weight left",width=25,height=5,)
button_weight_left.grid(row=4,column=0)
stop_button_weight_left = tk.Button(text="weight left stop",width=25,height=5,)
stop_button_weight_left.grid(row=5,column=0)

button_weight_right = tk.Button(text="weight right",width=25,height=5,)
button_weight_right.grid(row=6,column=0)
stop_button_weight_right = tk.Button(text="weight right stop",width=25,height=5,)
stop_button_weight_right.grid(row=7,column=0)

button_metronome = tk.Button(text="Metronome",width=25,height=5,)
button_metronome.grid(row=8,column=0)

button_Start_1 = tk.Button(text="Start_1",width=25,height=5,)
button_Start_1.grid(row=1,column=2)
button_Stop_1 = tk.Button(text="Stop_1",width=25,height=5,)
button_Stop_1.grid(row=1,column=3)

button_Start_2 = tk.Button(text="Start_2",width=25,height=5,)
button_Start_2.grid(row=2,column=2)
button_Stop_2 = tk.Button(text="Stop_2",width=25,height=5,)
button_Stop_2.grid(row=2,column=3)

button_Start_3 = tk.Button(text="Start_3",width=25,height=5,)
button_Start_3.grid(row=3,column=2)
button_Stop_3 = tk.Button(text="Stop_3",width=25,height=5,)
button_Stop_3.grid(row=3,column=3)

button_Start_4 = tk.Button(text="Start_4",width=25,height=5,)
button_Start_4.grid(row=4,column=2)
button_Stop_4 = tk.Button(text="Stop_4",width=25,height=5,)
button_Stop_4.grid(row=4,column=3)

# NI GUI methods
metronome=m.Metronome('config/config_metronome.py')
# ni_reader=ni.NIReader(date,'config/config_nireader_real.py') # à utiliser sur place
# weight_reader_left=wei.WEIGHTReader(date,'config/config_nireader_real.py','left',True) # à utiliser sur place
# weight_reader_right=wei.WEIGHTReader(date,'config/config_nireader_real.py','right',False) # à utiliser sur place

ni_reader=ni.NIReader(date,'config/config_nireader_simulated.py') #à utiliser pour simulation
weight_reader_left=wei.WEIGHTReader(date,'config/config_nireader_simulated.py','left',True) #à utiliser pour simulation
weight_reader_right=wei.WEIGHTReader(date,'config/config_nireader_simulated.py','right',False) #à utiliser pour simulation
sound_player_cont_narrow=so.SoundPlayer(date,'config/config_sound_player_cont_narrow.py')
sound_player_cont_narrow_repeat=so.SoundPlayer(date,'config/config_sound_player_cont_narrow_repeat.py')
sound_player_discret_large=so.SoundPlayer(date,'config/config_sound_player_discret_large.py')
sound_player_discret_large_repeat=so.SoundPlayer(date,'config/config_sound_player_discret_large_repeat.py')

config_list = [sound_player_cont_narrow,sound_player_cont_narrow_repeat,sound_player_discret_large,sound_player_discret_large_repeat]
random.shuffle(config_list)

def weight_mesurement_left():
	print("start acquisition of weight on left side")
	time_start_left=time.time()
	file = "config_ni"
	weight_reader_left.set_participant_wei(text_field.get())
	weight_reader_left.start_acquisition_wei(time_start_left,weight_reader_left.get_participant_wei(),file)

def stop_left():
	print("stop acquisition of weight on left side")
	weight_reader_left.stop_acquisition_wei()

def stop_right():
	print("stop acquisition of weight on right side")
	weight_reader_right.stop_acquisition_wei()

def weight_mesurement_right():
	print("start acquisition of weight on right side")
	time_start_right=time.time()
	file = "config_ni"
	weight_reader_right.set_participant_wei(text_field.get())
	weight_reader_right.start_acquisition_wei(time_start_right,weight_reader_right.get_participant_wei(),file)

def startingMetronome():
	print("start of the metronome")
	metronome.start()


def start_1():
	print("stop of the metronome")
	metronome.stop_playing()
	time_start=time.time()
	file = config_list[0].get_config_file()
	cf.copy_file(file,text_field.get())
	ni_reader.set_participant(text_field.get())
	config_list[0].set_participant(text_field.get())
	config_list[0].set_header(True)
	config_list[0].set_order(1)
	ni_reader.start_acquisition(time_start,ni_reader.get_participant(),file,1)
	config_list[0].set_start_time(time_start)
	config_list[0].start()

def start_2():
	print("stop of the metronome")
	metronome.stop_playing()
	time_start=time.time()
	file = config_list[1].get_config_file()
	cf.copy_file(file,text_field.get())
	ni_reader.set_participant(text_field.get())
	config_list[1].set_participant(text_field.get())
	config_list[1].set_header(False)
	config_list[1].set_order(2)
	ni_reader.start_acquisition(time_start,ni_reader.get_participant(),file,2)
	config_list[1].set_start_time(time_start)
	config_list[1].start()

def start_3():
	print("stop of the metronome")
	metronome.stop_playing()
	time_start=time.time()
	file = config_list[2].get_config_file()
	cf.copy_file(file,text_field.get())
	ni_reader.set_participant(text_field.get())
	config_list[2].set_participant(text_field.get())
	config_list[2].set_header(False)
	config_list[2].set_order(3)
	ni_reader.start_acquisition(time_start,ni_reader.get_participant(),file,3)
	config_list[2].set_start_time(time_start)
	config_list[2].start()

def start_4():
	print("stop of the metronome")
	metronome.stop_playing()
	time_start=time.time()
	file = config_list[3].get_config_file()
	cf.copy_file(file,text_field.get())
	ni_reader.set_participant(text_field.get())
	config_list[3].set_participant(text_field.get())
	config_list[3].set_header(False)
	config_list[3].set_order(4)
	ni_reader.start_acquisition(time_start,ni_reader.get_participant(),file,4)
	config_list[3].set_start_time(time_start)
	config_list[3].start()


def stop_1():
	ni_reader.stop_acquisition()
	config_list[0].stop_playing()

def stop_2():
	ni_reader.stop_acquisition()
	config_list[1].stop_playing()

def stop_3():
	ni_reader.stop_acquisition()
	config_list[2].stop_playing()

def stop_4():
	ni_reader.stop_acquisition()
	config_list[3].stop_playing()

button_metronome.config(command = startingMetronome)
button_Start_1.config(command = start_1)
button_Stop_1.config(command = stop_1)
button_Start_2.config(command = start_2)
button_Stop_2.config(command = stop_2)
button_Start_3.config(command = start_3)
button_Stop_3.config(command = stop_3)
button_Start_4.config(command = start_4)
button_Stop_4.config(command = stop_4)
button_weight_left.config(command = weight_mesurement_left)
button_weight_right.config(command = weight_mesurement_right)
stop_button_weight_left.config(command = stop_left)
stop_button_weight_right.config(command = stop_right)


# start GUI
window.mainloop()





