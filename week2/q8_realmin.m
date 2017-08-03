% Student ID: 2594 4800
% Name: JiaHui (Jeffrey) Lu
% Aug-2017

num = 1;
%keep halving the num until num > 0 condition fails
while num > 0
    num_previous = num;
    num = num / 2;
end

% print out the num just before the while loop is exited 
% (the smallest number where the condition num > 0 is satisfied).
disp(num_previous)
realmin

%realmin returns the smallest positive normalized floating-point number in IEEE® double precision.
%A normalized floating point number has no leading zeros in the significand
%however, the smallest positive real number we obtained here is
%unnormalised, hence it is possible to obtain a double precision digit that
%is still a double with size of 8 Bytes.
