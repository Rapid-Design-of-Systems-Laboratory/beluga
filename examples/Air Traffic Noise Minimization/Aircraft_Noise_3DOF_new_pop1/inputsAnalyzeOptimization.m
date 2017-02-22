function [in] = inputsAnalyzeOptimization()

%%%%%%%%%%%%%%%%%
%% Output File %%
%%%%%%%%%%%%%%%%%

in.outputFile{1} = 'data/results_bvp4c_pop1.mat';
ind = 0;

%%%%%%%%%%%%%%%%%%%%%
%% Plotting Inputs %%
%%%%%%%%%%%%%%%%%%%%%

% General plotting items
in.plot.linewidth = 1;
in.plot.markersize = 10;
in.plot.title = true;
in.plot.presentation = true;
in.plot.legend = false;

in.plot.colorSegments.flag = false;
in.plot.colorSegments.colorSet = {'k','r','b'};

% Initial guess
in.plot.initialGuess.flag = false;
in.plot.initialGuess.style = '--';

% Continuation
in.plot.continuation.flag = true;
in.plot.continuation.style = {'k'};
in.plot.contStartCtr = 0; % 0 = only last solution. Fraction = fraction*numCases
in.plot.contSkip = 1; % How many solutions to skip for plotting, 0 = skip all but last solution (to create envelopes)
in.cont.Index = 1; % Continuation index for plotting

% General movie options
in.movie.fps = 5;
in.movie.quality = 100;
in.movie.compression = 'None';

bank = '(60*pi/180*sin(banktrig))';
alfa = '(15*pi/180*sin(alfatrig))';
D = '(0.226*v^2+5.2e6/(v^2))';
L = '(7180)';
T = '(1560*sin(Ttrignew)+1860)';
Ft = ['(',T,'*cos(',alfa,')-',D,')']; % force along velocity vector
Fn = ['(',T,'*sin(',alfa,')+',L,')']; % force perpendicular to velocity vector

pop = '1';
H = [pop,'*',T,'^5.2*cos(gam)/(v*(z+50)^2.5) + lamX*(v*cos(gam)*cos(psii)) + lamY*(v*cos(gam)*sin(psii)) + lamZ*(v*sin(gam)) + lamV*(',Ft,'/mass - g*sin(gam)) + lamPSII*(',Fn,'*sin(',bank,')/(mass*cos(gam)*v)) + lamGAM*(',Fn,'*cos(',bank,')/(mass*v) - g*cos(gam)/v)'];

%%%%%%%%%%%%%%%%%%%
%% Regular Plots %%
%%%%%%%%%%%%%%%%%%%

% Specify regular plots to make (lamR for costate of r, t for time)
% {variable name,bias,scaleFactor,units,plotName}
ind = ind+1;
in.figure(ind).plot(1).x{1} = {'t','s','Time'};
in.figure(ind).plot(1).y{1} = {'x/1000','km','Downrange'};
in.figure(ind).plot(1).legend.location = 'NorthWest';
in.figure(ind).plot(2).x{1} = {'t','s','Time'};
in.figure(ind).plot(2).y{1} = {'y/1000','km','Crossrange'};
in.figure(ind).plot(2).legend.location = 'NorthWest';
in.figure(ind).plot(3).x{1} = {'t','s','Time'};
in.figure(ind).plot(3).y{1} = {'z/1000','km','Altitude'};
in.figure(ind).plot(3).legend.location = 'NorthWest';
in.figure(ind).plot(4).x{1} = {'t','s','Time'};
in.figure(ind).plot(4).y{1} = {'v','m/s','Velocity'};
in.figure(ind).plot(4).legend.location = 'NorthWest';
in.figure(ind).plot(5).x{1} = {'t','s','Time'};
in.figure(ind).plot(5).y{1} = {'psii*180/pi','deg','Heading Angle'};
in.figure(ind).plot(5).legend.location = 'NorthWest';
in.figure(ind).plot(6).x{1} = {'t','s','Time'};
in.figure(ind).plot(6).y{1} = {'gam*180/pi','deg','Flight-Path Angle'};
in.figure(ind).plot(6).legend.location = 'NorthWest';
in.figure(ind).movie.make = false;
in.figure(ind).movie.name = 'testMovie';
in.figure(ind).movie.figPos = [1 31 1280 856*0.9];

