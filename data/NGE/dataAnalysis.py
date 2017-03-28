import os
import radical.analytics as ra
import math
import numpy as np
import math
import scipy.stats as st
QUEUE = ['AGENT_EXECUTING_PENDING', 'AGENT_EXECUTING']
REC = ['AGENT_SCHEDULING_PENDING', 'AGENT_SCHEDULING']
SCHED = ['AGENT_SCHEDULING', 'AGENT_EXECUTING_PENDING']
EXEC = ['AGENT_EXECUTING', 'AGENT_STAGING_OUTPUT_PENDING']
def loadData(filePath,cols):
	inputFile = open(filePath)
	inputFile.readline() #consume line
	data = []
	size = len(cols)
	for i in range(0,size):
		data.append([])
	for line in inputFile:
		tokens = line.split(',')
		counter=0
		for i in cols:
			data[counter].append(tokens[i])
			counter+=1
	return data

def loadSessions(path):
        sessions = []
        for sandbox in os.listdir(path):
                if os.path.isdir(path+"/"+sandbox):
                	sessions.append(ra.Session(sandbox, 'radical.pilot'))
        return sessions

def loadSession(path,sandbox):
        return ra.Session(sandbox, 'radical.pilot')

def extractFromSession(session,state):
	return session.concurrency(state)

def extractFromSessions(sessions,state):
	data = []
	for session in sessions:
		data.append(session.concurrency(state))
	return data

def countTime(data,sampling=1):
	last = 0
	counter = 0.0
	for item in data:
		if (item[0]-last) >= sampling:
			last = math.floor(item[0])
			counter+=sampling
	return counter


def extractTimes(path,states,sampling=1):
	currPath = os.getcwd()
	times = []
	numstates = len(states)
	os.chdir(path)	
	for i in range(0,numstates+2):
		times.append([])

        for sandbox in os.listdir('.'):
                if os.path.isdir('./'+sandbox):
			print("Processing "+sandbox)
                        session = ra.Session(sandbox, 'radical.pilot')
			temp = extractFromSession(session,states[numstates-1])
			value1 = temp[len(temp)-1][0]-temp[0][0] 
			value2 = temp[len(temp)-1][1]
			print(str(value1) + " " + str(value2))
			times[numstates-1].append(value1)
			countall = 0
			queueTime = 0
			for i in range(0,numstates-1):
				time = countTime(extractFromSession(session,states[i]),sampling)
				times[i].append(time)
				countall +=time 
				if i == 2:
					queueTime = time
			times[numstates].append(countall)
			times[numstates+1].append(value1-queueTime)
			del session	
        os.chdir(currPath)
	return times


def countServiceTimes(data):
	times = []
	
	for session in data:
		last = -1
		counter = 0
		for item in session:
			print(str(item[0]) + " " +str(last) + " "+ str(counter))
			if last != math.floor(item[0]):
				last = math.floor(item[0])
				counter+=1
		times.append(counter)
	return times

def getAvgAndSDFromList(listValues,scale=1,perc=0.05):
	M1 = 0.0
	M2 = 0.0
	count = 0
	for item in listValues: 
		temp = float(item)/scale
		M1 += temp
		M2 += temp*temp
	 	count+=1
	if count > 1:
		avg = M1/count
		sd = math.sqrt(M2/count - avg*avg)/math.sqrt(count)
		hmin,hmax = st.t.interval(1-perc, count-1, loc=avg,scale=sd)
		return (avg,sd,hmin,hmax,count)
	else:
		return (-1,0,0,0,0)	

def sumLists(data):
	numcols = len(data)
	size = len(data[0])
	newList =[]

	for i in range(0,size):
		sum = 0.0
		for j in range(0,numcols):
			sum+=data[j][i]
		newList.append(sum)
	return newList
		



