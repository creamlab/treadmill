import os

liste_sons=os.listdir("C:/Users/qdecu/Downloads/piano/")
print(liste_sons)

for trial_id, sound_file in enumerate(liste_sons):
	son_converti = liste_sons[trial_id].replace('.',"")
	son_converti1 = son_converti[:-4] + ".wav"
	myCommand = "ffmpeg -i " + r"C:/Users/qdecu/Downloads/piano/" + sound_file + " -af loudnorm,aformat=s16,silenceremove=start_periods=1:start_silence=0.05:start_threshold=-60dB,afade=out:st=1.25:d=0.25,afade=in:st=0:d=0.05 -to 1.5 " + r"C:/Users/qdecu/Downloads/piano/" + son_converti1
	os.system(myCommand)
	# son_converti2 = son_converti1[:-4] +"2" + ".wav"
	myCommand2 = "ffmpeg -i " + r"C:/Users/qdecu/Downloads/piano/" + son_converti1 + " -acodec pcm_s16le -ar 44100 " + r"C:/Users/qdecu/Documents/StageTapis/Treadmill/treadmill/piano/" + son_converti1
	os.system(myCommand2)






