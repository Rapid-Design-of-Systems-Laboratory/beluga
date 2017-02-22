/*
 * bc_initialize.c
 *
 * Code generation for function 'bc_initialize'
 *
 * C source code generated on: Sat Jan 21 02:03:41 2017
 *
 */

/* Include files */
#include "rt_nonfinite.h"
#include "bc.h"
#include "bc_initialize.h"
#include "bc_data.h"

/* Function Definitions */
void bc_initialize(emlrtContext *aContext)
{
  emlrtBreakCheckR2012bFlagVar = emlrtGetBreakCheckFlagAddressR2012b();
  emlrtCreateRootTLS(&emlrtRootTLSGlobal, aContext, NULL, 1);
  emlrtClearAllocCountR2012b(emlrtRootTLSGlobal, FALSE, 0U, 0);
  emlrtEnterRtStackR2012b(emlrtRootTLSGlobal);
  emlrtFirstTimeR2012b(emlrtRootTLSGlobal);
}

/* End of code generation (bc_initialize.c) */
