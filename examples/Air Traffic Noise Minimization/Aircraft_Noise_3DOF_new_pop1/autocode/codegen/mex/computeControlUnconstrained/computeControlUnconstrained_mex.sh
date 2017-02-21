MATLAB="/apps/rhel6/MATLAB/R2013a"
Arch=glnxa64
ENTRYPOINT=mexFunction
MAPFILE=$ENTRYPOINT'.map'
PREFDIR="/home/mall/.matlab/R2013a"
OPTSFILE_NAME="./mexopts.sh"
. $OPTSFILE_NAME
COMPILER=$CC
. $OPTSFILE_NAME
echo "# Make settings for computeControlUnconstrained" > computeControlUnconstrained_mex.mki
echo "CC=$CC" >> computeControlUnconstrained_mex.mki
echo "CFLAGS=$CFLAGS" >> computeControlUnconstrained_mex.mki
echo "CLIBS=$CLIBS" >> computeControlUnconstrained_mex.mki
echo "COPTIMFLAGS=$COPTIMFLAGS" >> computeControlUnconstrained_mex.mki
echo "CDEBUGFLAGS=$CDEBUGFLAGS" >> computeControlUnconstrained_mex.mki
echo "CXX=$CXX" >> computeControlUnconstrained_mex.mki
echo "CXXFLAGS=$CXXFLAGS" >> computeControlUnconstrained_mex.mki
echo "CXXLIBS=$CXXLIBS" >> computeControlUnconstrained_mex.mki
echo "CXXOPTIMFLAGS=$CXXOPTIMFLAGS" >> computeControlUnconstrained_mex.mki
echo "CXXDEBUGFLAGS=$CXXDEBUGFLAGS" >> computeControlUnconstrained_mex.mki
echo "LD=$LD" >> computeControlUnconstrained_mex.mki
echo "LDFLAGS=$LDFLAGS" >> computeControlUnconstrained_mex.mki
echo "LDOPTIMFLAGS=$LDOPTIMFLAGS" >> computeControlUnconstrained_mex.mki
echo "LDDEBUGFLAGS=$LDDEBUGFLAGS" >> computeControlUnconstrained_mex.mki
echo "Arch=$Arch" >> computeControlUnconstrained_mex.mki
echo OMPFLAGS= >> computeControlUnconstrained_mex.mki
echo OMPLINKFLAGS= >> computeControlUnconstrained_mex.mki
echo "EMC_COMPILER=" >> computeControlUnconstrained_mex.mki
echo "EMC_CONFIG=optim" >> computeControlUnconstrained_mex.mki
"/apps/rhel6/MATLAB/R2013a/bin/glnxa64/gmake" -B -f computeControlUnconstrained_mex.mk
