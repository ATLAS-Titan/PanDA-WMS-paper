import numpy
import dataAnalysis as da
#hashMap={'exp1':1000, 'exp2':2000,'exp3':250,'exp4':500}
hashMap={'exp1':256, 'exp2':512,'exp3':1024,'exp4':2048}
sessionFile ="sessions.csv"
pilotFile= "pilots.csv"
CUFile="units.csv"
path ="../weak2/"

QTFile = "PilotTimes2.csv"
UnitFile ="UnitFiles2.csv"
OverheadFile = "Overhead2.csv"

PSIZE_PF_I=6
PRUN_PF_I=2
QT_PF_I=1

EFFTIME_CU_I=1
LASTTIME_I = 6

SES_ST =8
SES_SP =13
SES_NCU =19

PIL_ST =3
PIL_SP =6
PIL_NCU =9

def ComputeOverhead2(inputPath,outputPath):

	infile = open(inputPath)
	infile.readline() # Consunme first line
	outfile= open("./"+outputPath,"w+")
	Overhead = {}
	for key in hashMap.keys():
		Overhead[key] = []
	for line in infile:
		tokens = line.split(',')
		sum = 0
		for i in range(PIL_ST,PIL_SP):
			sum+=float(tokens[i])
		print(str(sum) +  " "+ tokens[PIL_SP])		
		Overhead[tokens[PIL_SP]] +=[sum]
	for k in Overhead.keys():
		(avg,sd,hmin,hmax,count) = da.getAvgAndSDFromList(Overhead[k],1.0,perc=0.05)
		outfile.write(str(hashMap[k])  + " " + str(avg) + " " + str(sd) + " " + str(hmin)  + " " + str(hmax) + " "+ k +" ")
		(avg,sd,hmin,hmax,count) = da.getAvgAndSDFromList(Overhead[k],float(tokens[PIL_NCU]),perc=0.05)
		outfile.write(str(hashMap[k])  + " " + str(avg) + " " + str(sd) + " " + str(hmin)  + " " + str(hmax) + " "+ k +"\n")	
	outfile.close()
	infile.close()






def ComputeOverhead(inputPath,outputPath):

	infile = open(inputPath)
	infile.readline() # Consunme first line
	outfile= open("./"+outputPath,"w+")
	Overhead = {}
	for key in hashMap.keys():
		Overhead[key] = []
	for line in infile:
		tokens = line.split(',')
		sum = float(tokens[2])-float(tokens[7])
		Overhead[tokens[SES_SP]] +=[sum]
	for k in Overhead.keys():
		(avg,sd,hmin,hmax,count) = da.getAvgAndSDFromList(Overhead[k],1.0,perc=0.05)
		outfile.write(str(hashMap[k])  + " " + str(avg) + " " + str(sd) + " " + str(hmin)  + " " + str(hmax) + " "+ k +"\n")	
	outfile.close()
	infile.close()





def ComputeExecutionTime(inputPath,outputPath):

	infile = open(inputPath)
	infile.readline() # Consume first line
	outfile= open("./"+outputPath,"w+")
	EffTime = {}
	Overhead = {}
	TotDur = {}
	for key in hashMap.keys():
		EffTime[key] =[]
		Overhead[key] = []
		TotDur[key] = []
	for line in infile:
		tokens = line.split(',')
		EffTime[tokens[LASTTIME_I+1]]+=[tokens[QT_PF_I]]	
		sum = 0
		for i in range(2,LASTTIME_I):
			if(i != 4):
				sum+=float(tokens[i])
		#print(str(sum) + " "+tokens[LASTTIME_I+1])
		Overhead[tokens[LASTTIME_I+1]] +=[sum]
		TotDur[tokens[LASTTIME_I+1]] +=[float(sum)+float(tokens[QT_PF_I])]
	for k in EffTime.keys():
		(avg,sd,hmin,hmax,count) = da.getAvgAndSDFromList(EffTime[k],60.0,perc=0.05)
		outfile.write(str(hashMap[k])  + " " + str(avg) + " " + str(sd) + " " + str(hmin)  + " " + str(hmax) + " " )
		(avg,sd,hmin,hmax,count) = da.getAvgAndSDFromList(Overhead[k],60.0,perc=0.05)
		outfile.write(str(hashMap[k])  + " " + str(avg) + " " + str(sd) + " " + str(hmin)  + " " + str(hmax) + " " )
		(avg,sd,hmin,hmax,count) = da.getAvgAndSDFromList(TotDur[k],60.0,perc=0.05)
		outfile.write(str(hashMap[k])  + " " + str(avg) + " " + str(sd) + " " + str(hmin)  + " " + str(hmax) + "\n")	
	outfile.close()
	infile.close()




def ComputePilotTimes(inputPath,outputPath):

	infile = open(inputPath)
	infile.readline() # Consunme first line
	outfile= open("./"+outputPath,"w+")
	queueTime = {}
	duration = {}
	for key in hashMap.keys():
		queueTime[key] =[]
		duration[key] =[]
	for line in infile:
		tokens = line.split(',')
		queueTime[tokens[PSIZE_PF_I]]+=[tokens[QT_PF_I]]	
		duration[tokens[PSIZE_PF_I]]+=[tokens[PRUN_PF_I]]
	for k in queueTime.keys():
		(avg,sd,hmin,hmax,count) = da.getAvgAndSDFromList(queueTime[k],60.0,perc=0.05)
		outfile.write(str(hashMap[k])  + " " + str(avg) + " " + str(sd) + " " + str(hmin)  + " " + str(hmax) + " ")
		(avg,sd,hmin,hmax,count) = da.getAvgAndSDFromList(duration[k],60.0,perc=0.05)
		outfile.write(str(hashMap[k])  + " " + str(avg) + " " + str(sd) + " " + str(hmin)  + " " + str(hmax) + "\n")
	
	outfile.close()
	infile.close()
def main():
	ComputePilotTimes(path+pilotFile,QTFile)
	ComputeExecutionTime(path+CUFile,UnitFile)
	ComputeOverhead(path+sessionFile,OverheadFile)
if __name__=="__main__":
	main()
