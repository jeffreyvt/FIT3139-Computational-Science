A = [0.1 0.2 0.3;0.4 0.5 0.6;0.7 0.8 0.9];
b = [0.1;0.3;0.5];
A\b

% warning is shown, the matrix A is close to singular, hence the solution
% may be inaccuarte.