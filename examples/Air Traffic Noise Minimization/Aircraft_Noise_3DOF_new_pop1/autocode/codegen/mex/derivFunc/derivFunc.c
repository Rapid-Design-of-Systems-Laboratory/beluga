/*
 * derivFunc.c
 *
 * Code generation for function 'derivFunc'
 *
 * C source code generated on: Sat Jan 21 02:02:06 2017
 *
 */

/* Include files */
#include "rt_nonfinite.h"
#include "derivFunc.h"
#include "computeControlUnconstrained.h"
#include "derivFunc_data.h"

/* Variable Definitions */
static emlrtRSInfo emlrtRSI = { 89, "derivFunc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/derivFunc.m"
};

static emlrtRSInfo b_emlrtRSI = { 94, "derivFunc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/derivFunc.m"
};

static emlrtECInfo emlrtECI = { 1, 87, 3, "derivFunc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/derivFunc.m"
};

static emlrtDCInfo emlrtDCI = { 85, 8, "derivFunc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/derivFunc.m",
  1 };

static emlrtBCInfo emlrtBCI = { -1, -1, 80, 8, "p", "derivFunc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/derivFunc.m",
  0 };

/* Function Definitions */
void derivFunc(real_T t, const real_T X[12], const real_T p_data[19], const
               int32_T p_size[1], const struct_T *b_const, real_T arcSequence,
               const real_T x0[6], const real_T xf[6], real_T xDotOut[12])
{
  real_T banktrig;
  real_T alfatrig;
  real_T Ttrignew;
  real_T X_data[13];
  real_T b_X[12];
  real_T hamiltonian;
  real_T y;
  real_T b_y;
  real_T x;
  int32_T i0;
  memset(&xDotOut[0], 0, 12U * sizeof(real_T));

  /* %%%%%%%%%%%%%%% */
  /* % Parameters %% */
  /* %%%%%%%%%%%%%%% */
  /*  States */
  /*  Costates */
  /*  Constants */
  emlrtDynamicBoundsCheckFastR2012b(1, 1, p_size[0], &emlrtBCI,
    emlrtRootTLSGlobal);
  banktrig = rtNaN;
  alfatrig = rtNaN;
  Ttrignew = rtNaN;
  switch ((int32_T)emlrtIntegerCheckFastR2012b(arcSequence, &emlrtDCI,
           emlrtRootTLSGlobal)) {
   case 0:
    /*  unconstrained arc */
    emlrtDimSizeGeqCheckFastR2012b(13, 12, &emlrtECI, emlrtRootTLSGlobal);
    emlrtPushRtStackR2012b(&emlrtRSI, emlrtRootTLSGlobal);
    b_X[0] = X[0];
    b_X[1] = X[1];
    b_X[2] = X[2];
    b_X[3] = X[3];
    b_X[4] = X[4];
    b_X[5] = X[5];
    b_X[6] = X[6];
    b_X[7] = X[7];
    b_X[8] = X[8];
    b_X[9] = X[9];
    b_X[10] = X[10];
    b_X[11] = X[11];
    memcpy(&X_data[0], &b_X[0], 12U * sizeof(real_T));
    computeControlUnconstrained(X_data, b_const->C1, b_const->C2,
      b_const->alfamax, b_const->bankmax, b_const->g, b_const->mass, &banktrig,
      &alfatrig, &Ttrignew, &hamiltonian);
    emlrtPopRtStackR2012b(&emlrtRSI, emlrtRootTLSGlobal);
    emlrtPushRtStackR2012b(&b_emlrtRSI, emlrtRootTLSGlobal);
    hamiltonian = 1560.0 * muDoubleScalarSin(Ttrignew);
    emlrtPushRtStackR2012b(&nc_emlrtRSI, emlrtRootTLSGlobal);
    emlrtPushRtStackR2012b(&oc_emlrtRSI, emlrtRootTLSGlobal);
    if (hamiltonian + 1860.0 < 0.0) {
      emlrtPushRtStackR2012b(&pc_emlrtRSI, emlrtRootTLSGlobal);
      eml_error();
      emlrtPopRtStackR2012b(&pc_emlrtRSI, emlrtRootTLSGlobal);
    }

    emlrtPopRtStackR2012b(&oc_emlrtRSI, emlrtRootTLSGlobal);
    emlrtPopRtStackR2012b(&nc_emlrtRSI, emlrtRootTLSGlobal);
    emlrtPushRtStackR2012b(&nc_emlrtRSI, emlrtRootTLSGlobal);
    emlrtPushRtStackR2012b(&oc_emlrtRSI, emlrtRootTLSGlobal);
    if (X[2] + 50.0 < 0.0) {
      emlrtPushRtStackR2012b(&pc_emlrtRSI, emlrtRootTLSGlobal);
      eml_error();
      emlrtPopRtStackR2012b(&pc_emlrtRSI, emlrtRootTLSGlobal);
    }

    emlrtPopRtStackR2012b(&oc_emlrtRSI, emlrtRootTLSGlobal);
    emlrtPopRtStackR2012b(&nc_emlrtRSI, emlrtRootTLSGlobal);
    y = 1560.0 * muDoubleScalarSin(Ttrignew);
    emlrtPushRtStackR2012b(&nc_emlrtRSI, emlrtRootTLSGlobal);
    emlrtPushRtStackR2012b(&oc_emlrtRSI, emlrtRootTLSGlobal);
    if (y + 1860.0 < 0.0) {
      emlrtPushRtStackR2012b(&pc_emlrtRSI, emlrtRootTLSGlobal);
      eml_error();
      emlrtPopRtStackR2012b(&pc_emlrtRSI, emlrtRootTLSGlobal);
    }

    emlrtPopRtStackR2012b(&oc_emlrtRSI, emlrtRootTLSGlobal);
    emlrtPopRtStackR2012b(&nc_emlrtRSI, emlrtRootTLSGlobal);
    emlrtPushRtStackR2012b(&nc_emlrtRSI, emlrtRootTLSGlobal);
    emlrtPushRtStackR2012b(&oc_emlrtRSI, emlrtRootTLSGlobal);
    if (X[2] + 50.0 < 0.0) {
      emlrtPushRtStackR2012b(&pc_emlrtRSI, emlrtRootTLSGlobal);
      eml_error();
      emlrtPopRtStackR2012b(&pc_emlrtRSI, emlrtRootTLSGlobal);
    }

    emlrtPopRtStackR2012b(&oc_emlrtRSI, emlrtRootTLSGlobal);
    emlrtPopRtStackR2012b(&nc_emlrtRSI, emlrtRootTLSGlobal);
    b_y = 1560.0 * muDoubleScalarSin(Ttrignew);
    emlrtPushRtStackR2012b(&nc_emlrtRSI, emlrtRootTLSGlobal);
    emlrtPushRtStackR2012b(&oc_emlrtRSI, emlrtRootTLSGlobal);
    if (b_y + 1860.0 < 0.0) {
      emlrtPushRtStackR2012b(&pc_emlrtRSI, emlrtRootTLSGlobal);
      eml_error();
      emlrtPopRtStackR2012b(&pc_emlrtRSI, emlrtRootTLSGlobal);
    }

    emlrtPopRtStackR2012b(&oc_emlrtRSI, emlrtRootTLSGlobal);
    emlrtPopRtStackR2012b(&nc_emlrtRSI, emlrtRootTLSGlobal);
    emlrtPushRtStackR2012b(&nc_emlrtRSI, emlrtRootTLSGlobal);
    emlrtPushRtStackR2012b(&oc_emlrtRSI, emlrtRootTLSGlobal);
    if (X[2] + 50.0 < 0.0) {
      emlrtPushRtStackR2012b(&pc_emlrtRSI, emlrtRootTLSGlobal);
      eml_error();
      emlrtPopRtStackR2012b(&pc_emlrtRSI, emlrtRootTLSGlobal);
    }

    emlrtPopRtStackR2012b(&oc_emlrtRSI, emlrtRootTLSGlobal);
    emlrtPopRtStackR2012b(&nc_emlrtRSI, emlrtRootTLSGlobal);
    x = muDoubleScalarCos(X[5]);
    xDotOut[6] = 0.0;
    xDotOut[7] = 0.0;
    xDotOut[8] = 2.5 * muDoubleScalarCos(X[5]) * muDoubleScalarPower(hamiltonian
      + 1860.0, 5.2) / (X[3] * muDoubleScalarPower(X[2] + 50.0, 3.5));
    xDotOut[9] = (((((X[9] * (2.0 * b_const->C1 * X[3] - 2.0 * b_const->C2 /
      muDoubleScalarPower(X[3], 3.0)) / b_const->mass - X[8] * muDoubleScalarSin
                      (X[5])) - X[6] * muDoubleScalarCos(X[5]) *
                     muDoubleScalarCos(X[4])) - X[7] * muDoubleScalarCos(X[5]) *
                    muDoubleScalarSin(X[4])) - X[11] * (b_const->g *
      muDoubleScalarCos(X[5]) / (X[3] * X[3]) - muDoubleScalarCos
      (b_const->bankmax * muDoubleScalarSin(banktrig)) * (b_const->g *
      b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
      (alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0)) /
      (b_const->mass * (X[3] * X[3])))) + muDoubleScalarCos(X[5]) *
                  muDoubleScalarPower(y + 1860.0, 5.2) / (X[3] * X[3] *
      muDoubleScalarPower(X[2] + 50.0, 2.5))) + X[10] * muDoubleScalarSin
      (b_const->bankmax * muDoubleScalarSin(banktrig)) * (b_const->g *
      b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
      (alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0)) /
      (b_const->mass * (X[3] * X[3]) * muDoubleScalarCos(X[5]));
    xDotOut[10] = X[6] * X[3] * muDoubleScalarCos(X[5]) * muDoubleScalarSin(X[4])
      - X[7] * X[3] * muDoubleScalarCos(X[5]) * muDoubleScalarCos(X[4]);
    xDotOut[11] = (((((b_const->g * X[9] * muDoubleScalarCos(X[5]) - X[8] * X[3]
                       * muDoubleScalarCos(X[5])) + X[7] * X[3] *
                      muDoubleScalarSin(X[5]) * muDoubleScalarSin(X[4])) +
                     muDoubleScalarSin(X[5]) * muDoubleScalarPower(b_y + 1860.0,
      5.2) / (X[3] * muDoubleScalarPower(X[2] + 50.0, 2.5))) - b_const->g * X[11]
                    * muDoubleScalarSin(X[5]) / X[3]) + X[6] * X[3] *
                   muDoubleScalarCos(X[4]) * muDoubleScalarSin(X[5])) - X[10] *
      muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) *
      muDoubleScalarSin(X[5]) * (b_const->g * b_const->mass + muDoubleScalarSin
      (b_const->alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
      muDoubleScalarSin(Ttrignew) + 1860.0)) / (b_const->mass * X[3] * (x * x));
    emlrtPopRtStackR2012b(&b_emlrtRSI, emlrtRootTLSGlobal);
    break;
  }

  /*  Equations of motion */
  xDotOut[0] = X[3] * muDoubleScalarCos(X[5]) * muDoubleScalarCos(X[4]);
  xDotOut[1] = X[3] * muDoubleScalarCos(X[5]) * muDoubleScalarSin(X[4]);
  xDotOut[2] = X[3] * muDoubleScalarSin(X[5]);
  xDotOut[3] = -((b_const->C1 * (X[3] * X[3]) + b_const->C2 / (X[3] * X[3])) -
                 muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig))
                 * (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0)) /
    b_const->mass - b_const->g * muDoubleScalarSin(X[5]);
  xDotOut[4] = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig))
    * (b_const->g * b_const->mass + muDoubleScalarSin(b_const->alfamax *
        muDoubleScalarSin(alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) +
        1860.0)) / (b_const->mass * X[3] * muDoubleScalarCos(X[5]));
  xDotOut[5] = muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig))
    * (b_const->g * b_const->mass + muDoubleScalarSin(b_const->alfamax *
        muDoubleScalarSin(alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) +
        1860.0)) / (b_const->mass * X[3]) - b_const->g * muDoubleScalarCos(X[5])
    / X[3];

  /*  Account for variable endpoints in derivative */
  for (i0 = 0; i0 < 12; i0++) {
    xDotOut[i0] *= p_data[0];
  }
}

void eml_error(void)
{
  emlrtPushRtStackR2012b(&qc_emlrtRSI, emlrtRootTLSGlobal);
  emlrtErrorWithMessageIdR2012b(emlrtRootTLSGlobal, &b_emlrtRTEI,
    "Coder:toolbox:power_domainError", 0);
  emlrtPopRtStackR2012b(&qc_emlrtRSI, emlrtRootTLSGlobal);
}

/* End of code generation (derivFunc.c) */
