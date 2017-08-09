function [L, matrix, P] = q3_gaussian(matrix)
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
            [max_val, max_i] = max(abs(matrix(i:row_size,i)));
            if max_i+i-1 ~= i
                P = q2_permMatrix(P, i+max_i-1, i);
                matrix = q2_permMatrix(matrix, i+max_i-1, i);
            end
            for j = i+1:row_size
                L_tmp(j, i) = matrix(j, i)/matrix(i,i);
                matrix(j,:) = matrix(j,:) - matrix(i,:)*L_tmp(j, i);
            end
            if max_i+i-1 ~= i
                L_tmp = q2_permMatrix(L_tmp, i+max_i-1, i);
            end
            L = L*L_tmp;
        end
        L = P*L;
    end
end