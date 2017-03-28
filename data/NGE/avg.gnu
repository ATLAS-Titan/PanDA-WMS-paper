!rm 'weakET1.eps'
set term pos eps color enhanced "Helvetica" 16
set out 'weakET1.eps' 
set key top left
set xlabel '# AthenaMP/# nodes'  
set ylabel 'Average time (seconds)'
#set title "Execution time vs Total Pilot duration"  
set yrange[0:7200]
set xrange[0:5]
set xtics ("250/250" 1,"500/500" 2,"1000/1000" 3,"2000/2000" 4)		
set grid ytics
set style fill solid 1.0 border rgb 'black'
plot 'data.csv' u ($1-0.2):17:19:20:(0.35) title 'Pilot Duration' with boxerrorbars fs solid lc rgb 'red' lw 3,\
'data.csv' u ($1+0.2):2:4:5:(0.35)  title 'AthenaMP Execution time' with boxerrorbars fs solid lc rgb 'blue' lw 3;



!rm 'weakOver1.eps'
set term pos eps color enhanced "Helvetica" 16
set out 'weakOver1.eps' 
set key top left
set xlabel '# AthenaMP/# nodes' 
set ylabel 'Average time (seconds)'
#set title "Avera"  
set yrange[0:*]
set xrange[0:5]
set xtics ("250/250" 1,"500/500" 2,"1000/1000" 3,"2000/2000" 4)	
set grid ytics
set style fill solid 1.0 border rgb 'black'
plot 'data.csv' u ($1):12:14:15:(0.4) title 'Overhead' with boxerrorbars fs solid lc rgb 'red' lw 3;




!rm 'weakET2.eps'
set term pos eps color enhanced "Helvetica" 16
set out 'weakET2.eps' 
set key top left
set xlabel '# AthenaMP/# nodes'  
set ylabel 'Average time (seconds)'
#set title "Execution time vs Total Pilot duration"  
set yrange[0:8400]
set xrange[0:5]
set xtics ("1280/256" 1,"2560/512" 2,"5120/1024" 3,"10240/2048" 4)		
set grid ytics
set style fill solid 1.0 border rgb 'black'
plot 'weak2.csv' u ($1-0.2):17:19:20:(0.35) title 'Pilot Duration' with boxerrorbars fs solid lc rgb 'red' lw 3,\
'weak2.csv' u ($1+0.2):2:4:5:(0.35)  title 'AthenaMP Execution time (5 executions)' with boxerrorbars fs solid lc rgb 'blue' lw 3;



!rm 'weakOver2.eps'
set term pos eps color enhanced "Helvetica" 16
set out 'weakOver2.eps' 
set key top left
set xlabel '# AthenaMP/# nodes' 
set ylabel 'Average time (seconds)'
#set title "Avera"  
set yrange[0:*]
set xrange[0:5]
set xtics ("1280/256" 1,"2560/512" 2,"5120/1024" 3,"10240/2048" 4)	
set grid ytics
set style fill solid 1.0 border rgb 'black'
plot 'weak2.csv' u ($1):12:14:15:(0.4) title 'Overhead' with boxerrorbars fs solid lc rgb 'red' lw 3;


!rm 'strongET.eps'
set term pos eps color enhanced "Helvetica" 16
set out 'strongET.eps'
set key top right
set xlabel '# AthenaMP/# nodes'  
set ylabel 'Average time (seconds)'
#set title "Execution time vs Total Pilot duration"  
set yrange[0:*]
set xrange[0:5]
set xtics ("2048/256" 1,"2048/512" 2,"2048/1024" 3,"2048/2048" 4)		
set grid ytics
set style fill solid 1.0 border rgb 'black'
plot 'strong.csv' u ($1-0.2):17:19:20:(0.35) title 'AthenaMP sequential Execution time per node' with boxerrorbars fs solid lc rgb 'red' lw 3,\
'strong.csv' u ($1+0.2):2:4:5:(0.35)  title 'Pilot Duration' with boxerrorbars fs solid lc rgb 'blue' lw 3;



!rm 'strongOver.eps'
set term pos eps color enhanced "Helvetica" 16
set out 'strongOver.eps' 
set key top left
set xlabel '# AthenaMP/# nodes' 
set ylabel 'Average time (seconds)'
#set title "Avera"  
set yrange[0:*]
set xrange[0:5]
set xtics ("2048/256" 1,"2028/512" 2,"2048/1024" 3,"2048/2048" 4)	
set grid ytics
set style fill solid 1.0 border rgb 'black'
plot 'strong.csv' u ($1):12:14:15:(0.4) title 'Overhead' with boxerrorbars fs solid lc rgb 'red' lw 3;

!rm 'MDET.eps'
set term pos eps color enhanced "Helvetica" 16
set out 'MDET.eps'
set key top right
set xlabel '# AthenaMP/# nodes'  
set ylabel 'Average time (seconds)'
#set title "Execution time vs Total Pilot duration"  
set yrange[0:1500]
set xrange[0:5]
set xtics ("68/8" 1,"136/16" 2,"272/32" 3,"544/64" 4)		
set grid ytics
set style fill solid 1.0 border rgb 'black'
plot 'MD.csv' u ($1-0.2):17:19:20:(0.35) title 'Pilot Duration' with boxerrorbars fs solid lc rgb 'red' lw 3,\
'MD.csv' u ($1+0.2):2:4:5:(0.35)  title 'CU Execution time' with boxerrorbars fs solid lc rgb 'blue' lw 3;



!rm 'MDOver.eps'
set term pos eps color enhanced "Helvetica" 16
set out 'MDOver.eps' 
set key top left
set xlabel '# AthenaMP/# nodes' 
set ylabel 'Average time (seconds)'
#set title "Avera"  
set yrange[0:*]
set xrange[0:5]
set xtics ("68/8" 1,"136/16" 2,"272/32" 3,"544/64" 4)	
set grid ytics
set style fill solid 1.0 border rgb 'black'
plot 'MD.csv' u ($1):12:14:15:(0.4) title 'Overhead' with boxerrorbars fs solid lc rgb 'red' lw 3;

