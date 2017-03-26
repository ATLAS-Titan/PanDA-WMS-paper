#!/bin/env python
#from ROOT import *
from  ROOT import TFile
from  ROOT import TH1F
from  ROOT import TCanvas
from  ROOT import TText
from  ROOT import TGraph
from  ROOT import TMultiGraph
from  ROOT import TLegend
from  ROOT import gStyle
from  ROOT import gPad

from array import array

from datetime import datetime


#
# option to save a canvas
#
save_option = False
#save_option = True

import json
from pprint import pprint

input_file = 'task_5387358__data.json'
input_file = "task_5890530_data.json"
input_file = "task_7353647_data_cleaned.json"

input_file = "task_7244729_data_SIGNET.json"
input_file = "task_7244951_data_BNL_PROD_MCORE.json"


# Output file name
out_name = input_file.split(".")[0] + ".root"

# Task ID

task_id = input_file.split(".")[0].split("_")[1]
print task_id

print out_name



with open(input_file) as data_file:    
    data = json.load(data_file)

#pprint(data)

n_tests = len(data)
print n_tests

#exit()
#---------------------------------------------------------------
system ='titan'

task   = task_id

n_tests = 180
t_limit = 1800.

hist_name_1 = 'h1'
hist_title_1 = 'Stage-In time for finished jobs'

hist_name_1a = 'h1a'
hist_title_1a = 'Stage-In time for finished jobs. T_stage_in > 0 s'

hist_name_2 = 'h2'
hist_title_2 = 'Run time for finished jobs'

hist_name_3 = 'h3'
hist_title_3 = 'Stage-Out time for finished jobs'

hist_name_4 = 'h4'
hist_title_4 = 'Stage-Out time for finished jobs. T_stage_out > 600 s'


h_1=TH1F(hist_name_1, hist_title_1, n_tests, 0., t_limit)
h_1a=TH1F(hist_name_1a, hist_title_1a, n_tests, 0., t_limit)
h_2=TH1F(hist_name_2, hist_title_2, 100, 300., 1900.)
h_3=TH1F(hist_name_3, hist_title_3, n_tests, 0., t_limit)
h_4=TH1F(hist_name_4, hist_title_4, n_tests, 0., t_limit)

# CPU types 
hist_name_5 = 'h5'
hist_title_5 = 'CPU Types'

h_5=TH1F(hist_name_5, hist_title_5, 8, 0., 8.)


hist_name_2_1 = 'h2_1'
hist_title_2_1 = 'Run time for finished jobs. CPU X5660'


hist_name_2_2 = 'h2_2'
hist_title_2_2 = 'Run time for finished jobs. CPU E5-2660v2'

hist_name_2_3 = 'h2_3'
hist_title_2_3 = 'Run time for finished jobs. CPU E5-2660v0'

hist_name_2_4 = 'h2_4'
hist_title_2_4 = 'Run time for finished jobs. CPU X5650'

hist_name_2_5 = 'h2_5'
hist_title_2_5 = 'Run time for finished jobs. CPU E5-2660v3'

hist_name_2_6 = 'h2_6'
hist_title_2_6 = 'Run time for finished jobs. CPU X5560'


h_2_1=TH1F(hist_name_2_1, hist_title_2_1, 100, 300., 1900.)
h_2_2=TH1F(hist_name_2_2, hist_title_2_2, 100, 300., 1900.)
h_2_3=TH1F(hist_name_2_3, hist_title_2_3, 100, 300., 1900.)
h_2_4=TH1F(hist_name_2_4, hist_title_2_4, 100, 300., 1900.)
h_2_5=TH1F(hist_name_2_5, hist_title_2_5, 100, 300., 1900.)
h_2_6=TH1F(hist_name_2_6, hist_title_2_6, 100, 300., 1900.)




# Processing rate histograms

# All cpus in h20
hist_name_20 = 'h20'
hist_title_20 = 'Event rate for finished jobs. All CPUs'


