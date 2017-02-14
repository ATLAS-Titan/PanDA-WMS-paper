!rm 'mean.eps'
set out 'mean.eps'
set term pos eps color "Helvetica" 24

set auto
set key top left
set grid
set yrange [0:*]
set xlabel 'Time(hours)'
set ylabel '# completed events'
f(x,y) = (x < 50)? 0 : x < 100 ? y-1000 : y 
g(x,y) = (x < 100)? 0 : x < 300 ? y-800 : y
h(x,y) = (x < 200)? 0 : x < 250 ? y-2000 : y
scaleX= 100
scaleY =1000
plot 'mean.dat' u ($1*scaleX):(f($1*scaleX,$2*scaleY)) title 'exp.1' with l lt 1 lw 5,\
'' u ($1*scaleX):(g($1*scaleX,$3*scaleY)) title 'exp.2' with l lt 2 lw 5,\
'' u ($1*scaleX):(h($1*scaleX,$4*scaleY)) title 'exp.3' with l lt 3 lw 5;
