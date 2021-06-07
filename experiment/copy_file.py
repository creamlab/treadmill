import shutil

def copy_file(file,participant):
	newfile = file[7:]
	source=r'C:/Users/qdecu/Documents/StageTapis/Treadmill/treadmill/experiment/' + file
	destination=r'C:/Users/qdecu/Documents/StageTapis/Treadmill/treadmill/experiment/data/' + newfile[:-3] + '_' + str(participant) +'.py'
	shutil.copyfile(source, destination)



