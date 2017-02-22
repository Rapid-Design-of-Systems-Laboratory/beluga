function threed_plot()

cd ./data
load('results.mat')
data_init = out.setCONT(1).CONT(1,1).sol;
data_end = out.setCONT(end).CONT(end).sol;
cd ..

% Final trajectory
x_init = data_init.y(1,:)/1000;
y_init = data_init.y(2,:)/1000;
z_init = data_init.y(3,:)/1000;

% Final trajectory
x_end = data_end.y(1,:)/1000;
y_end = data_end.y(2,:)/1000;
z_end = data_end.y(3,:)/1000;

figure(1)
plot3(x_init,y_init,z_init,'r','markersize', 3, 'linewidth', 2)
title('3D Plot: Initial Guess Trajectory', 'fontSize', 14 , 'fontWeight' , 'bold')
xlabel('Downrange [km]', 'fontSize', 12 , 'fontWeight' , 'bold')
ylabel('Crossrange [km]', 'fontSize', 12 , 'fontWeight' , 'bold')
zlabel('Altitude [km]', 'fontSize', 12 , 'fontWeight' , 'bold')
grid on
set(gca,'FontSize',12,'FontWeight' , 'bold');

figure(2)
plot3(x_end,y_end,z_end,'r','markersize', 3, 'linewidth', 2)
title('3D Plot: Final Desired Trajectory', 'fontSize', 14 , 'fontWeight' , 'bold')
xlabel('Downrange [km]', 'fontSize', 12 , 'fontWeight' , 'bold')
ylabel('Crossrange [km]', 'fontSize', 12 , 'fontWeight' , 'bold')
zlabel('Altitude [km]', 'fontSize', 12 , 'fontWeight' , 'bold')
grid on
set(gca,'FontSize',12,'FontWeight' , 'bold');

return