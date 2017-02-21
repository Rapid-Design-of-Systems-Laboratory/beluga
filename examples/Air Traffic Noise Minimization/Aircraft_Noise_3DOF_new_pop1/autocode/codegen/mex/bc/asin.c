/*
 * asin.c
 *
 * Code generation for function 'asin'
 *
 * C source code generated on: Sat Jan 21 02:03:43 2017
 *
 */

/* Include files */
#include "rt_nonfinite.h"
#include "bc.h"
#include "asin.h"
#include "bc_data.h"

/* Variable Definitions */
static emlrtRSInfo rc_emlrtRSI = { 14, "asin",
  "/apps/rhel6/MATLAB/R2013a/toolbox/eml/lib/matlab/elfun/asin.m" };

/* Function Declarations */
static void b_eml_error(void);

/* Function Definitions */
static void b_eml_error(void)
{
  static char_T cv0[4][1] = { { 'a' }, { 's' }, { 'i' }, { 'n' } };

  emlrtPushRtStackR2012b(&qc_emlrtRSI, emlrtRootTLSGlobal);
  emlrtErrorWithMessageIdR2012b(emlrtRootTLSGlobal, &emlrtRTEI,
    "Coder:toolbox:ElFunDomainError", 3, 4, 4, cv0);
  emlrtPopRtStackR2012b(&qc_emlrtRSI, emlrtRootTLSGlobal);
}

void b_asin(real_T *x)
{
  if ((*x < -1.0) || (1.0 < *x)) {
    emlrtPushRtStackR2012b(&rc_emlrtRSI, emlrtRootTLSGlobal);
    b_eml_error();
    emlrtPopRtStackR2012b(&rc_emlrtRSI, emlrtRootTLSGlobal);
  }

  *x = muDoubleScalarAsin(*x);
}

void c_asin(creal_T *x)
{
  real_T uvr;
  creal_T v;
  creal_T u;
  real_T yr;
  if ((x->im == 0.0) && (!(muDoubleScalarAbs(x->re) > 1.0))) {
    uvr = x->re;
    x->re = muDoubleScalarAsin(uvr);
    x->im = 0.0;
  } else {
    v.re = 1.0 + x->re;
    v.im = x->im;
    eml_scalar_sqrt(&v);
    if (x->im != 0.0) {
      u.re = 1.0 - x->re;
      u.im = -x->im;
      eml_scalar_sqrt(&u);
    } else {
      u.re = 1.0 - x->re;
      u.im = x->im;
      eml_scalar_sqrt(&u);
    }

    uvr = u.re * v.re - u.im * v.im;
    yr = muDoubleScalarAtan2(muDoubleScalarAbs(x->re), muDoubleScalarAbs(uvr));
    if ((x->re < 0.0) != (uvr < 0.0)) {
      yr = -yr;
    }

    uvr = u.re * v.im - u.im * v.re;
    eml_scalar_asinh(&uvr);
    x->re = yr;
    x->im = uvr;
  }
}

void eml_scalar_asinh(real_T *x)
{
  boolean_T xneg;
  real_T t;
  real_T absz;
  xneg = (*x < 0.0);
  if (xneg) {
    *x = -*x;
  }

  if (*x >= 2.68435456E+8) {
    *x = muDoubleScalarLog(*x) + 0.69314718055994529;
  } else if (*x > 2.0) {
    *x = muDoubleScalarLog(2.0 * *x + 1.0 / (muDoubleScalarSqrt(*x * *x + 1.0) +
      *x));
  } else {
    t = *x * *x;
    t = *x + t / (1.0 + muDoubleScalarSqrt(1.0 + t));
    *x = t;
    absz = muDoubleScalarAbs(t);
    if ((absz > 4.503599627370496E+15) || (!((!muDoubleScalarIsInf(t)) &&
          (!muDoubleScalarIsNaN(t))))) {
      *x = muDoubleScalarLog(1.0 + t);
    } else if (absz < 2.2204460492503131E-16) {
    } else {
      *x = muDoubleScalarLog(1.0 + t) * (t / ((1.0 + t) - 1.0));
    }
  }

  if (xneg) {
    *x = -*x;
  }
}

void eml_scalar_sqrt(creal_T *x)
{
  real_T absxi;
  real_T absxr;
  if (x->im == 0.0) {
    if (x->re < 0.0) {
      absxi = 0.0;
      absxr = muDoubleScalarSqrt(muDoubleScalarAbs(x->re));
    } else {
      absxi = muDoubleScalarSqrt(x->re);
      absxr = 0.0;
    }
  } else if (x->re == 0.0) {
    if (x->im < 0.0) {
      absxi = muDoubleScalarSqrt(-x->im / 2.0);
      absxr = -absxi;
    } else {
      absxi = muDoubleScalarSqrt(x->im / 2.0);
      absxr = absxi;
    }
  } else if (muDoubleScalarIsNaN(x->re) || muDoubleScalarIsNaN(x->im)) {
    absxi = rtNaN;
    absxr = rtNaN;
  } else if (muDoubleScalarIsInf(x->im)) {
    absxi = rtInf;
    absxr = x->im;
  } else if (muDoubleScalarIsInf(x->re)) {
    if (x->re < 0.0) {
      absxi = 0.0;
      absxr = rtInf;
    } else {
      absxi = rtInf;
      absxr = 0.0;
    }
  } else {
    absxr = muDoubleScalarAbs(x->re);
    absxi = muDoubleScalarAbs(x->im);
    if ((absxr > 4.4942328371557893E+307) || (absxi > 4.4942328371557893E+307))
    {
      absxr *= 0.5;
      absxi *= 0.5;
      absxi = muDoubleScalarHypot(absxr, absxi);
      if (absxi > absxr) {
        absxi = muDoubleScalarSqrt(absxi) * muDoubleScalarSqrt(1.0 + absxr /
          absxi);
      } else {
        absxi = muDoubleScalarSqrt(absxi) * 1.4142135623730951;
      }
    } else {
      absxi = muDoubleScalarSqrt((muDoubleScalarHypot(absxr, absxi) + absxr) *
        0.5);
    }

    if (x->re > 0.0) {
      absxr = 0.5 * (x->im / absxi);
    } else {
      if (x->im < 0.0) {
        absxr = -absxi;
      } else {
        absxr = absxi;
      }

      absxi = 0.5 * (x->im / absxr);
    }
  }

  x->re = absxi;
  x->im = absxr;
}

/* End of code generation (asin.c) */
