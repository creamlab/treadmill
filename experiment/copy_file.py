import shutil

def copy_file(file,participant,order,date):
	newfile = file[7:]
	source=r'C:/Users/qdecu/Documents/StageTapis/Treadmill/treadmill/experiment/' + file
	filename = 'treadmill_participant_'+participant+"_order_"+str(order)+'_'+str(date)+'_'+ newfile[:-3] + '.py'
	destination=r'C:/Users/qdecu/Documents/StageTapis/Treadmill/treadmill/experiment/data/'+filename
	shutil.copyfile(source, destination)
	return filename


