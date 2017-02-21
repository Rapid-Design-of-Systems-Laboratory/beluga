/*
 * computeControlUnconstrained.h
 *
 * Code generation for function 'computeControlUnconstrained'
 *
 * C source code generated on: Sat Jan 21 02:03:43 2017
 *
 */

#ifndef __COMPUTECONTROLUNCONSTRAINED_H__
#define __COMPUTECONTROLUNCONSTRAINED_H__
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
extern void computeControlUnconstrained(const real_T xAndLambda[12], real_T const_C1, real_T const_C2, real_T const_alfamax, real_T const_bankmax, real_T const_g, real_T const_mass, real_T *banktrigSave, real_T *alfatrigSave, real_T *TtrignewSave, real_T *hamiltonianSave);
extern creal_T eml_div(real_T x, const creal_T y);
#endif
/* End of code generation (computeControlUnconstrained.h) */
