%==========================================================================
% Makes some sweet graphics using data output by Beluga
% Author: Justin Mansell (2016)
%==========================================================================

%Construct Terrain Grid
x=linspace(0,10,50);
y=linspace(0,10,50);
terr=transpose(x)*y;
for i=1:length(x)
    for j=1:length(y)
        terr(i,j)=50*TerrainFunc(x(i),y(j));
    end
end

%Read Data from files
fileID=fopen('DillData25.txt','r');
sizeData=[2 Inf];
Dat25=fscanf(fileID,'%f %f',sizeData);
fclose(fileID);

fileID=fopen('DillData35.txt','r');
sizeData=[2 Inf];
Dat35=fscanf(fileID,'%f %f',sizeData);
fclose(fileID);

fileID=fopen('DillData45.txt','r');
sizeData=[2 Inf];
Dat45=fscanf(fileID,'%f %f',sizeData);
fclose(fileID);

fileID=fopen('DillData55.txt','r');
sizeData=[2 Inf];
Dat55=fscanf(fileID,'%f %f',sizeData);
fclose(fileID);

fileID=fopen('DillData65.txt','r');
sizeData=[2 Inf];
Dat65=fscanf(fileID,'%f %f',sizeData);
fclose(fileID);

fileID=fopen('DillData75.txt','r');
sizeData=[2 Inf];
Dat75=fscanf(fileID,'%f %f',sizeData);
fclose(fileID);

fileID=fopen('DillData15.txt','r');
sizeData=[2 Inf];
Dat15=fscanf(fileID,'%f %f',sizeData);
fclose(fileID);

%Create solution z vector
% Datz=zeros(6,length(Dat(1,:)));
% for j=1:6
%     for i=1:length(Datz)
%         Datz(j,i)=TerrainFunc(Dat(1+2*(j-1),i),Dat(2+2*(j-1),i))+0.1;
%     end
% end
Datz25=Dat25(1,:)*0.0;
Datz35=Dat35(1,:)*0.0;
Datz45=Dat45(1,:)*0.0;
Datz55=Dat55(1,:)*0.0;
Datz65=Dat65(1,:)*0.0;
Datz75=Dat75(1,:)*0.0;
Datz15=Dat15(1,:)*0.0;
for i=1:length(Datz25)
    Datz25(i)=50*TerrainFunc(Dat25(1,i),Dat25(2,i))+3;
end
for i=1:length(Datz35)
    Datz35(i)=50*TerrainFunc(Dat35(1,i),Dat35(2,i))+3;
end
for i=1:length(Datz45)
    Datz45(i)=50*TerrainFunc(Dat45(1,i),Dat45(2,i))+3;
end
for i=1:length(Datz55)
    Datz55(i)=50*TerrainFunc(Dat55(1,i),Dat55(2,i))+3;
end
for i=1:length(Datz65)
    Datz65(i)=50*TerrainFunc(Dat65(1,i),Dat65(2,i))+3;
end
for i=1:length(Datz75)
    Datz75(i)=50*TerrainFunc(Dat75(1,i),Dat75(2,i))+3;
end
for i=1:length(Datz15)
    Datz15(i)=50*TerrainFunc(Dat15(1,i),Dat15(2,i))+3;
end

%Plot Data

%Contour Plot
figure(1)
scatter([0.4,8.5],[4.9,7.2],75,'r')
hold on
plot(Dat25(2,:),Dat25(1,:),'r','Linewidth',1)
plot(Dat35(2,:),Dat35(1,:),'r','Linewidth',1)
plot(Dat45(2,:),Dat45(1,:),'r','Linewidth',1)
plot(Dat55(2,:),Dat55(1,:),'r','Linewidth',1)
plot(Dat65(2,:),Dat65(1,:),'r','Linewidth',1)
plot(Dat75(2,:),Dat75(1,:),'r','Linewidth',1)
plot(Dat15(2,:),Dat15(1,:),'r','Linewidth',1)
%plot(Dat(4,:),Dat(3,:),Dat(10,:),Dat(9,:),'r','Linewidth',2)
%plot(Dat(6,:),Dat(5,:),Dat(8,:),Dat(7,:),'r','Linewidth',3)
axis([0 10 0 10])
xlabel('East (km)')
ylabel('North (km)')
set(gca,'FontSize',12)
contour(y,x,terr,...
    'ShowText','on')
hold off

%forest=transpose(exp(-0.4*(y-4.5).^2))*exp(-0.2*(x-5.6).^2)+...
%    transpose(exp(-0.1*(y-2).^2))*exp(-0.5*(x-2.5).^2);
%colormapeditor

figure(2)
surf(y,x,terr)
axis([0 10 0 10 -inf 300])
xlabel('East (km)')
ylabel('North (km)')
zlabel('Elevation (m)')
hold on
plot3(Dat25(2,:),Dat25(1,:),Datz25,'r','Linewidth',3)
plot3(Dat35(2,:),Dat35(1,:),Datz35,'r','Linewidth',3)
plot3(Dat45(2,:),Dat45(1,:),Datz45,'r','Linewidth',3)
plot3(Dat55(2,:),Dat55(1,:),Datz55,'r','Linewidth',3)
plot3(Dat65(2,:),Dat65(1,:),Datz65,'r','Linewidth',3)
plot3(Dat75(2,:),Dat75(1,:),Datz75,'r','Linewidth',3)
plot3(Dat15(2,:),Dat15(1,:),Datz15,'r','Linewidth',3)

