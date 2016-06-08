function cart67

n = 21;

figure(3);
clf
figure(4)
clf
% colors = get(gca, 'colororder');
colors = colormap(jet(n));

Dt = 0.1;
sigv = 0.1;
sigw = 0.1;
sigr = 0.1;

v = 30;

xb = 5;
yb = 5;

for k = 0:1:n;
    
    file = ['cart67set',num2str(k),'dist'];
    
    X = load([file,'.txt'])';
    
    save([file,'.mat'], 'X')
    
    t = X(:,end);
    
    x     = X(:,1);
    y     = X(:,2);
    theta = X(:,3);
    p11   = X(:,4)*1e-3;
    p12   = X(:,5)*1e-3;
    p13   = X(:,6)*1e-3;
    p22   = X(:,7)*1e-1;
    p23   = X(:,8)*1e-2;
    p33   = X(:,9)*1e-3;
    
    lam_x     = X(:,10);
    lam_y     = X(:,11);
    lam_theta = X(:,12);
    lam_p11   = X(:,13);
    lam_p12   = X(:,14);
    lam_p13   = X(:,15);
    lam_p22   = X(:,16);
    lam_p23   = X(:,17);
    lam_p33   = X(:,18);
    
    u = X(:,end-1);
    
    figure(3)
    
    subplot(3,4,1)
    hold on
    plot(x, y, 'color',colors(k+1,:))
    grid on
    title('Trajectory')
    xlabel('x [m]')
    ylabel('y [m]')
    axis([0,80,-40,40])
    
    subplot(3,4,6)
    hold on
    plot(t, sqrt((x-xb).^2+(y-yb).^2),'color',colors(k+1,:))
    grid on
    title('Measurement')
    xlabel('t [s]')
    ylabel('\rho [m]')
    
    subplot(3,4,5)
    hold on
    plot(t,p13.*v.*cos(theta) + p23.*v.*cos(theta), ...
        t, - p12.*(x - xb).*(p12.*(x - xb)./sqrt((x - xb).^2 + (y - yb).^2) + p22.*(y - yb)./sqrt((x - xb).^2 + (y - yb).^2))./(Dt.*sigr.^2.*sqrt((x - xb).^2 + (y - yb).^2)) - p22.*(y - yb).*(p12.*(x - xb)./sqrt((x - xb).^2 + (y - yb).^2) + p22.*(y - yb)./sqrt((x - xb).^2 + (y - yb).^2))./(Dt.*sigr.^2.*sqrt((x - xb).^2 + (y - yb).^2)),...
        t,  Dt*sigv.^2.*sin(theta).^2, ...
        t, Dt.*sigv.^2.*sin(theta).^2 + p13.*v.*cos(theta) + p23.*v.*cos(theta) - p12.*(x - xb).*(p12.*(x - xb)./sqrt((x - xb).^2 + (y - yb).^2) + p22.*(y - yb)./sqrt((x - xb).^2 + (y - yb).^2))./(Dt.*sigr.^2.*sqrt((x - xb).^2 + (y - yb).^2)) - p22.*(y - yb).*(p12.*(x - xb)./sqrt((x - xb).^2 + (y - yb).^2) + p22.*(y - yb)./sqrt((x - xb).^2 + (y - yb).^2))./(Dt.*sigr.^2.*sqrt((x - xb).^2 + (y - yb).^2)))
    grid on
    title('Cost Components')
    xlabel('t [s]')
    ylabel('dp_{22}/dt (from component) [m^2]')
    %     - p12.*(x - xb).*(p12.*(x - xb)./sqrt((x - xb)^2 + (y - yb)^2) + p22.*(y - yb)./sqrt((x - xb)^2 + (y - yb)^2))./(Dt.*sigr^2.*sqrt((x - xb)^2 + (y - yb)^2)) - p22.*(y - yb).*(p12.*(x - xb)./sqrt((x - xb)^2 + (y - yb)^2) + p22.*(y - yb)./sqrt((x - xb)^2 + (y - yb)^2))./(Dt.*sigr^2.*sqrt((x - xb)^2 + (y - yb)^2))
    
    subplot(3,4,2)
    hold on
    plot(t, p11,'color',colors(k+1,:))
    grid on
    title('Variance in x')
    xlabel('t [s]')
    ylabel('p_{11} [m^2]')
    
    subplot(3,4,3)
    hold on
    plot(t, p12,'color',colors(k+1,:))
    grid on
    %     title('Variance in x')
    xlabel('t [s]')
    ylabel('p_{12} [m^2]')
    
    subplot(3,4,4)
    hold on
    plot(t, p13,'color',colors(k+1,:))
    grid on
    %     title('Variance in x')
    xlabel('t [s]')
    ylabel('p_{13} [m*rad]')
    
    subplot(3,4,7)
    hold on
    plot(t, p22,'color',colors(k+1,:))
    grid on
    title('Variance in y')
    xlabel('t [s]')
    ylabel('p_{22} [m^2]')
    
    subplot(3,4,8)
    hold on
    plot(t, p23,'color',colors(k+1,:))
    grid on
    %     title('Variance in y')
    xlabel('t [s]')
    ylabel('p_{23} [m*rad]')
    
    subplot(3,4,12)
    hold on
    plot(t, p33,'color',colors(k+1,:))
    grid on
    title('Variance in \theta')
    xlabel('t [s]')
    ylabel('p_{33} [rad^2]')
    
    subplot(3,4,9)
    hold on
    plot(t, 0.1*sin(u),'color',colors(k+1,:))
    grid on
    title('Control Law')
    xlabel('t [s]')
    ylabel('\partial\theta/\partialt, [rad/s]')
    
    subplot(3,4,10)
    hold on
    plot(t, theta*180/pi,'color',colors(k+1,:))
    grid on
    title('Angle')
    xlabel('t [s]')
    ylabel('\theta [deg]')
    
    subplot(3,4,11)
    hold on
    plot(t, lam_theta,'color',colors(k+1,:))
    grid on
    title('Costate for \theta')
    xlabel('t [s]')
    ylabel('\lambda_\theta')
    
    %     set(findobj('type','line'), 'LineWidth', 2.5);
    
    %%%
    
    figure(4)
    
    subplot(3,4,1)
    hold on
    plot(t, lam_x, 'color',colors(k+1,:))
    grid on
    title('Costate for x')
    xlabel('t')
    ylabel('\lambda_x')
    
    subplot(3,4,5)
    hold on
    plot(t, lam_y, 'color',colors(k+1,:))
    grid on
    title('Costate for y')
    xlabel('t')
    ylabel('\lambda_y')
    
    subplot(3,4,9)
    hold on
    plot(t, lam_theta, 'color',colors(k+1,:))
    grid on
    title('Costate for \theta')
    xlabel('t')
    ylabel('\lambda_\theta')
    
    subplot(3,4,2)
    hold on
    plot(t, lam_p11, 'color',colors(k+1,:))
    grid on
    title('Costate for p_{11}')
    xlabel('t')
    ylabel('\lambda_{p_{11}}')
    
    subplot(3,4,3)
    hold on
    plot(t, lam_p12, 'color',colors(k+1,:))
    grid on
    title('Costate for p_{12}')
    xlabel('t')
    ylabel('\lambda_{p_{12}}')    
    
    subplot(3,4,4)
    hold on
    plot(t, lam_p13, 'color',colors(k+1,:))
    grid on
    title('Costate for p_{13}')
    xlabel('t')
    ylabel('\lambda_{p_{13}}')
    
    subplot(3,4,7)
    hold on
    plot(t, lam_p22, 'color',colors(k+1,:))
    grid on
    title('Costate for p_{22}')
    xlabel('t')
    ylabel('\lambda_{p_{22}}')
    
    subplot(3,4,8)
    hold on
    plot(t, lam_p23, 'color',colors(k+1,:))
    grid on
    title('Costate for p_{23}')
    xlabel('t')
    ylabel('\lambda_{p_{23}}')
    
    subplot(3,4,12)
    hold on
    plot(t, lam_p33, 'color',colors(k+1,:))
    grid on
    title('Costate for p_{33}')
    xlabel('t')
    ylabel('\lambda_{p_{33}}')
       
end

set(findobj('type','line'), 'LineWidth', 1.5);

end

