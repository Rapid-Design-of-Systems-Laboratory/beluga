function [banktrigSave,alfatrigSave,TtrignewSave,hamiltonianSave] = computeControlUnconstrained(xAndLambda,const,constraint,numArcs)
coder.extrinsic('keyboard');
%#codegen
assert(isa(const,'struct'));
assert(isa(const.Aref,'double'));
assert(isa(const.C1,'double'));
assert(isa(const.C2,'double'));
assert(isa(const.H,'double'));
assert(isa(const.Tmax,'double'));
assert(isa(const.Tmin,'double'));
assert(isa(const.alfamax,'double'));
assert(isa(const.bankmax,'double'));
assert(isa(const.epsilon,'double'));
assert(isa(const.g,'double'));
assert(isa(const.mass,'double'));
assert(isa(const.mu,'double'));
assert(isa(const.re,'double'));
assert(isa(const.rho0,'double'));
assert(isa(constraint,'struct'));
assert(isa(xAndLambda,'double'));
assert(all(size(xAndLambda)== [12,1]));
assert(isa(numArcs,'double'));
assert(all(size(numArcs)== [1,1]));
% Constants
Aref = const.Aref;
C1 = const.C1;
C2 = const.C2;
H = const.H;
Tmax = const.Tmax;
Tmin = const.Tmin;
alfamax = const.alfamax;
bankmax = const.bankmax;
epsilon = const.epsilon;
g = const.g;
mass = const.mass;
mu = const.mu;
re = const.re;
rho0 = const.rho0;




% States
x = complex(xAndLambda(1,1));
y = complex(xAndLambda(2,1));
z = complex(xAndLambda(3,1));
v = complex(xAndLambda(4,1));
psii = complex(xAndLambda(5,1));
gam = complex(xAndLambda(6,1));

% Costates
lamX = complex(xAndLambda(7,1));
lamY = complex(xAndLambda(8,1));
lamZ = complex(xAndLambda(9,1));
lamV = complex(xAndLambda(10,1));
lamPSII = complex(xAndLambda(11,1));
lamGAM = complex(xAndLambda(12,1));

% Control
banktrig = NaN;
banktrigSave = NaN;
alfatrig = NaN;
alfatrigSave = NaN;
Ttrignew = NaN;
TtrignewSave = NaN;

