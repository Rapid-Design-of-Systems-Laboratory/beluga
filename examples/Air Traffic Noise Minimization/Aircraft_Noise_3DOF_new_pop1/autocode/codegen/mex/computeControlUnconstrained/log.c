/*
 * log.c
 *
 * Code generation for function 'log'
 *
 * C source code generated on: Sat Jan 21 02:01:21 2017
 *
 */

/* Include files */
#include "rt_nonfinite.h"
#include "computeControlUnconstrained.h"
#include "log.h"

/* Function Definitions */
void b_log(creal_T *x)
{
  real_T x_re;
  real_T x_im;
  real_T b_x_im;
  real_T b_x_re;
  if ((x->im == 0.0) && muDoubleScalarIsNaN(x->re)) {
  } else if ((muDoubleScalarAbs(x->re) > 8.9884656743115785E+307) ||
             (muDoubleScalarAbs(x->im) > 8.9884656743115785E+307)) {
    x_re = x->re;
    x_im = x->im;
    b_x_im = x->im;
    b_x_re = x->re;
    x->re = muDoubleScalarLog(muDoubleScalarHypot(x_re / 2.0, x_im / 2.0)) +
      0.69314718055994529;
    x->im = muDoubleScalarAtan2(b_x_im, b_x_re);
  } else {
    x_re = x->re;
    x_im = x->im;
    b_x_im = x->im;
    b_x_re = x->re;
    x->re = muDoubleScalarLog(muDoubleScalarHypot(x_re, x_im));
    x->im = muDoubleScalarAtan2(b_x_im, b_x_re);
  }
}

/* End of code generation (log.c) */
