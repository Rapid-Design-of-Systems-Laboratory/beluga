/*
 * bc_terminate.c
 *
 * Code generation for function 'bc_terminate'
 *
 * C source code generated on: Sat Jan 21 02:03:41 2017
 *
 */

/* Include files */
#include "rt_nonfinite.h"
#include "bc.h"
#include "bc_terminate.h"

/* Function Definitions */
void bc_atexit(void)
{
  emlrtCreateRootTLS(&emlrtRootTLSGlobal, &emlrtContextGlobal, NULL, 1);
  emlrtEnterRtStackR2012b(emlrtRootTLSGlobal);
  emlrtLeaveRtStackR2012b(emlrtRootTLSGlobal);
  emlrtDestroyRootTLS(&emlrtRootTLSGlobal);
}

void bc_terminate(void)
{
  emlrtLeaveRtStackR2012b(emlrtRootTLSGlobal);
  emlrtDestroyRootTLS(&emlrtRootTLSGlobal);
}

/* End of code generation (bc_terminate.c) */
