function cart58

H = figure(1);
clf
colors = get(gca, 'colororder');

xb = linspace(5,7,10);
yb = linspace(5,7,10);

for k = 0:9;
    
    file = ['cart58nset',num2str(k)];
    
    X = load([file,'.txt'])';
    
    save([file,'.mat'], 'X')
    
    t = X(:,end);
        
    x     = X(:,1);
    y     = X(:,2);
    theta = X(:,3)*180/pi;
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
    lam_p33   = X(:,17);
    
    u = X(:,end-1);
        
    subplot(3,3,1)
    hold on
    plot(x, y, 'color',colors(1,:))
    grid on
    title('Trajectory')
    xlabel('x [m]')
    ylabel('y [m]')
    axis([0,80,-40,40])
    
    subplot(3,3,4)
    hold on
    plot(t, sqrt((x-xb(k+1)).^2+(y-yb(k+1)).^2), 'color',colors(1,:))
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
    hold on
    plot(t, p11,'color',colors(2,:))
    grid on
    title('Variance in x')
    xlabel('t [s]')
    ylabel('p_{11} [m^2]')
    
    subplot(3,3,5)
    hold on
    plot(t, p22,'color',colors(2,:))
    grid on
    title('Variance in y')
    xlabel('t [s]')
    ylabel('p_{22} [m^2]')
    
    subplot(3,3,8)
    hold on
    plot(t, p33,'color',colors(2,:))
    grid on
    title('Variance in \theta')
    xlabel('t [s]')
    ylabel('p_{33} [rad^2]')
    
    subplot(3,3,3)
    hold on
    plot(t, 0.1*sin(u),'color',colors(3,:))
    grid on
    title('Control Law')
    xlabel('t [s]')
    ylabel('\partial\theta/\partialt, [deg/s]')
    
    subplot(3,3,6)
    hold on
    plot(t, theta,'color',colors(3,:))
    grid on
    title('Angle')
    xlabel('t [s]')
    ylabel('\theta [deg]')
    
    subplot(3,3,9)
    hold on
    plot(t, lam_theta,'color',colors(3,:))
    grid on
    title('Costate for \theta')
    xlabel('t [s]')
    ylabel('\lambda_\theta')
    
%     set(findobj('type','line'), 'LineWidth', 2.5);
    
end

end

