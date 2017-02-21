function comparison()
close all
cd ./data
load('results_bvp4c_pop1.mat')
data1 = out.setCONT(end).CONT(end).sol;

load('results_gpops_pop1.mat')
down_gpops = down;
cross_gpops = crossrange;
alt_gpops = alt;
v_gpops = v;
psi_gpops = psii;
gam_gpops = gam;
time_gpops = time;

lamX_gpops = lamx;
lamY_gpops = lamy;
lamZ_gpops = lamz;
lamV_gpops = lamv;
lamPSII_gpops = lampsii;
lamGAM_gpops = lamgam;

bank_gpops = bank;
aoa_gpops = aoa;
T_gpops = T;
Noise_gpops = Noise;
cd ..

% Constants
mass = 7180/9.81;
g = 9.81;

% Traditional Approach
down_bvp4c = data1.y(1,:)/1000;
cross_bvp4c = data1.y(2,:)/1000;
alt_bvp4c = data1.y(3,:)/1000;
v_bvp4c = data1.y(4,:);
psi_bvp4c = data1.y(5,:)*180/pi;
gam_bvp4c = data1.y(6,:)*180/pi;
tau_bvp4c = data1.x;
time_bvp4c = data1.parameters(1)*tau_bvp4c;
lamX_bvp4c = data1.y(7,:);
lamY_bvp4c = data1.y(8,:);
lamZ_bvp4c = data1.y(9,:);
lamV_bvp4c = data1.y(10,:);
lamPSII_bvp4c = data1.y(11,:);
lamGAM_bvp4c = data1.y(12,:);
bank_bvp4c = 60*sin(data1.control(1,:));
aoa_bvp4c = 15*sin(data1.control(2,:));
T_bvp4c = 1560*sin(data1.control(3,:))+1860;
Noise_bvp4c = 10*log10(((18.73*T_bvp4c.^(5.2).*cos(gam_bvp4c.*pi./180))./(v_bvp4c.*(alt_bvp4c.*1000+50).^(2.5))));
% ham = lamZ.*v.*sin(gam) - lamGAM.*((g.*cos(gam))./v - (cos(bank).*(L + T.*(1 - (D + g.*mass.*sin(gam)).^2/T.^2).^(1/2)))./(mass.*v)) + lamX.*v.*cos(gam).*cos(psii) + lamY.*v.*cos(gam).*sin(psii) + (lamPSII.*sin(bank).*(L + T.*(1 - (D + g.*mass.*sin(gam)).^2./T.^2).^(1/2)))./(mass.*v.*cos(gam)) + 1;


%%%%%%%%%%
%% Plot %%
%%%%%%%%%%
% Noise and 3DOF trajectory plot
figure(1)
subplot(1,3,1:2)
h1 = plot3(down_bvp4c,cross_bvp4c,alt_bvp4c,'b-*','markersize', 3, 'linewidth', 2)
title('3D Trajectory', 'fontSize', 14 , 'fontWeight' , 'bold')
xlabel('Downrange [km]', 'fontSize', 12 , 'fontWeight' , 'bold')
ylabel('Crossrange [km]', 'fontSize', 12 , 'fontWeight' , 'bold')
zlabel('Altitude [km]', 'fontSize', 12 , 'fontWeight' , 'bold')
grid on
hold on
h2 = plot3(down_gpops,cross_gpops,alt_gpops,'r-o','markersize', 3, 'linewidth', 1)
set(gca,'FontSize',12,'FontWeight' , 'bold');
legend([h1 h2],{'BVP4C','GPOPS'},'fontSize', 12)

