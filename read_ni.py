"""
Analog data acquisition for QuSpin's OPMs via National Instruments' cDAQ unit
The following assumes:
"""

# Imports
import matplotlib.pyplot as plt
import numpy as np
import time
import tkinter as tk
from datetime import datetime

from scipy.interpolate import interp1d
from scipy.interpolate import splev, splrep

import nidaqmx
from nidaqmx.stream_readers import AnalogMultiChannelReader
from nidaqmx import constants
# from nidaqmx import stream_readers  # not needed in this script
# from nidaqmx import stream_writers  # not needed in this script

import threading
import pickle
from datetime import datetime
import scipy.io


# Parameters
sampling_freq_in = 1000  # in Hz
buffer_in_size = 100
bufsize_callback = buffer_in_size
buffer_in_size_cfg = round(buffer_in_size * 1)  # clock configuration
chans_in = 6  # set to number of active OPMs (x2 if By and Bz are used, but that is not recommended)
refresh_rate_plot = 10  # in Hz
crop = 10  # number of seconds to drop at acquisition start before saving
my_filename = 'test_3_opms'  # with full path if target folder different from current folder (do not leave trailing /)



# Initialize data placeholders
buffer_in = np.zeros((chans_in, buffer_in_size))
data = np.zeros((chans_in, 1))  # will contain a first column with zeros but that's fine


# Definitions of basic functions
def ask_user():
    global running
    input("Acquisition starting")
    running = False


def reading_task_callback(task_idx, event_type, num_samples, callback_data):  # bufsize_callback is passed to num_samples
    global data
    global buffer_in
    global time_start

    if running:
        # It may be wiser to read slightly more than num_samples here, to make sure one does not miss any sample,
        # see: https://documentation.help/NI-DAQmx-Key-Concepts/contCAcqGen.html
        buffer_in = np.zeros((chans_in, num_samples))  # double definition ???
        stream_in.read_many_sample(buffer_in, num_samples, timeout=constants.WAIT_INFINITELY)
        with open("treadmill_"+str(entry.get())+'_'+str(date)+".txt","a") as file:
            current_time=time.time()
            for i in range(len(buffer_in[0])):
                file.write(str(current_time-time_start+i)+','+str(buffer_in[0][i])+','+str(buffer_in[1][i])+','+str(buffer_in[2][i])+','+str(buffer_in[3][i])+','+str(buffer_in[4][i])+','+str(buffer_in[5][i])+'\n')
        data = np.append(data, buffer_in, axis=1)  # appends buffered data to total variable data

    return 0  # Absolutely needed for this callback to be well defined (see nidaqmx doc).

date=str(datetime.now())
date=date.replace(':','-')
date=date.replace(' ','_')
date=date[:-7]
window = tk.Tk()
label = tk.Label(text="Data collecting tool",width=30,height=10)
label.pack()
victim_name = tk.Label(text="Victim's name")
entry = tk.Entry()
victim_name.pack()
entry.pack()
button_Start = tk.Button(text="Start",width=25,height=5,)
button_Start.pack()
button_Stop = tk.Button(text="Stop",width=25,height=5,)
button_Stop.pack()
information = tk.Label()
information.pack()


def start_acquisition():
    global button_Start
    global running  #cette variable ne sert plus à rien
    global stream_in
    global task_in
    global information
    global time_start

    time_start=time.time()
    # Configure and setup the tasks
    task_in = nidaqmx.Task()
    task_in.ai_channels.add_ai_voltage_chan("Dev2/ai0:5")  # has to match with chans_in
    task_in.timing.cfg_samp_clk_timing(rate=sampling_freq_in, 
                                       sample_mode=constants.AcquisitionType.CONTINUOUS,
                                       samps_per_chan=buffer_in_size_cfg)
    stream_in = AnalogMultiChannelReader(task_in.in_stream)
    task_in.register_every_n_samples_acquired_into_buffer_event(bufsize_callback, reading_task_callback)


    # Start threading to prompt user to stop
    thread_user = threading.Thread(target=ask_user)
    thread_user.start()


    # Main loop
    running = True
    # time_start = datetime.now()
    task_in.start()

