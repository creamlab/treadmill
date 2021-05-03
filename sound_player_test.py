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
		self.parameters={}
		self.config_file = config_file
		self.terminated = False 
		self.date = date
		exec(open(self.config_file).read(),self.parameters)
		pars = self.parameters['params']
		if self.config_file == 'config/config_sound_player.py':
			self.n_repeats = pars['n_repeats']
			liste_sons=os.listdir("C:/Users/qdecu/Documents/StageTapis/Treadmill/treadmill/piano/")
			self.list_of_sounds = pars['list_of_sounds']
			index_min = liste_sons.index(self.list_of_sounds[0])
			index_max = liste_sons.index(self.list_of_sounds[1])
			self.list_of_sounds_between = liste_sons[index_min:index_max]*self.n_repeats
			self.isi = pars['isi']
			self.polling_time = pars['polling_time']
			self.wf = [] #liste de longueur len(liste_of_sounds_between)
			self.output_stream = [] #idem

			random.shuffle(self.list_of_sounds_between)
			print(self.list_of_sounds_between)
		elif self.config_file == 'config/config_sound_player_frequencies.py':
			self.rep_num = pars['rep_num']
			self.frequency_minimum_value = pars['frequency minimum value (in Hz):']
			self.frequency_maximum_value = pars['frequency maximum value (in Hz):']


	def set_participant(self, participant): 
		self.participant = participant

	def set_start_time(self,start_time):
		self.start_time = start_time


	def play_audio_callback(self,in_data, frame_count, time_info,status):
		if self.config_file == 'config/config_sound_player.py':
			if self.terminated :
				a=1
			if self.numero_du_son_en_cours < len(self.list_of_sounds_between)-1:
				print("a")
				data=self.wf[self.numero_du_son_en_cours].readframes(frame_count)
				if time.time()-self.current_time > self.isi:
					print("b")
					self.output_stream[self.numero_du_son_en_cours+1].start_stream()
					# print("a")
					data2=self.wf[self.numero_du_son_en_cours+1].readframes(frame_count)
					# print("a")
					# decodeddata1 = numpy.fromstring(data, numpy.int16)
					# decodeddata2 = numpy.fromstring(data2, numpy.int16)
					data = (data * 0.5 + data2 * 0.5).astype(numpy.int16)

			return (data, pyaudio.paContinue)
		elif self.config_file == 'config/config_sound_player_frequencies.py':
			out = self.samples[:frame_count]
			self.samples = self.samples[frame_count:]
			return (out, pyaudio.paContinue)

	
	def run(self):
		if self.config_file == 'config/config_sound_player.py':
			self.planning_file="data/treadmill_"+self.participant+'_'+str(self.date)+"_sound.csv"
			with open(self.planning_file, 'a') as file :
					writer = csv.writer(file,lineterminator='\n')
					header = ['time','sound_played']
					writer.writerow(header)
			self.numero_du_son_en_cours=0
			start_time=time.time()
			self.current_time=time.time()
			audio = pyaudio.PyAudio()		
			for i in range(len(self.list_of_sounds_between)-1):
				self.wf.append( wave.open("piano/"+self.list_of_sounds_between[i]))
				self.output_stream.append(audio.open(format = audio.get_format_from_width(self.wf[i].getsampwidth()),
							channels = self.wf[i].getnchannels(),
							rate = self.wf[i].getframerate(),
							output = True, 
							stream_callback = self.play_audio_callback))

			
			self.output_stream[0].start_stream()

			if not self.output_stream[self.numero_du_son_en_cours].is_active():
				self.output_stream[self.numero_du_son_en_cours].stop_stream()
				self.output_stream[self.numero_du_son_en_cours].close()
				self.output_stream[self.numero_du_son_en_cours].terminate()
				self.numero_du_son_en_cours+=1
			
			
			
				
		elif self.config_file == 'config/config_sound_player_frequencies.py':
			self.planning_file="data/treadmill_"+self.participant+'_'+str(self.date)+"_sound_from_frequencies.csv"
			#Generating random frequencies between given limits and storing them in the file
			with open(self.planning_file, 'a') as file :
				writer = csv.writer(file,lineterminator='\n')
				writer.writerow(['time',
						'frequency']) 

			for i in range(0,self.rep_num):
				if self.terminated:
					break
				self.n = random.uniform(self.frequency_minimum_value,
					self.frequency_maximum_value)
				p = pyaudio.PyAudio()

				volume = 0.5     # range [0.0, 1.0]
				fs = 44100       # CD quality
				duration = 0.5   # in seconds
				f = self.n            # sine frequency, Hz, may be float
				# generate samples, note conversion to float32 array
				self.samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)


				# for paFloat32 sample values must be in range [-1.0, 1.0]
				stream = p.open(format=pyaudio.paFloat32,
							channels=1,
							rate=fs,
							output=True,
							stream_callback = self.play_audio_callback)

				stream.start_stream()
				self.current_time=time.time()-self.start_time
				with open(self.planning_file, 'a') as file :
					writer = csv.writer(file,lineterminator='\n')
					writer.writerow([self.current_time,
						str(self.n)]) 
				while stream.is_active():
					time.sleep(0.1) # note: in multithread, this may not work (stops the thread)

				stream.stop_stream()
				stream.close()

				p.terminate()
				time.sleep(0.8-duration)

	def stop_playing(self):
		self.terminated = True