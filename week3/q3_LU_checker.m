% creates a large non-singular square matrix
a = rand(100, 95);
a = a'*a;

% runs LU decomposition
[L, U, P] = q3_gaussian(a);

% checks the accuracy of LU. the smaller the better (close to 0).
sum(sum(P*a - L*U))/(size(P,1)*size(P,2))