subplot(1,3,3)
h1 = plot(time_bvp4c,Noise_bvp4c, 'b-*','markersize', 3, 'linewidth', 2)
title('Time History Plot for Noise', 'fontSize', 14 , 'fontWeight' , 'bold')
ylabel('Noise [dB]', 'fontSize', 12 , 'fontWeight' , 'bold')
xlabel('Time [s]', 'fontSize', 12 , 'fontWeight' , 'bold')
grid on
hold on
h2 = plot(time_gpops,Noise_gpops, 'r-o','markersize', 3, 'linewidth', 1)
set(gca,'FontSize',12,'FontWeight' , 'bold');
legend([h1 h2],{'BVP4C','GPOPS'},'fontSize', 12)

% States Time History Plot
figure(2)
subplot(2,3,1)
h1 = plot(time_bvp4c,down_bvp4c, 'b-*','markersize', 3, 'linewidth', 2)
title('Time History Plot for Downrange', 'fontSize', 14 , 'fontWeight' , 'bold')
ylabel('Downrange [km]', 'fontSize', 12 , 'fontWeight' , 'bold')
xlabel('Time [s]', 'fontSize', 12 , 'fontWeight' , 'bold')
grid on
hold on
h2 = plot(time_gpops,down_gpops, 'r-o','markersize', 3, 'linewidth', 1)
set(gca,'FontSize',12,'FontWeight' , 'bold');
legend([h1 h2],{'BVP4C','GPOPS'},'fontSize', 12)

subplot(2,3,2)
h1 = plot(time_bvp4c,cross_bvp4c, 'b-*','markersize', 3, 'linewidth', 2)
title('Time History Plot for Crossrange', 'fontSize', 14 , 'fontWeight' , 'bold')
ylabel('Crossrange [km]', 'fontSize', 12 , 'fontWeight' , 'bold')
xlabel('Time [s]', 'fontSize', 12 , 'fontWeight' , 'bold')
grid on
hold on
h2 = plot(time_gpops,cross_gpops, 'r-o','markersize', 3, 'linewidth', 1)
set(gca,'FontSize',12,'FontWeight' , 'bold');
legend([h1 h2],{'BVP4C','GPOPS'},'fontSize', 12)

subplot(2,3,3)
h1 = plot(time_bvp4c,alt_bvp4c, 'b-*','markersize', 3, 'linewidth', 2)
title('Time History Plot for Altitude', 'fontSize', 14 , 'fontWeight' , 'bold')
ylabel('Altitude [km]', 'fontSize', 12 , 'fontWeight' , 'bold')
xlabel('Time [s]', 'fontSize', 12 , 'fontWeight' , 'bold')
grid on
hold on
h2 = plot(time_gpops,alt_gpops, 'r-o','markersize', 3, 'linewidth', 1)
set(gca,'FontSize',12,'FontWeight' , 'bold');
legend([h1 h2],{'BVP4C','GPOPS'},'fontSize', 12)

subplot(2,3,4)
h1 = plot(time_bvp4c,v_bvp4c, 'b-*','markersize', 3, 'linewidth', 2)
title('Time History Plot for Velocity', 'fontSize', 14 , 'fontWeight' , 'bold')
ylabel('Velocity [m/s]', 'fontSize', 12 , 'fontWeight' , 'bold')
xlabel('Time [s]', 'fontSize', 12 , 'fontWeight' , 'bold')
grid on
hold on
h2 = plot(time_gpops,v_gpops, 'r-o','markersize', 3, 'linewidth', 1)
set(gca,'FontSize',12,'FontWeight' , 'bold');
legend([h1 h2],{'BVP4C','GPOPS'},'fontSize', 12)

subplot(2,3,5)
h1 = plot(time_bvp4c,psi_bvp4c, 'b-*','markersize', 3, 'linewidth', 2)
title('Time History Plot for \psi', 'fontSize', 14 , 'fontWeight' , 'bold')
ylabel('\psi [deg]', 'fontSize', 12 , 'fontWeight' , 'bold')
xlabel('Time [s]', 'fontSize', 12 , 'fontWeight' , 'bold')
grid on
hold on
h2 = plot(time_gpops,psi_gpops, 'r-o','markersize', 3, 'linewidth', 1)
set(gca,'FontSize',12,'FontWeight' , 'bold');
legend([h1 h2],{'BVP4C','GPOPS'},'fontSize', 12)

