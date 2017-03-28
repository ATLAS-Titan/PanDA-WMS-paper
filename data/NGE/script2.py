import dataAnalysis as da

path = "strong"
states = [da.REC,da.SCHED,da.QUEUE,da.EXEC]
sampling = 0.1
output = path+".csv"
outfile = open(output,"w+")
#256
folder = "exp1"
print("Processing "+folder)
times = da.extractTimes(path+"/"+folder,states,sampling)
(avg,sd,hmin,hmax,count) = da.getAvgAndSDFromList(times[5],1.0,perc=0.05)
outfile.write("1 " +  str(avg) + " " + str(sd) + " "+ str(hmin) + " " + str(hmax) +" ")
(avg,sd,hmin,hmax,count) = da.getAvgAndSDFromList(times[4],1.0,perc=0.05)
outfile.write("1 " +  str(avg) + " " + str(sd) + " "+ str(hmin) + " " + str(hmax) +" ")
(avg,sd,hmin,hmax,count) = da.getAvgAndSDFromList(times[2],1.0,perc=0.05)
outfile.write("1 " +  str(avg) + " " + str(sd) + " "+ str(hmin) + " " + str(hmax) +" ")
(avg,sd,hmin,hmax,count) = da.getAvgAndSDFromList(times[3],1.0,perc=0.05)
outfile.write("1 " +  str(avg) + " " + str(sd) + " "+ str(hmin) + " " + str(hmax) +"\n")
#512
folder = "exp2"
print("Processing "+folder)
times = da.extractTimes(path+"/"+folder,states,sampling)
(avg,sd,hmin,hmax,count) = da.getAvgAndSDFromList(times[5],1.0,perc=0.05)
outfile.write("2 " +  str(avg) + " " + str(sd) + " "+ str(hmin) + " " + str(hmax) +" ")
(avg,sd,hmin,hmax,count) = da.getAvgAndSDFromList(times[4],1.0,perc=0.05)
outfile.write("2 " +  str(avg) + " " + str(sd) + " "+ str(hmin) + " " + str(hmax) +" ")
(avg,sd,hmin,hmax,count) = da.getAvgAndSDFromList(times[2],1.0,perc=0.05)
outfile.write("2 " +  str(avg) + " " + str(sd) + " "+ str(hmin) + " " + str(hmax) +" ")
(avg,sd,hmin,hmax,count) = da.getAvgAndSDFromList(times[3],1.0,perc=0.05)
outfile.write("2 " +  str(avg) + " " + str(sd) + " "+ str(hmin) + " " + str(hmax) +"\n")
#1024
folder = "exp3"
print("Processing "+folder)
times = da.extractTimes(path+"/"+folder,states,sampling)
(avg,sd,hmin,hmax,count) = da.getAvgAndSDFromList(times[5],1.0,perc=0.05)
outfile.write("3 " +  str(avg) + " " + str(sd) + " "+ str(hmin) + " " + str(hmax) +" ")
(avg,sd,hmin,hmax,count) = da.getAvgAndSDFromList(times[4],1.0,perc=0.05)
outfile.write("3 " +  str(avg) + " " + str(sd) + " "+ str(hmin) + " " + str(hmax) +" ")
(avg,sd,hmin,hmax,count) = da.getAvgAndSDFromList(times[2],1.0,perc=0.05)
outfile.write("3 " +  str(avg) + " " + str(sd) + " "+ str(hmin) + " " + str(hmax) +" ")
(avg,sd,hmin,hmax,count) = da.getAvgAndSDFromList(times[3],1.0,perc=0.05)
outfile.write("3 " +  str(avg) + " " + str(sd) + " "+ str(hmin) + " " + str(hmax) +"\n")
#2048
folder = "exp4"
print("Processing "+folder)
times = da.extractTimes(path+"/"+folder,states,sampling)
(avg,sd,hmin,hmax,count) = da.getAvgAndSDFromList(times[5],1.0,perc=0.05)
outfile.write("4 " +  str(avg) + " " + str(sd) + " "+ str(hmin) + " " + str(hmax) +" ")
(avg,sd,hmin,hmax,count) = da.getAvgAndSDFromList(times[4],1.0,perc=0.05)
outfile.write("4 " +  str(avg) + " " + str(sd) + " "+ str(hmin) + " " + str(hmax) +" ")
(avg,sd,hmin,hmax,count) = da.getAvgAndSDFromList(times[2],1.0,perc=0.05)
outfile.write("4 " +  str(avg) + " " + str(sd) + " "+ str(hmin) + " " + str(hmax) +" ")
(avg,sd,hmin,hmax,count) = da.getAvgAndSDFromList(times[3],1.0,perc=0.05)
outfile.write("4 " +  str(avg) + " " + str(sd) + " "+ str(hmin) + " " + str(hmax) +"\n")
