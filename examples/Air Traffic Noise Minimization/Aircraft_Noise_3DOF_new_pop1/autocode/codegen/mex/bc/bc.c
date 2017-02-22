/*
 * bc.c
 *
 * Code generation for function 'bc'
 *
 * C source code generated on: Sat Jan 21 02:03:42 2017
 *
 */

/* Include files */
#include "rt_nonfinite.h"
#include "bc.h"
#include "computeControlUnconstrained.h"
#include "bc_data.h"

/* Variable Definitions */
static emlrtRSInfo emlrtRSI = { 216, "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m"
};

static emlrtRSInfo b_emlrtRSI = { 214, "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m"
};

static emlrtRSInfo c_emlrtRSI = { 207, "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m"
};

static emlrtBCInfo emlrtBCI = { -1, -1, 84, 8, "p", "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m",
  0 };

static emlrtBCInfo b_emlrtBCI = { -1, -1, 86, 14, "p", "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m",
  0 };

static emlrtBCInfo c_emlrtBCI = { -1, -1, 87, 14, "p", "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m",
  0 };

static emlrtBCInfo d_emlrtBCI = { -1, -1, 88, 14, "p", "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m",
  0 };

static emlrtBCInfo e_emlrtBCI = { -1, -1, 89, 14, "p", "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m",
  0 };

static emlrtBCInfo f_emlrtBCI = { -1, -1, 90, 14, "p", "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m",
  0 };

static emlrtBCInfo g_emlrtBCI = { -1, -1, 91, 14, "p", "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m",
  0 };

static emlrtBCInfo h_emlrtBCI = { -1, -1, 93, 15, "p", "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m",
  0 };

static emlrtBCInfo i_emlrtBCI = { -1, -1, 94, 15, "p", "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m",
  0 };

static emlrtBCInfo j_emlrtBCI = { -1, -1, 95, 15, "p", "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m",
  0 };

static emlrtBCInfo k_emlrtBCI = { -1, -1, 96, 15, "p", "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m",
  0 };

static emlrtBCInfo l_emlrtBCI = { -1, -1, 97, 15, "p", "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m",
  0 };

static emlrtBCInfo m_emlrtBCI = { -1, -1, 98, 15, "p", "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m",
  0 };

static emlrtBCInfo n_emlrtBCI = { -1, -1, 100, 19, "p", "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m",
  0 };

static emlrtECInfo emlrtECI = { -1, 100, 19, "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m"
};

static emlrtBCInfo o_emlrtBCI = { -1, -1, 135, 11, "YL", "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m",
  0 };

static emlrtBCInfo p_emlrtBCI = { -1, -1, 136, 11, "YL", "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m",
  0 };

static emlrtBCInfo q_emlrtBCI = { -1, -1, 137, 11, "YL", "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m",
  0 };

static emlrtBCInfo r_emlrtBCI = { -1, -1, 138, 11, "YL", "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m",
  0 };

static emlrtBCInfo s_emlrtBCI = { -1, -1, 139, 14, "YL", "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m",
  0 };

static emlrtBCInfo t_emlrtBCI = { -1, -1, 140, 13, "YL", "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m",
  0 };

static emlrtBCInfo u_emlrtBCI = { -1, -1, 143, 14, "YL", "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m",
  0 };

static emlrtBCInfo v_emlrtBCI = { -1, -1, 144, 14, "YL", "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m",
  0 };

static emlrtBCInfo w_emlrtBCI = { -1, -1, 145, 14, "YL", "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m",
  0 };

static emlrtBCInfo x_emlrtBCI = { -1, -1, 146, 14, "YL", "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m",
  0 };

static emlrtBCInfo y_emlrtBCI = { -1, -1, 147, 17, "YL", "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m",
  0 };

static emlrtBCInfo ab_emlrtBCI = { -1, -1, 148, 16, "YL", "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m",
  0 };

static emlrtBCInfo bb_emlrtBCI = { -1, -1, 170, 11, "YR", "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m",
  0 };

static emlrtBCInfo cb_emlrtBCI = { -1, -1, 171, 11, "YR", "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m",
  0 };

