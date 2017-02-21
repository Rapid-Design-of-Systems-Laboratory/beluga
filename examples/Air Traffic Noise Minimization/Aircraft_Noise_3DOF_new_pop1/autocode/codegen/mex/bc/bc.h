/*
 * bc.h
 *
 * Code generation for function 'bc'
 *
 * C source code generated on: Sat Jan 21 02:03:42 2017
 *
 */

#ifndef __BC_H__
#define __BC_H__
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
#include "bc_types.h"

/* Function Declarations */
extern void bc(const real_T YL_data[12], const int32_T YL_size[1], const real_T YR_data[12], const int32_T YR_size[1], const real_T p_data[19], const int32_T p_size[1], const struct_T *b_const, real_T arcSequence, const real_T x0[6], const real_T xf[6], real_T zeroVec[25]);
extern void eml_error(void);
#endif
/* End of code generation (bc.h) */
