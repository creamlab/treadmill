import time
import random
import pyaudio
import wave
import csv
import pickle
import threading

class SoundPlayer(threading.Thread):
	def __init__(self,date,config_file):
		threading.Thread.__init__(self)
		self.parameters={}
		exec(open(config_file).read(),self.parameters)
		pars = self.parameters['params']
		self.n_repeats = pars['n_repeats']
		self.list_of_sounds = pars['list_of_sounds']*self.n_repeats
		self.isi = pars['isi']
		self.polling_time = pars['polling_time']
		self.date = date
		self.terminated = False 

		random.shuffle(self.list_of_sounds)
		print(self.list_of_sounds)

	def set_participant(self, participant): 
		self.participant = participant

	def set_start_time(self,start_time):
		self.start_time = start_time


	def play_audio_callback(self,in_data, frame_count, time_info,status):
		data = self.wf.readframes(frame_count) #read maximum frame_count frames
		return (data, pyaudio.paContinue)

	
	def run(self):

		self.planning_file="data/treadmill_"+self.participant
					+'_'+str(self.date)+"_sound.csv"
		with open(self.planning_file, 'a') as file :
				writer = csv.writer(file,lineterminator='\n')
				header = ['time','sound_played']
				writer.writerow(header)

		for trial_id, sound_file in enumerate(self.list_of_sounds):
			if self.terminated :
				break
			audio = pyaudio.PyAudio()
			self.wf = wave.open(sound_file)
			print (self.list_of_sounds[trial_id])
			output_stream = audio.open(format = audio.get_format_from_width(self.wf.getsampwidth()),
						channels = self.wf.getnchannels(),
						rate = self.wf.getframerate(),
						output = True, 
						stream_callback = self.play_audio_callback)
			self.current_time=time.time()-self.start_time
			output_stream.start_stream()
			with open(self.planning_file, 'a') as file :
				writer = csv.writer(file,lineterminator='\n')
				writer.writerow([self.current_time,
					sound_file])
			while output_stream.is_active():
				time.sleep(self.polling_time) # note: in multithread, this may not work (stops the thread)
			output_stream.stop_stream()
			output_stream.close()
			time.sleep(self.isi)


	def stop_playing(self):
		self.terminated = True