hist_name_20_1 = 'h20_1'
hist_title_20_1 = 'Event rate for finished jobs. CPU X5660'

hist_name_20_2 = 'h20_2'
hist_title_20_2 = 'Event rate for finished jobs. CPU E5-2660v2'

hist_name_20_3 = 'h20_3'
hist_title_20_3 = 'Event rate for finished jobs. CPU E5-2660v0'

hist_name_20_4 = 'h20_4'
hist_title_20_4 = 'Event rate for finished jobs. CPU X5650'

hist_name_20_5 = 'h20_5'
hist_title_20_5 = 'Event rate for finished jobs. CPU E5-2660v3'

hist_name_20_6 = 'h20_6'
hist_title_20_6 = 'Event rate for finished jobs. CPU X5560'


h_20=TH1F(hist_name_20, hist_title_20, 100,  0., 3.)

h_20_1=TH1F(hist_name_20_1, hist_title_20_1, 100, 0., 3.)
h_20_2=TH1F(hist_name_20_2, hist_title_20_2, 100, 0., 3.)
h_20_3=TH1F(hist_name_20_3, hist_title_20_3, 100, 0., 3.)
h_20_4=TH1F(hist_name_20_4, hist_title_20_4, 100, 0., 3.)
h_20_5=TH1F(hist_name_20_5, hist_title_20_5, 100, 0., 3.)
h_20_6=TH1F(hist_name_20_6, hist_title_20_6, 100, 0., 3.)


rate_list = []
rate_list.append(h_20_1)
rate_list.append(h_20_2)
rate_list.append(h_20_3)
rate_list.append(h_20_4)
rate_list.append(h_20_5)
rate_list.append(h_20_6)

#---------------------------------------------------------------
type_list =['X5660','E5-2660+v2+2.20GHz', 'E5-2660+0+2.20GHz', 'X5650', 'E5-2660+v3+2.60GHz', 'X5560']

hepspec_list = [8.3, 9.6, 9.6, 8.0, 11.2, 7.1]

i=0
for line in data['jobs']:


    if 'finished' in line['jobstatus']:
        i+=1
#        print i," ",line['pilottiming'], "\n"
        

        if line["computingsite"] != "BNL_PROD_MCORE":
            print line["computingsite"]

        t_stage_in  = line['pilottiming'].split('|')[1]
        t_run       = line['pilottiming'].split('|')[2]
        t_stage_out = line['pilottiming'].split('|')[3]

# determine cpu type        
        cpu = line['cpuconsumptionunit']
#        print cpu
        cpu_list = cpu.split()
#        print cpu_list

        kk = len(cpu_list)
#        print kk
        if kk == 8:
            cpu_type = cpu_list[3]
        if kk == 9:
            cpu_type = cpu_list[3]+"+"+cpu_list[4]+"+"+cpu_list[6]

        if kk !=8 and kk !=9:
            print kk, "", cpu_list

        n_events = line["nevents"]
#        print "n_events = ", n_events
#        print cpu_type

        h_1.Fill(float(t_stage_in))
        h_2.Fill(float(t_run)/60.,1.)
        h_3.Fill(float(t_stage_out))
        if float(t_stage_in) > 0.:
            h_1a.Fill(float(t_stage_in),1.)
        if float(t_stage_out) > 600.:
            h_4.Fill(float(t_stage_out))
            print line['starttime'], " ", t_stage_out

#       Fill CPU type
        h_5.Fill(cpu_type,1.)

#       Fill event rate for all CPUs
        t_run_min = float(t_run)/60.

        h_20.Fill(float(n_events)/t_run_min, 1.)



