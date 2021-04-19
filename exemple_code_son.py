# coding=utf-8
import time
import random
import pyaudio
import wave


def play_sound(sound):
    audio = pyaudio.PyAudio()
    wf = wave.open(sound)
    def play_audio_callback(in_data, frame_count, time_info,status):
        data = wf.readframes(frame_count) #read maximum frame_count frames
        return (data, pyaudio.paContinue)
    #define data stream for playing audio and start it
    output_stream = audio.open(format = audio.get_format_from_width(wf.getsampwidth()),
                            channels = wf.getnchannels(),
                            rate = wf.getframerate(),
                            output = True, 
                            stream_callback = play_audio_callback)
    output_stream.start_stream()
    while output_stream.is_active():
        time.sleep(0.01) # note: in multithread, this may not work (stops the thread)
        continue

# prepare list of trials
n_repeats = 5
sounds = ['sounds/a1.wav', 'sounds/a2.wav']
sound_trials = sounds*n_repeats
random.shuffle(sound_trials)

# loop through them and play
for trial_id, sound_file in enumerate(sound_trials):

    print("trial:%d"%(trial_id+1)+sound_trials[trial_id])
    play_sound(sound_file)
    time.sleep(0.5) # note: in multithread, this may not work (stops the thread)

 

