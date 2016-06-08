function hyperKalman60plot

X = load('cart43.txt')';

save('cart43.mat', 'X')

t = X(:,end);

x     = X(:,1);
y     = X(:,2);
theta = X(:,3);
p11   = X(:,4);
p12   = X(:,5);
p13   = X(:,6);
p22   = X(:,7);
p23   = X(:,8);
p33   = X(:,9);

lam_x     = X(:,10);
lam_y     = X(:,11);
lam_theta = X(:,12);
lam_p11   = X(:,13);
lam_p12   = X(:,14);
lam_p13   = X(:,15);
lam_p22   = X(:,16);
lam_p33   = X(:,17);

u = X(:,end-1);

H = figure(1);
colors = get(gca, 'colororder');
clf

subplot(3,3,1)
plot(x, y, 'color',colors(1,:))
grid on
title('Trajectory')
xlabel('x [m]')
ylabel('y [m]')
axis([0,80,-40,40])

subplot(3,3,4)
plot(t, sqrt((x-10).^2+(y-10).^2), 'color',colors(1,:))
grid on
title('Measurement')
xlabel('t [s]')
ylabel('\rho [m]')

% subplot(3,3,7)
% plot(t, u, 'color',colors(1,:))
% grid on
% title('Flight Path Angle')
% xlabel('t [s]')
% ylabel('\gamma [deg]')

subplot(3,3,2)
plot(t, p11,'color',colors(2,:))
grid on
title('Variance in x')
xlabel('t [s]')
ylabel('p_{11} [m^2]')

subplot(3,3,5)
plot(t, p22,'color',colors(2,:))
grid on
title('Variance in y')
xlabel('t [s]')
ylabel('p_{22} [m^2]')

subplot(3,3,8)
plot(t, p33,'color',colors(2,:))
grid on
title('Variance in \theta')
xlabel('t [s]')
ylabel('p_{33} [rad^2]')

subplot(3,3,3)
plot(t, 0.1*sin(u),'color',colors(3,:))
grid on
title('Control Law')
xlabel('t [s]')
ylabel('\partial\alpha/\partialt, [deg/s]')

subplot(3,3,6)
plot(t, theta,'color',colors(3,:))
grid on
title('Angle')
xlabel('t [s]')
ylabel('\alpha [deg]')

subplot(3,3,9)
plot(t, lam_theta,'color',colors(3,:))
grid on
title('Costate for \theta')
xlabel('t [s]')
ylabel('\lambda_\theta')

set(findobj('type','line'), 'LineWidth', 2.5);

