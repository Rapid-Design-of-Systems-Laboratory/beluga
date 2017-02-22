/*
 * derivFunc_terminate.c
 *
 * Code generation for function 'derivFunc_terminate'
 *
 * C source code generated on: Sat Jan 21 02:02:06 2017
 *
 */

/* Include files */
#include "rt_nonfinite.h"
#include "derivFunc.h"
#include "derivFunc_terminate.h"

/* Function Definitions */
void derivFunc_atexit(void)
{
  emlrtCreateRootTLS(&emlrtRootTLSGlobal, &emlrtContextGlobal, NULL, 1);
  emlrtEnterRtStackR2012b(emlrtRootTLSGlobal);
  emlrtLeaveRtStackR2012b(emlrtRootTLSGlobal);
  emlrtDestroyRootTLS(&emlrtRootTLSGlobal);
}

void derivFunc_terminate(void)
{
  emlrtLeaveRtStackR2012b(emlrtRootTLSGlobal);
  emlrtDestroyRootTLS(&emlrtRootTLSGlobal);
}

/* End of code generation (derivFunc_terminate.c) */
