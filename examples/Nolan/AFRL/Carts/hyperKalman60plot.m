function hyperKalman60plot

X = load('solSet.txt')';

save('data.mat', 'X')

t = X(:,end);

% h     = X(end,1)*1000
% theta = X(end,2)
% v     = X(end,3)*1000
% gam   = X(end,4)
% alpha = X(end,5)*180/pi
% p11   = X(end,6)*1e5
% p12   = X(end,7)*1e-4
% p13   = X(end,8)*100
% p14   = X(end,9)*0.1
% p22   = X(end,10)*1e-9
% p23   = X(end,11)*1e-4
% p24   = X(end,12)*1e-8
% p33   = X(end,13)*10
% p34   = X(end,14)*1e-3
% p44   = X(end,15)*1e-6

h     = X(:,1)*1000;
theta = X(:,2);
v     = X(:,3)*1000;
gam   = X(:,4);
alpha = X(:,5)*180/pi;
p11   = X(:,6)*1e5;
p12   = X(:,7)*1e-4;
p13   = X(:,8)*100;
p14   = X(:,9)*0.1;
p22   = X(:,10)*1e-9;
p23   = X(:,11)*1e-4;
p24   = X(:,12)*1e-8;
p33   = X(:,13)*10;
p34   = X(:,14)*1e-3;
p44   = X(:,15)*1e-6;

lam_h     = X(:,16);
lam_theta = X(:,17);
lam_v     = X(:,18);
lam_gam   = X(:,19);
lam_alpha = X(:,20);
lam_p11   = X(:,21);
lam_p12   = X(:,22);
lam_p13   = X(:,23);
lam_p14   = X(:,24);
lam_p22   = X(:,25);
lam_p23   = X(:,26);
lam_p24   = X(:,27);
lam_p33   = X(:,28);
lam_p34   = X(:,29);
lam_p44   = X(:,30);

u = X(:,end-1);

H = figure(1);
colors = get(gca, 'colororder');
clf

subplot(3,3,1)
plot(theta, h, 'color',colors(1,:))
grid on
title('Trajectory')
xlabel('\theta [deg]')
ylabel('h [m]')
axis([0,0.75,0,80000])

subplot(3,3,4)
plot(t, v, 'color',colors(1,:))
grid on
title('Velocity')
xlabel('t [s]')
ylabel('v [m/s]')
axis([0,t(end),0.9*min(v),1.1*max(v)])

subplot(3,3,7)
plot(t, gam, 'color',colors(1,:))
grid on
title('Flight Path Angle')
xlabel('t [s]')
ylabel('\gamma [deg]')
axis([0,t(end),1.1*min(gam),0.9*max(gam)])

subplot(3,3,2)
plot(t, p11,'color',colors(2,:))
grid on
title('Variance in h')
xlabel('t [s]')
ylabel('p_{11} [m^2]')
axis([0,t(end),0,max(p11)])

subplot(3,3,5)
plot(t, p22,'color',colors(2,:))
grid on
title('Variance in \theta')
xlabel('t [s]')
ylabel('p_{22} [rad^2]')
axis([0,t(end),0,max(p22)])

subplot(3,3,8)
plot(t, X(:,6) + X(:,10),'color',colors(2,:))
grid on
title('Path Cost')
xlabel('t [s]')
ylabel('cost')
axis([0,t(end),0,max(X(:,6) + X(:,10))])

subplot(3,3,3)
plot(t, 0.25*sin(u),'color',colors(3,:))
grid on
title('Control Law')
xlabel('t [s]')
ylabel('\partial\alpha/\partialt, [deg/s]')
axis([0,t(end),-.3,.3])

subplot(3,3,6)
plot(t, alpha,'color',colors(3,:))
grid on
title('Angle of Attack')
xlabel('t [s]')
ylabel('\alpha [deg]')
axis([0,t(end),1.1*min(alpha),1.1*max(alpha)])

subplot(3,3,9)
plot(t, lam_alpha,'color',colors(3,:))
grid on
title('Costate for Angle of Attack')
xlabel('t [s]')
ylabel('\lambda_\alpha')
axis([0,t(end),1.1*min(lam_alpha),1.1*max(lam_alpha)])

set(findobj('type','line'), 'LineWidth', 2.5);

%%%%

figure(2);
colors = get(gca, 'colororder');
clf

subplot(5,4,1)
plot(t, h,'color',colors(2,:))
grid on
title('height, h')
xlabel('t [s]')
ylabel('h [m]')

subplot(5,4,2)
plot(t, theta,'color',colors(2,:))
grid on
title('downrange angle, \theta')
xlabel('t [s]')
ylabel('\theta [rad]')

subplot(5,4,3)
plot(t, v,'color',colors(2,:))
grid on
title('velocity, v')
xlabel('t [s]')
ylabel('v [m/s]')

subplot(5,4,4)
plot(t, gam,'color',colors(2,:))
grid on
title('flight path angle, \gamma')
xlabel('t [s]')
ylabel('\gamma [rad]')


%%

subplot(5,4,5)
plot(t, p11)
grid on
title('p_{11}')
xlabel('t [s]')
ylabel('p_{11} [m^2]')

