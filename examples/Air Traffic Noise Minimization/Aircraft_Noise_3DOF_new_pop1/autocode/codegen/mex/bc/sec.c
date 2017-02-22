/*
 * sec.c
 *
 * Code generation for function 'sec'
 *
 * C source code generated on: Sat Jan 21 02:03:43 2017
 *
 */

/* Include files */
#include "rt_nonfinite.h"
#include "bc.h"
#include "sec.h"
#include "computeControlUnconstrained.h"

/* Function Definitions */
void sec(creal_T *x)
{
  real_T x_re;
  real_T x_im;
  real_T b_x_re;
  real_T b_x_im;
  if (x->im == 0.0) {
    x_re = x->re;
    x->re = muDoubleScalarCos(x_re);
    x->im = 0.0;
  } else {
    x_re = x->re;
    x_im = x->im;
    b_x_re = x->re;
    b_x_im = x->im;
    x->re = muDoubleScalarCos(x_re) * muDoubleScalarCosh(x_im);
    x->im = -muDoubleScalarSin(b_x_re) * muDoubleScalarSinh(b_x_im);
  }

  *x = eml_div(1.0, *x);
}

/* End of code generation (sec.c) */
