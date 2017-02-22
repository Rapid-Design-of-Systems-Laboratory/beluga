function [zeroVec] = bc(YL,YR,p,const,constraint,arcSequence,interiorPointConstraintSequence,interiorPointNumLagrangeMultipliers,x0,xf)
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
coder.varsize('YL', [12 1]);
coder.varsize('YR', [12 1]);
assert(isa(YL,'double'));
assert(isa(YR,'double'));
assert(isa(p,'double'));
coder.varsize('p', [19 1]);
assert(isa(x0,'double'));
assert(all(size(x0)== [6 1]));
assert(isa(xf,'double'));
assert(all(size(xf)== [6 1]));
assert(isa(arcSequence, 'double'));
coder.varsize('arcSequence', [1 1]);
assert(isa(interiorPointConstraintSequence, 'double'));
assert(all(size(interiorPointConstraintSequence) == [0 0]));
assert(isa(interiorPointNumLagrangeMultipliers, 'double'));
assert(all(size(interiorPointNumLagrangeMultipliers) == [0 0]));
coder.varsize('constraintDeriv', [6 1]);
coder.varsize('constraintDeriv1', [6 1]);
coder.varsize('H_t_plus', [1 1]);
coder.varsize('H_t_minus', [1 1]);
coder.varsize('Harcs', [1 1]);
coder.varsize('continuityStates', [6 1]);
coder.varsize('costateArcs', [6 1]);
coder.varsize('dNdt', [6,1]);
coder.varsize('dNdx', [6,6]);
coder.varsize('hamiltonianDiscontinuity', [6,1]);
coder.varsize('costateDiscontinuity', [6,6]);

numArcs = length(arcSequence);
interiorPointConstraintIndex = 0;
lmInteriorPointIndex = 1;
interiorPointConstraintIndex1 = 0;
lmInteriorPointIndex1 = 1;
indexConstraintDeriv = 0;
indexConstraintDeriv1 = 0;
indexContinuityStates = 1;
indexCostateArcs = 1;
indexHarcs = 0;
H_t_plus = NaN(numArcs,1);
H_t_minus = NaN(numArcs,1);
Harcs = NaN(1,1);
x = NaN;
y = NaN;
z = NaN;
v = NaN;
psii = NaN;
gam = NaN;
lamX = NaN;
lamY = NaN;
lamZ = NaN;
lamV = NaN;
lamPSII = NaN;
lamGAM = NaN;
banktrig = NaN;
alfatrig = NaN;
Ttrignew = NaN;
xAndLambda0Constraint = NaN(12,1);
xAndLambdaFConstraint = NaN(12,1);
xAndLambda = NaN(12,1);
pii = NaN;
pii1 = NaN;
%%%%%%%%%%%%%%%%
%% Parameters %%
%%%%%%%%%%%%%%%%

tSet = p(1:numArcs);

lmInitial1 = p(numArcs+1);
lmInitial2 = p(numArcs+2);
lmInitial3 = p(numArcs+3);
lmInitial4 = p(numArcs+4);
lmInitial5 = p(numArcs+5);
lmInitial6 = p(numArcs+6);

lmTerminal1 = p(numArcs+6+1);
lmTerminal2 = p(numArcs+6+2);
lmTerminal3 = p(numArcs+6+3);
lmTerminal4 = p(numArcs+6+4);
lmTerminal5 = p(numArcs+6+5);
lmTerminal6 = p(numArcs+6+6);

lmInteriorPoint = p(numArcs+6+6+1:end);
lmInteriorPoint1 = 0;

dNdt = NaN(length(lmInteriorPoint),1);
dNdx = NaN(6,length(lmInteriorPoint));
constraintDeriv = NaN(length(lmInteriorPoint),1);
constraintDeriv1 = NaN(length(lmInteriorPoint1),1);
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