subplot(5,4,6)
plot(t, p12)%./sqrt(X(:,5).*X(:,9)))
grid on
title('p_{12}')
xlabel('t [s]')
ylabel('p_{12} [m*rad]')

subplot(5,4,7)
plot(t, p13)%./sqrt(X(:,5).*X(:,12)))
grid on
title('p_{13}')
xlabel('t [s]')
ylabel('p_{13} [m^2/s]')

subplot(5,4,8)
plot(t, p14)%./sqrt(X(:,5).*X(:,14)))
grid on
title('p_{14}')
xlabel('t [s]')
ylabel('p_{14} [m*rad]')

%%

subplot(5,4,10)
plot(t, p22)
grid on
title('p_{22}')
xlabel('t [s]')
ylabel('p_{22} [rad^2]')

subplot(5,4,11)
plot(t, p23)%./sqrt(X(:,9).*X(:,12)))
grid on
title('p_{23}')
xlabel('t [s]')
ylabel('p_{23} [m*rad/s]')

subplot(5,4,12)
plot(t, p24)%./sqrt(X(:,9).*X(:,14)))
grid on
title('p_{24}')
xlabel('t [s]')
ylabel('p_{24} [rad^2]')

%%

subplot(5,4,15)
plot(t, p33)
grid on
title('p_{33}')
xlabel('t [s]')
ylabel('p_{33} [m^2/s^2]')

subplot(5,4,16)
plot(t, p34)%./sqrt(X(:,12).*X(:,14)))
grid on
title('p_{34}')
xlabel('t [s]')
ylabel('p_{34} [m*rad/s]')

%%

subplot(5,4,19)
plot(t, X(:,6) + X(:,10),'r')
grid on
title('cost')
xlabel('t [s]')
ylabel('p_{11}_n + p_{22}_n [rad^2]')

subplot(5,4,20)
plot(t, p44)
grid on
title('p_{44}')
xlabel('t [s]')
ylabel('p_{44} [rad^2]')

%%

subplot(5,4,[13,14,17,18])
plot(theta, h, 'r*')
title('Flight Path')
xlabel('downrange angle, \theta [deg]')
ylabel('height, h [m]')
grid on


set(findobj('type','line'), 'LineWidth', 1.5);

%%

figure(3);
colors = get(gca, 'colororder');
clf

subplot(5,4,1)
plot(t, lam_h,'color',colors(2,:))
grid on
title('height, h')
xlabel('t [s]')
ylabel('h [m]')

subplot(5,4,2)
plot(t, lam_theta,'color',colors(2,:))
grid on
title('downrange angle, \theta')
xlabel('t [s]')
ylabel('\theta [rad]')

subplot(5,4,3)
plot(t, lam_v,'color',colors(2,:))
grid on
title('velocity, v')
xlabel('t [s]')
ylabel('v [m/s]')

subplot(5,4,4)
plot(t, lam_gam,'color',colors(2,:))
grid on
title('flight path angle, \gamma')
xlabel('t [s]')
ylabel('\gamma [rad]')


%%

subplot(5,4,5)
plot(t, lam_p11)
grid on
title('p_{11}')
xlabel('t [s]')
ylabel('p_{11} [m^2]')

subplot(5,4,6)
plot(t, lam_p12)%./sqrt(X(:,5).*X(:,9)))
grid on
title('p_{12}')
xlabel('t [s]')
ylabel('p_{12} [m*rad]')

subplot(5,4,7)
plot(t, lam_p13)%./sqrt(X(:,5).*X(:,12)))
grid on
title('p_{13}')
xlabel('t [s]')
ylabel('p_{13} [m^2/s]')

subplot(5,4,8)
plot(t, lam_p14)%./sqrt(X(:,5).*X(:,14)))
grid on
title('p_{14}')
xlabel('t [s]')
ylabel('p_{14} [m*rad]')

%%

subplot(5,4,10)
plot(t, lam_p22)
grid on
title('p_{22}')
xlabel('t [s]')
ylabel('p_{22} [rad^2]')

subplot(5,4,11)
plot(t, lam_p23)%./sqrt(X(:,9).*X(:,12)))
grid on
title('p_{23}')
xlabel('t [s]')
ylabel('p_{23} [m*rad/s]')

subplot(5,4,12)
plot(t, lam_p24)%./sqrt(X(:,9).*X(:,14)))
grid on
title('p_{24}')
xlabel('t [s]')
ylabel('p_{24} [rad^2]')

%%

subplot(5,4,15)
plot(t, lam_p33)
grid on
title('p_{33}')
xlabel('t [s]')
ylabel('p_{33} [m^2/s^2]')

subplot(5,4,16)
plot(t, lam_p34)%./sqrt(X(:,12).*X(:,14)))
grid on
title('p_{34}')
xlabel('t [s]')
ylabel('p_{34} [m*rad/s]')

%%

subplot(5,4,20)
plot(t, lam_p44)
grid on
title('p_{44}')
xlabel('t [s]')
ylabel('p_{44} [rad^2]')

%%

subplot(5,4,[13,14,17,18])
plot(t, lam_alpha, 'r')
title('Flight Path')
xlabel('downrange angle, \theta [deg]')
ylabel('height, h [m]')
grid on

set(findobj('type','line'), 'LineWidth', 1.5);


end

