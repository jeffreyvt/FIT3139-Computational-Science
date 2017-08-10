
% input the data
Data = [0.0, 2.9;0.5, 2.7;1.0, 4.8;1.5, 5.3;2.0, 7.1;2.5, 7.6;3.0, 7.7;3.5, 7.6;4.0, 9.4;4.5, 9.0;5.0, 9.6;5.5, 10.0;6.0, 10.2;6.5, 9.7;7.0, 8.3;7.5, 8.4;8.0, 9.0;8.5, 8.3;9.0, 6.6;9.5, 6.7;10.0, 4.1];
%extract the data into matrix A
A = [Data(:,1).^2 Data(:,1) ones(size(Data,1),1)];
% extract the results
b = Data(:,2);

%apply least square estimate
x = A'*A\A'*b;

% plot the data, the result fits the data very well.
hold off
plot(Data(:,1), Data(:,2),'o'); 
hold on
plot(Data(:,1), A*x);