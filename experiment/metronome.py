import time
import random
import pyaudio
import wave
import csv
import pickle
import threading
import os
import numpy as np
import struct
import pandas as pd

class Metronome(threading.Thread):
	def __init__(self,config_file):
		threading.Thread.__init__(self)
		
		self.terminated = False 
		
		# read parameters in config files	
		parameters={}
		exec(open(config_file).read(),parameters)
		pars = parameters['params']
		self.period = pars['period']
		sound = pars['sound']
		self.n_trials = pars['n_trials']
		self.sound_list = sound*self.n_trials


	def play_audio_callback(self,in_data, frame_count, time_info,status):
		compteur=0
		delete_list = []
		data = np.zeros(frame_count*2).astype(np.int16)

		for index,file in enumerate(self.currently_playing):

			compteur+=1
			read_frame = file.readframes(frame_count)
			current_data=np.fromstring(read_frame,np.int16)
			
			# Uptade of 'compteur' for the late multiplication
			if current_data.size == 0:
				delete_list.append(index)
				compteur-=1

			# selection of only the non finished files left to play
			else :
				self.data_added=current_data
				if self.data_added.size<data.size:
					rest = data.size-self.data_added.size
					for index in range(rest):
						self.data_added = np.append(self.data_added,0)
				
				# overlap to buffer
				data += self.data_added
		return (data, pyaudio.paContinue)
	
	
	def run(self):		

		# Create and start audio thread	
		audio = pyaudio.PyAudio()		
		self.wf= wave.open("sounds/original/"+self.sound_list[0]) # BUG IF SOUND LIST IS EMPTY

		self.output_stream = audio.open(format = audio.get_format_from_width(self.wf.getsampwidth()),
						channels = self.wf.getnchannels(),
						rate = self.wf.getframerate(),
						output = True, 
						stream_callback = self.play_audio_callback)

		self.output_stream.start_stream()


		# Put files in queue
		self.currently_playing = []
		for file in self.sound_list: 
			# put file in queue
			if self.terminated==True:
				self.output_stream.stop_stream()
				self.output_stream.close()
				audio.terminate()
				break

			self.currently_playing.append(wave.open("sounds/original/"+file))
			time.sleep(self.period)

	def stop_playing(self):
		self.terminated = True