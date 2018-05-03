close all;
clear;
load('phu_2k5_eps4');

for i=1:20:length(sol_array)
    sol = sol_array(i);
    sol = sol{1};
    
    figure(1);
    hold on;
    plot(sol.y(2,:)*sol.aux.const.re/1000, sol.y(1,:)/1000,'LineWidth',1.5);
    xlabel('Downrange (km)','FontSize',16); 
    ylabel('Altitude (km)','FontSize',16);    
    set(findall(gcf,'-property','FontSize'),'FontSize',16);
    
    figure(2);
    hold on;
    plot(sol.y(3,:)/1000, sol.y(1,:)/1000,'LineWidth',1.5);
    xlabel('Velocity (km/s)','FontSize',16); 
    ylabel('Altitude (km)','FontSize',16);    
    set(findall(gcf,'-property','FontSize'),'FontSize',16);
    
    figure(3);
    hold on;
    plot(sol.x*sol.y(9,1),sol.u(1,:)*180/pi,'LineWidth',1.5);
    xlabel('Time (s)','FontSize',16);    
    ylabel('Angle of attack (deg)','FontSize',16); 
    set(findall(gcf,'-property','FontSize'),'FontSize',16)
end
x = linspace(-5,5,512);
ub = 1;
lb = -1;
s = 4/(ub-lb);
psi = ub - (ub - lb)./(1+exp(s.*x));
figure(4);
plot(x, psi, 'LineWidth', 1.5);
grid on;
ax = gca;
ax.YTick = -1:0.2:1;
ax.XTick = -5:1:5;

xlabel('x');
ylabel('\psi(x)');
set(findall(gcf,'-property','FontSize'),'FontSize',16)
print -dpng -r200 satfcn.png

print(1, '-dpng','-r200', 'figure_1_m.png');
print(2, '-dpng','-r200', 'figure_2_m.png');
print(3, '-dpng','-r200', 'figure_3_m.png');