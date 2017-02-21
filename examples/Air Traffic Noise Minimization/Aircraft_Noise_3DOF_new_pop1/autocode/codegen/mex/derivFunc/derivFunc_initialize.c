/*
 * derivFunc_initialize.c
 *
 * Code generation for function 'derivFunc_initialize'
 *
 * C source code generated on: Sat Jan 21 02:02:06 2017
 *
 */

/* Include files */
#include "rt_nonfinite.h"
#include "derivFunc.h"
#include "derivFunc_initialize.h"

/* Variable Definitions */
static const volatile char_T *emlrtBreakCheckR2012bFlagVar;

/* Function Definitions */
void derivFunc_initialize(emlrtContext *aContext)
{
  emlrtBreakCheckR2012bFlagVar = emlrtGetBreakCheckFlagAddressR2012b();
  emlrtCreateRootTLS(&emlrtRootTLSGlobal, aContext, NULL, 1);
  emlrtClearAllocCountR2012b(emlrtRootTLSGlobal, FALSE, 0U, 0);
  emlrtEnterRtStackR2012b(emlrtRootTLSGlobal);
  emlrtFirstTimeR2012b(emlrtRootTLSGlobal);
}

/* End of code generation (derivFunc_initialize.c) */
