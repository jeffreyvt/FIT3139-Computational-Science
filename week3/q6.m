
%input data
Data = [0.0, 2.9;0.5, 2.7;1.0, 4.8;1.5, 5.3;2.0, 7.1;2.5, 7.6;3.0, 7.7;3.5, 7.6;4.0, 9.4;4.5, 9.0;5.0, 9.6;5.5, 10.0;6.0, 10.2];

% extract data
A = [Data(:,1) ones(size(Data,1),1)];
% extract solution
b = Data(:,2);

% apply least square estimate.
x = A'*A\A'*b;

% plot the data, the result fits the data very well.
hold off
plot(Data(:,1), Data(:,2),'*'); 
hold on
plot(Data(:,1), A*x);