hamiltonian = inf;
hamiltonianSave = inf;
I = 1i;
% Coefficients
banktrig = real(-pi/2);
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(-pi/2);
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
% Coefficients
banktrig = real(pi/2);
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(-pi/2);
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(-asin(3.1416/(2*bankmax)));
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(-pi/2);
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(asin(3.1416/(2*bankmax)));
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(-pi/2);
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(-pi/2);
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(pi/2);
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(pi/2);
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(pi/2);
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(-asin(3.1416/(2*bankmax)));
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(pi/2);
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(asin(3.1416/(2*bankmax)));
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(pi/2);
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(-pi/2);
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(-asin(acos(-((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig)))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(pi/2);
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(-asin(acos(-((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig)))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(-asin(3.1416/(2*bankmax)));
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(-asin(acos(-((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig)))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(asin(3.1416/(2*bankmax)));
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(-asin(acos(-((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig)))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(-pi/2);
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(asin(acos(-((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig)))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(pi/2);
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(asin(acos(-((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig)))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(-asin(3.1416/(2*bankmax)));
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(asin(acos(-((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig)))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(asin(3.1416/(2*bankmax)));
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(asin(acos(-((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig)))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(-pi/2);
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(-asin(acos((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(pi/2);
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(-asin(acos((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(-asin(3.1416/(2*bankmax)));
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(-asin(acos((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(asin(3.1416/(2*bankmax)));
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(-asin(acos((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(-pi/2);
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(asin(acos((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(pi/2);
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(asin(acos((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(-asin(3.1416/(2*bankmax)));
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(asin(acos((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(asin(3.1416/(2*bankmax)));
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(asin(acos((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(-pi/2);
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(-pi/2);
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(-pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(pi/2);
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(-pi/2);
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(-pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(-asin(3.1416/(2*bankmax)));
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(-pi/2);
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(-pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(asin(3.1416/(2*bankmax)));
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(-pi/2);
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(-pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(-pi/2);
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(pi/2);
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(-pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(pi/2);
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(pi/2);
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(-pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(-asin(3.1416/(2*bankmax)));
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(pi/2);
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(-pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(asin(3.1416/(2*bankmax)));
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(pi/2);
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(-pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(-pi/2);
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(-asin(acos(-((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig)))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(-pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(pi/2);
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(-asin(acos(-((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig)))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(-pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(-asin(3.1416/(2*bankmax)));
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(-asin(acos(-((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig)))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(-pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(asin(3.1416/(2*bankmax)));
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(-asin(acos(-((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig)))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(-pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(-pi/2);
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(asin(acos(-((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig)))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(-pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(pi/2);
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(asin(acos(-((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig)))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(-pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(-asin(3.1416/(2*bankmax)));
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(asin(acos(-((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig)))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(-pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(asin(3.1416/(2*bankmax)));
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(asin(acos(-((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig)))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(-pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(-pi/2);
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(-asin(acos((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(-pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(pi/2);
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(-asin(acos((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(-pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(-asin(3.1416/(2*bankmax)));
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(-asin(acos((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(-pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(asin(3.1416/(2*bankmax)));
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(-asin(acos((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(-pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(-pi/2);
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(asin(acos((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(-pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(pi/2);
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(asin(acos((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(-pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(-asin(3.1416/(2*bankmax)));
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(asin(acos((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(-pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(asin(3.1416/(2*bankmax)));
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(asin(acos((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(-pi/2);
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(-pi/2);
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(-pi/2);
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(asin(((((v*(z + 50)^2.5)*(-(1560*lamV*cos(alfamax*sin(alfatrig)))/mass-(1560*lamGAM*sin(alfamax*sin(alfatrig))*cos(bankmax*sin(banktrig)))/(mass*v)-(1560*lamPSII*sin(alfamax*sin(alfatrig))*sin(bankmax*sin(banktrig)))/(mass*v*cos(gam))))/(8112.0*cos(gam)))^(1/4.2)-1860)/1560));
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(pi/2);
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(-pi/2);
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(asin(((((v*(z + 50)^2.5)*(-(1560*lamV*cos(alfamax*sin(alfatrig)))/mass-(1560*lamGAM*sin(alfamax*sin(alfatrig))*cos(bankmax*sin(banktrig)))/(mass*v)-(1560*lamPSII*sin(alfamax*sin(alfatrig))*sin(bankmax*sin(banktrig)))/(mass*v*cos(gam))))/(8112.0*cos(gam)))^(1/4.2)-1860)/1560));
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(-asin(3.1416/(2*bankmax)));
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(-pi/2);
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(asin(((((v*(z + 50)^2.5)*(-(1560*lamV*cos(alfamax*sin(alfatrig)))/mass-(1560*lamGAM*sin(alfamax*sin(alfatrig))*cos(bankmax*sin(banktrig)))/(mass*v)-(1560*lamPSII*sin(alfamax*sin(alfatrig))*sin(bankmax*sin(banktrig)))/(mass*v*cos(gam))))/(8112.0*cos(gam)))^(1/4.2)-1860)/1560));
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(asin(3.1416/(2*bankmax)));
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(-pi/2);
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(asin(((((v*(z + 50)^2.5)*(-(1560*lamV*cos(alfamax*sin(alfatrig)))/mass-(1560*lamGAM*sin(alfamax*sin(alfatrig))*cos(bankmax*sin(banktrig)))/(mass*v)-(1560*lamPSII*sin(alfamax*sin(alfatrig))*sin(bankmax*sin(banktrig)))/(mass*v*cos(gam))))/(8112.0*cos(gam)))^(1/4.2)-1860)/1560));
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(-pi/2);
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(pi/2);
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(asin(((((v*(z + 50)^2.5)*(-(1560*lamV*cos(alfamax*sin(alfatrig)))/mass-(1560*lamGAM*sin(alfamax*sin(alfatrig))*cos(bankmax*sin(banktrig)))/(mass*v)-(1560*lamPSII*sin(alfamax*sin(alfatrig))*sin(bankmax*sin(banktrig)))/(mass*v*cos(gam))))/(8112.0*cos(gam)))^(1/4.2)-1860)/1560));
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(pi/2);
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(pi/2);
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(asin(((((v*(z + 50)^2.5)*(-(1560*lamV*cos(alfamax*sin(alfatrig)))/mass-(1560*lamGAM*sin(alfamax*sin(alfatrig))*cos(bankmax*sin(banktrig)))/(mass*v)-(1560*lamPSII*sin(alfamax*sin(alfatrig))*sin(bankmax*sin(banktrig)))/(mass*v*cos(gam))))/(8112.0*cos(gam)))^(1/4.2)-1860)/1560));
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(-asin(3.1416/(2*bankmax)));
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(pi/2);
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(asin(((((v*(z + 50)^2.5)*(-(1560*lamV*cos(alfamax*sin(alfatrig)))/mass-(1560*lamGAM*sin(alfamax*sin(alfatrig))*cos(bankmax*sin(banktrig)))/(mass*v)-(1560*lamPSII*sin(alfamax*sin(alfatrig))*sin(bankmax*sin(banktrig)))/(mass*v*cos(gam))))/(8112.0*cos(gam)))^(1/4.2)-1860)/1560));
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(asin(3.1416/(2*bankmax)));
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(pi/2);
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(asin(((((v*(z + 50)^2.5)*(-(1560*lamV*cos(alfamax*sin(alfatrig)))/mass-(1560*lamGAM*sin(alfamax*sin(alfatrig))*cos(bankmax*sin(banktrig)))/(mass*v)-(1560*lamPSII*sin(alfamax*sin(alfatrig))*sin(bankmax*sin(banktrig)))/(mass*v*cos(gam))))/(8112.0*cos(gam)))^(1/4.2)-1860)/1560));
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(-pi/2);
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(-asin(acos(-((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig)))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(asin(((((v*(z + 50)^2.5)*(-(1560*lamV*cos(alfamax*sin(alfatrig)))/mass-(1560*lamGAM*sin(alfamax*sin(alfatrig))*cos(bankmax*sin(banktrig)))/(mass*v)-(1560*lamPSII*sin(alfamax*sin(alfatrig))*sin(bankmax*sin(banktrig)))/(mass*v*cos(gam))))/(8112.0*cos(gam)))^(1/4.2)-1860)/1560));
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(pi/2);
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(-asin(acos(-((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig)))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(asin(((((v*(z + 50)^2.5)*(-(1560*lamV*cos(alfamax*sin(alfatrig)))/mass-(1560*lamGAM*sin(alfamax*sin(alfatrig))*cos(bankmax*sin(banktrig)))/(mass*v)-(1560*lamPSII*sin(alfamax*sin(alfatrig))*sin(bankmax*sin(banktrig)))/(mass*v*cos(gam))))/(8112.0*cos(gam)))^(1/4.2)-1860)/1560));
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(-asin(3.1416/(2*bankmax)));
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(-asin(acos(-((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig)))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(asin(((((v*(z + 50)^2.5)*(-(1560*lamV*cos(alfamax*sin(alfatrig)))/mass-(1560*lamGAM*sin(alfamax*sin(alfatrig))*cos(bankmax*sin(banktrig)))/(mass*v)-(1560*lamPSII*sin(alfamax*sin(alfatrig))*sin(bankmax*sin(banktrig)))/(mass*v*cos(gam))))/(8112.0*cos(gam)))^(1/4.2)-1860)/1560));
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(asin(3.1416/(2*bankmax)));
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(-asin(acos(-((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig)))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(asin(((((v*(z + 50)^2.5)*(-(1560*lamV*cos(alfamax*sin(alfatrig)))/mass-(1560*lamGAM*sin(alfamax*sin(alfatrig))*cos(bankmax*sin(banktrig)))/(mass*v)-(1560*lamPSII*sin(alfamax*sin(alfatrig))*sin(bankmax*sin(banktrig)))/(mass*v*cos(gam))))/(8112.0*cos(gam)))^(1/4.2)-1860)/1560));
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(-pi/2);
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(asin(acos(-((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig)))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(asin(((((v*(z + 50)^2.5)*(-(1560*lamV*cos(alfamax*sin(alfatrig)))/mass-(1560*lamGAM*sin(alfamax*sin(alfatrig))*cos(bankmax*sin(banktrig)))/(mass*v)-(1560*lamPSII*sin(alfamax*sin(alfatrig))*sin(bankmax*sin(banktrig)))/(mass*v*cos(gam))))/(8112.0*cos(gam)))^(1/4.2)-1860)/1560));
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(pi/2);
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(asin(acos(-((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig)))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(asin(((((v*(z + 50)^2.5)*(-(1560*lamV*cos(alfamax*sin(alfatrig)))/mass-(1560*lamGAM*sin(alfamax*sin(alfatrig))*cos(bankmax*sin(banktrig)))/(mass*v)-(1560*lamPSII*sin(alfamax*sin(alfatrig))*sin(bankmax*sin(banktrig)))/(mass*v*cos(gam))))/(8112.0*cos(gam)))^(1/4.2)-1860)/1560));
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(-asin(3.1416/(2*bankmax)));
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(asin(acos(-((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig)))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(asin(((((v*(z + 50)^2.5)*(-(1560*lamV*cos(alfamax*sin(alfatrig)))/mass-(1560*lamGAM*sin(alfamax*sin(alfatrig))*cos(bankmax*sin(banktrig)))/(mass*v)-(1560*lamPSII*sin(alfamax*sin(alfatrig))*sin(bankmax*sin(banktrig)))/(mass*v*cos(gam))))/(8112.0*cos(gam)))^(1/4.2)-1860)/1560));
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(asin(3.1416/(2*bankmax)));
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(asin(acos(-((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig)))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(asin(((((v*(z + 50)^2.5)*(-(1560*lamV*cos(alfamax*sin(alfatrig)))/mass-(1560*lamGAM*sin(alfamax*sin(alfatrig))*cos(bankmax*sin(banktrig)))/(mass*v)-(1560*lamPSII*sin(alfamax*sin(alfatrig))*sin(bankmax*sin(banktrig)))/(mass*v*cos(gam))))/(8112.0*cos(gam)))^(1/4.2)-1860)/1560));
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(-pi/2);
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(-asin(acos((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(asin(((((v*(z + 50)^2.5)*(-(1560*lamV*cos(alfamax*sin(alfatrig)))/mass-(1560*lamGAM*sin(alfamax*sin(alfatrig))*cos(bankmax*sin(banktrig)))/(mass*v)-(1560*lamPSII*sin(alfamax*sin(alfatrig))*sin(bankmax*sin(banktrig)))/(mass*v*cos(gam))))/(8112.0*cos(gam)))^(1/4.2)-1860)/1560));
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(pi/2);
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(-asin(acos((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(asin(((((v*(z + 50)^2.5)*(-(1560*lamV*cos(alfamax*sin(alfatrig)))/mass-(1560*lamGAM*sin(alfamax*sin(alfatrig))*cos(bankmax*sin(banktrig)))/(mass*v)-(1560*lamPSII*sin(alfamax*sin(alfatrig))*sin(bankmax*sin(banktrig)))/(mass*v*cos(gam))))/(8112.0*cos(gam)))^(1/4.2)-1860)/1560));
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(-asin(3.1416/(2*bankmax)));
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(-asin(acos((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(asin(((((v*(z + 50)^2.5)*(-(1560*lamV*cos(alfamax*sin(alfatrig)))/mass-(1560*lamGAM*sin(alfamax*sin(alfatrig))*cos(bankmax*sin(banktrig)))/(mass*v)-(1560*lamPSII*sin(alfamax*sin(alfatrig))*sin(bankmax*sin(banktrig)))/(mass*v*cos(gam))))/(8112.0*cos(gam)))^(1/4.2)-1860)/1560));
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(asin(3.1416/(2*bankmax)));
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(-asin(acos((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(asin(((((v*(z + 50)^2.5)*(-(1560*lamV*cos(alfamax*sin(alfatrig)))/mass-(1560*lamGAM*sin(alfamax*sin(alfatrig))*cos(bankmax*sin(banktrig)))/(mass*v)-(1560*lamPSII*sin(alfamax*sin(alfatrig))*sin(bankmax*sin(banktrig)))/(mass*v*cos(gam))))/(8112.0*cos(gam)))^(1/4.2)-1860)/1560));
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(-pi/2);
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(asin(acos((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(asin(((((v*(z + 50)^2.5)*(-(1560*lamV*cos(alfamax*sin(alfatrig)))/mass-(1560*lamGAM*sin(alfamax*sin(alfatrig))*cos(bankmax*sin(banktrig)))/(mass*v)-(1560*lamPSII*sin(alfamax*sin(alfatrig))*sin(bankmax*sin(banktrig)))/(mass*v*cos(gam))))/(8112.0*cos(gam)))^(1/4.2)-1860)/1560));
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(pi/2);
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(asin(acos((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(asin(((((v*(z + 50)^2.5)*(-(1560*lamV*cos(alfamax*sin(alfatrig)))/mass-(1560*lamGAM*sin(alfamax*sin(alfatrig))*cos(bankmax*sin(banktrig)))/(mass*v)-(1560*lamPSII*sin(alfamax*sin(alfatrig))*sin(bankmax*sin(banktrig)))/(mass*v*cos(gam))))/(8112.0*cos(gam)))^(1/4.2)-1860)/1560));
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(-asin(3.1416/(2*bankmax)));
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(asin(acos((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(asin(((((v*(z + 50)^2.5)*(-(1560*lamV*cos(alfamax*sin(alfatrig)))/mass-(1560*lamGAM*sin(alfamax*sin(alfatrig))*cos(bankmax*sin(banktrig)))/(mass*v)-(1560*lamPSII*sin(alfamax*sin(alfatrig))*sin(bankmax*sin(banktrig)))/(mass*v*cos(gam))))/(8112.0*cos(gam)))^(1/4.2)-1860)/1560));
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end
% Coefficients
banktrig = real(asin(3.1416/(2*bankmax)));
if isnan(real(banktrig)) || isinf(real(banktrig))
	banktrig = 0;
end
% Coefficients
alfatrig = real(asin(acos((lamV*v)/sqrt(lamV^2*v^2+lamGAM^2*cos(bankmax*sin(banktrig))^2+lamPSII^2*sec(gam)^2*sin(bankmax*sin(banktrig))^2+lamGAM*lamPSII*sec(gam)*sin(2*bankmax*sin(banktrig))))/alfamax));
if isnan(real(alfatrig)) || isinf(real(alfatrig))
	alfatrig = 0;
end
% Coefficients
Ttrignew = real(asin(((((v*(z + 50)^2.5)*(-(1560*lamV*cos(alfamax*sin(alfatrig)))/mass-(1560*lamGAM*sin(alfamax*sin(alfatrig))*cos(bankmax*sin(banktrig)))/(mass*v)-(1560*lamPSII*sin(alfamax*sin(alfatrig))*sin(bankmax*sin(banktrig)))/(mass*v*cos(gam))))/(8112.0*cos(gam)))^(1/4.2)-1860)/1560));
if isnan(real(Ttrignew)) || isinf(real(Ttrignew))
	Ttrignew = 0;
end
hamiltonian = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
if hamiltonian < hamiltonianSave
	banktrigSave = real(banktrig);
	alfatrigSave = real(alfatrig);
	TtrignewSave = real(Ttrignew);
	hamiltonianSave = hamiltonian;
end

return

