function m = q2_permMatrix(matrix, row1, row2)
    % matrix: n by m matrix the input matrix for row swap operation
    % row1, row2: integers representing the index of the rows, swap row1
    % with row2.
    row_size = size(matrix, 1);
    % check whether the inputs are valid.
    if row1 > row_size || row2 > row_size
        disp('invalid inputs, check dimensions')
    else
        perm_matrix = eye(row_size);
        tmp = perm_matrix(row1,:);
        perm_matrix(row1,:) = perm_matrix(row2,:);
        perm_matrix(row2,:) = tmp;
        m = perm_matrix*matrix;
    end

end