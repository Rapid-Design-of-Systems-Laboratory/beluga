X=[0:20:10*1000];
Y=[0:20:10*1000];
Z=transpose(Y)*X*0.0;
for i=1:length(X)
    for j=1:length(Y)
        Z(i,j)=50*(sin(0.5*X(i)/1000))^2;
    end
end
plot(X,Z)
