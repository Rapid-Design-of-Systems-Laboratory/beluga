/*
 * computeControlUnconstrained.h
 *
 * Code generation for function 'computeControlUnconstrained'
 *
 * C source code generated on: Sat Jan 21 02:01:20 2017
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
#include "computeControlUnconstrained_types.h"

/* Function Declarations */
extern void computeControlUnconstrained(const real_T xAndLambda[12], const struct_T *b_const, real_T numArcs, real_T *banktrigSave, real_T *alfatrigSave, real_T *TtrignewSave, real_T *hamiltonianSave);
extern creal_T eml_div(real_T x, const creal_T y);
#endif
/* End of code generation (computeControlUnconstrained.h) */
