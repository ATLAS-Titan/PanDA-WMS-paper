set datafile separator ","

!rm 'ET.eps'
set term pos eps color enhanced "Helvetica" 8
set out 'ET.eps' 
set key top right
set xlabel 'Pilot Size (nodes)' 
set ylabel 'Average time (minutes)'
set y2label 'Ratio between Execution time and Walltime'
set title "Execution time vs Total Pilot duration"  
set grid
f(x,y) = "exp1" eq x ? y : 1/0
g(x,y) = "exp2" eq x ? y : 1/0
h(x,y) = "exp3" eq x ? y : 1/0
k(x,y) = "exp4" eq x ? y : 1/0

plot '../weak2/units.csv' u 1:(f(strcol(8),$2)) title '1000' with p,\
'../weak2/units.csv' u 1:(g(strcol(8),$2)) title '2000' with p,\
'../weak2/units.csv' u 1:(h(strcol(8),$2)) title '250' with p,\
'../weak2/units.csv' u 1:(k(strcol(8),$2)) title '500' with p;

reset 
set datafile separator ","

!rm 'ET.gif'
set terminal gif font "arial,8"
set out 'ET.gif' 
set key top right
set xlabel 'Pilot Size (nodes)' 
set ylabel 'Average time (minutes)'
set y2label 'Ratio between Execution time and Walltime'
set title "Execution time vs Total Pilot duration"  
set grid
f(x,y) = "exp1" eq x ? y : 1/0
g(x,y) = "exp2" eq x ? y : 1/0
h(x,y) = "exp3" eq x ? y : 1/0
k(x,y) = "exp4" eq x ? y : 1/0

plot '../data/units2.csv' u 1:(f(strcol(8),$2)) title '1000' with p,\
'../data/units2.csv' u 1:(g(strcol(8),$2)) title '2000' with p,\
'../data/units2.csv' u 1:(h(strcol(8),$2)) title '250' with p,\
'../data/units2.csv' u 1:(k(strcol(8),$2)) title '500' with p;

reset



!rm 'weakET1.eps'
set term pos eps color enhanced "Helvetica" 16
set out 'weakET1.eps' 
set key top right
set xlabel '# AthenaMP/# nodes'  
set ylabel 'Average time (minutes)'
#set title "Execution time vs Total Pilot duration"  
set yrange[0:100]
set xrange[0:5]
set xtics ("256/256" 1,"512/512" 2,"1024/1024" 3,"2048/2048" 4)		
set grid ytics
plot 'UnitFiles.csv' u ($1-0.2):2:4:5:(0.35) title 'AthenaMP Execution time' with boxerrorbars lw 3,\
'PilotTimes.csv' u ($1+0.2):7:9:10:(0.4)  title 'Pilot Duration' with boxerrorbars lw 3;


!rm 'weakET2.eps'
set term pos eps color enhanced "Helvetica" 16
set out 'weakET2.eps' 
set key top right
set xlabel '# AthenaMP/# nodes' 
set ylabel 'Average time (minutes)'
#set title "Execution time vs Total Pilot duration"  
set yrange[0:160]
set xrange[0:5]
set xtics ("1280/256" 1,"2560/512" 2,"5120/1024" 3,"10240/2048" 4)	
set grid ytics
plot 'UnitFiles2.csv' u ($1-0.2):2:4:5:(0.35) title 'AthenaMP Execution time' with boxerrorbars lw 3,\
'PilotTimes2.csv' u ($1+0.2):7:9:10:(0.4)  title 'Pilot Duration' with boxerrorbars lw 3,\
'' u 1:(100) title 'Ideal Pilot Duration' with lines lc 4 lt 7 lw 2;

!rm 'weakOver1.eps'
set term pos eps color enhanced "Helvetica" 16
set out 'weakOver1.eps' 
set key top left
set xlabel '# AthenaMP/# nodes' 
set ylabel 'Average time (seconds)'
#set title "Avera"  
set yrange[0:*]
set xrange[0:5]
set xtics ("256/256" 1,"512/512" 2,"1024/1024" 3,"2048/2048" 4)	
set grid ytics
plot 'Overhead.csv' u ($1):2:4:5:(0.4) title 'Time to start running' with boxerrorbars lw 3;

!rm 'weakOver2.eps'
set term pos eps color enhanced "Helvetica" 16
set out 'weakOver2.eps' 
set key top right
set xlabel '# AthenaMP/# nodes'  
set ylabel 'Average time (seconds)'
#set title "Avera"  
set yrange[0:*]
set xrange[0:5]
#set xtics rotate 90
set xtics ("1280/256" 1,"2560/512" 2,"5120/1024" 3,"10240/2048" 4) 	
set grid ytic
plot 'Overhead2.csv' u ($1):2:4:5:(0.4) title 'Time to start running' with boxerrorbars lw 3;

