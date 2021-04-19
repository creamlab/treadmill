import numpy as np
import random
import pyaudio as pyaudio
import pickle
import threading
import time
import csv

class SoundPlayerFrequencies(threading.Thread):
    def __init__(self,date,config_file):
        threading.Thread.__init__(self)
        self.parameters={}
        exec(open(config_file).read(),self.parameters)
        pars = self.parameters['params']
        self.rep_num = pars['rep_num']
        self.frequency_minimum_value = pars['frequency minimum value (in Hz):']
        self.frequency_maximum_value = pars['frequency maximum value (in Hz):']
        self.date = date
        self.terminated = False 
    
    def set_participant(self, participant): 
        self.participant = participant

    def set_start_time(self,start_time):
        self.start_time = start_time


    def run(self):

        self.planning_file="data/treadmill_"+self.participant+'_'+str(self.date)+"_sound_from_frequencies.csv"
        #Generating random frequencies between given limits and storing them in the file
        with open(self.planning_file, 'a') as file :
            writer = csv.writer(file,lineterminator='\n')
            writer.writerow(['time',
                    'frequency']) 

        for i in range(0,self.rep_num):
            if self.terminated:
                break
            n = random.uniform(self.frequency_minimum_value,
                self.frequency_maximum_value)
            p = pyaudio.PyAudio()

            volume = 0.5     # range [0.0, 1.0]
            fs = 44100       # CD quality
            duration = 2.0   # in seconds
            f = n            # sine frequency, Hz, may be float
            # generate samples, note conversion to float32 array
            samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)

            # for paFloat32 sample values must be in range [-1.0, 1.0]
            stream = p.open(format=pyaudio.paFloat32,
                        channels=2,
                        rate=fs,
                        output=True)

            self.current_time=time.time()-self.start_time
            with open(self.planning_file, 'a') as file :
                writer = csv.writer(file,lineterminator='\n')
                writer.writerow([self.current_time,
                    str(n)])    

            # play
            stream.write(volume*samples)

            stream.stop_stream()
            stream.close()

            p.terminate()

    def stop_playing(self):
        self.terminated = True