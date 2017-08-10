% generate a 4 by 4 test matrix
A = magic(4);
% swap the rows of the matrix
A2 = q2_permMatrix(A, 1, 2);

%check whether the rows are swapped and if they equal
sum(A(1,:) - A2(2,:))
sum(A(2,:) - A2(1,:))
% if the rows are equal, the resulting difference should equate to 0.