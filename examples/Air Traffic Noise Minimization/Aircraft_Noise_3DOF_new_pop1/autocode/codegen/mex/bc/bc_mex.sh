MATLAB="/apps/rhel6/MATLAB/R2013a"
Arch=glnxa64
ENTRYPOINT=mexFunction
MAPFILE=$ENTRYPOINT'.map'
PREFDIR="/home/mall/.matlab/R2013a"
OPTSFILE_NAME="./mexopts.sh"
. $OPTSFILE_NAME
COMPILER=$CC
. $OPTSFILE_NAME
echo "# Make settings for bc" > bc_mex.mki
echo "CC=$CC" >> bc_mex.mki
echo "CFLAGS=$CFLAGS" >> bc_mex.mki
echo "CLIBS=$CLIBS" >> bc_mex.mki
echo "COPTIMFLAGS=$COPTIMFLAGS" >> bc_mex.mki
echo "CDEBUGFLAGS=$CDEBUGFLAGS" >> bc_mex.mki
echo "CXX=$CXX" >> bc_mex.mki
echo "CXXFLAGS=$CXXFLAGS" >> bc_mex.mki
echo "CXXLIBS=$CXXLIBS" >> bc_mex.mki
echo "CXXOPTIMFLAGS=$CXXOPTIMFLAGS" >> bc_mex.mki
echo "CXXDEBUGFLAGS=$CXXDEBUGFLAGS" >> bc_mex.mki
echo "LD=$LD" >> bc_mex.mki
echo "LDFLAGS=$LDFLAGS" >> bc_mex.mki
echo "LDOPTIMFLAGS=$LDOPTIMFLAGS" >> bc_mex.mki
echo "LDDEBUGFLAGS=$LDDEBUGFLAGS" >> bc_mex.mki
echo "Arch=$Arch" >> bc_mex.mki
echo OMPFLAGS= >> bc_mex.mki
echo OMPLINKFLAGS= >> bc_mex.mki
echo "EMC_COMPILER=" >> bc_mex.mki
echo "EMC_CONFIG=optim" >> bc_mex.mki
"/apps/rhel6/MATLAB/R2013a/bin/glnxa64/gmake" -B -f bc_mex.mk