static emlrtBCInfo db_emlrtBCI = { -1, -1, 172, 11, "YR", "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m",
  0 };

static emlrtBCInfo eb_emlrtBCI = { -1, -1, 173, 11, "YR", "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m",
  0 };

static emlrtBCInfo fb_emlrtBCI = { -1, -1, 174, 14, "YR", "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m",
  0 };

static emlrtBCInfo gb_emlrtBCI = { -1, -1, 175, 13, "YR", "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m",
  0 };

static emlrtBCInfo hb_emlrtBCI = { -1, -1, 178, 14, "YR", "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m",
  0 };

static emlrtBCInfo ib_emlrtBCI = { -1, -1, 179, 14, "YR", "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m",
  0 };

static emlrtBCInfo jb_emlrtBCI = { -1, -1, 180, 14, "YR", "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m",
  0 };

static emlrtBCInfo kb_emlrtBCI = { -1, -1, 181, 14, "YR", "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m",
  0 };

static emlrtBCInfo lb_emlrtBCI = { -1, -1, 182, 17, "YR", "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m",
  0 };

static emlrtBCInfo mb_emlrtBCI = { -1, -1, 183, 16, "YR", "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m",
  0 };

static emlrtDCInfo emlrtDCI = { 204, 10, "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m",
  1 };

static emlrtECInfo b_emlrtECI = { 1, 103, 1, "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m"
};

static emlrtECInfo c_emlrtECI = { 2, 104, 1, "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m"
};

static emlrtECInfo d_emlrtECI = { 1, 105, 1, "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m"
};

static emlrtECInfo e_emlrtECI = { 2, 128, 2, "bc",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/bc.m"
};