# Fill run time for diffeerent cpu time
        if cpu_type == 'X5660':
            h_2_1.Fill(float(t_run)/60.,1.)
            h_20_1.Fill(float(n_events)/t_run_min, 1.)
            
        if cpu_type == 'E5-2660+v2+2.20GHz':
            h_2_2.Fill(float(t_run)/60.,1.)
            h_20_2.Fill(float(n_events)/t_run_min, 1.)

        if cpu_type == 'E5-2660+0+2.20GHz':
            h_2_3.Fill(float(t_run)/60.,1.)
            h_20_3.Fill(float(n_events)/t_run_min, 1.)

        if cpu_type == 'X5650':
            h_2_4.Fill(float(t_run)/60.,1.)
            h_20_4.Fill(float(n_events)/t_run_min, 1.)

        if cpu_type == 'E5-2660+v3+2.60GHz':
            h_2_5.Fill(float(t_run)/60.,1.)
            h_20_5.Fill(float(n_events)/t_run_min, 1.)

        if cpu_type == 'X5560':
            h_2_6.Fill(float(t_run)/60.,1.)
            h_20_6.Fill(float(n_events)/t_run_min, 1.)


c1 = TCanvas("c1","Root Canvas",40,20,800,600)

gStyle.SetOptStat(111111)

h_1.SetFillColor(36)
h_1.GetYaxis().SetTitleOffset(1.2)
h_1.SetYTitle('Entries')
h_1.SetXTitle('Time, s')
c1.SetLogy()
h_1.Draw()

t_task = TText(0.20,0.85,'Task '+ task + " BNL_PROD_MCORE" )
t_task.SetNDC()
t_task.Draw()

#print time stamp
t_time = datetime.now()
t_label = 'SP ' + t_time.strftime("%Y-%m-%d")

t = TText(0.905,0.6,t_label)
t.SetNDC()
t.SetTextAlign(21) # middle, bottom
t.SetTextAngle(-90)
t.SetTextSize(0.017)
t.Draw()

c1.Modified()
c1.Update()

# optional wait for keypress
input = raw_input('Press Enter to continue, E to exit')
if 'E' in input:
    c1.Close()


h_2.SetFillColor(37)
h_2.GetYaxis().SetTitleOffset(1.2)
h_2.SetYTitle('Entries')
h_2.SetXTitle('Time, min.')
h_2.Draw()

t_task.Draw()
t.Draw()

c1.Modified()
c1.Update()




# optional wait for keypress
input = raw_input('Press Enter to continue, E to exit')
if 'E' in input:
    c1.Close()


h_3.SetFillColor(38)
h_3.GetYaxis().SetTitleOffset(1.2)
h_3.SetYTitle('Entries')
h_3.SetXTitle('Time, s')
h_3.Draw()
c1.SetLogy()

t_task.Draw()
t.Draw()

c1.Modified()
c1.Update()

# optional wait for keypress
input = raw_input('Press Enter to continue, E to exit')
if 'E' in input:
    c1.Close()


h_4.SetFillColor(38)
h_4.GetYaxis().SetTitleOffset(1.2)
h_4.SetYTitle('Entries')
h_4.SetXTitle('Time, s')
h_4.Draw()
c1.SetLogy()

t_task.Draw()
t.Draw()

c1.Modified()
c1.Update()



h_1a.SetFillColor(36)
h_1a.GetYaxis().SetTitleOffset(1.2)
h_1a.SetYTitle('Entries')
h_1a.SetXTitle('Time, s')
c1.SetLogy()
h_1a.Draw()

t_task.Draw()
t.Draw()

c1.Modified()
c1.Update()

# optional wait for keypress
input = raw_input('Press Enter to continue, E to exit')
if 'E' in input:
    c1.Close()


h_5.SetFillColor(36)
h_5.GetYaxis().SetTitleOffset(1.2)
h_5.SetYTitle('Entries')
h_5.SetXTitle('CPU Type')
c1.SetLogy()
h_5.Draw()

t_task.Draw()
t.Draw()

c1.Modified()
c1.Update()

# optional wait for keypress
input = raw_input('Press Enter to continue, E to exit')
if 'E' in input:
    c1.Close()


h_2_5.SetTitle("Run time for finished jobs")
h_2_5.SetFillColor(36)
h_2_5.GetYaxis().SetTitleOffset(1.2)
h_2_5.SetYTitle('Entries')
h_2_5.SetXTitle('Run time, min')
c1.SetLogy()
h_2_5.Draw()