subplot(2,3,6)
h1 = plot(time_bvp4c,gam_bvp4c, 'b-*','markersize', 3, 'linewidth', 2)
title('Time History Plot for \gamma', 'fontSize', 14 , 'fontWeight' , 'bold')
ylabel('\gamma [deg]', 'fontSize', 12 , 'fontWeight' , 'bold')
xlabel('Time [s]', 'fontSize', 12 , 'fontWeight' , 'bold')
grid on
hold on
h2 = plot(time_gpops,gam_gpops, 'r-o','markersize', 3, 'linewidth', 1)
set(gca,'FontSize',12,'FontWeight' , 'bold');
legend([h1 h2],{'BVP4C','GPOPS'},'fontSize', 12)

% Hamiltonian and Control History Plot
figure(3)
subplot(1,3,1)
h1 = plot(time_bvp4c,bank_bvp4c, 'b-*','markersize', 3, 'linewidth', 2)
title('Bank Angle History', 'fontSize', 14 , 'fontWeight' , 'bold')
ylabel('Bank Angle [deg]', 'fontSize', 12 , 'fontWeight' , 'bold')
xlabel('Time [s]', 'fontSize', 12 , 'fontWeight' , 'bold')
grid on
hold on
h2 = plot(time_gpops,bank_gpops, 'r-o','markersize', 3, 'linewidth', 1)
set(gca,'FontSize',12,'FontWeight' , 'bold');
legend([h1 h2],{'BVP4C','GPOPS'},'fontSize', 12)

subplot(1,3,2)
h1 = plot(time_bvp4c,aoa_bvp4c, 'b-*','markersize', 3, 'linewidth', 2)
title('Angle of Attack History', 'fontSize', 14 , 'fontWeight' , 'bold')
ylabel('Angle of Attack [deg]', 'fontSize', 12 , 'fontWeight' , 'bold')
xlabel('Time [s]', 'fontSize', 12 , 'fontWeight' , 'bold')
grid on
hold on
h2 = plot(time_gpops,aoa_gpops, 'r-o','markersize', 3, 'linewidth', 1)
set(gca,'FontSize',12,'FontWeight' , 'bold');
legend([h1 h2],{'BVP4C','GPOPS'},'fontSize', 12)

subplot(1,3,3)
h1 = plot(time_bvp4c,T_bvp4c, 'b-*','markersize', 3, 'linewidth', 2)
title('Thrust History', 'fontSize', 14 , 'fontWeight' , 'bold')
ylabel('Thrust [N]', 'fontSize', 12 , 'fontWeight' , 'bold')
xlabel('Time [s]', 'fontSize', 12 , 'fontWeight' , 'bold')
grid on
hold on
h2 = plot(time_gpops,T_gpops, 'r-o','markersize', 3, 'linewidth', 1)
set(gca,'FontSize',12,'FontWeight' , 'bold');
legend([h1 h2],{'BVP4C','GPOPS'},'fontSize', 12)

% Costates
figure(4)
subplot(2,3,1)
h1 = plot(time_bvp4c,lamX_bvp4c/1e6, 'b','markersize', 3, 'linewidth', 2)
title('Time History Plot for \lambda_{x}', 'fontSize', 14 , 'fontWeight' , 'bold')
ylabel('\lambda_{x} [dB/m] X 10^{6}', 'fontSize', 12 , 'fontWeight' , 'bold')
xlabel('Time [s]', 'fontSize', 12 , 'fontWeight' , 'bold')
grid on
hold on
h2 = plot(time_gpops,lamX_gpops/1e6, 'r','markersize', 3, 'linewidth', 2)
set(gca,'FontSize',12,'FontWeight' , 'bold');
legend([h1 h2],{'BVP4C','GPOPS'},'fontSize', 12)

