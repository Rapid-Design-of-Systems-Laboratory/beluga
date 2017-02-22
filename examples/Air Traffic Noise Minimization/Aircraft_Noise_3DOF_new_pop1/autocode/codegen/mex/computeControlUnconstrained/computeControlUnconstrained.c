/*
 * computeControlUnconstrained.c
 *
 * Code generation for function 'computeControlUnconstrained'
 *
 * C source code generated on: Sat Jan 21 02:01:19 2017
 *
 */

/* Include files */
#include "rt_nonfinite.h"
#include "computeControlUnconstrained.h"
#include "mpower.h"
#include "cos.h"
#include "sin.h"
#include "asin.h"
#include "acos.h"
#include "sec.h"

/* Variable Definitions */
static emlrtRSInfo emlrtRSI = { 113, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo b_emlrtRSI = { 135, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo c_emlrtRSI = { 201, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo d_emlrtRSI = { 223, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo e_emlrtRSI = { 289, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo f_emlrtRSI = { 311, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo g_emlrtRSI = { 377, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo h_emlrtRSI = { 399, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo i_emlrtRSI = { 465, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo j_emlrtRSI = { 487, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo k_emlrtRSI = { 553, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo l_emlrtRSI = { 575, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo m_emlrtRSI = { 641, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo n_emlrtRSI = { 663, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo o_emlrtRSI = { 729, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo p_emlrtRSI = { 751, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo q_emlrtRSI = { 817, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo r_emlrtRSI = { 839, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo s_emlrtRSI = { 905, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo t_emlrtRSI = { 927, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo u_emlrtRSI = { 993, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo v_emlrtRSI = { 1015, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo w_emlrtRSI = { 1081, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo x_emlrtRSI = { 1103, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo y_emlrtRSI = { 1139, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo ab_emlrtRSI = { 1161, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo bb_emlrtRSI = { 1169, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo cb_emlrtRSI = { 1183, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo db_emlrtRSI = { 1191, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo eb_emlrtRSI = { 1205, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo fb_emlrtRSI = { 1227, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo gb_emlrtRSI = { 1249, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo hb_emlrtRSI = { 1257, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo ib_emlrtRSI = { 1271, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo jb_emlrtRSI = { 1279, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo kb_emlrtRSI = { 1293, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo lb_emlrtRSI = { 1315, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo mb_emlrtRSI = { 1337, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo nb_emlrtRSI = { 1345, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo ob_emlrtRSI = { 1359, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo pb_emlrtRSI = { 1367, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo qb_emlrtRSI = { 1381, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo rb_emlrtRSI = { 1403, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo sb_emlrtRSI = { 1425, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo tb_emlrtRSI = { 1433, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo ub_emlrtRSI = { 1447, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo vb_emlrtRSI = { 1455, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo wb_emlrtRSI = { 1469, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo xb_emlrtRSI = { 1491, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo yb_emlrtRSI = { 1513, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo ac_emlrtRSI = { 1521, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo bc_emlrtRSI = { 1535, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo cc_emlrtRSI = { 1543, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo dc_emlrtRSI = { 1557, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo ec_emlrtRSI = { 1579, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo fc_emlrtRSI = { 1601, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo gc_emlrtRSI = { 1609, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo hc_emlrtRSI = { 1623, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo ic_emlrtRSI = { 1631, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo jc_emlrtRSI = { 1645, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

/* Function Definitions */
void computeControlUnconstrained(const real_T xAndLambda[12], const struct_T
  *b_const, real_T numArcs, real_T *banktrigSave, real_T *alfatrigSave, real_T
  *TtrignewSave, real_T *hamiltonianSave)
{
  creal_T psii;
  creal_T gam;
  creal_T dc0;
  creal_T a;
  creal_T dc1;
  creal_T dc2;
  creal_T dc3;
  creal_T dc4;
  creal_T dc5;
  creal_T dc6;
  creal_T dc7;
  creal_T v;
  real_T ar;
  real_T ai;
  real_T const_re;
  real_T const_im;
  real_T b_const_re;
  real_T b_const_im;
  creal_T c_const;
  creal_T z;
  real_T v_re;
  real_T v_im;
  real_T re;
  real_T brm;
  real_T bim;
  real_T b_v_re;
  real_T b_v_im;
  real_T lamX_re;
  real_T lamX_im;
  real_T lamY_re;
  real_T lamY_im;
  real_T hamiltonian;
  real_T c_const_im;
  real_T c_const_re;
  real_T d_const_re;
  real_T d_const_im;
  creal_T b_v;
  creal_T d_const;
  creal_T b_z;
  real_T c_v_re;
  real_T c_v_im;
  real_T e_const_re;
  real_T e_const_im;
  real_T banktrig;
  creal_T c_v;
  creal_T e_const;
  creal_T c_z;
  real_T d_v_re;
  real_T d_v_im;
  real_T f_const_re;
  real_T f_const_im;
  creal_T d_v;
  creal_T f_const;
  creal_T d_z;
  real_T e_v_re;
  real_T e_v_im;
  real_T g_const_re;
  real_T g_const_im;
  creal_T e_v;
  creal_T g_const;
  creal_T e_z;
  real_T f_v_re;
  real_T f_v_im;
  real_T h_const_re;
  real_T h_const_im;
  creal_T f_v;
  creal_T h_const;
  creal_T f_z;
  real_T g_v_re;
  real_T g_v_im;
  real_T i_const_re;
  real_T i_const_im;
  creal_T g_v;
  creal_T i_const;
  creal_T g_z;
  real_T h_v_re;
  real_T h_v_im;
  real_T j_const_re;
  real_T j_const_im;
  creal_T h_v;
  creal_T j_const;
  creal_T h_z;
  real_T i_v_re;
  real_T i_v_im;
  real_T k_const_re;
  real_T k_const_im;
  real_T Ttrignew;
  real_T alfatrig;
  creal_T i_v;
  creal_T k_const;
  creal_T i_z;
  real_T j_v_re;
  real_T j_v_im;
  real_T l_const_re;
  real_T l_const_im;
  creal_T j_v;
  creal_T l_const;
  creal_T j_z;
  real_T k_v_re;
  real_T k_v_im;
  real_T m_const_re;
  real_T m_const_im;
  creal_T k_v;
  creal_T m_const;
  creal_T k_z;
  real_T l_v_re;
  real_T l_v_im;
  real_T n_const_re;
  real_T n_const_im;
  creal_T l_v;
  creal_T n_const;
  creal_T l_z;
  real_T m_v_re;
  real_T m_v_im;
  real_T o_const_re;
  real_T o_const_im;
  creal_T m_v;
  creal_T o_const;
  creal_T m_z;
  real_T n_v_re;
  real_T n_v_im;
  real_T p_const_re;
  real_T p_const_im;
  creal_T n_v;
  creal_T p_const;
  creal_T n_z;
  real_T o_v_re;
  real_T o_v_im;
  real_T q_const_re;
  real_T q_const_im;
  creal_T o_v;
  creal_T q_const;
  creal_T o_z;
  real_T p_v_re;
  real_T p_v_im;
  real_T r_const_re;
  real_T r_const_im;
  creal_T p_v;
  creal_T r_const;
  creal_T p_z;
  real_T q_v_re;
  real_T q_v_im;
  real_T s_const_re;
  real_T s_const_im;
  creal_T q_v;
  creal_T s_const;
  creal_T q_z;
  real_T r_v_re;
  real_T r_v_im;
  real_T t_const_re;
  real_T t_const_im;
  creal_T r_v;
  creal_T t_const;
  creal_T r_z;
  real_T s_v_re;
  real_T s_v_im;
  real_T u_const_re;
  real_T u_const_im;
  creal_T s_v;
  creal_T u_const;
  creal_T s_z;
  real_T t_v_re;
  real_T t_v_im;
  real_T v_const_re;
  real_T v_const_im;
  creal_T t_v;
  creal_T v_const;
  creal_T t_z;
  real_T u_v_re;
  real_T u_v_im;
  real_T w_const_re;
  real_T w_const_im;
  creal_T u_v;
  creal_T w_const;
  creal_T u_z;
  real_T v_v_re;
  real_T v_v_im;
  real_T x_const_re;
  real_T x_const_im;
  creal_T v_v;
  creal_T x_const;
  creal_T v_z;
  real_T w_v_re;
  real_T w_v_im;
  real_T y_const_re;
  real_T y_const_im;
  creal_T w_v;
  creal_T y_const;
  creal_T w_z;
  real_T x_v_re;
  real_T x_v_im;
  real_T ab_const_re;
  real_T ab_const_im;
  creal_T x_v;
  creal_T ab_const;
  creal_T x_z;
  real_T y_v_re;
  real_T y_v_im;
  real_T bb_const_re;
  real_T bb_const_im;
  creal_T y_v;
  creal_T bb_const;
  creal_T y_z;
  real_T ab_v_re;
  real_T ab_v_im;
  real_T cb_const_re;
  real_T cb_const_im;
  creal_T ab_v;
  creal_T cb_const;
  creal_T ab_z;
  real_T bb_v_re;
  real_T bb_v_im;
  real_T db_const_re;
  real_T db_const_im;
  creal_T bb_v;
  creal_T db_const;
  creal_T bb_z;
  real_T cb_v_re;
  real_T cb_v_im;
  real_T eb_const_re;
  real_T eb_const_im;
  creal_T cb_v;
  creal_T eb_const;
  creal_T cb_z;
  real_T db_v_re;
  real_T db_v_im;
  real_T fb_const_re;
  real_T fb_const_im;
  creal_T db_v;
  creal_T fb_const;
  creal_T db_z;
  real_T eb_v_re;
  real_T eb_v_im;
  real_T gb_const_re;
  real_T gb_const_im;
  creal_T eb_v;
  creal_T gb_const;
  creal_T eb_z;
  real_T fb_v_re;
  real_T fb_v_im;
  real_T hb_const_re;
  real_T hb_const_im;
  creal_T fb_v;
  creal_T hb_const;
  creal_T fb_z;
  real_T gb_v_re;
  real_T gb_v_im;
  real_T ib_const_re;
  real_T ib_const_im;
  creal_T gb_v;
  creal_T ib_const;
  creal_T gb_z;
  real_T hb_v_re;
  real_T hb_v_im;
  real_T jb_const_re;
  real_T jb_const_im;
  creal_T hb_v;
  creal_T jb_const;
  creal_T hb_z;
  real_T ib_v_re;
  real_T ib_v_im;
  real_T kb_const_re;
  real_T kb_const_im;
  creal_T ib_v;
  creal_T kb_const;
  creal_T ib_z;
  real_T jb_v_re;
  real_T jb_v_im;
  real_T lb_const_re;
  real_T lb_const_im;
  creal_T jb_v;
  creal_T lb_const;
  creal_T jb_z;
  real_T kb_v_re;
  real_T kb_v_im;
  real_T mb_const_re;
  real_T mb_const_im;
  creal_T kb_v;
  creal_T mb_const;
  creal_T kb_z;
  real_T lb_v_re;
  real_T lb_v_im;
  real_T nb_const_re;
  real_T nb_const_im;
  creal_T lb_v;
  creal_T nb_const;
  creal_T lb_z;
  real_T mb_v_re;
  real_T mb_v_im;
  real_T ob_const_re;
  real_T ob_const_im;
  creal_T mb_v;
  creal_T ob_const;
  creal_T mb_z;
  real_T nb_v_re;
  real_T nb_v_im;
  real_T pb_const_re;
  real_T pb_const_im;
  creal_T nb_v;
  creal_T pb_const;
  creal_T nb_z;
  real_T ob_v_re;
  real_T ob_v_im;
  real_T qb_const_re;
  real_T qb_const_im;
  creal_T ob_v;
  creal_T qb_const;
  creal_T ob_z;
  real_T pb_v_re;
  real_T pb_v_im;
  real_T rb_const_re;
  real_T rb_const_im;
  creal_T pb_v;
  creal_T rb_const;
  creal_T pb_z;
  real_T qb_v_re;
  real_T qb_v_im;
  real_T sb_const_re;
  real_T sb_const_im;
  creal_T qb_v;
  creal_T sb_const;
  creal_T qb_z;
  real_T rb_v_re;
  real_T rb_v_im;
  real_T tb_const_re;
  real_T tb_const_im;
  creal_T rb_v;
  creal_T tb_const;
  creal_T rb_z;
  real_T sb_v_re;
  real_T sb_v_im;
  real_T ub_const_re;
  real_T ub_const_im;
  creal_T sb_v;
  creal_T ub_const;
  creal_T sb_z;
  real_T tb_v_re;
  real_T tb_v_im;
  real_T vb_const_re;
  real_T vb_const_im;
  creal_T tb_v;
  creal_T vb_const;
  creal_T tb_z;
  real_T ub_v_re;
  real_T ub_v_im;
  real_T wb_const_re;
  real_T wb_const_im;
  creal_T ub_v;
  creal_T wb_const;
  creal_T ub_z;
  real_T vb_v_re;
  real_T vb_v_im;
  real_T xb_const_re;
  real_T xb_const_im;
  creal_T vb_v;
  creal_T xb_const;
  creal_T vb_z;
  real_T wb_v_re;
  real_T wb_v_im;
  real_T yb_const_re;
  real_T yb_const_im;
  creal_T wb_v;
  creal_T yb_const;
  creal_T wb_z;
  real_T xb_v_re;
  real_T xb_v_im;
  real_T ac_const_re;
  real_T ac_const_im;
  creal_T xb_z;
  creal_T xb_v;
  creal_T yb_v;
  creal_T ac_const;
  creal_T yb_z;
  real_T yb_v_re;
  real_T yb_v_im;
  real_T bc_const_re;
  real_T bc_const_im;
  creal_T ac_z;
  creal_T ac_v;
  creal_T bc_v;
  creal_T bc_const;
  creal_T bc_z;
  real_T ac_v_re;
  real_T ac_v_im;
  real_T cc_const_re;
  real_T cc_const_im;
  creal_T cc_z;
  creal_T cc_v;
  creal_T dc_v;
  creal_T cc_const;
  creal_T dc_z;
  real_T bc_v_re;
  real_T bc_v_im;
  real_T dc_const_re;
  real_T dc_const_im;
  creal_T ec_z;
  creal_T ec_v;
  creal_T fc_v;
  creal_T dc_const;
  creal_T fc_z;
  real_T cc_v_re;
  real_T cc_v_im;
  real_T ec_const_re;
  real_T ec_const_im;
  creal_T gc_z;
  creal_T gc_v;
  creal_T hc_v;
  creal_T ec_const;
  creal_T hc_z;
  real_T dc_v_re;
  real_T dc_v_im;
  real_T fc_const_re;
  real_T fc_const_im;
  creal_T ic_z;
  creal_T ic_v;
  creal_T jc_v;
  creal_T fc_const;
  creal_T jc_z;
  real_T ec_v_re;
  real_T ec_v_im;
  real_T gc_const_re;
  real_T gc_const_im;
  creal_T kc_z;
  creal_T kc_v;
  creal_T lc_v;
  creal_T gc_const;
  creal_T lc_z;
  real_T fc_v_re;
  real_T fc_v_im;
  real_T hc_const_re;
  real_T hc_const_im;
  creal_T mc_z;
  creal_T mc_v;
  creal_T nc_v;
  creal_T hc_const;
  creal_T nc_z;
  real_T gc_v_re;
  real_T gc_v_im;
  real_T ic_const_re;
  real_T ic_const_im;
  creal_T oc_z;
  creal_T oc_v;
  creal_T pc_v;
  creal_T ic_const;
  creal_T pc_z;
  real_T hc_v_re;
  real_T hc_v_im;
  real_T jc_const_re;
  real_T jc_const_im;
  creal_T qc_z;
  creal_T qc_v;
  creal_T rc_v;
  creal_T jc_const;
  creal_T rc_z;
  real_T ic_v_re;
  real_T ic_v_im;
  real_T kc_const_re;
  real_T kc_const_im;
  creal_T sc_z;
  creal_T sc_v;
  creal_T tc_v;
  creal_T kc_const;
  creal_T tc_z;
  real_T jc_v_re;
  real_T jc_v_im;
  real_T lc_const_re;
  real_T lc_const_im;
  creal_T uc_z;
  creal_T uc_v;
  creal_T vc_v;
  creal_T lc_const;
  creal_T vc_z;
  real_T kc_v_re;
  real_T kc_v_im;
  real_T mc_const_re;
  real_T mc_const_im;
  creal_T wc_z;
  creal_T wc_v;
  creal_T xc_v;
  creal_T mc_const;
  creal_T xc_z;
  real_T lc_v_re;
  real_T lc_v_im;
  real_T nc_const_re;
  real_T nc_const_im;
  creal_T yc_z;
  creal_T yc_v;
  creal_T ad_v;
  creal_T nc_const;
  creal_T ad_z;
  real_T mc_v_re;
  real_T mc_v_im;
  real_T oc_const_re;
  real_T oc_const_im;
  creal_T bd_z;
  creal_T bd_v;
  creal_T cd_v;
  creal_T oc_const;
  creal_T cd_z;
  real_T nc_v_re;
  real_T nc_v_im;
  real_T pc_const_re;
  real_T pc_const_im;
  creal_T dd_z;
  creal_T dd_v;
  creal_T ed_v;
  creal_T pc_const;
  creal_T ed_z;
  real_T oc_v_re;
  real_T oc_v_im;
  real_T qc_const_re;
  real_T qc_const_im;
  creal_T fd_z;
  creal_T fd_v;
  creal_T gd_v;
  creal_T qc_const;
  creal_T gd_z;
  real_T pc_v_re;
  real_T pc_v_im;
  real_T rc_const_re;
  real_T rc_const_im;
  creal_T hd_z;
  creal_T hd_v;
  creal_T id_v;
  creal_T rc_const;
  creal_T id_z;
  real_T qc_v_re;
  real_T qc_v_im;
  real_T sc_const_re;
  real_T sc_const_im;
  creal_T jd_z;
  creal_T jd_v;
  creal_T kd_v;
  creal_T sc_const;
  creal_T kd_z;
  real_T rc_v_re;
  real_T rc_v_im;
  real_T tc_const_re;
  real_T tc_const_im;
  creal_T ld_z;
  creal_T ld_v;
  creal_T md_v;
  creal_T tc_const;
  creal_T md_z;
  real_T sc_v_re;
  real_T sc_v_im;
  real_T uc_const_re;
  real_T uc_const_im;
  creal_T nd_z;
  creal_T nd_v;
  creal_T od_v;
  creal_T uc_const;
  creal_T od_z;
  real_T tc_v_re;
  real_T tc_v_im;
  real_T vc_const_re;
  real_T vc_const_im;
  creal_T pd_z;
  creal_T pd_v;
  creal_T qd_v;
  creal_T vc_const;
  creal_T qd_z;
  real_T uc_v_re;
  real_T uc_v_im;
  real_T wc_const_re;
  real_T wc_const_im;
  creal_T rd_z;
  creal_T rd_v;
  creal_T sd_v;
  creal_T wc_const;
  creal_T sd_z;
  real_T vc_v_re;
  real_T vc_v_im;
  real_T xc_const_re;
  real_T xc_const_im;
  creal_T td_z;
  creal_T td_v;
  creal_T ud_v;
  creal_T xc_const;
  creal_T ud_z;
  real_T wc_v_re;
  real_T wc_v_im;
  real_T yc_const_re;
  real_T yc_const_im;

  /*  Constants */
  /*  States */
  psii.re = xAndLambda[4];
  psii.im = 0.0;
  gam.re = xAndLambda[5];
  gam.im = 0.0;

  /*  Costates */
  /*  Control */
  /*  Coefficients */
  /*  Coefficients */
  /*  Coefficients */
  *banktrigSave = -1.5707963267948966;
  *alfatrigSave = -1.5707963267948966;
  *TtrignewSave = 1.5707963267948966;
  dc0 = gam;
  b_sin(&dc0);
  a = psii;
  b_cos(&a);
  dc1 = psii;
  b_sin(&dc1);
  dc2 = gam;
  b_sin(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = gam;
  b_cos(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_cos(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  v.re = xAndLambda[3] * xAndLambda[3];
  v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(-b_const->alfamax) * 3420.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc3.re;
  ai = b_const->g * dc3.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  c_const.re = b_const->mass * xAndLambda[3];
  c_const.im = b_const->mass * 0.0;
  dc3 = eml_div(muDoubleScalarCos(-b_const->bankmax) * (b_const->g *
    b_const->mass + muDoubleScalarSin(-b_const->alfamax) * 3420.0), c_const);
  z.re = xAndLambda[2] + 50.0;
  z.im = 0.0;
  v = b_mpower(z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = dc4.re * 2.3819670606660884E+18;
  ai = dc4.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        b_v_re = 0.5;
      } else {
        b_v_re = -0.5;
      }

      if (v_im > 0.0) {
        b_v_im = 0.5;
      } else {
        b_v_im = -0.5;
      }

      re = (ar * b_v_re + ai * b_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc7.re - c_const_im * dc7.im;
  c_const_im = hamiltonian * dc7.im + c_const_im * dc7.re;
  ar = muDoubleScalarSin(-b_const->bankmax) * xAndLambda[10] * (b_const->g *
    b_const->mass + muDoubleScalarSin(-b_const->alfamax) * 3420.0);
  ai = muDoubleScalarSin(-b_const->bankmax) * 0.0 * (b_const->g * b_const->mass
    + muDoubleScalarSin(-b_const->alfamax) * 3420.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        d_const_re = 0.5;
      } else {
        d_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        d_const_im = 0.5;
      } else {
        d_const_im = -0.5;
      }

      bim = (ar * d_const_re + ai * d_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  *hamiltonianSave = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda
    [8] * 0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc2.re) - 0.0 * (const_im + b_const->g * dc2.im))) -
    (xAndLambda[11] * (b_const_re - dc3.re) - 0.0 * (b_const_im - dc3.im))) + re)
                       + ((lamX_re * dc5.re - lamX_im * dc5.im) * a.re -
    (lamX_re * dc5.im + lamX_im * dc5.re) * a.im)) + ((lamY_re * dc6.re -
    lamY_im * dc6.im) * dc1.re - (lamY_re * dc6.im + lamY_im * dc6.re) * dc1.im))
    + bim;

  /*  Coefficients */
  /*  Coefficients */
  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  b_v.re = xAndLambda[3] * xAndLambda[3];
  b_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, b_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(-b_const->alfamax) * 3420.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  d_const.re = b_const->mass * xAndLambda[3];
  d_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax) * (b_const->g *
    b_const->mass + muDoubleScalarSin(-b_const->alfamax) * 3420.0), d_const);
  b_z.re = xAndLambda[2] + 50.0;
  b_z.im = 0.0;
  v = b_mpower(b_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        c_v_re = 0.5;
      } else {
        c_v_re = -0.5;
      }

      if (v_im > 0.0) {
        c_v_im = 0.5;
      } else {
        c_v_im = -0.5;
      }

      re = (ar * c_v_re + ai * c_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax) * xAndLambda[10] * (b_const->g *
    b_const->mass + muDoubleScalarSin(-b_const->alfamax) * 3420.0);
  ai = muDoubleScalarSin(b_const->bankmax) * 0.0 * (b_const->g * b_const->mass +
    muDoubleScalarSin(-b_const->alfamax) * 3420.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        e_const_re = 0.5;
      } else {
        e_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        e_const_im = 0.5;
      } else {
        e_const_im = -0.5;
      }

      bim = (ar * e_const_re + ai * e_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = 1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = 3.1416 / (2.0 * b_const->bankmax);
  b_asin(&hamiltonian);
  banktrig = -hamiltonian;
  emlrtPopRtStackR2012b(&emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(-hamiltonian) || muDoubleScalarIsInf(-hamiltonian)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  c_v.re = xAndLambda[3] * xAndLambda[3];
  c_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, c_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(-b_const->alfamax) * 3420.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  e_const.re = b_const->mass * xAndLambda[3];
  e_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig))
                * (b_const->g * b_const->mass + muDoubleScalarSin
                   (-b_const->alfamax) * 3420.0), e_const);
  c_z.re = xAndLambda[2] + 50.0;
  c_z.im = 0.0;
  v = b_mpower(c_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        d_v_re = 0.5;
      } else {
        d_v_re = -0.5;
      }

      if (v_im > 0.0) {
        d_v_im = 0.5;
      } else {
        d_v_im = -0.5;
      }

      re = (ar * d_v_re + ai * d_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda[10] * (b_const->g * b_const->mass + muDoubleScalarSin
                      (-b_const->alfamax) * 3420.0);
  ai = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (b_const->g * b_const->mass + muDoubleScalarSin(-b_const->alfamax) * 3420.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        f_const_re = 0.5;
      } else {
        f_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        f_const_im = 0.5;
      } else {
        f_const_im = -0.5;
      }

      bim = (ar * f_const_re + ai * f_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&b_emlrtRSI, emlrtRootTLSGlobal);
  banktrig = 3.1416 / (2.0 * b_const->bankmax);
  b_asin(&banktrig);
  emlrtPopRtStackR2012b(&b_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(banktrig) || muDoubleScalarIsInf(banktrig)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  d_v.re = xAndLambda[3] * xAndLambda[3];
  d_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, d_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(-b_const->alfamax) * 3420.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  f_const.re = b_const->mass * xAndLambda[3];
  f_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig))
                * (b_const->g * b_const->mass + muDoubleScalarSin
                   (-b_const->alfamax) * 3420.0), f_const);
  d_z.re = xAndLambda[2] + 50.0;
  d_z.im = 0.0;
  v = b_mpower(d_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        e_v_re = 0.5;
      } else {
        e_v_re = -0.5;
      }

      if (v_im > 0.0) {
        e_v_im = 0.5;
      } else {
        e_v_im = -0.5;
      }

      re = (ar * e_v_re + ai * e_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda[10] * (b_const->g * b_const->mass + muDoubleScalarSin
                      (-b_const->alfamax) * 3420.0);
  ai = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (b_const->g * b_const->mass + muDoubleScalarSin(-b_const->alfamax) * 3420.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        g_const_re = 0.5;
      } else {
        g_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        g_const_im = 0.5;
      } else {
        g_const_im = -0.5;
      }

      bim = (ar * g_const_re + ai * g_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  e_v.re = xAndLambda[3] * xAndLambda[3];
  e_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, e_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax) * 3420.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  g_const.re = b_const->mass * xAndLambda[3];
  g_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(-b_const->bankmax) * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax) * 3420.0), g_const);
  e_z.re = xAndLambda[2] + 50.0;
  e_z.im = 0.0;
  v = b_mpower(e_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        f_v_re = 0.5;
      } else {
        f_v_re = -0.5;
      }

      if (v_im > 0.0) {
        f_v_im = 0.5;
      } else {
        f_v_im = -0.5;
      }

      re = (ar * f_v_re + ai * f_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(-b_const->bankmax) * xAndLambda[10] * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax) * 3420.0);
  ai = muDoubleScalarSin(-b_const->bankmax) * 0.0 * (b_const->g * b_const->mass
    + muDoubleScalarSin(b_const->alfamax) * 3420.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        h_const_re = 0.5;
      } else {
        h_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        h_const_im = 0.5;
      } else {
        h_const_im = -0.5;
      }

      bim = (ar * h_const_re + ai * h_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = -1.5707963267948966;
    *alfatrigSave = 1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  f_v.re = xAndLambda[3] * xAndLambda[3];
  f_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, f_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax) * 3420.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  h_const.re = b_const->mass * xAndLambda[3];
  h_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax) * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax) * 3420.0), h_const);
  f_z.re = xAndLambda[2] + 50.0;
  f_z.im = 0.0;
  v = b_mpower(f_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        g_v_re = 0.5;
      } else {
        g_v_re = -0.5;
      }

      if (v_im > 0.0) {
        g_v_im = 0.5;
      } else {
        g_v_im = -0.5;
      }

      re = (ar * g_v_re + ai * g_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax) * xAndLambda[10] * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax) * 3420.0);
  ai = muDoubleScalarSin(b_const->bankmax) * 0.0 * (b_const->g * b_const->mass +
    muDoubleScalarSin(b_const->alfamax) * 3420.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        i_const_re = 0.5;
      } else {
        i_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        i_const_im = 0.5;
      } else {
        i_const_im = -0.5;
      }

      bim = (ar * i_const_re + ai * i_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = 1.5707963267948966;
    *alfatrigSave = 1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&c_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = 3.1416 / (2.0 * b_const->bankmax);
  b_asin(&hamiltonian);
  banktrig = -hamiltonian;
  emlrtPopRtStackR2012b(&c_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(-hamiltonian) || muDoubleScalarIsInf(-hamiltonian)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  g_v.re = xAndLambda[3] * xAndLambda[3];
  g_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, g_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax) * 3420.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  i_const.re = b_const->mass * xAndLambda[3];
  i_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig))
                * (b_const->g * b_const->mass + muDoubleScalarSin
                   (b_const->alfamax) * 3420.0), i_const);
  g_z.re = xAndLambda[2] + 50.0;
  g_z.im = 0.0;
  v = b_mpower(g_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        h_v_re = 0.5;
      } else {
        h_v_re = -0.5;
      }

      if (v_im > 0.0) {
        h_v_im = 0.5;
      } else {
        h_v_im = -0.5;
      }

      re = (ar * h_v_re + ai * h_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda[10] * (b_const->g * b_const->mass + muDoubleScalarSin
                      (b_const->alfamax) * 3420.0);
  ai = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (b_const->g * b_const->mass + muDoubleScalarSin(b_const->alfamax) * 3420.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        j_const_re = 0.5;
      } else {
        j_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        j_const_im = 0.5;
      } else {
        j_const_im = -0.5;
      }

      bim = (ar * j_const_re + ai * j_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = 1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&d_emlrtRSI, emlrtRootTLSGlobal);
  banktrig = 3.1416 / (2.0 * b_const->bankmax);
  b_asin(&banktrig);
  emlrtPopRtStackR2012b(&d_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(banktrig) || muDoubleScalarIsInf(banktrig)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  h_v.re = xAndLambda[3] * xAndLambda[3];
  h_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, h_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax) * 3420.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  j_const.re = b_const->mass * xAndLambda[3];
  j_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig))
                * (b_const->g * b_const->mass + muDoubleScalarSin
                   (b_const->alfamax) * 3420.0), j_const);
  h_z.re = xAndLambda[2] + 50.0;
  h_z.im = 0.0;
  v = b_mpower(h_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        i_v_re = 0.5;
      } else {
        i_v_re = -0.5;
      }

      if (v_im > 0.0) {
        i_v_im = 0.5;
      } else {
        i_v_im = -0.5;
      }

      re = (ar * i_v_re + ai * i_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda[10] * (b_const->g * b_const->mass + muDoubleScalarSin
                      (b_const->alfamax) * 3420.0);
  ai = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (b_const->g * b_const->mass + muDoubleScalarSin(b_const->alfamax) * 3420.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        k_const_re = 0.5;
      } else {
        k_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        k_const_im = 0.5;
      } else {
        k_const_im = -0.5;
      }

      bim = (ar * k_const_re + ai * k_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = 1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(-b_const->bankmax);
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(-b_const->bankmax);
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(-(2.0 * b_const->bankmax));
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(-(2.0 * b_const->bankmax));
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew = 0.0;
    } else if (b_const_im == 0.0) {
      hamiltonian = 0.0;
      Ttrignew /= dc0.re;
    } else {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = 0.0;
    } else if (Ttrignew == 0.0) {
      hamiltonian = 0.0;
      Ttrignew = -(b_const_im / dc0.im);
    } else {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = -(b_const_im / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      hamiltonian = (b_const_im + bim * Ttrignew) / c_const_re;
      Ttrignew = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      hamiltonian = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      Ttrignew = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      hamiltonian = (bim * b_const_im + Ttrignew) / c_const_re;
      Ttrignew = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -Ttrignew;
  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = -dc0.re;
  if (muDoubleScalarIsNaN(-dc0.re) || muDoubleScalarIsInf(-dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  i_v.re = xAndLambda[3] * xAndLambda[3];
  i_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, i_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 3420.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  k_const.re = b_const->mass * xAndLambda[3];
  k_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(-b_const->bankmax) * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * 3420.0), k_const);
  i_z.re = xAndLambda[2] + 50.0;
  i_z.im = 0.0;
  v = b_mpower(i_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        j_v_re = 0.5;
      } else {
        j_v_re = -0.5;
      }

      if (v_im > 0.0) {
        j_v_im = 0.5;
      } else {
        j_v_im = -0.5;
      }

      re = (ar * j_v_re + ai * j_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(-b_const->bankmax) * xAndLambda[10] * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * 3420.0);
  ai = muDoubleScalarSin(-b_const->bankmax) * 0.0 * (b_const->g * b_const->mass
    + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 3420.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        l_const_re = 0.5;
      } else {
        l_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        l_const_im = 0.5;
      } else {
        l_const_im = -0.5;
      }

      bim = (ar * l_const_re + ai * l_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = -1.5707963267948966;
    *alfatrigSave = alfatrig;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(b_const->bankmax);
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(b_const->bankmax);
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(2.0 * b_const->bankmax);
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(2.0 * b_const->bankmax);
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew = 0.0;
    } else if (b_const_im == 0.0) {
      hamiltonian = 0.0;
      Ttrignew /= dc0.re;
    } else {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = 0.0;
    } else if (Ttrignew == 0.0) {
      hamiltonian = 0.0;
      Ttrignew = -(b_const_im / dc0.im);
    } else {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = -(b_const_im / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      hamiltonian = (b_const_im + bim * Ttrignew) / c_const_re;
      Ttrignew = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      hamiltonian = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      Ttrignew = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      hamiltonian = (bim * b_const_im + Ttrignew) / c_const_re;
      Ttrignew = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -Ttrignew;
  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = -dc0.re;
  if (muDoubleScalarIsNaN(-dc0.re) || muDoubleScalarIsInf(-dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  j_v.re = xAndLambda[3] * xAndLambda[3];
  j_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, j_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 3420.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  l_const.re = b_const->mass * xAndLambda[3];
  l_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax) * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * 3420.0), l_const);
  j_z.re = xAndLambda[2] + 50.0;
  j_z.im = 0.0;
  v = b_mpower(j_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        k_v_re = 0.5;
      } else {
        k_v_re = -0.5;
      }

      if (v_im > 0.0) {
        k_v_im = 0.5;
      } else {
        k_v_im = -0.5;
      }

      re = (ar * k_v_re + ai * k_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax) * xAndLambda[10] * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * 3420.0);
  ai = muDoubleScalarSin(b_const->bankmax) * 0.0 * (b_const->g * b_const->mass +
    muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 3420.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        m_const_re = 0.5;
      } else {
        m_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        m_const_im = 0.5;
      } else {
        m_const_im = -0.5;
      }

      bim = (ar * m_const_re + ai * m_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = 1.5707963267948966;
    *alfatrigSave = alfatrig;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&e_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = 3.1416 / (2.0 * b_const->bankmax);
  b_asin(&hamiltonian);
  banktrig = -hamiltonian;
  emlrtPopRtStackR2012b(&e_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(-hamiltonian) || muDoubleScalarIsInf(-hamiltonian)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(2.0 * b_const->bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(2.0 * b_const->bankmax * muDoubleScalarSin(banktrig));
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew = 0.0;
    } else if (b_const_im == 0.0) {
      hamiltonian = 0.0;
      Ttrignew /= dc0.re;
    } else {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = 0.0;
    } else if (Ttrignew == 0.0) {
      hamiltonian = 0.0;
      Ttrignew = -(b_const_im / dc0.im);
    } else {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = -(b_const_im / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      hamiltonian = (b_const_im + bim * Ttrignew) / c_const_re;
      Ttrignew = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      hamiltonian = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      Ttrignew = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      hamiltonian = (bim * b_const_im + Ttrignew) / c_const_re;
      Ttrignew = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -Ttrignew;
  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = -dc0.re;
  if (muDoubleScalarIsNaN(-dc0.re) || muDoubleScalarIsInf(-dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  k_v.re = xAndLambda[3] * xAndLambda[3];
  k_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, k_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 3420.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  m_const.re = b_const->mass * xAndLambda[3];
  m_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig))
                * (b_const->g * b_const->mass + muDoubleScalarSin
                   (b_const->alfamax * muDoubleScalarSin(alfatrig)) * 3420.0),
                m_const);
  k_z.re = xAndLambda[2] + 50.0;
  k_z.im = 0.0;
  v = b_mpower(k_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        l_v_re = 0.5;
      } else {
        l_v_re = -0.5;
      }

      if (v_im > 0.0) {
        l_v_im = 0.5;
      } else {
        l_v_im = -0.5;
      }

      re = (ar * l_v_re + ai * l_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda[10] * (b_const->g * b_const->mass + muDoubleScalarSin
                      (b_const->alfamax * muDoubleScalarSin(alfatrig)) * 3420.0);
  ai = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (b_const->g * b_const->mass + muDoubleScalarSin(b_const->alfamax *
      muDoubleScalarSin(alfatrig)) * 3420.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        n_const_re = 0.5;
      } else {
        n_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        n_const_im = 0.5;
      } else {
        n_const_im = -0.5;
      }

      bim = (ar * n_const_re + ai * n_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&f_emlrtRSI, emlrtRootTLSGlobal);
  banktrig = 3.1416 / (2.0 * b_const->bankmax);
  b_asin(&banktrig);
  emlrtPopRtStackR2012b(&f_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(banktrig) || muDoubleScalarIsInf(banktrig)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(2.0 * b_const->bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(2.0 * b_const->bankmax * muDoubleScalarSin(banktrig));
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew = 0.0;
    } else if (b_const_im == 0.0) {
      hamiltonian = 0.0;
      Ttrignew /= dc0.re;
    } else {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = 0.0;
    } else if (Ttrignew == 0.0) {
      hamiltonian = 0.0;
      Ttrignew = -(b_const_im / dc0.im);
    } else {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = -(b_const_im / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      hamiltonian = (b_const_im + bim * Ttrignew) / c_const_re;
      Ttrignew = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      hamiltonian = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      Ttrignew = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      hamiltonian = (bim * b_const_im + Ttrignew) / c_const_re;
      Ttrignew = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -Ttrignew;
  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = -dc0.re;
  if (muDoubleScalarIsNaN(-dc0.re) || muDoubleScalarIsInf(-dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  l_v.re = xAndLambda[3] * xAndLambda[3];
  l_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, l_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 3420.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  n_const.re = b_const->mass * xAndLambda[3];
  n_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig))
                * (b_const->g * b_const->mass + muDoubleScalarSin
                   (b_const->alfamax * muDoubleScalarSin(alfatrig)) * 3420.0),
                n_const);
  l_z.re = xAndLambda[2] + 50.0;
  l_z.im = 0.0;
  v = b_mpower(l_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        m_v_re = 0.5;
      } else {
        m_v_re = -0.5;
      }

      if (v_im > 0.0) {
        m_v_im = 0.5;
      } else {
        m_v_im = -0.5;
      }

      re = (ar * m_v_re + ai * m_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda[10] * (b_const->g * b_const->mass + muDoubleScalarSin
                      (b_const->alfamax * muDoubleScalarSin(alfatrig)) * 3420.0);
  ai = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (b_const->g * b_const->mass + muDoubleScalarSin(b_const->alfamax *
      muDoubleScalarSin(alfatrig)) * 3420.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        o_const_re = 0.5;
      } else {
        o_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        o_const_im = 0.5;
      } else {
        o_const_im = -0.5;
      }

      bim = (ar * o_const_re + ai * o_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(-b_const->bankmax);
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(-b_const->bankmax);
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(-(2.0 * b_const->bankmax));
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(-(2.0 * b_const->bankmax));
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew = 0.0;
    } else if (b_const_im == 0.0) {
      hamiltonian = 0.0;
      Ttrignew /= dc0.re;
    } else {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = 0.0;
    } else if (Ttrignew == 0.0) {
      hamiltonian = 0.0;
      Ttrignew = -(b_const_im / dc0.im);
    } else {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = -(b_const_im / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      hamiltonian = (b_const_im + bim * Ttrignew) / c_const_re;
      Ttrignew = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      hamiltonian = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      Ttrignew = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      hamiltonian = (bim * b_const_im + Ttrignew) / c_const_re;
      Ttrignew = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -Ttrignew;
  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  m_v.re = xAndLambda[3] * xAndLambda[3];
  m_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, m_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 3420.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  o_const.re = b_const->mass * xAndLambda[3];
  o_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(-b_const->bankmax) * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * 3420.0), o_const);
  m_z.re = xAndLambda[2] + 50.0;
  m_z.im = 0.0;
  v = b_mpower(m_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        n_v_re = 0.5;
      } else {
        n_v_re = -0.5;
      }

      if (v_im > 0.0) {
        n_v_im = 0.5;
      } else {
        n_v_im = -0.5;
      }

      re = (ar * n_v_re + ai * n_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(-b_const->bankmax) * xAndLambda[10] * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * 3420.0);
  ai = muDoubleScalarSin(-b_const->bankmax) * 0.0 * (b_const->g * b_const->mass
    + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 3420.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        p_const_re = 0.5;
      } else {
        p_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        p_const_im = 0.5;
      } else {
        p_const_im = -0.5;
      }

      bim = (ar * p_const_re + ai * p_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = -1.5707963267948966;
    *alfatrigSave = alfatrig;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(b_const->bankmax);
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(b_const->bankmax);
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(2.0 * b_const->bankmax);
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(2.0 * b_const->bankmax);
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew = 0.0;
    } else if (b_const_im == 0.0) {
      hamiltonian = 0.0;
      Ttrignew /= dc0.re;
    } else {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = 0.0;
    } else if (Ttrignew == 0.0) {
      hamiltonian = 0.0;
      Ttrignew = -(b_const_im / dc0.im);
    } else {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = -(b_const_im / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      hamiltonian = (b_const_im + bim * Ttrignew) / c_const_re;
      Ttrignew = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      hamiltonian = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      Ttrignew = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      hamiltonian = (bim * b_const_im + Ttrignew) / c_const_re;
      Ttrignew = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -Ttrignew;
  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  n_v.re = xAndLambda[3] * xAndLambda[3];
  n_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, n_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 3420.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  p_const.re = b_const->mass * xAndLambda[3];
  p_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax) * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * 3420.0), p_const);
  n_z.re = xAndLambda[2] + 50.0;
  n_z.im = 0.0;
  v = b_mpower(n_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        o_v_re = 0.5;
      } else {
        o_v_re = -0.5;
      }

      if (v_im > 0.0) {
        o_v_im = 0.5;
      } else {
        o_v_im = -0.5;
      }

      re = (ar * o_v_re + ai * o_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax) * xAndLambda[10] * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * 3420.0);
  ai = muDoubleScalarSin(b_const->bankmax) * 0.0 * (b_const->g * b_const->mass +
    muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 3420.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        q_const_re = 0.5;
      } else {
        q_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        q_const_im = 0.5;
      } else {
        q_const_im = -0.5;
      }

      bim = (ar * q_const_re + ai * q_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = 1.5707963267948966;
    *alfatrigSave = alfatrig;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&g_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = 3.1416 / (2.0 * b_const->bankmax);
  b_asin(&hamiltonian);
  banktrig = -hamiltonian;
  emlrtPopRtStackR2012b(&g_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(-hamiltonian) || muDoubleScalarIsInf(-hamiltonian)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(2.0 * b_const->bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(2.0 * b_const->bankmax * muDoubleScalarSin(banktrig));
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew = 0.0;
    } else if (b_const_im == 0.0) {
      hamiltonian = 0.0;
      Ttrignew /= dc0.re;
    } else {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = 0.0;
    } else if (Ttrignew == 0.0) {
      hamiltonian = 0.0;
      Ttrignew = -(b_const_im / dc0.im);
    } else {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = -(b_const_im / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      hamiltonian = (b_const_im + bim * Ttrignew) / c_const_re;
      Ttrignew = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      hamiltonian = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      Ttrignew = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      hamiltonian = (bim * b_const_im + Ttrignew) / c_const_re;
      Ttrignew = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -Ttrignew;
  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  o_v.re = xAndLambda[3] * xAndLambda[3];
  o_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, o_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 3420.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  q_const.re = b_const->mass * xAndLambda[3];
  q_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig))
                * (b_const->g * b_const->mass + muDoubleScalarSin
                   (b_const->alfamax * muDoubleScalarSin(alfatrig)) * 3420.0),
                q_const);
  o_z.re = xAndLambda[2] + 50.0;
  o_z.im = 0.0;
  v = b_mpower(o_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        p_v_re = 0.5;
      } else {
        p_v_re = -0.5;
      }

      if (v_im > 0.0) {
        p_v_im = 0.5;
      } else {
        p_v_im = -0.5;
      }

      re = (ar * p_v_re + ai * p_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda[10] * (b_const->g * b_const->mass + muDoubleScalarSin
                      (b_const->alfamax * muDoubleScalarSin(alfatrig)) * 3420.0);
  ai = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (b_const->g * b_const->mass + muDoubleScalarSin(b_const->alfamax *
      muDoubleScalarSin(alfatrig)) * 3420.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        r_const_re = 0.5;
      } else {
        r_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        r_const_im = 0.5;
      } else {
        r_const_im = -0.5;
      }

      bim = (ar * r_const_re + ai * r_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&h_emlrtRSI, emlrtRootTLSGlobal);
  banktrig = 3.1416 / (2.0 * b_const->bankmax);
  b_asin(&banktrig);
  emlrtPopRtStackR2012b(&h_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(banktrig) || muDoubleScalarIsInf(banktrig)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(2.0 * b_const->bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(2.0 * b_const->bankmax * muDoubleScalarSin(banktrig));
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew = 0.0;
    } else if (b_const_im == 0.0) {
      hamiltonian = 0.0;
      Ttrignew /= dc0.re;
    } else {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = 0.0;
    } else if (Ttrignew == 0.0) {
      hamiltonian = 0.0;
      Ttrignew = -(b_const_im / dc0.im);
    } else {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = -(b_const_im / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      hamiltonian = (b_const_im + bim * Ttrignew) / c_const_re;
      Ttrignew = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      hamiltonian = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      Ttrignew = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      hamiltonian = (bim * b_const_im + Ttrignew) / c_const_re;
      Ttrignew = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -Ttrignew;
  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  p_v.re = xAndLambda[3] * xAndLambda[3];
  p_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, p_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 3420.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  r_const.re = b_const->mass * xAndLambda[3];
  r_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig))
                * (b_const->g * b_const->mass + muDoubleScalarSin
                   (b_const->alfamax * muDoubleScalarSin(alfatrig)) * 3420.0),
                r_const);
  p_z.re = xAndLambda[2] + 50.0;
  p_z.im = 0.0;
  v = b_mpower(p_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        q_v_re = 0.5;
      } else {
        q_v_re = -0.5;
      }

      if (v_im > 0.0) {
        q_v_im = 0.5;
      } else {
        q_v_im = -0.5;
      }

      re = (ar * q_v_re + ai * q_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda[10] * (b_const->g * b_const->mass + muDoubleScalarSin
                      (b_const->alfamax * muDoubleScalarSin(alfatrig)) * 3420.0);
  ai = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (b_const->g * b_const->mass + muDoubleScalarSin(b_const->alfamax *
      muDoubleScalarSin(alfatrig)) * 3420.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        s_const_re = 0.5;
      } else {
        s_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        s_const_im = 0.5;
      } else {
        s_const_im = -0.5;
      }

      bim = (ar * s_const_re + ai * s_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(-b_const->bankmax);
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(-b_const->bankmax);
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(-(2.0 * b_const->bankmax));
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(-(2.0 * b_const->bankmax));
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  re = dc0.re;
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      dc0.re = b_const_im / dc0.re;
      dc0.im = 0.0;
    } else if (b_const_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = Ttrignew / re;
    } else {
      dc0.re = b_const_im / dc0.re;
      dc0.im = Ttrignew / re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = 0.0;
    } else if (Ttrignew == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(b_const_im / lamY_im);
    } else {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = -(b_const_im / lamY_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      dc0.re = (b_const_im + bim * Ttrignew) / c_const_re;
      dc0.im = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      dc0.re = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      dc0.im = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      dc0.re = (bim * b_const_im + Ttrignew) / c_const_re;
      dc0.im = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = -dc0.re;
  if (muDoubleScalarIsNaN(-dc0.re) || muDoubleScalarIsInf(-dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  q_v.re = xAndLambda[3] * xAndLambda[3];
  q_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, q_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 3420.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  s_const.re = b_const->mass * xAndLambda[3];
  s_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(-b_const->bankmax) * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * 3420.0), s_const);
  q_z.re = xAndLambda[2] + 50.0;
  q_z.im = 0.0;
  v = b_mpower(q_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        r_v_re = 0.5;
      } else {
        r_v_re = -0.5;
      }

      if (v_im > 0.0) {
        r_v_im = 0.5;
      } else {
        r_v_im = -0.5;
      }

      re = (ar * r_v_re + ai * r_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(-b_const->bankmax) * xAndLambda[10] * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * 3420.0);
  ai = muDoubleScalarSin(-b_const->bankmax) * 0.0 * (b_const->g * b_const->mass
    + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 3420.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        t_const_re = 0.5;
      } else {
        t_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        t_const_im = 0.5;
      } else {
        t_const_im = -0.5;
      }

      bim = (ar * t_const_re + ai * t_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = -1.5707963267948966;
    *alfatrigSave = alfatrig;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(b_const->bankmax);
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(b_const->bankmax);
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(2.0 * b_const->bankmax);
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(2.0 * b_const->bankmax);
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  re = dc0.re;
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      dc0.re = b_const_im / dc0.re;
      dc0.im = 0.0;
    } else if (b_const_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = Ttrignew / re;
    } else {
      dc0.re = b_const_im / dc0.re;
      dc0.im = Ttrignew / re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = 0.0;
    } else if (Ttrignew == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(b_const_im / lamY_im);
    } else {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = -(b_const_im / lamY_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      dc0.re = (b_const_im + bim * Ttrignew) / c_const_re;
      dc0.im = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      dc0.re = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      dc0.im = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      dc0.re = (bim * b_const_im + Ttrignew) / c_const_re;
      dc0.im = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = -dc0.re;
  if (muDoubleScalarIsNaN(-dc0.re) || muDoubleScalarIsInf(-dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  r_v.re = xAndLambda[3] * xAndLambda[3];
  r_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, r_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 3420.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  t_const.re = b_const->mass * xAndLambda[3];
  t_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax) * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * 3420.0), t_const);
  r_z.re = xAndLambda[2] + 50.0;
  r_z.im = 0.0;
  v = b_mpower(r_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        s_v_re = 0.5;
      } else {
        s_v_re = -0.5;
      }

      if (v_im > 0.0) {
        s_v_im = 0.5;
      } else {
        s_v_im = -0.5;
      }

      re = (ar * s_v_re + ai * s_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax) * xAndLambda[10] * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * 3420.0);
  ai = muDoubleScalarSin(b_const->bankmax) * 0.0 * (b_const->g * b_const->mass +
    muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 3420.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        u_const_re = 0.5;
      } else {
        u_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        u_const_im = 0.5;
      } else {
        u_const_im = -0.5;
      }

      bim = (ar * u_const_re + ai * u_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = 1.5707963267948966;
    *alfatrigSave = alfatrig;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&i_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = 3.1416 / (2.0 * b_const->bankmax);
  b_asin(&hamiltonian);
  banktrig = -hamiltonian;
  emlrtPopRtStackR2012b(&i_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(-hamiltonian) || muDoubleScalarIsInf(-hamiltonian)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(2.0 * b_const->bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(2.0 * b_const->bankmax * muDoubleScalarSin(banktrig));
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  re = dc0.re;
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      dc0.re = b_const_im / dc0.re;
      dc0.im = 0.0;
    } else if (b_const_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = Ttrignew / re;
    } else {
      dc0.re = b_const_im / dc0.re;
      dc0.im = Ttrignew / re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = 0.0;
    } else if (Ttrignew == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(b_const_im / lamY_im);
    } else {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = -(b_const_im / lamY_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      dc0.re = (b_const_im + bim * Ttrignew) / c_const_re;
      dc0.im = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      dc0.re = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      dc0.im = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      dc0.re = (bim * b_const_im + Ttrignew) / c_const_re;
      dc0.im = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = -dc0.re;
  if (muDoubleScalarIsNaN(-dc0.re) || muDoubleScalarIsInf(-dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  s_v.re = xAndLambda[3] * xAndLambda[3];
  s_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, s_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 3420.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  u_const.re = b_const->mass * xAndLambda[3];
  u_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig))
                * (b_const->g * b_const->mass + muDoubleScalarSin
                   (b_const->alfamax * muDoubleScalarSin(alfatrig)) * 3420.0),
                u_const);
  s_z.re = xAndLambda[2] + 50.0;
  s_z.im = 0.0;
  v = b_mpower(s_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        t_v_re = 0.5;
      } else {
        t_v_re = -0.5;
      }

      if (v_im > 0.0) {
        t_v_im = 0.5;
      } else {
        t_v_im = -0.5;
      }

      re = (ar * t_v_re + ai * t_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda[10] * (b_const->g * b_const->mass + muDoubleScalarSin
                      (b_const->alfamax * muDoubleScalarSin(alfatrig)) * 3420.0);
  ai = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (b_const->g * b_const->mass + muDoubleScalarSin(b_const->alfamax *
      muDoubleScalarSin(alfatrig)) * 3420.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        v_const_re = 0.5;
      } else {
        v_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        v_const_im = 0.5;
      } else {
        v_const_im = -0.5;
      }

      bim = (ar * v_const_re + ai * v_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&j_emlrtRSI, emlrtRootTLSGlobal);
  banktrig = 3.1416 / (2.0 * b_const->bankmax);
  b_asin(&banktrig);
  emlrtPopRtStackR2012b(&j_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(banktrig) || muDoubleScalarIsInf(banktrig)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(2.0 * b_const->bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(2.0 * b_const->bankmax * muDoubleScalarSin(banktrig));
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  re = dc0.re;
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      dc0.re = b_const_im / dc0.re;
      dc0.im = 0.0;
    } else if (b_const_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = Ttrignew / re;
    } else {
      dc0.re = b_const_im / dc0.re;
      dc0.im = Ttrignew / re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = 0.0;
    } else if (Ttrignew == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(b_const_im / lamY_im);
    } else {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = -(b_const_im / lamY_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      dc0.re = (b_const_im + bim * Ttrignew) / c_const_re;
      dc0.im = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      dc0.re = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      dc0.im = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      dc0.re = (bim * b_const_im + Ttrignew) / c_const_re;
      dc0.im = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = -dc0.re;
  if (muDoubleScalarIsNaN(-dc0.re) || muDoubleScalarIsInf(-dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  t_v.re = xAndLambda[3] * xAndLambda[3];
  t_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, t_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 3420.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  v_const.re = b_const->mass * xAndLambda[3];
  v_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig))
                * (b_const->g * b_const->mass + muDoubleScalarSin
                   (b_const->alfamax * muDoubleScalarSin(alfatrig)) * 3420.0),
                v_const);
  t_z.re = xAndLambda[2] + 50.0;
  t_z.im = 0.0;
  v = b_mpower(t_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        u_v_re = 0.5;
      } else {
        u_v_re = -0.5;
      }

      if (v_im > 0.0) {
        u_v_im = 0.5;
      } else {
        u_v_im = -0.5;
      }

      re = (ar * u_v_re + ai * u_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda[10] * (b_const->g * b_const->mass + muDoubleScalarSin
                      (b_const->alfamax * muDoubleScalarSin(alfatrig)) * 3420.0);
  ai = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (b_const->g * b_const->mass + muDoubleScalarSin(b_const->alfamax *
      muDoubleScalarSin(alfatrig)) * 3420.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        w_const_re = 0.5;
      } else {
        w_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        w_const_im = 0.5;
      } else {
        w_const_im = -0.5;
      }

      bim = (ar * w_const_re + ai * w_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(-b_const->bankmax);
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(-b_const->bankmax);
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(-(2.0 * b_const->bankmax));
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(-(2.0 * b_const->bankmax));
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  re = dc0.re;
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      dc0.re = b_const_im / dc0.re;
      dc0.im = 0.0;
    } else if (b_const_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = Ttrignew / re;
    } else {
      dc0.re = b_const_im / dc0.re;
      dc0.im = Ttrignew / re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = 0.0;
    } else if (Ttrignew == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(b_const_im / lamY_im);
    } else {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = -(b_const_im / lamY_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      dc0.re = (b_const_im + bim * Ttrignew) / c_const_re;
      dc0.im = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      dc0.re = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      dc0.im = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      dc0.re = (bim * b_const_im + Ttrignew) / c_const_re;
      dc0.im = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  u_v.re = xAndLambda[3] * xAndLambda[3];
  u_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, u_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 3420.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  w_const.re = b_const->mass * xAndLambda[3];
  w_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(-b_const->bankmax) * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * 3420.0), w_const);
  u_z.re = xAndLambda[2] + 50.0;
  u_z.im = 0.0;
  v = b_mpower(u_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        v_v_re = 0.5;
      } else {
        v_v_re = -0.5;
      }

      if (v_im > 0.0) {
        v_v_im = 0.5;
      } else {
        v_v_im = -0.5;
      }

      re = (ar * v_v_re + ai * v_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(-b_const->bankmax) * xAndLambda[10] * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * 3420.0);
  ai = muDoubleScalarSin(-b_const->bankmax) * 0.0 * (b_const->g * b_const->mass
    + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 3420.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        x_const_re = 0.5;
      } else {
        x_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        x_const_im = 0.5;
      } else {
        x_const_im = -0.5;
      }

      bim = (ar * x_const_re + ai * x_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = -1.5707963267948966;
    *alfatrigSave = alfatrig;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(b_const->bankmax);
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(b_const->bankmax);
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(2.0 * b_const->bankmax);
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(2.0 * b_const->bankmax);
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  re = dc0.re;
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      dc0.re = b_const_im / dc0.re;
      dc0.im = 0.0;
    } else if (b_const_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = Ttrignew / re;
    } else {
      dc0.re = b_const_im / dc0.re;
      dc0.im = Ttrignew / re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = 0.0;
    } else if (Ttrignew == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(b_const_im / lamY_im);
    } else {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = -(b_const_im / lamY_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      dc0.re = (b_const_im + bim * Ttrignew) / c_const_re;
      dc0.im = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      dc0.re = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      dc0.im = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      dc0.re = (bim * b_const_im + Ttrignew) / c_const_re;
      dc0.im = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  v_v.re = xAndLambda[3] * xAndLambda[3];
  v_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, v_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 3420.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  x_const.re = b_const->mass * xAndLambda[3];
  x_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax) * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * 3420.0), x_const);
  v_z.re = xAndLambda[2] + 50.0;
  v_z.im = 0.0;
  v = b_mpower(v_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        w_v_re = 0.5;
      } else {
        w_v_re = -0.5;
      }

      if (v_im > 0.0) {
        w_v_im = 0.5;
      } else {
        w_v_im = -0.5;
      }

      re = (ar * w_v_re + ai * w_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax) * xAndLambda[10] * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * 3420.0);
  ai = muDoubleScalarSin(b_const->bankmax) * 0.0 * (b_const->g * b_const->mass +
    muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 3420.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        y_const_re = 0.5;
      } else {
        y_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        y_const_im = 0.5;
      } else {
        y_const_im = -0.5;
      }

      bim = (ar * y_const_re + ai * y_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = 1.5707963267948966;
    *alfatrigSave = alfatrig;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&k_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = 3.1416 / (2.0 * b_const->bankmax);
  b_asin(&hamiltonian);
  banktrig = -hamiltonian;
  emlrtPopRtStackR2012b(&k_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(-hamiltonian) || muDoubleScalarIsInf(-hamiltonian)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(2.0 * b_const->bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(2.0 * b_const->bankmax * muDoubleScalarSin(banktrig));
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  re = dc0.re;
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      dc0.re = b_const_im / dc0.re;
      dc0.im = 0.0;
    } else if (b_const_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = Ttrignew / re;
    } else {
      dc0.re = b_const_im / dc0.re;
      dc0.im = Ttrignew / re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = 0.0;
    } else if (Ttrignew == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(b_const_im / lamY_im);
    } else {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = -(b_const_im / lamY_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      dc0.re = (b_const_im + bim * Ttrignew) / c_const_re;
      dc0.im = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      dc0.re = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      dc0.im = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      dc0.re = (bim * b_const_im + Ttrignew) / c_const_re;
      dc0.im = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  w_v.re = xAndLambda[3] * xAndLambda[3];
  w_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, w_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 3420.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  y_const.re = b_const->mass * xAndLambda[3];
  y_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig))
                * (b_const->g * b_const->mass + muDoubleScalarSin
                   (b_const->alfamax * muDoubleScalarSin(alfatrig)) * 3420.0),
                y_const);
  w_z.re = xAndLambda[2] + 50.0;
  w_z.im = 0.0;
  v = b_mpower(w_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        x_v_re = 0.5;
      } else {
        x_v_re = -0.5;
      }

      if (v_im > 0.0) {
        x_v_im = 0.5;
      } else {
        x_v_im = -0.5;
      }

      re = (ar * x_v_re + ai * x_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda[10] * (b_const->g * b_const->mass + muDoubleScalarSin
                      (b_const->alfamax * muDoubleScalarSin(alfatrig)) * 3420.0);
  ai = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (b_const->g * b_const->mass + muDoubleScalarSin(b_const->alfamax *
      muDoubleScalarSin(alfatrig)) * 3420.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        ab_const_re = 0.5;
      } else {
        ab_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        ab_const_im = 0.5;
      } else {
        ab_const_im = -0.5;
      }

      bim = (ar * ab_const_re + ai * ab_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&l_emlrtRSI, emlrtRootTLSGlobal);
  banktrig = 3.1416 / (2.0 * b_const->bankmax);
  b_asin(&banktrig);
  emlrtPopRtStackR2012b(&l_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(banktrig) || muDoubleScalarIsInf(banktrig)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(2.0 * b_const->bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(2.0 * b_const->bankmax * muDoubleScalarSin(banktrig));
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  re = dc0.re;
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      dc0.re = b_const_im / dc0.re;
      dc0.im = 0.0;
    } else if (b_const_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = Ttrignew / re;
    } else {
      dc0.re = b_const_im / dc0.re;
      dc0.im = Ttrignew / re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = 0.0;
    } else if (Ttrignew == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(b_const_im / lamY_im);
    } else {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = -(b_const_im / lamY_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      dc0.re = (b_const_im + bim * Ttrignew) / c_const_re;
      dc0.im = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      dc0.re = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      dc0.im = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      dc0.re = (bim * b_const_im + Ttrignew) / c_const_re;
      dc0.im = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  x_v.re = xAndLambda[3] * xAndLambda[3];
  x_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, x_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 3420.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  ab_const.re = b_const->mass * xAndLambda[3];
  ab_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig))
                * (b_const->g * b_const->mass + muDoubleScalarSin
                   (b_const->alfamax * muDoubleScalarSin(alfatrig)) * 3420.0),
                ab_const);
  x_z.re = xAndLambda[2] + 50.0;
  x_z.im = 0.0;
  v = b_mpower(x_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        y_v_re = 0.5;
      } else {
        y_v_re = -0.5;
      }

      if (v_im > 0.0) {
        y_v_im = 0.5;
      } else {
        y_v_im = -0.5;
      }

      re = (ar * y_v_re + ai * y_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda[10] * (b_const->g * b_const->mass + muDoubleScalarSin
                      (b_const->alfamax * muDoubleScalarSin(alfatrig)) * 3420.0);
  ai = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (b_const->g * b_const->mass + muDoubleScalarSin(b_const->alfamax *
      muDoubleScalarSin(alfatrig)) * 3420.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        bb_const_re = 0.5;
      } else {
        bb_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        bb_const_im = 0.5;
      } else {
        bb_const_im = -0.5;
      }

      bim = (ar * bb_const_re + ai * bb_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  y_v.re = xAndLambda[3] * xAndLambda[3];
  y_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, y_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(-b_const->alfamax) * 300.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  bb_const.re = b_const->mass * xAndLambda[3];
  bb_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(-b_const->bankmax) * (b_const->g *
    b_const->mass + muDoubleScalarSin(-b_const->alfamax) * 300.0), bb_const);
  y_z.re = xAndLambda[2] + 50.0;
  y_z.im = 0.0;
  v = b_mpower(y_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        ab_v_re = 0.5;
      } else {
        ab_v_re = -0.5;
      }

      if (v_im > 0.0) {
        ab_v_im = 0.5;
      } else {
        ab_v_im = -0.5;
      }

      re = (ar * ab_v_re + ai * ab_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(-b_const->bankmax) * xAndLambda[10] * (b_const->g *
    b_const->mass + muDoubleScalarSin(-b_const->alfamax) * 300.0);
  ai = muDoubleScalarSin(-b_const->bankmax) * 0.0 * (b_const->g * b_const->mass
    + muDoubleScalarSin(-b_const->alfamax) * 300.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        cb_const_re = 0.5;
      } else {
        cb_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        cb_const_im = 0.5;
      } else {
        cb_const_im = -0.5;
      }

      bim = (ar * cb_const_re + ai * cb_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = -1.5707963267948966;
    *alfatrigSave = -1.5707963267948966;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  ab_v.re = xAndLambda[3] * xAndLambda[3];
  ab_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, ab_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(-b_const->alfamax) * 300.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  cb_const.re = b_const->mass * xAndLambda[3];
  cb_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax) * (b_const->g *
    b_const->mass + muDoubleScalarSin(-b_const->alfamax) * 300.0), cb_const);
  ab_z.re = xAndLambda[2] + 50.0;
  ab_z.im = 0.0;
  v = b_mpower(ab_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        bb_v_re = 0.5;
      } else {
        bb_v_re = -0.5;
      }

      if (v_im > 0.0) {
        bb_v_im = 0.5;
      } else {
        bb_v_im = -0.5;
      }

      re = (ar * bb_v_re + ai * bb_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax) * xAndLambda[10] * (b_const->g *
    b_const->mass + muDoubleScalarSin(-b_const->alfamax) * 300.0);
  ai = muDoubleScalarSin(b_const->bankmax) * 0.0 * (b_const->g * b_const->mass +
    muDoubleScalarSin(-b_const->alfamax) * 300.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        db_const_re = 0.5;
      } else {
        db_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        db_const_im = 0.5;
      } else {
        db_const_im = -0.5;
      }

      bim = (ar * db_const_re + ai * db_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = 1.5707963267948966;
    *alfatrigSave = -1.5707963267948966;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&m_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = 3.1416 / (2.0 * b_const->bankmax);
  b_asin(&hamiltonian);
  banktrig = -hamiltonian;
  emlrtPopRtStackR2012b(&m_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(-hamiltonian) || muDoubleScalarIsInf(-hamiltonian)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  bb_v.re = xAndLambda[3] * xAndLambda[3];
  bb_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, bb_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(-b_const->alfamax) * 300.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  db_const.re = b_const->mass * xAndLambda[3];
  db_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig))
                * (b_const->g * b_const->mass + muDoubleScalarSin
                   (-b_const->alfamax) * 300.0), db_const);
  bb_z.re = xAndLambda[2] + 50.0;
  bb_z.im = 0.0;
  v = b_mpower(bb_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        cb_v_re = 0.5;
      } else {
        cb_v_re = -0.5;
      }

      if (v_im > 0.0) {
        cb_v_im = 0.5;
      } else {
        cb_v_im = -0.5;
      }

      re = (ar * cb_v_re + ai * cb_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda[10] * (b_const->g * b_const->mass + muDoubleScalarSin
                      (-b_const->alfamax) * 300.0);
  ai = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (b_const->g * b_const->mass + muDoubleScalarSin(-b_const->alfamax) * 300.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        eb_const_re = 0.5;
      } else {
        eb_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        eb_const_im = 0.5;
      } else {
        eb_const_im = -0.5;
      }

      bim = (ar * eb_const_re + ai * eb_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = -1.5707963267948966;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&n_emlrtRSI, emlrtRootTLSGlobal);
  banktrig = 3.1416 / (2.0 * b_const->bankmax);
  b_asin(&banktrig);
  emlrtPopRtStackR2012b(&n_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(banktrig) || muDoubleScalarIsInf(banktrig)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  cb_v.re = xAndLambda[3] * xAndLambda[3];
  cb_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, cb_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(-b_const->alfamax) * 300.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  eb_const.re = b_const->mass * xAndLambda[3];
  eb_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig))
                * (b_const->g * b_const->mass + muDoubleScalarSin
                   (-b_const->alfamax) * 300.0), eb_const);
  cb_z.re = xAndLambda[2] + 50.0;
  cb_z.im = 0.0;
  v = b_mpower(cb_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        db_v_re = 0.5;
      } else {
        db_v_re = -0.5;
      }

      if (v_im > 0.0) {
        db_v_im = 0.5;
      } else {
        db_v_im = -0.5;
      }

      re = (ar * db_v_re + ai * db_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda[10] * (b_const->g * b_const->mass + muDoubleScalarSin
                      (-b_const->alfamax) * 300.0);
  ai = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (b_const->g * b_const->mass + muDoubleScalarSin(-b_const->alfamax) * 300.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        fb_const_re = 0.5;
      } else {
        fb_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        fb_const_im = 0.5;
      } else {
        fb_const_im = -0.5;
      }

      bim = (ar * fb_const_re + ai * fb_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = -1.5707963267948966;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  db_v.re = xAndLambda[3] * xAndLambda[3];
  db_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, db_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax) * 300.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  fb_const.re = b_const->mass * xAndLambda[3];
  fb_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(-b_const->bankmax) * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax) * 300.0), fb_const);
  db_z.re = xAndLambda[2] + 50.0;
  db_z.im = 0.0;
  v = b_mpower(db_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        eb_v_re = 0.5;
      } else {
        eb_v_re = -0.5;
      }

      if (v_im > 0.0) {
        eb_v_im = 0.5;
      } else {
        eb_v_im = -0.5;
      }

      re = (ar * eb_v_re + ai * eb_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(-b_const->bankmax) * xAndLambda[10] * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax) * 300.0);
  ai = muDoubleScalarSin(-b_const->bankmax) * 0.0 * (b_const->g * b_const->mass
    + muDoubleScalarSin(b_const->alfamax) * 300.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        gb_const_re = 0.5;
      } else {
        gb_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        gb_const_im = 0.5;
      } else {
        gb_const_im = -0.5;
      }

      bim = (ar * gb_const_re + ai * gb_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = -1.5707963267948966;
    *alfatrigSave = 1.5707963267948966;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  eb_v.re = xAndLambda[3] * xAndLambda[3];
  eb_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, eb_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax) * 300.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  gb_const.re = b_const->mass * xAndLambda[3];
  gb_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax) * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax) * 300.0), gb_const);
  eb_z.re = xAndLambda[2] + 50.0;
  eb_z.im = 0.0;
  v = b_mpower(eb_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        fb_v_re = 0.5;
      } else {
        fb_v_re = -0.5;
      }

      if (v_im > 0.0) {
        fb_v_im = 0.5;
      } else {
        fb_v_im = -0.5;
      }

      re = (ar * fb_v_re + ai * fb_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax) * xAndLambda[10] * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax) * 300.0);
  ai = muDoubleScalarSin(b_const->bankmax) * 0.0 * (b_const->g * b_const->mass +
    muDoubleScalarSin(b_const->alfamax) * 300.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        hb_const_re = 0.5;
      } else {
        hb_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        hb_const_im = 0.5;
      } else {
        hb_const_im = -0.5;
      }

      bim = (ar * hb_const_re + ai * hb_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = 1.5707963267948966;
    *alfatrigSave = 1.5707963267948966;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&o_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = 3.1416 / (2.0 * b_const->bankmax);
  b_asin(&hamiltonian);
  banktrig = -hamiltonian;
  emlrtPopRtStackR2012b(&o_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(-hamiltonian) || muDoubleScalarIsInf(-hamiltonian)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  fb_v.re = xAndLambda[3] * xAndLambda[3];
  fb_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, fb_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax) * 300.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  hb_const.re = b_const->mass * xAndLambda[3];
  hb_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig))
                * (b_const->g * b_const->mass + muDoubleScalarSin
                   (b_const->alfamax) * 300.0), hb_const);
  fb_z.re = xAndLambda[2] + 50.0;
  fb_z.im = 0.0;
  v = b_mpower(fb_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        gb_v_re = 0.5;
      } else {
        gb_v_re = -0.5;
      }

      if (v_im > 0.0) {
        gb_v_im = 0.5;
      } else {
        gb_v_im = -0.5;
      }

      re = (ar * gb_v_re + ai * gb_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda[10] * (b_const->g * b_const->mass + muDoubleScalarSin
                      (b_const->alfamax) * 300.0);
  ai = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (b_const->g * b_const->mass + muDoubleScalarSin(b_const->alfamax) * 300.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        ib_const_re = 0.5;
      } else {
        ib_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        ib_const_im = 0.5;
      } else {
        ib_const_im = -0.5;
      }

      bim = (ar * ib_const_re + ai * ib_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = 1.5707963267948966;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&p_emlrtRSI, emlrtRootTLSGlobal);
  banktrig = 3.1416 / (2.0 * b_const->bankmax);
  b_asin(&banktrig);
  emlrtPopRtStackR2012b(&p_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(banktrig) || muDoubleScalarIsInf(banktrig)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  gb_v.re = xAndLambda[3] * xAndLambda[3];
  gb_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, gb_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax) * 300.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  ib_const.re = b_const->mass * xAndLambda[3];
  ib_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig))
                * (b_const->g * b_const->mass + muDoubleScalarSin
                   (b_const->alfamax) * 300.0), ib_const);
  gb_z.re = xAndLambda[2] + 50.0;
  gb_z.im = 0.0;
  v = b_mpower(gb_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        hb_v_re = 0.5;
      } else {
        hb_v_re = -0.5;
      }

      if (v_im > 0.0) {
        hb_v_im = 0.5;
      } else {
        hb_v_im = -0.5;
      }

      re = (ar * hb_v_re + ai * hb_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda[10] * (b_const->g * b_const->mass + muDoubleScalarSin
                      (b_const->alfamax) * 300.0);
  ai = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (b_const->g * b_const->mass + muDoubleScalarSin(b_const->alfamax) * 300.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        jb_const_re = 0.5;
      } else {
        jb_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        jb_const_im = 0.5;
      } else {
        jb_const_im = -0.5;
      }

      bim = (ar * jb_const_re + ai * jb_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = 1.5707963267948966;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(-b_const->bankmax);
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(-b_const->bankmax);
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(-(2.0 * b_const->bankmax));
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(-(2.0 * b_const->bankmax));
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew = 0.0;
    } else if (b_const_im == 0.0) {
      hamiltonian = 0.0;
      Ttrignew /= dc0.re;
    } else {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = 0.0;
    } else if (Ttrignew == 0.0) {
      hamiltonian = 0.0;
      Ttrignew = -(b_const_im / dc0.im);
    } else {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = -(b_const_im / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      hamiltonian = (b_const_im + bim * Ttrignew) / c_const_re;
      Ttrignew = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      hamiltonian = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      Ttrignew = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      hamiltonian = (bim * b_const_im + Ttrignew) / c_const_re;
      Ttrignew = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -Ttrignew;
  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = -dc0.re;
  if (muDoubleScalarIsNaN(-dc0.re) || muDoubleScalarIsInf(-dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  hb_v.re = xAndLambda[3] * xAndLambda[3];
  hb_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, hb_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 300.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  jb_const.re = b_const->mass * xAndLambda[3];
  jb_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(-b_const->bankmax) * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * 300.0), jb_const);
  hb_z.re = xAndLambda[2] + 50.0;
  hb_z.im = 0.0;
  v = b_mpower(hb_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        ib_v_re = 0.5;
      } else {
        ib_v_re = -0.5;
      }

      if (v_im > 0.0) {
        ib_v_im = 0.5;
      } else {
        ib_v_im = -0.5;
      }

      re = (ar * ib_v_re + ai * ib_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(-b_const->bankmax) * xAndLambda[10] * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * 300.0);
  ai = muDoubleScalarSin(-b_const->bankmax) * 0.0 * (b_const->g * b_const->mass
    + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 300.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        kb_const_re = 0.5;
      } else {
        kb_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        kb_const_im = 0.5;
      } else {
        kb_const_im = -0.5;
      }

      bim = (ar * kb_const_re + ai * kb_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = -1.5707963267948966;
    *alfatrigSave = alfatrig;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(b_const->bankmax);
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(b_const->bankmax);
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(2.0 * b_const->bankmax);
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(2.0 * b_const->bankmax);
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew = 0.0;
    } else if (b_const_im == 0.0) {
      hamiltonian = 0.0;
      Ttrignew /= dc0.re;
    } else {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = 0.0;
    } else if (Ttrignew == 0.0) {
      hamiltonian = 0.0;
      Ttrignew = -(b_const_im / dc0.im);
    } else {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = -(b_const_im / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      hamiltonian = (b_const_im + bim * Ttrignew) / c_const_re;
      Ttrignew = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      hamiltonian = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      Ttrignew = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      hamiltonian = (bim * b_const_im + Ttrignew) / c_const_re;
      Ttrignew = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -Ttrignew;
  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = -dc0.re;
  if (muDoubleScalarIsNaN(-dc0.re) || muDoubleScalarIsInf(-dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  ib_v.re = xAndLambda[3] * xAndLambda[3];
  ib_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, ib_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 300.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  kb_const.re = b_const->mass * xAndLambda[3];
  kb_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax) * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * 300.0), kb_const);
  ib_z.re = xAndLambda[2] + 50.0;
  ib_z.im = 0.0;
  v = b_mpower(ib_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        jb_v_re = 0.5;
      } else {
        jb_v_re = -0.5;
      }

      if (v_im > 0.0) {
        jb_v_im = 0.5;
      } else {
        jb_v_im = -0.5;
      }

      re = (ar * jb_v_re + ai * jb_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax) * xAndLambda[10] * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * 300.0);
  ai = muDoubleScalarSin(b_const->bankmax) * 0.0 * (b_const->g * b_const->mass +
    muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 300.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        lb_const_re = 0.5;
      } else {
        lb_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        lb_const_im = 0.5;
      } else {
        lb_const_im = -0.5;
      }

      bim = (ar * lb_const_re + ai * lb_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = 1.5707963267948966;
    *alfatrigSave = alfatrig;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&q_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = 3.1416 / (2.0 * b_const->bankmax);
  b_asin(&hamiltonian);
  banktrig = -hamiltonian;
  emlrtPopRtStackR2012b(&q_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(-hamiltonian) || muDoubleScalarIsInf(-hamiltonian)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(2.0 * b_const->bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(2.0 * b_const->bankmax * muDoubleScalarSin(banktrig));
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew = 0.0;
    } else if (b_const_im == 0.0) {
      hamiltonian = 0.0;
      Ttrignew /= dc0.re;
    } else {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = 0.0;
    } else if (Ttrignew == 0.0) {
      hamiltonian = 0.0;
      Ttrignew = -(b_const_im / dc0.im);
    } else {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = -(b_const_im / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      hamiltonian = (b_const_im + bim * Ttrignew) / c_const_re;
      Ttrignew = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      hamiltonian = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      Ttrignew = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      hamiltonian = (bim * b_const_im + Ttrignew) / c_const_re;
      Ttrignew = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -Ttrignew;
  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = -dc0.re;
  if (muDoubleScalarIsNaN(-dc0.re) || muDoubleScalarIsInf(-dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  jb_v.re = xAndLambda[3] * xAndLambda[3];
  jb_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, jb_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 300.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  lb_const.re = b_const->mass * xAndLambda[3];
  lb_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig))
                * (b_const->g * b_const->mass + muDoubleScalarSin
                   (b_const->alfamax * muDoubleScalarSin(alfatrig)) * 300.0),
                lb_const);
  jb_z.re = xAndLambda[2] + 50.0;
  jb_z.im = 0.0;
  v = b_mpower(jb_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        kb_v_re = 0.5;
      } else {
        kb_v_re = -0.5;
      }

      if (v_im > 0.0) {
        kb_v_im = 0.5;
      } else {
        kb_v_im = -0.5;
      }

      re = (ar * kb_v_re + ai * kb_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda[10] * (b_const->g * b_const->mass + muDoubleScalarSin
                      (b_const->alfamax * muDoubleScalarSin(alfatrig)) * 300.0);
  ai = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (b_const->g * b_const->mass + muDoubleScalarSin(b_const->alfamax *
      muDoubleScalarSin(alfatrig)) * 300.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        mb_const_re = 0.5;
      } else {
        mb_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        mb_const_im = 0.5;
      } else {
        mb_const_im = -0.5;
      }

      bim = (ar * mb_const_re + ai * mb_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&r_emlrtRSI, emlrtRootTLSGlobal);
  banktrig = 3.1416 / (2.0 * b_const->bankmax);
  b_asin(&banktrig);
  emlrtPopRtStackR2012b(&r_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(banktrig) || muDoubleScalarIsInf(banktrig)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(2.0 * b_const->bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(2.0 * b_const->bankmax * muDoubleScalarSin(banktrig));
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew = 0.0;
    } else if (b_const_im == 0.0) {
      hamiltonian = 0.0;
      Ttrignew /= dc0.re;
    } else {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = 0.0;
    } else if (Ttrignew == 0.0) {
      hamiltonian = 0.0;
      Ttrignew = -(b_const_im / dc0.im);
    } else {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = -(b_const_im / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      hamiltonian = (b_const_im + bim * Ttrignew) / c_const_re;
      Ttrignew = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      hamiltonian = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      Ttrignew = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      hamiltonian = (bim * b_const_im + Ttrignew) / c_const_re;
      Ttrignew = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -Ttrignew;
  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = -dc0.re;
  if (muDoubleScalarIsNaN(-dc0.re) || muDoubleScalarIsInf(-dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  kb_v.re = xAndLambda[3] * xAndLambda[3];
  kb_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, kb_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 300.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  mb_const.re = b_const->mass * xAndLambda[3];
  mb_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig))
                * (b_const->g * b_const->mass + muDoubleScalarSin
                   (b_const->alfamax * muDoubleScalarSin(alfatrig)) * 300.0),
                mb_const);
  kb_z.re = xAndLambda[2] + 50.0;
  kb_z.im = 0.0;
  v = b_mpower(kb_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        lb_v_re = 0.5;
      } else {
        lb_v_re = -0.5;
      }

      if (v_im > 0.0) {
        lb_v_im = 0.5;
      } else {
        lb_v_im = -0.5;
      }

      re = (ar * lb_v_re + ai * lb_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda[10] * (b_const->g * b_const->mass + muDoubleScalarSin
                      (b_const->alfamax * muDoubleScalarSin(alfatrig)) * 300.0);
  ai = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (b_const->g * b_const->mass + muDoubleScalarSin(b_const->alfamax *
      muDoubleScalarSin(alfatrig)) * 300.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        nb_const_re = 0.5;
      } else {
        nb_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        nb_const_im = 0.5;
      } else {
        nb_const_im = -0.5;
      }

      bim = (ar * nb_const_re + ai * nb_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(-b_const->bankmax);
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(-b_const->bankmax);
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(-(2.0 * b_const->bankmax));
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(-(2.0 * b_const->bankmax));
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew = 0.0;
    } else if (b_const_im == 0.0) {
      hamiltonian = 0.0;
      Ttrignew /= dc0.re;
    } else {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = 0.0;
    } else if (Ttrignew == 0.0) {
      hamiltonian = 0.0;
      Ttrignew = -(b_const_im / dc0.im);
    } else {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = -(b_const_im / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      hamiltonian = (b_const_im + bim * Ttrignew) / c_const_re;
      Ttrignew = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      hamiltonian = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      Ttrignew = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      hamiltonian = (bim * b_const_im + Ttrignew) / c_const_re;
      Ttrignew = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -Ttrignew;
  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  lb_v.re = xAndLambda[3] * xAndLambda[3];
  lb_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, lb_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 300.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  nb_const.re = b_const->mass * xAndLambda[3];
  nb_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(-b_const->bankmax) * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * 300.0), nb_const);
  lb_z.re = xAndLambda[2] + 50.0;
  lb_z.im = 0.0;
  v = b_mpower(lb_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        mb_v_re = 0.5;
      } else {
        mb_v_re = -0.5;
      }

      if (v_im > 0.0) {
        mb_v_im = 0.5;
      } else {
        mb_v_im = -0.5;
      }

      re = (ar * mb_v_re + ai * mb_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(-b_const->bankmax) * xAndLambda[10] * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * 300.0);
  ai = muDoubleScalarSin(-b_const->bankmax) * 0.0 * (b_const->g * b_const->mass
    + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 300.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        ob_const_re = 0.5;
      } else {
        ob_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        ob_const_im = 0.5;
      } else {
        ob_const_im = -0.5;
      }

      bim = (ar * ob_const_re + ai * ob_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = -1.5707963267948966;
    *alfatrigSave = alfatrig;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(b_const->bankmax);
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(b_const->bankmax);
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(2.0 * b_const->bankmax);
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(2.0 * b_const->bankmax);
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew = 0.0;
    } else if (b_const_im == 0.0) {
      hamiltonian = 0.0;
      Ttrignew /= dc0.re;
    } else {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = 0.0;
    } else if (Ttrignew == 0.0) {
      hamiltonian = 0.0;
      Ttrignew = -(b_const_im / dc0.im);
    } else {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = -(b_const_im / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      hamiltonian = (b_const_im + bim * Ttrignew) / c_const_re;
      Ttrignew = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      hamiltonian = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      Ttrignew = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      hamiltonian = (bim * b_const_im + Ttrignew) / c_const_re;
      Ttrignew = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -Ttrignew;
  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  mb_v.re = xAndLambda[3] * xAndLambda[3];
  mb_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, mb_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 300.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  ob_const.re = b_const->mass * xAndLambda[3];
  ob_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax) * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * 300.0), ob_const);
  mb_z.re = xAndLambda[2] + 50.0;
  mb_z.im = 0.0;
  v = b_mpower(mb_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        nb_v_re = 0.5;
      } else {
        nb_v_re = -0.5;
      }

      if (v_im > 0.0) {
        nb_v_im = 0.5;
      } else {
        nb_v_im = -0.5;
      }

      re = (ar * nb_v_re + ai * nb_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax) * xAndLambda[10] * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * 300.0);
  ai = muDoubleScalarSin(b_const->bankmax) * 0.0 * (b_const->g * b_const->mass +
    muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 300.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        pb_const_re = 0.5;
      } else {
        pb_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        pb_const_im = 0.5;
      } else {
        pb_const_im = -0.5;
      }

      bim = (ar * pb_const_re + ai * pb_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = 1.5707963267948966;
    *alfatrigSave = alfatrig;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&s_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = 3.1416 / (2.0 * b_const->bankmax);
  b_asin(&hamiltonian);
  banktrig = -hamiltonian;
  emlrtPopRtStackR2012b(&s_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(-hamiltonian) || muDoubleScalarIsInf(-hamiltonian)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(2.0 * b_const->bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(2.0 * b_const->bankmax * muDoubleScalarSin(banktrig));
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew = 0.0;
    } else if (b_const_im == 0.0) {
      hamiltonian = 0.0;
      Ttrignew /= dc0.re;
    } else {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = 0.0;
    } else if (Ttrignew == 0.0) {
      hamiltonian = 0.0;
      Ttrignew = -(b_const_im / dc0.im);
    } else {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = -(b_const_im / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      hamiltonian = (b_const_im + bim * Ttrignew) / c_const_re;
      Ttrignew = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      hamiltonian = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      Ttrignew = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      hamiltonian = (bim * b_const_im + Ttrignew) / c_const_re;
      Ttrignew = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -Ttrignew;
  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  nb_v.re = xAndLambda[3] * xAndLambda[3];
  nb_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, nb_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 300.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  pb_const.re = b_const->mass * xAndLambda[3];
  pb_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig))
                * (b_const->g * b_const->mass + muDoubleScalarSin
                   (b_const->alfamax * muDoubleScalarSin(alfatrig)) * 300.0),
                pb_const);
  nb_z.re = xAndLambda[2] + 50.0;
  nb_z.im = 0.0;
  v = b_mpower(nb_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        ob_v_re = 0.5;
      } else {
        ob_v_re = -0.5;
      }

      if (v_im > 0.0) {
        ob_v_im = 0.5;
      } else {
        ob_v_im = -0.5;
      }

      re = (ar * ob_v_re + ai * ob_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda[10] * (b_const->g * b_const->mass + muDoubleScalarSin
                      (b_const->alfamax * muDoubleScalarSin(alfatrig)) * 300.0);
  ai = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (b_const->g * b_const->mass + muDoubleScalarSin(b_const->alfamax *
      muDoubleScalarSin(alfatrig)) * 300.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        qb_const_re = 0.5;
      } else {
        qb_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        qb_const_im = 0.5;
      } else {
        qb_const_im = -0.5;
      }

      bim = (ar * qb_const_re + ai * qb_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&t_emlrtRSI, emlrtRootTLSGlobal);
  banktrig = 3.1416 / (2.0 * b_const->bankmax);
  b_asin(&banktrig);
  emlrtPopRtStackR2012b(&t_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(banktrig) || muDoubleScalarIsInf(banktrig)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(2.0 * b_const->bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(2.0 * b_const->bankmax * muDoubleScalarSin(banktrig));
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew = 0.0;
    } else if (b_const_im == 0.0) {
      hamiltonian = 0.0;
      Ttrignew /= dc0.re;
    } else {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = 0.0;
    } else if (Ttrignew == 0.0) {
      hamiltonian = 0.0;
      Ttrignew = -(b_const_im / dc0.im);
    } else {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = -(b_const_im / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      hamiltonian = (b_const_im + bim * Ttrignew) / c_const_re;
      Ttrignew = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      hamiltonian = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      Ttrignew = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      hamiltonian = (bim * b_const_im + Ttrignew) / c_const_re;
      Ttrignew = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -Ttrignew;
  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  ob_v.re = xAndLambda[3] * xAndLambda[3];
  ob_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, ob_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 300.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  qb_const.re = b_const->mass * xAndLambda[3];
  qb_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig))
                * (b_const->g * b_const->mass + muDoubleScalarSin
                   (b_const->alfamax * muDoubleScalarSin(alfatrig)) * 300.0),
                qb_const);
  ob_z.re = xAndLambda[2] + 50.0;
  ob_z.im = 0.0;
  v = b_mpower(ob_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        pb_v_re = 0.5;
      } else {
        pb_v_re = -0.5;
      }

      if (v_im > 0.0) {
        pb_v_im = 0.5;
      } else {
        pb_v_im = -0.5;
      }

      re = (ar * pb_v_re + ai * pb_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda[10] * (b_const->g * b_const->mass + muDoubleScalarSin
                      (b_const->alfamax * muDoubleScalarSin(alfatrig)) * 300.0);
  ai = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (b_const->g * b_const->mass + muDoubleScalarSin(b_const->alfamax *
      muDoubleScalarSin(alfatrig)) * 300.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        rb_const_re = 0.5;
      } else {
        rb_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        rb_const_im = 0.5;
      } else {
        rb_const_im = -0.5;
      }

      bim = (ar * rb_const_re + ai * rb_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(-b_const->bankmax);
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(-b_const->bankmax);
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(-(2.0 * b_const->bankmax));
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(-(2.0 * b_const->bankmax));
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  re = dc0.re;
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      dc0.re = b_const_im / dc0.re;
      dc0.im = 0.0;
    } else if (b_const_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = Ttrignew / re;
    } else {
      dc0.re = b_const_im / dc0.re;
      dc0.im = Ttrignew / re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = 0.0;
    } else if (Ttrignew == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(b_const_im / lamY_im);
    } else {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = -(b_const_im / lamY_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      dc0.re = (b_const_im + bim * Ttrignew) / c_const_re;
      dc0.im = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      dc0.re = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      dc0.im = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      dc0.re = (bim * b_const_im + Ttrignew) / c_const_re;
      dc0.im = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = -dc0.re;
  if (muDoubleScalarIsNaN(-dc0.re) || muDoubleScalarIsInf(-dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  pb_v.re = xAndLambda[3] * xAndLambda[3];
  pb_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, pb_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 300.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  rb_const.re = b_const->mass * xAndLambda[3];
  rb_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(-b_const->bankmax) * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * 300.0), rb_const);
  pb_z.re = xAndLambda[2] + 50.0;
  pb_z.im = 0.0;
  v = b_mpower(pb_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        qb_v_re = 0.5;
      } else {
        qb_v_re = -0.5;
      }

      if (v_im > 0.0) {
        qb_v_im = 0.5;
      } else {
        qb_v_im = -0.5;
      }

      re = (ar * qb_v_re + ai * qb_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(-b_const->bankmax) * xAndLambda[10] * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * 300.0);
  ai = muDoubleScalarSin(-b_const->bankmax) * 0.0 * (b_const->g * b_const->mass
    + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 300.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        sb_const_re = 0.5;
      } else {
        sb_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        sb_const_im = 0.5;
      } else {
        sb_const_im = -0.5;
      }

      bim = (ar * sb_const_re + ai * sb_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = -1.5707963267948966;
    *alfatrigSave = alfatrig;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(b_const->bankmax);
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(b_const->bankmax);
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(2.0 * b_const->bankmax);
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(2.0 * b_const->bankmax);
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  re = dc0.re;
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      dc0.re = b_const_im / dc0.re;
      dc0.im = 0.0;
    } else if (b_const_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = Ttrignew / re;
    } else {
      dc0.re = b_const_im / dc0.re;
      dc0.im = Ttrignew / re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = 0.0;
    } else if (Ttrignew == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(b_const_im / lamY_im);
    } else {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = -(b_const_im / lamY_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      dc0.re = (b_const_im + bim * Ttrignew) / c_const_re;
      dc0.im = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      dc0.re = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      dc0.im = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      dc0.re = (bim * b_const_im + Ttrignew) / c_const_re;
      dc0.im = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = -dc0.re;
  if (muDoubleScalarIsNaN(-dc0.re) || muDoubleScalarIsInf(-dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  qb_v.re = xAndLambda[3] * xAndLambda[3];
  qb_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, qb_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 300.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  sb_const.re = b_const->mass * xAndLambda[3];
  sb_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax) * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * 300.0), sb_const);
  qb_z.re = xAndLambda[2] + 50.0;
  qb_z.im = 0.0;
  v = b_mpower(qb_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        rb_v_re = 0.5;
      } else {
        rb_v_re = -0.5;
      }

      if (v_im > 0.0) {
        rb_v_im = 0.5;
      } else {
        rb_v_im = -0.5;
      }

      re = (ar * rb_v_re + ai * rb_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax) * xAndLambda[10] * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * 300.0);
  ai = muDoubleScalarSin(b_const->bankmax) * 0.0 * (b_const->g * b_const->mass +
    muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 300.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        tb_const_re = 0.5;
      } else {
        tb_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        tb_const_im = 0.5;
      } else {
        tb_const_im = -0.5;
      }

      bim = (ar * tb_const_re + ai * tb_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = 1.5707963267948966;
    *alfatrigSave = alfatrig;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&u_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = 3.1416 / (2.0 * b_const->bankmax);
  b_asin(&hamiltonian);
  banktrig = -hamiltonian;
  emlrtPopRtStackR2012b(&u_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(-hamiltonian) || muDoubleScalarIsInf(-hamiltonian)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(2.0 * b_const->bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(2.0 * b_const->bankmax * muDoubleScalarSin(banktrig));
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  re = dc0.re;
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      dc0.re = b_const_im / dc0.re;
      dc0.im = 0.0;
    } else if (b_const_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = Ttrignew / re;
    } else {
      dc0.re = b_const_im / dc0.re;
      dc0.im = Ttrignew / re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = 0.0;
    } else if (Ttrignew == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(b_const_im / lamY_im);
    } else {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = -(b_const_im / lamY_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      dc0.re = (b_const_im + bim * Ttrignew) / c_const_re;
      dc0.im = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      dc0.re = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      dc0.im = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      dc0.re = (bim * b_const_im + Ttrignew) / c_const_re;
      dc0.im = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = -dc0.re;
  if (muDoubleScalarIsNaN(-dc0.re) || muDoubleScalarIsInf(-dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  rb_v.re = xAndLambda[3] * xAndLambda[3];
  rb_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, rb_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 300.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  tb_const.re = b_const->mass * xAndLambda[3];
  tb_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig))
                * (b_const->g * b_const->mass + muDoubleScalarSin
                   (b_const->alfamax * muDoubleScalarSin(alfatrig)) * 300.0),
                tb_const);
  rb_z.re = xAndLambda[2] + 50.0;
  rb_z.im = 0.0;
  v = b_mpower(rb_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        sb_v_re = 0.5;
      } else {
        sb_v_re = -0.5;
      }

      if (v_im > 0.0) {
        sb_v_im = 0.5;
      } else {
        sb_v_im = -0.5;
      }

      re = (ar * sb_v_re + ai * sb_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda[10] * (b_const->g * b_const->mass + muDoubleScalarSin
                      (b_const->alfamax * muDoubleScalarSin(alfatrig)) * 300.0);
  ai = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (b_const->g * b_const->mass + muDoubleScalarSin(b_const->alfamax *
      muDoubleScalarSin(alfatrig)) * 300.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        ub_const_re = 0.5;
      } else {
        ub_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        ub_const_im = 0.5;
      } else {
        ub_const_im = -0.5;
      }

      bim = (ar * ub_const_re + ai * ub_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&v_emlrtRSI, emlrtRootTLSGlobal);
  banktrig = 3.1416 / (2.0 * b_const->bankmax);
  b_asin(&banktrig);
  emlrtPopRtStackR2012b(&v_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(banktrig) || muDoubleScalarIsInf(banktrig)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(2.0 * b_const->bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(2.0 * b_const->bankmax * muDoubleScalarSin(banktrig));
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  re = dc0.re;
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      dc0.re = b_const_im / dc0.re;
      dc0.im = 0.0;
    } else if (b_const_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = Ttrignew / re;
    } else {
      dc0.re = b_const_im / dc0.re;
      dc0.im = Ttrignew / re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = 0.0;
    } else if (Ttrignew == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(b_const_im / lamY_im);
    } else {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = -(b_const_im / lamY_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      dc0.re = (b_const_im + bim * Ttrignew) / c_const_re;
      dc0.im = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      dc0.re = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      dc0.im = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      dc0.re = (bim * b_const_im + Ttrignew) / c_const_re;
      dc0.im = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = -dc0.re;
  if (muDoubleScalarIsNaN(-dc0.re) || muDoubleScalarIsInf(-dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  sb_v.re = xAndLambda[3] * xAndLambda[3];
  sb_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, sb_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 300.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  ub_const.re = b_const->mass * xAndLambda[3];
  ub_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig))
                * (b_const->g * b_const->mass + muDoubleScalarSin
                   (b_const->alfamax * muDoubleScalarSin(alfatrig)) * 300.0),
                ub_const);
  sb_z.re = xAndLambda[2] + 50.0;
  sb_z.im = 0.0;
  v = b_mpower(sb_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        tb_v_re = 0.5;
      } else {
        tb_v_re = -0.5;
      }

      if (v_im > 0.0) {
        tb_v_im = 0.5;
      } else {
        tb_v_im = -0.5;
      }

      re = (ar * tb_v_re + ai * tb_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda[10] * (b_const->g * b_const->mass + muDoubleScalarSin
                      (b_const->alfamax * muDoubleScalarSin(alfatrig)) * 300.0);
  ai = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (b_const->g * b_const->mass + muDoubleScalarSin(b_const->alfamax *
      muDoubleScalarSin(alfatrig)) * 300.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        vb_const_re = 0.5;
      } else {
        vb_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        vb_const_im = 0.5;
      } else {
        vb_const_im = -0.5;
      }

      bim = (ar * vb_const_re + ai * vb_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(-b_const->bankmax);
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(-b_const->bankmax);
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(-(2.0 * b_const->bankmax));
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(-(2.0 * b_const->bankmax));
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  re = dc0.re;
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      dc0.re = b_const_im / dc0.re;
      dc0.im = 0.0;
    } else if (b_const_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = Ttrignew / re;
    } else {
      dc0.re = b_const_im / dc0.re;
      dc0.im = Ttrignew / re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = 0.0;
    } else if (Ttrignew == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(b_const_im / lamY_im);
    } else {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = -(b_const_im / lamY_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      dc0.re = (b_const_im + bim * Ttrignew) / c_const_re;
      dc0.im = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      dc0.re = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      dc0.im = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      dc0.re = (bim * b_const_im + Ttrignew) / c_const_re;
      dc0.im = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  tb_v.re = xAndLambda[3] * xAndLambda[3];
  tb_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, tb_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 300.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  vb_const.re = b_const->mass * xAndLambda[3];
  vb_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(-b_const->bankmax) * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * 300.0), vb_const);
  tb_z.re = xAndLambda[2] + 50.0;
  tb_z.im = 0.0;
  v = b_mpower(tb_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        ub_v_re = 0.5;
      } else {
        ub_v_re = -0.5;
      }

      if (v_im > 0.0) {
        ub_v_im = 0.5;
      } else {
        ub_v_im = -0.5;
      }

      re = (ar * ub_v_re + ai * ub_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(-b_const->bankmax) * xAndLambda[10] * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * 300.0);
  ai = muDoubleScalarSin(-b_const->bankmax) * 0.0 * (b_const->g * b_const->mass
    + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 300.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        wb_const_re = 0.5;
      } else {
        wb_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        wb_const_im = 0.5;
      } else {
        wb_const_im = -0.5;
      }

      bim = (ar * wb_const_re + ai * wb_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = -1.5707963267948966;
    *alfatrigSave = alfatrig;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(b_const->bankmax);
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(b_const->bankmax);
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(2.0 * b_const->bankmax);
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(2.0 * b_const->bankmax);
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  re = dc0.re;
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      dc0.re = b_const_im / dc0.re;
      dc0.im = 0.0;
    } else if (b_const_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = Ttrignew / re;
    } else {
      dc0.re = b_const_im / dc0.re;
      dc0.im = Ttrignew / re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = 0.0;
    } else if (Ttrignew == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(b_const_im / lamY_im);
    } else {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = -(b_const_im / lamY_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      dc0.re = (b_const_im + bim * Ttrignew) / c_const_re;
      dc0.im = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      dc0.re = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      dc0.im = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      dc0.re = (bim * b_const_im + Ttrignew) / c_const_re;
      dc0.im = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  ub_v.re = xAndLambda[3] * xAndLambda[3];
  ub_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, ub_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 300.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  wb_const.re = b_const->mass * xAndLambda[3];
  wb_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax) * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * 300.0), wb_const);
  ub_z.re = xAndLambda[2] + 50.0;
  ub_z.im = 0.0;
  v = b_mpower(ub_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        vb_v_re = 0.5;
      } else {
        vb_v_re = -0.5;
      }

      if (v_im > 0.0) {
        vb_v_im = 0.5;
      } else {
        vb_v_im = -0.5;
      }

      re = (ar * vb_v_re + ai * vb_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax) * xAndLambda[10] * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * 300.0);
  ai = muDoubleScalarSin(b_const->bankmax) * 0.0 * (b_const->g * b_const->mass +
    muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 300.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        xb_const_re = 0.5;
      } else {
        xb_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        xb_const_im = 0.5;
      } else {
        xb_const_im = -0.5;
      }

      bim = (ar * xb_const_re + ai * xb_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = 1.5707963267948966;
    *alfatrigSave = alfatrig;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&w_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = 3.1416 / (2.0 * b_const->bankmax);
  b_asin(&hamiltonian);
  banktrig = -hamiltonian;
  emlrtPopRtStackR2012b(&w_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(-hamiltonian) || muDoubleScalarIsInf(-hamiltonian)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(2.0 * b_const->bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(2.0 * b_const->bankmax * muDoubleScalarSin(banktrig));
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  re = dc0.re;
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      dc0.re = b_const_im / dc0.re;
      dc0.im = 0.0;
    } else if (b_const_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = Ttrignew / re;
    } else {
      dc0.re = b_const_im / dc0.re;
      dc0.im = Ttrignew / re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = 0.0;
    } else if (Ttrignew == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(b_const_im / lamY_im);
    } else {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = -(b_const_im / lamY_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      dc0.re = (b_const_im + bim * Ttrignew) / c_const_re;
      dc0.im = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      dc0.re = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      dc0.im = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      dc0.re = (bim * b_const_im + Ttrignew) / c_const_re;
      dc0.im = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  vb_v.re = xAndLambda[3] * xAndLambda[3];
  vb_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, vb_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 300.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  xb_const.re = b_const->mass * xAndLambda[3];
  xb_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig))
                * (b_const->g * b_const->mass + muDoubleScalarSin
                   (b_const->alfamax * muDoubleScalarSin(alfatrig)) * 300.0),
                xb_const);
  vb_z.re = xAndLambda[2] + 50.0;
  vb_z.im = 0.0;
  v = b_mpower(vb_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        wb_v_re = 0.5;
      } else {
        wb_v_re = -0.5;
      }

      if (v_im > 0.0) {
        wb_v_im = 0.5;
      } else {
        wb_v_im = -0.5;
      }

      re = (ar * wb_v_re + ai * wb_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda[10] * (b_const->g * b_const->mass + muDoubleScalarSin
                      (b_const->alfamax * muDoubleScalarSin(alfatrig)) * 300.0);
  ai = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (b_const->g * b_const->mass + muDoubleScalarSin(b_const->alfamax *
      muDoubleScalarSin(alfatrig)) * 300.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        yb_const_re = 0.5;
      } else {
        yb_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        yb_const_im = 0.5;
      } else {
        yb_const_im = -0.5;
      }

      bim = (ar * yb_const_re + ai * yb_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&x_emlrtRSI, emlrtRootTLSGlobal);
  banktrig = 3.1416 / (2.0 * b_const->bankmax);
  b_asin(&banktrig);
  emlrtPopRtStackR2012b(&x_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(banktrig) || muDoubleScalarIsInf(banktrig)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(2.0 * b_const->bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(2.0 * b_const->bankmax * muDoubleScalarSin(banktrig));
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  re = dc0.re;
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      dc0.re = b_const_im / dc0.re;
      dc0.im = 0.0;
    } else if (b_const_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = Ttrignew / re;
    } else {
      dc0.re = b_const_im / dc0.re;
      dc0.im = Ttrignew / re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = 0.0;
    } else if (Ttrignew == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(b_const_im / lamY_im);
    } else {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = -(b_const_im / lamY_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      dc0.re = (b_const_im + bim * Ttrignew) / c_const_re;
      dc0.im = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      dc0.re = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      dc0.im = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      dc0.re = (bim * b_const_im + Ttrignew) / c_const_re;
      dc0.im = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  wb_v.re = xAndLambda[3] * xAndLambda[3];
  wb_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, wb_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 300.0;
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  yb_const.re = b_const->mass * xAndLambda[3];
  yb_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig))
                * (b_const->g * b_const->mass + muDoubleScalarSin
                   (b_const->alfamax * muDoubleScalarSin(alfatrig)) * 300.0),
                yb_const);
  wb_z.re = xAndLambda[2] + 50.0;
  wb_z.im = 0.0;
  v = b_mpower(wb_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        xb_v_re = 0.5;
      } else {
        xb_v_re = -0.5;
      }

      if (v_im > 0.0) {
        xb_v_im = 0.5;
      } else {
        xb_v_im = -0.5;
      }

      re = (ar * xb_v_re + ai * xb_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda[10] * (b_const->g * b_const->mass + muDoubleScalarSin
                      (b_const->alfamax * muDoubleScalarSin(alfatrig)) * 300.0);
  ai = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (b_const->g * b_const->mass + muDoubleScalarSin(b_const->alfamax *
      muDoubleScalarSin(alfatrig)) * 300.0);
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        ac_const_re = 0.5;
      } else {
        ac_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        ac_const_im = 0.5;
      } else {
        ac_const_im = -0.5;
      }

      bim = (ar * ac_const_re + ai * ac_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  /*  Coefficients */
  dc0 = gam;
  b_cos(&dc0);
  a = gam;
  b_cos(&a);
  xb_z.re = xAndLambda[2] + 50.0;
  xb_z.im = 0.0;
  dc1 = b_mpower(xb_z);
  v_re = xAndLambda[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda[9] * muDoubleScalarCos(-b_const->alfamax));
  ai = -(0.0 * muDoubleScalarCos(-b_const->alfamax));
  if (ai == 0.0) {
    re = ar / b_const->mass;
    lamY_im = 0.0;
  } else if (ar == 0.0) {
    re = 0.0;
    lamY_im = ai / b_const->mass;
  } else {
    re = ar / b_const->mass;
    lamY_im = ai / b_const->mass;
  }

  ar = muDoubleScalarSin(-b_const->alfamax) * (1560.0 * xAndLambda[11]) *
    muDoubleScalarCos(-b_const->bankmax);
  ai = muDoubleScalarSin(-b_const->alfamax) * 0.0 * muDoubleScalarCos
    (-b_const->bankmax);
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_re = b_const->mass * 0.0;
  if (c_const_re == 0.0) {
    if (ai == 0.0) {
      lamY_re = ar / hamiltonian;
      lamX_im = 0.0;
    } else if (ar == 0.0) {
      lamY_re = 0.0;
      lamX_im = ai / hamiltonian;
    } else {
      lamY_re = ar / hamiltonian;
      lamX_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      lamY_re = ai / c_const_re;
      lamX_im = 0.0;
    } else if (ai == 0.0) {
      lamY_re = 0.0;
      lamX_im = -(ar / c_const_re);
    } else {
      lamY_re = ai / c_const_re;
      lamX_im = -(ar / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > c_const_re) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      lamY_re = (ar + bim * ai) / c_const_re;
      lamX_im = (ai - bim * ar) / c_const_re;
    } else if (c_const_re == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      lamY_re = (ar * lamX_re + ai * -0.5) / 0.0;
      lamX_im = (ai * lamX_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      lamY_re = (bim * ar + ai) / c_const_re;
      lamX_im = (bim * ai - ar) / c_const_re;
    }
  }

  const_re = b_const->mass * xAndLambda[3];
  const_im = b_const->mass * 0.0;
  b_const_re = const_re * a.re - const_im * a.im;
  const_im = const_re * a.im + const_im * a.re;
  ar = muDoubleScalarSin(-b_const->alfamax) * (1560.0 * xAndLambda[10]) *
    muDoubleScalarSin(-b_const->bankmax);
  ai = muDoubleScalarSin(-b_const->alfamax) * 0.0 * muDoubleScalarSin
    (-b_const->bankmax);
  if (const_im == 0.0) {
    if (ai == 0.0) {
      c_const_im = ar / b_const_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      c_const_im = 0.0;
      hamiltonian = ai / b_const_re;
    } else {
      c_const_im = ar / b_const_re;
      hamiltonian = ai / b_const_re;
    }
  } else if (b_const_re == 0.0) {
    if (ar == 0.0) {
      c_const_im = ai / const_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      c_const_im = 0.0;
      hamiltonian = -(ar / const_im);
    } else {
      c_const_im = ai / const_im;
      hamiltonian = -(ar / const_im);
    }
  } else {
    brm = muDoubleScalarAbs(b_const_re);
    bim = muDoubleScalarAbs(const_im);
    if (brm > bim) {
      bim = const_im / b_const_re;
      c_const_re = b_const_re + bim * const_im;
      c_const_im = (ar + bim * ai) / c_const_re;
      hamiltonian = (ai - bim * ar) / c_const_re;
    } else if (bim == brm) {
      if (b_const_re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (const_im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      c_const_im = (ar * lamX_re + ai * c_const_re) / brm;
      hamiltonian = (ai * lamX_re - ar * c_const_re) / brm;
    } else {
      bim = b_const_re / const_im;
      c_const_re = const_im + bim * b_const_re;
      c_const_im = (bim * ar + ai) / c_const_re;
      hamiltonian = (bim * ai - ar) / c_const_re;
    }
  }

  re = (re - lamY_re) - c_const_im;
  lamY_im = (lamY_im - lamX_im) - hamiltonian;
  c_const_im = v_re * re - v_im * lamY_im;
  v_im = v_re * lamY_im + v_im * re;
  hamiltonian = 8112.0 * dc0.re;
  c_const_re = 8112.0 * dc0.im;
  if (c_const_re == 0.0) {
    if (v_im == 0.0) {
      xb_v.re = c_const_im / hamiltonian;
      xb_v.im = 0.0;
    } else if (c_const_im == 0.0) {
      xb_v.re = 0.0;
      xb_v.im = v_im / hamiltonian;
    } else {
      xb_v.re = c_const_im / hamiltonian;
      xb_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (c_const_im == 0.0) {
      xb_v.re = v_im / c_const_re;
      xb_v.im = 0.0;
    } else if (v_im == 0.0) {
      xb_v.re = 0.0;
      xb_v.im = -(c_const_im / c_const_re);
    } else {
      xb_v.re = v_im / c_const_re;
      xb_v.im = -(c_const_im / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(c_const_re);
    if (brm > bim) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      xb_v.re = (c_const_im + bim * v_im) / c_const_re;
      xb_v.im = (v_im - bim * c_const_im) / c_const_re;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (c_const_re > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      xb_v.re = (c_const_im * lamX_re + v_im * c_const_re) / brm;
      xb_v.im = (v_im * lamX_re - c_const_im * c_const_re) / brm;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      xb_v.re = (bim * c_const_im + v_im) / c_const_re;
      xb_v.im = (bim * v_im - c_const_im) / c_const_re;
    }
  }

  dc1 = c_mpower(xb_v);
  ar = dc1.re - 1860.0;
  ai = dc1.im;
  if (ai == 0.0) {
    dc0.re = ar / 1560.0;
    dc0.im = 0.0;
  } else if (ar == 0.0) {
    dc0.re = 0.0;
    dc0.im = ai / 1560.0;
  } else {
    dc0.re = ar / 1560.0;
    dc0.im = ai / 1560.0;
  }

  c_asin(&dc0);
  Ttrignew = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    Ttrignew = 0.0;
  }

  emlrtPushRtStackR2012b(&y_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = mpower(1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0);
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  yb_v.re = xAndLambda[3] * xAndLambda[3];
  yb_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, yb_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(-b_const->alfamax) * (1560.0 * muDoubleScalarSin(Ttrignew)
    + 1860.0);
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  ac_const.re = b_const->mass * xAndLambda[3];
  ac_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(-b_const->bankmax) * (b_const->g *
    b_const->mass + muDoubleScalarSin(-b_const->alfamax) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0)), ac_const);
  yb_z.re = xAndLambda[2] + 50.0;
  yb_z.im = 0.0;
  v = b_mpower(yb_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        yb_v_re = 0.5;
      } else {
        yb_v_re = -0.5;
      }

      if (v_im > 0.0) {
        yb_v_im = 0.5;
      } else {
        yb_v_im = -0.5;
      }

      re = (ar * yb_v_re + ai * yb_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(-b_const->bankmax) * xAndLambda[10] * (b_const->g *
    b_const->mass + muDoubleScalarSin(-b_const->alfamax) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(-b_const->bankmax) * 0.0 * (b_const->g * b_const->mass
    + muDoubleScalarSin(-b_const->alfamax) * (1560.0 * muDoubleScalarSin
    (Ttrignew) + 1860.0));
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        bc_const_re = 0.5;
      } else {
        bc_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        bc_const_im = 0.5;
      } else {
        bc_const_im = -0.5;
      }

      bim = (ar * bc_const_re + ai * bc_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  emlrtPopRtStackR2012b(&y_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = -1.5707963267948966;
    *alfatrigSave = -1.5707963267948966;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  /*  Coefficients */
  dc0 = gam;
  b_cos(&dc0);
  a = gam;
  b_cos(&a);
  ac_z.re = xAndLambda[2] + 50.0;
  ac_z.im = 0.0;
  dc1 = b_mpower(ac_z);
  v_re = xAndLambda[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda[9] * muDoubleScalarCos(-b_const->alfamax));
  ai = -(0.0 * muDoubleScalarCos(-b_const->alfamax));
  if (ai == 0.0) {
    re = ar / b_const->mass;
    lamY_im = 0.0;
  } else if (ar == 0.0) {
    re = 0.0;
    lamY_im = ai / b_const->mass;
  } else {
    re = ar / b_const->mass;
    lamY_im = ai / b_const->mass;
  }

  ar = muDoubleScalarSin(-b_const->alfamax) * (1560.0 * xAndLambda[11]) *
    muDoubleScalarCos(b_const->bankmax);
  ai = muDoubleScalarSin(-b_const->alfamax) * 0.0 * muDoubleScalarCos
    (b_const->bankmax);
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_re = b_const->mass * 0.0;
  if (c_const_re == 0.0) {
    if (ai == 0.0) {
      lamY_re = ar / hamiltonian;
      lamX_im = 0.0;
    } else if (ar == 0.0) {
      lamY_re = 0.0;
      lamX_im = ai / hamiltonian;
    } else {
      lamY_re = ar / hamiltonian;
      lamX_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      lamY_re = ai / c_const_re;
      lamX_im = 0.0;
    } else if (ai == 0.0) {
      lamY_re = 0.0;
      lamX_im = -(ar / c_const_re);
    } else {
      lamY_re = ai / c_const_re;
      lamX_im = -(ar / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > c_const_re) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      lamY_re = (ar + bim * ai) / c_const_re;
      lamX_im = (ai - bim * ar) / c_const_re;
    } else if (c_const_re == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      lamY_re = (ar * lamX_re + ai * -0.5) / 0.0;
      lamX_im = (ai * lamX_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      lamY_re = (bim * ar + ai) / c_const_re;
      lamX_im = (bim * ai - ar) / c_const_re;
    }
  }

  const_re = b_const->mass * xAndLambda[3];
  const_im = b_const->mass * 0.0;
  b_const_re = const_re * a.re - const_im * a.im;
  const_im = const_re * a.im + const_im * a.re;
  ar = muDoubleScalarSin(-b_const->alfamax) * (1560.0 * xAndLambda[10]) *
    muDoubleScalarSin(b_const->bankmax);
  ai = muDoubleScalarSin(-b_const->alfamax) * 0.0 * muDoubleScalarSin
    (b_const->bankmax);
  if (const_im == 0.0) {
    if (ai == 0.0) {
      c_const_im = ar / b_const_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      c_const_im = 0.0;
      hamiltonian = ai / b_const_re;
    } else {
      c_const_im = ar / b_const_re;
      hamiltonian = ai / b_const_re;
    }
  } else if (b_const_re == 0.0) {
    if (ar == 0.0) {
      c_const_im = ai / const_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      c_const_im = 0.0;
      hamiltonian = -(ar / const_im);
    } else {
      c_const_im = ai / const_im;
      hamiltonian = -(ar / const_im);
    }
  } else {
    brm = muDoubleScalarAbs(b_const_re);
    bim = muDoubleScalarAbs(const_im);
    if (brm > bim) {
      bim = const_im / b_const_re;
      c_const_re = b_const_re + bim * const_im;
      c_const_im = (ar + bim * ai) / c_const_re;
      hamiltonian = (ai - bim * ar) / c_const_re;
    } else if (bim == brm) {
      if (b_const_re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (const_im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      c_const_im = (ar * lamX_re + ai * c_const_re) / brm;
      hamiltonian = (ai * lamX_re - ar * c_const_re) / brm;
    } else {
      bim = b_const_re / const_im;
      c_const_re = const_im + bim * b_const_re;
      c_const_im = (bim * ar + ai) / c_const_re;
      hamiltonian = (bim * ai - ar) / c_const_re;
    }
  }

  re = (re - lamY_re) - c_const_im;
  lamY_im = (lamY_im - lamX_im) - hamiltonian;
  c_const_im = v_re * re - v_im * lamY_im;
  v_im = v_re * lamY_im + v_im * re;
  hamiltonian = 8112.0 * dc0.re;
  c_const_re = 8112.0 * dc0.im;
  if (c_const_re == 0.0) {
    if (v_im == 0.0) {
      ac_v.re = c_const_im / hamiltonian;
      ac_v.im = 0.0;
    } else if (c_const_im == 0.0) {
      ac_v.re = 0.0;
      ac_v.im = v_im / hamiltonian;
    } else {
      ac_v.re = c_const_im / hamiltonian;
      ac_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (c_const_im == 0.0) {
      ac_v.re = v_im / c_const_re;
      ac_v.im = 0.0;
    } else if (v_im == 0.0) {
      ac_v.re = 0.0;
      ac_v.im = -(c_const_im / c_const_re);
    } else {
      ac_v.re = v_im / c_const_re;
      ac_v.im = -(c_const_im / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(c_const_re);
    if (brm > bim) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      ac_v.re = (c_const_im + bim * v_im) / c_const_re;
      ac_v.im = (v_im - bim * c_const_im) / c_const_re;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (c_const_re > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      ac_v.re = (c_const_im * lamX_re + v_im * c_const_re) / brm;
      ac_v.im = (v_im * lamX_re - c_const_im * c_const_re) / brm;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      ac_v.re = (bim * c_const_im + v_im) / c_const_re;
      ac_v.im = (bim * v_im - c_const_im) / c_const_re;
    }
  }

  dc1 = c_mpower(ac_v);
  ar = dc1.re - 1860.0;
  ai = dc1.im;
  if (ai == 0.0) {
    dc0.re = ar / 1560.0;
    dc0.im = 0.0;
  } else if (ar == 0.0) {
    dc0.re = 0.0;
    dc0.im = ai / 1560.0;
  } else {
    dc0.re = ar / 1560.0;
    dc0.im = ai / 1560.0;
  }

  c_asin(&dc0);
  Ttrignew = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    Ttrignew = 0.0;
  }

  emlrtPushRtStackR2012b(&ab_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = mpower(1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0);
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  bc_v.re = xAndLambda[3] * xAndLambda[3];
  bc_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, bc_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(-b_const->alfamax) * (1560.0 * muDoubleScalarSin(Ttrignew)
    + 1860.0);
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  bc_const.re = b_const->mass * xAndLambda[3];
  bc_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax) * (b_const->g *
    b_const->mass + muDoubleScalarSin(-b_const->alfamax) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0)), bc_const);
  bc_z.re = xAndLambda[2] + 50.0;
  bc_z.im = 0.0;
  v = b_mpower(bc_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        ac_v_re = 0.5;
      } else {
        ac_v_re = -0.5;
      }

      if (v_im > 0.0) {
        ac_v_im = 0.5;
      } else {
        ac_v_im = -0.5;
      }

      re = (ar * ac_v_re + ai * ac_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax) * xAndLambda[10] * (b_const->g *
    b_const->mass + muDoubleScalarSin(-b_const->alfamax) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(b_const->bankmax) * 0.0 * (b_const->g * b_const->mass +
    muDoubleScalarSin(-b_const->alfamax) * (1560.0 * muDoubleScalarSin(Ttrignew)
    + 1860.0));
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        cc_const_re = 0.5;
      } else {
        cc_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        cc_const_im = 0.5;
      } else {
        cc_const_im = -0.5;
      }

      bim = (ar * cc_const_re + ai * cc_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  emlrtPopRtStackR2012b(&ab_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = 1.5707963267948966;
    *alfatrigSave = -1.5707963267948966;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&bb_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = 3.1416 / (2.0 * b_const->bankmax);
  b_asin(&hamiltonian);
  banktrig = -hamiltonian;
  emlrtPopRtStackR2012b(&bb_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(-hamiltonian) || muDoubleScalarIsInf(-hamiltonian)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  /*  Coefficients */
  dc0 = gam;
  b_cos(&dc0);
  a = gam;
  b_cos(&a);
  cc_z.re = xAndLambda[2] + 50.0;
  cc_z.im = 0.0;
  dc1 = b_mpower(cc_z);
  v_re = xAndLambda[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda[9] * muDoubleScalarCos(-b_const->alfamax));
  ai = -(0.0 * muDoubleScalarCos(-b_const->alfamax));
  if (ai == 0.0) {
    re = ar / b_const->mass;
    lamY_im = 0.0;
  } else if (ar == 0.0) {
    re = 0.0;
    lamY_im = ai / b_const->mass;
  } else {
    re = ar / b_const->mass;
    lamY_im = ai / b_const->mass;
  }

  ar = muDoubleScalarSin(-b_const->alfamax) * (1560.0 * xAndLambda[11]) *
    muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig));
  ai = muDoubleScalarSin(-b_const->alfamax) * 0.0 * muDoubleScalarCos
    (b_const->bankmax * muDoubleScalarSin(banktrig));
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_re = b_const->mass * 0.0;
  if (c_const_re == 0.0) {
    if (ai == 0.0) {
      lamY_re = ar / hamiltonian;
      lamX_im = 0.0;
    } else if (ar == 0.0) {
      lamY_re = 0.0;
      lamX_im = ai / hamiltonian;
    } else {
      lamY_re = ar / hamiltonian;
      lamX_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      lamY_re = ai / c_const_re;
      lamX_im = 0.0;
    } else if (ai == 0.0) {
      lamY_re = 0.0;
      lamX_im = -(ar / c_const_re);
    } else {
      lamY_re = ai / c_const_re;
      lamX_im = -(ar / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > c_const_re) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      lamY_re = (ar + bim * ai) / c_const_re;
      lamX_im = (ai - bim * ar) / c_const_re;
    } else if (c_const_re == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      lamY_re = (ar * lamX_re + ai * -0.5) / 0.0;
      lamX_im = (ai * lamX_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      lamY_re = (bim * ar + ai) / c_const_re;
      lamX_im = (bim * ai - ar) / c_const_re;
    }
  }

  const_re = b_const->mass * xAndLambda[3];
  const_im = b_const->mass * 0.0;
  b_const_re = const_re * a.re - const_im * a.im;
  const_im = const_re * a.im + const_im * a.re;
  ar = muDoubleScalarSin(-b_const->alfamax) * (1560.0 * xAndLambda[10]) *
    muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig));
  ai = muDoubleScalarSin(-b_const->alfamax) * 0.0 * muDoubleScalarSin
    (b_const->bankmax * muDoubleScalarSin(banktrig));
  if (const_im == 0.0) {
    if (ai == 0.0) {
      c_const_im = ar / b_const_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      c_const_im = 0.0;
      hamiltonian = ai / b_const_re;
    } else {
      c_const_im = ar / b_const_re;
      hamiltonian = ai / b_const_re;
    }
  } else if (b_const_re == 0.0) {
    if (ar == 0.0) {
      c_const_im = ai / const_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      c_const_im = 0.0;
      hamiltonian = -(ar / const_im);
    } else {
      c_const_im = ai / const_im;
      hamiltonian = -(ar / const_im);
    }
  } else {
    brm = muDoubleScalarAbs(b_const_re);
    bim = muDoubleScalarAbs(const_im);
    if (brm > bim) {
      bim = const_im / b_const_re;
      c_const_re = b_const_re + bim * const_im;
      c_const_im = (ar + bim * ai) / c_const_re;
      hamiltonian = (ai - bim * ar) / c_const_re;
    } else if (bim == brm) {
      if (b_const_re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (const_im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      c_const_im = (ar * lamX_re + ai * c_const_re) / brm;
      hamiltonian = (ai * lamX_re - ar * c_const_re) / brm;
    } else {
      bim = b_const_re / const_im;
      c_const_re = const_im + bim * b_const_re;
      c_const_im = (bim * ar + ai) / c_const_re;
      hamiltonian = (bim * ai - ar) / c_const_re;
    }
  }

  re = (re - lamY_re) - c_const_im;
  lamY_im = (lamY_im - lamX_im) - hamiltonian;
  c_const_im = v_re * re - v_im * lamY_im;
  v_im = v_re * lamY_im + v_im * re;
  hamiltonian = 8112.0 * dc0.re;
  c_const_re = 8112.0 * dc0.im;
  if (c_const_re == 0.0) {
    if (v_im == 0.0) {
      cc_v.re = c_const_im / hamiltonian;
      cc_v.im = 0.0;
    } else if (c_const_im == 0.0) {
      cc_v.re = 0.0;
      cc_v.im = v_im / hamiltonian;
    } else {
      cc_v.re = c_const_im / hamiltonian;
      cc_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (c_const_im == 0.0) {
      cc_v.re = v_im / c_const_re;
      cc_v.im = 0.0;
    } else if (v_im == 0.0) {
      cc_v.re = 0.0;
      cc_v.im = -(c_const_im / c_const_re);
    } else {
      cc_v.re = v_im / c_const_re;
      cc_v.im = -(c_const_im / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(c_const_re);
    if (brm > bim) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      cc_v.re = (c_const_im + bim * v_im) / c_const_re;
      cc_v.im = (v_im - bim * c_const_im) / c_const_re;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (c_const_re > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      cc_v.re = (c_const_im * lamX_re + v_im * c_const_re) / brm;
      cc_v.im = (v_im * lamX_re - c_const_im * c_const_re) / brm;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      cc_v.re = (bim * c_const_im + v_im) / c_const_re;
      cc_v.im = (bim * v_im - c_const_im) / c_const_re;
    }
  }

  dc1 = c_mpower(cc_v);
  ar = dc1.re - 1860.0;
  ai = dc1.im;
  if (ai == 0.0) {
    dc0.re = ar / 1560.0;
    dc0.im = 0.0;
  } else if (ar == 0.0) {
    dc0.re = 0.0;
    dc0.im = ai / 1560.0;
  } else {
    dc0.re = ar / 1560.0;
    dc0.im = ai / 1560.0;
  }

  c_asin(&dc0);
  Ttrignew = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    Ttrignew = 0.0;
  }

  emlrtPushRtStackR2012b(&cb_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = mpower(1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0);
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  dc_v.re = xAndLambda[3] * xAndLambda[3];
  dc_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, dc_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(-b_const->alfamax) * (1560.0 * muDoubleScalarSin(Ttrignew)
    + 1860.0);
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  cc_const.re = b_const->mass * xAndLambda[3];
  cc_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig))
                * (b_const->g * b_const->mass + muDoubleScalarSin
                   (-b_const->alfamax) * (1560.0 * muDoubleScalarSin(Ttrignew) +
    1860.0)), cc_const);
  dc_z.re = xAndLambda[2] + 50.0;
  dc_z.im = 0.0;
  v = b_mpower(dc_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        bc_v_re = 0.5;
      } else {
        bc_v_re = -0.5;
      }

      if (v_im > 0.0) {
        bc_v_im = 0.5;
      } else {
        bc_v_im = -0.5;
      }

      re = (ar * bc_v_re + ai * bc_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda[10] * (b_const->g * b_const->mass + muDoubleScalarSin
                      (-b_const->alfamax) * (1560.0 * muDoubleScalarSin(Ttrignew)
    + 1860.0));
  ai = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (b_const->g * b_const->mass + muDoubleScalarSin(-b_const->alfamax) * (1560.0
      * muDoubleScalarSin(Ttrignew) + 1860.0));
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        dc_const_re = 0.5;
      } else {
        dc_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        dc_const_im = 0.5;
      } else {
        dc_const_im = -0.5;
      }

      bim = (ar * dc_const_re + ai * dc_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  emlrtPopRtStackR2012b(&cb_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = -1.5707963267948966;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&db_emlrtRSI, emlrtRootTLSGlobal);
  banktrig = 3.1416 / (2.0 * b_const->bankmax);
  b_asin(&banktrig);
  emlrtPopRtStackR2012b(&db_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(banktrig) || muDoubleScalarIsInf(banktrig)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  /*  Coefficients */
  dc0 = gam;
  b_cos(&dc0);
  a = gam;
  b_cos(&a);
  ec_z.re = xAndLambda[2] + 50.0;
  ec_z.im = 0.0;
  dc1 = b_mpower(ec_z);
  v_re = xAndLambda[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda[9] * muDoubleScalarCos(-b_const->alfamax));
  ai = -(0.0 * muDoubleScalarCos(-b_const->alfamax));
  if (ai == 0.0) {
    re = ar / b_const->mass;
    lamY_im = 0.0;
  } else if (ar == 0.0) {
    re = 0.0;
    lamY_im = ai / b_const->mass;
  } else {
    re = ar / b_const->mass;
    lamY_im = ai / b_const->mass;
  }

  ar = muDoubleScalarSin(-b_const->alfamax) * (1560.0 * xAndLambda[11]) *
    muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig));
  ai = muDoubleScalarSin(-b_const->alfamax) * 0.0 * muDoubleScalarCos
    (b_const->bankmax * muDoubleScalarSin(banktrig));
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_re = b_const->mass * 0.0;
  if (c_const_re == 0.0) {
    if (ai == 0.0) {
      lamY_re = ar / hamiltonian;
      lamX_im = 0.0;
    } else if (ar == 0.0) {
      lamY_re = 0.0;
      lamX_im = ai / hamiltonian;
    } else {
      lamY_re = ar / hamiltonian;
      lamX_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      lamY_re = ai / c_const_re;
      lamX_im = 0.0;
    } else if (ai == 0.0) {
      lamY_re = 0.0;
      lamX_im = -(ar / c_const_re);
    } else {
      lamY_re = ai / c_const_re;
      lamX_im = -(ar / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > c_const_re) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      lamY_re = (ar + bim * ai) / c_const_re;
      lamX_im = (ai - bim * ar) / c_const_re;
    } else if (c_const_re == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      lamY_re = (ar * lamX_re + ai * -0.5) / 0.0;
      lamX_im = (ai * lamX_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      lamY_re = (bim * ar + ai) / c_const_re;
      lamX_im = (bim * ai - ar) / c_const_re;
    }
  }

  const_re = b_const->mass * xAndLambda[3];
  const_im = b_const->mass * 0.0;
  b_const_re = const_re * a.re - const_im * a.im;
  const_im = const_re * a.im + const_im * a.re;
  ar = muDoubleScalarSin(-b_const->alfamax) * (1560.0 * xAndLambda[10]) *
    muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig));
  ai = muDoubleScalarSin(-b_const->alfamax) * 0.0 * muDoubleScalarSin
    (b_const->bankmax * muDoubleScalarSin(banktrig));
  if (const_im == 0.0) {
    if (ai == 0.0) {
      c_const_im = ar / b_const_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      c_const_im = 0.0;
      hamiltonian = ai / b_const_re;
    } else {
      c_const_im = ar / b_const_re;
      hamiltonian = ai / b_const_re;
    }
  } else if (b_const_re == 0.0) {
    if (ar == 0.0) {
      c_const_im = ai / const_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      c_const_im = 0.0;
      hamiltonian = -(ar / const_im);
    } else {
      c_const_im = ai / const_im;
      hamiltonian = -(ar / const_im);
    }
  } else {
    brm = muDoubleScalarAbs(b_const_re);
    bim = muDoubleScalarAbs(const_im);
    if (brm > bim) {
      bim = const_im / b_const_re;
      c_const_re = b_const_re + bim * const_im;
      c_const_im = (ar + bim * ai) / c_const_re;
      hamiltonian = (ai - bim * ar) / c_const_re;
    } else if (bim == brm) {
      if (b_const_re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (const_im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      c_const_im = (ar * lamX_re + ai * c_const_re) / brm;
      hamiltonian = (ai * lamX_re - ar * c_const_re) / brm;
    } else {
      bim = b_const_re / const_im;
      c_const_re = const_im + bim * b_const_re;
      c_const_im = (bim * ar + ai) / c_const_re;
      hamiltonian = (bim * ai - ar) / c_const_re;
    }
  }

  re = (re - lamY_re) - c_const_im;
  lamY_im = (lamY_im - lamX_im) - hamiltonian;
  c_const_im = v_re * re - v_im * lamY_im;
  v_im = v_re * lamY_im + v_im * re;
  hamiltonian = 8112.0 * dc0.re;
  c_const_re = 8112.0 * dc0.im;
  if (c_const_re == 0.0) {
    if (v_im == 0.0) {
      ec_v.re = c_const_im / hamiltonian;
      ec_v.im = 0.0;
    } else if (c_const_im == 0.0) {
      ec_v.re = 0.0;
      ec_v.im = v_im / hamiltonian;
    } else {
      ec_v.re = c_const_im / hamiltonian;
      ec_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (c_const_im == 0.0) {
      ec_v.re = v_im / c_const_re;
      ec_v.im = 0.0;
    } else if (v_im == 0.0) {
      ec_v.re = 0.0;
      ec_v.im = -(c_const_im / c_const_re);
    } else {
      ec_v.re = v_im / c_const_re;
      ec_v.im = -(c_const_im / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(c_const_re);
    if (brm > bim) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      ec_v.re = (c_const_im + bim * v_im) / c_const_re;
      ec_v.im = (v_im - bim * c_const_im) / c_const_re;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (c_const_re > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      ec_v.re = (c_const_im * lamX_re + v_im * c_const_re) / brm;
      ec_v.im = (v_im * lamX_re - c_const_im * c_const_re) / brm;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      ec_v.re = (bim * c_const_im + v_im) / c_const_re;
      ec_v.im = (bim * v_im - c_const_im) / c_const_re;
    }
  }

  dc1 = c_mpower(ec_v);
  ar = dc1.re - 1860.0;
  ai = dc1.im;
  if (ai == 0.0) {
    dc0.re = ar / 1560.0;
    dc0.im = 0.0;
  } else if (ar == 0.0) {
    dc0.re = 0.0;
    dc0.im = ai / 1560.0;
  } else {
    dc0.re = ar / 1560.0;
    dc0.im = ai / 1560.0;
  }

  c_asin(&dc0);
  Ttrignew = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    Ttrignew = 0.0;
  }

  emlrtPushRtStackR2012b(&eb_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = mpower(1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0);
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  fc_v.re = xAndLambda[3] * xAndLambda[3];
  fc_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, fc_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(-b_const->alfamax) * (1560.0 * muDoubleScalarSin(Ttrignew)
    + 1860.0);
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  dc_const.re = b_const->mass * xAndLambda[3];
  dc_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig))
                * (b_const->g * b_const->mass + muDoubleScalarSin
                   (-b_const->alfamax) * (1560.0 * muDoubleScalarSin(Ttrignew) +
    1860.0)), dc_const);
  fc_z.re = xAndLambda[2] + 50.0;
  fc_z.im = 0.0;
  v = b_mpower(fc_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        cc_v_re = 0.5;
      } else {
        cc_v_re = -0.5;
      }

      if (v_im > 0.0) {
        cc_v_im = 0.5;
      } else {
        cc_v_im = -0.5;
      }

      re = (ar * cc_v_re + ai * cc_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda[10] * (b_const->g * b_const->mass + muDoubleScalarSin
                      (-b_const->alfamax) * (1560.0 * muDoubleScalarSin(Ttrignew)
    + 1860.0));
  ai = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (b_const->g * b_const->mass + muDoubleScalarSin(-b_const->alfamax) * (1560.0
      * muDoubleScalarSin(Ttrignew) + 1860.0));
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        ec_const_re = 0.5;
      } else {
        ec_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        ec_const_im = 0.5;
      } else {
        ec_const_im = -0.5;
      }

      bim = (ar * ec_const_re + ai * ec_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  emlrtPopRtStackR2012b(&eb_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = -1.5707963267948966;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  /*  Coefficients */
  dc0 = gam;
  b_cos(&dc0);
  a = gam;
  b_cos(&a);
  gc_z.re = xAndLambda[2] + 50.0;
  gc_z.im = 0.0;
  dc1 = b_mpower(gc_z);
  v_re = xAndLambda[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda[9] * muDoubleScalarCos(b_const->alfamax));
  ai = -(0.0 * muDoubleScalarCos(b_const->alfamax));
  if (ai == 0.0) {
    re = ar / b_const->mass;
    lamY_im = 0.0;
  } else if (ar == 0.0) {
    re = 0.0;
    lamY_im = ai / b_const->mass;
  } else {
    re = ar / b_const->mass;
    lamY_im = ai / b_const->mass;
  }

  ar = muDoubleScalarSin(b_const->alfamax) * (1560.0 * xAndLambda[11]) *
    muDoubleScalarCos(-b_const->bankmax);
  ai = muDoubleScalarSin(b_const->alfamax) * 0.0 * muDoubleScalarCos
    (-b_const->bankmax);
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_re = b_const->mass * 0.0;
  if (c_const_re == 0.0) {
    if (ai == 0.0) {
      lamY_re = ar / hamiltonian;
      lamX_im = 0.0;
    } else if (ar == 0.0) {
      lamY_re = 0.0;
      lamX_im = ai / hamiltonian;
    } else {
      lamY_re = ar / hamiltonian;
      lamX_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      lamY_re = ai / c_const_re;
      lamX_im = 0.0;
    } else if (ai == 0.0) {
      lamY_re = 0.0;
      lamX_im = -(ar / c_const_re);
    } else {
      lamY_re = ai / c_const_re;
      lamX_im = -(ar / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > c_const_re) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      lamY_re = (ar + bim * ai) / c_const_re;
      lamX_im = (ai - bim * ar) / c_const_re;
    } else if (c_const_re == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      lamY_re = (ar * lamX_re + ai * -0.5) / 0.0;
      lamX_im = (ai * lamX_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      lamY_re = (bim * ar + ai) / c_const_re;
      lamX_im = (bim * ai - ar) / c_const_re;
    }
  }

  const_re = b_const->mass * xAndLambda[3];
  const_im = b_const->mass * 0.0;
  b_const_re = const_re * a.re - const_im * a.im;
  const_im = const_re * a.im + const_im * a.re;
  ar = muDoubleScalarSin(b_const->alfamax) * (1560.0 * xAndLambda[10]) *
    muDoubleScalarSin(-b_const->bankmax);
  ai = muDoubleScalarSin(b_const->alfamax) * 0.0 * muDoubleScalarSin
    (-b_const->bankmax);
  if (const_im == 0.0) {
    if (ai == 0.0) {
      c_const_im = ar / b_const_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      c_const_im = 0.0;
      hamiltonian = ai / b_const_re;
    } else {
      c_const_im = ar / b_const_re;
      hamiltonian = ai / b_const_re;
    }
  } else if (b_const_re == 0.0) {
    if (ar == 0.0) {
      c_const_im = ai / const_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      c_const_im = 0.0;
      hamiltonian = -(ar / const_im);
    } else {
      c_const_im = ai / const_im;
      hamiltonian = -(ar / const_im);
    }
  } else {
    brm = muDoubleScalarAbs(b_const_re);
    bim = muDoubleScalarAbs(const_im);
    if (brm > bim) {
      bim = const_im / b_const_re;
      c_const_re = b_const_re + bim * const_im;
      c_const_im = (ar + bim * ai) / c_const_re;
      hamiltonian = (ai - bim * ar) / c_const_re;
    } else if (bim == brm) {
      if (b_const_re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (const_im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      c_const_im = (ar * lamX_re + ai * c_const_re) / brm;
      hamiltonian = (ai * lamX_re - ar * c_const_re) / brm;
    } else {
      bim = b_const_re / const_im;
      c_const_re = const_im + bim * b_const_re;
      c_const_im = (bim * ar + ai) / c_const_re;
      hamiltonian = (bim * ai - ar) / c_const_re;
    }
  }

  re = (re - lamY_re) - c_const_im;
  lamY_im = (lamY_im - lamX_im) - hamiltonian;
  c_const_im = v_re * re - v_im * lamY_im;
  v_im = v_re * lamY_im + v_im * re;
  hamiltonian = 8112.0 * dc0.re;
  c_const_re = 8112.0 * dc0.im;
  if (c_const_re == 0.0) {
    if (v_im == 0.0) {
      gc_v.re = c_const_im / hamiltonian;
      gc_v.im = 0.0;
    } else if (c_const_im == 0.0) {
      gc_v.re = 0.0;
      gc_v.im = v_im / hamiltonian;
    } else {
      gc_v.re = c_const_im / hamiltonian;
      gc_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (c_const_im == 0.0) {
      gc_v.re = v_im / c_const_re;
      gc_v.im = 0.0;
    } else if (v_im == 0.0) {
      gc_v.re = 0.0;
      gc_v.im = -(c_const_im / c_const_re);
    } else {
      gc_v.re = v_im / c_const_re;
      gc_v.im = -(c_const_im / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(c_const_re);
    if (brm > bim) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      gc_v.re = (c_const_im + bim * v_im) / c_const_re;
      gc_v.im = (v_im - bim * c_const_im) / c_const_re;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (c_const_re > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      gc_v.re = (c_const_im * lamX_re + v_im * c_const_re) / brm;
      gc_v.im = (v_im * lamX_re - c_const_im * c_const_re) / brm;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      gc_v.re = (bim * c_const_im + v_im) / c_const_re;
      gc_v.im = (bim * v_im - c_const_im) / c_const_re;
    }
  }

  dc1 = c_mpower(gc_v);
  ar = dc1.re - 1860.0;
  ai = dc1.im;
  if (ai == 0.0) {
    dc0.re = ar / 1560.0;
    dc0.im = 0.0;
  } else if (ar == 0.0) {
    dc0.re = 0.0;
    dc0.im = ai / 1560.0;
  } else {
    dc0.re = ar / 1560.0;
    dc0.im = ai / 1560.0;
  }

  c_asin(&dc0);
  Ttrignew = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    Ttrignew = 0.0;
  }

  emlrtPushRtStackR2012b(&fb_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = mpower(1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0);
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  hc_v.re = xAndLambda[3] * xAndLambda[3];
  hc_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, hc_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax) * (1560.0 * muDoubleScalarSin(Ttrignew)
    + 1860.0);
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  ec_const.re = b_const->mass * xAndLambda[3];
  ec_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(-b_const->bankmax) * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0)), ec_const);
  hc_z.re = xAndLambda[2] + 50.0;
  hc_z.im = 0.0;
  v = b_mpower(hc_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        dc_v_re = 0.5;
      } else {
        dc_v_re = -0.5;
      }

      if (v_im > 0.0) {
        dc_v_im = 0.5;
      } else {
        dc_v_im = -0.5;
      }

      re = (ar * dc_v_re + ai * dc_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(-b_const->bankmax) * xAndLambda[10] * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(-b_const->bankmax) * 0.0 * (b_const->g * b_const->mass
    + muDoubleScalarSin(b_const->alfamax) * (1560.0 * muDoubleScalarSin(Ttrignew)
    + 1860.0));
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        fc_const_re = 0.5;
      } else {
        fc_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        fc_const_im = 0.5;
      } else {
        fc_const_im = -0.5;
      }

      bim = (ar * fc_const_re + ai * fc_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  emlrtPopRtStackR2012b(&fb_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = -1.5707963267948966;
    *alfatrigSave = 1.5707963267948966;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  /*  Coefficients */
  dc0 = gam;
  b_cos(&dc0);
  a = gam;
  b_cos(&a);
  ic_z.re = xAndLambda[2] + 50.0;
  ic_z.im = 0.0;
  dc1 = b_mpower(ic_z);
  v_re = xAndLambda[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda[9] * muDoubleScalarCos(b_const->alfamax));
  ai = -(0.0 * muDoubleScalarCos(b_const->alfamax));
  if (ai == 0.0) {
    re = ar / b_const->mass;
    lamY_im = 0.0;
  } else if (ar == 0.0) {
    re = 0.0;
    lamY_im = ai / b_const->mass;
  } else {
    re = ar / b_const->mass;
    lamY_im = ai / b_const->mass;
  }

  ar = muDoubleScalarSin(b_const->alfamax) * (1560.0 * xAndLambda[11]) *
    muDoubleScalarCos(b_const->bankmax);
  ai = muDoubleScalarSin(b_const->alfamax) * 0.0 * muDoubleScalarCos
    (b_const->bankmax);
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_re = b_const->mass * 0.0;
  if (c_const_re == 0.0) {
    if (ai == 0.0) {
      lamY_re = ar / hamiltonian;
      lamX_im = 0.0;
    } else if (ar == 0.0) {
      lamY_re = 0.0;
      lamX_im = ai / hamiltonian;
    } else {
      lamY_re = ar / hamiltonian;
      lamX_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      lamY_re = ai / c_const_re;
      lamX_im = 0.0;
    } else if (ai == 0.0) {
      lamY_re = 0.0;
      lamX_im = -(ar / c_const_re);
    } else {
      lamY_re = ai / c_const_re;
      lamX_im = -(ar / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > c_const_re) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      lamY_re = (ar + bim * ai) / c_const_re;
      lamX_im = (ai - bim * ar) / c_const_re;
    } else if (c_const_re == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      lamY_re = (ar * lamX_re + ai * -0.5) / 0.0;
      lamX_im = (ai * lamX_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      lamY_re = (bim * ar + ai) / c_const_re;
      lamX_im = (bim * ai - ar) / c_const_re;
    }
  }

  const_re = b_const->mass * xAndLambda[3];
  const_im = b_const->mass * 0.0;
  b_const_re = const_re * a.re - const_im * a.im;
  const_im = const_re * a.im + const_im * a.re;
  ar = muDoubleScalarSin(b_const->alfamax) * (1560.0 * xAndLambda[10]) *
    muDoubleScalarSin(b_const->bankmax);
  ai = muDoubleScalarSin(b_const->alfamax) * 0.0 * muDoubleScalarSin
    (b_const->bankmax);
  if (const_im == 0.0) {
    if (ai == 0.0) {
      c_const_im = ar / b_const_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      c_const_im = 0.0;
      hamiltonian = ai / b_const_re;
    } else {
      c_const_im = ar / b_const_re;
      hamiltonian = ai / b_const_re;
    }
  } else if (b_const_re == 0.0) {
    if (ar == 0.0) {
      c_const_im = ai / const_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      c_const_im = 0.0;
      hamiltonian = -(ar / const_im);
    } else {
      c_const_im = ai / const_im;
      hamiltonian = -(ar / const_im);
    }
  } else {
    brm = muDoubleScalarAbs(b_const_re);
    bim = muDoubleScalarAbs(const_im);
    if (brm > bim) {
      bim = const_im / b_const_re;
      c_const_re = b_const_re + bim * const_im;
      c_const_im = (ar + bim * ai) / c_const_re;
      hamiltonian = (ai - bim * ar) / c_const_re;
    } else if (bim == brm) {
      if (b_const_re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (const_im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      c_const_im = (ar * lamX_re + ai * c_const_re) / brm;
      hamiltonian = (ai * lamX_re - ar * c_const_re) / brm;
    } else {
      bim = b_const_re / const_im;
      c_const_re = const_im + bim * b_const_re;
      c_const_im = (bim * ar + ai) / c_const_re;
      hamiltonian = (bim * ai - ar) / c_const_re;
    }
  }

  re = (re - lamY_re) - c_const_im;
  lamY_im = (lamY_im - lamX_im) - hamiltonian;
  c_const_im = v_re * re - v_im * lamY_im;
  v_im = v_re * lamY_im + v_im * re;
  hamiltonian = 8112.0 * dc0.re;
  c_const_re = 8112.0 * dc0.im;
  if (c_const_re == 0.0) {
    if (v_im == 0.0) {
      ic_v.re = c_const_im / hamiltonian;
      ic_v.im = 0.0;
    } else if (c_const_im == 0.0) {
      ic_v.re = 0.0;
      ic_v.im = v_im / hamiltonian;
    } else {
      ic_v.re = c_const_im / hamiltonian;
      ic_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (c_const_im == 0.0) {
      ic_v.re = v_im / c_const_re;
      ic_v.im = 0.0;
    } else if (v_im == 0.0) {
      ic_v.re = 0.0;
      ic_v.im = -(c_const_im / c_const_re);
    } else {
      ic_v.re = v_im / c_const_re;
      ic_v.im = -(c_const_im / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(c_const_re);
    if (brm > bim) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      ic_v.re = (c_const_im + bim * v_im) / c_const_re;
      ic_v.im = (v_im - bim * c_const_im) / c_const_re;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (c_const_re > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      ic_v.re = (c_const_im * lamX_re + v_im * c_const_re) / brm;
      ic_v.im = (v_im * lamX_re - c_const_im * c_const_re) / brm;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      ic_v.re = (bim * c_const_im + v_im) / c_const_re;
      ic_v.im = (bim * v_im - c_const_im) / c_const_re;
    }
  }

  dc1 = c_mpower(ic_v);
  ar = dc1.re - 1860.0;
  ai = dc1.im;
  if (ai == 0.0) {
    dc0.re = ar / 1560.0;
    dc0.im = 0.0;
  } else if (ar == 0.0) {
    dc0.re = 0.0;
    dc0.im = ai / 1560.0;
  } else {
    dc0.re = ar / 1560.0;
    dc0.im = ai / 1560.0;
  }

  c_asin(&dc0);
  Ttrignew = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    Ttrignew = 0.0;
  }

  emlrtPushRtStackR2012b(&gb_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = mpower(1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0);
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  jc_v.re = xAndLambda[3] * xAndLambda[3];
  jc_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, jc_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax) * (1560.0 * muDoubleScalarSin(Ttrignew)
    + 1860.0);
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  fc_const.re = b_const->mass * xAndLambda[3];
  fc_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax) * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0)), fc_const);
  jc_z.re = xAndLambda[2] + 50.0;
  jc_z.im = 0.0;
  v = b_mpower(jc_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        ec_v_re = 0.5;
      } else {
        ec_v_re = -0.5;
      }

      if (v_im > 0.0) {
        ec_v_im = 0.5;
      } else {
        ec_v_im = -0.5;
      }

      re = (ar * ec_v_re + ai * ec_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax) * xAndLambda[10] * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(b_const->bankmax) * 0.0 * (b_const->g * b_const->mass +
    muDoubleScalarSin(b_const->alfamax) * (1560.0 * muDoubleScalarSin(Ttrignew)
    + 1860.0));
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        gc_const_re = 0.5;
      } else {
        gc_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        gc_const_im = 0.5;
      } else {
        gc_const_im = -0.5;
      }

      bim = (ar * gc_const_re + ai * gc_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  emlrtPopRtStackR2012b(&gb_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = 1.5707963267948966;
    *alfatrigSave = 1.5707963267948966;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&hb_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = 3.1416 / (2.0 * b_const->bankmax);
  b_asin(&hamiltonian);
  banktrig = -hamiltonian;
  emlrtPopRtStackR2012b(&hb_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(-hamiltonian) || muDoubleScalarIsInf(-hamiltonian)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  /*  Coefficients */
  dc0 = gam;
  b_cos(&dc0);
  a = gam;
  b_cos(&a);
  kc_z.re = xAndLambda[2] + 50.0;
  kc_z.im = 0.0;
  dc1 = b_mpower(kc_z);
  v_re = xAndLambda[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda[9] * muDoubleScalarCos(b_const->alfamax));
  ai = -(0.0 * muDoubleScalarCos(b_const->alfamax));
  if (ai == 0.0) {
    re = ar / b_const->mass;
    lamY_im = 0.0;
  } else if (ar == 0.0) {
    re = 0.0;
    lamY_im = ai / b_const->mass;
  } else {
    re = ar / b_const->mass;
    lamY_im = ai / b_const->mass;
  }

  ar = muDoubleScalarSin(b_const->alfamax) * (1560.0 * xAndLambda[11]) *
    muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig));
  ai = muDoubleScalarSin(b_const->alfamax) * 0.0 * muDoubleScalarCos
    (b_const->bankmax * muDoubleScalarSin(banktrig));
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_re = b_const->mass * 0.0;
  if (c_const_re == 0.0) {
    if (ai == 0.0) {
      lamY_re = ar / hamiltonian;
      lamX_im = 0.0;
    } else if (ar == 0.0) {
      lamY_re = 0.0;
      lamX_im = ai / hamiltonian;
    } else {
      lamY_re = ar / hamiltonian;
      lamX_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      lamY_re = ai / c_const_re;
      lamX_im = 0.0;
    } else if (ai == 0.0) {
      lamY_re = 0.0;
      lamX_im = -(ar / c_const_re);
    } else {
      lamY_re = ai / c_const_re;
      lamX_im = -(ar / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > c_const_re) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      lamY_re = (ar + bim * ai) / c_const_re;
      lamX_im = (ai - bim * ar) / c_const_re;
    } else if (c_const_re == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      lamY_re = (ar * lamX_re + ai * -0.5) / 0.0;
      lamX_im = (ai * lamX_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      lamY_re = (bim * ar + ai) / c_const_re;
      lamX_im = (bim * ai - ar) / c_const_re;
    }
  }

  const_re = b_const->mass * xAndLambda[3];
  const_im = b_const->mass * 0.0;
  b_const_re = const_re * a.re - const_im * a.im;
  const_im = const_re * a.im + const_im * a.re;
  ar = muDoubleScalarSin(b_const->alfamax) * (1560.0 * xAndLambda[10]) *
    muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig));
  ai = muDoubleScalarSin(b_const->alfamax) * 0.0 * muDoubleScalarSin
    (b_const->bankmax * muDoubleScalarSin(banktrig));
  if (const_im == 0.0) {
    if (ai == 0.0) {
      c_const_im = ar / b_const_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      c_const_im = 0.0;
      hamiltonian = ai / b_const_re;
    } else {
      c_const_im = ar / b_const_re;
      hamiltonian = ai / b_const_re;
    }
  } else if (b_const_re == 0.0) {
    if (ar == 0.0) {
      c_const_im = ai / const_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      c_const_im = 0.0;
      hamiltonian = -(ar / const_im);
    } else {
      c_const_im = ai / const_im;
      hamiltonian = -(ar / const_im);
    }
  } else {
    brm = muDoubleScalarAbs(b_const_re);
    bim = muDoubleScalarAbs(const_im);
    if (brm > bim) {
      bim = const_im / b_const_re;
      c_const_re = b_const_re + bim * const_im;
      c_const_im = (ar + bim * ai) / c_const_re;
      hamiltonian = (ai - bim * ar) / c_const_re;
    } else if (bim == brm) {
      if (b_const_re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (const_im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      c_const_im = (ar * lamX_re + ai * c_const_re) / brm;
      hamiltonian = (ai * lamX_re - ar * c_const_re) / brm;
    } else {
      bim = b_const_re / const_im;
      c_const_re = const_im + bim * b_const_re;
      c_const_im = (bim * ar + ai) / c_const_re;
      hamiltonian = (bim * ai - ar) / c_const_re;
    }
  }

  re = (re - lamY_re) - c_const_im;
  lamY_im = (lamY_im - lamX_im) - hamiltonian;
  c_const_im = v_re * re - v_im * lamY_im;
  v_im = v_re * lamY_im + v_im * re;
  hamiltonian = 8112.0 * dc0.re;
  c_const_re = 8112.0 * dc0.im;
  if (c_const_re == 0.0) {
    if (v_im == 0.0) {
      kc_v.re = c_const_im / hamiltonian;
      kc_v.im = 0.0;
    } else if (c_const_im == 0.0) {
      kc_v.re = 0.0;
      kc_v.im = v_im / hamiltonian;
    } else {
      kc_v.re = c_const_im / hamiltonian;
      kc_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (c_const_im == 0.0) {
      kc_v.re = v_im / c_const_re;
      kc_v.im = 0.0;
    } else if (v_im == 0.0) {
      kc_v.re = 0.0;
      kc_v.im = -(c_const_im / c_const_re);
    } else {
      kc_v.re = v_im / c_const_re;
      kc_v.im = -(c_const_im / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(c_const_re);
    if (brm > bim) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      kc_v.re = (c_const_im + bim * v_im) / c_const_re;
      kc_v.im = (v_im - bim * c_const_im) / c_const_re;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (c_const_re > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      kc_v.re = (c_const_im * lamX_re + v_im * c_const_re) / brm;
      kc_v.im = (v_im * lamX_re - c_const_im * c_const_re) / brm;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      kc_v.re = (bim * c_const_im + v_im) / c_const_re;
      kc_v.im = (bim * v_im - c_const_im) / c_const_re;
    }
  }

  dc1 = c_mpower(kc_v);
  ar = dc1.re - 1860.0;
  ai = dc1.im;
  if (ai == 0.0) {
    dc0.re = ar / 1560.0;
    dc0.im = 0.0;
  } else if (ar == 0.0) {
    dc0.re = 0.0;
    dc0.im = ai / 1560.0;
  } else {
    dc0.re = ar / 1560.0;
    dc0.im = ai / 1560.0;
  }

  c_asin(&dc0);
  Ttrignew = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    Ttrignew = 0.0;
  }

  emlrtPushRtStackR2012b(&ib_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = mpower(1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0);
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  lc_v.re = xAndLambda[3] * xAndLambda[3];
  lc_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, lc_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax) * (1560.0 * muDoubleScalarSin(Ttrignew)
    + 1860.0);
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  gc_const.re = b_const->mass * xAndLambda[3];
  gc_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig))
                * (b_const->g * b_const->mass + muDoubleScalarSin
                   (b_const->alfamax) * (1560.0 * muDoubleScalarSin(Ttrignew) +
    1860.0)), gc_const);
  lc_z.re = xAndLambda[2] + 50.0;
  lc_z.im = 0.0;
  v = b_mpower(lc_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        fc_v_re = 0.5;
      } else {
        fc_v_re = -0.5;
      }

      if (v_im > 0.0) {
        fc_v_im = 0.5;
      } else {
        fc_v_im = -0.5;
      }

      re = (ar * fc_v_re + ai * fc_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda[10] * (b_const->g * b_const->mass + muDoubleScalarSin
                      (b_const->alfamax) * (1560.0 * muDoubleScalarSin(Ttrignew)
    + 1860.0));
  ai = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (b_const->g * b_const->mass + muDoubleScalarSin(b_const->alfamax) * (1560.0 *
      muDoubleScalarSin(Ttrignew) + 1860.0));
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        hc_const_re = 0.5;
      } else {
        hc_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        hc_const_im = 0.5;
      } else {
        hc_const_im = -0.5;
      }

      bim = (ar * hc_const_re + ai * hc_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  emlrtPopRtStackR2012b(&ib_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = 1.5707963267948966;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&jb_emlrtRSI, emlrtRootTLSGlobal);
  banktrig = 3.1416 / (2.0 * b_const->bankmax);
  b_asin(&banktrig);
  emlrtPopRtStackR2012b(&jb_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(banktrig) || muDoubleScalarIsInf(banktrig)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  /*  Coefficients */
  dc0 = gam;
  b_cos(&dc0);
  a = gam;
  b_cos(&a);
  mc_z.re = xAndLambda[2] + 50.0;
  mc_z.im = 0.0;
  dc1 = b_mpower(mc_z);
  v_re = xAndLambda[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda[9] * muDoubleScalarCos(b_const->alfamax));
  ai = -(0.0 * muDoubleScalarCos(b_const->alfamax));
  if (ai == 0.0) {
    re = ar / b_const->mass;
    lamY_im = 0.0;
  } else if (ar == 0.0) {
    re = 0.0;
    lamY_im = ai / b_const->mass;
  } else {
    re = ar / b_const->mass;
    lamY_im = ai / b_const->mass;
  }

  ar = muDoubleScalarSin(b_const->alfamax) * (1560.0 * xAndLambda[11]) *
    muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig));
  ai = muDoubleScalarSin(b_const->alfamax) * 0.0 * muDoubleScalarCos
    (b_const->bankmax * muDoubleScalarSin(banktrig));
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_re = b_const->mass * 0.0;
  if (c_const_re == 0.0) {
    if (ai == 0.0) {
      lamY_re = ar / hamiltonian;
      lamX_im = 0.0;
    } else if (ar == 0.0) {
      lamY_re = 0.0;
      lamX_im = ai / hamiltonian;
    } else {
      lamY_re = ar / hamiltonian;
      lamX_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      lamY_re = ai / c_const_re;
      lamX_im = 0.0;
    } else if (ai == 0.0) {
      lamY_re = 0.0;
      lamX_im = -(ar / c_const_re);
    } else {
      lamY_re = ai / c_const_re;
      lamX_im = -(ar / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > c_const_re) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      lamY_re = (ar + bim * ai) / c_const_re;
      lamX_im = (ai - bim * ar) / c_const_re;
    } else if (c_const_re == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      lamY_re = (ar * lamX_re + ai * -0.5) / 0.0;
      lamX_im = (ai * lamX_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      lamY_re = (bim * ar + ai) / c_const_re;
      lamX_im = (bim * ai - ar) / c_const_re;
    }
  }

  const_re = b_const->mass * xAndLambda[3];
  const_im = b_const->mass * 0.0;
  b_const_re = const_re * a.re - const_im * a.im;
  const_im = const_re * a.im + const_im * a.re;
  ar = muDoubleScalarSin(b_const->alfamax) * (1560.0 * xAndLambda[10]) *
    muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig));
  ai = muDoubleScalarSin(b_const->alfamax) * 0.0 * muDoubleScalarSin
    (b_const->bankmax * muDoubleScalarSin(banktrig));
  if (const_im == 0.0) {
    if (ai == 0.0) {
      c_const_im = ar / b_const_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      c_const_im = 0.0;
      hamiltonian = ai / b_const_re;
    } else {
      c_const_im = ar / b_const_re;
      hamiltonian = ai / b_const_re;
    }
  } else if (b_const_re == 0.0) {
    if (ar == 0.0) {
      c_const_im = ai / const_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      c_const_im = 0.0;
      hamiltonian = -(ar / const_im);
    } else {
      c_const_im = ai / const_im;
      hamiltonian = -(ar / const_im);
    }
  } else {
    brm = muDoubleScalarAbs(b_const_re);
    bim = muDoubleScalarAbs(const_im);
    if (brm > bim) {
      bim = const_im / b_const_re;
      c_const_re = b_const_re + bim * const_im;
      c_const_im = (ar + bim * ai) / c_const_re;
      hamiltonian = (ai - bim * ar) / c_const_re;
    } else if (bim == brm) {
      if (b_const_re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (const_im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      c_const_im = (ar * lamX_re + ai * c_const_re) / brm;
      hamiltonian = (ai * lamX_re - ar * c_const_re) / brm;
    } else {
      bim = b_const_re / const_im;
      c_const_re = const_im + bim * b_const_re;
      c_const_im = (bim * ar + ai) / c_const_re;
      hamiltonian = (bim * ai - ar) / c_const_re;
    }
  }

  re = (re - lamY_re) - c_const_im;
  lamY_im = (lamY_im - lamX_im) - hamiltonian;
  c_const_im = v_re * re - v_im * lamY_im;
  v_im = v_re * lamY_im + v_im * re;
  hamiltonian = 8112.0 * dc0.re;
  c_const_re = 8112.0 * dc0.im;
  if (c_const_re == 0.0) {
    if (v_im == 0.0) {
      mc_v.re = c_const_im / hamiltonian;
      mc_v.im = 0.0;
    } else if (c_const_im == 0.0) {
      mc_v.re = 0.0;
      mc_v.im = v_im / hamiltonian;
    } else {
      mc_v.re = c_const_im / hamiltonian;
      mc_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (c_const_im == 0.0) {
      mc_v.re = v_im / c_const_re;
      mc_v.im = 0.0;
    } else if (v_im == 0.0) {
      mc_v.re = 0.0;
      mc_v.im = -(c_const_im / c_const_re);
    } else {
      mc_v.re = v_im / c_const_re;
      mc_v.im = -(c_const_im / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(c_const_re);
    if (brm > bim) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      mc_v.re = (c_const_im + bim * v_im) / c_const_re;
      mc_v.im = (v_im - bim * c_const_im) / c_const_re;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (c_const_re > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      mc_v.re = (c_const_im * lamX_re + v_im * c_const_re) / brm;
      mc_v.im = (v_im * lamX_re - c_const_im * c_const_re) / brm;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      mc_v.re = (bim * c_const_im + v_im) / c_const_re;
      mc_v.im = (bim * v_im - c_const_im) / c_const_re;
    }
  }

  dc1 = c_mpower(mc_v);
  ar = dc1.re - 1860.0;
  ai = dc1.im;
  if (ai == 0.0) {
    dc0.re = ar / 1560.0;
    dc0.im = 0.0;
  } else if (ar == 0.0) {
    dc0.re = 0.0;
    dc0.im = ai / 1560.0;
  } else {
    dc0.re = ar / 1560.0;
    dc0.im = ai / 1560.0;
  }

  c_asin(&dc0);
  Ttrignew = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    Ttrignew = 0.0;
  }

  emlrtPushRtStackR2012b(&kb_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = mpower(1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0);
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  nc_v.re = xAndLambda[3] * xAndLambda[3];
  nc_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, nc_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax) * (1560.0 * muDoubleScalarSin(Ttrignew)
    + 1860.0);
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  hc_const.re = b_const->mass * xAndLambda[3];
  hc_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig))
                * (b_const->g * b_const->mass + muDoubleScalarSin
                   (b_const->alfamax) * (1560.0 * muDoubleScalarSin(Ttrignew) +
    1860.0)), hc_const);
  nc_z.re = xAndLambda[2] + 50.0;
  nc_z.im = 0.0;
  v = b_mpower(nc_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        gc_v_re = 0.5;
      } else {
        gc_v_re = -0.5;
      }

      if (v_im > 0.0) {
        gc_v_im = 0.5;
      } else {
        gc_v_im = -0.5;
      }

      re = (ar * gc_v_re + ai * gc_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda[10] * (b_const->g * b_const->mass + muDoubleScalarSin
                      (b_const->alfamax) * (1560.0 * muDoubleScalarSin(Ttrignew)
    + 1860.0));
  ai = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (b_const->g * b_const->mass + muDoubleScalarSin(b_const->alfamax) * (1560.0 *
      muDoubleScalarSin(Ttrignew) + 1860.0));
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        ic_const_re = 0.5;
      } else {
        ic_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        ic_const_im = 0.5;
      } else {
        ic_const_im = -0.5;
      }

      bim = (ar * ic_const_re + ai * ic_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  emlrtPopRtStackR2012b(&kb_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = 1.5707963267948966;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(-b_const->bankmax);
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(-b_const->bankmax);
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(-(2.0 * b_const->bankmax));
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(-(2.0 * b_const->bankmax));
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew = 0.0;
    } else if (b_const_im == 0.0) {
      hamiltonian = 0.0;
      Ttrignew /= dc0.re;
    } else {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = 0.0;
    } else if (Ttrignew == 0.0) {
      hamiltonian = 0.0;
      Ttrignew = -(b_const_im / dc0.im);
    } else {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = -(b_const_im / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      hamiltonian = (b_const_im + bim * Ttrignew) / c_const_re;
      Ttrignew = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      hamiltonian = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      Ttrignew = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      hamiltonian = (bim * b_const_im + Ttrignew) / c_const_re;
      Ttrignew = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -Ttrignew;
  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = -dc0.re;
  if (muDoubleScalarIsNaN(-dc0.re) || muDoubleScalarIsInf(-dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_cos(&dc0);
  a = gam;
  b_cos(&a);
  oc_z.re = xAndLambda[2] + 50.0;
  oc_z.im = 0.0;
  dc1 = b_mpower(oc_z);
  v_re = xAndLambda[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda[9] * muDoubleScalarCos(b_const->alfamax *
          muDoubleScalarSin(alfatrig)));
  ai = -(0.0 * muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)));
  if (ai == 0.0) {
    re = ar / b_const->mass;
    lamY_im = 0.0;
  } else if (ar == 0.0) {
    re = 0.0;
    lamY_im = ai / b_const->mass;
  } else {
    re = ar / b_const->mass;
    lamY_im = ai / b_const->mass;
  }

  ar = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * xAndLambda[11]) * muDoubleScalarCos(-b_const->bankmax);
  ai = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarCos(-b_const->bankmax);
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_re = b_const->mass * 0.0;
  if (c_const_re == 0.0) {
    if (ai == 0.0) {
      lamY_re = ar / hamiltonian;
      lamX_im = 0.0;
    } else if (ar == 0.0) {
      lamY_re = 0.0;
      lamX_im = ai / hamiltonian;
    } else {
      lamY_re = ar / hamiltonian;
      lamX_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      lamY_re = ai / c_const_re;
      lamX_im = 0.0;
    } else if (ai == 0.0) {
      lamY_re = 0.0;
      lamX_im = -(ar / c_const_re);
    } else {
      lamY_re = ai / c_const_re;
      lamX_im = -(ar / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > c_const_re) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      lamY_re = (ar + bim * ai) / c_const_re;
      lamX_im = (ai - bim * ar) / c_const_re;
    } else if (c_const_re == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      lamY_re = (ar * lamX_re + ai * -0.5) / 0.0;
      lamX_im = (ai * lamX_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      lamY_re = (bim * ar + ai) / c_const_re;
      lamX_im = (bim * ai - ar) / c_const_re;
    }
  }

  const_re = b_const->mass * xAndLambda[3];
  const_im = b_const->mass * 0.0;
  b_const_re = const_re * a.re - const_im * a.im;
  const_im = const_re * a.im + const_im * a.re;
  ar = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * xAndLambda[10]) * muDoubleScalarSin(-b_const->bankmax);
  ai = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarSin(-b_const->bankmax);
  if (const_im == 0.0) {
    if (ai == 0.0) {
      c_const_im = ar / b_const_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      c_const_im = 0.0;
      hamiltonian = ai / b_const_re;
    } else {
      c_const_im = ar / b_const_re;
      hamiltonian = ai / b_const_re;
    }
  } else if (b_const_re == 0.0) {
    if (ar == 0.0) {
      c_const_im = ai / const_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      c_const_im = 0.0;
      hamiltonian = -(ar / const_im);
    } else {
      c_const_im = ai / const_im;
      hamiltonian = -(ar / const_im);
    }
  } else {
    brm = muDoubleScalarAbs(b_const_re);
    bim = muDoubleScalarAbs(const_im);
    if (brm > bim) {
      bim = const_im / b_const_re;
      c_const_re = b_const_re + bim * const_im;
      c_const_im = (ar + bim * ai) / c_const_re;
      hamiltonian = (ai - bim * ar) / c_const_re;
    } else if (bim == brm) {
      if (b_const_re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (const_im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      c_const_im = (ar * lamX_re + ai * c_const_re) / brm;
      hamiltonian = (ai * lamX_re - ar * c_const_re) / brm;
    } else {
      bim = b_const_re / const_im;
      c_const_re = const_im + bim * b_const_re;
      c_const_im = (bim * ar + ai) / c_const_re;
      hamiltonian = (bim * ai - ar) / c_const_re;
    }
  }

  re = (re - lamY_re) - c_const_im;
  lamY_im = (lamY_im - lamX_im) - hamiltonian;
  c_const_im = v_re * re - v_im * lamY_im;
  v_im = v_re * lamY_im + v_im * re;
  hamiltonian = 8112.0 * dc0.re;
  c_const_re = 8112.0 * dc0.im;
  if (c_const_re == 0.0) {
    if (v_im == 0.0) {
      oc_v.re = c_const_im / hamiltonian;
      oc_v.im = 0.0;
    } else if (c_const_im == 0.0) {
      oc_v.re = 0.0;
      oc_v.im = v_im / hamiltonian;
    } else {
      oc_v.re = c_const_im / hamiltonian;
      oc_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (c_const_im == 0.0) {
      oc_v.re = v_im / c_const_re;
      oc_v.im = 0.0;
    } else if (v_im == 0.0) {
      oc_v.re = 0.0;
      oc_v.im = -(c_const_im / c_const_re);
    } else {
      oc_v.re = v_im / c_const_re;
      oc_v.im = -(c_const_im / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(c_const_re);
    if (brm > bim) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      oc_v.re = (c_const_im + bim * v_im) / c_const_re;
      oc_v.im = (v_im - bim * c_const_im) / c_const_re;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (c_const_re > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      oc_v.re = (c_const_im * lamX_re + v_im * c_const_re) / brm;
      oc_v.im = (v_im * lamX_re - c_const_im * c_const_re) / brm;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      oc_v.re = (bim * c_const_im + v_im) / c_const_re;
      oc_v.im = (bim * v_im - c_const_im) / c_const_re;
    }
  }

  dc1 = c_mpower(oc_v);
  ar = dc1.re - 1860.0;
  ai = dc1.im;
  if (ai == 0.0) {
    dc0.re = ar / 1560.0;
    dc0.im = 0.0;
  } else if (ar == 0.0) {
    dc0.re = 0.0;
    dc0.im = ai / 1560.0;
  } else {
    dc0.re = ar / 1560.0;
    dc0.im = ai / 1560.0;
  }

  c_asin(&dc0);
  Ttrignew = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    Ttrignew = 0.0;
  }

  emlrtPushRtStackR2012b(&lb_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = mpower(1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0);
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  pc_v.re = xAndLambda[3] * xAndLambda[3];
  pc_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, pc_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0);
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  ic_const.re = b_const->mass * xAndLambda[3];
  ic_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(-b_const->bankmax) * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0)), ic_const);
  pc_z.re = xAndLambda[2] + 50.0;
  pc_z.im = 0.0;
  v = b_mpower(pc_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        hc_v_re = 0.5;
      } else {
        hc_v_re = -0.5;
      }

      if (v_im > 0.0) {
        hc_v_im = 0.5;
      } else {
        hc_v_im = -0.5;
      }

      re = (ar * hc_v_re + ai * hc_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(-b_const->bankmax) * xAndLambda[10] * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(-b_const->bankmax) * 0.0 * (b_const->g * b_const->mass
    + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0));
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        jc_const_re = 0.5;
      } else {
        jc_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        jc_const_im = 0.5;
      } else {
        jc_const_im = -0.5;
      }

      bim = (ar * jc_const_re + ai * jc_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  emlrtPopRtStackR2012b(&lb_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = -1.5707963267948966;
    *alfatrigSave = alfatrig;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(b_const->bankmax);
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(b_const->bankmax);
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(2.0 * b_const->bankmax);
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(2.0 * b_const->bankmax);
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew = 0.0;
    } else if (b_const_im == 0.0) {
      hamiltonian = 0.0;
      Ttrignew /= dc0.re;
    } else {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = 0.0;
    } else if (Ttrignew == 0.0) {
      hamiltonian = 0.0;
      Ttrignew = -(b_const_im / dc0.im);
    } else {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = -(b_const_im / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      hamiltonian = (b_const_im + bim * Ttrignew) / c_const_re;
      Ttrignew = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      hamiltonian = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      Ttrignew = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      hamiltonian = (bim * b_const_im + Ttrignew) / c_const_re;
      Ttrignew = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -Ttrignew;
  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = -dc0.re;
  if (muDoubleScalarIsNaN(-dc0.re) || muDoubleScalarIsInf(-dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_cos(&dc0);
  a = gam;
  b_cos(&a);
  qc_z.re = xAndLambda[2] + 50.0;
  qc_z.im = 0.0;
  dc1 = b_mpower(qc_z);
  v_re = xAndLambda[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda[9] * muDoubleScalarCos(b_const->alfamax *
          muDoubleScalarSin(alfatrig)));
  ai = -(0.0 * muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)));
  if (ai == 0.0) {
    re = ar / b_const->mass;
    lamY_im = 0.0;
  } else if (ar == 0.0) {
    re = 0.0;
    lamY_im = ai / b_const->mass;
  } else {
    re = ar / b_const->mass;
    lamY_im = ai / b_const->mass;
  }

  ar = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * xAndLambda[11]) * muDoubleScalarCos(b_const->bankmax);
  ai = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarCos(b_const->bankmax);
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_re = b_const->mass * 0.0;
  if (c_const_re == 0.0) {
    if (ai == 0.0) {
      lamY_re = ar / hamiltonian;
      lamX_im = 0.0;
    } else if (ar == 0.0) {
      lamY_re = 0.0;
      lamX_im = ai / hamiltonian;
    } else {
      lamY_re = ar / hamiltonian;
      lamX_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      lamY_re = ai / c_const_re;
      lamX_im = 0.0;
    } else if (ai == 0.0) {
      lamY_re = 0.0;
      lamX_im = -(ar / c_const_re);
    } else {
      lamY_re = ai / c_const_re;
      lamX_im = -(ar / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > c_const_re) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      lamY_re = (ar + bim * ai) / c_const_re;
      lamX_im = (ai - bim * ar) / c_const_re;
    } else if (c_const_re == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      lamY_re = (ar * lamX_re + ai * -0.5) / 0.0;
      lamX_im = (ai * lamX_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      lamY_re = (bim * ar + ai) / c_const_re;
      lamX_im = (bim * ai - ar) / c_const_re;
    }
  }

  const_re = b_const->mass * xAndLambda[3];
  const_im = b_const->mass * 0.0;
  b_const_re = const_re * a.re - const_im * a.im;
  const_im = const_re * a.im + const_im * a.re;
  ar = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * xAndLambda[10]) * muDoubleScalarSin(b_const->bankmax);
  ai = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarSin(b_const->bankmax);
  if (const_im == 0.0) {
    if (ai == 0.0) {
      c_const_im = ar / b_const_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      c_const_im = 0.0;
      hamiltonian = ai / b_const_re;
    } else {
      c_const_im = ar / b_const_re;
      hamiltonian = ai / b_const_re;
    }
  } else if (b_const_re == 0.0) {
    if (ar == 0.0) {
      c_const_im = ai / const_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      c_const_im = 0.0;
      hamiltonian = -(ar / const_im);
    } else {
      c_const_im = ai / const_im;
      hamiltonian = -(ar / const_im);
    }
  } else {
    brm = muDoubleScalarAbs(b_const_re);
    bim = muDoubleScalarAbs(const_im);
    if (brm > bim) {
      bim = const_im / b_const_re;
      c_const_re = b_const_re + bim * const_im;
      c_const_im = (ar + bim * ai) / c_const_re;
      hamiltonian = (ai - bim * ar) / c_const_re;
    } else if (bim == brm) {
      if (b_const_re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (const_im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      c_const_im = (ar * lamX_re + ai * c_const_re) / brm;
      hamiltonian = (ai * lamX_re - ar * c_const_re) / brm;
    } else {
      bim = b_const_re / const_im;
      c_const_re = const_im + bim * b_const_re;
      c_const_im = (bim * ar + ai) / c_const_re;
      hamiltonian = (bim * ai - ar) / c_const_re;
    }
  }

  re = (re - lamY_re) - c_const_im;
  lamY_im = (lamY_im - lamX_im) - hamiltonian;
  c_const_im = v_re * re - v_im * lamY_im;
  v_im = v_re * lamY_im + v_im * re;
  hamiltonian = 8112.0 * dc0.re;
  c_const_re = 8112.0 * dc0.im;
  if (c_const_re == 0.0) {
    if (v_im == 0.0) {
      qc_v.re = c_const_im / hamiltonian;
      qc_v.im = 0.0;
    } else if (c_const_im == 0.0) {
      qc_v.re = 0.0;
      qc_v.im = v_im / hamiltonian;
    } else {
      qc_v.re = c_const_im / hamiltonian;
      qc_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (c_const_im == 0.0) {
      qc_v.re = v_im / c_const_re;
      qc_v.im = 0.0;
    } else if (v_im == 0.0) {
      qc_v.re = 0.0;
      qc_v.im = -(c_const_im / c_const_re);
    } else {
      qc_v.re = v_im / c_const_re;
      qc_v.im = -(c_const_im / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(c_const_re);
    if (brm > bim) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      qc_v.re = (c_const_im + bim * v_im) / c_const_re;
      qc_v.im = (v_im - bim * c_const_im) / c_const_re;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (c_const_re > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      qc_v.re = (c_const_im * lamX_re + v_im * c_const_re) / brm;
      qc_v.im = (v_im * lamX_re - c_const_im * c_const_re) / brm;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      qc_v.re = (bim * c_const_im + v_im) / c_const_re;
      qc_v.im = (bim * v_im - c_const_im) / c_const_re;
    }
  }

  dc1 = c_mpower(qc_v);
  ar = dc1.re - 1860.0;
  ai = dc1.im;
  if (ai == 0.0) {
    dc0.re = ar / 1560.0;
    dc0.im = 0.0;
  } else if (ar == 0.0) {
    dc0.re = 0.0;
    dc0.im = ai / 1560.0;
  } else {
    dc0.re = ar / 1560.0;
    dc0.im = ai / 1560.0;
  }

  c_asin(&dc0);
  Ttrignew = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    Ttrignew = 0.0;
  }

  emlrtPushRtStackR2012b(&mb_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = mpower(1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0);
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  rc_v.re = xAndLambda[3] * xAndLambda[3];
  rc_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, rc_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0);
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  jc_const.re = b_const->mass * xAndLambda[3];
  jc_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax) * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0)), jc_const);
  rc_z.re = xAndLambda[2] + 50.0;
  rc_z.im = 0.0;
  v = b_mpower(rc_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        ic_v_re = 0.5;
      } else {
        ic_v_re = -0.5;
      }

      if (v_im > 0.0) {
        ic_v_im = 0.5;
      } else {
        ic_v_im = -0.5;
      }

      re = (ar * ic_v_re + ai * ic_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax) * xAndLambda[10] * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(b_const->bankmax) * 0.0 * (b_const->g * b_const->mass +
    muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0));
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        kc_const_re = 0.5;
      } else {
        kc_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        kc_const_im = 0.5;
      } else {
        kc_const_im = -0.5;
      }

      bim = (ar * kc_const_re + ai * kc_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  emlrtPopRtStackR2012b(&mb_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = 1.5707963267948966;
    *alfatrigSave = alfatrig;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&nb_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = 3.1416 / (2.0 * b_const->bankmax);
  b_asin(&hamiltonian);
  banktrig = -hamiltonian;
  emlrtPopRtStackR2012b(&nb_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(-hamiltonian) || muDoubleScalarIsInf(-hamiltonian)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(2.0 * b_const->bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(2.0 * b_const->bankmax * muDoubleScalarSin(banktrig));
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew = 0.0;
    } else if (b_const_im == 0.0) {
      hamiltonian = 0.0;
      Ttrignew /= dc0.re;
    } else {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = 0.0;
    } else if (Ttrignew == 0.0) {
      hamiltonian = 0.0;
      Ttrignew = -(b_const_im / dc0.im);
    } else {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = -(b_const_im / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      hamiltonian = (b_const_im + bim * Ttrignew) / c_const_re;
      Ttrignew = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      hamiltonian = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      Ttrignew = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      hamiltonian = (bim * b_const_im + Ttrignew) / c_const_re;
      Ttrignew = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -Ttrignew;
  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = -dc0.re;
  if (muDoubleScalarIsNaN(-dc0.re) || muDoubleScalarIsInf(-dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_cos(&dc0);
  a = gam;
  b_cos(&a);
  sc_z.re = xAndLambda[2] + 50.0;
  sc_z.im = 0.0;
  dc1 = b_mpower(sc_z);
  v_re = xAndLambda[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda[9] * muDoubleScalarCos(b_const->alfamax *
          muDoubleScalarSin(alfatrig)));
  ai = -(0.0 * muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)));
  if (ai == 0.0) {
    re = ar / b_const->mass;
    lamY_im = 0.0;
  } else if (ar == 0.0) {
    re = 0.0;
    lamY_im = ai / b_const->mass;
  } else {
    re = ar / b_const->mass;
    lamY_im = ai / b_const->mass;
  }

  ar = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * xAndLambda[11]) * muDoubleScalarCos(b_const->bankmax *
    muDoubleScalarSin(banktrig));
  ai = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig));
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_re = b_const->mass * 0.0;
  if (c_const_re == 0.0) {
    if (ai == 0.0) {
      lamY_re = ar / hamiltonian;
      lamX_im = 0.0;
    } else if (ar == 0.0) {
      lamY_re = 0.0;
      lamX_im = ai / hamiltonian;
    } else {
      lamY_re = ar / hamiltonian;
      lamX_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      lamY_re = ai / c_const_re;
      lamX_im = 0.0;
    } else if (ai == 0.0) {
      lamY_re = 0.0;
      lamX_im = -(ar / c_const_re);
    } else {
      lamY_re = ai / c_const_re;
      lamX_im = -(ar / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > c_const_re) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      lamY_re = (ar + bim * ai) / c_const_re;
      lamX_im = (ai - bim * ar) / c_const_re;
    } else if (c_const_re == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      lamY_re = (ar * lamX_re + ai * -0.5) / 0.0;
      lamX_im = (ai * lamX_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      lamY_re = (bim * ar + ai) / c_const_re;
      lamX_im = (bim * ai - ar) / c_const_re;
    }
  }

  const_re = b_const->mass * xAndLambda[3];
  const_im = b_const->mass * 0.0;
  b_const_re = const_re * a.re - const_im * a.im;
  const_im = const_re * a.im + const_im * a.re;
  ar = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * xAndLambda[10]) * muDoubleScalarSin(b_const->bankmax *
    muDoubleScalarSin(banktrig));
  ai = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig));
  if (const_im == 0.0) {
    if (ai == 0.0) {
      c_const_im = ar / b_const_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      c_const_im = 0.0;
      hamiltonian = ai / b_const_re;
    } else {
      c_const_im = ar / b_const_re;
      hamiltonian = ai / b_const_re;
    }
  } else if (b_const_re == 0.0) {
    if (ar == 0.0) {
      c_const_im = ai / const_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      c_const_im = 0.0;
      hamiltonian = -(ar / const_im);
    } else {
      c_const_im = ai / const_im;
      hamiltonian = -(ar / const_im);
    }
  } else {
    brm = muDoubleScalarAbs(b_const_re);
    bim = muDoubleScalarAbs(const_im);
    if (brm > bim) {
      bim = const_im / b_const_re;
      c_const_re = b_const_re + bim * const_im;
      c_const_im = (ar + bim * ai) / c_const_re;
      hamiltonian = (ai - bim * ar) / c_const_re;
    } else if (bim == brm) {
      if (b_const_re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (const_im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      c_const_im = (ar * lamX_re + ai * c_const_re) / brm;
      hamiltonian = (ai * lamX_re - ar * c_const_re) / brm;
    } else {
      bim = b_const_re / const_im;
      c_const_re = const_im + bim * b_const_re;
      c_const_im = (bim * ar + ai) / c_const_re;
      hamiltonian = (bim * ai - ar) / c_const_re;
    }
  }

  re = (re - lamY_re) - c_const_im;
  lamY_im = (lamY_im - lamX_im) - hamiltonian;
  c_const_im = v_re * re - v_im * lamY_im;
  v_im = v_re * lamY_im + v_im * re;
  hamiltonian = 8112.0 * dc0.re;
  c_const_re = 8112.0 * dc0.im;
  if (c_const_re == 0.0) {
    if (v_im == 0.0) {
      sc_v.re = c_const_im / hamiltonian;
      sc_v.im = 0.0;
    } else if (c_const_im == 0.0) {
      sc_v.re = 0.0;
      sc_v.im = v_im / hamiltonian;
    } else {
      sc_v.re = c_const_im / hamiltonian;
      sc_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (c_const_im == 0.0) {
      sc_v.re = v_im / c_const_re;
      sc_v.im = 0.0;
    } else if (v_im == 0.0) {
      sc_v.re = 0.0;
      sc_v.im = -(c_const_im / c_const_re);
    } else {
      sc_v.re = v_im / c_const_re;
      sc_v.im = -(c_const_im / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(c_const_re);
    if (brm > bim) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      sc_v.re = (c_const_im + bim * v_im) / c_const_re;
      sc_v.im = (v_im - bim * c_const_im) / c_const_re;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (c_const_re > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      sc_v.re = (c_const_im * lamX_re + v_im * c_const_re) / brm;
      sc_v.im = (v_im * lamX_re - c_const_im * c_const_re) / brm;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      sc_v.re = (bim * c_const_im + v_im) / c_const_re;
      sc_v.im = (bim * v_im - c_const_im) / c_const_re;
    }
  }

  dc1 = c_mpower(sc_v);
  ar = dc1.re - 1860.0;
  ai = dc1.im;
  if (ai == 0.0) {
    dc0.re = ar / 1560.0;
    dc0.im = 0.0;
  } else if (ar == 0.0) {
    dc0.re = 0.0;
    dc0.im = ai / 1560.0;
  } else {
    dc0.re = ar / 1560.0;
    dc0.im = ai / 1560.0;
  }

  c_asin(&dc0);
  Ttrignew = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    Ttrignew = 0.0;
  }

  emlrtPushRtStackR2012b(&ob_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = mpower(1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0);
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  tc_v.re = xAndLambda[3] * xAndLambda[3];
  tc_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, tc_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0);
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  kc_const.re = b_const->mass * xAndLambda[3];
  kc_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig))
                * (b_const->g * b_const->mass + muDoubleScalarSin
                   (b_const->alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0)), kc_const);
  tc_z.re = xAndLambda[2] + 50.0;
  tc_z.im = 0.0;
  v = b_mpower(tc_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        jc_v_re = 0.5;
      } else {
        jc_v_re = -0.5;
      }

      if (v_im > 0.0) {
        jc_v_im = 0.5;
      } else {
        jc_v_im = -0.5;
      }

      re = (ar * jc_v_re + ai * jc_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda[10] * (b_const->g * b_const->mass + muDoubleScalarSin
                      (b_const->alfamax * muDoubleScalarSin(alfatrig)) * (1560.0
    * muDoubleScalarSin(Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (b_const->g * b_const->mass + muDoubleScalarSin(b_const->alfamax *
      muDoubleScalarSin(alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) +
      1860.0));
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        lc_const_re = 0.5;
      } else {
        lc_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        lc_const_im = 0.5;
      } else {
        lc_const_im = -0.5;
      }

      bim = (ar * lc_const_re + ai * lc_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  emlrtPopRtStackR2012b(&ob_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&pb_emlrtRSI, emlrtRootTLSGlobal);
  banktrig = 3.1416 / (2.0 * b_const->bankmax);
  b_asin(&banktrig);
  emlrtPopRtStackR2012b(&pb_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(banktrig) || muDoubleScalarIsInf(banktrig)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(2.0 * b_const->bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(2.0 * b_const->bankmax * muDoubleScalarSin(banktrig));
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew = 0.0;
    } else if (b_const_im == 0.0) {
      hamiltonian = 0.0;
      Ttrignew /= dc0.re;
    } else {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = 0.0;
    } else if (Ttrignew == 0.0) {
      hamiltonian = 0.0;
      Ttrignew = -(b_const_im / dc0.im);
    } else {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = -(b_const_im / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      hamiltonian = (b_const_im + bim * Ttrignew) / c_const_re;
      Ttrignew = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      hamiltonian = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      Ttrignew = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      hamiltonian = (bim * b_const_im + Ttrignew) / c_const_re;
      Ttrignew = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -Ttrignew;
  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = -dc0.re;
  if (muDoubleScalarIsNaN(-dc0.re) || muDoubleScalarIsInf(-dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_cos(&dc0);
  a = gam;
  b_cos(&a);
  uc_z.re = xAndLambda[2] + 50.0;
  uc_z.im = 0.0;
  dc1 = b_mpower(uc_z);
  v_re = xAndLambda[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda[9] * muDoubleScalarCos(b_const->alfamax *
          muDoubleScalarSin(alfatrig)));
  ai = -(0.0 * muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)));
  if (ai == 0.0) {
    re = ar / b_const->mass;
    lamY_im = 0.0;
  } else if (ar == 0.0) {
    re = 0.0;
    lamY_im = ai / b_const->mass;
  } else {
    re = ar / b_const->mass;
    lamY_im = ai / b_const->mass;
  }

  ar = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * xAndLambda[11]) * muDoubleScalarCos(b_const->bankmax *
    muDoubleScalarSin(banktrig));
  ai = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig));
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_re = b_const->mass * 0.0;
  if (c_const_re == 0.0) {
    if (ai == 0.0) {
      lamY_re = ar / hamiltonian;
      lamX_im = 0.0;
    } else if (ar == 0.0) {
      lamY_re = 0.0;
      lamX_im = ai / hamiltonian;
    } else {
      lamY_re = ar / hamiltonian;
      lamX_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      lamY_re = ai / c_const_re;
      lamX_im = 0.0;
    } else if (ai == 0.0) {
      lamY_re = 0.0;
      lamX_im = -(ar / c_const_re);
    } else {
      lamY_re = ai / c_const_re;
      lamX_im = -(ar / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > c_const_re) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      lamY_re = (ar + bim * ai) / c_const_re;
      lamX_im = (ai - bim * ar) / c_const_re;
    } else if (c_const_re == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      lamY_re = (ar * lamX_re + ai * -0.5) / 0.0;
      lamX_im = (ai * lamX_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      lamY_re = (bim * ar + ai) / c_const_re;
      lamX_im = (bim * ai - ar) / c_const_re;
    }
  }

  const_re = b_const->mass * xAndLambda[3];
  const_im = b_const->mass * 0.0;
  b_const_re = const_re * a.re - const_im * a.im;
  const_im = const_re * a.im + const_im * a.re;
  ar = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * xAndLambda[10]) * muDoubleScalarSin(b_const->bankmax *
    muDoubleScalarSin(banktrig));
  ai = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig));
  if (const_im == 0.0) {
    if (ai == 0.0) {
      c_const_im = ar / b_const_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      c_const_im = 0.0;
      hamiltonian = ai / b_const_re;
    } else {
      c_const_im = ar / b_const_re;
      hamiltonian = ai / b_const_re;
    }
  } else if (b_const_re == 0.0) {
    if (ar == 0.0) {
      c_const_im = ai / const_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      c_const_im = 0.0;
      hamiltonian = -(ar / const_im);
    } else {
      c_const_im = ai / const_im;
      hamiltonian = -(ar / const_im);
    }
  } else {
    brm = muDoubleScalarAbs(b_const_re);
    bim = muDoubleScalarAbs(const_im);
    if (brm > bim) {
      bim = const_im / b_const_re;
      c_const_re = b_const_re + bim * const_im;
      c_const_im = (ar + bim * ai) / c_const_re;
      hamiltonian = (ai - bim * ar) / c_const_re;
    } else if (bim == brm) {
      if (b_const_re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (const_im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      c_const_im = (ar * lamX_re + ai * c_const_re) / brm;
      hamiltonian = (ai * lamX_re - ar * c_const_re) / brm;
    } else {
      bim = b_const_re / const_im;
      c_const_re = const_im + bim * b_const_re;
      c_const_im = (bim * ar + ai) / c_const_re;
      hamiltonian = (bim * ai - ar) / c_const_re;
    }
  }

  re = (re - lamY_re) - c_const_im;
  lamY_im = (lamY_im - lamX_im) - hamiltonian;
  c_const_im = v_re * re - v_im * lamY_im;
  v_im = v_re * lamY_im + v_im * re;
  hamiltonian = 8112.0 * dc0.re;
  c_const_re = 8112.0 * dc0.im;
  if (c_const_re == 0.0) {
    if (v_im == 0.0) {
      uc_v.re = c_const_im / hamiltonian;
      uc_v.im = 0.0;
    } else if (c_const_im == 0.0) {
      uc_v.re = 0.0;
      uc_v.im = v_im / hamiltonian;
    } else {
      uc_v.re = c_const_im / hamiltonian;
      uc_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (c_const_im == 0.0) {
      uc_v.re = v_im / c_const_re;
      uc_v.im = 0.0;
    } else if (v_im == 0.0) {
      uc_v.re = 0.0;
      uc_v.im = -(c_const_im / c_const_re);
    } else {
      uc_v.re = v_im / c_const_re;
      uc_v.im = -(c_const_im / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(c_const_re);
    if (brm > bim) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      uc_v.re = (c_const_im + bim * v_im) / c_const_re;
      uc_v.im = (v_im - bim * c_const_im) / c_const_re;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (c_const_re > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      uc_v.re = (c_const_im * lamX_re + v_im * c_const_re) / brm;
      uc_v.im = (v_im * lamX_re - c_const_im * c_const_re) / brm;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      uc_v.re = (bim * c_const_im + v_im) / c_const_re;
      uc_v.im = (bim * v_im - c_const_im) / c_const_re;
    }
  }

  dc1 = c_mpower(uc_v);
  ar = dc1.re - 1860.0;
  ai = dc1.im;
  if (ai == 0.0) {
    dc0.re = ar / 1560.0;
    dc0.im = 0.0;
  } else if (ar == 0.0) {
    dc0.re = 0.0;
    dc0.im = ai / 1560.0;
  } else {
    dc0.re = ar / 1560.0;
    dc0.im = ai / 1560.0;
  }

  c_asin(&dc0);
  Ttrignew = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    Ttrignew = 0.0;
  }

  emlrtPushRtStackR2012b(&qb_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = mpower(1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0);
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  vc_v.re = xAndLambda[3] * xAndLambda[3];
  vc_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, vc_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0);
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  lc_const.re = b_const->mass * xAndLambda[3];
  lc_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig))
                * (b_const->g * b_const->mass + muDoubleScalarSin
                   (b_const->alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0)), lc_const);
  vc_z.re = xAndLambda[2] + 50.0;
  vc_z.im = 0.0;
  v = b_mpower(vc_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        kc_v_re = 0.5;
      } else {
        kc_v_re = -0.5;
      }

      if (v_im > 0.0) {
        kc_v_im = 0.5;
      } else {
        kc_v_im = -0.5;
      }

      re = (ar * kc_v_re + ai * kc_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda[10] * (b_const->g * b_const->mass + muDoubleScalarSin
                      (b_const->alfamax * muDoubleScalarSin(alfatrig)) * (1560.0
    * muDoubleScalarSin(Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (b_const->g * b_const->mass + muDoubleScalarSin(b_const->alfamax *
      muDoubleScalarSin(alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) +
      1860.0));
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        mc_const_re = 0.5;
      } else {
        mc_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        mc_const_im = 0.5;
      } else {
        mc_const_im = -0.5;
      }

      bim = (ar * mc_const_re + ai * mc_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  emlrtPopRtStackR2012b(&qb_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(-b_const->bankmax);
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(-b_const->bankmax);
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(-(2.0 * b_const->bankmax));
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(-(2.0 * b_const->bankmax));
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew = 0.0;
    } else if (b_const_im == 0.0) {
      hamiltonian = 0.0;
      Ttrignew /= dc0.re;
    } else {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = 0.0;
    } else if (Ttrignew == 0.0) {
      hamiltonian = 0.0;
      Ttrignew = -(b_const_im / dc0.im);
    } else {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = -(b_const_im / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      hamiltonian = (b_const_im + bim * Ttrignew) / c_const_re;
      Ttrignew = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      hamiltonian = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      Ttrignew = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      hamiltonian = (bim * b_const_im + Ttrignew) / c_const_re;
      Ttrignew = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -Ttrignew;
  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_cos(&dc0);
  a = gam;
  b_cos(&a);
  wc_z.re = xAndLambda[2] + 50.0;
  wc_z.im = 0.0;
  dc1 = b_mpower(wc_z);
  v_re = xAndLambda[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda[9] * muDoubleScalarCos(b_const->alfamax *
          muDoubleScalarSin(alfatrig)));
  ai = -(0.0 * muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)));
  if (ai == 0.0) {
    re = ar / b_const->mass;
    lamY_im = 0.0;
  } else if (ar == 0.0) {
    re = 0.0;
    lamY_im = ai / b_const->mass;
  } else {
    re = ar / b_const->mass;
    lamY_im = ai / b_const->mass;
  }

  ar = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * xAndLambda[11]) * muDoubleScalarCos(-b_const->bankmax);
  ai = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarCos(-b_const->bankmax);
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_re = b_const->mass * 0.0;
  if (c_const_re == 0.0) {
    if (ai == 0.0) {
      lamY_re = ar / hamiltonian;
      lamX_im = 0.0;
    } else if (ar == 0.0) {
      lamY_re = 0.0;
      lamX_im = ai / hamiltonian;
    } else {
      lamY_re = ar / hamiltonian;
      lamX_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      lamY_re = ai / c_const_re;
      lamX_im = 0.0;
    } else if (ai == 0.0) {
      lamY_re = 0.0;
      lamX_im = -(ar / c_const_re);
    } else {
      lamY_re = ai / c_const_re;
      lamX_im = -(ar / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > c_const_re) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      lamY_re = (ar + bim * ai) / c_const_re;
      lamX_im = (ai - bim * ar) / c_const_re;
    } else if (c_const_re == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      lamY_re = (ar * lamX_re + ai * -0.5) / 0.0;
      lamX_im = (ai * lamX_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      lamY_re = (bim * ar + ai) / c_const_re;
      lamX_im = (bim * ai - ar) / c_const_re;
    }
  }

  const_re = b_const->mass * xAndLambda[3];
  const_im = b_const->mass * 0.0;
  b_const_re = const_re * a.re - const_im * a.im;
  const_im = const_re * a.im + const_im * a.re;
  ar = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * xAndLambda[10]) * muDoubleScalarSin(-b_const->bankmax);
  ai = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarSin(-b_const->bankmax);
  if (const_im == 0.0) {
    if (ai == 0.0) {
      c_const_im = ar / b_const_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      c_const_im = 0.0;
      hamiltonian = ai / b_const_re;
    } else {
      c_const_im = ar / b_const_re;
      hamiltonian = ai / b_const_re;
    }
  } else if (b_const_re == 0.0) {
    if (ar == 0.0) {
      c_const_im = ai / const_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      c_const_im = 0.0;
      hamiltonian = -(ar / const_im);
    } else {
      c_const_im = ai / const_im;
      hamiltonian = -(ar / const_im);
    }
  } else {
    brm = muDoubleScalarAbs(b_const_re);
    bim = muDoubleScalarAbs(const_im);
    if (brm > bim) {
      bim = const_im / b_const_re;
      c_const_re = b_const_re + bim * const_im;
      c_const_im = (ar + bim * ai) / c_const_re;
      hamiltonian = (ai - bim * ar) / c_const_re;
    } else if (bim == brm) {
      if (b_const_re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (const_im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      c_const_im = (ar * lamX_re + ai * c_const_re) / brm;
      hamiltonian = (ai * lamX_re - ar * c_const_re) / brm;
    } else {
      bim = b_const_re / const_im;
      c_const_re = const_im + bim * b_const_re;
      c_const_im = (bim * ar + ai) / c_const_re;
      hamiltonian = (bim * ai - ar) / c_const_re;
    }
  }

  re = (re - lamY_re) - c_const_im;
  lamY_im = (lamY_im - lamX_im) - hamiltonian;
  c_const_im = v_re * re - v_im * lamY_im;
  v_im = v_re * lamY_im + v_im * re;
  hamiltonian = 8112.0 * dc0.re;
  c_const_re = 8112.0 * dc0.im;
  if (c_const_re == 0.0) {
    if (v_im == 0.0) {
      wc_v.re = c_const_im / hamiltonian;
      wc_v.im = 0.0;
    } else if (c_const_im == 0.0) {
      wc_v.re = 0.0;
      wc_v.im = v_im / hamiltonian;
    } else {
      wc_v.re = c_const_im / hamiltonian;
      wc_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (c_const_im == 0.0) {
      wc_v.re = v_im / c_const_re;
      wc_v.im = 0.0;
    } else if (v_im == 0.0) {
      wc_v.re = 0.0;
      wc_v.im = -(c_const_im / c_const_re);
    } else {
      wc_v.re = v_im / c_const_re;
      wc_v.im = -(c_const_im / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(c_const_re);
    if (brm > bim) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      wc_v.re = (c_const_im + bim * v_im) / c_const_re;
      wc_v.im = (v_im - bim * c_const_im) / c_const_re;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (c_const_re > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      wc_v.re = (c_const_im * lamX_re + v_im * c_const_re) / brm;
      wc_v.im = (v_im * lamX_re - c_const_im * c_const_re) / brm;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      wc_v.re = (bim * c_const_im + v_im) / c_const_re;
      wc_v.im = (bim * v_im - c_const_im) / c_const_re;
    }
  }

  dc1 = c_mpower(wc_v);
  ar = dc1.re - 1860.0;
  ai = dc1.im;
  if (ai == 0.0) {
    dc0.re = ar / 1560.0;
    dc0.im = 0.0;
  } else if (ar == 0.0) {
    dc0.re = 0.0;
    dc0.im = ai / 1560.0;
  } else {
    dc0.re = ar / 1560.0;
    dc0.im = ai / 1560.0;
  }

  c_asin(&dc0);
  Ttrignew = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    Ttrignew = 0.0;
  }

  emlrtPushRtStackR2012b(&rb_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = mpower(1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0);
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  xc_v.re = xAndLambda[3] * xAndLambda[3];
  xc_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, xc_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0);
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  mc_const.re = b_const->mass * xAndLambda[3];
  mc_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(-b_const->bankmax) * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0)), mc_const);
  xc_z.re = xAndLambda[2] + 50.0;
  xc_z.im = 0.0;
  v = b_mpower(xc_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        lc_v_re = 0.5;
      } else {
        lc_v_re = -0.5;
      }

      if (v_im > 0.0) {
        lc_v_im = 0.5;
      } else {
        lc_v_im = -0.5;
      }

      re = (ar * lc_v_re + ai * lc_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(-b_const->bankmax) * xAndLambda[10] * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(-b_const->bankmax) * 0.0 * (b_const->g * b_const->mass
    + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0));
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        nc_const_re = 0.5;
      } else {
        nc_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        nc_const_im = 0.5;
      } else {
        nc_const_im = -0.5;
      }

      bim = (ar * nc_const_re + ai * nc_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  emlrtPopRtStackR2012b(&rb_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = -1.5707963267948966;
    *alfatrigSave = alfatrig;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(b_const->bankmax);
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(b_const->bankmax);
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(2.0 * b_const->bankmax);
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(2.0 * b_const->bankmax);
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew = 0.0;
    } else if (b_const_im == 0.0) {
      hamiltonian = 0.0;
      Ttrignew /= dc0.re;
    } else {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = 0.0;
    } else if (Ttrignew == 0.0) {
      hamiltonian = 0.0;
      Ttrignew = -(b_const_im / dc0.im);
    } else {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = -(b_const_im / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      hamiltonian = (b_const_im + bim * Ttrignew) / c_const_re;
      Ttrignew = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      hamiltonian = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      Ttrignew = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      hamiltonian = (bim * b_const_im + Ttrignew) / c_const_re;
      Ttrignew = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -Ttrignew;
  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_cos(&dc0);
  a = gam;
  b_cos(&a);
  yc_z.re = xAndLambda[2] + 50.0;
  yc_z.im = 0.0;
  dc1 = b_mpower(yc_z);
  v_re = xAndLambda[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda[9] * muDoubleScalarCos(b_const->alfamax *
          muDoubleScalarSin(alfatrig)));
  ai = -(0.0 * muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)));
  if (ai == 0.0) {
    re = ar / b_const->mass;
    lamY_im = 0.0;
  } else if (ar == 0.0) {
    re = 0.0;
    lamY_im = ai / b_const->mass;
  } else {
    re = ar / b_const->mass;
    lamY_im = ai / b_const->mass;
  }

  ar = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * xAndLambda[11]) * muDoubleScalarCos(b_const->bankmax);
  ai = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarCos(b_const->bankmax);
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_re = b_const->mass * 0.0;
  if (c_const_re == 0.0) {
    if (ai == 0.0) {
      lamY_re = ar / hamiltonian;
      lamX_im = 0.0;
    } else if (ar == 0.0) {
      lamY_re = 0.0;
      lamX_im = ai / hamiltonian;
    } else {
      lamY_re = ar / hamiltonian;
      lamX_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      lamY_re = ai / c_const_re;
      lamX_im = 0.0;
    } else if (ai == 0.0) {
      lamY_re = 0.0;
      lamX_im = -(ar / c_const_re);
    } else {
      lamY_re = ai / c_const_re;
      lamX_im = -(ar / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > c_const_re) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      lamY_re = (ar + bim * ai) / c_const_re;
      lamX_im = (ai - bim * ar) / c_const_re;
    } else if (c_const_re == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      lamY_re = (ar * lamX_re + ai * -0.5) / 0.0;
      lamX_im = (ai * lamX_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      lamY_re = (bim * ar + ai) / c_const_re;
      lamX_im = (bim * ai - ar) / c_const_re;
    }
  }

  const_re = b_const->mass * xAndLambda[3];
  const_im = b_const->mass * 0.0;
  b_const_re = const_re * a.re - const_im * a.im;
  const_im = const_re * a.im + const_im * a.re;
  ar = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * xAndLambda[10]) * muDoubleScalarSin(b_const->bankmax);
  ai = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarSin(b_const->bankmax);
  if (const_im == 0.0) {
    if (ai == 0.0) {
      c_const_im = ar / b_const_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      c_const_im = 0.0;
      hamiltonian = ai / b_const_re;
    } else {
      c_const_im = ar / b_const_re;
      hamiltonian = ai / b_const_re;
    }
  } else if (b_const_re == 0.0) {
    if (ar == 0.0) {
      c_const_im = ai / const_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      c_const_im = 0.0;
      hamiltonian = -(ar / const_im);
    } else {
      c_const_im = ai / const_im;
      hamiltonian = -(ar / const_im);
    }
  } else {
    brm = muDoubleScalarAbs(b_const_re);
    bim = muDoubleScalarAbs(const_im);
    if (brm > bim) {
      bim = const_im / b_const_re;
      c_const_re = b_const_re + bim * const_im;
      c_const_im = (ar + bim * ai) / c_const_re;
      hamiltonian = (ai - bim * ar) / c_const_re;
    } else if (bim == brm) {
      if (b_const_re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (const_im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      c_const_im = (ar * lamX_re + ai * c_const_re) / brm;
      hamiltonian = (ai * lamX_re - ar * c_const_re) / brm;
    } else {
      bim = b_const_re / const_im;
      c_const_re = const_im + bim * b_const_re;
      c_const_im = (bim * ar + ai) / c_const_re;
      hamiltonian = (bim * ai - ar) / c_const_re;
    }
  }

  re = (re - lamY_re) - c_const_im;
  lamY_im = (lamY_im - lamX_im) - hamiltonian;
  c_const_im = v_re * re - v_im * lamY_im;
  v_im = v_re * lamY_im + v_im * re;
  hamiltonian = 8112.0 * dc0.re;
  c_const_re = 8112.0 * dc0.im;
  if (c_const_re == 0.0) {
    if (v_im == 0.0) {
      yc_v.re = c_const_im / hamiltonian;
      yc_v.im = 0.0;
    } else if (c_const_im == 0.0) {
      yc_v.re = 0.0;
      yc_v.im = v_im / hamiltonian;
    } else {
      yc_v.re = c_const_im / hamiltonian;
      yc_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (c_const_im == 0.0) {
      yc_v.re = v_im / c_const_re;
      yc_v.im = 0.0;
    } else if (v_im == 0.0) {
      yc_v.re = 0.0;
      yc_v.im = -(c_const_im / c_const_re);
    } else {
      yc_v.re = v_im / c_const_re;
      yc_v.im = -(c_const_im / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(c_const_re);
    if (brm > bim) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      yc_v.re = (c_const_im + bim * v_im) / c_const_re;
      yc_v.im = (v_im - bim * c_const_im) / c_const_re;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (c_const_re > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      yc_v.re = (c_const_im * lamX_re + v_im * c_const_re) / brm;
      yc_v.im = (v_im * lamX_re - c_const_im * c_const_re) / brm;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      yc_v.re = (bim * c_const_im + v_im) / c_const_re;
      yc_v.im = (bim * v_im - c_const_im) / c_const_re;
    }
  }

  dc1 = c_mpower(yc_v);
  ar = dc1.re - 1860.0;
  ai = dc1.im;
  if (ai == 0.0) {
    dc0.re = ar / 1560.0;
    dc0.im = 0.0;
  } else if (ar == 0.0) {
    dc0.re = 0.0;
    dc0.im = ai / 1560.0;
  } else {
    dc0.re = ar / 1560.0;
    dc0.im = ai / 1560.0;
  }

  c_asin(&dc0);
  Ttrignew = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    Ttrignew = 0.0;
  }

  emlrtPushRtStackR2012b(&sb_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = mpower(1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0);
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  ad_v.re = xAndLambda[3] * xAndLambda[3];
  ad_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, ad_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0);
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  nc_const.re = b_const->mass * xAndLambda[3];
  nc_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax) * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0)), nc_const);
  ad_z.re = xAndLambda[2] + 50.0;
  ad_z.im = 0.0;
  v = b_mpower(ad_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        mc_v_re = 0.5;
      } else {
        mc_v_re = -0.5;
      }

      if (v_im > 0.0) {
        mc_v_im = 0.5;
      } else {
        mc_v_im = -0.5;
      }

      re = (ar * mc_v_re + ai * mc_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax) * xAndLambda[10] * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(b_const->bankmax) * 0.0 * (b_const->g * b_const->mass +
    muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0));
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        oc_const_re = 0.5;
      } else {
        oc_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        oc_const_im = 0.5;
      } else {
        oc_const_im = -0.5;
      }

      bim = (ar * oc_const_re + ai * oc_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  emlrtPopRtStackR2012b(&sb_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = 1.5707963267948966;
    *alfatrigSave = alfatrig;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&tb_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = 3.1416 / (2.0 * b_const->bankmax);
  b_asin(&hamiltonian);
  banktrig = -hamiltonian;
  emlrtPopRtStackR2012b(&tb_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(-hamiltonian) || muDoubleScalarIsInf(-hamiltonian)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(2.0 * b_const->bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(2.0 * b_const->bankmax * muDoubleScalarSin(banktrig));
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew = 0.0;
    } else if (b_const_im == 0.0) {
      hamiltonian = 0.0;
      Ttrignew /= dc0.re;
    } else {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = 0.0;
    } else if (Ttrignew == 0.0) {
      hamiltonian = 0.0;
      Ttrignew = -(b_const_im / dc0.im);
    } else {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = -(b_const_im / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      hamiltonian = (b_const_im + bim * Ttrignew) / c_const_re;
      Ttrignew = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      hamiltonian = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      Ttrignew = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      hamiltonian = (bim * b_const_im + Ttrignew) / c_const_re;
      Ttrignew = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -Ttrignew;
  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_cos(&dc0);
  a = gam;
  b_cos(&a);
  bd_z.re = xAndLambda[2] + 50.0;
  bd_z.im = 0.0;
  dc1 = b_mpower(bd_z);
  v_re = xAndLambda[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda[9] * muDoubleScalarCos(b_const->alfamax *
          muDoubleScalarSin(alfatrig)));
  ai = -(0.0 * muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)));
  if (ai == 0.0) {
    re = ar / b_const->mass;
    lamY_im = 0.0;
  } else if (ar == 0.0) {
    re = 0.0;
    lamY_im = ai / b_const->mass;
  } else {
    re = ar / b_const->mass;
    lamY_im = ai / b_const->mass;
  }

  ar = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * xAndLambda[11]) * muDoubleScalarCos(b_const->bankmax *
    muDoubleScalarSin(banktrig));
  ai = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig));
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_re = b_const->mass * 0.0;
  if (c_const_re == 0.0) {
    if (ai == 0.0) {
      lamY_re = ar / hamiltonian;
      lamX_im = 0.0;
    } else if (ar == 0.0) {
      lamY_re = 0.0;
      lamX_im = ai / hamiltonian;
    } else {
      lamY_re = ar / hamiltonian;
      lamX_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      lamY_re = ai / c_const_re;
      lamX_im = 0.0;
    } else if (ai == 0.0) {
      lamY_re = 0.0;
      lamX_im = -(ar / c_const_re);
    } else {
      lamY_re = ai / c_const_re;
      lamX_im = -(ar / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > c_const_re) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      lamY_re = (ar + bim * ai) / c_const_re;
      lamX_im = (ai - bim * ar) / c_const_re;
    } else if (c_const_re == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      lamY_re = (ar * lamX_re + ai * -0.5) / 0.0;
      lamX_im = (ai * lamX_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      lamY_re = (bim * ar + ai) / c_const_re;
      lamX_im = (bim * ai - ar) / c_const_re;
    }
  }

  const_re = b_const->mass * xAndLambda[3];
  const_im = b_const->mass * 0.0;
  b_const_re = const_re * a.re - const_im * a.im;
  const_im = const_re * a.im + const_im * a.re;
  ar = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * xAndLambda[10]) * muDoubleScalarSin(b_const->bankmax *
    muDoubleScalarSin(banktrig));
  ai = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig));
  if (const_im == 0.0) {
    if (ai == 0.0) {
      c_const_im = ar / b_const_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      c_const_im = 0.0;
      hamiltonian = ai / b_const_re;
    } else {
      c_const_im = ar / b_const_re;
      hamiltonian = ai / b_const_re;
    }
  } else if (b_const_re == 0.0) {
    if (ar == 0.0) {
      c_const_im = ai / const_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      c_const_im = 0.0;
      hamiltonian = -(ar / const_im);
    } else {
      c_const_im = ai / const_im;
      hamiltonian = -(ar / const_im);
    }
  } else {
    brm = muDoubleScalarAbs(b_const_re);
    bim = muDoubleScalarAbs(const_im);
    if (brm > bim) {
      bim = const_im / b_const_re;
      c_const_re = b_const_re + bim * const_im;
      c_const_im = (ar + bim * ai) / c_const_re;
      hamiltonian = (ai - bim * ar) / c_const_re;
    } else if (bim == brm) {
      if (b_const_re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (const_im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      c_const_im = (ar * lamX_re + ai * c_const_re) / brm;
      hamiltonian = (ai * lamX_re - ar * c_const_re) / brm;
    } else {
      bim = b_const_re / const_im;
      c_const_re = const_im + bim * b_const_re;
      c_const_im = (bim * ar + ai) / c_const_re;
      hamiltonian = (bim * ai - ar) / c_const_re;
    }
  }

  re = (re - lamY_re) - c_const_im;
  lamY_im = (lamY_im - lamX_im) - hamiltonian;
  c_const_im = v_re * re - v_im * lamY_im;
  v_im = v_re * lamY_im + v_im * re;
  hamiltonian = 8112.0 * dc0.re;
  c_const_re = 8112.0 * dc0.im;
  if (c_const_re == 0.0) {
    if (v_im == 0.0) {
      bd_v.re = c_const_im / hamiltonian;
      bd_v.im = 0.0;
    } else if (c_const_im == 0.0) {
      bd_v.re = 0.0;
      bd_v.im = v_im / hamiltonian;
    } else {
      bd_v.re = c_const_im / hamiltonian;
      bd_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (c_const_im == 0.0) {
      bd_v.re = v_im / c_const_re;
      bd_v.im = 0.0;
    } else if (v_im == 0.0) {
      bd_v.re = 0.0;
      bd_v.im = -(c_const_im / c_const_re);
    } else {
      bd_v.re = v_im / c_const_re;
      bd_v.im = -(c_const_im / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(c_const_re);
    if (brm > bim) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      bd_v.re = (c_const_im + bim * v_im) / c_const_re;
      bd_v.im = (v_im - bim * c_const_im) / c_const_re;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (c_const_re > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      bd_v.re = (c_const_im * lamX_re + v_im * c_const_re) / brm;
      bd_v.im = (v_im * lamX_re - c_const_im * c_const_re) / brm;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      bd_v.re = (bim * c_const_im + v_im) / c_const_re;
      bd_v.im = (bim * v_im - c_const_im) / c_const_re;
    }
  }

  dc1 = c_mpower(bd_v);
  ar = dc1.re - 1860.0;
  ai = dc1.im;
  if (ai == 0.0) {
    dc0.re = ar / 1560.0;
    dc0.im = 0.0;
  } else if (ar == 0.0) {
    dc0.re = 0.0;
    dc0.im = ai / 1560.0;
  } else {
    dc0.re = ar / 1560.0;
    dc0.im = ai / 1560.0;
  }

  c_asin(&dc0);
  Ttrignew = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    Ttrignew = 0.0;
  }

  emlrtPushRtStackR2012b(&ub_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = mpower(1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0);
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  cd_v.re = xAndLambda[3] * xAndLambda[3];
  cd_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, cd_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0);
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  oc_const.re = b_const->mass * xAndLambda[3];
  oc_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig))
                * (b_const->g * b_const->mass + muDoubleScalarSin
                   (b_const->alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0)), oc_const);
  cd_z.re = xAndLambda[2] + 50.0;
  cd_z.im = 0.0;
  v = b_mpower(cd_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        nc_v_re = 0.5;
      } else {
        nc_v_re = -0.5;
      }

      if (v_im > 0.0) {
        nc_v_im = 0.5;
      } else {
        nc_v_im = -0.5;
      }

      re = (ar * nc_v_re + ai * nc_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda[10] * (b_const->g * b_const->mass + muDoubleScalarSin
                      (b_const->alfamax * muDoubleScalarSin(alfatrig)) * (1560.0
    * muDoubleScalarSin(Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (b_const->g * b_const->mass + muDoubleScalarSin(b_const->alfamax *
      muDoubleScalarSin(alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) +
      1860.0));
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        pc_const_re = 0.5;
      } else {
        pc_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        pc_const_im = 0.5;
      } else {
        pc_const_im = -0.5;
      }

      bim = (ar * pc_const_re + ai * pc_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  emlrtPopRtStackR2012b(&ub_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&vb_emlrtRSI, emlrtRootTLSGlobal);
  banktrig = 3.1416 / (2.0 * b_const->bankmax);
  b_asin(&banktrig);
  emlrtPopRtStackR2012b(&vb_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(banktrig) || muDoubleScalarIsInf(banktrig)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(2.0 * b_const->bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(2.0 * b_const->bankmax * muDoubleScalarSin(banktrig));
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew = 0.0;
    } else if (b_const_im == 0.0) {
      hamiltonian = 0.0;
      Ttrignew /= dc0.re;
    } else {
      hamiltonian = b_const_im / dc0.re;
      Ttrignew /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = 0.0;
    } else if (Ttrignew == 0.0) {
      hamiltonian = 0.0;
      Ttrignew = -(b_const_im / dc0.im);
    } else {
      hamiltonian = Ttrignew / dc0.im;
      Ttrignew = -(b_const_im / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      hamiltonian = (b_const_im + bim * Ttrignew) / c_const_re;
      Ttrignew = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      hamiltonian = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      Ttrignew = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      hamiltonian = (bim * b_const_im + Ttrignew) / c_const_re;
      Ttrignew = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -Ttrignew;
  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_cos(&dc0);
  a = gam;
  b_cos(&a);
  dd_z.re = xAndLambda[2] + 50.0;
  dd_z.im = 0.0;
  dc1 = b_mpower(dd_z);
  v_re = xAndLambda[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda[9] * muDoubleScalarCos(b_const->alfamax *
          muDoubleScalarSin(alfatrig)));
  ai = -(0.0 * muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)));
  if (ai == 0.0) {
    re = ar / b_const->mass;
    lamY_im = 0.0;
  } else if (ar == 0.0) {
    re = 0.0;
    lamY_im = ai / b_const->mass;
  } else {
    re = ar / b_const->mass;
    lamY_im = ai / b_const->mass;
  }

  ar = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * xAndLambda[11]) * muDoubleScalarCos(b_const->bankmax *
    muDoubleScalarSin(banktrig));
  ai = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig));
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_re = b_const->mass * 0.0;
  if (c_const_re == 0.0) {
    if (ai == 0.0) {
      lamY_re = ar / hamiltonian;
      lamX_im = 0.0;
    } else if (ar == 0.0) {
      lamY_re = 0.0;
      lamX_im = ai / hamiltonian;
    } else {
      lamY_re = ar / hamiltonian;
      lamX_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      lamY_re = ai / c_const_re;
      lamX_im = 0.0;
    } else if (ai == 0.0) {
      lamY_re = 0.0;
      lamX_im = -(ar / c_const_re);
    } else {
      lamY_re = ai / c_const_re;
      lamX_im = -(ar / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > c_const_re) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      lamY_re = (ar + bim * ai) / c_const_re;
      lamX_im = (ai - bim * ar) / c_const_re;
    } else if (c_const_re == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      lamY_re = (ar * lamX_re + ai * -0.5) / 0.0;
      lamX_im = (ai * lamX_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      lamY_re = (bim * ar + ai) / c_const_re;
      lamX_im = (bim * ai - ar) / c_const_re;
    }
  }

  const_re = b_const->mass * xAndLambda[3];
  const_im = b_const->mass * 0.0;
  b_const_re = const_re * a.re - const_im * a.im;
  const_im = const_re * a.im + const_im * a.re;
  ar = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * xAndLambda[10]) * muDoubleScalarSin(b_const->bankmax *
    muDoubleScalarSin(banktrig));
  ai = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig));
  if (const_im == 0.0) {
    if (ai == 0.0) {
      c_const_im = ar / b_const_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      c_const_im = 0.0;
      hamiltonian = ai / b_const_re;
    } else {
      c_const_im = ar / b_const_re;
      hamiltonian = ai / b_const_re;
    }
  } else if (b_const_re == 0.0) {
    if (ar == 0.0) {
      c_const_im = ai / const_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      c_const_im = 0.0;
      hamiltonian = -(ar / const_im);
    } else {
      c_const_im = ai / const_im;
      hamiltonian = -(ar / const_im);
    }
  } else {
    brm = muDoubleScalarAbs(b_const_re);
    bim = muDoubleScalarAbs(const_im);
    if (brm > bim) {
      bim = const_im / b_const_re;
      c_const_re = b_const_re + bim * const_im;
      c_const_im = (ar + bim * ai) / c_const_re;
      hamiltonian = (ai - bim * ar) / c_const_re;
    } else if (bim == brm) {
      if (b_const_re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (const_im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      c_const_im = (ar * lamX_re + ai * c_const_re) / brm;
      hamiltonian = (ai * lamX_re - ar * c_const_re) / brm;
    } else {
      bim = b_const_re / const_im;
      c_const_re = const_im + bim * b_const_re;
      c_const_im = (bim * ar + ai) / c_const_re;
      hamiltonian = (bim * ai - ar) / c_const_re;
    }
  }

  re = (re - lamY_re) - c_const_im;
  lamY_im = (lamY_im - lamX_im) - hamiltonian;
  c_const_im = v_re * re - v_im * lamY_im;
  v_im = v_re * lamY_im + v_im * re;
  hamiltonian = 8112.0 * dc0.re;
  c_const_re = 8112.0 * dc0.im;
  if (c_const_re == 0.0) {
    if (v_im == 0.0) {
      dd_v.re = c_const_im / hamiltonian;
      dd_v.im = 0.0;
    } else if (c_const_im == 0.0) {
      dd_v.re = 0.0;
      dd_v.im = v_im / hamiltonian;
    } else {
      dd_v.re = c_const_im / hamiltonian;
      dd_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (c_const_im == 0.0) {
      dd_v.re = v_im / c_const_re;
      dd_v.im = 0.0;
    } else if (v_im == 0.0) {
      dd_v.re = 0.0;
      dd_v.im = -(c_const_im / c_const_re);
    } else {
      dd_v.re = v_im / c_const_re;
      dd_v.im = -(c_const_im / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(c_const_re);
    if (brm > bim) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      dd_v.re = (c_const_im + bim * v_im) / c_const_re;
      dd_v.im = (v_im - bim * c_const_im) / c_const_re;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (c_const_re > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      dd_v.re = (c_const_im * lamX_re + v_im * c_const_re) / brm;
      dd_v.im = (v_im * lamX_re - c_const_im * c_const_re) / brm;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      dd_v.re = (bim * c_const_im + v_im) / c_const_re;
      dd_v.im = (bim * v_im - c_const_im) / c_const_re;
    }
  }

  dc1 = c_mpower(dd_v);
  ar = dc1.re - 1860.0;
  ai = dc1.im;
  if (ai == 0.0) {
    dc0.re = ar / 1560.0;
    dc0.im = 0.0;
  } else if (ar == 0.0) {
    dc0.re = 0.0;
    dc0.im = ai / 1560.0;
  } else {
    dc0.re = ar / 1560.0;
    dc0.im = ai / 1560.0;
  }

  c_asin(&dc0);
  Ttrignew = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    Ttrignew = 0.0;
  }

  emlrtPushRtStackR2012b(&wb_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = mpower(1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0);
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  ed_v.re = xAndLambda[3] * xAndLambda[3];
  ed_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, ed_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0);
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  pc_const.re = b_const->mass * xAndLambda[3];
  pc_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig))
                * (b_const->g * b_const->mass + muDoubleScalarSin
                   (b_const->alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0)), pc_const);
  ed_z.re = xAndLambda[2] + 50.0;
  ed_z.im = 0.0;
  v = b_mpower(ed_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        oc_v_re = 0.5;
      } else {
        oc_v_re = -0.5;
      }

      if (v_im > 0.0) {
        oc_v_im = 0.5;
      } else {
        oc_v_im = -0.5;
      }

      re = (ar * oc_v_re + ai * oc_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda[10] * (b_const->g * b_const->mass + muDoubleScalarSin
                      (b_const->alfamax * muDoubleScalarSin(alfatrig)) * (1560.0
    * muDoubleScalarSin(Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (b_const->g * b_const->mass + muDoubleScalarSin(b_const->alfamax *
      muDoubleScalarSin(alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) +
      1860.0));
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        qc_const_re = 0.5;
      } else {
        qc_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        qc_const_im = 0.5;
      } else {
        qc_const_im = -0.5;
      }

      bim = (ar * qc_const_re + ai * qc_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  emlrtPopRtStackR2012b(&wb_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(-b_const->bankmax);
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(-b_const->bankmax);
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(-(2.0 * b_const->bankmax));
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(-(2.0 * b_const->bankmax));
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  re = dc0.re;
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      dc0.re = b_const_im / dc0.re;
      dc0.im = 0.0;
    } else if (b_const_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = Ttrignew / re;
    } else {
      dc0.re = b_const_im / dc0.re;
      dc0.im = Ttrignew / re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = 0.0;
    } else if (Ttrignew == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(b_const_im / lamY_im);
    } else {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = -(b_const_im / lamY_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      dc0.re = (b_const_im + bim * Ttrignew) / c_const_re;
      dc0.im = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      dc0.re = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      dc0.im = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      dc0.re = (bim * b_const_im + Ttrignew) / c_const_re;
      dc0.im = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = -dc0.re;
  if (muDoubleScalarIsNaN(-dc0.re) || muDoubleScalarIsInf(-dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_cos(&dc0);
  a = gam;
  b_cos(&a);
  fd_z.re = xAndLambda[2] + 50.0;
  fd_z.im = 0.0;
  dc1 = b_mpower(fd_z);
  v_re = xAndLambda[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda[9] * muDoubleScalarCos(b_const->alfamax *
          muDoubleScalarSin(alfatrig)));
  ai = -(0.0 * muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)));
  if (ai == 0.0) {
    re = ar / b_const->mass;
    lamY_im = 0.0;
  } else if (ar == 0.0) {
    re = 0.0;
    lamY_im = ai / b_const->mass;
  } else {
    re = ar / b_const->mass;
    lamY_im = ai / b_const->mass;
  }

  ar = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * xAndLambda[11]) * muDoubleScalarCos(-b_const->bankmax);
  ai = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarCos(-b_const->bankmax);
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_re = b_const->mass * 0.0;
  if (c_const_re == 0.0) {
    if (ai == 0.0) {
      lamY_re = ar / hamiltonian;
      lamX_im = 0.0;
    } else if (ar == 0.0) {
      lamY_re = 0.0;
      lamX_im = ai / hamiltonian;
    } else {
      lamY_re = ar / hamiltonian;
      lamX_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      lamY_re = ai / c_const_re;
      lamX_im = 0.0;
    } else if (ai == 0.0) {
      lamY_re = 0.0;
      lamX_im = -(ar / c_const_re);
    } else {
      lamY_re = ai / c_const_re;
      lamX_im = -(ar / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > c_const_re) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      lamY_re = (ar + bim * ai) / c_const_re;
      lamX_im = (ai - bim * ar) / c_const_re;
    } else if (c_const_re == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      lamY_re = (ar * lamX_re + ai * -0.5) / 0.0;
      lamX_im = (ai * lamX_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      lamY_re = (bim * ar + ai) / c_const_re;
      lamX_im = (bim * ai - ar) / c_const_re;
    }
  }

  const_re = b_const->mass * xAndLambda[3];
  const_im = b_const->mass * 0.0;
  b_const_re = const_re * a.re - const_im * a.im;
  const_im = const_re * a.im + const_im * a.re;
  ar = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * xAndLambda[10]) * muDoubleScalarSin(-b_const->bankmax);
  ai = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarSin(-b_const->bankmax);
  if (const_im == 0.0) {
    if (ai == 0.0) {
      c_const_im = ar / b_const_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      c_const_im = 0.0;
      hamiltonian = ai / b_const_re;
    } else {
      c_const_im = ar / b_const_re;
      hamiltonian = ai / b_const_re;
    }
  } else if (b_const_re == 0.0) {
    if (ar == 0.0) {
      c_const_im = ai / const_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      c_const_im = 0.0;
      hamiltonian = -(ar / const_im);
    } else {
      c_const_im = ai / const_im;
      hamiltonian = -(ar / const_im);
    }
  } else {
    brm = muDoubleScalarAbs(b_const_re);
    bim = muDoubleScalarAbs(const_im);
    if (brm > bim) {
      bim = const_im / b_const_re;
      c_const_re = b_const_re + bim * const_im;
      c_const_im = (ar + bim * ai) / c_const_re;
      hamiltonian = (ai - bim * ar) / c_const_re;
    } else if (bim == brm) {
      if (b_const_re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (const_im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      c_const_im = (ar * lamX_re + ai * c_const_re) / brm;
      hamiltonian = (ai * lamX_re - ar * c_const_re) / brm;
    } else {
      bim = b_const_re / const_im;
      c_const_re = const_im + bim * b_const_re;
      c_const_im = (bim * ar + ai) / c_const_re;
      hamiltonian = (bim * ai - ar) / c_const_re;
    }
  }

  re = (re - lamY_re) - c_const_im;
  lamY_im = (lamY_im - lamX_im) - hamiltonian;
  c_const_im = v_re * re - v_im * lamY_im;
  v_im = v_re * lamY_im + v_im * re;
  hamiltonian = 8112.0 * dc0.re;
  c_const_re = 8112.0 * dc0.im;
  if (c_const_re == 0.0) {
    if (v_im == 0.0) {
      fd_v.re = c_const_im / hamiltonian;
      fd_v.im = 0.0;
    } else if (c_const_im == 0.0) {
      fd_v.re = 0.0;
      fd_v.im = v_im / hamiltonian;
    } else {
      fd_v.re = c_const_im / hamiltonian;
      fd_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (c_const_im == 0.0) {
      fd_v.re = v_im / c_const_re;
      fd_v.im = 0.0;
    } else if (v_im == 0.0) {
      fd_v.re = 0.0;
      fd_v.im = -(c_const_im / c_const_re);
    } else {
      fd_v.re = v_im / c_const_re;
      fd_v.im = -(c_const_im / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(c_const_re);
    if (brm > bim) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      fd_v.re = (c_const_im + bim * v_im) / c_const_re;
      fd_v.im = (v_im - bim * c_const_im) / c_const_re;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (c_const_re > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      fd_v.re = (c_const_im * lamX_re + v_im * c_const_re) / brm;
      fd_v.im = (v_im * lamX_re - c_const_im * c_const_re) / brm;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      fd_v.re = (bim * c_const_im + v_im) / c_const_re;
      fd_v.im = (bim * v_im - c_const_im) / c_const_re;
    }
  }

  dc1 = c_mpower(fd_v);
  ar = dc1.re - 1860.0;
  ai = dc1.im;
  if (ai == 0.0) {
    dc0.re = ar / 1560.0;
    dc0.im = 0.0;
  } else if (ar == 0.0) {
    dc0.re = 0.0;
    dc0.im = ai / 1560.0;
  } else {
    dc0.re = ar / 1560.0;
    dc0.im = ai / 1560.0;
  }

  c_asin(&dc0);
  Ttrignew = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    Ttrignew = 0.0;
  }

  emlrtPushRtStackR2012b(&xb_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = mpower(1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0);
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  gd_v.re = xAndLambda[3] * xAndLambda[3];
  gd_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, gd_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0);
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  qc_const.re = b_const->mass * xAndLambda[3];
  qc_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(-b_const->bankmax) * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0)), qc_const);
  gd_z.re = xAndLambda[2] + 50.0;
  gd_z.im = 0.0;
  v = b_mpower(gd_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        pc_v_re = 0.5;
      } else {
        pc_v_re = -0.5;
      }

      if (v_im > 0.0) {
        pc_v_im = 0.5;
      } else {
        pc_v_im = -0.5;
      }

      re = (ar * pc_v_re + ai * pc_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(-b_const->bankmax) * xAndLambda[10] * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(-b_const->bankmax) * 0.0 * (b_const->g * b_const->mass
    + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0));
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        rc_const_re = 0.5;
      } else {
        rc_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        rc_const_im = 0.5;
      } else {
        rc_const_im = -0.5;
      }

      bim = (ar * rc_const_re + ai * rc_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  emlrtPopRtStackR2012b(&xb_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = -1.5707963267948966;
    *alfatrigSave = alfatrig;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(b_const->bankmax);
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(b_const->bankmax);
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(2.0 * b_const->bankmax);
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(2.0 * b_const->bankmax);
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  re = dc0.re;
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      dc0.re = b_const_im / dc0.re;
      dc0.im = 0.0;
    } else if (b_const_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = Ttrignew / re;
    } else {
      dc0.re = b_const_im / dc0.re;
      dc0.im = Ttrignew / re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = 0.0;
    } else if (Ttrignew == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(b_const_im / lamY_im);
    } else {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = -(b_const_im / lamY_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      dc0.re = (b_const_im + bim * Ttrignew) / c_const_re;
      dc0.im = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      dc0.re = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      dc0.im = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      dc0.re = (bim * b_const_im + Ttrignew) / c_const_re;
      dc0.im = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = -dc0.re;
  if (muDoubleScalarIsNaN(-dc0.re) || muDoubleScalarIsInf(-dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_cos(&dc0);
  a = gam;
  b_cos(&a);
  hd_z.re = xAndLambda[2] + 50.0;
  hd_z.im = 0.0;
  dc1 = b_mpower(hd_z);
  v_re = xAndLambda[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda[9] * muDoubleScalarCos(b_const->alfamax *
          muDoubleScalarSin(alfatrig)));
  ai = -(0.0 * muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)));
  if (ai == 0.0) {
    re = ar / b_const->mass;
    lamY_im = 0.0;
  } else if (ar == 0.0) {
    re = 0.0;
    lamY_im = ai / b_const->mass;
  } else {
    re = ar / b_const->mass;
    lamY_im = ai / b_const->mass;
  }

  ar = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * xAndLambda[11]) * muDoubleScalarCos(b_const->bankmax);
  ai = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarCos(b_const->bankmax);
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_re = b_const->mass * 0.0;
  if (c_const_re == 0.0) {
    if (ai == 0.0) {
      lamY_re = ar / hamiltonian;
      lamX_im = 0.0;
    } else if (ar == 0.0) {
      lamY_re = 0.0;
      lamX_im = ai / hamiltonian;
    } else {
      lamY_re = ar / hamiltonian;
      lamX_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      lamY_re = ai / c_const_re;
      lamX_im = 0.0;
    } else if (ai == 0.0) {
      lamY_re = 0.0;
      lamX_im = -(ar / c_const_re);
    } else {
      lamY_re = ai / c_const_re;
      lamX_im = -(ar / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > c_const_re) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      lamY_re = (ar + bim * ai) / c_const_re;
      lamX_im = (ai - bim * ar) / c_const_re;
    } else if (c_const_re == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      lamY_re = (ar * lamX_re + ai * -0.5) / 0.0;
      lamX_im = (ai * lamX_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      lamY_re = (bim * ar + ai) / c_const_re;
      lamX_im = (bim * ai - ar) / c_const_re;
    }
  }

  const_re = b_const->mass * xAndLambda[3];
  const_im = b_const->mass * 0.0;
  b_const_re = const_re * a.re - const_im * a.im;
  const_im = const_re * a.im + const_im * a.re;
  ar = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * xAndLambda[10]) * muDoubleScalarSin(b_const->bankmax);
  ai = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarSin(b_const->bankmax);
  if (const_im == 0.0) {
    if (ai == 0.0) {
      c_const_im = ar / b_const_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      c_const_im = 0.0;
      hamiltonian = ai / b_const_re;
    } else {
      c_const_im = ar / b_const_re;
      hamiltonian = ai / b_const_re;
    }
  } else if (b_const_re == 0.0) {
    if (ar == 0.0) {
      c_const_im = ai / const_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      c_const_im = 0.0;
      hamiltonian = -(ar / const_im);
    } else {
      c_const_im = ai / const_im;
      hamiltonian = -(ar / const_im);
    }
  } else {
    brm = muDoubleScalarAbs(b_const_re);
    bim = muDoubleScalarAbs(const_im);
    if (brm > bim) {
      bim = const_im / b_const_re;
      c_const_re = b_const_re + bim * const_im;
      c_const_im = (ar + bim * ai) / c_const_re;
      hamiltonian = (ai - bim * ar) / c_const_re;
    } else if (bim == brm) {
      if (b_const_re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (const_im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      c_const_im = (ar * lamX_re + ai * c_const_re) / brm;
      hamiltonian = (ai * lamX_re - ar * c_const_re) / brm;
    } else {
      bim = b_const_re / const_im;
      c_const_re = const_im + bim * b_const_re;
      c_const_im = (bim * ar + ai) / c_const_re;
      hamiltonian = (bim * ai - ar) / c_const_re;
    }
  }

  re = (re - lamY_re) - c_const_im;
  lamY_im = (lamY_im - lamX_im) - hamiltonian;
  c_const_im = v_re * re - v_im * lamY_im;
  v_im = v_re * lamY_im + v_im * re;
  hamiltonian = 8112.0 * dc0.re;
  c_const_re = 8112.0 * dc0.im;
  if (c_const_re == 0.0) {
    if (v_im == 0.0) {
      hd_v.re = c_const_im / hamiltonian;
      hd_v.im = 0.0;
    } else if (c_const_im == 0.0) {
      hd_v.re = 0.0;
      hd_v.im = v_im / hamiltonian;
    } else {
      hd_v.re = c_const_im / hamiltonian;
      hd_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (c_const_im == 0.0) {
      hd_v.re = v_im / c_const_re;
      hd_v.im = 0.0;
    } else if (v_im == 0.0) {
      hd_v.re = 0.0;
      hd_v.im = -(c_const_im / c_const_re);
    } else {
      hd_v.re = v_im / c_const_re;
      hd_v.im = -(c_const_im / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(c_const_re);
    if (brm > bim) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      hd_v.re = (c_const_im + bim * v_im) / c_const_re;
      hd_v.im = (v_im - bim * c_const_im) / c_const_re;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (c_const_re > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      hd_v.re = (c_const_im * lamX_re + v_im * c_const_re) / brm;
      hd_v.im = (v_im * lamX_re - c_const_im * c_const_re) / brm;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      hd_v.re = (bim * c_const_im + v_im) / c_const_re;
      hd_v.im = (bim * v_im - c_const_im) / c_const_re;
    }
  }

  dc1 = c_mpower(hd_v);
  ar = dc1.re - 1860.0;
  ai = dc1.im;
  if (ai == 0.0) {
    dc0.re = ar / 1560.0;
    dc0.im = 0.0;
  } else if (ar == 0.0) {
    dc0.re = 0.0;
    dc0.im = ai / 1560.0;
  } else {
    dc0.re = ar / 1560.0;
    dc0.im = ai / 1560.0;
  }

  c_asin(&dc0);
  Ttrignew = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    Ttrignew = 0.0;
  }

  emlrtPushRtStackR2012b(&yb_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = mpower(1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0);
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  id_v.re = xAndLambda[3] * xAndLambda[3];
  id_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, id_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0);
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  rc_const.re = b_const->mass * xAndLambda[3];
  rc_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax) * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0)), rc_const);
  id_z.re = xAndLambda[2] + 50.0;
  id_z.im = 0.0;
  v = b_mpower(id_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        qc_v_re = 0.5;
      } else {
        qc_v_re = -0.5;
      }

      if (v_im > 0.0) {
        qc_v_im = 0.5;
      } else {
        qc_v_im = -0.5;
      }

      re = (ar * qc_v_re + ai * qc_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax) * xAndLambda[10] * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(b_const->bankmax) * 0.0 * (b_const->g * b_const->mass +
    muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0));
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        sc_const_re = 0.5;
      } else {
        sc_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        sc_const_im = 0.5;
      } else {
        sc_const_im = -0.5;
      }

      bim = (ar * sc_const_re + ai * sc_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  emlrtPopRtStackR2012b(&yb_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = 1.5707963267948966;
    *alfatrigSave = alfatrig;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&ac_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = 3.1416 / (2.0 * b_const->bankmax);
  b_asin(&hamiltonian);
  banktrig = -hamiltonian;
  emlrtPopRtStackR2012b(&ac_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(-hamiltonian) || muDoubleScalarIsInf(-hamiltonian)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(2.0 * b_const->bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(2.0 * b_const->bankmax * muDoubleScalarSin(banktrig));
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  re = dc0.re;
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      dc0.re = b_const_im / dc0.re;
      dc0.im = 0.0;
    } else if (b_const_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = Ttrignew / re;
    } else {
      dc0.re = b_const_im / dc0.re;
      dc0.im = Ttrignew / re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = 0.0;
    } else if (Ttrignew == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(b_const_im / lamY_im);
    } else {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = -(b_const_im / lamY_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      dc0.re = (b_const_im + bim * Ttrignew) / c_const_re;
      dc0.im = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      dc0.re = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      dc0.im = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      dc0.re = (bim * b_const_im + Ttrignew) / c_const_re;
      dc0.im = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = -dc0.re;
  if (muDoubleScalarIsNaN(-dc0.re) || muDoubleScalarIsInf(-dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_cos(&dc0);
  a = gam;
  b_cos(&a);
  jd_z.re = xAndLambda[2] + 50.0;
  jd_z.im = 0.0;
  dc1 = b_mpower(jd_z);
  v_re = xAndLambda[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda[9] * muDoubleScalarCos(b_const->alfamax *
          muDoubleScalarSin(alfatrig)));
  ai = -(0.0 * muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)));
  if (ai == 0.0) {
    re = ar / b_const->mass;
    lamY_im = 0.0;
  } else if (ar == 0.0) {
    re = 0.0;
    lamY_im = ai / b_const->mass;
  } else {
    re = ar / b_const->mass;
    lamY_im = ai / b_const->mass;
  }

  ar = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * xAndLambda[11]) * muDoubleScalarCos(b_const->bankmax *
    muDoubleScalarSin(banktrig));
  ai = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig));
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_re = b_const->mass * 0.0;
  if (c_const_re == 0.0) {
    if (ai == 0.0) {
      lamY_re = ar / hamiltonian;
      lamX_im = 0.0;
    } else if (ar == 0.0) {
      lamY_re = 0.0;
      lamX_im = ai / hamiltonian;
    } else {
      lamY_re = ar / hamiltonian;
      lamX_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      lamY_re = ai / c_const_re;
      lamX_im = 0.0;
    } else if (ai == 0.0) {
      lamY_re = 0.0;
      lamX_im = -(ar / c_const_re);
    } else {
      lamY_re = ai / c_const_re;
      lamX_im = -(ar / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > c_const_re) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      lamY_re = (ar + bim * ai) / c_const_re;
      lamX_im = (ai - bim * ar) / c_const_re;
    } else if (c_const_re == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      lamY_re = (ar * lamX_re + ai * -0.5) / 0.0;
      lamX_im = (ai * lamX_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      lamY_re = (bim * ar + ai) / c_const_re;
      lamX_im = (bim * ai - ar) / c_const_re;
    }
  }

  const_re = b_const->mass * xAndLambda[3];
  const_im = b_const->mass * 0.0;
  b_const_re = const_re * a.re - const_im * a.im;
  const_im = const_re * a.im + const_im * a.re;
  ar = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * xAndLambda[10]) * muDoubleScalarSin(b_const->bankmax *
    muDoubleScalarSin(banktrig));
  ai = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig));
  if (const_im == 0.0) {
    if (ai == 0.0) {
      c_const_im = ar / b_const_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      c_const_im = 0.0;
      hamiltonian = ai / b_const_re;
    } else {
      c_const_im = ar / b_const_re;
      hamiltonian = ai / b_const_re;
    }
  } else if (b_const_re == 0.0) {
    if (ar == 0.0) {
      c_const_im = ai / const_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      c_const_im = 0.0;
      hamiltonian = -(ar / const_im);
    } else {
      c_const_im = ai / const_im;
      hamiltonian = -(ar / const_im);
    }
  } else {
    brm = muDoubleScalarAbs(b_const_re);
    bim = muDoubleScalarAbs(const_im);
    if (brm > bim) {
      bim = const_im / b_const_re;
      c_const_re = b_const_re + bim * const_im;
      c_const_im = (ar + bim * ai) / c_const_re;
      hamiltonian = (ai - bim * ar) / c_const_re;
    } else if (bim == brm) {
      if (b_const_re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (const_im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      c_const_im = (ar * lamX_re + ai * c_const_re) / brm;
      hamiltonian = (ai * lamX_re - ar * c_const_re) / brm;
    } else {
      bim = b_const_re / const_im;
      c_const_re = const_im + bim * b_const_re;
      c_const_im = (bim * ar + ai) / c_const_re;
      hamiltonian = (bim * ai - ar) / c_const_re;
    }
  }

  re = (re - lamY_re) - c_const_im;
  lamY_im = (lamY_im - lamX_im) - hamiltonian;
  c_const_im = v_re * re - v_im * lamY_im;
  v_im = v_re * lamY_im + v_im * re;
  hamiltonian = 8112.0 * dc0.re;
  c_const_re = 8112.0 * dc0.im;
  if (c_const_re == 0.0) {
    if (v_im == 0.0) {
      jd_v.re = c_const_im / hamiltonian;
      jd_v.im = 0.0;
    } else if (c_const_im == 0.0) {
      jd_v.re = 0.0;
      jd_v.im = v_im / hamiltonian;
    } else {
      jd_v.re = c_const_im / hamiltonian;
      jd_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (c_const_im == 0.0) {
      jd_v.re = v_im / c_const_re;
      jd_v.im = 0.0;
    } else if (v_im == 0.0) {
      jd_v.re = 0.0;
      jd_v.im = -(c_const_im / c_const_re);
    } else {
      jd_v.re = v_im / c_const_re;
      jd_v.im = -(c_const_im / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(c_const_re);
    if (brm > bim) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      jd_v.re = (c_const_im + bim * v_im) / c_const_re;
      jd_v.im = (v_im - bim * c_const_im) / c_const_re;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (c_const_re > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      jd_v.re = (c_const_im * lamX_re + v_im * c_const_re) / brm;
      jd_v.im = (v_im * lamX_re - c_const_im * c_const_re) / brm;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      jd_v.re = (bim * c_const_im + v_im) / c_const_re;
      jd_v.im = (bim * v_im - c_const_im) / c_const_re;
    }
  }

  dc1 = c_mpower(jd_v);
  ar = dc1.re - 1860.0;
  ai = dc1.im;
  if (ai == 0.0) {
    dc0.re = ar / 1560.0;
    dc0.im = 0.0;
  } else if (ar == 0.0) {
    dc0.re = 0.0;
    dc0.im = ai / 1560.0;
  } else {
    dc0.re = ar / 1560.0;
    dc0.im = ai / 1560.0;
  }

  c_asin(&dc0);
  Ttrignew = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    Ttrignew = 0.0;
  }

  emlrtPushRtStackR2012b(&bc_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = mpower(1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0);
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  kd_v.re = xAndLambda[3] * xAndLambda[3];
  kd_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, kd_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0);
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  sc_const.re = b_const->mass * xAndLambda[3];
  sc_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig))
                * (b_const->g * b_const->mass + muDoubleScalarSin
                   (b_const->alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0)), sc_const);
  kd_z.re = xAndLambda[2] + 50.0;
  kd_z.im = 0.0;
  v = b_mpower(kd_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        rc_v_re = 0.5;
      } else {
        rc_v_re = -0.5;
      }

      if (v_im > 0.0) {
        rc_v_im = 0.5;
      } else {
        rc_v_im = -0.5;
      }

      re = (ar * rc_v_re + ai * rc_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda[10] * (b_const->g * b_const->mass + muDoubleScalarSin
                      (b_const->alfamax * muDoubleScalarSin(alfatrig)) * (1560.0
    * muDoubleScalarSin(Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (b_const->g * b_const->mass + muDoubleScalarSin(b_const->alfamax *
      muDoubleScalarSin(alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) +
      1860.0));
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        tc_const_re = 0.5;
      } else {
        tc_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        tc_const_im = 0.5;
      } else {
        tc_const_im = -0.5;
      }

      bim = (ar * tc_const_re + ai * tc_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  emlrtPopRtStackR2012b(&bc_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&cc_emlrtRSI, emlrtRootTLSGlobal);
  banktrig = 3.1416 / (2.0 * b_const->bankmax);
  b_asin(&banktrig);
  emlrtPopRtStackR2012b(&cc_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(banktrig) || muDoubleScalarIsInf(banktrig)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(2.0 * b_const->bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(2.0 * b_const->bankmax * muDoubleScalarSin(banktrig));
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  re = dc0.re;
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      dc0.re = b_const_im / dc0.re;
      dc0.im = 0.0;
    } else if (b_const_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = Ttrignew / re;
    } else {
      dc0.re = b_const_im / dc0.re;
      dc0.im = Ttrignew / re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = 0.0;
    } else if (Ttrignew == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(b_const_im / lamY_im);
    } else {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = -(b_const_im / lamY_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      dc0.re = (b_const_im + bim * Ttrignew) / c_const_re;
      dc0.im = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      dc0.re = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      dc0.im = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      dc0.re = (bim * b_const_im + Ttrignew) / c_const_re;
      dc0.im = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = -dc0.re;
  if (muDoubleScalarIsNaN(-dc0.re) || muDoubleScalarIsInf(-dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_cos(&dc0);
  a = gam;
  b_cos(&a);
  ld_z.re = xAndLambda[2] + 50.0;
  ld_z.im = 0.0;
  dc1 = b_mpower(ld_z);
  v_re = xAndLambda[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda[9] * muDoubleScalarCos(b_const->alfamax *
          muDoubleScalarSin(alfatrig)));
  ai = -(0.0 * muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)));
  if (ai == 0.0) {
    re = ar / b_const->mass;
    lamY_im = 0.0;
  } else if (ar == 0.0) {
    re = 0.0;
    lamY_im = ai / b_const->mass;
  } else {
    re = ar / b_const->mass;
    lamY_im = ai / b_const->mass;
  }

  ar = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * xAndLambda[11]) * muDoubleScalarCos(b_const->bankmax *
    muDoubleScalarSin(banktrig));
  ai = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig));
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_re = b_const->mass * 0.0;
  if (c_const_re == 0.0) {
    if (ai == 0.0) {
      lamY_re = ar / hamiltonian;
      lamX_im = 0.0;
    } else if (ar == 0.0) {
      lamY_re = 0.0;
      lamX_im = ai / hamiltonian;
    } else {
      lamY_re = ar / hamiltonian;
      lamX_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      lamY_re = ai / c_const_re;
      lamX_im = 0.0;
    } else if (ai == 0.0) {
      lamY_re = 0.0;
      lamX_im = -(ar / c_const_re);
    } else {
      lamY_re = ai / c_const_re;
      lamX_im = -(ar / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > c_const_re) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      lamY_re = (ar + bim * ai) / c_const_re;
      lamX_im = (ai - bim * ar) / c_const_re;
    } else if (c_const_re == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      lamY_re = (ar * lamX_re + ai * -0.5) / 0.0;
      lamX_im = (ai * lamX_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      lamY_re = (bim * ar + ai) / c_const_re;
      lamX_im = (bim * ai - ar) / c_const_re;
    }
  }

  const_re = b_const->mass * xAndLambda[3];
  const_im = b_const->mass * 0.0;
  b_const_re = const_re * a.re - const_im * a.im;
  const_im = const_re * a.im + const_im * a.re;
  ar = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * xAndLambda[10]) * muDoubleScalarSin(b_const->bankmax *
    muDoubleScalarSin(banktrig));
  ai = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig));
  if (const_im == 0.0) {
    if (ai == 0.0) {
      c_const_im = ar / b_const_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      c_const_im = 0.0;
      hamiltonian = ai / b_const_re;
    } else {
      c_const_im = ar / b_const_re;
      hamiltonian = ai / b_const_re;
    }
  } else if (b_const_re == 0.0) {
    if (ar == 0.0) {
      c_const_im = ai / const_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      c_const_im = 0.0;
      hamiltonian = -(ar / const_im);
    } else {
      c_const_im = ai / const_im;
      hamiltonian = -(ar / const_im);
    }
  } else {
    brm = muDoubleScalarAbs(b_const_re);
    bim = muDoubleScalarAbs(const_im);
    if (brm > bim) {
      bim = const_im / b_const_re;
      c_const_re = b_const_re + bim * const_im;
      c_const_im = (ar + bim * ai) / c_const_re;
      hamiltonian = (ai - bim * ar) / c_const_re;
    } else if (bim == brm) {
      if (b_const_re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (const_im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      c_const_im = (ar * lamX_re + ai * c_const_re) / brm;
      hamiltonian = (ai * lamX_re - ar * c_const_re) / brm;
    } else {
      bim = b_const_re / const_im;
      c_const_re = const_im + bim * b_const_re;
      c_const_im = (bim * ar + ai) / c_const_re;
      hamiltonian = (bim * ai - ar) / c_const_re;
    }
  }

  re = (re - lamY_re) - c_const_im;
  lamY_im = (lamY_im - lamX_im) - hamiltonian;
  c_const_im = v_re * re - v_im * lamY_im;
  v_im = v_re * lamY_im + v_im * re;
  hamiltonian = 8112.0 * dc0.re;
  c_const_re = 8112.0 * dc0.im;
  if (c_const_re == 0.0) {
    if (v_im == 0.0) {
      ld_v.re = c_const_im / hamiltonian;
      ld_v.im = 0.0;
    } else if (c_const_im == 0.0) {
      ld_v.re = 0.0;
      ld_v.im = v_im / hamiltonian;
    } else {
      ld_v.re = c_const_im / hamiltonian;
      ld_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (c_const_im == 0.0) {
      ld_v.re = v_im / c_const_re;
      ld_v.im = 0.0;
    } else if (v_im == 0.0) {
      ld_v.re = 0.0;
      ld_v.im = -(c_const_im / c_const_re);
    } else {
      ld_v.re = v_im / c_const_re;
      ld_v.im = -(c_const_im / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(c_const_re);
    if (brm > bim) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      ld_v.re = (c_const_im + bim * v_im) / c_const_re;
      ld_v.im = (v_im - bim * c_const_im) / c_const_re;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (c_const_re > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      ld_v.re = (c_const_im * lamX_re + v_im * c_const_re) / brm;
      ld_v.im = (v_im * lamX_re - c_const_im * c_const_re) / brm;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      ld_v.re = (bim * c_const_im + v_im) / c_const_re;
      ld_v.im = (bim * v_im - c_const_im) / c_const_re;
    }
  }

  dc1 = c_mpower(ld_v);
  ar = dc1.re - 1860.0;
  ai = dc1.im;
  if (ai == 0.0) {
    dc0.re = ar / 1560.0;
    dc0.im = 0.0;
  } else if (ar == 0.0) {
    dc0.re = 0.0;
    dc0.im = ai / 1560.0;
  } else {
    dc0.re = ar / 1560.0;
    dc0.im = ai / 1560.0;
  }

  c_asin(&dc0);
  Ttrignew = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    Ttrignew = 0.0;
  }

  emlrtPushRtStackR2012b(&dc_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = mpower(1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0);
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  md_v.re = xAndLambda[3] * xAndLambda[3];
  md_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, md_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0);
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  tc_const.re = b_const->mass * xAndLambda[3];
  tc_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig))
                * (b_const->g * b_const->mass + muDoubleScalarSin
                   (b_const->alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0)), tc_const);
  md_z.re = xAndLambda[2] + 50.0;
  md_z.im = 0.0;
  v = b_mpower(md_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        sc_v_re = 0.5;
      } else {
        sc_v_re = -0.5;
      }

      if (v_im > 0.0) {
        sc_v_im = 0.5;
      } else {
        sc_v_im = -0.5;
      }

      re = (ar * sc_v_re + ai * sc_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda[10] * (b_const->g * b_const->mass + muDoubleScalarSin
                      (b_const->alfamax * muDoubleScalarSin(alfatrig)) * (1560.0
    * muDoubleScalarSin(Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (b_const->g * b_const->mass + muDoubleScalarSin(b_const->alfamax *
      muDoubleScalarSin(alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) +
      1860.0));
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        uc_const_re = 0.5;
      } else {
        uc_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        uc_const_im = 0.5;
      } else {
        uc_const_im = -0.5;
      }

      bim = (ar * uc_const_re + ai * uc_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  emlrtPopRtStackR2012b(&dc_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(-b_const->bankmax);
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(-b_const->bankmax);
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(-(2.0 * b_const->bankmax));
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(-(2.0 * b_const->bankmax));
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  re = dc0.re;
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      dc0.re = b_const_im / dc0.re;
      dc0.im = 0.0;
    } else if (b_const_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = Ttrignew / re;
    } else {
      dc0.re = b_const_im / dc0.re;
      dc0.im = Ttrignew / re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = 0.0;
    } else if (Ttrignew == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(b_const_im / lamY_im);
    } else {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = -(b_const_im / lamY_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      dc0.re = (b_const_im + bim * Ttrignew) / c_const_re;
      dc0.im = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      dc0.re = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      dc0.im = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      dc0.re = (bim * b_const_im + Ttrignew) / c_const_re;
      dc0.im = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_cos(&dc0);
  a = gam;
  b_cos(&a);
  nd_z.re = xAndLambda[2] + 50.0;
  nd_z.im = 0.0;
  dc1 = b_mpower(nd_z);
  v_re = xAndLambda[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda[9] * muDoubleScalarCos(b_const->alfamax *
          muDoubleScalarSin(alfatrig)));
  ai = -(0.0 * muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)));
  if (ai == 0.0) {
    re = ar / b_const->mass;
    lamY_im = 0.0;
  } else if (ar == 0.0) {
    re = 0.0;
    lamY_im = ai / b_const->mass;
  } else {
    re = ar / b_const->mass;
    lamY_im = ai / b_const->mass;
  }

  ar = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * xAndLambda[11]) * muDoubleScalarCos(-b_const->bankmax);
  ai = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarCos(-b_const->bankmax);
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_re = b_const->mass * 0.0;
  if (c_const_re == 0.0) {
    if (ai == 0.0) {
      lamY_re = ar / hamiltonian;
      lamX_im = 0.0;
    } else if (ar == 0.0) {
      lamY_re = 0.0;
      lamX_im = ai / hamiltonian;
    } else {
      lamY_re = ar / hamiltonian;
      lamX_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      lamY_re = ai / c_const_re;
      lamX_im = 0.0;
    } else if (ai == 0.0) {
      lamY_re = 0.0;
      lamX_im = -(ar / c_const_re);
    } else {
      lamY_re = ai / c_const_re;
      lamX_im = -(ar / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > c_const_re) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      lamY_re = (ar + bim * ai) / c_const_re;
      lamX_im = (ai - bim * ar) / c_const_re;
    } else if (c_const_re == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      lamY_re = (ar * lamX_re + ai * -0.5) / 0.0;
      lamX_im = (ai * lamX_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      lamY_re = (bim * ar + ai) / c_const_re;
      lamX_im = (bim * ai - ar) / c_const_re;
    }
  }

  const_re = b_const->mass * xAndLambda[3];
  const_im = b_const->mass * 0.0;
  b_const_re = const_re * a.re - const_im * a.im;
  const_im = const_re * a.im + const_im * a.re;
  ar = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * xAndLambda[10]) * muDoubleScalarSin(-b_const->bankmax);
  ai = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarSin(-b_const->bankmax);
  if (const_im == 0.0) {
    if (ai == 0.0) {
      c_const_im = ar / b_const_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      c_const_im = 0.0;
      hamiltonian = ai / b_const_re;
    } else {
      c_const_im = ar / b_const_re;
      hamiltonian = ai / b_const_re;
    }
  } else if (b_const_re == 0.0) {
    if (ar == 0.0) {
      c_const_im = ai / const_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      c_const_im = 0.0;
      hamiltonian = -(ar / const_im);
    } else {
      c_const_im = ai / const_im;
      hamiltonian = -(ar / const_im);
    }
  } else {
    brm = muDoubleScalarAbs(b_const_re);
    bim = muDoubleScalarAbs(const_im);
    if (brm > bim) {
      bim = const_im / b_const_re;
      c_const_re = b_const_re + bim * const_im;
      c_const_im = (ar + bim * ai) / c_const_re;
      hamiltonian = (ai - bim * ar) / c_const_re;
    } else if (bim == brm) {
      if (b_const_re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (const_im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      c_const_im = (ar * lamX_re + ai * c_const_re) / brm;
      hamiltonian = (ai * lamX_re - ar * c_const_re) / brm;
    } else {
      bim = b_const_re / const_im;
      c_const_re = const_im + bim * b_const_re;
      c_const_im = (bim * ar + ai) / c_const_re;
      hamiltonian = (bim * ai - ar) / c_const_re;
    }
  }

  re = (re - lamY_re) - c_const_im;
  lamY_im = (lamY_im - lamX_im) - hamiltonian;
  c_const_im = v_re * re - v_im * lamY_im;
  v_im = v_re * lamY_im + v_im * re;
  hamiltonian = 8112.0 * dc0.re;
  c_const_re = 8112.0 * dc0.im;
  if (c_const_re == 0.0) {
    if (v_im == 0.0) {
      nd_v.re = c_const_im / hamiltonian;
      nd_v.im = 0.0;
    } else if (c_const_im == 0.0) {
      nd_v.re = 0.0;
      nd_v.im = v_im / hamiltonian;
    } else {
      nd_v.re = c_const_im / hamiltonian;
      nd_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (c_const_im == 0.0) {
      nd_v.re = v_im / c_const_re;
      nd_v.im = 0.0;
    } else if (v_im == 0.0) {
      nd_v.re = 0.0;
      nd_v.im = -(c_const_im / c_const_re);
    } else {
      nd_v.re = v_im / c_const_re;
      nd_v.im = -(c_const_im / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(c_const_re);
    if (brm > bim) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      nd_v.re = (c_const_im + bim * v_im) / c_const_re;
      nd_v.im = (v_im - bim * c_const_im) / c_const_re;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (c_const_re > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      nd_v.re = (c_const_im * lamX_re + v_im * c_const_re) / brm;
      nd_v.im = (v_im * lamX_re - c_const_im * c_const_re) / brm;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      nd_v.re = (bim * c_const_im + v_im) / c_const_re;
      nd_v.im = (bim * v_im - c_const_im) / c_const_re;
    }
  }

  dc1 = c_mpower(nd_v);
  ar = dc1.re - 1860.0;
  ai = dc1.im;
  if (ai == 0.0) {
    dc0.re = ar / 1560.0;
    dc0.im = 0.0;
  } else if (ar == 0.0) {
    dc0.re = 0.0;
    dc0.im = ai / 1560.0;
  } else {
    dc0.re = ar / 1560.0;
    dc0.im = ai / 1560.0;
  }

  c_asin(&dc0);
  Ttrignew = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    Ttrignew = 0.0;
  }

  emlrtPushRtStackR2012b(&ec_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = mpower(1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0);
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  od_v.re = xAndLambda[3] * xAndLambda[3];
  od_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, od_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0);
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  uc_const.re = b_const->mass * xAndLambda[3];
  uc_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(-b_const->bankmax) * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0)), uc_const);
  od_z.re = xAndLambda[2] + 50.0;
  od_z.im = 0.0;
  v = b_mpower(od_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        tc_v_re = 0.5;
      } else {
        tc_v_re = -0.5;
      }

      if (v_im > 0.0) {
        tc_v_im = 0.5;
      } else {
        tc_v_im = -0.5;
      }

      re = (ar * tc_v_re + ai * tc_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(-b_const->bankmax) * xAndLambda[10] * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(-b_const->bankmax) * 0.0 * (b_const->g * b_const->mass
    + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0));
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        vc_const_re = 0.5;
      } else {
        vc_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        vc_const_im = 0.5;
      } else {
        vc_const_im = -0.5;
      }

      bim = (ar * vc_const_re + ai * vc_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  emlrtPopRtStackR2012b(&ec_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = -1.5707963267948966;
    *alfatrigSave = alfatrig;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(b_const->bankmax);
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(b_const->bankmax);
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(2.0 * b_const->bankmax);
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(2.0 * b_const->bankmax);
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  re = dc0.re;
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      dc0.re = b_const_im / dc0.re;
      dc0.im = 0.0;
    } else if (b_const_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = Ttrignew / re;
    } else {
      dc0.re = b_const_im / dc0.re;
      dc0.im = Ttrignew / re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = 0.0;
    } else if (Ttrignew == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(b_const_im / lamY_im);
    } else {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = -(b_const_im / lamY_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      dc0.re = (b_const_im + bim * Ttrignew) / c_const_re;
      dc0.im = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      dc0.re = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      dc0.im = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      dc0.re = (bim * b_const_im + Ttrignew) / c_const_re;
      dc0.im = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_cos(&dc0);
  a = gam;
  b_cos(&a);
  pd_z.re = xAndLambda[2] + 50.0;
  pd_z.im = 0.0;
  dc1 = b_mpower(pd_z);
  v_re = xAndLambda[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda[9] * muDoubleScalarCos(b_const->alfamax *
          muDoubleScalarSin(alfatrig)));
  ai = -(0.0 * muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)));
  if (ai == 0.0) {
    re = ar / b_const->mass;
    lamY_im = 0.0;
  } else if (ar == 0.0) {
    re = 0.0;
    lamY_im = ai / b_const->mass;
  } else {
    re = ar / b_const->mass;
    lamY_im = ai / b_const->mass;
  }

  ar = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * xAndLambda[11]) * muDoubleScalarCos(b_const->bankmax);
  ai = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarCos(b_const->bankmax);
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_re = b_const->mass * 0.0;
  if (c_const_re == 0.0) {
    if (ai == 0.0) {
      lamY_re = ar / hamiltonian;
      lamX_im = 0.0;
    } else if (ar == 0.0) {
      lamY_re = 0.0;
      lamX_im = ai / hamiltonian;
    } else {
      lamY_re = ar / hamiltonian;
      lamX_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      lamY_re = ai / c_const_re;
      lamX_im = 0.0;
    } else if (ai == 0.0) {
      lamY_re = 0.0;
      lamX_im = -(ar / c_const_re);
    } else {
      lamY_re = ai / c_const_re;
      lamX_im = -(ar / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > c_const_re) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      lamY_re = (ar + bim * ai) / c_const_re;
      lamX_im = (ai - bim * ar) / c_const_re;
    } else if (c_const_re == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      lamY_re = (ar * lamX_re + ai * -0.5) / 0.0;
      lamX_im = (ai * lamX_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      lamY_re = (bim * ar + ai) / c_const_re;
      lamX_im = (bim * ai - ar) / c_const_re;
    }
  }

  const_re = b_const->mass * xAndLambda[3];
  const_im = b_const->mass * 0.0;
  b_const_re = const_re * a.re - const_im * a.im;
  const_im = const_re * a.im + const_im * a.re;
  ar = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * xAndLambda[10]) * muDoubleScalarSin(b_const->bankmax);
  ai = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarSin(b_const->bankmax);
  if (const_im == 0.0) {
    if (ai == 0.0) {
      c_const_im = ar / b_const_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      c_const_im = 0.0;
      hamiltonian = ai / b_const_re;
    } else {
      c_const_im = ar / b_const_re;
      hamiltonian = ai / b_const_re;
    }
  } else if (b_const_re == 0.0) {
    if (ar == 0.0) {
      c_const_im = ai / const_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      c_const_im = 0.0;
      hamiltonian = -(ar / const_im);
    } else {
      c_const_im = ai / const_im;
      hamiltonian = -(ar / const_im);
    }
  } else {
    brm = muDoubleScalarAbs(b_const_re);
    bim = muDoubleScalarAbs(const_im);
    if (brm > bim) {
      bim = const_im / b_const_re;
      c_const_re = b_const_re + bim * const_im;
      c_const_im = (ar + bim * ai) / c_const_re;
      hamiltonian = (ai - bim * ar) / c_const_re;
    } else if (bim == brm) {
      if (b_const_re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (const_im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      c_const_im = (ar * lamX_re + ai * c_const_re) / brm;
      hamiltonian = (ai * lamX_re - ar * c_const_re) / brm;
    } else {
      bim = b_const_re / const_im;
      c_const_re = const_im + bim * b_const_re;
      c_const_im = (bim * ar + ai) / c_const_re;
      hamiltonian = (bim * ai - ar) / c_const_re;
    }
  }

  re = (re - lamY_re) - c_const_im;
  lamY_im = (lamY_im - lamX_im) - hamiltonian;
  c_const_im = v_re * re - v_im * lamY_im;
  v_im = v_re * lamY_im + v_im * re;
  hamiltonian = 8112.0 * dc0.re;
  c_const_re = 8112.0 * dc0.im;
  if (c_const_re == 0.0) {
    if (v_im == 0.0) {
      pd_v.re = c_const_im / hamiltonian;
      pd_v.im = 0.0;
    } else if (c_const_im == 0.0) {
      pd_v.re = 0.0;
      pd_v.im = v_im / hamiltonian;
    } else {
      pd_v.re = c_const_im / hamiltonian;
      pd_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (c_const_im == 0.0) {
      pd_v.re = v_im / c_const_re;
      pd_v.im = 0.0;
    } else if (v_im == 0.0) {
      pd_v.re = 0.0;
      pd_v.im = -(c_const_im / c_const_re);
    } else {
      pd_v.re = v_im / c_const_re;
      pd_v.im = -(c_const_im / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(c_const_re);
    if (brm > bim) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      pd_v.re = (c_const_im + bim * v_im) / c_const_re;
      pd_v.im = (v_im - bim * c_const_im) / c_const_re;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (c_const_re > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      pd_v.re = (c_const_im * lamX_re + v_im * c_const_re) / brm;
      pd_v.im = (v_im * lamX_re - c_const_im * c_const_re) / brm;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      pd_v.re = (bim * c_const_im + v_im) / c_const_re;
      pd_v.im = (bim * v_im - c_const_im) / c_const_re;
    }
  }

  dc1 = c_mpower(pd_v);
  ar = dc1.re - 1860.0;
  ai = dc1.im;
  if (ai == 0.0) {
    dc0.re = ar / 1560.0;
    dc0.im = 0.0;
  } else if (ar == 0.0) {
    dc0.re = 0.0;
    dc0.im = ai / 1560.0;
  } else {
    dc0.re = ar / 1560.0;
    dc0.im = ai / 1560.0;
  }

  c_asin(&dc0);
  Ttrignew = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    Ttrignew = 0.0;
  }

  emlrtPushRtStackR2012b(&fc_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = mpower(1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0);
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  qd_v.re = xAndLambda[3] * xAndLambda[3];
  qd_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, qd_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0);
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  vc_const.re = b_const->mass * xAndLambda[3];
  vc_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax) * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0)), vc_const);
  qd_z.re = xAndLambda[2] + 50.0;
  qd_z.im = 0.0;
  v = b_mpower(qd_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        uc_v_re = 0.5;
      } else {
        uc_v_re = -0.5;
      }

      if (v_im > 0.0) {
        uc_v_im = 0.5;
      } else {
        uc_v_im = -0.5;
      }

      re = (ar * uc_v_re + ai * uc_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax) * xAndLambda[10] * (b_const->g *
    b_const->mass + muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin
    (alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(b_const->bankmax) * 0.0 * (b_const->g * b_const->mass +
    muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0));
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        wc_const_re = 0.5;
      } else {
        wc_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        wc_const_im = 0.5;
      } else {
        wc_const_im = -0.5;
      }

      bim = (ar * wc_const_re + ai * wc_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  emlrtPopRtStackR2012b(&fc_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = 1.5707963267948966;
    *alfatrigSave = alfatrig;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&gc_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = 3.1416 / (2.0 * b_const->bankmax);
  b_asin(&hamiltonian);
  banktrig = -hamiltonian;
  emlrtPopRtStackR2012b(&gc_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(-hamiltonian) || muDoubleScalarIsInf(-hamiltonian)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(2.0 * b_const->bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(2.0 * b_const->bankmax * muDoubleScalarSin(banktrig));
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  re = dc0.re;
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      dc0.re = b_const_im / dc0.re;
      dc0.im = 0.0;
    } else if (b_const_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = Ttrignew / re;
    } else {
      dc0.re = b_const_im / dc0.re;
      dc0.im = Ttrignew / re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = 0.0;
    } else if (Ttrignew == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(b_const_im / lamY_im);
    } else {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = -(b_const_im / lamY_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      dc0.re = (b_const_im + bim * Ttrignew) / c_const_re;
      dc0.im = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      dc0.re = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      dc0.im = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      dc0.re = (bim * b_const_im + Ttrignew) / c_const_re;
      dc0.im = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_cos(&dc0);
  a = gam;
  b_cos(&a);
  rd_z.re = xAndLambda[2] + 50.0;
  rd_z.im = 0.0;
  dc1 = b_mpower(rd_z);
  v_re = xAndLambda[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda[9] * muDoubleScalarCos(b_const->alfamax *
          muDoubleScalarSin(alfatrig)));
  ai = -(0.0 * muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)));
  if (ai == 0.0) {
    re = ar / b_const->mass;
    lamY_im = 0.0;
  } else if (ar == 0.0) {
    re = 0.0;
    lamY_im = ai / b_const->mass;
  } else {
    re = ar / b_const->mass;
    lamY_im = ai / b_const->mass;
  }

  ar = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * xAndLambda[11]) * muDoubleScalarCos(b_const->bankmax *
    muDoubleScalarSin(banktrig));
  ai = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig));
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_re = b_const->mass * 0.0;
  if (c_const_re == 0.0) {
    if (ai == 0.0) {
      lamY_re = ar / hamiltonian;
      lamX_im = 0.0;
    } else if (ar == 0.0) {
      lamY_re = 0.0;
      lamX_im = ai / hamiltonian;
    } else {
      lamY_re = ar / hamiltonian;
      lamX_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      lamY_re = ai / c_const_re;
      lamX_im = 0.0;
    } else if (ai == 0.0) {
      lamY_re = 0.0;
      lamX_im = -(ar / c_const_re);
    } else {
      lamY_re = ai / c_const_re;
      lamX_im = -(ar / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > c_const_re) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      lamY_re = (ar + bim * ai) / c_const_re;
      lamX_im = (ai - bim * ar) / c_const_re;
    } else if (c_const_re == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      lamY_re = (ar * lamX_re + ai * -0.5) / 0.0;
      lamX_im = (ai * lamX_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      lamY_re = (bim * ar + ai) / c_const_re;
      lamX_im = (bim * ai - ar) / c_const_re;
    }
  }

  const_re = b_const->mass * xAndLambda[3];
  const_im = b_const->mass * 0.0;
  b_const_re = const_re * a.re - const_im * a.im;
  const_im = const_re * a.im + const_im * a.re;
  ar = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * xAndLambda[10]) * muDoubleScalarSin(b_const->bankmax *
    muDoubleScalarSin(banktrig));
  ai = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig));
  if (const_im == 0.0) {
    if (ai == 0.0) {
      c_const_im = ar / b_const_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      c_const_im = 0.0;
      hamiltonian = ai / b_const_re;
    } else {
      c_const_im = ar / b_const_re;
      hamiltonian = ai / b_const_re;
    }
  } else if (b_const_re == 0.0) {
    if (ar == 0.0) {
      c_const_im = ai / const_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      c_const_im = 0.0;
      hamiltonian = -(ar / const_im);
    } else {
      c_const_im = ai / const_im;
      hamiltonian = -(ar / const_im);
    }
  } else {
    brm = muDoubleScalarAbs(b_const_re);
    bim = muDoubleScalarAbs(const_im);
    if (brm > bim) {
      bim = const_im / b_const_re;
      c_const_re = b_const_re + bim * const_im;
      c_const_im = (ar + bim * ai) / c_const_re;
      hamiltonian = (ai - bim * ar) / c_const_re;
    } else if (bim == brm) {
      if (b_const_re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (const_im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      c_const_im = (ar * lamX_re + ai * c_const_re) / brm;
      hamiltonian = (ai * lamX_re - ar * c_const_re) / brm;
    } else {
      bim = b_const_re / const_im;
      c_const_re = const_im + bim * b_const_re;
      c_const_im = (bim * ar + ai) / c_const_re;
      hamiltonian = (bim * ai - ar) / c_const_re;
    }
  }

  re = (re - lamY_re) - c_const_im;
  lamY_im = (lamY_im - lamX_im) - hamiltonian;
  c_const_im = v_re * re - v_im * lamY_im;
  v_im = v_re * lamY_im + v_im * re;
  hamiltonian = 8112.0 * dc0.re;
  c_const_re = 8112.0 * dc0.im;
  if (c_const_re == 0.0) {
    if (v_im == 0.0) {
      rd_v.re = c_const_im / hamiltonian;
      rd_v.im = 0.0;
    } else if (c_const_im == 0.0) {
      rd_v.re = 0.0;
      rd_v.im = v_im / hamiltonian;
    } else {
      rd_v.re = c_const_im / hamiltonian;
      rd_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (c_const_im == 0.0) {
      rd_v.re = v_im / c_const_re;
      rd_v.im = 0.0;
    } else if (v_im == 0.0) {
      rd_v.re = 0.0;
      rd_v.im = -(c_const_im / c_const_re);
    } else {
      rd_v.re = v_im / c_const_re;
      rd_v.im = -(c_const_im / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(c_const_re);
    if (brm > bim) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      rd_v.re = (c_const_im + bim * v_im) / c_const_re;
      rd_v.im = (v_im - bim * c_const_im) / c_const_re;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (c_const_re > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      rd_v.re = (c_const_im * lamX_re + v_im * c_const_re) / brm;
      rd_v.im = (v_im * lamX_re - c_const_im * c_const_re) / brm;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      rd_v.re = (bim * c_const_im + v_im) / c_const_re;
      rd_v.im = (bim * v_im - c_const_im) / c_const_re;
    }
  }

  dc1 = c_mpower(rd_v);
  ar = dc1.re - 1860.0;
  ai = dc1.im;
  if (ai == 0.0) {
    dc0.re = ar / 1560.0;
    dc0.im = 0.0;
  } else if (ar == 0.0) {
    dc0.re = 0.0;
    dc0.im = ai / 1560.0;
  } else {
    dc0.re = ar / 1560.0;
    dc0.im = ai / 1560.0;
  }

  c_asin(&dc0);
  Ttrignew = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    Ttrignew = 0.0;
  }

  emlrtPushRtStackR2012b(&hc_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = mpower(1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0);
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  dc4 = psii;
  b_sin(&dc4);
  dc5 = gam;
  b_cos(&dc5);
  dc6 = gam;
  b_sin(&dc6);
  dc7 = gam;
  b_cos(&dc7);
  sd_v.re = xAndLambda[3] * xAndLambda[3];
  sd_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  v = eml_div(b_const->C2, sd_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + v.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0);
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + v.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * dc7.re;
  ai = b_const->g * dc7.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  wc_const.re = b_const->mass * xAndLambda[3];
  wc_const.im = b_const->mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig))
                * (b_const->g * b_const->mass + muDoubleScalarSin
                   (b_const->alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0)), wc_const);
  sd_z.re = xAndLambda[2] + 50.0;
  sd_z.im = 0.0;
  v = b_mpower(sd_z);
  v_re = xAndLambda[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        vc_v_re = 0.5;
      } else {
        vc_v_re = -0.5;
      }

      if (v_im > 0.0) {
        vc_v_im = 0.5;
      } else {
        vc_v_im = -0.5;
      }

      re = (ar * vc_v_re + ai * vc_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc5.re - c_const_im * dc5.im;
  c_const_im = hamiltonian * dc5.im + c_const_im * dc5.re;
  ar = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda[10] * (b_const->g * b_const->mass + muDoubleScalarSin
                      (b_const->alfamax * muDoubleScalarSin(alfatrig)) * (1560.0
    * muDoubleScalarSin(Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (b_const->g * b_const->mass + muDoubleScalarSin(b_const->alfamax *
      muDoubleScalarSin(alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) +
      1860.0));
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        xc_const_re = 0.5;
      } else {
        xc_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        xc_const_im = 0.5;
      } else {
        xc_const_im = -0.5;
      }

      bim = (ar * xc_const_re + ai * xc_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc6.re) - 0.0 * (const_im + b_const->g * dc6.im))) -
                    (xAndLambda[11] * (b_const_re - dc7.re) - 0.0 * (b_const_im
    - dc7.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + bim;
  emlrtPopRtStackR2012b(&hc_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&ic_emlrtRSI, emlrtRootTLSGlobal);
  banktrig = 3.1416 / (2.0 * b_const->bankmax);
  b_asin(&banktrig);
  emlrtPopRtStackR2012b(&ic_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(banktrig) || muDoubleScalarIsInf(banktrig)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  c_const_im = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[9];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[9];
  v_re = xAndLambda[3] * xAndLambda[3];
  v_im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  bim = xAndLambda[10] * xAndLambda[10];
  c_const_re = xAndLambda[10] * 0.0 + 0.0 * xAndLambda[10];
  re = a.re * a.re - a.im * a.im;
  lamX_re = a.re * a.im + a.im * a.re;
  lamX_im = xAndLambda[11] * xAndLambda[10];
  lamY_re = xAndLambda[11] * 0.0 + 0.0 * xAndLambda[10];
  lamY_im = lamX_im * dc0.im + lamY_re * dc0.re;
  dc0.re = (((b_const_im * v_re - Ttrignew * v_im) + xAndLambda[11] *
             xAndLambda[11] * (hamiltonian * hamiltonian)) + (bim * re -
             c_const_re * lamX_re) * (c_const_im * c_const_im)) + (lamX_im *
    dc0.re - lamY_re * dc0.im) * muDoubleScalarSin(2.0 * b_const->bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((b_const_im * v_im + Ttrignew * v_re) + (xAndLambda[11] * 0.0 + 0.0
              * xAndLambda[11]) * (hamiltonian * hamiltonian)) + (bim * lamX_re
             + c_const_re * re) * (c_const_im * c_const_im)) + lamY_im *
    muDoubleScalarSin(2.0 * b_const->bankmax * muDoubleScalarSin(banktrig));
  eml_scalar_sqrt(&dc0);
  b_const_im = xAndLambda[9] * xAndLambda[3];
  Ttrignew = xAndLambda[9] * 0.0 + 0.0 * xAndLambda[3];
  re = dc0.re;
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    if (Ttrignew == 0.0) {
      dc0.re = b_const_im / dc0.re;
      dc0.im = 0.0;
    } else if (b_const_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = Ttrignew / re;
    } else {
      dc0.re = b_const_im / dc0.re;
      dc0.im = Ttrignew / re;
    }
  } else if (dc0.re == 0.0) {
    if (b_const_im == 0.0) {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = 0.0;
    } else if (Ttrignew == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(b_const_im / lamY_im);
    } else {
      dc0.re = Ttrignew / dc0.im;
      dc0.im = -(b_const_im / lamY_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      c_const_re = dc0.re + bim * dc0.im;
      dc0.re = (b_const_im + bim * Ttrignew) / c_const_re;
      dc0.im = (Ttrignew - bim * b_const_im) / c_const_re;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (dc0.im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      dc0.re = (b_const_im * lamX_re + Ttrignew * c_const_re) / brm;
      dc0.im = (Ttrignew * lamX_re - b_const_im * c_const_re) / brm;
    } else {
      bim = dc0.re / dc0.im;
      c_const_re = dc0.im + bim * dc0.re;
      dc0.re = (bim * b_const_im + Ttrignew) / c_const_re;
      dc0.im = (bim * Ttrignew - b_const_im) / c_const_re;
    }
  }

  b_acos(&dc0);
  lamY_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= b_const->alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = lamY_im / b_const->alfamax;
  } else {
    dc0.re /= b_const->alfamax;
    dc0.im = lamY_im / b_const->alfamax;
  }

  c_asin(&dc0);
  alfatrig = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    alfatrig = 0.0;
  }

  /*  Coefficients */
  dc0 = gam;
  b_cos(&dc0);
  a = gam;
  b_cos(&a);
  td_z.re = xAndLambda[2] + 50.0;
  td_z.im = 0.0;
  dc1 = b_mpower(td_z);
  v_re = xAndLambda[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda[9] * muDoubleScalarCos(b_const->alfamax *
          muDoubleScalarSin(alfatrig)));
  ai = -(0.0 * muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)));
  if (ai == 0.0) {
    re = ar / b_const->mass;
    lamY_im = 0.0;
  } else if (ar == 0.0) {
    re = 0.0;
    lamY_im = ai / b_const->mass;
  } else {
    re = ar / b_const->mass;
    lamY_im = ai / b_const->mass;
  }

  ar = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * xAndLambda[11]) * muDoubleScalarCos(b_const->bankmax *
    muDoubleScalarSin(banktrig));
  ai = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig));
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_re = b_const->mass * 0.0;
  if (c_const_re == 0.0) {
    if (ai == 0.0) {
      lamY_re = ar / hamiltonian;
      lamX_im = 0.0;
    } else if (ar == 0.0) {
      lamY_re = 0.0;
      lamX_im = ai / hamiltonian;
    } else {
      lamY_re = ar / hamiltonian;
      lamX_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      lamY_re = ai / c_const_re;
      lamX_im = 0.0;
    } else if (ai == 0.0) {
      lamY_re = 0.0;
      lamX_im = -(ar / c_const_re);
    } else {
      lamY_re = ai / c_const_re;
      lamX_im = -(ar / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > c_const_re) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      lamY_re = (ar + bim * ai) / c_const_re;
      lamX_im = (ai - bim * ar) / c_const_re;
    } else if (c_const_re == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      lamY_re = (ar * lamX_re + ai * -0.5) / 0.0;
      lamX_im = (ai * lamX_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      lamY_re = (bim * ar + ai) / c_const_re;
      lamX_im = (bim * ai - ar) / c_const_re;
    }
  }

  const_re = b_const->mass * xAndLambda[3];
  const_im = b_const->mass * 0.0;
  b_const_re = const_re * a.re - const_im * a.im;
  const_im = const_re * a.im + const_im * a.re;
  ar = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * xAndLambda[10]) * muDoubleScalarSin(b_const->bankmax *
    muDoubleScalarSin(banktrig));
  ai = muDoubleScalarSin(b_const->alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig));
  if (const_im == 0.0) {
    if (ai == 0.0) {
      c_const_im = ar / b_const_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      c_const_im = 0.0;
      hamiltonian = ai / b_const_re;
    } else {
      c_const_im = ar / b_const_re;
      hamiltonian = ai / b_const_re;
    }
  } else if (b_const_re == 0.0) {
    if (ar == 0.0) {
      c_const_im = ai / const_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      c_const_im = 0.0;
      hamiltonian = -(ar / const_im);
    } else {
      c_const_im = ai / const_im;
      hamiltonian = -(ar / const_im);
    }
  } else {
    brm = muDoubleScalarAbs(b_const_re);
    bim = muDoubleScalarAbs(const_im);
    if (brm > bim) {
      bim = const_im / b_const_re;
      c_const_re = b_const_re + bim * const_im;
      c_const_im = (ar + bim * ai) / c_const_re;
      hamiltonian = (ai - bim * ar) / c_const_re;
    } else if (bim == brm) {
      if (b_const_re > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (const_im > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      c_const_im = (ar * lamX_re + ai * c_const_re) / brm;
      hamiltonian = (ai * lamX_re - ar * c_const_re) / brm;
    } else {
      bim = b_const_re / const_im;
      c_const_re = const_im + bim * b_const_re;
      c_const_im = (bim * ar + ai) / c_const_re;
      hamiltonian = (bim * ai - ar) / c_const_re;
    }
  }

  re = (re - lamY_re) - c_const_im;
  lamY_im = (lamY_im - lamX_im) - hamiltonian;
  c_const_im = v_re * re - v_im * lamY_im;
  v_im = v_re * lamY_im + v_im * re;
  hamiltonian = 8112.0 * dc0.re;
  c_const_re = 8112.0 * dc0.im;
  if (c_const_re == 0.0) {
    if (v_im == 0.0) {
      td_v.re = c_const_im / hamiltonian;
      td_v.im = 0.0;
    } else if (c_const_im == 0.0) {
      td_v.re = 0.0;
      td_v.im = v_im / hamiltonian;
    } else {
      td_v.re = c_const_im / hamiltonian;
      td_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (c_const_im == 0.0) {
      td_v.re = v_im / c_const_re;
      td_v.im = 0.0;
    } else if (v_im == 0.0) {
      td_v.re = 0.0;
      td_v.im = -(c_const_im / c_const_re);
    } else {
      td_v.re = v_im / c_const_re;
      td_v.im = -(c_const_im / c_const_re);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(c_const_re);
    if (brm > bim) {
      bim = c_const_re / hamiltonian;
      c_const_re = hamiltonian + bim * c_const_re;
      td_v.re = (c_const_im + bim * v_im) / c_const_re;
      td_v.im = (v_im - bim * c_const_im) / c_const_re;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamX_re = 0.5;
      } else {
        lamX_re = -0.5;
      }

      if (c_const_re > 0.0) {
        c_const_re = 0.5;
      } else {
        c_const_re = -0.5;
      }

      td_v.re = (c_const_im * lamX_re + v_im * c_const_re) / brm;
      td_v.im = (v_im * lamX_re - c_const_im * c_const_re) / brm;
    } else {
      bim = hamiltonian / c_const_re;
      c_const_re += bim * hamiltonian;
      td_v.re = (bim * c_const_im + v_im) / c_const_re;
      td_v.im = (bim * v_im - c_const_im) / c_const_re;
    }
  }

  dc1 = c_mpower(td_v);
  ar = dc1.re - 1860.0;
  ai = dc1.im;
  if (ai == 0.0) {
    dc0.re = ar / 1560.0;
    dc0.im = 0.0;
  } else if (ar == 0.0) {
    dc0.re = 0.0;
    dc0.im = ai / 1560.0;
  } else {
    dc0.re = ar / 1560.0;
    dc0.im = ai / 1560.0;
  }

  c_asin(&dc0);
  Ttrignew = dc0.re;
  if (muDoubleScalarIsNaN(dc0.re) || muDoubleScalarIsInf(dc0.re)) {
    Ttrignew = 0.0;
  }

  emlrtPushRtStackR2012b(&jc_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = mpower(1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0);
  dc0 = gam;
  b_sin(&dc0);
  a = gam;
  b_cos(&a);
  dc1 = gam;
  b_cos(&dc1);
  dc2 = psii;
  b_cos(&dc2);
  dc3 = gam;
  b_cos(&dc3);
  b_sin(&psii);
  dc4 = gam;
  b_cos(&dc4);
  dc5 = gam;
  b_sin(&dc5);
  b_cos(&gam);
  ud_v.re = xAndLambda[3] * xAndLambda[3];
  ud_v.im = xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3];
  dc6 = eml_div(b_const->C2, ud_v);
  ar = (b_const->C1 * (xAndLambda[3] * xAndLambda[3]) + dc6.re) -
    muDoubleScalarCos(b_const->alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0);
  ai = b_const->C1 * (xAndLambda[3] * 0.0 + 0.0 * xAndLambda[3]) + dc6.im;
  if (ai == 0.0) {
    const_re = ar / b_const->mass;
    const_im = 0.0;
  } else if (ar == 0.0) {
    const_re = 0.0;
    const_im = ai / b_const->mass;
  } else {
    const_re = ar / b_const->mass;
    const_im = ai / b_const->mass;
  }

  ar = b_const->g * gam.re;
  ai = b_const->g * gam.im;
  if (ai == 0.0) {
    b_const_re = ar / xAndLambda[3];
    b_const_im = 0.0;
  } else if (ar == 0.0) {
    b_const_re = 0.0;
    b_const_im = ai / xAndLambda[3];
  } else {
    b_const_re = ar / xAndLambda[3];
    b_const_im = ai / xAndLambda[3];
  }

  xc_const.re = b_const->mass * xAndLambda[3];
  xc_const.im = b_const->mass * 0.0;
  dc6 = eml_div(muDoubleScalarCos(b_const->bankmax * muDoubleScalarSin(banktrig))
                * (b_const->g * b_const->mass + muDoubleScalarSin
                   (b_const->alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0)), xc_const);
  ud_z.re = xAndLambda[2] + 50.0;
  ud_z.im = 0.0;
  dc7 = b_mpower(ud_z);
  v_re = xAndLambda[3] * dc7.re - 0.0 * dc7.im;
  v_im = xAndLambda[3] * dc7.im + 0.0 * dc7.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      re = ar / v_re;
    } else if (ar == 0.0) {
      re = 0.0;
    } else {
      re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      re = ai / v_im;
    } else if (ai == 0.0) {
      re = 0.0;
    } else {
      re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      re = (ar + bim * ai) / (v_re + bim * v_im);
    } else if (bim == brm) {
      if (v_re > 0.0) {
        wc_v_re = 0.5;
      } else {
        wc_v_re = -0.5;
      }

      if (v_im > 0.0) {
        wc_v_im = 0.5;
      } else {
        wc_v_im = -0.5;
      }

      re = (ar * wc_v_re + ai * wc_v_im) / brm;
    } else {
      bim = v_re / v_im;
      re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda[6] * xAndLambda[3];
  lamX_im = xAndLambda[6] * 0.0 + 0.0 * xAndLambda[3];
  lamY_re = xAndLambda[7] * xAndLambda[3];
  lamY_im = xAndLambda[7] * 0.0 + 0.0 * xAndLambda[3];
  hamiltonian = b_const->mass * xAndLambda[3];
  c_const_im = b_const->mass * 0.0;
  c_const_re = hamiltonian * dc4.re - c_const_im * dc4.im;
  c_const_im = hamiltonian * dc4.im + c_const_im * dc4.re;
  ar = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda[10] * (b_const->g * b_const->mass + muDoubleScalarSin
                      (b_const->alfamax * muDoubleScalarSin(alfatrig)) * (1560.0
    * muDoubleScalarSin(Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(b_const->bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (b_const->g * b_const->mass + muDoubleScalarSin(b_const->alfamax *
      muDoubleScalarSin(alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) +
      1860.0));
  if (c_const_im == 0.0) {
    if (ai == 0.0) {
      bim = ar / c_const_re;
    } else if (ar == 0.0) {
      bim = 0.0;
    } else {
      bim = ar / c_const_re;
    }
  } else if (c_const_re == 0.0) {
    if (ar == 0.0) {
      bim = ai / c_const_im;
    } else if (ai == 0.0) {
      bim = 0.0;
    } else {
      bim = ai / c_const_im;
    }
  } else {
    brm = muDoubleScalarAbs(c_const_re);
    bim = muDoubleScalarAbs(c_const_im);
    if (brm > bim) {
      bim = c_const_im / c_const_re;
      bim = (ar + bim * ai) / (c_const_re + bim * c_const_im);
    } else if (bim == brm) {
      if (c_const_re > 0.0) {
        yc_const_re = 0.5;
      } else {
        yc_const_re = -0.5;
      }

      if (c_const_im > 0.0) {
        yc_const_im = 0.5;
      } else {
        yc_const_im = -0.5;
      }

      bim = (ar * yc_const_re + ai * yc_const_im) / brm;
    } else {
      bim = c_const_re / c_const_im;
      bim = (bim * ar + ai) / (c_const_im + bim * c_const_re);
    }
  }

  hamiltonian = ((((((xAndLambda[8] * xAndLambda[3] * dc0.re - (xAndLambda[8] *
    0.0 + 0.0 * xAndLambda[3]) * dc0.im) - (xAndLambda[9] * (const_re +
    b_const->g * dc5.re) - 0.0 * (const_im + b_const->g * dc5.im))) -
                    (xAndLambda[11] * (b_const_re - dc6.re) - 0.0 * (b_const_im
    - dc6.im))) + re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * psii.re - (lamY_re * dc3.im + lamY_im * dc3.re) *
    psii.im)) + bim;
  emlrtPopRtStackR2012b(&jc_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }
}

creal_T eml_div(real_T x, const creal_T y)
{
  creal_T z;
  real_T brm;
  real_T bim;
  real_T d;
  if (y.im == 0.0) {
    z.re = x / y.re;
    z.im = 0.0;
  } else if (y.re == 0.0) {
    if (x == 0.0) {
      z.re = 0.0 / y.im;
      z.im = 0.0;
    } else {
      z.re = 0.0;
      z.im = -(x / y.im);
    }
  } else {
    brm = muDoubleScalarAbs(y.re);
    bim = muDoubleScalarAbs(y.im);
    if (brm > bim) {
      bim = y.im / y.re;
      d = y.re + bim * y.im;
      z.re = (x + bim * 0.0) / d;
      z.im = (0.0 - bim * x) / d;
    } else if (bim == brm) {
      if (y.re > 0.0) {
        bim = 0.5;
      } else {
        bim = -0.5;
      }

      if (y.im > 0.0) {
        d = 0.5;
      } else {
        d = -0.5;
      }

      z.re = x * bim / brm;
      z.im = (-0.0 - x * d) / brm;
    } else {
      bim = y.re / y.im;
      d = y.im + bim * y.re;
      z.re = bim * x / d;
      z.im = (bim * 0.0 - x) / d;
    }
  }

  return z;
}

/* End of code generation (computeControlUnconstrained.c) */
