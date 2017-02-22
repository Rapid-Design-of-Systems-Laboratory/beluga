function [xDotOut] = derivFunc(t,X,region,p,const,constraint,arcSequence,interiorPointConstraintSequence,interiorPointNumLagrangeMultipliers,x0,xf) %#ok<INUSD,INUSL>
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
assert(isa(t, 'double'));
assert(all(size(t)== [1 1]));
assert(isa(X, 'double'));
assert(isa(p, 'double'));
assert(isa(arcSequence, 'double'));
assert(all(size(X)== [12 1]));
coder.varsize('arcSequence', [1 1]);
coder.varsize('p', [19 1]);
assert(isa(interiorPointConstraintSequence, 'double'));
assert(isa(interiorPointNumLagrangeMultipliers, 'double'));
assert(all(size(interiorPointConstraintSequence) == [0 0]));
assert(all(size(interiorPointNumLagrangeMultipliers) == [0 0]));
assert(isa(x0, 'double'));
assert(all(size(x0)== [6 1]));
assert(isa(xf, 'double'));
assert(all(size(xf)== [6 1]));
xDot = nan(12,1);
assert(isa(region, 'double'));
assert(all(size(region)== [1 1]));
	xDot = zeros(size(X));
coder.varsize('xAndLambda',[13,1],[1,0]);

%%%%%%%%%%%%%%%%
%% Parameters %%
%%%%%%%%%%%%%%%%

numArcs = length(arcSequence);

% States
x = X(1);
y = X(2);
z = X(3);
v = X(4);
psii = X(5);
gam = X(6);

% Costates
lamX = X(7);
lamY = X(8);
lamZ = X(9);
lamV = X(10);
lamPSII = X(11);
lamGAM = X(12);

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



tSet = p(1:numArcs);
indexArc = arcSequence(region);
banktrig = NaN;
alfatrig = NaN;
Ttrignew = NaN;
switch indexArc
	case {0} % unconstrained arc
		xAndLambda = [x;y;z;v;psii;gam;lamX;lamY;lamZ;lamV;lamPSII;lamGAM];
		if(~isa(X,'sym'))
			[banktrig,alfatrig,Ttrignew,hamiltonian] = computeControlUnconstrained(xAndLambda,const,constraint,length(arcSequence));
		else
			[banktrig,alfatrig,Ttrignew,hamiltonian] = deal(sym('banktrig'),sym('alfatrig'),sym('Ttrignew'),sym('hamiltonian'));
		end

		xDot(7:12,1) = real([0; ...
				0; ...
				(2.5*cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^3.5); ...
				(lamV*(2*C1*v - (2*C2)/v^3))/mass - lamZ*sin(gam) - lamX*cos(gam)*cos(psii) - lamY*cos(gam)*sin(psii) - lamGAM*((g*cos(gam))/v^2 - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v^2)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v^2*(z + 50)^2.5) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v^2*cos(gam)); ...
				lamX*v*cos(gam)*sin(psii) - lamY*v*cos(gam)*cos(psii); ...
				g*lamV*cos(gam) - lamZ*v*cos(gam) + lamY*v*sin(gam)*sin(psii) + (sin(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) - (g*lamGAM*sin(gam))/v + lamX*v*cos(psii)*sin(gam) - (lamPSII*sin(bankmax*sin(banktrig))*sin(gam)*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)^2)]);

end
% Equations of motion
xDot(1:6,1) = real([v*cos(gam)*cos(psii); ...
				v*cos(gam)*sin(psii); ...
				v*sin(gam); ...
				- (C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass - g*sin(gam); ...
				(sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)); ...
				(cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v) - (g*cos(gam))/v]);

% Account for variable endpoints in derivative
xDotOut = xDot*tSet(region);

return

