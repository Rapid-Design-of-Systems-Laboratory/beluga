MATLAB="/apps/rhel6/MATLAB/R2013a"
Arch=glnxa64
ENTRYPOINT=mexFunction
MAPFILE=$ENTRYPOINT'.map'
PREFDIR="/home/mall/.matlab/R2013a"
OPTSFILE_NAME="./mexopts.sh"
. $OPTSFILE_NAME
COMPILER=$CC
. $OPTSFILE_NAME
echo "# Make settings for derivFuncRegion" > derivFuncRegion_mex.mki
echo "CC=$CC" >> derivFuncRegion_mex.mki
echo "CFLAGS=$CFLAGS" >> derivFuncRegion_mex.mki
echo "CLIBS=$CLIBS" >> derivFuncRegion_mex.mki
echo "COPTIMFLAGS=$COPTIMFLAGS" >> derivFuncRegion_mex.mki
echo "CDEBUGFLAGS=$CDEBUGFLAGS" >> derivFuncRegion_mex.mki
echo "CXX=$CXX" >> derivFuncRegion_mex.mki
echo "CXXFLAGS=$CXXFLAGS" >> derivFuncRegion_mex.mki
echo "CXXLIBS=$CXXLIBS" >> derivFuncRegion_mex.mki
echo "CXXOPTIMFLAGS=$CXXOPTIMFLAGS" >> derivFuncRegion_mex.mki
echo "CXXDEBUGFLAGS=$CXXDEBUGFLAGS" >> derivFuncRegion_mex.mki
echo "LD=$LD" >> derivFuncRegion_mex.mki
echo "LDFLAGS=$LDFLAGS" >> derivFuncRegion_mex.mki
echo "LDOPTIMFLAGS=$LDOPTIMFLAGS" >> derivFuncRegion_mex.mki
echo "LDDEBUGFLAGS=$LDDEBUGFLAGS" >> derivFuncRegion_mex.mki
echo "Arch=$Arch" >> derivFuncRegion_mex.mki
echo OMPFLAGS= >> derivFuncRegion_mex.mki
echo OMPLINKFLAGS= >> derivFuncRegion_mex.mki
echo "EMC_COMPILER=" >> derivFuncRegion_mex.mki
echo "EMC_CONFIG=optim" >> derivFuncRegion_mex.mki
"/apps/rhel6/MATLAB/R2013a/bin/glnxa64/gmake" -B -f derivFuncRegion_mex.mk