% %%%%
% 
% figure(2);
% colors = get(gca, 'colororder');
% clf
% 
% subplot(5,4,1)
% plot(t, h,'color',colors(2,:))
% grid on
% title('height, h')
% xlabel('t [s]')
% ylabel('h [m]')
% 
% subplot(5,4,2)
% plot(t, theta,'color',colors(2,:))
% grid on
% title('downrange angle, \theta')
% xlabel('t [s]')
% ylabel('\theta [rad]')
% 
% subplot(5,4,3)
% plot(t, v,'color',colors(2,:))
% grid on
% title('velocity, v')
% xlabel('t [s]')
% ylabel('v [m/s]')
% 
% subplot(5,4,4)
% plot(t, gam,'color',colors(2,:))
% grid on
% title('flight path angle, \gamma')
% xlabel('t [s]')
% ylabel('\gamma [rad]')
% 
% 
% %%
% 
% subplot(5,4,5)
% plot(t, p11)
% grid on
% title('p_{11}')
% xlabel('t [s]')
% ylabel('p_{11} [m^2]')
% 
% subplot(5,4,6)
% plot(t, p12)%./sqrt(X(:,5).*X(:,9)))
% grid on
% title('p_{12}')
% xlabel('t [s]')
% ylabel('p_{12} [m*rad]')
% 
% subplot(5,4,7)
% plot(t, p13)%./sqrt(X(:,5).*X(:,12)))
% grid on
% title('p_{13}')
% xlabel('t [s]')
% ylabel('p_{13} [m^2/s]')
% 
% subplot(5,4,8)
% plot(t, p14)%./sqrt(X(:,5).*X(:,14)))
% grid on
% title('p_{14}')
% xlabel('t [s]')
% ylabel('p_{14} [m*rad]')
% 
% %%
% 
% subplot(5,4,10)
% plot(t, p22)
% grid on
% title('p_{22}')
% xlabel('t [s]')
% ylabel('p_{22} [rad^2]')
% 
% subplot(5,4,11)
% plot(t, p23)%./sqrt(X(:,9).*X(:,12)))
% grid on
% title('p_{23}')
% xlabel('t [s]')
% ylabel('p_{23} [m*rad/s]')
% 
% subplot(5,4,12)
% plot(t, p24)%./sqrt(X(:,9).*X(:,14)))
% grid on
% title('p_{24}')
% xlabel('t [s]')
% ylabel('p_{24} [rad^2]')
% 
% %%
% 
% subplot(5,4,15)
% plot(t, p33)
% grid on
% title('p_{33}')
% xlabel('t [s]')
% ylabel('p_{33} [m^2/s^2]')
% 
% subplot(5,4,16)
% plot(t, p34)%./sqrt(X(:,12).*X(:,14)))
% grid on
% title('p_{34}')
% xlabel('t [s]')
% ylabel('p_{34} [m*rad/s]')
% 
% %%
% 
% subplot(5,4,19)
% plot(t, X(:,6) + X(:,10),'r')
% grid on
% title('cost')
% xlabel('t [s]')
% ylabel('p_{11}_n + p_{22}_n [rad^2]')
% 
% subplot(5,4,20)
% plot(t, p44)
% grid on
% title('p_{44}')
% xlabel('t [s]')
% ylabel('p_{44} [rad^2]')
% 
% %%
% 
% subplot(5,4,[13,14,17,18])
% plot(theta, h, 'r*')
% title('Flight Path')
% xlabel('downrange angle, \theta [deg]')
% ylabel('height, h [m]')
% grid on
% 
% 
% set(findobj('type','line'), 'LineWidth', 1.5);
% 
% %%
% 
% figure(3);
% colors = get(gca, 'colororder');
% clf
% 
% subplot(5,4,1)
% plot(t, lam_h,'color',colors(2,:))
% grid on
% title('height, h')
% xlabel('t [s]')
% ylabel('h [m]')
% 
% subplot(5,4,2)
% plot(t, lam_theta,'color',colors(2,:))
% grid on
% title('downrange angle, \theta')
% xlabel('t [s]')
% ylabel('\theta [rad]')
% 
% subplot(5,4,3)
% plot(t, lam_v,'color',colors(2,:))
% grid on
% title('velocity, v')
% xlabel('t [s]')
% ylabel('v [m/s]')
% 
% subplot(5,4,4)
% plot(t, lam_gam,'color',colors(2,:))
% grid on
% title('flight path angle, \gamma')
% xlabel('t [s]')
% ylabel('\gamma [rad]')
% 
% 
% %%
% 
% subplot(5,4,5)
% plot(t, lam_p11)
% grid on
% title('p_{11}')
% xlabel('t [s]')
% ylabel('p_{11} [m^2]')
% 
% subplot(5,4,6)
% plot(t, lam_p12)%./sqrt(X(:,5).*X(:,9)))
% grid on
% title('p_{12}')
% xlabel('t [s]')
% ylabel('p_{12} [m*rad]')
% 
% subplot(5,4,7)
% plot(t, lam_p13)%./sqrt(X(:,5).*X(:,12)))
% grid on
% title('p_{13}')
% xlabel('t [s]')
% ylabel('p_{13} [m^2/s]')
% 
% subplot(5,4,8)
% plot(t, lam_p14)%./sqrt(X(:,5).*X(:,14)))
% grid on
% title('p_{14}')
% xlabel('t [s]')
% ylabel('p_{14} [m*rad]')
% 
% %%
% 
% subplot(5,4,10)
% plot(t, lam_p22)
% grid on
% title('p_{22}')
% xlabel('t [s]')
% ylabel('p_{22} [rad^2]')
% 
% subplot(5,4,11)
% plot(t, lam_p23)%./sqrt(X(:,9).*X(:,12)))
% grid on
% title('p_{23}')
% xlabel('t [s]')
% ylabel('p_{23} [m*rad/s]')
% 
% subplot(5,4,12)
% plot(t, lam_p24)%./sqrt(X(:,9).*X(:,14)))
% grid on
% title('p_{24}')
% xlabel('t [s]')
% ylabel('p_{24} [rad^2]')
% 
% %%
% 
% subplot(5,4,15)
% plot(t, lam_p33)
% grid on
% title('p_{33}')
% xlabel('t [s]')
% ylabel('p_{33} [m^2/s^2]')
% 
% subplot(5,4,16)
% plot(t, lam_p34)%./sqrt(X(:,12).*X(:,14)))
% grid on
% title('p_{34}')
% xlabel('t [s]')
% ylabel('p_{34} [m*rad/s]')
% 
% %%
% 
% subplot(5,4,20)
% plot(t, lam_p44)
% grid on
% title('p_{44}')
% xlabel('t [s]')
% ylabel('p_{44} [rad^2]')
% 
% %%
% 
% subplot(5,4,[13,14,17,18])
% plot(t, lam_alpha, 'r')
% title('Flight Path')
% xlabel('downrange angle, \theta [deg]')
% ylabel('height, h [m]')
% grid on

set(findobj('type','line'), 'LineWidth', 1.5);


end

