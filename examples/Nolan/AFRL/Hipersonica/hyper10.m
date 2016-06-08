function hyper10

fig1 = 10;
fig2 = 200 + fig1;

n = 3;

figure(fig1);
clf
figure(fig2)
clf
% colors = get(gca, 'colororder');
colors = colormap(flipud(winter(n)));

mu = 3.986e5*1e9;
rho0 = 1.2;
h_ref = 7500;
mass = 750/2.2046226;
r_e = 6378000;
A_ref = pi*(24*0.0254/2)^2;
rn = 1/12*0.3048;

for k = 0:1:n-1;
    
    file = ['hyper10set',num2str(k)];
    
    X = load([file,'.txt'])';
    
    save([file,'.mat'], 'X')
    
    t = X(:,end);
    
    h     = X(:,1)*1000;
    theta = X(:,2)*1*pi/180;
    v     = X(:,3)*1000;
    gam   = X(:,4)*1*pi/180;
    alpha = X(:,5);
    p11   = X(:,6)*1e5;
    p12   = X(:,7)*1e-4;
    p13   = X(:,8)*1e2;
    p14   = X(:,9)*1e-1;
    p22   = X(:,10)*1e-9;
    p23   = X(:,11)*1e-4;
    p24   = X(:,12)*1e-8;
    p33   = X(:,13)*1e1;
    p34   = X(:,14)*1e-3;
    p44   = X(:,15)*1e-6;
    
    lam_h     = X(:,15);
    lam_theta = X(:,16);
    lam_v     = X(:,17);
    lam_gam   = X(:,18);
    lam_alpha = X(:,19);
    lam_p11   = X(:,20);
    lam_p12   = X(:,21);
    lam_p13   = X(:,22);
    lam_p14   = X(:,23);
    lam_p22   = X(:,24);
    lam_p23   = X(:,25);
    lam_p24   = X(:,26);
    lam_p33   = X(:,27);
    lam_p34   = X(:,28);
    lam_p44   = X(:,29);
    
    u = X(:,end-1);
    
    %%
    
    figure(fig1)
    
    subplot(5,4,[18,19])
    hold on
    plot(theta*180/pi, h, 'color',colors(k+1,:))
    grid on
    title('Trajectory')
    ylabel('h [m]')
    xlabel('\theta [deg]')
%     axis([0,250,-125,125])

    subplot(5,4,9)
    hold on
    plot(t, alpha,'color',colors(k+1,:))
    grid on
    title('Angle of Attack')
    xlabel('t [s]')
    ylabel('\alpha [deg]')
    
    subplot(5,4,13)
    hold on
    plot(t, sin(u)*0.25,'color',colors(k+1,:))
    grid on
    title('Control')
    xlabel('t [s]')
    ylabel('d\alpha/{dt} [deg]')
    
    subplot(5,4,17)
    hold on
    plot(t, lam_alpha, 'color',colors(k+1,:))
    grid on
    title('\lambda_\alpha')
    xlabel('t [s]')
    ylabel('\lambda_\alpha')
    
    subplot(5,4,14)
    hold on
    plot(t, -0.5.*A_ref.*rho0.*v.^2.*(5428.77686101442.*alpha.^2 + 0.0612).*exp(-h./h_ref)./mass - mu.*sin(gam)./(h + r_e).^2, 'color',colors(k+1,:))
    grid on
    title('Acceleration')
    xlabel('t [s]')
    ylabel('dv/dt')

    %
    
    subplot(5,4,1)
    hold on
    plot(t, h,'color',colors(k+1,:))
    grid on
    title('Altitude')
    xlabel('t [s]')
    ylabel('h [m]')
    
    subplot(5,4,2)
    hold on
    plot(t, theta*180/pi,'color',colors(k+1,:))
    grid on
    title('Downrange Angle')
    xlabel('t [s]')
    ylabel('\theta [deg]')
    
    subplot(5,4,3)
    hold on
    plot(t, v,'color',colors(k+1,:))
    grid on
    title('Velocity')
    xlabel('t [s]')
    ylabel('v [m/s]')
    
    subplot(5,4,4)
    hold on
    plot(t, gam*180/pi, 'color',colors(k+1,:))
    grid on
    title('Flight Path Angle')
    xlabel('t [s]')
    ylabel('\gamma [deg]')
    
    %
    
    subplot(5,4,5)
    hold on
    plot(t, p11, 'color',colors(k+1,:))
    grid on
    title('p_{11}')
    xlabel('t [s]')
    ylabel('p_{11} [m^2]')
    
    subplot(5,4,6)
    hold on
    plot(t, p12, 'color',colors(k+1,:))
    grid on
    title('p_{12}')
    xlabel('t [s]')
    ylabel('p_{12} [m*rad]')
    
    subplot(5,4,7)
    hold on
    plot(t, p13, 'color',colors(k+1,:))
    grid on
    title('p_{13}')
    xlabel('t [s]')
    ylabel('p_{13} [m^2/s]')
    
    subplot(5,4,8)
    hold on
    plot(t, p14, 'color',colors(k+1,:))
    grid on
    title('p_{14}')
    xlabel('t [s]')
    ylabel('p_{14} [m*rad]')
    
    %
    
    subplot(5,4,10)
    hold on
    plot(t, p22, 'color',colors(k+1,:))
    grid on
    title('p_{22}')
    xlabel('t [s]')
    ylabel('p_{22} [rad^2]')
    
    subplot(5,4,11)
    hold on
    plot(t, p23, 'color',colors(k+1,:))
    grid on
    title('p_{23}')
    xlabel('t [s]')
    ylabel('p_{23} [rad*m/s]')
    
    subplot(5,4,12)
    hold on
    plot(t, p24, 'color',colors(k+1,:))
    grid on
    title('p_{24}')
    xlabel('t [s]')
    ylabel('p_{24} [rad^2]')
    
    %
    
    subplot(5,4,15)
    hold on
    plot(t, p33, 'color',colors(k+1,:))
    grid on
    title('p_{33}')
    xlabel('t [s]')
    ylabel('p_{33} [m^2/s^2]')
    
    subplot(5,4,16)
    hold on
    plot(t, p34, 'color',colors(k+1,:))
    grid on
    title('p_{34}')
    xlabel('t [s]')
    ylabel('p_{34} [rad*m/s]')
    
    %
    
    subplot(5,4,20)
    hold on
    plot(t, p44, 'color',colors(k+1,:))
    grid on
    title('p_{44}')
    xlabel('t [s]')
    ylabel('p_{44} [rad^2]')
    
