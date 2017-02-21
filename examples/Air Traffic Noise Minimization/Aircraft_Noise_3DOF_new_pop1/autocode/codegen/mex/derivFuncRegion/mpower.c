/*
 * mpower.c
 *
 * Code generation for function 'mpower'
 *
 * C source code generated on: Sat Jan 21 02:02:55 2017
 *
 */

/* Include files */
#include "rt_nonfinite.h"
#include "derivFuncRegion.h"
#include "mpower.h"
#include "derivFuncRegion_data.h"

/* Function Definitions */
creal_T b_mpower(const creal_T a)
{
  creal_T c;
  real_T t_re;
  real_T t_im;
  if ((a.im == 0.0) && (a.re >= 0.0)) {
    c.re = muDoubleScalarPower(a.re, 2.5);
    c.im = 0.0;
  } else {
    t_re = a.re;
    t_im = a.im;
    if ((a.im == 0.0) && muDoubleScalarIsNaN(a.re)) {
    } else if ((muDoubleScalarAbs(a.re) > 8.9884656743115785E+307) ||
               (muDoubleScalarAbs(a.im) > 8.9884656743115785E+307)) {
      t_re = muDoubleScalarLog(muDoubleScalarHypot(a.re / 2.0, a.im / 2.0)) +
        0.69314718055994529;
      t_im = muDoubleScalarAtan2(a.im, a.re);
    } else {
      t_re = muDoubleScalarLog(muDoubleScalarHypot(a.re, a.im));
      t_im = muDoubleScalarAtan2(a.im, a.re);
    }

    t_re *= 2.5;
    t_im *= 2.5;
    t_re = muDoubleScalarExp(t_re);
    c.re = t_re * muDoubleScalarCos(t_im);
    c.im = t_re * muDoubleScalarSin(t_im);
  }

  return c;
}

creal_T c_mpower(const creal_T a)
{
  creal_T c;
  real_T t_re;
  real_T t_im;
  if ((a.im == 0.0) && (a.re >= 0.0)) {
    c.re = muDoubleScalarPower(a.re, 0.23809523809523808);
    c.im = 0.0;
  } else {
    t_re = a.re;
    t_im = a.im;
    if ((a.im == 0.0) && muDoubleScalarIsNaN(a.re)) {
    } else if ((muDoubleScalarAbs(a.re) > 8.9884656743115785E+307) ||
               (muDoubleScalarAbs(a.im) > 8.9884656743115785E+307)) {
      t_re = muDoubleScalarLog(muDoubleScalarHypot(a.re / 2.0, a.im / 2.0)) +
        0.69314718055994529;
      t_im = muDoubleScalarAtan2(a.im, a.re);
    } else {
      t_re = muDoubleScalarLog(muDoubleScalarHypot(a.re, a.im));
      t_im = muDoubleScalarAtan2(a.im, a.re);
    }

    t_re *= 0.23809523809523808;
    t_im *= 0.23809523809523808;
    t_re = muDoubleScalarExp(t_re);
    c.re = t_re * muDoubleScalarCos(t_im);
    c.im = t_re * muDoubleScalarSin(t_im);
  }

  return c;
}

real_T mpower(real_T a)
{
  real_T c;
  emlrtPushRtStackR2012b(&nc_emlrtRSI, emlrtRootTLSGlobal);
  emlrtPushRtStackR2012b(&oc_emlrtRSI, emlrtRootTLSGlobal);
  if (a < 0.0) {
    emlrtPushRtStackR2012b(&pc_emlrtRSI, emlrtRootTLSGlobal);
    eml_error();
    emlrtPopRtStackR2012b(&pc_emlrtRSI, emlrtRootTLSGlobal);
  }

  c = muDoubleScalarPower(a, 5.2);
  emlrtPopRtStackR2012b(&oc_emlrtRSI, emlrtRootTLSGlobal);
  emlrtPopRtStackR2012b(&nc_emlrtRSI, emlrtRootTLSGlobal);
  return c;
}

/* End of code generation (mpower.c) */
