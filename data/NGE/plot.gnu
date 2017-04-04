!rm 'weak1.eps'
set term pos eps color enhanced "Helvetica" 16
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
plot 'data.csv' u ($1):2:4:5:(0.2) axes x1y1  title 'AthenaMP Execution time' with boxerrorbars fs solid lc rgb 'blue' lw 3,\
'data.csv' u ($1-0.2):17:19:20:(0.2) axes x1y1 title 'Pilot Duration' with boxerrorbars fs solid lc rgb 'red' lw 3,\
'data.csv' u ($1+0.2):(f($12)):(f($14)):(f($15)):(0.2) axes x1y1 title 'Overhead' with boxerrorbars fs solid lc rgb 'green' lw 3;


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
plot 'weak2.csv' u ($1):2:4:5:(0.2) axes x1y1   title 'AthenaMP (5 executions)' with boxerrorbars fs solid lc rgb 'blue' lw 3,\
'weak2.csv' u ($1-0.2):17:19:20:(0.2) axes x1y1  title 'Pilot Duration' with boxerrorbars fs solid lc rgb 'red' lw 3,\
'weak2.csv' u ($1+0.2):($12):($14):($15):(0.2) axes x1y1 title 'Overhead' with boxerrorbars fs solid lc rgb 'green' lw 3;




reset

!rm 'strong.eps'
set term pos eps color enhanced "Helvetica" 16
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
plot 'strong.csv' u ($1):2:4:5:(0.2) axes x1y1 title 'Pilot Duration' with boxerrorbars fs solid lc rgb 'blue' lw 3,\
'strong.csv' u ($1-0.2):17:19:20:(0.2) axes x1y1 title 'AthenaMP duration per node' with boxerrorbars fs solid lc rgb 'red' lw 3,\
'strong.csv' u ($1+0.2):($12):($14):($15):(0.2) axes x1y1 title 'Overhead' with boxerrorbars fs solid lc rgb 'green' lw 3;



