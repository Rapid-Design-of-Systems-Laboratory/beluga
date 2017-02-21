/*
 * mpower.h
 *
 * Code generation for function 'mpower'
 *
 * C source code generated on: Sat Jan 21 02:02:08 2017
 *
 */

#ifndef __MPOWER_H__
#define __MPOWER_H__
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
extern creal_T b_mpower(const creal_T a);
extern creal_T c_mpower(const creal_T a);
extern real_T mpower(real_T a);
#ifdef __WATCOMC__
#pragma aux mpower value [8087];
#endif
#endif
/* End of code generation (mpower.h) */