/* Function Definitions */
void bc(const real_T YL_data[12], const int32_T YL_size[1], const real_T
        YR_data[12], const int32_T YR_size[1], const real_T p_data[19], const
        int32_T p_size[1], const struct_T *b_const, real_T arcSequence, const
        real_T x0[6], const real_T xf[6], real_T zeroVec[25])
{
  real_T H_t_minus;
  real_T banktrig;
  real_T alfatrig;
  real_T Ttrignew;
  real_T xAndLambda0Constraint[12];
  real_T xAndLambdaFConstraint[12];
  int32_T i;
  int32_T i0;
  int32_T i1;
  real_T z;
  real_T v;
  real_T psii;
  real_T gam;
  real_T lamX;
  real_T lamY;
  real_T lamZ;
  real_T lamV;
  real_T lamPSII;
  real_T lamGAM;
  real_T xAndLambda[12];
  real_T d2Hdu2;
  H_t_minus = rtNaN;
  banktrig = rtNaN;
  alfatrig = rtNaN;
  Ttrignew = rtNaN;
  for (i = 0; i < 12; i++) {
    xAndLambda0Constraint[i] = rtNaN;
    xAndLambdaFConstraint[i] = rtNaN;
  }

  /* %%%%%%%%%%%%%%% */
  /* % Parameters %% */
  /* %%%%%%%%%%%%%%% */
  emlrtDynamicBoundsCheckFastR2012b(1, 1, p_size[0], &emlrtBCI,
    emlrtRootTLSGlobal);
  emlrtDynamicBoundsCheckFastR2012b(2, 1, p_size[0], &b_emlrtBCI,
    emlrtRootTLSGlobal);
  emlrtDynamicBoundsCheckFastR2012b(3, 1, p_size[0], &c_emlrtBCI,
    emlrtRootTLSGlobal);
  emlrtDynamicBoundsCheckFastR2012b(4, 1, p_size[0], &d_emlrtBCI,
    emlrtRootTLSGlobal);
  emlrtDynamicBoundsCheckFastR2012b(5, 1, p_size[0], &e_emlrtBCI,
    emlrtRootTLSGlobal);
  emlrtDynamicBoundsCheckFastR2012b(6, 1, p_size[0], &f_emlrtBCI,
    emlrtRootTLSGlobal);
  emlrtDynamicBoundsCheckFastR2012b(7, 1, p_size[0], &g_emlrtBCI,
    emlrtRootTLSGlobal);
  emlrtDynamicBoundsCheckFastR2012b(8, 1, p_size[0], &h_emlrtBCI,
    emlrtRootTLSGlobal);
  emlrtDynamicBoundsCheckFastR2012b(9, 1, p_size[0], &i_emlrtBCI,
    emlrtRootTLSGlobal);
  emlrtDynamicBoundsCheckFastR2012b(10, 1, p_size[0], &j_emlrtBCI,
    emlrtRootTLSGlobal);
  emlrtDynamicBoundsCheckFastR2012b(11, 1, p_size[0], &k_emlrtBCI,
    emlrtRootTLSGlobal);
  emlrtDynamicBoundsCheckFastR2012b(12, 1, p_size[0], &l_emlrtBCI,
    emlrtRootTLSGlobal);
  emlrtDynamicBoundsCheckFastR2012b(13, 1, p_size[0], &m_emlrtBCI,
    emlrtRootTLSGlobal);
  if (14 > p_size[0]) {
    i = 1;
    i0 = 1;
  } else {
    i = 14;
    i0 = emlrtDynamicBoundsCheckFastR2012b(p_size[0], 1, p_size[0], &n_emlrtBCI,
      emlrtRootTLSGlobal) + 1;
  }

  emlrtVectorVectorIndexCheckR2012b(p_size[0], 1, 1, i0 - i, &emlrtECI,
    emlrtRootTLSGlobal);
  i1 = i0 - i;
  emlrtDimSizeGeqCheckFastR2012b(6, i1, &b_emlrtECI, emlrtRootTLSGlobal);
  i1 = i0 - i;
  emlrtDimSizeGeqCheckFastR2012b(6, i1, &c_emlrtECI, emlrtRootTLSGlobal);
  i = i0 - i;
  emlrtDimSizeGeqCheckFastR2012b(6, i, &d_emlrtECI, emlrtRootTLSGlobal);

  /*  Constants */
  emlrtDimSizeGeqCheckFastR2012b(6, 1, &e_emlrtECI, emlrtRootTLSGlobal);
  for (i = 0; i < 2; i++) {
    if (1 + i == 1) {
      /*  Left endpoint */
      /*  States */
      emlrtDynamicBoundsCheckFastR2012b(1, 1, YL_size[0], &o_emlrtBCI,
        emlrtRootTLSGlobal);
      emlrtDynamicBoundsCheckFastR2012b(2, 1, YL_size[0], &p_emlrtBCI,
        emlrtRootTLSGlobal);
      emlrtDynamicBoundsCheckFastR2012b(3, 1, YL_size[0], &q_emlrtBCI,
        emlrtRootTLSGlobal);
      z = YL_data[2];
      emlrtDynamicBoundsCheckFastR2012b(4, 1, YL_size[0], &r_emlrtBCI,
        emlrtRootTLSGlobal);
      v = YL_data[3];
      emlrtDynamicBoundsCheckFastR2012b(5, 1, YL_size[0], &s_emlrtBCI,
        emlrtRootTLSGlobal);
      psii = YL_data[4];
      emlrtDynamicBoundsCheckFastR2012b(6, 1, YL_size[0], &t_emlrtBCI,
        emlrtRootTLSGlobal);
      gam = YL_data[5];

      /*  Costates */
      emlrtDynamicBoundsCheckFastR2012b(7, 1, YL_size[0], &u_emlrtBCI,
        emlrtRootTLSGlobal);
      lamX = YL_data[6];
      emlrtDynamicBoundsCheckFastR2012b(8, 1, YL_size[0], &v_emlrtBCI,
        emlrtRootTLSGlobal);
      lamY = YL_data[7];
      emlrtDynamicBoundsCheckFastR2012b(9, 1, YL_size[0], &w_emlrtBCI,
        emlrtRootTLSGlobal);
      lamZ = YL_data[8];
      emlrtDynamicBoundsCheckFastR2012b(10, 1, YL_size[0], &x_emlrtBCI,
        emlrtRootTLSGlobal);
      lamV = YL_data[9];
      emlrtDynamicBoundsCheckFastR2012b(11, 1, YL_size[0], &y_emlrtBCI,
        emlrtRootTLSGlobal);
      lamPSII = YL_data[10];
      emlrtDynamicBoundsCheckFastR2012b(12, 1, YL_size[0], &ab_emlrtBCI,
        emlrtRootTLSGlobal);
      lamGAM = YL_data[11];
      xAndLambda[0] = YL_data[0];
      xAndLambda[1] = YL_data[1];
      xAndLambda[2] = YL_data[2];
      xAndLambda[3] = YL_data[3];
      xAndLambda[4] = YL_data[4];
      xAndLambda[5] = YL_data[5];
      xAndLambda[6] = YL_data[6];
      xAndLambda[7] = YL_data[7];
      xAndLambda[8] = YL_data[8];
      xAndLambda[9] = YL_data[9];
      xAndLambda[10] = YL_data[10];
      xAndLambda[11] = YL_data[11];
      xAndLambda0Constraint[0] = YL_data[6] - p_data[1];
      xAndLambda0Constraint[1] = YL_data[7] - p_data[2];
      xAndLambda0Constraint[2] = YL_data[8] - p_data[3];
      xAndLambda0Constraint[3] = YL_data[9] - p_data[4];
      xAndLambda0Constraint[4] = YL_data[10] - p_data[5];
      xAndLambda0Constraint[5] = YL_data[11] - p_data[6];
      xAndLambda0Constraint[6] = YL_data[0] - x0[0];
      xAndLambda0Constraint[7] = YL_data[1] - x0[1];
      xAndLambda0Constraint[8] = YL_data[2] - x0[2];
      xAndLambda0Constraint[9] = YL_data[3] - x0[3];
      xAndLambda0Constraint[10] = YL_data[4] - x0[4];
      xAndLambda0Constraint[11] = YL_data[5] - x0[5];
    } else {
      /*  Right endpoint */
      /*  States */
      emlrtDynamicBoundsCheckFastR2012b(1, 1, YR_size[0], &bb_emlrtBCI,
        emlrtRootTLSGlobal);
      emlrtDynamicBoundsCheckFastR2012b(2, 1, YR_size[0], &cb_emlrtBCI,
        emlrtRootTLSGlobal);
      emlrtDynamicBoundsCheckFastR2012b(3, 1, YR_size[0], &db_emlrtBCI,
        emlrtRootTLSGlobal);
      z = YR_data[2];
      emlrtDynamicBoundsCheckFastR2012b(4, 1, YR_size[0], &eb_emlrtBCI,
        emlrtRootTLSGlobal);
      v = YR_data[3];
      emlrtDynamicBoundsCheckFastR2012b(5, 1, YR_size[0], &fb_emlrtBCI,
        emlrtRootTLSGlobal);
      psii = YR_data[4];
      emlrtDynamicBoundsCheckFastR2012b(6, 1, YR_size[0], &gb_emlrtBCI,
        emlrtRootTLSGlobal);
      gam = YR_data[5];

      /*  Costates */
      emlrtDynamicBoundsCheckFastR2012b(7, 1, YR_size[0], &hb_emlrtBCI,
        emlrtRootTLSGlobal);
      lamX = YR_data[6];
      emlrtDynamicBoundsCheckFastR2012b(8, 1, YR_size[0], &ib_emlrtBCI,
        emlrtRootTLSGlobal);
      lamY = YR_data[7];
      emlrtDynamicBoundsCheckFastR2012b(9, 1, YR_size[0], &jb_emlrtBCI,
        emlrtRootTLSGlobal);
      lamZ = YR_data[8];
      emlrtDynamicBoundsCheckFastR2012b(10, 1, YR_size[0], &kb_emlrtBCI,
        emlrtRootTLSGlobal);
      lamV = YR_data[9];
      emlrtDynamicBoundsCheckFastR2012b(11, 1, YR_size[0], &lb_emlrtBCI,
        emlrtRootTLSGlobal);
      lamPSII = YR_data[10];
      emlrtDynamicBoundsCheckFastR2012b(12, 1, YR_size[0], &mb_emlrtBCI,
        emlrtRootTLSGlobal);
      lamGAM = YR_data[11];
      xAndLambda[0] = YR_data[0];
      xAndLambda[1] = YR_data[1];
      xAndLambda[2] = YR_data[2];
      xAndLambda[3] = YR_data[3];
      xAndLambda[4] = YR_data[4];
      xAndLambda[5] = YR_data[5];
      xAndLambda[6] = YR_data[6];
      xAndLambda[7] = YR_data[7];
      xAndLambda[8] = YR_data[8];
      xAndLambda[9] = YR_data[9];
      xAndLambda[10] = YR_data[10];
      xAndLambda[11] = YR_data[11];
      xAndLambdaFConstraint[0] = YR_data[6] - p_data[7];
      xAndLambdaFConstraint[1] = YR_data[7] - p_data[8];
      xAndLambdaFConstraint[2] = YR_data[8] - p_data[9];
      xAndLambdaFConstraint[3] = YR_data[9] - p_data[10];
      xAndLambdaFConstraint[4] = YR_data[10] - p_data[11];
      xAndLambdaFConstraint[5] = YR_data[11] - p_data[12];
      xAndLambdaFConstraint[6] = YR_data[0] - xf[0];
      xAndLambdaFConstraint[7] = YR_data[1] - xf[1];
      xAndLambdaFConstraint[8] = YR_data[2] - xf[2];
      xAndLambdaFConstraint[9] = YR_data[3] - xf[3];
      xAndLambdaFConstraint[10] = YR_data[4] - xf[4];
      xAndLambdaFConstraint[11] = YR_data[5] - xf[5];
    }

    switch ((int32_T)emlrtIntegerCheckFastR2012b(arcSequence, &emlrtDCI,
             emlrtRootTLSGlobal)) {
     case 0:
      /*  unconstrained arc */
      emlrtPushRtStackR2012b(&c_emlrtRSI, emlrtRootTLSGlobal);
      computeControlUnconstrained(xAndLambda, b_const->C1, b_const->C2,
        b_const->alfamax, b_const->bankmax, b_const->g, b_const->mass, &banktrig,
        &alfatrig, &Ttrignew, &d2Hdu2);
      emlrtPopRtStackR2012b(&c_emlrtRSI, emlrtRootTLSGlobal);
      break;
    }

    if (1 + i == 1) {
      emlrtPushRtStackR2012b(&b_emlrtRSI, emlrtRootTLSGlobal);
      emlrtPushRtStackR2012b(&nc_emlrtRSI, emlrtRootTLSGlobal);
      emlrtPushRtStackR2012b(&oc_emlrtRSI, emlrtRootTLSGlobal);
      if (z + 50.0 < 0.0) {
        emlrtPushRtStackR2012b(&pc_emlrtRSI, emlrtRootTLSGlobal);
        eml_error();
        emlrtPopRtStackR2012b(&pc_emlrtRSI, emlrtRootTLSGlobal);
      }

      emlrtPopRtStackR2012b(&oc_emlrtRSI, emlrtRootTLSGlobal);
      emlrtPopRtStackR2012b(&nc_emlrtRSI, emlrtRootTLSGlobal);
      emlrtPopRtStackR2012b(&b_emlrtRSI, emlrtRootTLSGlobal);
      emlrtPushRtStackR2012b(&b_emlrtRSI, emlrtRootTLSGlobal);
      emlrtPushRtStackR2012b(&nc_emlrtRSI, emlrtRootTLSGlobal);
      emlrtPushRtStackR2012b(&oc_emlrtRSI, emlrtRootTLSGlobal);
      if (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0 < 0.0) {
        emlrtPushRtStackR2012b(&pc_emlrtRSI, emlrtRootTLSGlobal);
        eml_error();
        emlrtPopRtStackR2012b(&pc_emlrtRSI, emlrtRootTLSGlobal);
      }

      emlrtPopRtStackR2012b(&oc_emlrtRSI, emlrtRootTLSGlobal);
      emlrtPopRtStackR2012b(&nc_emlrtRSI, emlrtRootTLSGlobal);
      emlrtPopRtStackR2012b(&b_emlrtRSI, emlrtRootTLSGlobal);
    } else {
      emlrtPushRtStackR2012b(&emlrtRSI, emlrtRootTLSGlobal);
      H_t_minus = 1560.0 * muDoubleScalarSin(Ttrignew);
      emlrtPushRtStackR2012b(&nc_emlrtRSI, emlrtRootTLSGlobal);
      emlrtPushRtStackR2012b(&oc_emlrtRSI, emlrtRootTLSGlobal);
      if (H_t_minus + 1860.0 < 0.0) {
        emlrtPushRtStackR2012b(&pc_emlrtRSI, emlrtRootTLSGlobal);
        eml_error();
        emlrtPopRtStackR2012b(&pc_emlrtRSI, emlrtRootTLSGlobal);
      }

      emlrtPopRtStackR2012b(&oc_emlrtRSI, emlrtRootTLSGlobal);
      emlrtPopRtStackR2012b(&nc_emlrtRSI, emlrtRootTLSGlobal);
      emlrtPushRtStackR2012b(&nc_emlrtRSI, emlrtRootTLSGlobal);
      emlrtPushRtStackR2012b(&oc_emlrtRSI, emlrtRootTLSGlobal);
      if (z + 50.0 < 0.0) {
        emlrtPushRtStackR2012b(&pc_emlrtRSI, emlrtRootTLSGlobal);
        eml_error();
        emlrtPopRtStackR2012b(&pc_emlrtRSI, emlrtRootTLSGlobal);
      }

      emlrtPopRtStackR2012b(&oc_emlrtRSI, emlrtRootTLSGlobal);
      emlrtPopRtStackR2012b(&nc_emlrtRSI, emlrtRootTLSGlobal);
      H_t_minus = (((((lamZ * v * muDoubleScalarSin(gam) - lamV * (((b_const->C1
        * (v * v) + b_const->C2 / (v * v)) - muDoubleScalarCos(b_const->alfamax *
        muDoubleScalarSin(alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) +
        1860.0)) / b_const->mass + b_const->g * muDoubleScalarSin(gam))) -
                      lamGAM * (b_const->g * muDoubleScalarCos(gam) / v -
        muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig)) *
        (b_const->g * b_const->mass + muDoubleScalarSin(b_const->alfamax *
        muDoubleScalarSin(alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) +
        1860.0)) / (b_const->mass * v))) + muDoubleScalarCos(gam) *
                     muDoubleScalarPower(H_t_minus + 1860.0, 5.2) / (v *
        muDoubleScalarPower(z + 50.0, 2.5))) + lamX * v * muDoubleScalarCos(gam)
                    * muDoubleScalarCos(psii)) + lamY * v * muDoubleScalarCos
                   (gam) * muDoubleScalarSin(psii)) + lamPSII *
        muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) *
        (b_const->g * b_const->mass + muDoubleScalarSin(b_const->alfamax *
          muDoubleScalarSin(alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) +
          1860.0)) / (b_const->mass * v * muDoubleScalarCos(gam));
      emlrtPopRtStackR2012b(&emlrtRSI, emlrtRootTLSGlobal);
    }

    emlrtBreakCheckFastR2012b(emlrtBreakCheckR2012bFlagVar, emlrtRootTLSGlobal);
  }

  memcpy(&zeroVec[0], &xAndLambda0Constraint[0], 12U * sizeof(real_T));
  memcpy(&zeroVec[12], &xAndLambdaFConstraint[0], 12U * sizeof(real_T));
  zeroVec[24] = H_t_minus;
}

void eml_error(void)
{
  emlrtPushRtStackR2012b(&qc_emlrtRSI, emlrtRootTLSGlobal);
  emlrtErrorWithMessageIdR2012b(emlrtRootTLSGlobal, &emlrtRTEI,
    "Coder:toolbox:power_domainError", 0);
  emlrtPopRtStackR2012b(&qc_emlrtRSI, emlrtRootTLSGlobal);
}

/* End of code generation (bc.c) */
