function x = q3_LU_solver(A, b)
    %check size
    row_size = size(A, 1);
    col_size = size(A, 2);
    if row_size ~= col_size
        disp('The dimension of the input matrix must be n by n')
    end
    [L, U, P] = q3_gaussian(A);
    b = P*b;
    % forward substitution
    for i = 1:row_size
        for j = 1:i
            if j == i
                b(i) = b(i)/L(i, i);
            else
                b(i) = b(i) - L(i, j)*b(j);
            end           
        end        
    end
    % back substitution
    for i = row_size:-1:1
        for j = row_size:-1:i
            if j == i
                b(i) = b(i) / U(i, i);
            else
                b(i) = b(i) - U(i, j)*b(j);
            end
        end
    end
    x = b;

end