%%
    
    figure(fig2)
    
    subplot(5,4,1)
    hold on
    plot(t, lam_h,'color',colors(k+1,:))
    grid on
    title('\lambda_h')
    xlabel('t [s]')
    ylabel('\lambda_h')
    
    subplot(5,4,2)
    hold on
    plot(t, lam_theta,'color',colors(k+1,:))
    grid on
    title('\lambda_\theta')
    xlabel('t [s]')
    ylabel('\lambda_\theta')
    
    subplot(5,4,3)
    hold on
    plot(t, lam_v,'color',colors(k+1,:))
    grid on
    title('\lambda_v')
    xlabel('t [s]')
    ylabel('\lambda_v')
    
    subplot(5,4,4)
    hold on
    plot(t, lam_gam, 'color',colors(k+1,:))
    grid on
    title('\lambda_\gamma')
    xlabel('t [s]')
    ylabel('\lambda_\gamma')
    
    %
    
    subplot(5,4,5)
    hold on
    plot(t, lam_p11, 'color',colors(k+1,:))
    grid on
    title('\lambda_{p_{11}}')
    xlabel('t [s]')
    ylabel('\lambda_{p_{11}}')
    
    subplot(5,4,6)
    hold on
    plot(t, lam_p12, 'color',colors(k+1,:))
    grid on
    title('\lambda_{p_{12}}')
    xlabel('t [s]')
    ylabel('\lambda_{p_{12}}')
    
    subplot(5,4,7)
    hold on
    plot(t, lam_p13, 'color',colors(k+1,:))
    grid on
    title('\lambda_{p_{13}}')
    xlabel('t [s]')
    ylabel('\lambda_{p_{13}}')
    
    subplot(5,4,8)
    hold on
    plot(t, lam_p14, 'color',colors(k+1,:))
    grid on
    title('\lambda_{p_{14}}')
    xlabel('t [s]')
    ylabel('\lambda_{p_{14}}')
    
    %
    
    subplot(5,4,10)
    hold on
    plot(t, lam_p22, 'color',colors(k+1,:))
    grid on
    title('\lambda_{p_{22}}')
    xlabel('t [s]')
    ylabel('\lambda_{p_{22}}')
    
    subplot(5,4,11)
    hold on
    plot(t, lam_p23, 'color',colors(k+1,:))
    grid on
    title('\lambda_{p_{23}}')
    xlabel('t [s]')
    ylabel('\lambda_{p_{23}}')
    
    subplot(5,4,12)
    hold on
    plot(t, lam_p24, 'color',colors(k+1,:))
    grid on
    title('\lambda_{p_{24}}')
    xlabel('t [s]')
    ylabel('\lambda_{p_{24}}')
    
    %
    
    subplot(5,4,15)
    hold on
    plot(t, lam_p33, 'color',colors(k+1,:))
    grid on
    title('\lambda_{p_{33}}')
    xlabel('t [s]')
    ylabel('\lambda_{p_{33}}')
    
    subplot(5,4,16)
    hold on
    plot(t, lam_p34, 'color',colors(k+1,:))
    grid on
    title('\lambda_{p_{34}}')
    xlabel('t [s]')
    ylabel('\lambda_{p_{34}}')
    
    %
    
    subplot(5,4,20)
    hold on
    plot(t, lam_p44, 'color',colors(k+1,:))
    grid on
    title('\lambda_{p_{44}}')
    xlabel('t [s]')
    ylabel('\lambda_{p_{44}}')
    
    %
    
    subplot(5,4,13)
    hold on
    plot(t, lam_alpha, 'color',colors(k+1,:))
    grid on
    title('\lambda_\alpha')
    xlabel('t [s]')
    ylabel('\lambda_\alpha')
    
    
       
end

set(findobj('type','line'), 'LineWidth', 1.5);

end

