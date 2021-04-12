import matplotlib.pyplot as plt
import numpy as np
import time
from datetime import datetime
import tkinter as tk
import nidaqmx
from nidaqmx.stream_readers import AnalogMultiChannelReader
from nidaqmx import constants
import threading
import pickle
import scipy.io


class data_acquisitor:
	def __init__(self,entry,date):
		self.sampling_freq_in = 1000  # in Hz
		self.buffer_in_size = 100
		self.bufsize_callback = self.buffer_in_size
		self.buffer_in_size_cfg = round(self.buffer_in_size * 1)  # clock configuration
		self.chans_in = 6  # set to number of active OPMs (x2 if By and Bz are used, but that is not recommended)
		self.buffer_in = np.zeros((self.chans_in, self.buffer_in_size))
		self.running=False
		self.entry=entry
		self.date=date

	def ask_user(self):
		input("Acquisition starting")
		self.running = False


	def reading_task_callback(self,task_idx, event_type, num_samples, callback_data):  # bufsize_callback is passed to num_samples
		global time_start
		global compteur
		global temps_de_lancement

		if self.running:
			# It may be wiser to read slightly more than num_samples here, to make sure one does not miss any sample,
			# see: https://documentation.help/NI-DAQmx-Key-Concepts/contCAcqGen.html
			self.buffer_in = np.zeros((self.chans_in, num_samples))  # double definition ???
			stream_in.read_many_sample(self.buffer_in, num_samples, timeout=constants.WAIT_INFINITELY)
			with open("treadmill_"+str(self.entry.get())+'_'+str(self.date)+".txt","a") as file:
				current_time=time.time()
				if compteur==0:
					temps_de_lancement=current_time-time_start
					for i in range(len(self.buffer_in[0])):
						file.write(str(temps_de_lancement+i)+','+str(self.buffer_in[0][i])+','+str(self.buffer_in[1][i])+','+str(self.buffer_in[2][i])+','+str(self.buffer_in[3][i])+','+str(self.buffer_in[4][i])+','+str(self.buffer_in[5][i])+'\n')
				else :
					for i in range(len(self.buffer_in[0])):
						file.write(str(temps_de_lancement+i+100*compteur)+','+str(self.buffer_in[0][i])+','+str(self.buffer_in[1][i])+','+str(self.buffer_in[2][i])+','+str(self.buffer_in[3][i])+','+str(self.buffer_in[4][i])+','+str(self.buffer_in[5][i])+'\n')
				compteur+=1

		return 0  # Absolutely needed for this callback to be well defined (see nidaqmx doc).

	def start_acquisition(self):
		global stream_in
		global task_in
		global time_start
		global compteur

		time_start=time.time()
		compteur=0
		# Configure and setup the tasks
		task_in = nidaqmx.Task()
		task_in.ai_channels.add_ai_voltage_chan("Dev2/ai0:5")  # has to match with chans_in
		task_in.timing.cfg_samp_clk_timing(rate=self.sampling_freq_in, 
									   sample_mode=constants.AcquisitionType.CONTINUOUS,
									   samps_per_chan=self.buffer_in_size_cfg)
		stream_in = AnalogMultiChannelReader(task_in.in_stream)
		task_in.register_every_n_samples_acquired_into_buffer_event(self.bufsize_callback, self.reading_task_callback)


		# Start threading to prompt user to stop
		thread_user = threading.Thread(target=self.ask_user)
		thread_user.start()


		# Main loop
		self.running = True
		# time_start = datetime.now()
		task_in.start()

	def stop_acquisition(self):
		self.running = False
		task_in.close()
		print('\n'+"Acquisition stopped")

