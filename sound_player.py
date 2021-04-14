import time
import random
import pyaudio
import wave
import csv

class SoundPlayer:
	def __init__(self,date):
		self.n_repeats = 10
		self.list_of_sounds = ['sounds/a1.wav', 'sounds/a2.wav']*self.n_repeats
		self.time_sleep=0.25
		self.date=date

		random.shuffle(self.list_of_sounds)
		print(self.list_of_sounds)

	def set_participant(self, participant): 
		self.participant = participant


	def play_audio_callback(self,in_data, frame_count, time_info,status):
		data = self.wf.readframes(frame_count) #read maximum frame_count frames
		return (data, pyaudio.paContinue)


	def start_playing(self,start_time):
		self.planning_file="data/treadmill_"+self.participant+'_'+str(self.date)+"_sound.csv"
		self.callback_counter=0
		with open(self.planning_file, 'a') as file :
				writer = csv.writer(file,lineterminator='\n')
				header = ['time','sound_played']
				writer.writerow(header)
		for trial_id, sound_file in enumerate(self.list_of_sounds):
			audio = pyaudio.PyAudio()
			self.wf = wave.open(sound_file)
			print (self.list_of_sounds[trial_id])
			output_stream = audio.open(format = audio.get_format_from_width(self.wf.getsampwidth()),
							channels = self.wf.getnchannels(),
							rate = self.wf.getframerate(),
							output = True, 
							stream_callback = self.play_audio_callback)
			if self.callback_counter==0:
				self.current_time=time.time()-start_time
			output_stream.start_stream()
			with open(self.planning_file, 'a') as file :
				writer = csv.writer(file,lineterminator='\n')
				writer.writerow([self.time_sleep*self.callback_counter+self.current_time]+[str(self.list_of_sounds[self.callback_counter])])
				self.callback_counter+=1
			while output_stream.is_active():
				time.sleep(self.time_sleep) # note: in multithread, this may not work (stops the thread)
				continue











