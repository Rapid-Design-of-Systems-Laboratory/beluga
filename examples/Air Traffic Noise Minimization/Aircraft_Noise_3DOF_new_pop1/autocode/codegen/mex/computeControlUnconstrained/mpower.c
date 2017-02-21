/*
 * mpower.c
 *
 * Code generation for function 'mpower'
 *
 * C source code generated on: Sat Jan 21 02:01:21 2017
 *
 */

/* Include files */
#include "rt_nonfinite.h"
#include "computeControlUnconstrained.h"
#include "mpower.h"
#include "log.h"
#include "computeControlUnconstrained_data.h"

/* Variable Definitions */
static emlrtRSInfo kc_emlrtRSI = { 37, "mpower",
  "/apps/rhel6/MATLAB/R2013a/toolbox/eml/lib/matlab/ops/mpower.m" };

static emlrtRSInfo lc_emlrtRSI = { 42, "power",
  "/apps/rhel6/MATLAB/R2013a/toolbox/eml/lib/matlab/ops/power.m" };

static emlrtRSInfo mc_emlrtRSI = { 56, "power",
  "/apps/rhel6/MATLAB/R2013a/toolbox/eml/lib/matlab/ops/power.m" };

/* Function Declarations */
static void eml_error(void);

/* Function Definitions */
static void eml_error(void)
{
  emlrtPushRtStackR2012b(&nc_emlrtRSI, emlrtRootTLSGlobal);
  emlrtErrorWithMessageIdR2012b(emlrtRootTLSGlobal, &emlrtRTEI,
    "Coder:toolbox:power_domainError", 0);
  emlrtPopRtStackR2012b(&nc_emlrtRSI, emlrtRootTLSGlobal);
}

creal_T b_mpower(const creal_T a)
{
  creal_T c;
  creal_T t;
  real_T tr;
  if ((a.im == 0.0) && (a.re >= 0.0)) {
    c.re = muDoubleScalarPower(a.re, 2.5);
    c.im = 0.0;
  } else {
    t = a;
    b_log(&t);
    t.re *= 2.5;
    t.im *= 2.5;
    tr = muDoubleScalarExp(t.re);
    c.re = tr * muDoubleScalarCos(t.im);
    c.im = tr * muDoubleScalarSin(t.im);
  }

  return c;
}

creal_T c_mpower(const creal_T a)
{
  creal_T c;
  creal_T t;
  real_T tr;
  if ((a.im == 0.0) && (a.re >= 0.0)) {
    c.re = muDoubleScalarPower(a.re, 0.23809523809523808);
    c.im = 0.0;
  } else {
    t = a;
    b_log(&t);
    t.re *= 0.23809523809523808;
    t.im *= 0.23809523809523808;
    tr = muDoubleScalarExp(t.re);
    c.re = tr * muDoubleScalarCos(t.im);
    c.im = tr * muDoubleScalarSin(t.im);
  }

  return c;
}

real_T mpower(real_T a)
{
  real_T c;
  emlrtPushRtStackR2012b(&kc_emlrtRSI, emlrtRootTLSGlobal);
  emlrtPushRtStackR2012b(&lc_emlrtRSI, emlrtRootTLSGlobal);
  if (a < 0.0) {
    emlrtPushRtStackR2012b(&mc_emlrtRSI, emlrtRootTLSGlobal);
    eml_error();
    emlrtPopRtStackR2012b(&mc_emlrtRSI, emlrtRootTLSGlobal);
  }

  c = muDoubleScalarPower(a, 5.2);
  emlrtPopRtStackR2012b(&lc_emlrtRSI, emlrtRootTLSGlobal);
  emlrtPopRtStackR2012b(&kc_emlrtRSI, emlrtRootTLSGlobal);
  return c;
}

/* End of code generation (mpower.c) */
