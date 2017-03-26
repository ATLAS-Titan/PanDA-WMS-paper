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
#input_file = "task_7244951_data_BNL_PROD_MCORE.json"


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
h_2=TH1F(hist_name_2, hist_title_2, 100, 600., 2300.)
h_3=TH1F(hist_name_3, hist_title_3, n_tests, 0., t_limit)
h_4=TH1F(hist_name_4, hist_title_4, n_tests, 0., t_limit)

# CPU types 
hist_name_5 = 'h5'
hist_title_5 = 'CPU Types'

h_5=TH1F(hist_name_5, hist_title_5, 8, 0., 8.)


hist_name_2_1 = 'h2_1'
hist_title_2_1 = 'Run time for finished jobs. CPU 6274'


hist_name_2_2 = 'h2_2'
hist_title_2_2 = 'Run time for finished jobs. CPU 6378'

hist_name_2_3 = 'h2_3'
hist_title_2_3 = 'Run time for finished jobs. CPU 6376'

hist_name_2_4 = 'h2_4'
hist_title_2_4 = 'Run time for finished jobs. CPU 2431'

hist_name_2_5 = 'h2_5'
hist_title_2_5 = 'Run time for finished jobs. CPU 2350'

hist_name_2_6 = 'h2_6'
hist_title_2_6 = 'Run time for finished jobs. CPU 2376'


h_2_1=TH1F(hist_name_2_1, hist_title_2_1, 100, 600., 2300.)
h_2_2=TH1F(hist_name_2_2, hist_title_2_2, 100, 600., 2300.)
h_2_3=TH1F(hist_name_2_3, hist_title_2_3, 100, 600., 2300.)
h_2_4=TH1F(hist_name_2_4, hist_title_2_4, 100, 600., 2300.)
h_2_5=TH1F(hist_name_2_5, hist_title_2_5, 100, 600., 2300.)
h_2_6=TH1F(hist_name_2_6, hist_title_2_6, 100, 600., 2300.)


#---------------------------------------------------------------

i=0
for line in data['jobs']:


    if 'finished' in line['jobstatus']:
        i+=1
#        print i," ",line['pilottiming'], "\n"
        
        t_stage_in  = line['pilottiming'].split('|')[1]
        t_run       = line['pilottiming'].split('|')[2]
        t_stage_out = line['pilottiming'].split('|')[3]

# determine cpu type        
        cpu = line['cpuconsumptionunit']
#        print cpu
        cpu_list = cpu.split(" ")
        kk = len(cpu_list)
        if kk == 6:
            cpu_type = cpu_list[3]
        if kk == 7:
            cpu_type = cpu_list[4]

        if kk != 6 and kk !=7:
            print cpu

#        print cpu_type

        h_1.Fill(float(t_stage_in))
        h_2.Fill(float(t_run)/60.)
        h_3.Fill(float(t_stage_out))
        if float(t_stage_in) > 0.:
            h_1a.Fill(float(t_stage_in))
        if float(t_stage_out) > 600.:
            h_4.Fill(float(t_stage_out))
            print line['starttime'], " ", t_stage_out

#       Fill CPU type
        h_5.Fill(cpu_type,1.)


# Fill run time for diffeerent cpu time
        if cpu_type == '6274':
            h_2_1.Fill(float(t_run)/60.)

        if cpu_type == '6378':
            h_2_2.Fill(float(t_run)/60.)

        if cpu_type == '6376':
            h_2_3.Fill(float(t_run)/60.)

        if cpu_type == '2431':
            h_2_4.Fill(float(t_run)/60.)

        if cpu_type == '2350':
            h_2_5.Fill(float(t_run)/60.)

        if cpu_type == '2376':
            h_2_6.Fill(float(t_run)/60.)

c1 = TCanvas("c1","Root Canvas",40,20,800,600)

gStyle.SetOptStat(111111)

h_1.SetFillColor(36)
h_1.GetYaxis().SetTitleOffset(1.2)
h_1.SetYTitle('Entries')
h_1.SetXTitle('Time, s')
c1.SetLogy()
h_1.Draw()

t_task = TText(0.35,0.8,'Task '+ task + " SIGNET" )
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


h_2_2.SetTitle("Run time for finished jobs")
h_2_2.SetFillColor(36)
h_2_2.GetYaxis().SetTitleOffset(1.2)
h_2_2.SetYTitle('Entries')
h_2_2.SetXTitle('Run time, min')
c1.SetLogy()
h_2_2.Draw()

h_2_1.SetFillColor(42)
h_2_1.Draw("same")

h_2_3.SetFillColor(22)
h_2_3.Draw("same")

h_2_4.SetFillColor(3)
h_2_4.Draw("same")

h_2_5.SetFillColor(4)
h_2_5.Draw("same")

h_2_6.SetFillColor(2)
h_2_6.Draw("same")


leg = TLegend(0.7,0.45, 0.85, 0.68)
leg.SetHeader("CPU Type")

leg.AddEntry(h_2_2,"AMD 6378","f")
leg.AddEntry(h_2_3,"AMD 6376","f")
leg.AddEntry(h_2_1,"AMD 6274","f")
leg.AddEntry(h_2_4,"AMD 2431","f")
leg.AddEntry(h_2_6,"AMD 2376","f")
leg.AddEntry(h_2_5,"AMD 2350","f")


leg.Draw()

t_task.Draw()
t.Draw()

c1.Modified()
c1.Update()

# optional wait for keypress
input = raw_input('Press Enter to continue, E to exit')
if 'E' in input:
    c1.Close()

if save_option:
#write out histogramm

    fout = TFile(out_name,"RECREATE")
    h_1.Write()
    h_2.Write()
    h_3.Write()
    fout.Close()