ind = ind+1;
in.figure(ind).plot(1).x{1} = {'t','s','Time'};
in.figure(ind).plot(1).y{1} = {'60*sin(banktrig)','deg','Bank Angle'};
in.figure(ind).plot(1).legend.location = 'NorthWest';
in.figure(ind).plot(2).x{1} = {'t','s','Time'};
in.figure(ind).plot(2).y{1} = {'15*sin(alfatrig)','deg','Angle of Attack'};
in.figure(ind).plot(2).legend.location = 'NorthEast';
in.figure(ind).plot(3).x{1} = {'t','s','Time'};
in.figure(ind).plot(3).y{1} = {'1560*sin(Ttrignew)+1860','N','Thrust'};
in.figure(ind).plot(3).legend.location = 'NorthEast';
in.figure(ind).movie.make = false;
in.figure(ind).movie.name = 'testMovie';
in.figure(ind).movie.figPos = [1 31 1280 856*0.9];
% ind = ind+1;
% in.figure(ind).plot(1).x{1} = {'t','s','Time'};
% in.figure(ind).plot(1).y{1} = {'lamZ*v*sin(gam) - lamGAM*((g*cos(gam))/v - (cos(bank)*(L + T*(1 - (D + g*mass*sin(gam))^2/T^2)^(1/2)))/(mass*v)) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bank)*(L + T*(1 - (D + g*mass*sin(gam))^2/T^2)^(1/2)))/(mass*v*cos(gam)) + 1','nd','Hamiltonian'};
% in.figure(ind).plot(1).legend.location = 'NorthWest';
% in.figure(ind).movie.make = false;
% in.figure(ind).movie.name = 'testMovie';
% in.figure(ind).movie.figPos = [1 31 1280 856*0.9];

ind = ind+1;
in.figure(ind).plot(1).x{1} = {'t','s','Time'};
in.figure(ind).plot(1).y{1} = {'10*log10(18.73*((1560*sin(Ttrignew)+1860)^5.2)*cos(gam)/(v*(z+50)^2.5))','dB','Noise'};
in.figure(ind).plot(1).legend.location = 'NorthWest';
in.figure(ind).movie.make = false;
in.figure(ind).movie.name = 'testMovie';
in.figure(ind).movie.figPos = [1 31 1280 856*0.9];
%%%%%%%%%%%%%%
%% Subplots %%
%%%%%%%%%%%%%%

ind = ind+1;
in.figure(ind).plot(1).x{1} = {'t','s','Time'};
in.figure(ind).plot(1).y{1} = {'lamX','s/m','\lambda_x'};
in.figure(ind).plot(1).legend.location = 'NorthEast';
in.figure(ind).plot(2).x{1} = {'t','s','Time'};
in.figure(ind).plot(2).y{1} = {'lamY','s/m','\lambda_y'};
in.figure(ind).plot(2).legend.location = 'NorthEast';
in.figure(ind).plot(3).x{1} = {'t','s','Time'};
in.figure(ind).plot(3).y{1} = {'lamZ','s/m','\lambda_z'};
in.figure(ind).plot(3).legend.location = 'NorthEast';
in.figure(ind).plot(4).x{1} = {'t','s','Time'};
in.figure(ind).plot(4).y{1} = {'lamV','s^2/m','\lambda_v'};
in.figure(ind).plot(4).legend.location = 'SouthEast';
in.figure(ind).plot(5).x{1} = {'t','s','Time'};
in.figure(ind).plot(5).y{1} = {'lamPSII','s/rad','\lambda_\psi'};
in.figure(ind).plot(5).legend.location = 'NorthWest';
in.figure(ind).plot(6).x{1} = {'t','s','Time'};
in.figure(ind).plot(6).y{1} = {'lamGAM','s/rad','\lambda_\gamma'};
in.figure(ind).plot(6).legend.location = 'NorthWest';
in.figure(ind).movie.make = false;
in.figure(ind).movie.name = 'testMovie';
in.figure(ind).movie.figPos = [1 31 1280 856*0.9];

ind = ind+1;
in.figure(ind).plot(1).x{1} = {'x/1000','km','Downrange'};
in.figure(ind).plot(1).y{1} = {'z/1000','km','Altitude'};
in.figure(ind).plot(1).legend.location = 'NorthWest';
in.figure(ind).movie.make = false;
in.figure(ind).movie.name = 'testMovie';
in.figure(ind).movie.figPos = [1 31 1280 856*0.9];

ind = ind+1;
in.figure(ind).plot(1).x{1} = {'y/1000','km','Crossrange'};
in.figure(ind).plot(1).y{1} = {'z/1000','km','Altitude'};
in.figure(ind).plot(1).legend.location = 'NorthWest';
in.figure(ind).movie.make = false;
in.figure(ind).movie.name = 'testMovie';
in.figure(ind).movie.figPos = [1 31 1280 856*0.9];

ind = ind+1;
in.figure(ind).plot(1).x{1} = {'t','s','Time'};
in.figure(ind).plot(1).y{1} = {H,'nd','Hamiltonian'};
in.figure(ind).plot(1).legend.location = 'NorthWest';
in.figure(ind).movie.make = false;
in.figure(ind).movie.name = 'testMovie';
in.figure(ind).movie.figPos = [1 31 1280 856*0.9];
return