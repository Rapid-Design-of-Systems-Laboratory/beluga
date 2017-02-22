/*
 * derivFuncRegion_terminate.c
 *
 * Code generation for function 'derivFuncRegion_terminate'
 *
 * C source code generated on: Sat Jan 21 02:02:52 2017
 *
 */

/* Include files */
#include "rt_nonfinite.h"
#include "derivFuncRegion.h"
#include "derivFuncRegion_terminate.h"

/* Function Definitions */
void derivFuncRegion_atexit(void)
{
  emlrtCreateRootTLS(&emlrtRootTLSGlobal, &emlrtContextGlobal, NULL, 1);
  emlrtEnterRtStackR2012b(emlrtRootTLSGlobal);
  emlrtLeaveRtStackR2012b(emlrtRootTLSGlobal);
  emlrtDestroyRootTLS(&emlrtRootTLSGlobal);
}

void derivFuncRegion_terminate(void)
{
  emlrtLeaveRtStackR2012b(emlrtRootTLSGlobal);
  emlrtDestroyRootTLS(&emlrtRootTLSGlobal);
}

/* End of code generation (derivFuncRegion_terminate.c) */
