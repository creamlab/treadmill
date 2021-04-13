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
		self.dev="dev1/ai0:5"

	def ask_user(self):
		input("Acquisition starting")
		self.running = False


	def reading_task_callback(self,task_idx, event_type, num_samples, callback_data):  # bufsize_callback is passed to num_samples
		global callback_counter

		if self.running:
			
			# get buffer data
			buffer_in = np.zeros((self.chans_in, num_samples)) 
			self.stream_in.read_many_sample(buffer_in,
								 num_samples, 
								 timeout=constants.WAIT_INFINITELY)
			buffer_time = self.current_time + self.buffer_in_size*callback_counter*1000/self.sampling_freq_in # start time of the ith buffer, in ms
				
			# write in file
			result_file = "data/treadmill_"+self.entry+'_'+str(self.date)+".csv"
			with open(result_file, 'a') as file :
				writer = csv.writer(file,lineterminator='\n')
				for n_sample in range(num_samples):
					time_in_buffer = n_sample*1000/self.sampling_freq_in # time offset of the n_sample sample in current buffer
					result = [buffer_time + time_in_buffer] # time stamp of current sample
					for channel_buffer in buffer_in: 
						result += [channel_buffer[n_sample]] # each channel of the current sample
					writer.writerow(result)

			callback_counter+=1

		return 0  

	def start_acquisition(self,entry):
		global task_in
		global time_start
		global callback_counter
		self.entry=entry

		time_start=time.time()
		callback_counter=0
		# Configure and setup the tasks
		task_in = nidaqmx.Task()
		task_in.ai_channels.add_ai_voltage_chan(self.dev)  # has to match with chans_in
		task_in.timing.cfg_samp_clk_timing(rate=self.sampling_freq_in, 
									   sample_mode=constants.AcquisitionType.CONTINUOUS,
									   samps_per_chan=self.buffer_in_size_cfg)
		self.stream_in = AnalogMultiChannelReader(task_in.in_stream)
		task_in.register_every_n_samples_acquired_into_buffer_event(self.bufsize_callback, self.reading_task_callback)


		# Start threading to prompt user to stop
		thread_user = threading.Thread(target=self.ask_user)

		thread_user.start()


		# Main loop
		self.running = True
		# time_start = datetime.now()
		self.current_time=time_start-time.time()
		task_in.start()

	def stop_acquisition(self):
		self.running = False
		task_in.close()
		print('\n'+"Acquisition stopped")

