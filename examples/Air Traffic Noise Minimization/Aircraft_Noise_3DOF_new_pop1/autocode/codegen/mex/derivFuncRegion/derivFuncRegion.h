/*
 * derivFuncRegion.h
 *
 * Code generation for function 'derivFuncRegion'
 *
 * C source code generated on: Sat Jan 21 02:02:53 2017
 *
 */

#ifndef __DERIVFUNCREGION_H__
#define __DERIVFUNCREGION_H__
/* Include files */
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include "mwmathutil.h"

#include "tmwtypes.h"
#include "mex.h"
#include "emlrt.h"
#include "blas.h"
#include "rtwtypes.h"
#include "derivFuncRegion_types.h"

/* Function Declarations */
extern void derivFuncRegion(real_T t, const real_T X[12], real_T region, const real_T p_data[19], const int32_T p_size[1], const struct_T *b_const, real_T arcSequence, const real_T x0[6], const real_T xf[6], real_T xDotOut[12]);
extern void eml_error(void);
#endif
/* End of code generation (derivFuncRegion.h) */
