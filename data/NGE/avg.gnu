
reset

!rm 'strongFluc.gif'
set terminal gif font "Helvetica" 8
set out 'strongFluc.gif' 
set key bottom right	
set xlabel 'Date of the execution'  
set ylabel 'Execution time (seconds)'
set timefmt "%s"
set xdata time
set format x "%m/%d"
set grid ytics
#set xtics rotate 90
plot 'strong-units.csv' u 2:3 index 0 title '256 nodes' with p lc rgb 'blue' lw 2,\
'strong-units.csv' u 2:3 index 1 title '512 nodes' with p lc rgb 'red' lw 2,\
'strong-units.csv' u 2:3 index 2 title '1024 nodes' with p lc rgb 'green' lw 2,\
'strong-units.csv' u 2:3 index 3 title '2048 nodes' with p lc rgb 'purple' lw 2;

!rm 'weak1Fluc.gif'
set terminal gif font "Helvetica" 8
set out 'weak1Fluc.gif' 
set key top right	
set xlabel 'Date of the execution'  
set ylabel 'Execution time (seconds)'
set timefmt "%s"
set xdata time
set format x "%m/%d"
set grid ytics
#set xtics rotate 90
plot 'data-units.csv' u 2:3 index 2 title '256 nodes' with p lc rgb 'blue' lw 2,\
'data-units.csv' u 2:3 index 3 title '512 nodes' with p lc rgb 'red' lw 2,\
'data-units.csv' u 2:3 index 0 title '1024 nodes' with p lc rgb 'green' lw 2,\
'data-units.csv' u 2:3 index 1 title '2048 nodes' with p lc rgb 'purple' lw 2;


!rm 'weak2Fluc.gif'
set terminal gif font "Helvetica" 8
set out 'weak2Fluc.gif' 
set key bottom right	
set xlabel 'Date of the execution'  
set ylabel 'Execution time (seconds)'
set timefmt "%s"
set xdata time
set format x "%m/%d"
set yrange[0:2200]
set grid ytics
#set xtics rotate 90
plot 'weak2-units.csv' u 2:3 index 0 title '256 nodes' with p lc rgb 'blue' lw 2,\
'weak2-units.csv' u 2:3 index 1 title '512 nodes' with p lc rgb 'red' lw 2,\
'weak2-units.csv' u 2:3 index 2 title '1024 nodes' with p lc rgb 'green' lw 2,\
'weak2-units.csv' u 2:3 index 3 title '2048 nodes' with p lc rgb 'purple' lw 2;

!rm 'weak1.gif'
set terminal gif font "Helvetica" 8
set out 'weak1.gif' 
set key top left
set xlabel '# AthenaMP/# nodes'  
set ylabel 'Average time (seconds)'
#set title "Execution time vs Total Pilot duration"  
set yrange[0:6000]
set xrange[0:5]
f(x) = x <= 1000 ? x*2.2 : x
set xtics ("250/250" 1,"500/500" 2,"1000/1000" 3,"2000/2000" 4)		
set ytics ("50" f(50),"100" f(100),"200" f(200),"400" f(400),2000,4000,5000,6000)
set grid ytics
#set y2label 'Average time (seconds x 10)'
#set y2range[0:4200]
#set y2tics 
set style fill solid 1.0 border rgb 'black'
plot 'data.csv' u ($1):2:4:5:(0.2) axes x1y1  title 'AthenaMP Execution time' with boxerrorbars fs solid lc rgb 'blue' lw 3,\
'data.csv' u ($1-0.2):17:19:20:(0.2) axes x1y1 title 'Pilot Duration' with boxerrorbars fs solid lc rgb 'red' lw 3,\
'data.csv' u ($1+0.2):(f($12)):(f($14)):(f($15)):(0.2) axes x1y1 title 'Overhead' with boxerrorbars fs solid lc rgb 'green' lw 3;




!rm 'weak1.eps'
set term pos eps color enhanced "Helvetica" 15
set out 'weak1.eps' 
set key top left
set xlabel '# AthenaMP/# nodes'  
set ylabel 'Average time (seconds)'
#set title "Execution time vs Total Pilot duration"  
set yrange[0:6000]
set xrange[0:5]
f(x) = x <= 400 ? x*2.2: x
set xtics ("250/250" 1,"500/500" 2,"1000/1000" 3,"2000/2000" 4)		
set ytics ("50" f(50),"100" f(100),"200" f(200),"400" f(400),2000,4000,6000)
set grid ytics
#set y2label 'Average time (seconds x 10)'
#set y2range[0:4200]
#set y2tics 
set style fill solid 1.0 border rgb 'black'
plot 'data.csv' u ($1-0.2):17:19:20:(0.2) axes x1y1 title 'Pilot Duration' with boxerrorbars fs solid lc rgb 'red' lw 3,\
'data.csv' u ($1):2:4:5:(0.2) axes x1y1  title 'AthenaMP Execution time' with boxerrorbars fs solid lc rgb 'blue' lw 3,\
'data.csv' u ($1+0.2):(f($12)):(f($14)):(f($15)):(0.2) axes x1y1 title 'Overhead' with boxerrorbars fs solid lc rgb 'green' lw 3;