def stop_acquisition():
    global button_Stop
    global running
    running = False
    task_in.close()
    print('\n'+"Acquisition stopped")

# def start_time():
#     global button_Start
#     global time_start
#     time_start=time.time()

# button_Start.config(command = start_time)
button_Start.config(command = start_acquisition)
button_Stop.config(command = stop_acquisition)
window.mainloop()




# Plot a visual feedback for the user's mental health
# f, (ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(6, 1, sharex='all', sharey='none')    


# while running:  # make this adapt to number of channels automatically
#     print(data)
#     current_time=time.time()
#     if current_time-time_start>1:
#         running=False
#         print(current_time-time_start)
    # ax1.clear()
    # ax2.clear()
    # ax3.clear()
    # ax4.clear()
    # ax5.clear()
    # ax6.clear()
    # ax1.plot(data[0, -sampling_freq_in * 5:].T)  # 5 seconds rolling window
    # ax2.plot(data[1, -sampling_freq_in * 5:].T)
    # ax3.plot(data[2, -sampling_freq_in * 5:].T)
    # ax4.plot(data[3, -sampling_freq_in * 5:].T)  # 5 seconds rolling window
    # ax5.plot(data[4, -sampling_freq_in * 5:].T)
    # ax6.plot(data[5, -sampling_freq_in * 5:].T)
    # # Label and axis formatting
    # ax6.set_xlabel('time [s]')
    # ax1.set_ylabel('Force_axe_X_gauche')
    # ax2.set_ylabel('Force_axe_Y_gauche')
    # ax3.set_ylabel('Force_axe_Z_gauche')
    # xticks = np.arange(0, data[0, -sampling_freq_in * 5:].size, sampling_freq_in)
    # xticklabels = np.arange(0, xticks.size, 1)
    # ax3.set_xticks(xticks)
    # ax3.set_xticklabels(xticklabels)

    # plt.pause(1/refresh_rate_plot)  # required for dynamic plot to work (if too low, nulling performance bad)

# Close task to clear connection once done
# task_in.close()
# duration = datetime.now() - time_start



# # Final save data and metadata ... first in python reloadable format:
# filename = my_filename
# with open(filename, 'wb') as f:
#     pickle.dump(data, f)
# '''
# Load this variable back with:
# with open(name, 'rb') as f:
#     data_reloaded = pickle.load(f)
# '''
# # Human-readable text file:
# extension = '.txt'
# np.set_printoptions(threshold=np.inf, linewidth=np.inf)  # turn off summarization, line-wrapping
# with open(filename + extension, 'w') as f:
#     f.write(np.array2string(data.T, separator=', '))  # improve precision here!
# # Now in matlab:
# extension = '.mat'
# scipy.io.savemat(filename + extension, {'data':data})


# # Some messages at the end
# num_samples_acquired = data[0,:].size
# print("\n")
# print("OPM acquisition ended.\n")
# print("Acquisition duration: {}.".format(duration))
# print("Acquired samples: {}.".format(num_samples_acquired - 1))


# # Final plot of whole time course the acquisition
# plt.close('all')
# f_tot, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex='all', sharey='none')
# ax1.plot(data[0, 10:].T)  # note the exclusion of the first 10 iterations (automatically zoomed in plot)
# ax2.plot(data[1, 10:].T)
# ax3.plot(data[2, 10:].T)
# # Label formatting ...
# ax3.set_xlabel('time [s]')
# ax1.set_ylabel('voltage [V]')
# ax2.set_ylabel('voltage [V]')
# ax3.set_ylabel('voltage [V]')
# xticks = np.arange(0, data[0, :].size, sampling_freq_in)
# xticklabels = np.arange(0, xticks.size, 1)
# ax3.set_xticks(xticks)
# ax3.set_xticklabels(xticklabels)
# plt.show()
