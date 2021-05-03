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

class SoundPlayer(threading.Thread):
	def __init__(self,date,config_file):
		threading.Thread.__init__(self)
		
		self.terminated = False 
		self.date = date
		
		# read parameters in config files	
		parameters={}
		exec(open(config_file).read(),parameters)
		pars = parameters['params']
		n_repeats = pars['n_repeats']
		self.isi = pars['isi']
		
		# create sound list
		sound_list =os.listdir("sounds/piano/")
		sound_bounds = pars['list_of_sounds']
		index_min = sound_list.index(sound_bounds[0])
		index_max = sound_list.index(sound_bounds[1])
		self.sound_list = sound_list[index_min:index_max+1]*n_repeats
		random.shuffle(self.sound_list)
		print(self.sound_list)


	def set_participant(self, participant): 
		self.participant = participant

	def set_start_time(self,start_time):
		self.start_time = start_time


	def play_audio_callback(self,in_data, frame_count, time_info,status):
		
		# read frames from all files currently playing
		compteur=0
		data = np.zeros(frame_count).astype(np.int16)

		for index,file in enumerate(self.currently_playing):
			
			# termination condition
			if self.terminated==True:
				self.output_stream.stop_stream()
				self.output_stream.close()
				self.output_stream.terminate()
				break

			# read frames
			compteur+=1
			read_frame = file.readframes(frame_count)
			current_data=np.fromstring(read_frame,np.int16)

			# Uptade of 'compteur' for the late multiplication
			if current_data.size == 0:
				compteur-=1

			# selection of only the non finished files left to play
			else :
				self.data_added=current_data

				# cases where sizes differ from file to file
				if self.data_added.size>data.size:
					rest = self.data_added.size-data.size
					for index in range(rest):
						data = np.append(data,0)

				if self.data_added.size<data.size:
					rest = data.size-self.data_added.size
					for index in range(rest):
						self.data_added = np.append(self.data_added,0)
				
				# overlap to buffer
				data += self.data_added

		print ('compteur ' + str(compteur))

		# multiplication to prevent the coded data to produce overflow error
		data = (data/compteur).astype(np.int16)

		return (data.tostring(), pyaudio.paContinue)
	
	
	def run(self):
		
		# Prepare csv for logging times  
		self.planning_file="data/treadmill_"+self.participant+'_'+str(self.date)+"_sound.csv"
		with open(self.planning_file, 'a') as file :
				writer = csv.writer(file,lineterminator='\n')
				header = ['time','sound_played']
				writer.writerow(header)

		
		self.start_time=time.time()
		self.current_time=time.time()


		# Create and start audio thread	
		audio = pyaudio.PyAudio()		
		self.wf= wave.open("sounds/piano/"+self.sound_list[0]) # BUG IF SOUND LIST IS EMPTY

		self.output_stream = audio.open(format = audio.get_format_from_width(self.wf.getsampwidth()),
						channels = self.wf.getnchannels(),
						rate = self.wf.getframerate(),
						output = True, 
						stream_callback = self.play_audio_callback)

		#print(self.sound_list[self.numero_du_son_en_cours])
		self.output_stream.start_stream()


		# Put files in queue
		self.numero_du_son_en_cours=0
		self.currently_playing = []
		for file in self.sound_list: 
			self.currently_playing.append(wave.open("sounds/piano/"+file))
			with open(self.planning_file, 'a') as data_file :
				writer = csv.writer(data_file,lineterminator='\n')
				writer.writerow([time.time()-self.start_time,
								file])
		
			time.sleep(self.isi)


	def stop_playing(self):
		self.terminated = True











