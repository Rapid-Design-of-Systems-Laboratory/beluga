/*
 * acos.c
 *
 * Code generation for function 'acos'
 *
 * C source code generated on: Sat Jan 21 02:03:43 2017
 *
 */

/* Include files */
#include "rt_nonfinite.h"
#include "bc.h"
#include "acos.h"
#include "asin.h"

/* Function Definitions */
void b_acos(creal_T *x)
{
  real_T yr;
  creal_T v;
  creal_T u;
  real_T d0;
  if ((x->im == 0.0) && (!(muDoubleScalarAbs(x->re) > 1.0))) {
    yr = x->re;
    x->re = muDoubleScalarAcos(yr);
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

    if (x->re == 0.0) {
      yr = 1.5707963267948966;
    } else {
      yr = 2.0 * muDoubleScalarAtan2(muDoubleScalarAbs(u.re), muDoubleScalarAbs
        (v.re));
      if ((u.re < 0.0) != (v.re < 0.0)) {
        yr = -yr;
      }
    }

    d0 = u.im * v.re - u.re * v.im;
    eml_scalar_asinh(&d0);
    x->re = yr;
    x->im = d0;
  }
}

/* End of code generation (acos.c) */
