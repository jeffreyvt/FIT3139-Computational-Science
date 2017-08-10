
%initialises the variables so that the it's easier to input
c = cos(pi/4);
d = -cos(pi/4);
e = 1;
f = -1;
% input the variables for computation.    
A = [0 e 0 0 0 f 0 0 0 0 0 0 0;  %2 x-axis
     0 0 e 0 0 0 0 0 0 0 0 0 0;  %2 y-axis
     c 0 0 f d 0 0 0 0 0 0 0 0;  %3 x-axis
     c 0 e 0 c 0 0 0 0 0 0 0 0;  %3 y-axis
     0 0 0 e 0 0 0 e 0 0 0 0 0;  %4 x-axis
     0 0 0 0 0 0 e 0 0 0 0 0 0;  %4 y-axis
     0 0 0 0 c e 0 0 c e 0 0 0;  %5 x-axis
     0 0 0 0 c 0 e 0 d 0 0 0 0;  %5 y-axis
     0 0 0 0 0 0 0 0 0 e 0 0 e;  %6 x-axis
     0 0 0 0 0 0 0 0 0 0 e 0 0;  %6 y-axis
     0 0 0 0 0 0 0 e c 0 0 c 0;  %7 x-axis
     0 0 0 0 0 0 0 0 c 0 f d 0;  %7 y-axis
     0 0 0 0 0 0 0 0 0 0 0 c e]; %8 x-axis
b = [0;-10;0;0;0;0;-15;0;0;-20;0;0;0];

solution = A\b;
%displays the solution, first column: force index, second column: force value
[[1:13]' solution]