for ctrArc = 1 : 1 : numArcs
	indexArc = arcSequence(ctrArc);
	hamiltonianDiscontinuity = zeros(1,1);
	costateDiscontinuity = zeros(6,1);
	hamiltonianDiscontinuity1 = zeros(1,1);
	costateDiscontinuity1 = zeros(6,1);
	for ctrEndpoint = 1 : 1 : 2
		if ctrEndpoint == 1
			% Left endpoint
			% States
			x = YL(1,ctrArc);
			y = YL(2,ctrArc);
			z = YL(3,ctrArc);
			v = YL(4,ctrArc);
			psii = YL(5,ctrArc);
			gam = YL(6,ctrArc);

			% Costates
			lamX = YL(7,ctrArc);
			lamY = YL(8,ctrArc);
			lamZ = YL(9,ctrArc);
			lamV = YL(10,ctrArc);
			lamPSII = YL(11,ctrArc);
			lamGAM = YL(12,ctrArc);

			xAndLambda = [x;y;z;v;psii;gam;lamX;lamY;lamZ;lamV;lamPSII;lamGAM];
			if ctrArc == 1
				xAndLambda0Constraint = [
					lamX - (lmInitial1);
					lamY - (lmInitial2);
					lamZ - (lmInitial3);
					lamV - (lmInitial4);
					lamPSII - (lmInitial5);
					lamGAM - (lmInitial6);
					x - x0(1);
					y - x0(2);
					z - x0(3);
					v - x0(4);
					psii - x0(5);
					gam - x0(6);
				];
			end
		elseif ctrEndpoint == 2
			% Right endpoint
			% States
			x = YR(1,ctrArc);
			y = YR(2,ctrArc);
			z = YR(3,ctrArc);
			v = YR(4,ctrArc);
			psii = YR(5,ctrArc);
			gam = YR(6,ctrArc);

			% Costates
			lamX = YR(7,ctrArc);
			lamY = YR(8,ctrArc);
			lamZ = YR(9,ctrArc);
			lamV = YR(10,ctrArc);
			lamPSII = YR(11,ctrArc);
			lamGAM = YR(12,ctrArc);

			xAndLambda = [x;y;z;v;psii;gam;lamX;lamY;lamZ;lamV;lamPSII;lamGAM];
			if ctrArc == numArcs
				xAndLambdaFConstraint = [
					lamX - (lmTerminal1);
					lamY - (lmTerminal2);
					lamZ - (lmTerminal3);
					lamV - (lmTerminal4);
					lamPSII - (lmTerminal5);
					lamGAM - (lmTerminal6);
					x - xf(1);
					y - xf(2);
					z - xf(3);
					v - xf(4);
					psii - xf(5);
					gam - xf(6);
				];
			end
		end

		switch indexArc
		case {0} % unconstrained arc
			if(~isa(YL,'sym'))
				[banktrig,alfatrig,Ttrignew,d2Hdu2] = computeControlUnconstrained(xAndLambda,const,constraint,numArcs);
			else
				[banktrig,alfatrig,Ttrignew,d2Hdu2] = deal(sym('banktrig'),sym('alfatrig'),sym('Ttrignew'),0);
			end

		end
		if ctrEndpoint == 1
			H_t_plus(ctrArc) = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
		elseif ctrEndpoint == 2
			H_t_minus(ctrArc) = real(lamZ*v*sin(gam) - lamV*((C1*v^2 + C2/v^2 - cos(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860))/mass + g*sin(gam)) - lamGAM*((g*cos(gam))/v - (cos(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v)) + (cos(gam)*(1560*sin(Ttrignew) + 1860)^5.2)/(v*(z + 50)^2.5) + lamX*v*cos(gam)*cos(psii) + lamY*v*cos(gam)*sin(psii) + (lamPSII*sin(bankmax*sin(banktrig))*(g*mass + sin(alfamax*sin(alfatrig))*(1560*sin(Ttrignew) + 1860)))/(mass*v*cos(gam)));
		end
		if ctrArc > 1 && ctrEndpoint == 1
			for ctrInteriorPoint = 1 : 1 : 0
				switch interiorPointConstraintSequence(ctrInteriorPoint,ctrArc)
				case {0}
					dNdx = zeros(6,1);
					dNdt = 0;
					pii = 0;
				end
				hamiltonianDiscontinuity = hamiltonianDiscontinuity + pii'*dNdt;
				costateDiscontinuity = costateDiscontinuity + dNdx*pii;
			end
			continuityStates(indexContinuityStates:indexContinuityStates+6-1,1) = YR(1:6,ctrArc-1) - YL(1:6,ctrArc);
			indexContinuityStates = indexContinuityStates + 6;
			indexHarcs = indexHarcs + 1;
			Harcs(indexHarcs) = H_t_minus(ctrArc-1) - H_t_plus(ctrArc) - hamiltonianDiscontinuity;
			costateArcs(indexCostateArcs:indexCostateArcs+6-1,1) = YR(7:12,ctrArc-1) - YL(7:12,ctrArc) - costateDiscontinuity;
			indexCostateArcs = indexCostateArcs + 6;
		end
	end
end

if numArcs < 2
	zeroVec = real([xAndLambda0Constraint;
		xAndLambdaFConstraint;
		H_t_minus(end);
	]);
else
	zeroVec = real([xAndLambda0Constraint;
		xAndLambdaFConstraint;
		H_t_minus(end);
		Harcs;
	]);
end

return

