MATLAB="/apps/rhel6/MATLAB/R2013a"
Arch=glnxa64
ENTRYPOINT=mexFunction
MAPFILE=$ENTRYPOINT'.map'
PREFDIR="/home/mall/.matlab/R2013a"
OPTSFILE_NAME="./mexopts.sh"
. $OPTSFILE_NAME
COMPILER=$CC
. $OPTSFILE_NAME
echo "# Make settings for derivFunc" > derivFunc_mex.mki
echo "CC=$CC" >> derivFunc_mex.mki
echo "CFLAGS=$CFLAGS" >> derivFunc_mex.mki
echo "CLIBS=$CLIBS" >> derivFunc_mex.mki
echo "COPTIMFLAGS=$COPTIMFLAGS" >> derivFunc_mex.mki
echo "CDEBUGFLAGS=$CDEBUGFLAGS" >> derivFunc_mex.mki
echo "CXX=$CXX" >> derivFunc_mex.mki
echo "CXXFLAGS=$CXXFLAGS" >> derivFunc_mex.mki
echo "CXXLIBS=$CXXLIBS" >> derivFunc_mex.mki
echo "CXXOPTIMFLAGS=$CXXOPTIMFLAGS" >> derivFunc_mex.mki
echo "CXXDEBUGFLAGS=$CXXDEBUGFLAGS" >> derivFunc_mex.mki
echo "LD=$LD" >> derivFunc_mex.mki
echo "LDFLAGS=$LDFLAGS" >> derivFunc_mex.mki
echo "LDOPTIMFLAGS=$LDOPTIMFLAGS" >> derivFunc_mex.mki
echo "LDDEBUGFLAGS=$LDDEBUGFLAGS" >> derivFunc_mex.mki
echo "Arch=$Arch" >> derivFunc_mex.mki
echo OMPFLAGS= >> derivFunc_mex.mki
echo OMPLINKFLAGS= >> derivFunc_mex.mki
echo "EMC_COMPILER=" >> derivFunc_mex.mki
echo "EMC_CONFIG=optim" >> derivFunc_mex.mki
"/apps/rhel6/MATLAB/R2013a/bin/glnxa64/gmake" -B -f derivFunc_mex.mk
