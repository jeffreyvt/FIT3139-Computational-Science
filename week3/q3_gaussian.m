function [L, matrix, P] = q3_gaussian(matrix)
    % This function returns the LU decomposition of the matrix with
    % permutation matrix P
    % return value L will be the lower triangular
    % return value of matrix will be upper triangular
    % return value of P will be permutation matrix similar to the identity matrix
    
    row_size = size(matrix, 1);
    col_size = size(matrix, 2);
    % check the dimension of the 
    if row_size ~= col_size
        disp('The dimension of the input matrix must be n by n')
    else
        L = eye(row_size);
        P = eye(row_size);
        for i = 1:row_size-1
            L_tmp = eye(row_size);
            % finds the maximum value for partial pivoting
            [max_val, max_i] = max(abs(matrix(i:row_size,i)));
            % pivot if the current pivot isnt the max in magnitude.
            if max_i+i-1 ~= i
                P = q2_permMatrix(P, i+max_i-1, i);
                matrix = q2_permMatrix(matrix, i+max_i-1, i);
            end
            % calculating the L matrix
            for j = i+1:row_size
                L_tmp(j, i) = matrix(j, i)/matrix(i,i);
                matrix(j,:) = matrix(j,:) - matrix(i,:)*L_tmp(j, i);
            end
            % pivoting the L matrix
            if max_i+i-1 ~= i
                L_tmp = q2_permMatrix(L_tmp, i+max_i-1, i);
            end
            % combining the L matrix together
            L = L*L_tmp;
        end
        % pivot back to original for return value
        L = P*L;
    end
end