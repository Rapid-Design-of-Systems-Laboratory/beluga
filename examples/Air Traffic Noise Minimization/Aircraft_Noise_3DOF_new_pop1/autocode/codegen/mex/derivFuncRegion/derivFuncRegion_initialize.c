/*
 * derivFuncRegion_initialize.c
 *
 * Code generation for function 'derivFuncRegion_initialize'
 *
 * C source code generated on: Sat Jan 21 02:02:52 2017
 *
 */

/* Include files */
#include "rt_nonfinite.h"
#include "derivFuncRegion.h"
#include "derivFuncRegion_initialize.h"

/* Variable Definitions */
static const volatile char_T *emlrtBreakCheckR2012bFlagVar;

/* Function Definitions */
void derivFuncRegion_initialize(emlrtContext *aContext)
{
  emlrtBreakCheckR2012bFlagVar = emlrtGetBreakCheckFlagAddressR2012b();
  emlrtCreateRootTLS(&emlrtRootTLSGlobal, aContext, NULL, 1);
  emlrtClearAllocCountR2012b(emlrtRootTLSGlobal, FALSE, 0U, 0);
  emlrtEnterRtStackR2012b(emlrtRootTLSGlobal);
  emlrtFirstTimeR2012b(emlrtRootTLSGlobal);
}

/* End of code generation (derivFuncRegion_initialize.c) */
