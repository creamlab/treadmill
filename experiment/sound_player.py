import time
import random
import pyaudio
import wave
import csv
import pickle
import threading
import os
import numpy as np

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
		self.polling_time = pars['polling_time']
		
		# create sound list
		sound_list =os.listdir("piano/")
		sound_bounds = pars['list_of_sounds']
		index_min = sound_list.index(sound_bounds[0])
		index_max = sound_list.index(sound_bounds[1])
		self.sound_list = sound_list[index_min:index_max]*n_repeats
		random.shuffle(self.sound_list)
		print(self.sound_list)


	def set_participant(self, participant): 
		self.participant = participant

	def set_start_time(self,start_time):
		self.start_time = start_time


	def play_audio_callback(self,in_data, frame_count, time_info,status):
		if self.terminated:
			self.output_stream.stop_stream()
			self.output_stream.close()
			self.output_stream.terminate()
			print("a")
			return None
		if self.numero_du_son_en_cours < len(self.sound_list)-1:
				
			self.data=self.wf.readframes(frame_count)
			if time.time()-self.current_time > self.isi:
				self.numero_du_son_en_cours+=1
				print(self.sound_list[self.numero_du_son_en_cours])
				self.wf= wave.open("piano/"+self.sound_list[self.numero_du_son_en_cours])
				data2=self.wf.readframes(frame_count)
				decodeddata1 = np.fromstring(self.data, np.int16)
				decodeddata2 = np.fromstring(data2, np.int16)
				self.data = (decodeddata1 * 0.5 + decodeddata2 * 0.5).astype(np.int16)
				self.current_time=time.time()
				with open(self.planning_file, 'a') as file :
					writer = csv.writer(file,lineterminator='\n')
					writer.writerow([time.time()-self.start_time,
						self.sound_list[self.numero_du_son_en_cours]])

		return (self.data, pyaudio.paContinue)
	
	
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
		self.wf= wave.open("piano/"+self.sound_list[0]) # BUG IF SOUND LIST IS EMPTY
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
		for file in sound_list: 
			currently_playing.append(wave.open("piano/"+file))
			with open(self.planning_file, 'a') as file :
				writer = csv.writer(file,lineterminator='\n')
				writer.writerow([time.time()-self.start_time,
								file])
		
			time.sleep(self.isi)

			


	def stop_playing(self):
		self.terminated = True