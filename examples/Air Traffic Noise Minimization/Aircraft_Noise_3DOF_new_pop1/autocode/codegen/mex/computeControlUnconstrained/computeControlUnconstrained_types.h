/*
 * computeControlUnconstrained_types.h
 *
 * Code generation for function 'computeControlUnconstrained'
 *
 * C source code generated on: Sat Jan 21 02:01:19 2017
 *
 */

#ifndef __COMPUTECONTROLUNCONSTRAINED_TYPES_H__
#define __COMPUTECONTROLUNCONSTRAINED_TYPES_H__

/* Include files */
#include "rtwtypes.h"

/* Type Definitions */
#ifndef typedef_ResolvedFunctionInfo
#define typedef_ResolvedFunctionInfo
typedef struct
{
    const char * context;
    const char * name;
    const char * dominantType;
    const char * resolved;
    uint32_T fileTimeLo;
    uint32_T fileTimeHi;
    uint32_T mFileTimeLo;
    uint32_T mFileTimeHi;
} ResolvedFunctionInfo;
#endif /*typedef_ResolvedFunctionInfo*/
#ifndef typedef_struct_T
#define typedef_struct_T
typedef struct
{
    real_T Aref;
    real_T C1;
    real_T C2;
    real_T H;
    real_T Tmax;
    real_T Tmin;
    real_T alfamax;
    real_T bankmax;
    real_T epsilon;
    real_T g;
    real_T mass;
    real_T mu;
    real_T re;
    real_T rho0;
} struct_T;
#endif /*typedef_struct_T*/

#endif
/* End of code generation (computeControlUnconstrained_types.h) */
