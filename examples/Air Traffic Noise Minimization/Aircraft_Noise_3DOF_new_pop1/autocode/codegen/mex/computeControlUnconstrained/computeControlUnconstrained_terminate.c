/*
 * computeControlUnconstrained_terminate.c
 *
 * Code generation for function 'computeControlUnconstrained_terminate'
 *
 * C source code generated on: Sat Jan 21 02:01:19 2017
 *
 */

/* Include files */
#include "rt_nonfinite.h"
#include "computeControlUnconstrained.h"
#include "computeControlUnconstrained_terminate.h"

/* Function Definitions */
void computeControlUnconstrained_atexit(void)
{
  emlrtCreateRootTLS(&emlrtRootTLSGlobal, &emlrtContextGlobal, NULL, 1);
  emlrtEnterRtStackR2012b(emlrtRootTLSGlobal);
  emlrtLeaveRtStackR2012b(emlrtRootTLSGlobal);
  emlrtDestroyRootTLS(&emlrtRootTLSGlobal);
}

void computeControlUnconstrained_terminate(void)
{
  emlrtLeaveRtStackR2012b(emlrtRootTLSGlobal);
  emlrtDestroyRootTLS(&emlrtRootTLSGlobal);
}

/* End of code generation (computeControlUnconstrained_terminate.c) */
