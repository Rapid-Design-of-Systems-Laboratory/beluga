/*
 * derivFunc.h
 *
 * Code generation for function 'derivFunc'
 *
 * C source code generated on: Sat Jan 21 02:02:06 2017
 *
 */

#ifndef __DERIVFUNC_H__
#define __DERIVFUNC_H__
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
#include "derivFunc_types.h"

/* Function Declarations */
extern void derivFunc(real_T t, const real_T X[12], const real_T p_data[19], const int32_T p_size[1], const struct_T *b_const, real_T arcSequence, const real_T x0[6], const real_T xf[6], real_T xDotOut[12]);
extern void eml_error(void);
#endif
/* End of code generation (derivFunc.h) */