subplot(2,3,2)
h1 = plot(time_bvp4c,lamY_bvp4c/1e6, 'b','markersize', 3, 'linewidth', 2)
title('Time History Plot for \lambda_{y}', 'fontSize', 14 , 'fontWeight' , 'bold')
ylabel('\lambda_{y} [dB/m] X 10^{6}', 'fontSize', 12 , 'fontWeight' , 'bold')
xlabel('Time [s]', 'fontSize', 12 , 'fontWeight' , 'bold')
grid on
hold on
h2 = plot(time_gpops,lamY_gpops/1e6, 'r','markersize', 3, 'linewidth', 2)
set(gca,'FontSize',12,'FontWeight' , 'bold');
legend([h1 h2],{'BVP4C','GPOPS'},'fontSize', 12)

subplot(2,3,3)
h1 = plot(time_bvp4c,lamZ_bvp4c/1e10, 'b','markersize', 3, 'linewidth', 2)
title('Time History Plot for \lambda_{z}', 'fontSize', 14 , 'fontWeight' , 'bold')
ylabel('\lambda_{z} [dB/m] X 10^{10}', 'fontSize', 12 , 'fontWeight' , 'bold')
xlabel('Time [s]', 'fontSize', 12 , 'fontWeight' , 'bold')
grid on
hold on
h2 = plot(time_gpops,lamZ_gpops/1e10, 'r','markersize', 3, 'linewidth', 2)
set(gca,'FontSize',12,'FontWeight' , 'bold');
legend([h1 h2],{'BVP4C','GPOPS'},'fontSize', 12)

subplot(2,3,4)
h1 = plot(time_bvp4c,lamV_bvp4c/1e10, 'b','markersize', 3, 'linewidth', 2)
title('Time History Plot for \lambda_{z}', 'fontSize', 14 , 'fontWeight' , 'bold')
ylabel('\lambda_{v} [dB.s/m] X 10^{10}', 'fontSize', 12 , 'fontWeight' , 'bold')
xlabel('Time [s]', 'fontSize', 12 , 'fontWeight' , 'bold')
grid on
hold on
h2 = plot(time_gpops,lamV_gpops/1e10, 'r','markersize', 3, 'linewidth', 2)
set(gca,'FontSize',12,'FontWeight' , 'bold');
legend([h1 h2],{'BVP4C','GPOPS'},'fontSize', 12)

subplot(2,3,5)
h1 = plot(time_bvp4c,lamPSII_bvp4c/1e10, 'b','markersize', 3, 'linewidth', 2)
title('Time History Plot for \lambda_{\psi}', 'fontSize', 14 , 'fontWeight' , 'bold')
ylabel('\lambda_{\psi}[dB/rad] X 10^{10}', 'fontSize', 12 , 'fontWeight' , 'bold')
xlabel('Time [s]', 'fontSize', 12 , 'fontWeight' , 'bold')
grid on
hold on
h2 = plot(time_gpops,lamPSII_gpops/1e10, 'r','markersize', 3, 'linewidth', 2)
set(gca,'FontSize',12,'FontWeight' , 'bold');
legend([h1 h2],{'BVP4C','GPOPS'},'fontSize', 12)

subplot(2,3,6)
h1 = plot(time_bvp4c,lamGAM_bvp4c/1e13, 'b','markersize', 3, 'linewidth', 2)
title('Time History Plot for \lambda_{\gamma}', 'fontSize', 14 , 'fontWeight' , 'bold')
ylabel('\lambda_{\gamma} [dB/rad] X 10^{13}', 'fontSize', 12 , 'fontWeight' , 'bold')
xlabel('Time [s]', 'fontSize', 12 , 'fontWeight' , 'bold')
grid on
hold on
h2 = plot(time_gpops,lamGAM_gpops/1e13, 'r','markersize', 3, 'linewidth', 2)
set(gca,'FontSize',12,'FontWeight' , 'bold');
legend([h1 h2],{'BVP4C','GPOPS'},'fontSize', 12)
return