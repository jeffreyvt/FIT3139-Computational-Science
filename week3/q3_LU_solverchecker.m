%this script checks whether the LU solver is functioning properly

%generates a non-singular large square matrix
A = rand(100, 95);
A = A'*A;
%generate a random solution b
b = rand(95,1);

%using matlab inbuilt function to solve the system
solution = A^-1*b;

%using the LU_solver to solve the system
LU_solution = q3_LU_solver(A, b);

%compare the solutions. If the error is expected to be small (close to 0).
sum(solution - LU_solution)