!rm 'weakET1.eps'
set terminal gif font "Helvetica" 16
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

!rm 'weak2.gif'
set term gif font "Helvetica" 12
set out 'weak2.gif' 
set key left
set xlabel '# AthenaMP/# nodes'  
set ylabel 'Average time (seconds)'
#set title "Execution time vs Total Pilot duration"  
set yrange[0:8000]
set xrange[0:5]
set xtics ("1280/256" 1,"2560/512" 2,"5120/1024" 3,"10240/2048" 4)		
set ytics (250, 500,1000,2000,4000,6000,8000)
set grid ytics
#set y2label 'Average time (seconds x 10)'
#set y2range[0:*]
#set y2tics 
set style fill solid 1.0 border rgb 'black'
plot 'weak2.csv' u ($1):2:4:5:(0.2) axes x1y1   title 'AthenaMP (5 executions)' with boxerrorbars fs solid lc rgb 'blue' lw 3,\
'weak2.csv' u ($1-0.2):17:19:20:(0.2) axes x1y1  title 'Pilot Duration' with boxerrorbars fs solid lc rgb 'red' lw 3,\
'weak2.csv' u ($1+0.2):($12):($14):($15):(0.2) axes x1y1 title 'Overhead' with boxerrorbars fs solid lc rgb 'green' lw 3;


reset

!rm 'weak2.eps'
set term pos eps color enhanced "Helvetica" 16
set out 'weak2.eps' 
set key left
set xlabel '# AthenaMP/# nodes'  
set ylabel 'Average time (seconds)'
#set title "Execution time vs Total Pilot duration"  
set yrange[0:8000]
set xrange[0:5]
set xtics ("1280/256" 1,"2560/512" 2,"5120/1024" 3,"10240/2048" 4)		
set ytics (250, 500,1000,2000,4000,6000,8000)
set grid ytics
#set y2label 'Average time (seconds x 10)'
#set y2range[0:*]
#set y2tics 
set style fill solid 1.0 border rgb 'black'
plot 'weak2.csv' u ($1-0.2):17:19:20:(0.2) axes x1y1  title 'Pilot Duration' with boxerrorbars fs solid lc rgb 'red' lw 3,\
'weak2.csv' u ($1):2:4:5:(0.2) axes x1y1   title 'AthenaMP (5 executions)' with boxerrorbars fs solid lc rgb 'blue' lw 3,\
'weak2.csv' u ($1+0.2):($12):($14):($15):(0.2) axes x1y1 title 'Overhead' with boxerrorbars fs solid lc rgb 'green' lw 3;




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

reset
!rm 'strong.gif'
set term gif font "Helvetica" 10
set out 'strong.gif'
set key top right
set xlabel '# AthenaMP/# nodes'  
set ylabel 'Average time (seconds)'
#set title "Execution time vs Total Pilot duration"  
set yrange[0:11000]
set xrange[0:5]
set xtics ("2048/256" 1,"2048/512" 2,"2048/1024" 3,"2048/2048" 4)	
set ytics (400,1000,2000,4000,6000,8000,10000)	
set grid ytics
#set y2label 'Average time (seconds x 10)'
#set y2range[0:4200]
#set y2tics 
set style fill solid 1.0 border rgb 'black'
plot 'strong.csv' u ($1-0.2):2:4:5:(0.2) axes x1y1 title 'Pilot Duration' with boxerrorbars fs solid lc rgb 'blue' lw 3,\
'strong.csv' u ($1):17:19:20:(0.2) axes x1y1 title 'AthenaMP duration per node' with boxerrorbars fs solid lc rgb 'red' lw 3,\
'strong.csv' u ($1+0.2):($12):($14):($15):(0.2) axes x1y1 title 'Overhead' with boxerrorbars fs solid lc rgb 'green' lw 3;


reset

!rm 'strong.eps'
set term pos eps color enhanced "Helvetica" 12
set out 'strong.eps'
set key top right
set xlabel '# AthenaMP/# nodes'  
set ylabel 'Average time (seconds)'
#set title "Execution time vs Total Pilot duration"  
set yrange[0:11000]
set xrange[0:5]
set xtics ("2048/256" 1,"2048/512" 2,"2048/1024" 3,"2048/2048" 4)		
set ytics (400,1000,2000,4000,6000,8000,10000)
set grid ytics
set style fill solid 1.0 border rgb 'black'
plot 'strong.csv' u ($1-0.2):17:19:20:(0.2) axes x1y1 title 'AthenaMP duration per node' with boxerrorbars fs solid lc rgb 'red' lw 3,\
'strong.csv' u ($1):2:4:5:(0.2) axes x1y1 title 'Pilot Duration' with boxerrorbars fs solid lc rgb 'blue' lw 3,\
'strong.csv' u ($1+0.2):($12):($14):($15):(0.2) axes x1y1 title 'Overhead' with boxerrorbars fs solid lc rgb 'green' lw 3;


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
set yrange[0:420]
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

