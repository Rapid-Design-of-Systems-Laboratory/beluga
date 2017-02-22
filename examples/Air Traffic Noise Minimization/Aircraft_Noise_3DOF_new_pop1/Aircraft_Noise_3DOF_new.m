function [in] = Aircraft_Noise_3DOF_new() 
% 
% This function creates input for the optimization problem,  
% which is later used by other functions  
% 
% input : void 
% output : in [structure] 
% Developed by : Kshitij Mall and Janav Udani
% Last modified: 25 Nov, 2016 

%%%%%%%%%%%%%%%%%%%%%%%
%% Execution Control %%
%%%%%%%%%%%%%%%%%%%%%%%

in.oc.writeEquations = false; % Determine if we need to regenerate the equation files

%%%%%%%%%%%%%
%% Scaling %%
%%%%%%%%%%%%%

% Doubles must be equal to one (not dynamically updated during continuation)
in.autoScale = true;

in.scale = {'m',1; ...
    'rad',1; ...
    's',1; ...
    'kg',1; ...
    'nd',1}; % nd = nondimensional

%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Independent Variable %%
%%%%%%%%%%%%%%%%%%%%%%%%%%
% e.g., time

in.oc.independentVariable = {'t','s'}; % time

%%%%%%%%%%%%
%% States %%
%%%%%%%%%%%%

in.oc.state = {'x','m'; ... % longitude, positive eastward
			   'y','m'; ... % latitude, positive northward
			   'z','m'; ... % radial position magnitude
               'v','m/s';...% velocity
			   'psii','rad'; ... % Azimuth
			   'gam','rad'};... % relative flight-path angle 

%%%%%%%%%%%%%%%%%%%%%%%%%
%% Equations of Motion %%
%%%%%%%%%%%%%%%%%%%%%%%%%

bank = '(bankmax*sin(banktrig))';
alfa = '(alfamax*sin(alfatrig))';
D = '(C1*v^2+C2/(v^2))';
L = '(mass*g)';
T = '(1560*sin(Ttrignew)+1860)';
Ft = ['(',T,'*cos(',alfa,')-',D,')']; % force along velocity vector
Fn = ['(',T,'*sin(',alfa,')+',L,')']; % force perpendicular to velocity vector

pop = '1';

in.oc.stateRate = {'v*cos(gam)*cos(psii)'; ...
				   'v*cos(gam)*sin(psii)'; ...
                   'v*sin(gam)'; ...
                   [Ft,'/mass - g*sin(gam)']; ... 
                   [Fn,'*sin(',bank,')/(mass*cos(gam)*v)'];...
  				   [Fn,'*cos(',bank,')/(mass*v) - g*cos(gam)/v']};   
            
%%%%%%%%%%%%%
%% Control %%
%%%%%%%%%%%%%

in.oc.control = {'banktrig','rad';...
                 'alfatrig','rad';...
                 'Ttrignew','kg*m/s^2'};
in.oc.assumptions.control = ''; % assumptions for Mathematica when solving for control

%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Objective Information %%
%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Maximize/minimize
in.minimize = true;

% Path cost
in.oc.cost.path = {[pop,'*',T,'^5.2*cos(gam)/(v*(z+50)^2.5)'],'nd'};

% Terminal cost
in.oc.cost.terminal = {'0','nd'};

% Initial cost
in.oc.cost.initial = {'0','nd'};

%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Endpoint Constraints %%
%%%%%%%%%%%%%%%%%%%%%%%%%%

% Initial constraint 
in.oc.constraint.initial = {'x-x0(1)','m'; ...
							'y-x0(2)','m'; ...
							'z-x0(3)','m'; ...
                            'v-x0(4)','m/s';...
							'psii-x0(5)','rad'; ...
							'gam-x0(6)','rad'};
													
% Terminal constraint
in.oc.constraint.terminal = {'x-xf(1)','m'; ...
							 'y-xf(2)','m'; ...
							 'z-xf(3)','m'; ...
                             'v-xf(4)','m/s';...
							 'psii-xf(5)','rad'; ...
							 'gam-xf(6)','rad'};

%%%%%%%%%%%%%%%
%% Constants %%
%%%%%%%%%%%%%%%
in.const.mu = {3.986e5*1e9,'m^3/s^2'}; % Gravitational parameter, m^3/s^2
in.const.rho0 = {1.2,'kg/m^3'}; % Sea-level atmospheric density, kg/m^3
in.const.H = {7500,'m'}; % Scale height for atmosphere of Earth, m
in.const.re = {6378000,'m'}; % Radius of planet, m
in.const.Aref = {112,'m^2'};
in.const.bankmax = {60*pi/180,'rad'};
in.const.alfamax = {15*pi/180,'rad'};
in.const.Tmax  = {3420,'kg*m/s^2'};
in.const.Tmin  = {300,'kg*m/s^2'};
in.const.g  = {9.81,'m/s^2'};
in.const.mass  = {7180/9.81,'kg'}; % 7180
in.const.C1  = {0.226,'kg/m'};
in.const.C2  = {5.2e6,'kg*m^3/s^4'};

%%%%%%%%%%%%%%%%%%%
%% Initial Guess %%
%%%%%%%%%%%%%%%%%%%
in.oc.guess.mode = 'auto';
in.oc.guess.timeIntegrate = 40; % 10 runs with 1 as costate guess

% % Use automatic init
% Conditions at entry

in.oc.guess.initial.x = 0;
in.oc.guess.initial.y = 0;
in.oc.guess.initial.z = 1197;
in.oc.guess.initial.v = 124;  
in.oc.guess.initial.psii = 0*pi/180;
in.oc.guess.initial.gam = 0*pi/180;
in.oc.guess.costate = 1e5; 

ind = 0;

%%%%%%%%%%%%%%%%%%%%%%
%% Continuation Set %%
%%%%%%%%%%%%%%%%%%%%%%
 
ind = ind+1;
in.cont.method(ind) = 1;
in.CONT{ind}.numCases = 20; % Number of steps in the continuation set

in.CONT{ind}.constraint.terminal.x = 5400;
in.CONT{ind}.constraint.terminal.y = 4600; 
in.CONT{ind}.constraint.terminal.z = 0;
in.CONT{ind}.constraint.terminal.v = 77.5; 
in.CONT{ind}.constraint.terminal.psii = 45*pi/180;
in.CONT{ind}.constraint.terminal.gam = 0;

% %%%%%%%%%%%%%%%%%%%%%%
% %% Continuation Set %%
% %%%%%%%%%%%%%%%%%%%%%%
% 
% ind = ind+1;
% in.cont.method(ind) = 1;
% 
% in.CONT{ind}.numCases = 2;% Number of steps in the continuation set 
% in.CONT{ind}.constraint.terminal.x = 6000;
% in.CONT{ind}.constraint.terminal.y = 5000;
%  
return
