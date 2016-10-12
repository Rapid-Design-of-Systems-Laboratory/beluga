%==========================================================================
% Makes some sweet graphics using data output by Beluga
% Author: Justin Mansell (2016)
%==========================================================================

%Construct Terrain Grid
x=linspace(0,10,20);
y=linspace(0,10,20);
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

fileID=fopen('DillData00.txt','r');
sizeData=[2 Inf];
Dat00=fscanf(fileID,'%f %f',sizeData);
fclose(fileID);

%Create solution z vector
% Datz=zeros(7,length(Dat00));
% for j=1:7
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
Datz00=Dat00(1,:)*0.0;
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
for i=1:length(Datz00)
    Datz00(i)=50*TerrainFunc(Dat00(1,i),Dat00(2,i))+3;
end

%Plot Data

%Contour Plot
cbar=transpose(linspace(0.0,1.0,8));
cbar=[cbar zeros(8,1) zeros(8,1)];
%cbar=[zeros(8,1)+1 zeros(8,1) cbar];
%cbar=spring(8);
%cbar=flipud(cbar);
figure(1)
scatter([0.4,8.5],[4.9,7.2],75,[1 0 1],'filled')
hold on

axis([0 10 0 10])
xlabel('East (km)')
ylabel('North (km)')
set(gca,'FontSize',14)
contour(y,x,terr,'ShowText','on')

p0=plot(Dat00(2,:),Dat00(1,:),'Color',cbar(1,:),'Linewidth',1.5);
plot(Dat15(2,:),Dat15(1,:),'Color',cbar(2,:),'Linewidth',1.5)
plot(Dat25(2,:),Dat25(1,:),'Color',cbar(3,:),'Linewidth',1.5)
plot(Dat35(2,:),Dat35(1,:),'Color',cbar(4,:),'Linewidth',1.5)
plot(Dat45(2,:),Dat45(1,:),'Color',cbar(5,:),'Linewidth',1.5)
plot(Dat55(2,:),Dat55(1,:),'Color',cbar(6,:),'Linewidth',1.5)
plot(Dat65(2,:),Dat65(1,:),'Color',cbar(7,:),'Linewidth',1.5)
p75=plot(Dat75(2,:),Dat75(1,:),'Color',cbar(8,:),'Linewidth',1.5);


% plot(Dat00(2,:),Dat00(1,:),'r','Linewidth',0.25)
% plot(Dat15(2,:),Dat15(1,:),'r','Linewidth',0.5)
% plot(Dat25(2,:),Dat25(1,:),'r','Linewidth',0.75)
% plot(Dat35(2,:),Dat35(1,:),'r','Linewidth',1.0)
% plot(Dat45(2,:),Dat45(1,:),'r','Linewidth',1.25)
% plot(Dat55(2,:),Dat55(1,:),'r','Linewidth',1.5)
% plot(Dat65(2,:),Dat65(1,:),'r','Linewidth',1.75)
% plot(Dat75(2,:),Dat75(1,:),'r','Linewidth',2)

%plot(Dat(4,:),Dat(3,:),Dat(10,:),Dat(9,:),'r','Linewidth',2)
%plot(Dat(6,:),Dat(5,:),Dat(8,:),Dat(7,:),'r','Linewidth',3)
plegend=legend([p0 p75],'w=0','w=0.75','Location','Northwest');
set(plegend,'FontSize',14)
set(gca,'XTick',[0 2 4 6 8 10])
set(gca,'YTick',[0 2 4 6 8 10])
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
p0=plot3(Dat00(2,:),Dat00(1,:),Datz00,'Color',cbar(1,:),'Linewidth',3);
plot3(Dat15(2,:),Dat15(1,:),Datz15,'Color',cbar(2,:),'Linewidth',3)
plot3(Dat25(2,:),Dat25(1,:),Datz25,'Color',cbar(3,:),'Linewidth',3)
plot3(Dat35(2,:),Dat35(1,:),Datz35,'Color',cbar(4,:),'Linewidth',3)
plot3(Dat45(2,:),Dat45(1,:),Datz45,'Color',cbar(5,:),'Linewidth',3)
plot3(Dat55(2,:),Dat55(1,:),Datz55,'Color',cbar(6,:),'Linewidth',3)
plot3(Dat65(2,:),Dat65(1,:),Datz65,'Color',cbar(7,:),'Linewidth',3)
p75=plot3(Dat75(2,:),Dat75(1,:),Datz75,'Color',cbar(8,:),'Linewidth',3);
set(gca,'FontSize',14)
plegend=legend([p0 p75],'w=0','w=0.75','Location','West');
set(plegend,'FontSize',14)
scatter3([0.4,8.5],[4.9,7.2],[50*TerrainFunc(4.9,0.4)+3 50*TerrainFunc(7.2,8.5)+3],...
    75,[1 0 1],'filled')