h_2_2.SetFillColor(2)
h_2_2.Draw("same")

h_2_1.SetFillColor(42)
h_2_1.Draw("same")

h_2_3.SetFillColor(22)
h_2_3.Draw("same")

h_2_4.SetFillColor(3)
h_2_4.Draw("same")

h_2_6.SetFillColor(4)
h_2_6.Draw("same")


leg = TLegend(0.7,0.45, 0.85, 0.68)
leg.SetHeader("CPU Type")

leg.AddEntry(h_2_2,"E5-2660v2","f")
leg.AddEntry(h_2_3,"E5-2660v0","f")
leg.AddEntry(h_2_1,"X5660","f")
leg.AddEntry(h_2_4,"X5650","f")
leg.AddEntry(h_2_6,"X5560","f")
leg.AddEntry(h_2_5,"E5-2660v3","f")


leg.Draw()

t_task.Draw()
t.Draw()

c1.Modified()
c1.Update()

# optional wait for keypress
input = raw_input('Press Enter to continue, E to exit')
if 'E' in input:
    c1.Close()


# Plot rate histograms
h_20.SetFillColor(17)
h_20.GetYaxis().SetTitleOffset(1.2)
h_20.SetYTitle('Entries')
h_20.SetXTitle('Events per minute')
h_20.Draw()

t_task.Draw()
t.Draw()

c1.Modified()
c1.Update()

# optional wait for keypress
input = raw_input('Press Enter to continue, E to exit')
if 'E' in input:
    c1.Close()


h_20_1.SetTitle("Event rate for finished jobs")
h_20_1.SetFillColor(42)
h_20_1.GetYaxis().SetTitleOffset(1.2)
h_20_1.SetYTitle('Entries')
h_20_1.SetXTitle('Events per minute')
c1.SetLogy()
h_20_1.Draw()

h_20_2.SetFillColor(2)
h_20_2.Draw("same")

h_20_5.SetFillColor(36)
h_20_5.Draw("same")

h_20_3.SetFillColor(22)
h_20_3.Draw("same")

h_20_4.SetFillColor(3)
h_20_4.Draw("same")

h_20_6.SetFillColor(4)
h_20_6.Draw("same")


leg = TLegend(0.7,0.45, 0.85, 0.68)
leg.SetHeader("CPU Type")

leg.AddEntry(h_20_2,"E5-2660v2","f")
leg.AddEntry(h_20_3,"E5-2660v0","f")
leg.AddEntry(h_20_1,"X5660","f")
leg.AddEntry(h_20_4,"X5650","f")
leg.AddEntry(h_20_6,"X5560","f")
leg.AddEntry(h_20_5,"E5-2660v3","f")


leg.Draw()

t_task.Draw()
t.Draw()

c1.Modified()
c1.Update()

# optional wait for keypress
input = raw_input('Press Enter to continue, E to exit')
if 'E' in input:
    c1.Close()

weighted_rate    = 0.
sum_of_weights   = 0.
weighted_hepspec = 0.

i=0
for h in rate_list:
    h_mean = h.GetMean()
    h_entries = h.GetEntries()
    
    weighted_rate    += h_mean * float(h_entries)
    weighted_hepspec += hepspec_list[i] * float(h_entries)
    sum_of_weights   += h_entries

    i += 1
    print "i= ",i ,"CPU =",type_list[i-1], " M = ", h_mean, " E = ", h_entries, "HEPSPEC = ", hepspec_list[i-1]

result = weighted_rate/float(sum_of_weights)
hepspec_result = weighted_hepspec/float(sum_of_weights)

print "Weighter event rate = ", result
print "Weighted HEPSPEC = ", hepspec_result
 
if save_option:
#write out histogramm

    fout = TFile(out_name,"RECREATE")
    h_1.Write()
    h_2.Write()
    h_3.Write()
    fout.Close()
