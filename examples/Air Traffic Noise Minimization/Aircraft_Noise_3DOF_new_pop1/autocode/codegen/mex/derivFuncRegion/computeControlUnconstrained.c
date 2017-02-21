/*
 * computeControlUnconstrained.c
 *
 * Code generation for function 'computeControlUnconstrained'
 *
 * C source code generated on: Sat Jan 21 02:02:53 2017
 *
 */

/* Include files */
#include "rt_nonfinite.h"
#include "derivFuncRegion.h"
#include "computeControlUnconstrained.h"
#include "mpower.h"
#include "cos.h"
#include "sin.h"
#include "asin.h"
#include "acos.h"
#include "sec.h"

/* Variable Definitions */
static emlrtRSInfo d_emlrtRSI = { 113, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo e_emlrtRSI = { 135, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo f_emlrtRSI = { 201, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo g_emlrtRSI = { 223, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo h_emlrtRSI = { 289, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo i_emlrtRSI = { 311, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo j_emlrtRSI = { 377, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo k_emlrtRSI = { 399, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo l_emlrtRSI = { 465, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo m_emlrtRSI = { 487, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo n_emlrtRSI = { 553, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo o_emlrtRSI = { 575, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo p_emlrtRSI = { 641, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo q_emlrtRSI = { 663, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo r_emlrtRSI = { 729, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo s_emlrtRSI = { 751, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo t_emlrtRSI = { 817, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo u_emlrtRSI = { 839, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo v_emlrtRSI = { 905, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo w_emlrtRSI = { 927, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo x_emlrtRSI = { 993, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo y_emlrtRSI = { 1015, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo ab_emlrtRSI = { 1081, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo bb_emlrtRSI = { 1103, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo cb_emlrtRSI = { 1139, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo db_emlrtRSI = { 1161, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo eb_emlrtRSI = { 1169, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo fb_emlrtRSI = { 1183, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo gb_emlrtRSI = { 1191, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo hb_emlrtRSI = { 1205, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo ib_emlrtRSI = { 1227, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo jb_emlrtRSI = { 1249, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo kb_emlrtRSI = { 1257, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo lb_emlrtRSI = { 1271, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo mb_emlrtRSI = { 1279, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo nb_emlrtRSI = { 1293, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo ob_emlrtRSI = { 1315, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo pb_emlrtRSI = { 1337, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo qb_emlrtRSI = { 1345, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo rb_emlrtRSI = { 1359, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo sb_emlrtRSI = { 1367, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo tb_emlrtRSI = { 1381, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo ub_emlrtRSI = { 1403, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo vb_emlrtRSI = { 1425, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo wb_emlrtRSI = { 1433, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo xb_emlrtRSI = { 1447, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo yb_emlrtRSI = { 1455, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo ac_emlrtRSI = { 1469, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo bc_emlrtRSI = { 1491, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo cc_emlrtRSI = { 1513, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo dc_emlrtRSI = { 1521, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo ec_emlrtRSI = { 1535, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo fc_emlrtRSI = { 1543, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo gc_emlrtRSI = { 1557, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo hc_emlrtRSI = { 1579, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo ic_emlrtRSI = { 1601, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo jc_emlrtRSI = { 1609, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo kc_emlrtRSI = { 1623, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo lc_emlrtRSI = { 1631, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

static emlrtRSInfo mc_emlrtRSI = { 1645, "computeControlUnconstrained",
  "/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m"
};

/* Function Definitions */
void computeControlUnconstrained(const real_T xAndLambda_data[12], real_T
  const_C1, real_T const_C2, real_T const_alfamax, real_T const_bankmax, real_T
  const_g, real_T const_mass, real_T *banktrigSave, real_T *alfatrigSave, real_T
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
  real_T const_C1_re;
  real_T const_C1_im;
  real_T const_g_re;
  real_T const_g_im;
  creal_T b_const_mass;
  creal_T z;
  real_T v_re;
  real_T v_im;
  real_T Ttrignew;
  real_T brm;
  real_T bim;
  real_T b_v_re;
  real_T b_v_im;
  real_T lamX_re;
  real_T lamX_im;
  real_T lamY_re;
  real_T lamY_im;
  real_T hamiltonian;
  real_T const_mass_im;
  real_T const_mass_re;
  real_T b_const_mass_re;
  real_T b_const_mass_im;
  creal_T b_v;
  creal_T c_const_mass;
  creal_T b_z;
  real_T a_re;
  real_T c_v_re;
  real_T c_v_im;
  real_T c_const_mass_re;
  real_T c_const_mass_im;
  real_T banktrig;
  creal_T c_v;
  creal_T d_const_mass;
  creal_T c_z;
  real_T d_v_re;
  real_T d_v_im;
  real_T d_const_mass_re;
  real_T d_const_mass_im;
  creal_T d_v;
  creal_T e_const_mass;
  creal_T d_z;
  real_T e_v_re;
  real_T e_v_im;
  real_T e_const_mass_re;
  real_T e_const_mass_im;
  creal_T e_v;
  creal_T f_const_mass;
  creal_T e_z;
  real_T f_v_re;
  real_T f_v_im;
  real_T f_const_mass_re;
  real_T f_const_mass_im;
  creal_T f_v;
  creal_T g_const_mass;
  creal_T f_z;
  real_T g_v_re;
  real_T g_v_im;
  real_T g_const_mass_re;
  real_T g_const_mass_im;
  creal_T g_v;
  creal_T h_const_mass;
  creal_T g_z;
  real_T h_v_re;
  real_T h_v_im;
  real_T h_const_mass_re;
  real_T h_const_mass_im;
  creal_T h_v;
  creal_T i_const_mass;
  creal_T h_z;
  real_T i_v_re;
  real_T i_v_im;
  real_T i_const_mass_re;
  real_T i_const_mass_im;
  real_T alfatrig;
  creal_T i_v;
  creal_T j_const_mass;
  creal_T i_z;
  real_T j_v_re;
  real_T j_v_im;
  real_T j_const_mass_re;
  real_T j_const_mass_im;
  creal_T j_v;
  creal_T k_const_mass;
  creal_T j_z;
  real_T k_v_re;
  real_T k_v_im;
  real_T k_const_mass_re;
  real_T k_const_mass_im;
  creal_T k_v;
  creal_T l_const_mass;
  creal_T k_z;
  real_T l_v_re;
  real_T l_v_im;
  real_T l_const_mass_re;
  real_T l_const_mass_im;
  creal_T l_v;
  creal_T m_const_mass;
  creal_T l_z;
  real_T m_v_re;
  real_T m_v_im;
  real_T m_const_mass_re;
  real_T m_const_mass_im;
  creal_T m_v;
  creal_T n_const_mass;
  creal_T m_z;
  real_T n_v_re;
  real_T n_v_im;
  real_T n_const_mass_re;
  real_T n_const_mass_im;
  creal_T n_v;
  creal_T o_const_mass;
  creal_T n_z;
  real_T o_v_re;
  real_T o_v_im;
  real_T o_const_mass_re;
  real_T o_const_mass_im;
  creal_T o_v;
  creal_T p_const_mass;
  creal_T o_z;
  real_T p_v_re;
  real_T p_v_im;
  real_T p_const_mass_re;
  real_T p_const_mass_im;
  creal_T p_v;
  creal_T q_const_mass;
  creal_T p_z;
  real_T q_v_re;
  real_T q_v_im;
  real_T q_const_mass_re;
  real_T q_const_mass_im;
  creal_T q_v;
  creal_T r_const_mass;
  creal_T q_z;
  real_T r_v_re;
  real_T r_v_im;
  real_T r_const_mass_re;
  real_T r_const_mass_im;
  creal_T r_v;
  creal_T s_const_mass;
  creal_T r_z;
  real_T s_v_re;
  real_T s_v_im;
  real_T s_const_mass_re;
  real_T s_const_mass_im;
  creal_T s_v;
  creal_T t_const_mass;
  creal_T s_z;
  real_T t_v_re;
  real_T t_v_im;
  real_T t_const_mass_re;
  real_T t_const_mass_im;
  creal_T t_v;
  creal_T u_const_mass;
  creal_T t_z;
  real_T u_v_re;
  real_T u_v_im;
  real_T u_const_mass_re;
  real_T u_const_mass_im;
  creal_T u_v;
  creal_T v_const_mass;
  creal_T u_z;
  real_T v_v_re;
  real_T v_v_im;
  real_T v_const_mass_re;
  real_T v_const_mass_im;
  creal_T v_v;
  creal_T w_const_mass;
  creal_T v_z;
  real_T w_v_re;
  real_T w_v_im;
  real_T w_const_mass_re;
  real_T w_const_mass_im;
  creal_T w_v;
  creal_T x_const_mass;
  creal_T w_z;
  real_T x_v_re;
  real_T x_v_im;
  real_T x_const_mass_re;
  real_T x_const_mass_im;
  creal_T x_v;
  creal_T y_const_mass;
  creal_T x_z;
  real_T y_v_re;
  real_T y_v_im;
  real_T y_const_mass_re;
  real_T y_const_mass_im;
  creal_T y_v;
  creal_T ab_const_mass;
  creal_T y_z;
  real_T ab_v_re;
  real_T ab_v_im;
  real_T ab_const_mass_re;
  real_T ab_const_mass_im;
  creal_T ab_v;
  creal_T bb_const_mass;
  creal_T ab_z;
  real_T bb_v_re;
  real_T bb_v_im;
  real_T bb_const_mass_re;
  real_T bb_const_mass_im;
  creal_T bb_v;
  creal_T cb_const_mass;
  creal_T bb_z;
  real_T cb_v_re;
  real_T cb_v_im;
  real_T cb_const_mass_re;
  real_T cb_const_mass_im;
  creal_T cb_v;
  creal_T db_const_mass;
  creal_T cb_z;
  real_T db_v_re;
  real_T db_v_im;
  real_T db_const_mass_re;
  real_T db_const_mass_im;
  creal_T db_v;
  creal_T eb_const_mass;
  creal_T db_z;
  real_T eb_v_re;
  real_T eb_v_im;
  real_T eb_const_mass_re;
  real_T eb_const_mass_im;
  creal_T eb_v;
  creal_T fb_const_mass;
  creal_T eb_z;
  real_T fb_v_re;
  real_T fb_v_im;
  real_T fb_const_mass_re;
  real_T fb_const_mass_im;
  creal_T fb_v;
  creal_T gb_const_mass;
  creal_T fb_z;
  real_T gb_v_re;
  real_T gb_v_im;
  real_T gb_const_mass_re;
  real_T gb_const_mass_im;
  creal_T gb_v;
  creal_T hb_const_mass;
  creal_T gb_z;
  real_T hb_v_re;
  real_T hb_v_im;
  real_T hb_const_mass_re;
  real_T hb_const_mass_im;
  creal_T hb_v;
  creal_T ib_const_mass;
  creal_T hb_z;
  real_T ib_v_re;
  real_T ib_v_im;
  real_T ib_const_mass_re;
  real_T ib_const_mass_im;
  creal_T ib_v;
  creal_T jb_const_mass;
  creal_T ib_z;
  real_T jb_v_re;
  real_T jb_v_im;
  real_T jb_const_mass_re;
  real_T jb_const_mass_im;
  creal_T jb_v;
  creal_T kb_const_mass;
  creal_T jb_z;
  real_T kb_v_re;
  real_T kb_v_im;
  real_T kb_const_mass_re;
  real_T kb_const_mass_im;
  creal_T kb_v;
  creal_T lb_const_mass;
  creal_T kb_z;
  real_T lb_v_re;
  real_T lb_v_im;
  real_T lb_const_mass_re;
  real_T lb_const_mass_im;
  creal_T lb_v;
  creal_T mb_const_mass;
  creal_T lb_z;
  real_T mb_v_re;
  real_T mb_v_im;
  real_T mb_const_mass_re;
  real_T mb_const_mass_im;
  creal_T mb_v;
  creal_T nb_const_mass;
  creal_T mb_z;
  real_T nb_v_re;
  real_T nb_v_im;
  real_T nb_const_mass_re;
  real_T nb_const_mass_im;
  creal_T nb_v;
  creal_T ob_const_mass;
  creal_T nb_z;
  real_T ob_v_re;
  real_T ob_v_im;
  real_T ob_const_mass_re;
  real_T ob_const_mass_im;
  creal_T ob_v;
  creal_T pb_const_mass;
  creal_T ob_z;
  real_T pb_v_re;
  real_T pb_v_im;
  real_T pb_const_mass_re;
  real_T pb_const_mass_im;
  creal_T pb_v;
  creal_T qb_const_mass;
  creal_T pb_z;
  real_T qb_v_re;
  real_T qb_v_im;
  real_T qb_const_mass_re;
  real_T qb_const_mass_im;
  creal_T qb_v;
  creal_T rb_const_mass;
  creal_T qb_z;
  real_T rb_v_re;
  real_T rb_v_im;
  real_T rb_const_mass_re;
  real_T rb_const_mass_im;
  creal_T rb_v;
  creal_T sb_const_mass;
  creal_T rb_z;
  real_T sb_v_re;
  real_T sb_v_im;
  real_T sb_const_mass_re;
  real_T sb_const_mass_im;
  creal_T sb_v;
  creal_T tb_const_mass;
  creal_T sb_z;
  real_T tb_v_re;
  real_T tb_v_im;
  real_T tb_const_mass_re;
  real_T tb_const_mass_im;
  creal_T tb_v;
  creal_T ub_const_mass;
  creal_T tb_z;
  real_T ub_v_re;
  real_T ub_v_im;
  real_T ub_const_mass_re;
  real_T ub_const_mass_im;
  creal_T ub_v;
  creal_T vb_const_mass;
  creal_T ub_z;
  real_T vb_v_re;
  real_T vb_v_im;
  real_T vb_const_mass_re;
  real_T vb_const_mass_im;
  creal_T vb_v;
  creal_T wb_const_mass;
  creal_T vb_z;
  real_T wb_v_re;
  real_T wb_v_im;
  real_T wb_const_mass_re;
  real_T wb_const_mass_im;
  creal_T wb_v;
  creal_T xb_const_mass;
  creal_T wb_z;
  real_T xb_v_re;
  real_T xb_v_im;
  real_T xb_const_mass_re;
  real_T xb_const_mass_im;
  creal_T xb_z;
  creal_T xb_v;
  creal_T yb_v;
  creal_T yb_const_mass;
  creal_T yb_z;
  real_T yb_v_re;
  real_T yb_v_im;
  real_T yb_const_mass_re;
  real_T yb_const_mass_im;
  creal_T ac_z;
  creal_T ac_v;
  creal_T bc_v;
  creal_T ac_const_mass;
  creal_T bc_z;
  real_T ac_v_re;
  real_T ac_v_im;
  real_T ac_const_mass_re;
  real_T ac_const_mass_im;
  creal_T cc_z;
  creal_T cc_v;
  creal_T dc_v;
  creal_T bc_const_mass;
  creal_T dc_z;
  real_T bc_v_re;
  real_T bc_v_im;
  real_T bc_const_mass_re;
  real_T bc_const_mass_im;
  creal_T ec_z;
  creal_T ec_v;
  creal_T fc_v;
  creal_T cc_const_mass;
  creal_T fc_z;
  real_T cc_v_re;
  real_T cc_v_im;
  real_T cc_const_mass_re;
  real_T cc_const_mass_im;
  creal_T gc_z;
  creal_T gc_v;
  creal_T hc_v;
  creal_T dc_const_mass;
  creal_T hc_z;
  real_T dc_v_re;
  real_T dc_v_im;
  real_T dc_const_mass_re;
  real_T dc_const_mass_im;
  creal_T ic_z;
  creal_T ic_v;
  creal_T jc_v;
  creal_T ec_const_mass;
  creal_T jc_z;
  real_T ec_v_re;
  real_T ec_v_im;
  real_T ec_const_mass_re;
  real_T ec_const_mass_im;
  creal_T kc_z;
  creal_T kc_v;
  creal_T lc_v;
  creal_T fc_const_mass;
  creal_T lc_z;
  real_T fc_v_re;
  real_T fc_v_im;
  real_T fc_const_mass_re;
  real_T fc_const_mass_im;
  creal_T mc_z;
  creal_T mc_v;
  creal_T nc_v;
  creal_T gc_const_mass;
  creal_T nc_z;
  real_T gc_v_re;
  real_T gc_v_im;
  real_T gc_const_mass_re;
  real_T gc_const_mass_im;
  creal_T oc_z;
  creal_T oc_v;
  creal_T pc_v;
  creal_T hc_const_mass;
  creal_T pc_z;
  real_T hc_v_re;
  real_T hc_v_im;
  real_T hc_const_mass_re;
  real_T hc_const_mass_im;
  creal_T qc_z;
  creal_T qc_v;
  creal_T rc_v;
  creal_T ic_const_mass;
  creal_T rc_z;
  real_T ic_v_re;
  real_T ic_v_im;
  real_T ic_const_mass_re;
  real_T ic_const_mass_im;
  creal_T sc_z;
  creal_T sc_v;
  creal_T tc_v;
  creal_T jc_const_mass;
  creal_T tc_z;
  real_T jc_v_re;
  real_T jc_v_im;
  real_T jc_const_mass_re;
  real_T jc_const_mass_im;
  creal_T uc_z;
  creal_T uc_v;
  creal_T vc_v;
  creal_T kc_const_mass;
  creal_T vc_z;
  real_T kc_v_re;
  real_T kc_v_im;
  real_T kc_const_mass_re;
  real_T kc_const_mass_im;
  creal_T wc_z;
  creal_T wc_v;
  creal_T xc_v;
  creal_T lc_const_mass;
  creal_T xc_z;
  real_T lc_v_re;
  real_T lc_v_im;
  real_T lc_const_mass_re;
  real_T lc_const_mass_im;
  creal_T yc_z;
  creal_T yc_v;
  creal_T ad_v;
  creal_T mc_const_mass;
  creal_T ad_z;
  real_T mc_v_re;
  real_T mc_v_im;
  real_T mc_const_mass_re;
  real_T mc_const_mass_im;
  creal_T bd_z;
  creal_T bd_v;
  creal_T cd_v;
  creal_T nc_const_mass;
  creal_T cd_z;
  real_T nc_v_re;
  real_T nc_v_im;
  real_T nc_const_mass_re;
  real_T nc_const_mass_im;
  creal_T dd_z;
  creal_T dd_v;
  creal_T ed_v;
  creal_T oc_const_mass;
  creal_T ed_z;
  real_T oc_v_re;
  real_T oc_v_im;
  real_T oc_const_mass_re;
  real_T oc_const_mass_im;
  creal_T fd_z;
  creal_T fd_v;
  creal_T gd_v;
  creal_T pc_const_mass;
  creal_T gd_z;
  real_T pc_v_re;
  real_T pc_v_im;
  real_T pc_const_mass_re;
  real_T pc_const_mass_im;
  creal_T hd_z;
  creal_T hd_v;
  creal_T id_v;
  creal_T qc_const_mass;
  creal_T id_z;
  real_T qc_v_re;
  real_T qc_v_im;
  real_T qc_const_mass_re;
  real_T qc_const_mass_im;
  creal_T jd_z;
  creal_T jd_v;
  creal_T kd_v;
  creal_T rc_const_mass;
  creal_T kd_z;
  real_T rc_v_re;
  real_T rc_v_im;
  real_T rc_const_mass_re;
  real_T rc_const_mass_im;
  creal_T ld_z;
  creal_T ld_v;
  creal_T md_v;
  creal_T sc_const_mass;
  creal_T md_z;
  real_T sc_v_re;
  real_T sc_v_im;
  real_T sc_const_mass_re;
  real_T sc_const_mass_im;
  creal_T nd_z;
  creal_T nd_v;
  creal_T od_v;
  creal_T tc_const_mass;
  creal_T od_z;
  real_T tc_v_re;
  real_T tc_v_im;
  real_T tc_const_mass_re;
  real_T tc_const_mass_im;
  creal_T pd_z;
  creal_T pd_v;
  creal_T qd_v;
  creal_T uc_const_mass;
  creal_T qd_z;
  real_T uc_v_re;
  real_T uc_v_im;
  real_T uc_const_mass_re;
  real_T uc_const_mass_im;
  creal_T rd_z;
  creal_T rd_v;
  creal_T sd_v;
  creal_T vc_const_mass;
  creal_T sd_z;
  real_T vc_v_re;
  real_T vc_v_im;
  real_T vc_const_mass_re;
  real_T vc_const_mass_im;
  creal_T td_z;
  creal_T td_v;
  creal_T ud_v;
  creal_T wc_const_mass;
  creal_T ud_z;
  real_T wc_v_re;
  real_T wc_v_im;
  real_T wc_const_mass_re;
  real_T wc_const_mass_im;

  /*  Constants */
  /*  States */
  psii.re = xAndLambda_data[4];
  psii.im = 0.0;
  gam.re = xAndLambda_data[5];
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
  v.re = xAndLambda_data[3] * xAndLambda_data[3];
  v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(-const_alfamax) * 3420.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc3.re;
  ai = const_g * dc3.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  b_const_mass.re = const_mass * xAndLambda_data[3];
  b_const_mass.im = const_mass * 0.0;
  dc3 = eml_div(muDoubleScalarCos(-const_bankmax) * (const_g * const_mass +
    muDoubleScalarSin(-const_alfamax) * 3420.0), b_const_mass);
  z.re = xAndLambda_data[2] + 50.0;
  z.im = 0.0;
  v = b_mpower(z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = dc4.re * 2.3819670606660884E+18;
  ai = dc4.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      Ttrignew = ar / v_re;
    } else if (ar == 0.0) {
      Ttrignew = 0.0;
    } else {
      Ttrignew = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      Ttrignew = ai / v_im;
    } else if (ai == 0.0) {
      Ttrignew = 0.0;
    } else {
      Ttrignew = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      Ttrignew = (ar + bim * ai) / (v_re + bim * v_im);
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

      Ttrignew = (ar * b_v_re + ai * b_v_im) / brm;
    } else {
      bim = v_re / v_im;
      Ttrignew = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc7.re - const_mass_im * dc7.im;
  const_mass_im = hamiltonian * dc7.im + const_mass_im * dc7.re;
  ar = muDoubleScalarSin(-const_bankmax) * xAndLambda_data[10] * (const_g *
    const_mass + muDoubleScalarSin(-const_alfamax) * 3420.0);
  ai = muDoubleScalarSin(-const_bankmax) * 0.0 * (const_g * const_mass +
    muDoubleScalarSin(-const_alfamax) * 3420.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        b_const_mass_re = 0.5;
      } else {
        b_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        b_const_mass_im = 0.5;
      } else {
        b_const_mass_im = -0.5;
      }

      const_mass_re = (ar * b_const_mass_re + ai * b_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  *hamiltonianSave = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
    (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) * dc0.im) -
    (xAndLambda_data[9] * (const_C1_re + const_g * dc2.re) - 0.0 * (const_C1_im
    + const_g * dc2.im))) - (xAndLambda_data[11] * (const_g_re - dc3.re) - 0.0 *
                          (const_g_im - dc3.im))) + Ttrignew) + ((lamX_re *
    dc5.re - lamX_im * dc5.im) * a.re - (lamX_re * dc5.im + lamX_im * dc5.re) *
    a.im)) + ((lamY_re * dc6.re - lamY_im * dc6.im) * dc1.re - (lamY_re * dc6.im
    + lamY_im * dc6.re) * dc1.im)) + const_mass_re;

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
  b_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  b_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, b_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(-const_alfamax) * 3420.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  c_const_mass.re = const_mass * xAndLambda_data[3];
  c_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax) * (const_g * const_mass +
    muDoubleScalarSin(-const_alfamax) * 3420.0), c_const_mass);
  b_z.re = xAndLambda_data[2] + 50.0;
  b_z.im = 0.0;
  v = b_mpower(b_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * c_v_re + ai * c_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax) * xAndLambda_data[10] * (const_g *
    const_mass + muDoubleScalarSin(-const_alfamax) * 3420.0);
  ai = muDoubleScalarSin(const_bankmax) * 0.0 * (const_g * const_mass +
    muDoubleScalarSin(-const_alfamax) * 3420.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        c_const_mass_re = 0.5;
      } else {
        c_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        c_const_mass_im = 0.5;
      } else {
        c_const_mass_im = -0.5;
      }

      const_mass_re = (ar * c_const_mass_re + ai * c_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = 1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&d_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = 3.1416 / (2.0 * const_bankmax);
  b_asin(&hamiltonian);
  banktrig = -hamiltonian;
  emlrtPopRtStackR2012b(&d_emlrtRSI, emlrtRootTLSGlobal);
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
  c_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  c_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, c_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(-const_alfamax) * 3420.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  d_const_mass.re = const_mass * xAndLambda_data[3];
  d_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig)) *
                (const_g * const_mass + muDoubleScalarSin(-const_alfamax) *
                 3420.0), d_const_mass);
  c_z.re = xAndLambda_data[2] + 50.0;
  c_z.im = 0.0;
  v = b_mpower(c_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * d_v_re + ai * d_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda_data[10] * (const_g * const_mass + muDoubleScalarSin
    (-const_alfamax) * 3420.0);
  ai = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (const_g * const_mass + muDoubleScalarSin(-const_alfamax) * 3420.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        d_const_mass_re = 0.5;
      } else {
        d_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        d_const_mass_im = 0.5;
      } else {
        d_const_mass_im = -0.5;
      }

      const_mass_re = (ar * d_const_mass_re + ai * d_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&e_emlrtRSI, emlrtRootTLSGlobal);
  banktrig = 3.1416 / (2.0 * const_bankmax);
  b_asin(&banktrig);
  emlrtPopRtStackR2012b(&e_emlrtRSI, emlrtRootTLSGlobal);
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
  d_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  d_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, d_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(-const_alfamax) * 3420.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  e_const_mass.re = const_mass * xAndLambda_data[3];
  e_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig)) *
                (const_g * const_mass + muDoubleScalarSin(-const_alfamax) *
                 3420.0), e_const_mass);
  d_z.re = xAndLambda_data[2] + 50.0;
  d_z.im = 0.0;
  v = b_mpower(d_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * e_v_re + ai * e_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda_data[10] * (const_g * const_mass + muDoubleScalarSin
    (-const_alfamax) * 3420.0);
  ai = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (const_g * const_mass + muDoubleScalarSin(-const_alfamax) * 3420.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        e_const_mass_re = 0.5;
      } else {
        e_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        e_const_mass_im = 0.5;
      } else {
        e_const_mass_im = -0.5;
      }

      const_mass_re = (ar * e_const_mass_re + ai * e_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
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
  e_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  e_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, e_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax) * 3420.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  f_const_mass.re = const_mass * xAndLambda_data[3];
  f_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(-const_bankmax) * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax) * 3420.0), f_const_mass);
  e_z.re = xAndLambda_data[2] + 50.0;
  e_z.im = 0.0;
  v = b_mpower(e_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * f_v_re + ai * f_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(-const_bankmax) * xAndLambda_data[10] * (const_g *
    const_mass + muDoubleScalarSin(const_alfamax) * 3420.0);
  ai = muDoubleScalarSin(-const_bankmax) * 0.0 * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax) * 3420.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        f_const_mass_re = 0.5;
      } else {
        f_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        f_const_mass_im = 0.5;
      } else {
        f_const_mass_im = -0.5;
      }

      const_mass_re = (ar * f_const_mass_re + ai * f_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
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
  f_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  f_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, f_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax) * 3420.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  g_const_mass.re = const_mass * xAndLambda_data[3];
  g_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax) * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax) * 3420.0), g_const_mass);
  f_z.re = xAndLambda_data[2] + 50.0;
  f_z.im = 0.0;
  v = b_mpower(f_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * g_v_re + ai * g_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax) * xAndLambda_data[10] * (const_g *
    const_mass + muDoubleScalarSin(const_alfamax) * 3420.0);
  ai = muDoubleScalarSin(const_bankmax) * 0.0 * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax) * 3420.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        g_const_mass_re = 0.5;
      } else {
        g_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        g_const_mass_im = 0.5;
      } else {
        g_const_mass_im = -0.5;
      }

      const_mass_re = (ar * g_const_mass_re + ai * g_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = 1.5707963267948966;
    *alfatrigSave = 1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&f_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = 3.1416 / (2.0 * const_bankmax);
  b_asin(&hamiltonian);
  banktrig = -hamiltonian;
  emlrtPopRtStackR2012b(&f_emlrtRSI, emlrtRootTLSGlobal);
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
  g_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  g_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, g_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax) * 3420.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  h_const_mass.re = const_mass * xAndLambda_data[3];
  h_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig)) *
                (const_g * const_mass + muDoubleScalarSin(const_alfamax) *
                 3420.0), h_const_mass);
  g_z.re = xAndLambda_data[2] + 50.0;
  g_z.im = 0.0;
  v = b_mpower(g_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * h_v_re + ai * h_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda_data[10] * (const_g * const_mass + muDoubleScalarSin
    (const_alfamax) * 3420.0);
  ai = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (const_g * const_mass + muDoubleScalarSin(const_alfamax) * 3420.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        h_const_mass_re = 0.5;
      } else {
        h_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        h_const_mass_im = 0.5;
      } else {
        h_const_mass_im = -0.5;
      }

      const_mass_re = (ar * h_const_mass_re + ai * h_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = 1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&g_emlrtRSI, emlrtRootTLSGlobal);
  banktrig = 3.1416 / (2.0 * const_bankmax);
  b_asin(&banktrig);
  emlrtPopRtStackR2012b(&g_emlrtRSI, emlrtRootTLSGlobal);
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
  h_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  h_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, h_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax) * 3420.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  i_const_mass.re = const_mass * xAndLambda_data[3];
  i_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig)) *
                (const_g * const_mass + muDoubleScalarSin(const_alfamax) *
                 3420.0), i_const_mass);
  h_z.re = xAndLambda_data[2] + 50.0;
  h_z.im = 0.0;
  v = b_mpower(h_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * i_v_re + ai * i_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda_data[10] * (const_g * const_mass + muDoubleScalarSin
    (const_alfamax) * 3420.0);
  ai = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (const_g * const_mass + muDoubleScalarSin(const_alfamax) * 3420.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        i_const_mass_re = 0.5;
      } else {
        i_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        i_const_mass_im = 0.5;
      } else {
        i_const_mass_im = -0.5;
      }

      const_mass_re = (ar * i_const_mass_re + ai * i_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = 1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(-const_bankmax);
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(-const_bankmax);
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(-(2.0 * const_bankmax));
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(-(2.0 * const_bankmax));
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      hamiltonian = const_g_re / dc0.re;
      const_g_im = 0.0;
    } else if (const_g_re == 0.0) {
      hamiltonian = 0.0;
      const_g_im /= dc0.re;
    } else {
      hamiltonian = const_g_re / dc0.re;
      const_g_im /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = 0.0;
    } else if (const_g_im == 0.0) {
      hamiltonian = 0.0;
      const_g_im = -(const_g_re / dc0.im);
    } else {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = -(const_g_re / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      hamiltonian = (const_g_re + bim * const_g_im) / lamX_im;
      const_g_im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      hamiltonian = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      const_g_im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      hamiltonian = (bim * const_g_re + const_g_im) / lamX_im;
      const_g_im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -const_g_im;
  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  i_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  i_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, i_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * 3420.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  j_const_mass.re = const_mass * xAndLambda_data[3];
  j_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(-const_bankmax) * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 3420.0),
                j_const_mass);
  i_z.re = xAndLambda_data[2] + 50.0;
  i_z.im = 0.0;
  v = b_mpower(i_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * j_v_re + ai * j_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(-const_bankmax) * xAndLambda_data[10] * (const_g *
    const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) *
    3420.0);
  ai = muDoubleScalarSin(-const_bankmax) * 0.0 * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 3420.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        j_const_mass_re = 0.5;
      } else {
        j_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        j_const_mass_im = 0.5;
      } else {
        j_const_mass_im = -0.5;
      }

      const_mass_re = (ar * j_const_mass_re + ai * j_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = -1.5707963267948966;
    *alfatrigSave = alfatrig;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(const_bankmax);
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(const_bankmax);
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(2.0 * const_bankmax);
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(2.0 * const_bankmax);
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      hamiltonian = const_g_re / dc0.re;
      const_g_im = 0.0;
    } else if (const_g_re == 0.0) {
      hamiltonian = 0.0;
      const_g_im /= dc0.re;
    } else {
      hamiltonian = const_g_re / dc0.re;
      const_g_im /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = 0.0;
    } else if (const_g_im == 0.0) {
      hamiltonian = 0.0;
      const_g_im = -(const_g_re / dc0.im);
    } else {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = -(const_g_re / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      hamiltonian = (const_g_re + bim * const_g_im) / lamX_im;
      const_g_im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      hamiltonian = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      const_g_im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      hamiltonian = (bim * const_g_re + const_g_im) / lamX_im;
      const_g_im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -const_g_im;
  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  j_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  j_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, j_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * 3420.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  k_const_mass.re = const_mass * xAndLambda_data[3];
  k_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax) * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 3420.0),
                k_const_mass);
  j_z.re = xAndLambda_data[2] + 50.0;
  j_z.im = 0.0;
  v = b_mpower(j_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * k_v_re + ai * k_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax) * xAndLambda_data[10] * (const_g *
    const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) *
    3420.0);
  ai = muDoubleScalarSin(const_bankmax) * 0.0 * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 3420.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        k_const_mass_re = 0.5;
      } else {
        k_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        k_const_mass_im = 0.5;
      } else {
        k_const_mass_im = -0.5;
      }

      const_mass_re = (ar * k_const_mass_re + ai * k_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = 1.5707963267948966;
    *alfatrigSave = alfatrig;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&h_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = 3.1416 / (2.0 * const_bankmax);
  b_asin(&hamiltonian);
  banktrig = -hamiltonian;
  emlrtPopRtStackR2012b(&h_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(-hamiltonian) || muDoubleScalarIsInf(-hamiltonian)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(2.0 * const_bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(2.0 * const_bankmax * muDoubleScalarSin
    (banktrig));
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      hamiltonian = const_g_re / dc0.re;
      const_g_im = 0.0;
    } else if (const_g_re == 0.0) {
      hamiltonian = 0.0;
      const_g_im /= dc0.re;
    } else {
      hamiltonian = const_g_re / dc0.re;
      const_g_im /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = 0.0;
    } else if (const_g_im == 0.0) {
      hamiltonian = 0.0;
      const_g_im = -(const_g_re / dc0.im);
    } else {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = -(const_g_re / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      hamiltonian = (const_g_re + bim * const_g_im) / lamX_im;
      const_g_im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      hamiltonian = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      const_g_im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      hamiltonian = (bim * const_g_re + const_g_im) / lamX_im;
      const_g_im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -const_g_im;
  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  k_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  k_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, k_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * 3420.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  l_const_mass.re = const_mass * xAndLambda_data[3];
  l_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig)) *
                (const_g * const_mass + muDoubleScalarSin(const_alfamax *
    muDoubleScalarSin(alfatrig)) * 3420.0), l_const_mass);
  k_z.re = xAndLambda_data[2] + 50.0;
  k_z.im = 0.0;
  v = b_mpower(k_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * l_v_re + ai * l_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda_data[10] * (const_g * const_mass + muDoubleScalarSin
    (const_alfamax * muDoubleScalarSin(alfatrig)) * 3420.0);
  ai = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (const_g * const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin
      (alfatrig)) * 3420.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        l_const_mass_re = 0.5;
      } else {
        l_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        l_const_mass_im = 0.5;
      } else {
        l_const_mass_im = -0.5;
      }

      const_mass_re = (ar * l_const_mass_re + ai * l_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&i_emlrtRSI, emlrtRootTLSGlobal);
  banktrig = 3.1416 / (2.0 * const_bankmax);
  b_asin(&banktrig);
  emlrtPopRtStackR2012b(&i_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(banktrig) || muDoubleScalarIsInf(banktrig)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(2.0 * const_bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(2.0 * const_bankmax * muDoubleScalarSin
    (banktrig));
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      hamiltonian = const_g_re / dc0.re;
      const_g_im = 0.0;
    } else if (const_g_re == 0.0) {
      hamiltonian = 0.0;
      const_g_im /= dc0.re;
    } else {
      hamiltonian = const_g_re / dc0.re;
      const_g_im /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = 0.0;
    } else if (const_g_im == 0.0) {
      hamiltonian = 0.0;
      const_g_im = -(const_g_re / dc0.im);
    } else {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = -(const_g_re / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      hamiltonian = (const_g_re + bim * const_g_im) / lamX_im;
      const_g_im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      hamiltonian = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      const_g_im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      hamiltonian = (bim * const_g_re + const_g_im) / lamX_im;
      const_g_im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -const_g_im;
  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  l_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  l_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, l_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * 3420.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  m_const_mass.re = const_mass * xAndLambda_data[3];
  m_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig)) *
                (const_g * const_mass + muDoubleScalarSin(const_alfamax *
    muDoubleScalarSin(alfatrig)) * 3420.0), m_const_mass);
  l_z.re = xAndLambda_data[2] + 50.0;
  l_z.im = 0.0;
  v = b_mpower(l_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * m_v_re + ai * m_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda_data[10] * (const_g * const_mass + muDoubleScalarSin
    (const_alfamax * muDoubleScalarSin(alfatrig)) * 3420.0);
  ai = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (const_g * const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin
      (alfatrig)) * 3420.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        m_const_mass_re = 0.5;
      } else {
        m_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        m_const_mass_im = 0.5;
      } else {
        m_const_mass_im = -0.5;
      }

      const_mass_re = (ar * m_const_mass_re + ai * m_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(-const_bankmax);
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(-const_bankmax);
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(-(2.0 * const_bankmax));
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(-(2.0 * const_bankmax));
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      hamiltonian = const_g_re / dc0.re;
      const_g_im = 0.0;
    } else if (const_g_re == 0.0) {
      hamiltonian = 0.0;
      const_g_im /= dc0.re;
    } else {
      hamiltonian = const_g_re / dc0.re;
      const_g_im /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = 0.0;
    } else if (const_g_im == 0.0) {
      hamiltonian = 0.0;
      const_g_im = -(const_g_re / dc0.im);
    } else {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = -(const_g_re / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      hamiltonian = (const_g_re + bim * const_g_im) / lamX_im;
      const_g_im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      hamiltonian = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      const_g_im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      hamiltonian = (bim * const_g_re + const_g_im) / lamX_im;
      const_g_im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -const_g_im;
  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  m_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  m_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, m_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * 3420.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  n_const_mass.re = const_mass * xAndLambda_data[3];
  n_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(-const_bankmax) * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 3420.0),
                n_const_mass);
  m_z.re = xAndLambda_data[2] + 50.0;
  m_z.im = 0.0;
  v = b_mpower(m_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * n_v_re + ai * n_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(-const_bankmax) * xAndLambda_data[10] * (const_g *
    const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) *
    3420.0);
  ai = muDoubleScalarSin(-const_bankmax) * 0.0 * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 3420.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        n_const_mass_re = 0.5;
      } else {
        n_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        n_const_mass_im = 0.5;
      } else {
        n_const_mass_im = -0.5;
      }

      const_mass_re = (ar * n_const_mass_re + ai * n_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = -1.5707963267948966;
    *alfatrigSave = alfatrig;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(const_bankmax);
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(const_bankmax);
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(2.0 * const_bankmax);
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(2.0 * const_bankmax);
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      hamiltonian = const_g_re / dc0.re;
      const_g_im = 0.0;
    } else if (const_g_re == 0.0) {
      hamiltonian = 0.0;
      const_g_im /= dc0.re;
    } else {
      hamiltonian = const_g_re / dc0.re;
      const_g_im /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = 0.0;
    } else if (const_g_im == 0.0) {
      hamiltonian = 0.0;
      const_g_im = -(const_g_re / dc0.im);
    } else {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = -(const_g_re / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      hamiltonian = (const_g_re + bim * const_g_im) / lamX_im;
      const_g_im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      hamiltonian = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      const_g_im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      hamiltonian = (bim * const_g_re + const_g_im) / lamX_im;
      const_g_im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -const_g_im;
  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  n_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  n_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, n_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * 3420.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  o_const_mass.re = const_mass * xAndLambda_data[3];
  o_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax) * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 3420.0),
                o_const_mass);
  n_z.re = xAndLambda_data[2] + 50.0;
  n_z.im = 0.0;
  v = b_mpower(n_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * o_v_re + ai * o_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax) * xAndLambda_data[10] * (const_g *
    const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) *
    3420.0);
  ai = muDoubleScalarSin(const_bankmax) * 0.0 * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 3420.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        o_const_mass_re = 0.5;
      } else {
        o_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        o_const_mass_im = 0.5;
      } else {
        o_const_mass_im = -0.5;
      }

      const_mass_re = (ar * o_const_mass_re + ai * o_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = 1.5707963267948966;
    *alfatrigSave = alfatrig;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&j_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = 3.1416 / (2.0 * const_bankmax);
  b_asin(&hamiltonian);
  banktrig = -hamiltonian;
  emlrtPopRtStackR2012b(&j_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(-hamiltonian) || muDoubleScalarIsInf(-hamiltonian)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(2.0 * const_bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(2.0 * const_bankmax * muDoubleScalarSin
    (banktrig));
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      hamiltonian = const_g_re / dc0.re;
      const_g_im = 0.0;
    } else if (const_g_re == 0.0) {
      hamiltonian = 0.0;
      const_g_im /= dc0.re;
    } else {
      hamiltonian = const_g_re / dc0.re;
      const_g_im /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = 0.0;
    } else if (const_g_im == 0.0) {
      hamiltonian = 0.0;
      const_g_im = -(const_g_re / dc0.im);
    } else {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = -(const_g_re / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      hamiltonian = (const_g_re + bim * const_g_im) / lamX_im;
      const_g_im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      hamiltonian = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      const_g_im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      hamiltonian = (bim * const_g_re + const_g_im) / lamX_im;
      const_g_im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -const_g_im;
  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  o_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  o_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, o_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * 3420.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  p_const_mass.re = const_mass * xAndLambda_data[3];
  p_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig)) *
                (const_g * const_mass + muDoubleScalarSin(const_alfamax *
    muDoubleScalarSin(alfatrig)) * 3420.0), p_const_mass);
  o_z.re = xAndLambda_data[2] + 50.0;
  o_z.im = 0.0;
  v = b_mpower(o_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * p_v_re + ai * p_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda_data[10] * (const_g * const_mass + muDoubleScalarSin
    (const_alfamax * muDoubleScalarSin(alfatrig)) * 3420.0);
  ai = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (const_g * const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin
      (alfatrig)) * 3420.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        p_const_mass_re = 0.5;
      } else {
        p_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        p_const_mass_im = 0.5;
      } else {
        p_const_mass_im = -0.5;
      }

      const_mass_re = (ar * p_const_mass_re + ai * p_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&k_emlrtRSI, emlrtRootTLSGlobal);
  banktrig = 3.1416 / (2.0 * const_bankmax);
  b_asin(&banktrig);
  emlrtPopRtStackR2012b(&k_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(banktrig) || muDoubleScalarIsInf(banktrig)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(2.0 * const_bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(2.0 * const_bankmax * muDoubleScalarSin
    (banktrig));
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      hamiltonian = const_g_re / dc0.re;
      const_g_im = 0.0;
    } else if (const_g_re == 0.0) {
      hamiltonian = 0.0;
      const_g_im /= dc0.re;
    } else {
      hamiltonian = const_g_re / dc0.re;
      const_g_im /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = 0.0;
    } else if (const_g_im == 0.0) {
      hamiltonian = 0.0;
      const_g_im = -(const_g_re / dc0.im);
    } else {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = -(const_g_re / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      hamiltonian = (const_g_re + bim * const_g_im) / lamX_im;
      const_g_im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      hamiltonian = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      const_g_im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      hamiltonian = (bim * const_g_re + const_g_im) / lamX_im;
      const_g_im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -const_g_im;
  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  p_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  p_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, p_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * 3420.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  q_const_mass.re = const_mass * xAndLambda_data[3];
  q_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig)) *
                (const_g * const_mass + muDoubleScalarSin(const_alfamax *
    muDoubleScalarSin(alfatrig)) * 3420.0), q_const_mass);
  p_z.re = xAndLambda_data[2] + 50.0;
  p_z.im = 0.0;
  v = b_mpower(p_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * q_v_re + ai * q_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda_data[10] * (const_g * const_mass + muDoubleScalarSin
    (const_alfamax * muDoubleScalarSin(alfatrig)) * 3420.0);
  ai = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (const_g * const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin
      (alfatrig)) * 3420.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        q_const_mass_re = 0.5;
      } else {
        q_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        q_const_mass_im = 0.5;
      } else {
        q_const_mass_im = -0.5;
      }

      const_mass_re = (ar * q_const_mass_re + ai * q_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(-const_bankmax);
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(-const_bankmax);
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(-(2.0 * const_bankmax));
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(-(2.0 * const_bankmax));
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  Ttrignew = dc0.re;
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      dc0.re = const_g_re / dc0.re;
      dc0.im = 0.0;
    } else if (const_g_re == 0.0) {
      dc0.re = 0.0;
      dc0.im = const_g_im / Ttrignew;
    } else {
      dc0.re = const_g_re / dc0.re;
      dc0.im = const_g_im / Ttrignew;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      dc0.re = const_g_im / dc0.im;
      dc0.im = 0.0;
    } else if (const_g_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(const_g_re / const_C1_im);
    } else {
      dc0.re = const_g_im / dc0.im;
      dc0.im = -(const_g_re / const_C1_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      dc0.re = (const_g_re + bim * const_g_im) / lamX_im;
      dc0.im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      dc0.re = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      dc0.im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      dc0.re = (bim * const_g_re + const_g_im) / lamX_im;
      dc0.im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  q_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  q_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, q_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * 3420.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  r_const_mass.re = const_mass * xAndLambda_data[3];
  r_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(-const_bankmax) * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 3420.0),
                r_const_mass);
  q_z.re = xAndLambda_data[2] + 50.0;
  q_z.im = 0.0;
  v = b_mpower(q_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * r_v_re + ai * r_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(-const_bankmax) * xAndLambda_data[10] * (const_g *
    const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) *
    3420.0);
  ai = muDoubleScalarSin(-const_bankmax) * 0.0 * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 3420.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        r_const_mass_re = 0.5;
      } else {
        r_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        r_const_mass_im = 0.5;
      } else {
        r_const_mass_im = -0.5;
      }

      const_mass_re = (ar * r_const_mass_re + ai * r_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = -1.5707963267948966;
    *alfatrigSave = alfatrig;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(const_bankmax);
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(const_bankmax);
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(2.0 * const_bankmax);
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(2.0 * const_bankmax);
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  Ttrignew = dc0.re;
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      dc0.re = const_g_re / dc0.re;
      dc0.im = 0.0;
    } else if (const_g_re == 0.0) {
      dc0.re = 0.0;
      dc0.im = const_g_im / Ttrignew;
    } else {
      dc0.re = const_g_re / dc0.re;
      dc0.im = const_g_im / Ttrignew;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      dc0.re = const_g_im / dc0.im;
      dc0.im = 0.0;
    } else if (const_g_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(const_g_re / const_C1_im);
    } else {
      dc0.re = const_g_im / dc0.im;
      dc0.im = -(const_g_re / const_C1_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      dc0.re = (const_g_re + bim * const_g_im) / lamX_im;
      dc0.im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      dc0.re = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      dc0.im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      dc0.re = (bim * const_g_re + const_g_im) / lamX_im;
      dc0.im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  r_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  r_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, r_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * 3420.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  s_const_mass.re = const_mass * xAndLambda_data[3];
  s_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax) * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 3420.0),
                s_const_mass);
  r_z.re = xAndLambda_data[2] + 50.0;
  r_z.im = 0.0;
  v = b_mpower(r_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * s_v_re + ai * s_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax) * xAndLambda_data[10] * (const_g *
    const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) *
    3420.0);
  ai = muDoubleScalarSin(const_bankmax) * 0.0 * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 3420.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        s_const_mass_re = 0.5;
      } else {
        s_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        s_const_mass_im = 0.5;
      } else {
        s_const_mass_im = -0.5;
      }

      const_mass_re = (ar * s_const_mass_re + ai * s_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = 1.5707963267948966;
    *alfatrigSave = alfatrig;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&l_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = 3.1416 / (2.0 * const_bankmax);
  b_asin(&hamiltonian);
  banktrig = -hamiltonian;
  emlrtPopRtStackR2012b(&l_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(-hamiltonian) || muDoubleScalarIsInf(-hamiltonian)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(2.0 * const_bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(2.0 * const_bankmax * muDoubleScalarSin
    (banktrig));
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  Ttrignew = dc0.re;
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      dc0.re = const_g_re / dc0.re;
      dc0.im = 0.0;
    } else if (const_g_re == 0.0) {
      dc0.re = 0.0;
      dc0.im = const_g_im / Ttrignew;
    } else {
      dc0.re = const_g_re / dc0.re;
      dc0.im = const_g_im / Ttrignew;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      dc0.re = const_g_im / dc0.im;
      dc0.im = 0.0;
    } else if (const_g_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(const_g_re / const_C1_im);
    } else {
      dc0.re = const_g_im / dc0.im;
      dc0.im = -(const_g_re / const_C1_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      dc0.re = (const_g_re + bim * const_g_im) / lamX_im;
      dc0.im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      dc0.re = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      dc0.im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      dc0.re = (bim * const_g_re + const_g_im) / lamX_im;
      dc0.im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  s_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  s_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, s_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * 3420.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  t_const_mass.re = const_mass * xAndLambda_data[3];
  t_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig)) *
                (const_g * const_mass + muDoubleScalarSin(const_alfamax *
    muDoubleScalarSin(alfatrig)) * 3420.0), t_const_mass);
  s_z.re = xAndLambda_data[2] + 50.0;
  s_z.im = 0.0;
  v = b_mpower(s_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * t_v_re + ai * t_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda_data[10] * (const_g * const_mass + muDoubleScalarSin
    (const_alfamax * muDoubleScalarSin(alfatrig)) * 3420.0);
  ai = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (const_g * const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin
      (alfatrig)) * 3420.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        t_const_mass_re = 0.5;
      } else {
        t_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        t_const_mass_im = 0.5;
      } else {
        t_const_mass_im = -0.5;
      }

      const_mass_re = (ar * t_const_mass_re + ai * t_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&m_emlrtRSI, emlrtRootTLSGlobal);
  banktrig = 3.1416 / (2.0 * const_bankmax);
  b_asin(&banktrig);
  emlrtPopRtStackR2012b(&m_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(banktrig) || muDoubleScalarIsInf(banktrig)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(2.0 * const_bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(2.0 * const_bankmax * muDoubleScalarSin
    (banktrig));
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  Ttrignew = dc0.re;
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      dc0.re = const_g_re / dc0.re;
      dc0.im = 0.0;
    } else if (const_g_re == 0.0) {
      dc0.re = 0.0;
      dc0.im = const_g_im / Ttrignew;
    } else {
      dc0.re = const_g_re / dc0.re;
      dc0.im = const_g_im / Ttrignew;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      dc0.re = const_g_im / dc0.im;
      dc0.im = 0.0;
    } else if (const_g_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(const_g_re / const_C1_im);
    } else {
      dc0.re = const_g_im / dc0.im;
      dc0.im = -(const_g_re / const_C1_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      dc0.re = (const_g_re + bim * const_g_im) / lamX_im;
      dc0.im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      dc0.re = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      dc0.im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      dc0.re = (bim * const_g_re + const_g_im) / lamX_im;
      dc0.im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  t_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  t_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, t_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * 3420.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  u_const_mass.re = const_mass * xAndLambda_data[3];
  u_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig)) *
                (const_g * const_mass + muDoubleScalarSin(const_alfamax *
    muDoubleScalarSin(alfatrig)) * 3420.0), u_const_mass);
  t_z.re = xAndLambda_data[2] + 50.0;
  t_z.im = 0.0;
  v = b_mpower(t_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * u_v_re + ai * u_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda_data[10] * (const_g * const_mass + muDoubleScalarSin
    (const_alfamax * muDoubleScalarSin(alfatrig)) * 3420.0);
  ai = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (const_g * const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin
      (alfatrig)) * 3420.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        u_const_mass_re = 0.5;
      } else {
        u_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        u_const_mass_im = 0.5;
      } else {
        u_const_mass_im = -0.5;
      }

      const_mass_re = (ar * u_const_mass_re + ai * u_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(-const_bankmax);
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(-const_bankmax);
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(-(2.0 * const_bankmax));
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(-(2.0 * const_bankmax));
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  Ttrignew = dc0.re;
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      dc0.re = const_g_re / dc0.re;
      dc0.im = 0.0;
    } else if (const_g_re == 0.0) {
      dc0.re = 0.0;
      dc0.im = const_g_im / Ttrignew;
    } else {
      dc0.re = const_g_re / dc0.re;
      dc0.im = const_g_im / Ttrignew;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      dc0.re = const_g_im / dc0.im;
      dc0.im = 0.0;
    } else if (const_g_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(const_g_re / const_C1_im);
    } else {
      dc0.re = const_g_im / dc0.im;
      dc0.im = -(const_g_re / const_C1_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      dc0.re = (const_g_re + bim * const_g_im) / lamX_im;
      dc0.im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      dc0.re = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      dc0.im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      dc0.re = (bim * const_g_re + const_g_im) / lamX_im;
      dc0.im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  u_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  u_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, u_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * 3420.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  v_const_mass.re = const_mass * xAndLambda_data[3];
  v_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(-const_bankmax) * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 3420.0),
                v_const_mass);
  u_z.re = xAndLambda_data[2] + 50.0;
  u_z.im = 0.0;
  v = b_mpower(u_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * v_v_re + ai * v_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(-const_bankmax) * xAndLambda_data[10] * (const_g *
    const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) *
    3420.0);
  ai = muDoubleScalarSin(-const_bankmax) * 0.0 * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 3420.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        v_const_mass_re = 0.5;
      } else {
        v_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        v_const_mass_im = 0.5;
      } else {
        v_const_mass_im = -0.5;
      }

      const_mass_re = (ar * v_const_mass_re + ai * v_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = -1.5707963267948966;
    *alfatrigSave = alfatrig;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(const_bankmax);
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(const_bankmax);
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(2.0 * const_bankmax);
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(2.0 * const_bankmax);
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  Ttrignew = dc0.re;
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      dc0.re = const_g_re / dc0.re;
      dc0.im = 0.0;
    } else if (const_g_re == 0.0) {
      dc0.re = 0.0;
      dc0.im = const_g_im / Ttrignew;
    } else {
      dc0.re = const_g_re / dc0.re;
      dc0.im = const_g_im / Ttrignew;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      dc0.re = const_g_im / dc0.im;
      dc0.im = 0.0;
    } else if (const_g_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(const_g_re / const_C1_im);
    } else {
      dc0.re = const_g_im / dc0.im;
      dc0.im = -(const_g_re / const_C1_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      dc0.re = (const_g_re + bim * const_g_im) / lamX_im;
      dc0.im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      dc0.re = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      dc0.im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      dc0.re = (bim * const_g_re + const_g_im) / lamX_im;
      dc0.im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  v_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  v_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, v_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * 3420.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  w_const_mass.re = const_mass * xAndLambda_data[3];
  w_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax) * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 3420.0),
                w_const_mass);
  v_z.re = xAndLambda_data[2] + 50.0;
  v_z.im = 0.0;
  v = b_mpower(v_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * w_v_re + ai * w_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax) * xAndLambda_data[10] * (const_g *
    const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) *
    3420.0);
  ai = muDoubleScalarSin(const_bankmax) * 0.0 * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 3420.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        w_const_mass_re = 0.5;
      } else {
        w_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        w_const_mass_im = 0.5;
      } else {
        w_const_mass_im = -0.5;
      }

      const_mass_re = (ar * w_const_mass_re + ai * w_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = 1.5707963267948966;
    *alfatrigSave = alfatrig;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&n_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = 3.1416 / (2.0 * const_bankmax);
  b_asin(&hamiltonian);
  banktrig = -hamiltonian;
  emlrtPopRtStackR2012b(&n_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(-hamiltonian) || muDoubleScalarIsInf(-hamiltonian)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(2.0 * const_bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(2.0 * const_bankmax * muDoubleScalarSin
    (banktrig));
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  Ttrignew = dc0.re;
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      dc0.re = const_g_re / dc0.re;
      dc0.im = 0.0;
    } else if (const_g_re == 0.0) {
      dc0.re = 0.0;
      dc0.im = const_g_im / Ttrignew;
    } else {
      dc0.re = const_g_re / dc0.re;
      dc0.im = const_g_im / Ttrignew;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      dc0.re = const_g_im / dc0.im;
      dc0.im = 0.0;
    } else if (const_g_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(const_g_re / const_C1_im);
    } else {
      dc0.re = const_g_im / dc0.im;
      dc0.im = -(const_g_re / const_C1_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      dc0.re = (const_g_re + bim * const_g_im) / lamX_im;
      dc0.im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      dc0.re = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      dc0.im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      dc0.re = (bim * const_g_re + const_g_im) / lamX_im;
      dc0.im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  w_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  w_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, w_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * 3420.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  x_const_mass.re = const_mass * xAndLambda_data[3];
  x_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig)) *
                (const_g * const_mass + muDoubleScalarSin(const_alfamax *
    muDoubleScalarSin(alfatrig)) * 3420.0), x_const_mass);
  w_z.re = xAndLambda_data[2] + 50.0;
  w_z.im = 0.0;
  v = b_mpower(w_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * x_v_re + ai * x_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda_data[10] * (const_g * const_mass + muDoubleScalarSin
    (const_alfamax * muDoubleScalarSin(alfatrig)) * 3420.0);
  ai = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (const_g * const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin
      (alfatrig)) * 3420.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        x_const_mass_re = 0.5;
      } else {
        x_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        x_const_mass_im = 0.5;
      } else {
        x_const_mass_im = -0.5;
      }

      const_mass_re = (ar * x_const_mass_re + ai * x_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&o_emlrtRSI, emlrtRootTLSGlobal);
  banktrig = 3.1416 / (2.0 * const_bankmax);
  b_asin(&banktrig);
  emlrtPopRtStackR2012b(&o_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(banktrig) || muDoubleScalarIsInf(banktrig)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(2.0 * const_bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(2.0 * const_bankmax * muDoubleScalarSin
    (banktrig));
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  Ttrignew = dc0.re;
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      dc0.re = const_g_re / dc0.re;
      dc0.im = 0.0;
    } else if (const_g_re == 0.0) {
      dc0.re = 0.0;
      dc0.im = const_g_im / Ttrignew;
    } else {
      dc0.re = const_g_re / dc0.re;
      dc0.im = const_g_im / Ttrignew;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      dc0.re = const_g_im / dc0.im;
      dc0.im = 0.0;
    } else if (const_g_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(const_g_re / const_C1_im);
    } else {
      dc0.re = const_g_im / dc0.im;
      dc0.im = -(const_g_re / const_C1_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      dc0.re = (const_g_re + bim * const_g_im) / lamX_im;
      dc0.im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      dc0.re = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      dc0.im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      dc0.re = (bim * const_g_re + const_g_im) / lamX_im;
      dc0.im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  x_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  x_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, x_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * 3420.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  y_const_mass.re = const_mass * xAndLambda_data[3];
  y_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig)) *
                (const_g * const_mass + muDoubleScalarSin(const_alfamax *
    muDoubleScalarSin(alfatrig)) * 3420.0), y_const_mass);
  x_z.re = xAndLambda_data[2] + 50.0;
  x_z.im = 0.0;
  v = b_mpower(x_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 2.3819670606660884E+18;
  ai = a.im * 2.3819670606660884E+18;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * y_v_re + ai * y_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda_data[10] * (const_g * const_mass + muDoubleScalarSin
    (const_alfamax * muDoubleScalarSin(alfatrig)) * 3420.0);
  ai = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (const_g * const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin
      (alfatrig)) * 3420.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        y_const_mass_re = 0.5;
      } else {
        y_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        y_const_mass_im = 0.5;
      } else {
        y_const_mass_im = -0.5;
      }

      const_mass_re = (ar * y_const_mass_re + ai * y_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
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
  y_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  y_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, y_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(-const_alfamax) * 300.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  ab_const_mass.re = const_mass * xAndLambda_data[3];
  ab_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(-const_bankmax) * (const_g * const_mass +
    muDoubleScalarSin(-const_alfamax) * 300.0), ab_const_mass);
  y_z.re = xAndLambda_data[2] + 50.0;
  y_z.im = 0.0;
  v = b_mpower(y_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * ab_v_re + ai * ab_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(-const_bankmax) * xAndLambda_data[10] * (const_g *
    const_mass + muDoubleScalarSin(-const_alfamax) * 300.0);
  ai = muDoubleScalarSin(-const_bankmax) * 0.0 * (const_g * const_mass +
    muDoubleScalarSin(-const_alfamax) * 300.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        ab_const_mass_re = 0.5;
      } else {
        ab_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        ab_const_mass_im = 0.5;
      } else {
        ab_const_mass_im = -0.5;
      }

      const_mass_re = (ar * ab_const_mass_re + ai * ab_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
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
  ab_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  ab_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, ab_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(-const_alfamax) * 300.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  bb_const_mass.re = const_mass * xAndLambda_data[3];
  bb_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax) * (const_g * const_mass +
    muDoubleScalarSin(-const_alfamax) * 300.0), bb_const_mass);
  ab_z.re = xAndLambda_data[2] + 50.0;
  ab_z.im = 0.0;
  v = b_mpower(ab_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * bb_v_re + ai * bb_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax) * xAndLambda_data[10] * (const_g *
    const_mass + muDoubleScalarSin(-const_alfamax) * 300.0);
  ai = muDoubleScalarSin(const_bankmax) * 0.0 * (const_g * const_mass +
    muDoubleScalarSin(-const_alfamax) * 300.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        bb_const_mass_re = 0.5;
      } else {
        bb_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        bb_const_mass_im = 0.5;
      } else {
        bb_const_mass_im = -0.5;
      }

      const_mass_re = (ar * bb_const_mass_re + ai * bb_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = 1.5707963267948966;
    *alfatrigSave = -1.5707963267948966;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&p_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = 3.1416 / (2.0 * const_bankmax);
  b_asin(&hamiltonian);
  banktrig = -hamiltonian;
  emlrtPopRtStackR2012b(&p_emlrtRSI, emlrtRootTLSGlobal);
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
  bb_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  bb_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, bb_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(-const_alfamax) * 300.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  cb_const_mass.re = const_mass * xAndLambda_data[3];
  cb_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig)) *
                (const_g * const_mass + muDoubleScalarSin(-const_alfamax) *
                 300.0), cb_const_mass);
  bb_z.re = xAndLambda_data[2] + 50.0;
  bb_z.im = 0.0;
  v = b_mpower(bb_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * cb_v_re + ai * cb_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda_data[10] * (const_g * const_mass + muDoubleScalarSin
    (-const_alfamax) * 300.0);
  ai = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (const_g * const_mass + muDoubleScalarSin(-const_alfamax) * 300.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        cb_const_mass_re = 0.5;
      } else {
        cb_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        cb_const_mass_im = 0.5;
      } else {
        cb_const_mass_im = -0.5;
      }

      const_mass_re = (ar * cb_const_mass_re + ai * cb_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = -1.5707963267948966;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&q_emlrtRSI, emlrtRootTLSGlobal);
  banktrig = 3.1416 / (2.0 * const_bankmax);
  b_asin(&banktrig);
  emlrtPopRtStackR2012b(&q_emlrtRSI, emlrtRootTLSGlobal);
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
  cb_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  cb_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, cb_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(-const_alfamax) * 300.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  db_const_mass.re = const_mass * xAndLambda_data[3];
  db_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig)) *
                (const_g * const_mass + muDoubleScalarSin(-const_alfamax) *
                 300.0), db_const_mass);
  cb_z.re = xAndLambda_data[2] + 50.0;
  cb_z.im = 0.0;
  v = b_mpower(cb_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * db_v_re + ai * db_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda_data[10] * (const_g * const_mass + muDoubleScalarSin
    (-const_alfamax) * 300.0);
  ai = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (const_g * const_mass + muDoubleScalarSin(-const_alfamax) * 300.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        db_const_mass_re = 0.5;
      } else {
        db_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        db_const_mass_im = 0.5;
      } else {
        db_const_mass_im = -0.5;
      }

      const_mass_re = (ar * db_const_mass_re + ai * db_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
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
  db_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  db_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, db_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax) * 300.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  eb_const_mass.re = const_mass * xAndLambda_data[3];
  eb_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(-const_bankmax) * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax) * 300.0), eb_const_mass);
  db_z.re = xAndLambda_data[2] + 50.0;
  db_z.im = 0.0;
  v = b_mpower(db_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * eb_v_re + ai * eb_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(-const_bankmax) * xAndLambda_data[10] * (const_g *
    const_mass + muDoubleScalarSin(const_alfamax) * 300.0);
  ai = muDoubleScalarSin(-const_bankmax) * 0.0 * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax) * 300.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        eb_const_mass_re = 0.5;
      } else {
        eb_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        eb_const_mass_im = 0.5;
      } else {
        eb_const_mass_im = -0.5;
      }

      const_mass_re = (ar * eb_const_mass_re + ai * eb_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
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
  eb_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  eb_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, eb_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax) * 300.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  fb_const_mass.re = const_mass * xAndLambda_data[3];
  fb_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax) * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax) * 300.0), fb_const_mass);
  eb_z.re = xAndLambda_data[2] + 50.0;
  eb_z.im = 0.0;
  v = b_mpower(eb_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * fb_v_re + ai * fb_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax) * xAndLambda_data[10] * (const_g *
    const_mass + muDoubleScalarSin(const_alfamax) * 300.0);
  ai = muDoubleScalarSin(const_bankmax) * 0.0 * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax) * 300.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        fb_const_mass_re = 0.5;
      } else {
        fb_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        fb_const_mass_im = 0.5;
      } else {
        fb_const_mass_im = -0.5;
      }

      const_mass_re = (ar * fb_const_mass_re + ai * fb_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = 1.5707963267948966;
    *alfatrigSave = 1.5707963267948966;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&r_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = 3.1416 / (2.0 * const_bankmax);
  b_asin(&hamiltonian);
  banktrig = -hamiltonian;
  emlrtPopRtStackR2012b(&r_emlrtRSI, emlrtRootTLSGlobal);
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
  fb_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  fb_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, fb_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax) * 300.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  gb_const_mass.re = const_mass * xAndLambda_data[3];
  gb_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig)) *
                (const_g * const_mass + muDoubleScalarSin(const_alfamax) * 300.0),
                gb_const_mass);
  fb_z.re = xAndLambda_data[2] + 50.0;
  fb_z.im = 0.0;
  v = b_mpower(fb_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * gb_v_re + ai * gb_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda_data[10] * (const_g * const_mass + muDoubleScalarSin
    (const_alfamax) * 300.0);
  ai = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (const_g * const_mass + muDoubleScalarSin(const_alfamax) * 300.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        gb_const_mass_re = 0.5;
      } else {
        gb_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        gb_const_mass_im = 0.5;
      } else {
        gb_const_mass_im = -0.5;
      }

      const_mass_re = (ar * gb_const_mass_re + ai * gb_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = 1.5707963267948966;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&s_emlrtRSI, emlrtRootTLSGlobal);
  banktrig = 3.1416 / (2.0 * const_bankmax);
  b_asin(&banktrig);
  emlrtPopRtStackR2012b(&s_emlrtRSI, emlrtRootTLSGlobal);
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
  gb_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  gb_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, gb_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax) * 300.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  hb_const_mass.re = const_mass * xAndLambda_data[3];
  hb_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig)) *
                (const_g * const_mass + muDoubleScalarSin(const_alfamax) * 300.0),
                hb_const_mass);
  gb_z.re = xAndLambda_data[2] + 50.0;
  gb_z.im = 0.0;
  v = b_mpower(gb_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * hb_v_re + ai * hb_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda_data[10] * (const_g * const_mass + muDoubleScalarSin
    (const_alfamax) * 300.0);
  ai = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (const_g * const_mass + muDoubleScalarSin(const_alfamax) * 300.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        hb_const_mass_re = 0.5;
      } else {
        hb_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        hb_const_mass_im = 0.5;
      } else {
        hb_const_mass_im = -0.5;
      }

      const_mass_re = (ar * hb_const_mass_re + ai * hb_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = 1.5707963267948966;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(-const_bankmax);
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(-const_bankmax);
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(-(2.0 * const_bankmax));
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(-(2.0 * const_bankmax));
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      hamiltonian = const_g_re / dc0.re;
      const_g_im = 0.0;
    } else if (const_g_re == 0.0) {
      hamiltonian = 0.0;
      const_g_im /= dc0.re;
    } else {
      hamiltonian = const_g_re / dc0.re;
      const_g_im /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = 0.0;
    } else if (const_g_im == 0.0) {
      hamiltonian = 0.0;
      const_g_im = -(const_g_re / dc0.im);
    } else {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = -(const_g_re / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      hamiltonian = (const_g_re + bim * const_g_im) / lamX_im;
      const_g_im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      hamiltonian = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      const_g_im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      hamiltonian = (bim * const_g_re + const_g_im) / lamX_im;
      const_g_im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -const_g_im;
  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  hb_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  hb_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, hb_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * 300.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  ib_const_mass.re = const_mass * xAndLambda_data[3];
  ib_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(-const_bankmax) * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 300.0),
                ib_const_mass);
  hb_z.re = xAndLambda_data[2] + 50.0;
  hb_z.im = 0.0;
  v = b_mpower(hb_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * ib_v_re + ai * ib_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(-const_bankmax) * xAndLambda_data[10] * (const_g *
    const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) *
    300.0);
  ai = muDoubleScalarSin(-const_bankmax) * 0.0 * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 300.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        ib_const_mass_re = 0.5;
      } else {
        ib_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        ib_const_mass_im = 0.5;
      } else {
        ib_const_mass_im = -0.5;
      }

      const_mass_re = (ar * ib_const_mass_re + ai * ib_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = -1.5707963267948966;
    *alfatrigSave = alfatrig;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(const_bankmax);
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(const_bankmax);
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(2.0 * const_bankmax);
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(2.0 * const_bankmax);
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      hamiltonian = const_g_re / dc0.re;
      const_g_im = 0.0;
    } else if (const_g_re == 0.0) {
      hamiltonian = 0.0;
      const_g_im /= dc0.re;
    } else {
      hamiltonian = const_g_re / dc0.re;
      const_g_im /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = 0.0;
    } else if (const_g_im == 0.0) {
      hamiltonian = 0.0;
      const_g_im = -(const_g_re / dc0.im);
    } else {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = -(const_g_re / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      hamiltonian = (const_g_re + bim * const_g_im) / lamX_im;
      const_g_im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      hamiltonian = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      const_g_im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      hamiltonian = (bim * const_g_re + const_g_im) / lamX_im;
      const_g_im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -const_g_im;
  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  ib_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  ib_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, ib_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * 300.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  jb_const_mass.re = const_mass * xAndLambda_data[3];
  jb_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax) * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 300.0),
                jb_const_mass);
  ib_z.re = xAndLambda_data[2] + 50.0;
  ib_z.im = 0.0;
  v = b_mpower(ib_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * jb_v_re + ai * jb_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax) * xAndLambda_data[10] * (const_g *
    const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) *
    300.0);
  ai = muDoubleScalarSin(const_bankmax) * 0.0 * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 300.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        jb_const_mass_re = 0.5;
      } else {
        jb_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        jb_const_mass_im = 0.5;
      } else {
        jb_const_mass_im = -0.5;
      }

      const_mass_re = (ar * jb_const_mass_re + ai * jb_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = 1.5707963267948966;
    *alfatrigSave = alfatrig;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&t_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = 3.1416 / (2.0 * const_bankmax);
  b_asin(&hamiltonian);
  banktrig = -hamiltonian;
  emlrtPopRtStackR2012b(&t_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(-hamiltonian) || muDoubleScalarIsInf(-hamiltonian)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(2.0 * const_bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(2.0 * const_bankmax * muDoubleScalarSin
    (banktrig));
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      hamiltonian = const_g_re / dc0.re;
      const_g_im = 0.0;
    } else if (const_g_re == 0.0) {
      hamiltonian = 0.0;
      const_g_im /= dc0.re;
    } else {
      hamiltonian = const_g_re / dc0.re;
      const_g_im /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = 0.0;
    } else if (const_g_im == 0.0) {
      hamiltonian = 0.0;
      const_g_im = -(const_g_re / dc0.im);
    } else {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = -(const_g_re / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      hamiltonian = (const_g_re + bim * const_g_im) / lamX_im;
      const_g_im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      hamiltonian = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      const_g_im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      hamiltonian = (bim * const_g_re + const_g_im) / lamX_im;
      const_g_im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -const_g_im;
  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  jb_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  jb_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, jb_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * 300.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  kb_const_mass.re = const_mass * xAndLambda_data[3];
  kb_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig)) *
                (const_g * const_mass + muDoubleScalarSin(const_alfamax *
    muDoubleScalarSin(alfatrig)) * 300.0), kb_const_mass);
  jb_z.re = xAndLambda_data[2] + 50.0;
  jb_z.im = 0.0;
  v = b_mpower(jb_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * kb_v_re + ai * kb_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda_data[10] * (const_g * const_mass + muDoubleScalarSin
    (const_alfamax * muDoubleScalarSin(alfatrig)) * 300.0);
  ai = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (const_g * const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin
      (alfatrig)) * 300.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        kb_const_mass_re = 0.5;
      } else {
        kb_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        kb_const_mass_im = 0.5;
      } else {
        kb_const_mass_im = -0.5;
      }

      const_mass_re = (ar * kb_const_mass_re + ai * kb_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&u_emlrtRSI, emlrtRootTLSGlobal);
  banktrig = 3.1416 / (2.0 * const_bankmax);
  b_asin(&banktrig);
  emlrtPopRtStackR2012b(&u_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(banktrig) || muDoubleScalarIsInf(banktrig)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(2.0 * const_bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(2.0 * const_bankmax * muDoubleScalarSin
    (banktrig));
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      hamiltonian = const_g_re / dc0.re;
      const_g_im = 0.0;
    } else if (const_g_re == 0.0) {
      hamiltonian = 0.0;
      const_g_im /= dc0.re;
    } else {
      hamiltonian = const_g_re / dc0.re;
      const_g_im /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = 0.0;
    } else if (const_g_im == 0.0) {
      hamiltonian = 0.0;
      const_g_im = -(const_g_re / dc0.im);
    } else {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = -(const_g_re / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      hamiltonian = (const_g_re + bim * const_g_im) / lamX_im;
      const_g_im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      hamiltonian = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      const_g_im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      hamiltonian = (bim * const_g_re + const_g_im) / lamX_im;
      const_g_im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -const_g_im;
  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  kb_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  kb_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, kb_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * 300.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  lb_const_mass.re = const_mass * xAndLambda_data[3];
  lb_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig)) *
                (const_g * const_mass + muDoubleScalarSin(const_alfamax *
    muDoubleScalarSin(alfatrig)) * 300.0), lb_const_mass);
  kb_z.re = xAndLambda_data[2] + 50.0;
  kb_z.im = 0.0;
  v = b_mpower(kb_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * lb_v_re + ai * lb_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda_data[10] * (const_g * const_mass + muDoubleScalarSin
    (const_alfamax * muDoubleScalarSin(alfatrig)) * 300.0);
  ai = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (const_g * const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin
      (alfatrig)) * 300.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        lb_const_mass_re = 0.5;
      } else {
        lb_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        lb_const_mass_im = 0.5;
      } else {
        lb_const_mass_im = -0.5;
      }

      const_mass_re = (ar * lb_const_mass_re + ai * lb_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(-const_bankmax);
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(-const_bankmax);
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(-(2.0 * const_bankmax));
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(-(2.0 * const_bankmax));
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      hamiltonian = const_g_re / dc0.re;
      const_g_im = 0.0;
    } else if (const_g_re == 0.0) {
      hamiltonian = 0.0;
      const_g_im /= dc0.re;
    } else {
      hamiltonian = const_g_re / dc0.re;
      const_g_im /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = 0.0;
    } else if (const_g_im == 0.0) {
      hamiltonian = 0.0;
      const_g_im = -(const_g_re / dc0.im);
    } else {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = -(const_g_re / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      hamiltonian = (const_g_re + bim * const_g_im) / lamX_im;
      const_g_im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      hamiltonian = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      const_g_im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      hamiltonian = (bim * const_g_re + const_g_im) / lamX_im;
      const_g_im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -const_g_im;
  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  lb_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  lb_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, lb_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * 300.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  mb_const_mass.re = const_mass * xAndLambda_data[3];
  mb_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(-const_bankmax) * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 300.0),
                mb_const_mass);
  lb_z.re = xAndLambda_data[2] + 50.0;
  lb_z.im = 0.0;
  v = b_mpower(lb_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * mb_v_re + ai * mb_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(-const_bankmax) * xAndLambda_data[10] * (const_g *
    const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) *
    300.0);
  ai = muDoubleScalarSin(-const_bankmax) * 0.0 * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 300.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        mb_const_mass_re = 0.5;
      } else {
        mb_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        mb_const_mass_im = 0.5;
      } else {
        mb_const_mass_im = -0.5;
      }

      const_mass_re = (ar * mb_const_mass_re + ai * mb_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = -1.5707963267948966;
    *alfatrigSave = alfatrig;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(const_bankmax);
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(const_bankmax);
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(2.0 * const_bankmax);
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(2.0 * const_bankmax);
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      hamiltonian = const_g_re / dc0.re;
      const_g_im = 0.0;
    } else if (const_g_re == 0.0) {
      hamiltonian = 0.0;
      const_g_im /= dc0.re;
    } else {
      hamiltonian = const_g_re / dc0.re;
      const_g_im /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = 0.0;
    } else if (const_g_im == 0.0) {
      hamiltonian = 0.0;
      const_g_im = -(const_g_re / dc0.im);
    } else {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = -(const_g_re / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      hamiltonian = (const_g_re + bim * const_g_im) / lamX_im;
      const_g_im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      hamiltonian = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      const_g_im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      hamiltonian = (bim * const_g_re + const_g_im) / lamX_im;
      const_g_im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -const_g_im;
  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  mb_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  mb_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, mb_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * 300.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  nb_const_mass.re = const_mass * xAndLambda_data[3];
  nb_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax) * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 300.0),
                nb_const_mass);
  mb_z.re = xAndLambda_data[2] + 50.0;
  mb_z.im = 0.0;
  v = b_mpower(mb_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * nb_v_re + ai * nb_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax) * xAndLambda_data[10] * (const_g *
    const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) *
    300.0);
  ai = muDoubleScalarSin(const_bankmax) * 0.0 * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 300.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        nb_const_mass_re = 0.5;
      } else {
        nb_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        nb_const_mass_im = 0.5;
      } else {
        nb_const_mass_im = -0.5;
      }

      const_mass_re = (ar * nb_const_mass_re + ai * nb_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = 1.5707963267948966;
    *alfatrigSave = alfatrig;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&v_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = 3.1416 / (2.0 * const_bankmax);
  b_asin(&hamiltonian);
  banktrig = -hamiltonian;
  emlrtPopRtStackR2012b(&v_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(-hamiltonian) || muDoubleScalarIsInf(-hamiltonian)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(2.0 * const_bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(2.0 * const_bankmax * muDoubleScalarSin
    (banktrig));
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      hamiltonian = const_g_re / dc0.re;
      const_g_im = 0.0;
    } else if (const_g_re == 0.0) {
      hamiltonian = 0.0;
      const_g_im /= dc0.re;
    } else {
      hamiltonian = const_g_re / dc0.re;
      const_g_im /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = 0.0;
    } else if (const_g_im == 0.0) {
      hamiltonian = 0.0;
      const_g_im = -(const_g_re / dc0.im);
    } else {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = -(const_g_re / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      hamiltonian = (const_g_re + bim * const_g_im) / lamX_im;
      const_g_im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      hamiltonian = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      const_g_im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      hamiltonian = (bim * const_g_re + const_g_im) / lamX_im;
      const_g_im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -const_g_im;
  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  nb_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  nb_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, nb_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * 300.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  ob_const_mass.re = const_mass * xAndLambda_data[3];
  ob_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig)) *
                (const_g * const_mass + muDoubleScalarSin(const_alfamax *
    muDoubleScalarSin(alfatrig)) * 300.0), ob_const_mass);
  nb_z.re = xAndLambda_data[2] + 50.0;
  nb_z.im = 0.0;
  v = b_mpower(nb_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * ob_v_re + ai * ob_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda_data[10] * (const_g * const_mass + muDoubleScalarSin
    (const_alfamax * muDoubleScalarSin(alfatrig)) * 300.0);
  ai = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (const_g * const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin
      (alfatrig)) * 300.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        ob_const_mass_re = 0.5;
      } else {
        ob_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        ob_const_mass_im = 0.5;
      } else {
        ob_const_mass_im = -0.5;
      }

      const_mass_re = (ar * ob_const_mass_re + ai * ob_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&w_emlrtRSI, emlrtRootTLSGlobal);
  banktrig = 3.1416 / (2.0 * const_bankmax);
  b_asin(&banktrig);
  emlrtPopRtStackR2012b(&w_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(banktrig) || muDoubleScalarIsInf(banktrig)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(2.0 * const_bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(2.0 * const_bankmax * muDoubleScalarSin
    (banktrig));
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      hamiltonian = const_g_re / dc0.re;
      const_g_im = 0.0;
    } else if (const_g_re == 0.0) {
      hamiltonian = 0.0;
      const_g_im /= dc0.re;
    } else {
      hamiltonian = const_g_re / dc0.re;
      const_g_im /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = 0.0;
    } else if (const_g_im == 0.0) {
      hamiltonian = 0.0;
      const_g_im = -(const_g_re / dc0.im);
    } else {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = -(const_g_re / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      hamiltonian = (const_g_re + bim * const_g_im) / lamX_im;
      const_g_im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      hamiltonian = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      const_g_im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      hamiltonian = (bim * const_g_re + const_g_im) / lamX_im;
      const_g_im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -const_g_im;
  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  ob_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  ob_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, ob_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * 300.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  pb_const_mass.re = const_mass * xAndLambda_data[3];
  pb_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig)) *
                (const_g * const_mass + muDoubleScalarSin(const_alfamax *
    muDoubleScalarSin(alfatrig)) * 300.0), pb_const_mass);
  ob_z.re = xAndLambda_data[2] + 50.0;
  ob_z.im = 0.0;
  v = b_mpower(ob_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * pb_v_re + ai * pb_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda_data[10] * (const_g * const_mass + muDoubleScalarSin
    (const_alfamax * muDoubleScalarSin(alfatrig)) * 300.0);
  ai = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (const_g * const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin
      (alfatrig)) * 300.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        pb_const_mass_re = 0.5;
      } else {
        pb_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        pb_const_mass_im = 0.5;
      } else {
        pb_const_mass_im = -0.5;
      }

      const_mass_re = (ar * pb_const_mass_re + ai * pb_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(-const_bankmax);
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(-const_bankmax);
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(-(2.0 * const_bankmax));
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(-(2.0 * const_bankmax));
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  Ttrignew = dc0.re;
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      dc0.re = const_g_re / dc0.re;
      dc0.im = 0.0;
    } else if (const_g_re == 0.0) {
      dc0.re = 0.0;
      dc0.im = const_g_im / Ttrignew;
    } else {
      dc0.re = const_g_re / dc0.re;
      dc0.im = const_g_im / Ttrignew;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      dc0.re = const_g_im / dc0.im;
      dc0.im = 0.0;
    } else if (const_g_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(const_g_re / const_C1_im);
    } else {
      dc0.re = const_g_im / dc0.im;
      dc0.im = -(const_g_re / const_C1_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      dc0.re = (const_g_re + bim * const_g_im) / lamX_im;
      dc0.im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      dc0.re = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      dc0.im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      dc0.re = (bim * const_g_re + const_g_im) / lamX_im;
      dc0.im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  pb_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  pb_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, pb_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * 300.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  qb_const_mass.re = const_mass * xAndLambda_data[3];
  qb_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(-const_bankmax) * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 300.0),
                qb_const_mass);
  pb_z.re = xAndLambda_data[2] + 50.0;
  pb_z.im = 0.0;
  v = b_mpower(pb_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * qb_v_re + ai * qb_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(-const_bankmax) * xAndLambda_data[10] * (const_g *
    const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) *
    300.0);
  ai = muDoubleScalarSin(-const_bankmax) * 0.0 * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 300.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        qb_const_mass_re = 0.5;
      } else {
        qb_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        qb_const_mass_im = 0.5;
      } else {
        qb_const_mass_im = -0.5;
      }

      const_mass_re = (ar * qb_const_mass_re + ai * qb_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = -1.5707963267948966;
    *alfatrigSave = alfatrig;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(const_bankmax);
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(const_bankmax);
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(2.0 * const_bankmax);
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(2.0 * const_bankmax);
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  Ttrignew = dc0.re;
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      dc0.re = const_g_re / dc0.re;
      dc0.im = 0.0;
    } else if (const_g_re == 0.0) {
      dc0.re = 0.0;
      dc0.im = const_g_im / Ttrignew;
    } else {
      dc0.re = const_g_re / dc0.re;
      dc0.im = const_g_im / Ttrignew;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      dc0.re = const_g_im / dc0.im;
      dc0.im = 0.0;
    } else if (const_g_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(const_g_re / const_C1_im);
    } else {
      dc0.re = const_g_im / dc0.im;
      dc0.im = -(const_g_re / const_C1_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      dc0.re = (const_g_re + bim * const_g_im) / lamX_im;
      dc0.im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      dc0.re = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      dc0.im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      dc0.re = (bim * const_g_re + const_g_im) / lamX_im;
      dc0.im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  qb_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  qb_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, qb_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * 300.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  rb_const_mass.re = const_mass * xAndLambda_data[3];
  rb_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax) * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 300.0),
                rb_const_mass);
  qb_z.re = xAndLambda_data[2] + 50.0;
  qb_z.im = 0.0;
  v = b_mpower(qb_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * rb_v_re + ai * rb_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax) * xAndLambda_data[10] * (const_g *
    const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) *
    300.0);
  ai = muDoubleScalarSin(const_bankmax) * 0.0 * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 300.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        rb_const_mass_re = 0.5;
      } else {
        rb_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        rb_const_mass_im = 0.5;
      } else {
        rb_const_mass_im = -0.5;
      }

      const_mass_re = (ar * rb_const_mass_re + ai * rb_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = 1.5707963267948966;
    *alfatrigSave = alfatrig;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&x_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = 3.1416 / (2.0 * const_bankmax);
  b_asin(&hamiltonian);
  banktrig = -hamiltonian;
  emlrtPopRtStackR2012b(&x_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(-hamiltonian) || muDoubleScalarIsInf(-hamiltonian)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(2.0 * const_bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(2.0 * const_bankmax * muDoubleScalarSin
    (banktrig));
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  Ttrignew = dc0.re;
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      dc0.re = const_g_re / dc0.re;
      dc0.im = 0.0;
    } else if (const_g_re == 0.0) {
      dc0.re = 0.0;
      dc0.im = const_g_im / Ttrignew;
    } else {
      dc0.re = const_g_re / dc0.re;
      dc0.im = const_g_im / Ttrignew;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      dc0.re = const_g_im / dc0.im;
      dc0.im = 0.0;
    } else if (const_g_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(const_g_re / const_C1_im);
    } else {
      dc0.re = const_g_im / dc0.im;
      dc0.im = -(const_g_re / const_C1_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      dc0.re = (const_g_re + bim * const_g_im) / lamX_im;
      dc0.im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      dc0.re = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      dc0.im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      dc0.re = (bim * const_g_re + const_g_im) / lamX_im;
      dc0.im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  rb_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  rb_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, rb_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * 300.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  sb_const_mass.re = const_mass * xAndLambda_data[3];
  sb_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig)) *
                (const_g * const_mass + muDoubleScalarSin(const_alfamax *
    muDoubleScalarSin(alfatrig)) * 300.0), sb_const_mass);
  rb_z.re = xAndLambda_data[2] + 50.0;
  rb_z.im = 0.0;
  v = b_mpower(rb_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * sb_v_re + ai * sb_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda_data[10] * (const_g * const_mass + muDoubleScalarSin
    (const_alfamax * muDoubleScalarSin(alfatrig)) * 300.0);
  ai = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (const_g * const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin
      (alfatrig)) * 300.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        sb_const_mass_re = 0.5;
      } else {
        sb_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        sb_const_mass_im = 0.5;
      } else {
        sb_const_mass_im = -0.5;
      }

      const_mass_re = (ar * sb_const_mass_re + ai * sb_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&y_emlrtRSI, emlrtRootTLSGlobal);
  banktrig = 3.1416 / (2.0 * const_bankmax);
  b_asin(&banktrig);
  emlrtPopRtStackR2012b(&y_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(banktrig) || muDoubleScalarIsInf(banktrig)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(2.0 * const_bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(2.0 * const_bankmax * muDoubleScalarSin
    (banktrig));
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  Ttrignew = dc0.re;
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      dc0.re = const_g_re / dc0.re;
      dc0.im = 0.0;
    } else if (const_g_re == 0.0) {
      dc0.re = 0.0;
      dc0.im = const_g_im / Ttrignew;
    } else {
      dc0.re = const_g_re / dc0.re;
      dc0.im = const_g_im / Ttrignew;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      dc0.re = const_g_im / dc0.im;
      dc0.im = 0.0;
    } else if (const_g_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(const_g_re / const_C1_im);
    } else {
      dc0.re = const_g_im / dc0.im;
      dc0.im = -(const_g_re / const_C1_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      dc0.re = (const_g_re + bim * const_g_im) / lamX_im;
      dc0.im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      dc0.re = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      dc0.im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      dc0.re = (bim * const_g_re + const_g_im) / lamX_im;
      dc0.im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  sb_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  sb_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, sb_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * 300.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  tb_const_mass.re = const_mass * xAndLambda_data[3];
  tb_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig)) *
                (const_g * const_mass + muDoubleScalarSin(const_alfamax *
    muDoubleScalarSin(alfatrig)) * 300.0), tb_const_mass);
  sb_z.re = xAndLambda_data[2] + 50.0;
  sb_z.im = 0.0;
  v = b_mpower(sb_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * tb_v_re + ai * tb_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda_data[10] * (const_g * const_mass + muDoubleScalarSin
    (const_alfamax * muDoubleScalarSin(alfatrig)) * 300.0);
  ai = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (const_g * const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin
      (alfatrig)) * 300.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        tb_const_mass_re = 0.5;
      } else {
        tb_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        tb_const_mass_im = 0.5;
      } else {
        tb_const_mass_im = -0.5;
      }

      const_mass_re = (ar * tb_const_mass_re + ai * tb_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(-const_bankmax);
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(-const_bankmax);
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(-(2.0 * const_bankmax));
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(-(2.0 * const_bankmax));
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  Ttrignew = dc0.re;
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      dc0.re = const_g_re / dc0.re;
      dc0.im = 0.0;
    } else if (const_g_re == 0.0) {
      dc0.re = 0.0;
      dc0.im = const_g_im / Ttrignew;
    } else {
      dc0.re = const_g_re / dc0.re;
      dc0.im = const_g_im / Ttrignew;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      dc0.re = const_g_im / dc0.im;
      dc0.im = 0.0;
    } else if (const_g_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(const_g_re / const_C1_im);
    } else {
      dc0.re = const_g_im / dc0.im;
      dc0.im = -(const_g_re / const_C1_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      dc0.re = (const_g_re + bim * const_g_im) / lamX_im;
      dc0.im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      dc0.re = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      dc0.im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      dc0.re = (bim * const_g_re + const_g_im) / lamX_im;
      dc0.im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  tb_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  tb_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, tb_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * 300.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  ub_const_mass.re = const_mass * xAndLambda_data[3];
  ub_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(-const_bankmax) * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 300.0),
                ub_const_mass);
  tb_z.re = xAndLambda_data[2] + 50.0;
  tb_z.im = 0.0;
  v = b_mpower(tb_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * ub_v_re + ai * ub_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(-const_bankmax) * xAndLambda_data[10] * (const_g *
    const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) *
    300.0);
  ai = muDoubleScalarSin(-const_bankmax) * 0.0 * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 300.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        ub_const_mass_re = 0.5;
      } else {
        ub_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        ub_const_mass_im = 0.5;
      } else {
        ub_const_mass_im = -0.5;
      }

      const_mass_re = (ar * ub_const_mass_re + ai * ub_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = -1.5707963267948966;
    *alfatrigSave = alfatrig;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(const_bankmax);
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(const_bankmax);
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(2.0 * const_bankmax);
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(2.0 * const_bankmax);
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  Ttrignew = dc0.re;
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      dc0.re = const_g_re / dc0.re;
      dc0.im = 0.0;
    } else if (const_g_re == 0.0) {
      dc0.re = 0.0;
      dc0.im = const_g_im / Ttrignew;
    } else {
      dc0.re = const_g_re / dc0.re;
      dc0.im = const_g_im / Ttrignew;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      dc0.re = const_g_im / dc0.im;
      dc0.im = 0.0;
    } else if (const_g_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(const_g_re / const_C1_im);
    } else {
      dc0.re = const_g_im / dc0.im;
      dc0.im = -(const_g_re / const_C1_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      dc0.re = (const_g_re + bim * const_g_im) / lamX_im;
      dc0.im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      dc0.re = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      dc0.im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      dc0.re = (bim * const_g_re + const_g_im) / lamX_im;
      dc0.im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  ub_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  ub_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, ub_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * 300.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  vb_const_mass.re = const_mass * xAndLambda_data[3];
  vb_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax) * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 300.0),
                vb_const_mass);
  ub_z.re = xAndLambda_data[2] + 50.0;
  ub_z.im = 0.0;
  v = b_mpower(ub_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * vb_v_re + ai * vb_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax) * xAndLambda_data[10] * (const_g *
    const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) *
    300.0);
  ai = muDoubleScalarSin(const_bankmax) * 0.0 * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 300.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        vb_const_mass_re = 0.5;
      } else {
        vb_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        vb_const_mass_im = 0.5;
      } else {
        vb_const_mass_im = -0.5;
      }

      const_mass_re = (ar * vb_const_mass_re + ai * vb_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = 1.5707963267948966;
    *alfatrigSave = alfatrig;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&ab_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = 3.1416 / (2.0 * const_bankmax);
  b_asin(&hamiltonian);
  banktrig = -hamiltonian;
  emlrtPopRtStackR2012b(&ab_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(-hamiltonian) || muDoubleScalarIsInf(-hamiltonian)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(2.0 * const_bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(2.0 * const_bankmax * muDoubleScalarSin
    (banktrig));
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  Ttrignew = dc0.re;
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      dc0.re = const_g_re / dc0.re;
      dc0.im = 0.0;
    } else if (const_g_re == 0.0) {
      dc0.re = 0.0;
      dc0.im = const_g_im / Ttrignew;
    } else {
      dc0.re = const_g_re / dc0.re;
      dc0.im = const_g_im / Ttrignew;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      dc0.re = const_g_im / dc0.im;
      dc0.im = 0.0;
    } else if (const_g_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(const_g_re / const_C1_im);
    } else {
      dc0.re = const_g_im / dc0.im;
      dc0.im = -(const_g_re / const_C1_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      dc0.re = (const_g_re + bim * const_g_im) / lamX_im;
      dc0.im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      dc0.re = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      dc0.im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      dc0.re = (bim * const_g_re + const_g_im) / lamX_im;
      dc0.im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  vb_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  vb_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, vb_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * 300.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  wb_const_mass.re = const_mass * xAndLambda_data[3];
  wb_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig)) *
                (const_g * const_mass + muDoubleScalarSin(const_alfamax *
    muDoubleScalarSin(alfatrig)) * 300.0), wb_const_mass);
  vb_z.re = xAndLambda_data[2] + 50.0;
  vb_z.im = 0.0;
  v = b_mpower(vb_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * wb_v_re + ai * wb_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda_data[10] * (const_g * const_mass + muDoubleScalarSin
    (const_alfamax * muDoubleScalarSin(alfatrig)) * 300.0);
  ai = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (const_g * const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin
      (alfatrig)) * 300.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        wb_const_mass_re = 0.5;
      } else {
        wb_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        wb_const_mass_im = 0.5;
      } else {
        wb_const_mass_im = -0.5;
      }

      const_mass_re = (ar * wb_const_mass_re + ai * wb_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *TtrignewSave = -1.5707963267948966;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&bb_emlrtRSI, emlrtRootTLSGlobal);
  banktrig = 3.1416 / (2.0 * const_bankmax);
  b_asin(&banktrig);
  emlrtPopRtStackR2012b(&bb_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(banktrig) || muDoubleScalarIsInf(banktrig)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(2.0 * const_bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(2.0 * const_bankmax * muDoubleScalarSin
    (banktrig));
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  Ttrignew = dc0.re;
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      dc0.re = const_g_re / dc0.re;
      dc0.im = 0.0;
    } else if (const_g_re == 0.0) {
      dc0.re = 0.0;
      dc0.im = const_g_im / Ttrignew;
    } else {
      dc0.re = const_g_re / dc0.re;
      dc0.im = const_g_im / Ttrignew;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      dc0.re = const_g_im / dc0.im;
      dc0.im = 0.0;
    } else if (const_g_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(const_g_re / const_C1_im);
    } else {
      dc0.re = const_g_im / dc0.im;
      dc0.im = -(const_g_re / const_C1_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      dc0.re = (const_g_re + bim * const_g_im) / lamX_im;
      dc0.im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      dc0.re = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      dc0.im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      dc0.re = (bim * const_g_re + const_g_im) / lamX_im;
      dc0.im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  wb_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  wb_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, wb_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * 300.0;
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  xb_const_mass.re = const_mass * xAndLambda_data[3];
  xb_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig)) *
                (const_g * const_mass + muDoubleScalarSin(const_alfamax *
    muDoubleScalarSin(alfatrig)) * 300.0), xb_const_mass);
  wb_z.re = xAndLambda_data[2] + 50.0;
  wb_z.im = 0.0;
  v = b_mpower(wb_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * 7.60379718621252E+12;
  ai = a.im * 7.60379718621252E+12;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * xb_v_re + ai * xb_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda_data[10] * (const_g * const_mass + muDoubleScalarSin
    (const_alfamax * muDoubleScalarSin(alfatrig)) * 300.0);
  ai = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (const_g * const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin
      (alfatrig)) * 300.0);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        xb_const_mass_re = 0.5;
      } else {
        xb_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        xb_const_mass_im = 0.5;
      } else {
        xb_const_mass_im = -0.5;
      }

      const_mass_re = (ar * xb_const_mass_re + ai * xb_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
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
  xb_z.re = xAndLambda_data[2] + 50.0;
  xb_z.im = 0.0;
  dc1 = b_mpower(xb_z);
  v_re = xAndLambda_data[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda_data[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda_data[9] * muDoubleScalarCos(-const_alfamax));
  ai = -(0.0 * muDoubleScalarCos(-const_alfamax));
  if (ai == 0.0) {
    Ttrignew = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    Ttrignew = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    Ttrignew = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = muDoubleScalarSin(-const_alfamax) * (1560.0 * xAndLambda_data[11]) *
    muDoubleScalarCos(-const_bankmax);
  ai = muDoubleScalarSin(-const_alfamax) * 0.0 * muDoubleScalarCos
    (-const_bankmax);
  hamiltonian = const_mass * xAndLambda_data[3];
  lamX_im = const_mass * 0.0;
  if (lamX_im == 0.0) {
    if (ai == 0.0) {
      const_C1_re = ar / hamiltonian;
      lamY_im = 0.0;
    } else if (ar == 0.0) {
      const_C1_re = 0.0;
      lamY_im = ai / hamiltonian;
    } else {
      const_C1_re = ar / hamiltonian;
      lamY_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      const_C1_re = ai / lamX_im;
      lamY_im = 0.0;
    } else if (ai == 0.0) {
      const_C1_re = 0.0;
      lamY_im = -(ar / lamX_im);
    } else {
      const_C1_re = ai / lamX_im;
      lamY_im = -(ar / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > lamX_im) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      const_C1_re = (ar + bim * ai) / lamX_im;
      lamY_im = (ai - bim * ar) / lamX_im;
    } else if (lamX_im == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      const_C1_re = (ar * lamY_re + ai * -0.5) / 0.0;
      lamY_im = (ai * lamY_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      const_C1_re = (bim * ar + ai) / lamX_im;
      lamY_im = (bim * ai - ar) / lamX_im;
    }
  }

  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * a.re - const_mass_im * a.im;
  const_mass_im = hamiltonian * a.im + const_mass_im * a.re;
  ar = muDoubleScalarSin(-const_alfamax) * (1560.0 * xAndLambda_data[10]) *
    muDoubleScalarSin(-const_bankmax);
  ai = muDoubleScalarSin(-const_alfamax) * 0.0 * muDoubleScalarSin
    (-const_bankmax);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      lamX_re = ar / const_mass_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      lamX_re = 0.0;
      hamiltonian = ai / const_mass_re;
    } else {
      lamX_re = ar / const_mass_re;
      hamiltonian = ai / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      lamX_re = ai / const_mass_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      lamX_re = 0.0;
      hamiltonian = -(ar / const_mass_im);
    } else {
      lamX_re = ai / const_mass_im;
      hamiltonian = -(ar / const_mass_im);
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      lamX_im = const_mass_re + bim * const_mass_im;
      lamX_re = (ar + bim * ai) / lamX_im;
      hamiltonian = (ai - bim * ar) / lamX_im;
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      lamX_re = (ar * lamY_re + ai * lamX_im) / brm;
      hamiltonian = (ai * lamY_re - ar * lamX_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      lamX_im = const_mass_im + bim * const_mass_re;
      lamX_re = (bim * ar + ai) / lamX_im;
      hamiltonian = (bim * ai - ar) / lamX_im;
    }
  }

  Ttrignew = (Ttrignew - const_C1_re) - lamX_re;
  const_C1_im = (const_C1_im - lamY_im) - hamiltonian;
  lamX_re = v_re * Ttrignew - v_im * const_C1_im;
  v_im = v_re * const_C1_im + v_im * Ttrignew;
  hamiltonian = 8112.0 * dc0.re;
  lamX_im = 8112.0 * dc0.im;
  if (lamX_im == 0.0) {
    if (v_im == 0.0) {
      xb_v.re = lamX_re / hamiltonian;
      xb_v.im = 0.0;
    } else if (lamX_re == 0.0) {
      xb_v.re = 0.0;
      xb_v.im = v_im / hamiltonian;
    } else {
      xb_v.re = lamX_re / hamiltonian;
      xb_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (lamX_re == 0.0) {
      xb_v.re = v_im / lamX_im;
      xb_v.im = 0.0;
    } else if (v_im == 0.0) {
      xb_v.re = 0.0;
      xb_v.im = -(lamX_re / lamX_im);
    } else {
      xb_v.re = v_im / lamX_im;
      xb_v.im = -(lamX_re / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(lamX_im);
    if (brm > bim) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      xb_v.re = (lamX_re + bim * v_im) / lamX_im;
      xb_v.im = (v_im - bim * lamX_re) / lamX_im;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (lamX_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      xb_v.re = (lamX_re * lamY_re + v_im * lamX_im) / brm;
      xb_v.im = (v_im * lamY_re - lamX_re * lamX_im) / brm;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      xb_v.re = (bim * lamX_re + v_im) / lamX_im;
      xb_v.im = (bim * v_im - lamX_re) / lamX_im;
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
  yb_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  yb_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, yb_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(-const_alfamax) * (1560.0 * muDoubleScalarSin(Ttrignew) +
    1860.0);
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  yb_const_mass.re = const_mass * xAndLambda_data[3];
  yb_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(-const_bankmax) * (const_g * const_mass +
    muDoubleScalarSin(-const_alfamax) * (1560.0 * muDoubleScalarSin(Ttrignew) +
    1860.0)), yb_const_mass);
  yb_z.re = xAndLambda_data[2] + 50.0;
  yb_z.im = 0.0;
  v = b_mpower(yb_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * yb_v_re + ai * yb_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(-const_bankmax) * xAndLambda_data[10] * (const_g *
    const_mass + muDoubleScalarSin(-const_alfamax) * (1560.0 * muDoubleScalarSin
    (Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(-const_bankmax) * 0.0 * (const_g * const_mass +
    muDoubleScalarSin(-const_alfamax) * (1560.0 * muDoubleScalarSin(Ttrignew) +
    1860.0));
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        yb_const_mass_re = 0.5;
      } else {
        yb_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        yb_const_mass_im = 0.5;
      } else {
        yb_const_mass_im = -0.5;
      }

      const_mass_re = (ar * yb_const_mass_re + ai * yb_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  emlrtPopRtStackR2012b(&cb_emlrtRSI, emlrtRootTLSGlobal);
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
  ac_z.re = xAndLambda_data[2] + 50.0;
  ac_z.im = 0.0;
  dc1 = b_mpower(ac_z);
  v_re = xAndLambda_data[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda_data[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda_data[9] * muDoubleScalarCos(-const_alfamax));
  ai = -(0.0 * muDoubleScalarCos(-const_alfamax));
  if (ai == 0.0) {
    Ttrignew = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    Ttrignew = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    Ttrignew = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = muDoubleScalarSin(-const_alfamax) * (1560.0 * xAndLambda_data[11]) *
    muDoubleScalarCos(const_bankmax);
  ai = muDoubleScalarSin(-const_alfamax) * 0.0 * muDoubleScalarCos(const_bankmax);
  hamiltonian = const_mass * xAndLambda_data[3];
  lamX_im = const_mass * 0.0;
  if (lamX_im == 0.0) {
    if (ai == 0.0) {
      const_C1_re = ar / hamiltonian;
      lamY_im = 0.0;
    } else if (ar == 0.0) {
      const_C1_re = 0.0;
      lamY_im = ai / hamiltonian;
    } else {
      const_C1_re = ar / hamiltonian;
      lamY_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      const_C1_re = ai / lamX_im;
      lamY_im = 0.0;
    } else if (ai == 0.0) {
      const_C1_re = 0.0;
      lamY_im = -(ar / lamX_im);
    } else {
      const_C1_re = ai / lamX_im;
      lamY_im = -(ar / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > lamX_im) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      const_C1_re = (ar + bim * ai) / lamX_im;
      lamY_im = (ai - bim * ar) / lamX_im;
    } else if (lamX_im == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      const_C1_re = (ar * lamY_re + ai * -0.5) / 0.0;
      lamY_im = (ai * lamY_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      const_C1_re = (bim * ar + ai) / lamX_im;
      lamY_im = (bim * ai - ar) / lamX_im;
    }
  }

  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * a.re - const_mass_im * a.im;
  const_mass_im = hamiltonian * a.im + const_mass_im * a.re;
  ar = muDoubleScalarSin(-const_alfamax) * (1560.0 * xAndLambda_data[10]) *
    muDoubleScalarSin(const_bankmax);
  ai = muDoubleScalarSin(-const_alfamax) * 0.0 * muDoubleScalarSin(const_bankmax);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      lamX_re = ar / const_mass_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      lamX_re = 0.0;
      hamiltonian = ai / const_mass_re;
    } else {
      lamX_re = ar / const_mass_re;
      hamiltonian = ai / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      lamX_re = ai / const_mass_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      lamX_re = 0.0;
      hamiltonian = -(ar / const_mass_im);
    } else {
      lamX_re = ai / const_mass_im;
      hamiltonian = -(ar / const_mass_im);
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      lamX_im = const_mass_re + bim * const_mass_im;
      lamX_re = (ar + bim * ai) / lamX_im;
      hamiltonian = (ai - bim * ar) / lamX_im;
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      lamX_re = (ar * lamY_re + ai * lamX_im) / brm;
      hamiltonian = (ai * lamY_re - ar * lamX_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      lamX_im = const_mass_im + bim * const_mass_re;
      lamX_re = (bim * ar + ai) / lamX_im;
      hamiltonian = (bim * ai - ar) / lamX_im;
    }
  }

  Ttrignew = (Ttrignew - const_C1_re) - lamX_re;
  const_C1_im = (const_C1_im - lamY_im) - hamiltonian;
  lamX_re = v_re * Ttrignew - v_im * const_C1_im;
  v_im = v_re * const_C1_im + v_im * Ttrignew;
  hamiltonian = 8112.0 * dc0.re;
  lamX_im = 8112.0 * dc0.im;
  if (lamX_im == 0.0) {
    if (v_im == 0.0) {
      ac_v.re = lamX_re / hamiltonian;
      ac_v.im = 0.0;
    } else if (lamX_re == 0.0) {
      ac_v.re = 0.0;
      ac_v.im = v_im / hamiltonian;
    } else {
      ac_v.re = lamX_re / hamiltonian;
      ac_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (lamX_re == 0.0) {
      ac_v.re = v_im / lamX_im;
      ac_v.im = 0.0;
    } else if (v_im == 0.0) {
      ac_v.re = 0.0;
      ac_v.im = -(lamX_re / lamX_im);
    } else {
      ac_v.re = v_im / lamX_im;
      ac_v.im = -(lamX_re / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(lamX_im);
    if (brm > bim) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      ac_v.re = (lamX_re + bim * v_im) / lamX_im;
      ac_v.im = (v_im - bim * lamX_re) / lamX_im;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (lamX_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      ac_v.re = (lamX_re * lamY_re + v_im * lamX_im) / brm;
      ac_v.im = (v_im * lamY_re - lamX_re * lamX_im) / brm;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      ac_v.re = (bim * lamX_re + v_im) / lamX_im;
      ac_v.im = (bim * v_im - lamX_re) / lamX_im;
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

  emlrtPushRtStackR2012b(&db_emlrtRSI, emlrtRootTLSGlobal);
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
  bc_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  bc_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, bc_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(-const_alfamax) * (1560.0 * muDoubleScalarSin(Ttrignew) +
    1860.0);
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  ac_const_mass.re = const_mass * xAndLambda_data[3];
  ac_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax) * (const_g * const_mass +
    muDoubleScalarSin(-const_alfamax) * (1560.0 * muDoubleScalarSin(Ttrignew) +
    1860.0)), ac_const_mass);
  bc_z.re = xAndLambda_data[2] + 50.0;
  bc_z.im = 0.0;
  v = b_mpower(bc_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * ac_v_re + ai * ac_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax) * xAndLambda_data[10] * (const_g *
    const_mass + muDoubleScalarSin(-const_alfamax) * (1560.0 * muDoubleScalarSin
    (Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(const_bankmax) * 0.0 * (const_g * const_mass +
    muDoubleScalarSin(-const_alfamax) * (1560.0 * muDoubleScalarSin(Ttrignew) +
    1860.0));
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        ac_const_mass_re = 0.5;
      } else {
        ac_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        ac_const_mass_im = 0.5;
      } else {
        ac_const_mass_im = -0.5;
      }

      const_mass_re = (ar * ac_const_mass_re + ai * ac_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  emlrtPopRtStackR2012b(&db_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = 1.5707963267948966;
    *alfatrigSave = -1.5707963267948966;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&eb_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = 3.1416 / (2.0 * const_bankmax);
  b_asin(&hamiltonian);
  banktrig = -hamiltonian;
  emlrtPopRtStackR2012b(&eb_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(-hamiltonian) || muDoubleScalarIsInf(-hamiltonian)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  /*  Coefficients */
  dc0 = gam;
  b_cos(&dc0);
  a = gam;
  b_cos(&a);
  cc_z.re = xAndLambda_data[2] + 50.0;
  cc_z.im = 0.0;
  dc1 = b_mpower(cc_z);
  v_re = xAndLambda_data[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda_data[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda_data[9] * muDoubleScalarCos(-const_alfamax));
  ai = -(0.0 * muDoubleScalarCos(-const_alfamax));
  if (ai == 0.0) {
    Ttrignew = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    Ttrignew = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    Ttrignew = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = muDoubleScalarSin(-const_alfamax) * (1560.0 * xAndLambda_data[11]) *
    muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig));
  ai = muDoubleScalarSin(-const_alfamax) * 0.0 * muDoubleScalarCos(const_bankmax
    * muDoubleScalarSin(banktrig));
  hamiltonian = const_mass * xAndLambda_data[3];
  lamX_im = const_mass * 0.0;
  if (lamX_im == 0.0) {
    if (ai == 0.0) {
      const_C1_re = ar / hamiltonian;
      lamY_im = 0.0;
    } else if (ar == 0.0) {
      const_C1_re = 0.0;
      lamY_im = ai / hamiltonian;
    } else {
      const_C1_re = ar / hamiltonian;
      lamY_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      const_C1_re = ai / lamX_im;
      lamY_im = 0.0;
    } else if (ai == 0.0) {
      const_C1_re = 0.0;
      lamY_im = -(ar / lamX_im);
    } else {
      const_C1_re = ai / lamX_im;
      lamY_im = -(ar / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > lamX_im) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      const_C1_re = (ar + bim * ai) / lamX_im;
      lamY_im = (ai - bim * ar) / lamX_im;
    } else if (lamX_im == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      const_C1_re = (ar * lamY_re + ai * -0.5) / 0.0;
      lamY_im = (ai * lamY_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      const_C1_re = (bim * ar + ai) / lamX_im;
      lamY_im = (bim * ai - ar) / lamX_im;
    }
  }

  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * a.re - const_mass_im * a.im;
  const_mass_im = hamiltonian * a.im + const_mass_im * a.re;
  ar = muDoubleScalarSin(-const_alfamax) * (1560.0 * xAndLambda_data[10]) *
    muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig));
  ai = muDoubleScalarSin(-const_alfamax) * 0.0 * muDoubleScalarSin(const_bankmax
    * muDoubleScalarSin(banktrig));
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      lamX_re = ar / const_mass_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      lamX_re = 0.0;
      hamiltonian = ai / const_mass_re;
    } else {
      lamX_re = ar / const_mass_re;
      hamiltonian = ai / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      lamX_re = ai / const_mass_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      lamX_re = 0.0;
      hamiltonian = -(ar / const_mass_im);
    } else {
      lamX_re = ai / const_mass_im;
      hamiltonian = -(ar / const_mass_im);
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      lamX_im = const_mass_re + bim * const_mass_im;
      lamX_re = (ar + bim * ai) / lamX_im;
      hamiltonian = (ai - bim * ar) / lamX_im;
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      lamX_re = (ar * lamY_re + ai * lamX_im) / brm;
      hamiltonian = (ai * lamY_re - ar * lamX_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      lamX_im = const_mass_im + bim * const_mass_re;
      lamX_re = (bim * ar + ai) / lamX_im;
      hamiltonian = (bim * ai - ar) / lamX_im;
    }
  }

  Ttrignew = (Ttrignew - const_C1_re) - lamX_re;
  const_C1_im = (const_C1_im - lamY_im) - hamiltonian;
  lamX_re = v_re * Ttrignew - v_im * const_C1_im;
  v_im = v_re * const_C1_im + v_im * Ttrignew;
  hamiltonian = 8112.0 * dc0.re;
  lamX_im = 8112.0 * dc0.im;
  if (lamX_im == 0.0) {
    if (v_im == 0.0) {
      cc_v.re = lamX_re / hamiltonian;
      cc_v.im = 0.0;
    } else if (lamX_re == 0.0) {
      cc_v.re = 0.0;
      cc_v.im = v_im / hamiltonian;
    } else {
      cc_v.re = lamX_re / hamiltonian;
      cc_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (lamX_re == 0.0) {
      cc_v.re = v_im / lamX_im;
      cc_v.im = 0.0;
    } else if (v_im == 0.0) {
      cc_v.re = 0.0;
      cc_v.im = -(lamX_re / lamX_im);
    } else {
      cc_v.re = v_im / lamX_im;
      cc_v.im = -(lamX_re / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(lamX_im);
    if (brm > bim) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      cc_v.re = (lamX_re + bim * v_im) / lamX_im;
      cc_v.im = (v_im - bim * lamX_re) / lamX_im;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (lamX_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      cc_v.re = (lamX_re * lamY_re + v_im * lamX_im) / brm;
      cc_v.im = (v_im * lamY_re - lamX_re * lamX_im) / brm;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      cc_v.re = (bim * lamX_re + v_im) / lamX_im;
      cc_v.im = (bim * v_im - lamX_re) / lamX_im;
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
  dc_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  dc_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, dc_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(-const_alfamax) * (1560.0 * muDoubleScalarSin(Ttrignew) +
    1860.0);
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  bc_const_mass.re = const_mass * xAndLambda_data[3];
  bc_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig)) *
                (const_g * const_mass + muDoubleScalarSin(-const_alfamax) *
                 (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0)), bc_const_mass);
  dc_z.re = xAndLambda_data[2] + 50.0;
  dc_z.im = 0.0;
  v = b_mpower(dc_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * bc_v_re + ai * bc_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda_data[10] * (const_g * const_mass + muDoubleScalarSin
    (-const_alfamax) * (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (const_g * const_mass + muDoubleScalarSin(-const_alfamax) * (1560.0 *
      muDoubleScalarSin(Ttrignew) + 1860.0));
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        bc_const_mass_re = 0.5;
      } else {
        bc_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        bc_const_mass_im = 0.5;
      } else {
        bc_const_mass_im = -0.5;
      }

      const_mass_re = (ar * bc_const_mass_re + ai * bc_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  emlrtPopRtStackR2012b(&fb_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = -1.5707963267948966;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&gb_emlrtRSI, emlrtRootTLSGlobal);
  banktrig = 3.1416 / (2.0 * const_bankmax);
  b_asin(&banktrig);
  emlrtPopRtStackR2012b(&gb_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(banktrig) || muDoubleScalarIsInf(banktrig)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  /*  Coefficients */
  dc0 = gam;
  b_cos(&dc0);
  a = gam;
  b_cos(&a);
  ec_z.re = xAndLambda_data[2] + 50.0;
  ec_z.im = 0.0;
  dc1 = b_mpower(ec_z);
  v_re = xAndLambda_data[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda_data[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda_data[9] * muDoubleScalarCos(-const_alfamax));
  ai = -(0.0 * muDoubleScalarCos(-const_alfamax));
  if (ai == 0.0) {
    Ttrignew = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    Ttrignew = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    Ttrignew = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = muDoubleScalarSin(-const_alfamax) * (1560.0 * xAndLambda_data[11]) *
    muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig));
  ai = muDoubleScalarSin(-const_alfamax) * 0.0 * muDoubleScalarCos(const_bankmax
    * muDoubleScalarSin(banktrig));
  hamiltonian = const_mass * xAndLambda_data[3];
  lamX_im = const_mass * 0.0;
  if (lamX_im == 0.0) {
    if (ai == 0.0) {
      const_C1_re = ar / hamiltonian;
      lamY_im = 0.0;
    } else if (ar == 0.0) {
      const_C1_re = 0.0;
      lamY_im = ai / hamiltonian;
    } else {
      const_C1_re = ar / hamiltonian;
      lamY_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      const_C1_re = ai / lamX_im;
      lamY_im = 0.0;
    } else if (ai == 0.0) {
      const_C1_re = 0.0;
      lamY_im = -(ar / lamX_im);
    } else {
      const_C1_re = ai / lamX_im;
      lamY_im = -(ar / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > lamX_im) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      const_C1_re = (ar + bim * ai) / lamX_im;
      lamY_im = (ai - bim * ar) / lamX_im;
    } else if (lamX_im == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      const_C1_re = (ar * lamY_re + ai * -0.5) / 0.0;
      lamY_im = (ai * lamY_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      const_C1_re = (bim * ar + ai) / lamX_im;
      lamY_im = (bim * ai - ar) / lamX_im;
    }
  }

  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * a.re - const_mass_im * a.im;
  const_mass_im = hamiltonian * a.im + const_mass_im * a.re;
  ar = muDoubleScalarSin(-const_alfamax) * (1560.0 * xAndLambda_data[10]) *
    muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig));
  ai = muDoubleScalarSin(-const_alfamax) * 0.0 * muDoubleScalarSin(const_bankmax
    * muDoubleScalarSin(banktrig));
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      lamX_re = ar / const_mass_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      lamX_re = 0.0;
      hamiltonian = ai / const_mass_re;
    } else {
      lamX_re = ar / const_mass_re;
      hamiltonian = ai / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      lamX_re = ai / const_mass_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      lamX_re = 0.0;
      hamiltonian = -(ar / const_mass_im);
    } else {
      lamX_re = ai / const_mass_im;
      hamiltonian = -(ar / const_mass_im);
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      lamX_im = const_mass_re + bim * const_mass_im;
      lamX_re = (ar + bim * ai) / lamX_im;
      hamiltonian = (ai - bim * ar) / lamX_im;
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      lamX_re = (ar * lamY_re + ai * lamX_im) / brm;
      hamiltonian = (ai * lamY_re - ar * lamX_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      lamX_im = const_mass_im + bim * const_mass_re;
      lamX_re = (bim * ar + ai) / lamX_im;
      hamiltonian = (bim * ai - ar) / lamX_im;
    }
  }

  Ttrignew = (Ttrignew - const_C1_re) - lamX_re;
  const_C1_im = (const_C1_im - lamY_im) - hamiltonian;
  lamX_re = v_re * Ttrignew - v_im * const_C1_im;
  v_im = v_re * const_C1_im + v_im * Ttrignew;
  hamiltonian = 8112.0 * dc0.re;
  lamX_im = 8112.0 * dc0.im;
  if (lamX_im == 0.0) {
    if (v_im == 0.0) {
      ec_v.re = lamX_re / hamiltonian;
      ec_v.im = 0.0;
    } else if (lamX_re == 0.0) {
      ec_v.re = 0.0;
      ec_v.im = v_im / hamiltonian;
    } else {
      ec_v.re = lamX_re / hamiltonian;
      ec_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (lamX_re == 0.0) {
      ec_v.re = v_im / lamX_im;
      ec_v.im = 0.0;
    } else if (v_im == 0.0) {
      ec_v.re = 0.0;
      ec_v.im = -(lamX_re / lamX_im);
    } else {
      ec_v.re = v_im / lamX_im;
      ec_v.im = -(lamX_re / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(lamX_im);
    if (brm > bim) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      ec_v.re = (lamX_re + bim * v_im) / lamX_im;
      ec_v.im = (v_im - bim * lamX_re) / lamX_im;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (lamX_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      ec_v.re = (lamX_re * lamY_re + v_im * lamX_im) / brm;
      ec_v.im = (v_im * lamY_re - lamX_re * lamX_im) / brm;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      ec_v.re = (bim * lamX_re + v_im) / lamX_im;
      ec_v.im = (bim * v_im - lamX_re) / lamX_im;
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

  emlrtPushRtStackR2012b(&hb_emlrtRSI, emlrtRootTLSGlobal);
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
  fc_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  fc_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, fc_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(-const_alfamax) * (1560.0 * muDoubleScalarSin(Ttrignew) +
    1860.0);
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  cc_const_mass.re = const_mass * xAndLambda_data[3];
  cc_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig)) *
                (const_g * const_mass + muDoubleScalarSin(-const_alfamax) *
                 (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0)), cc_const_mass);
  fc_z.re = xAndLambda_data[2] + 50.0;
  fc_z.im = 0.0;
  v = b_mpower(fc_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * cc_v_re + ai * cc_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda_data[10] * (const_g * const_mass + muDoubleScalarSin
    (-const_alfamax) * (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (const_g * const_mass + muDoubleScalarSin(-const_alfamax) * (1560.0 *
      muDoubleScalarSin(Ttrignew) + 1860.0));
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        cc_const_mass_re = 0.5;
      } else {
        cc_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        cc_const_mass_im = 0.5;
      } else {
        cc_const_mass_im = -0.5;
      }

      const_mass_re = (ar * cc_const_mass_re + ai * cc_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  emlrtPopRtStackR2012b(&hb_emlrtRSI, emlrtRootTLSGlobal);
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
  gc_z.re = xAndLambda_data[2] + 50.0;
  gc_z.im = 0.0;
  dc1 = b_mpower(gc_z);
  v_re = xAndLambda_data[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda_data[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda_data[9] * muDoubleScalarCos(const_alfamax));
  ai = -(0.0 * muDoubleScalarCos(const_alfamax));
  if (ai == 0.0) {
    Ttrignew = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    Ttrignew = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    Ttrignew = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = muDoubleScalarSin(const_alfamax) * (1560.0 * xAndLambda_data[11]) *
    muDoubleScalarCos(-const_bankmax);
  ai = muDoubleScalarSin(const_alfamax) * 0.0 * muDoubleScalarCos(-const_bankmax);
  hamiltonian = const_mass * xAndLambda_data[3];
  lamX_im = const_mass * 0.0;
  if (lamX_im == 0.0) {
    if (ai == 0.0) {
      const_C1_re = ar / hamiltonian;
      lamY_im = 0.0;
    } else if (ar == 0.0) {
      const_C1_re = 0.0;
      lamY_im = ai / hamiltonian;
    } else {
      const_C1_re = ar / hamiltonian;
      lamY_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      const_C1_re = ai / lamX_im;
      lamY_im = 0.0;
    } else if (ai == 0.0) {
      const_C1_re = 0.0;
      lamY_im = -(ar / lamX_im);
    } else {
      const_C1_re = ai / lamX_im;
      lamY_im = -(ar / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > lamX_im) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      const_C1_re = (ar + bim * ai) / lamX_im;
      lamY_im = (ai - bim * ar) / lamX_im;
    } else if (lamX_im == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      const_C1_re = (ar * lamY_re + ai * -0.5) / 0.0;
      lamY_im = (ai * lamY_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      const_C1_re = (bim * ar + ai) / lamX_im;
      lamY_im = (bim * ai - ar) / lamX_im;
    }
  }

  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * a.re - const_mass_im * a.im;
  const_mass_im = hamiltonian * a.im + const_mass_im * a.re;
  ar = muDoubleScalarSin(const_alfamax) * (1560.0 * xAndLambda_data[10]) *
    muDoubleScalarSin(-const_bankmax);
  ai = muDoubleScalarSin(const_alfamax) * 0.0 * muDoubleScalarSin(-const_bankmax);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      lamX_re = ar / const_mass_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      lamX_re = 0.0;
      hamiltonian = ai / const_mass_re;
    } else {
      lamX_re = ar / const_mass_re;
      hamiltonian = ai / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      lamX_re = ai / const_mass_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      lamX_re = 0.0;
      hamiltonian = -(ar / const_mass_im);
    } else {
      lamX_re = ai / const_mass_im;
      hamiltonian = -(ar / const_mass_im);
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      lamX_im = const_mass_re + bim * const_mass_im;
      lamX_re = (ar + bim * ai) / lamX_im;
      hamiltonian = (ai - bim * ar) / lamX_im;
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      lamX_re = (ar * lamY_re + ai * lamX_im) / brm;
      hamiltonian = (ai * lamY_re - ar * lamX_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      lamX_im = const_mass_im + bim * const_mass_re;
      lamX_re = (bim * ar + ai) / lamX_im;
      hamiltonian = (bim * ai - ar) / lamX_im;
    }
  }

  Ttrignew = (Ttrignew - const_C1_re) - lamX_re;
  const_C1_im = (const_C1_im - lamY_im) - hamiltonian;
  lamX_re = v_re * Ttrignew - v_im * const_C1_im;
  v_im = v_re * const_C1_im + v_im * Ttrignew;
  hamiltonian = 8112.0 * dc0.re;
  lamX_im = 8112.0 * dc0.im;
  if (lamX_im == 0.0) {
    if (v_im == 0.0) {
      gc_v.re = lamX_re / hamiltonian;
      gc_v.im = 0.0;
    } else if (lamX_re == 0.0) {
      gc_v.re = 0.0;
      gc_v.im = v_im / hamiltonian;
    } else {
      gc_v.re = lamX_re / hamiltonian;
      gc_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (lamX_re == 0.0) {
      gc_v.re = v_im / lamX_im;
      gc_v.im = 0.0;
    } else if (v_im == 0.0) {
      gc_v.re = 0.0;
      gc_v.im = -(lamX_re / lamX_im);
    } else {
      gc_v.re = v_im / lamX_im;
      gc_v.im = -(lamX_re / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(lamX_im);
    if (brm > bim) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      gc_v.re = (lamX_re + bim * v_im) / lamX_im;
      gc_v.im = (v_im - bim * lamX_re) / lamX_im;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (lamX_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      gc_v.re = (lamX_re * lamY_re + v_im * lamX_im) / brm;
      gc_v.im = (v_im * lamY_re - lamX_re * lamX_im) / brm;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      gc_v.re = (bim * lamX_re + v_im) / lamX_im;
      gc_v.im = (bim * v_im - lamX_re) / lamX_im;
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
  hc_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  hc_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, hc_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax) * (1560.0 * muDoubleScalarSin(Ttrignew) +
    1860.0);
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  dc_const_mass.re = const_mass * xAndLambda_data[3];
  dc_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(-const_bankmax) * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax) * (1560.0 * muDoubleScalarSin(Ttrignew) +
    1860.0)), dc_const_mass);
  hc_z.re = xAndLambda_data[2] + 50.0;
  hc_z.im = 0.0;
  v = b_mpower(hc_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * dc_v_re + ai * dc_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(-const_bankmax) * xAndLambda_data[10] * (const_g *
    const_mass + muDoubleScalarSin(const_alfamax) * (1560.0 * muDoubleScalarSin
    (Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(-const_bankmax) * 0.0 * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax) * (1560.0 * muDoubleScalarSin(Ttrignew) +
    1860.0));
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        dc_const_mass_re = 0.5;
      } else {
        dc_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        dc_const_mass_im = 0.5;
      } else {
        dc_const_mass_im = -0.5;
      }

      const_mass_re = (ar * dc_const_mass_re + ai * dc_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  emlrtPopRtStackR2012b(&ib_emlrtRSI, emlrtRootTLSGlobal);
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
  ic_z.re = xAndLambda_data[2] + 50.0;
  ic_z.im = 0.0;
  dc1 = b_mpower(ic_z);
  v_re = xAndLambda_data[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda_data[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda_data[9] * muDoubleScalarCos(const_alfamax));
  ai = -(0.0 * muDoubleScalarCos(const_alfamax));
  if (ai == 0.0) {
    Ttrignew = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    Ttrignew = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    Ttrignew = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = muDoubleScalarSin(const_alfamax) * (1560.0 * xAndLambda_data[11]) *
    muDoubleScalarCos(const_bankmax);
  ai = muDoubleScalarSin(const_alfamax) * 0.0 * muDoubleScalarCos(const_bankmax);
  hamiltonian = const_mass * xAndLambda_data[3];
  lamX_im = const_mass * 0.0;
  if (lamX_im == 0.0) {
    if (ai == 0.0) {
      const_C1_re = ar / hamiltonian;
      lamY_im = 0.0;
    } else if (ar == 0.0) {
      const_C1_re = 0.0;
      lamY_im = ai / hamiltonian;
    } else {
      const_C1_re = ar / hamiltonian;
      lamY_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      const_C1_re = ai / lamX_im;
      lamY_im = 0.0;
    } else if (ai == 0.0) {
      const_C1_re = 0.0;
      lamY_im = -(ar / lamX_im);
    } else {
      const_C1_re = ai / lamX_im;
      lamY_im = -(ar / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > lamX_im) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      const_C1_re = (ar + bim * ai) / lamX_im;
      lamY_im = (ai - bim * ar) / lamX_im;
    } else if (lamX_im == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      const_C1_re = (ar * lamY_re + ai * -0.5) / 0.0;
      lamY_im = (ai * lamY_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      const_C1_re = (bim * ar + ai) / lamX_im;
      lamY_im = (bim * ai - ar) / lamX_im;
    }
  }

  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * a.re - const_mass_im * a.im;
  const_mass_im = hamiltonian * a.im + const_mass_im * a.re;
  ar = muDoubleScalarSin(const_alfamax) * (1560.0 * xAndLambda_data[10]) *
    muDoubleScalarSin(const_bankmax);
  ai = muDoubleScalarSin(const_alfamax) * 0.0 * muDoubleScalarSin(const_bankmax);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      lamX_re = ar / const_mass_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      lamX_re = 0.0;
      hamiltonian = ai / const_mass_re;
    } else {
      lamX_re = ar / const_mass_re;
      hamiltonian = ai / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      lamX_re = ai / const_mass_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      lamX_re = 0.0;
      hamiltonian = -(ar / const_mass_im);
    } else {
      lamX_re = ai / const_mass_im;
      hamiltonian = -(ar / const_mass_im);
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      lamX_im = const_mass_re + bim * const_mass_im;
      lamX_re = (ar + bim * ai) / lamX_im;
      hamiltonian = (ai - bim * ar) / lamX_im;
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      lamX_re = (ar * lamY_re + ai * lamX_im) / brm;
      hamiltonian = (ai * lamY_re - ar * lamX_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      lamX_im = const_mass_im + bim * const_mass_re;
      lamX_re = (bim * ar + ai) / lamX_im;
      hamiltonian = (bim * ai - ar) / lamX_im;
    }
  }

  Ttrignew = (Ttrignew - const_C1_re) - lamX_re;
  const_C1_im = (const_C1_im - lamY_im) - hamiltonian;
  lamX_re = v_re * Ttrignew - v_im * const_C1_im;
  v_im = v_re * const_C1_im + v_im * Ttrignew;
  hamiltonian = 8112.0 * dc0.re;
  lamX_im = 8112.0 * dc0.im;
  if (lamX_im == 0.0) {
    if (v_im == 0.0) {
      ic_v.re = lamX_re / hamiltonian;
      ic_v.im = 0.0;
    } else if (lamX_re == 0.0) {
      ic_v.re = 0.0;
      ic_v.im = v_im / hamiltonian;
    } else {
      ic_v.re = lamX_re / hamiltonian;
      ic_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (lamX_re == 0.0) {
      ic_v.re = v_im / lamX_im;
      ic_v.im = 0.0;
    } else if (v_im == 0.0) {
      ic_v.re = 0.0;
      ic_v.im = -(lamX_re / lamX_im);
    } else {
      ic_v.re = v_im / lamX_im;
      ic_v.im = -(lamX_re / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(lamX_im);
    if (brm > bim) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      ic_v.re = (lamX_re + bim * v_im) / lamX_im;
      ic_v.im = (v_im - bim * lamX_re) / lamX_im;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (lamX_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      ic_v.re = (lamX_re * lamY_re + v_im * lamX_im) / brm;
      ic_v.im = (v_im * lamY_re - lamX_re * lamX_im) / brm;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      ic_v.re = (bim * lamX_re + v_im) / lamX_im;
      ic_v.im = (bim * v_im - lamX_re) / lamX_im;
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

  emlrtPushRtStackR2012b(&jb_emlrtRSI, emlrtRootTLSGlobal);
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
  jc_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  jc_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, jc_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax) * (1560.0 * muDoubleScalarSin(Ttrignew) +
    1860.0);
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  ec_const_mass.re = const_mass * xAndLambda_data[3];
  ec_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax) * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax) * (1560.0 * muDoubleScalarSin(Ttrignew) +
    1860.0)), ec_const_mass);
  jc_z.re = xAndLambda_data[2] + 50.0;
  jc_z.im = 0.0;
  v = b_mpower(jc_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * ec_v_re + ai * ec_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax) * xAndLambda_data[10] * (const_g *
    const_mass + muDoubleScalarSin(const_alfamax) * (1560.0 * muDoubleScalarSin
    (Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(const_bankmax) * 0.0 * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax) * (1560.0 * muDoubleScalarSin(Ttrignew) +
    1860.0));
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        ec_const_mass_re = 0.5;
      } else {
        ec_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        ec_const_mass_im = 0.5;
      } else {
        ec_const_mass_im = -0.5;
      }

      const_mass_re = (ar * ec_const_mass_re + ai * ec_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  emlrtPopRtStackR2012b(&jb_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = 1.5707963267948966;
    *alfatrigSave = 1.5707963267948966;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&kb_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = 3.1416 / (2.0 * const_bankmax);
  b_asin(&hamiltonian);
  banktrig = -hamiltonian;
  emlrtPopRtStackR2012b(&kb_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(-hamiltonian) || muDoubleScalarIsInf(-hamiltonian)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  /*  Coefficients */
  dc0 = gam;
  b_cos(&dc0);
  a = gam;
  b_cos(&a);
  kc_z.re = xAndLambda_data[2] + 50.0;
  kc_z.im = 0.0;
  dc1 = b_mpower(kc_z);
  v_re = xAndLambda_data[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda_data[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda_data[9] * muDoubleScalarCos(const_alfamax));
  ai = -(0.0 * muDoubleScalarCos(const_alfamax));
  if (ai == 0.0) {
    Ttrignew = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    Ttrignew = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    Ttrignew = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = muDoubleScalarSin(const_alfamax) * (1560.0 * xAndLambda_data[11]) *
    muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig));
  ai = muDoubleScalarSin(const_alfamax) * 0.0 * muDoubleScalarCos(const_bankmax *
    muDoubleScalarSin(banktrig));
  hamiltonian = const_mass * xAndLambda_data[3];
  lamX_im = const_mass * 0.0;
  if (lamX_im == 0.0) {
    if (ai == 0.0) {
      const_C1_re = ar / hamiltonian;
      lamY_im = 0.0;
    } else if (ar == 0.0) {
      const_C1_re = 0.0;
      lamY_im = ai / hamiltonian;
    } else {
      const_C1_re = ar / hamiltonian;
      lamY_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      const_C1_re = ai / lamX_im;
      lamY_im = 0.0;
    } else if (ai == 0.0) {
      const_C1_re = 0.0;
      lamY_im = -(ar / lamX_im);
    } else {
      const_C1_re = ai / lamX_im;
      lamY_im = -(ar / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > lamX_im) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      const_C1_re = (ar + bim * ai) / lamX_im;
      lamY_im = (ai - bim * ar) / lamX_im;
    } else if (lamX_im == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      const_C1_re = (ar * lamY_re + ai * -0.5) / 0.0;
      lamY_im = (ai * lamY_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      const_C1_re = (bim * ar + ai) / lamX_im;
      lamY_im = (bim * ai - ar) / lamX_im;
    }
  }

  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * a.re - const_mass_im * a.im;
  const_mass_im = hamiltonian * a.im + const_mass_im * a.re;
  ar = muDoubleScalarSin(const_alfamax) * (1560.0 * xAndLambda_data[10]) *
    muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig));
  ai = muDoubleScalarSin(const_alfamax) * 0.0 * muDoubleScalarSin(const_bankmax *
    muDoubleScalarSin(banktrig));
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      lamX_re = ar / const_mass_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      lamX_re = 0.0;
      hamiltonian = ai / const_mass_re;
    } else {
      lamX_re = ar / const_mass_re;
      hamiltonian = ai / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      lamX_re = ai / const_mass_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      lamX_re = 0.0;
      hamiltonian = -(ar / const_mass_im);
    } else {
      lamX_re = ai / const_mass_im;
      hamiltonian = -(ar / const_mass_im);
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      lamX_im = const_mass_re + bim * const_mass_im;
      lamX_re = (ar + bim * ai) / lamX_im;
      hamiltonian = (ai - bim * ar) / lamX_im;
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      lamX_re = (ar * lamY_re + ai * lamX_im) / brm;
      hamiltonian = (ai * lamY_re - ar * lamX_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      lamX_im = const_mass_im + bim * const_mass_re;
      lamX_re = (bim * ar + ai) / lamX_im;
      hamiltonian = (bim * ai - ar) / lamX_im;
    }
  }

  Ttrignew = (Ttrignew - const_C1_re) - lamX_re;
  const_C1_im = (const_C1_im - lamY_im) - hamiltonian;
  lamX_re = v_re * Ttrignew - v_im * const_C1_im;
  v_im = v_re * const_C1_im + v_im * Ttrignew;
  hamiltonian = 8112.0 * dc0.re;
  lamX_im = 8112.0 * dc0.im;
  if (lamX_im == 0.0) {
    if (v_im == 0.0) {
      kc_v.re = lamX_re / hamiltonian;
      kc_v.im = 0.0;
    } else if (lamX_re == 0.0) {
      kc_v.re = 0.0;
      kc_v.im = v_im / hamiltonian;
    } else {
      kc_v.re = lamX_re / hamiltonian;
      kc_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (lamX_re == 0.0) {
      kc_v.re = v_im / lamX_im;
      kc_v.im = 0.0;
    } else if (v_im == 0.0) {
      kc_v.re = 0.0;
      kc_v.im = -(lamX_re / lamX_im);
    } else {
      kc_v.re = v_im / lamX_im;
      kc_v.im = -(lamX_re / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(lamX_im);
    if (brm > bim) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      kc_v.re = (lamX_re + bim * v_im) / lamX_im;
      kc_v.im = (v_im - bim * lamX_re) / lamX_im;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (lamX_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      kc_v.re = (lamX_re * lamY_re + v_im * lamX_im) / brm;
      kc_v.im = (v_im * lamY_re - lamX_re * lamX_im) / brm;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      kc_v.re = (bim * lamX_re + v_im) / lamX_im;
      kc_v.im = (bim * v_im - lamX_re) / lamX_im;
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
  lc_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  lc_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, lc_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax) * (1560.0 * muDoubleScalarSin(Ttrignew) +
    1860.0);
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  fc_const_mass.re = const_mass * xAndLambda_data[3];
  fc_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig)) *
                (const_g * const_mass + muDoubleScalarSin(const_alfamax) *
                 (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0)), fc_const_mass);
  lc_z.re = xAndLambda_data[2] + 50.0;
  lc_z.im = 0.0;
  v = b_mpower(lc_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * fc_v_re + ai * fc_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda_data[10] * (const_g * const_mass + muDoubleScalarSin
    (const_alfamax) * (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (const_g * const_mass + muDoubleScalarSin(const_alfamax) * (1560.0 *
      muDoubleScalarSin(Ttrignew) + 1860.0));
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        fc_const_mass_re = 0.5;
      } else {
        fc_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        fc_const_mass_im = 0.5;
      } else {
        fc_const_mass_im = -0.5;
      }

      const_mass_re = (ar * fc_const_mass_re + ai * fc_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  emlrtPopRtStackR2012b(&lb_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = 1.5707963267948966;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&mb_emlrtRSI, emlrtRootTLSGlobal);
  banktrig = 3.1416 / (2.0 * const_bankmax);
  b_asin(&banktrig);
  emlrtPopRtStackR2012b(&mb_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(banktrig) || muDoubleScalarIsInf(banktrig)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  /*  Coefficients */
  dc0 = gam;
  b_cos(&dc0);
  a = gam;
  b_cos(&a);
  mc_z.re = xAndLambda_data[2] + 50.0;
  mc_z.im = 0.0;
  dc1 = b_mpower(mc_z);
  v_re = xAndLambda_data[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda_data[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda_data[9] * muDoubleScalarCos(const_alfamax));
  ai = -(0.0 * muDoubleScalarCos(const_alfamax));
  if (ai == 0.0) {
    Ttrignew = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    Ttrignew = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    Ttrignew = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = muDoubleScalarSin(const_alfamax) * (1560.0 * xAndLambda_data[11]) *
    muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig));
  ai = muDoubleScalarSin(const_alfamax) * 0.0 * muDoubleScalarCos(const_bankmax *
    muDoubleScalarSin(banktrig));
  hamiltonian = const_mass * xAndLambda_data[3];
  lamX_im = const_mass * 0.0;
  if (lamX_im == 0.0) {
    if (ai == 0.0) {
      const_C1_re = ar / hamiltonian;
      lamY_im = 0.0;
    } else if (ar == 0.0) {
      const_C1_re = 0.0;
      lamY_im = ai / hamiltonian;
    } else {
      const_C1_re = ar / hamiltonian;
      lamY_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      const_C1_re = ai / lamX_im;
      lamY_im = 0.0;
    } else if (ai == 0.0) {
      const_C1_re = 0.0;
      lamY_im = -(ar / lamX_im);
    } else {
      const_C1_re = ai / lamX_im;
      lamY_im = -(ar / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > lamX_im) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      const_C1_re = (ar + bim * ai) / lamX_im;
      lamY_im = (ai - bim * ar) / lamX_im;
    } else if (lamX_im == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      const_C1_re = (ar * lamY_re + ai * -0.5) / 0.0;
      lamY_im = (ai * lamY_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      const_C1_re = (bim * ar + ai) / lamX_im;
      lamY_im = (bim * ai - ar) / lamX_im;
    }
  }

  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * a.re - const_mass_im * a.im;
  const_mass_im = hamiltonian * a.im + const_mass_im * a.re;
  ar = muDoubleScalarSin(const_alfamax) * (1560.0 * xAndLambda_data[10]) *
    muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig));
  ai = muDoubleScalarSin(const_alfamax) * 0.0 * muDoubleScalarSin(const_bankmax *
    muDoubleScalarSin(banktrig));
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      lamX_re = ar / const_mass_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      lamX_re = 0.0;
      hamiltonian = ai / const_mass_re;
    } else {
      lamX_re = ar / const_mass_re;
      hamiltonian = ai / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      lamX_re = ai / const_mass_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      lamX_re = 0.0;
      hamiltonian = -(ar / const_mass_im);
    } else {
      lamX_re = ai / const_mass_im;
      hamiltonian = -(ar / const_mass_im);
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      lamX_im = const_mass_re + bim * const_mass_im;
      lamX_re = (ar + bim * ai) / lamX_im;
      hamiltonian = (ai - bim * ar) / lamX_im;
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      lamX_re = (ar * lamY_re + ai * lamX_im) / brm;
      hamiltonian = (ai * lamY_re - ar * lamX_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      lamX_im = const_mass_im + bim * const_mass_re;
      lamX_re = (bim * ar + ai) / lamX_im;
      hamiltonian = (bim * ai - ar) / lamX_im;
    }
  }

  Ttrignew = (Ttrignew - const_C1_re) - lamX_re;
  const_C1_im = (const_C1_im - lamY_im) - hamiltonian;
  lamX_re = v_re * Ttrignew - v_im * const_C1_im;
  v_im = v_re * const_C1_im + v_im * Ttrignew;
  hamiltonian = 8112.0 * dc0.re;
  lamX_im = 8112.0 * dc0.im;
  if (lamX_im == 0.0) {
    if (v_im == 0.0) {
      mc_v.re = lamX_re / hamiltonian;
      mc_v.im = 0.0;
    } else if (lamX_re == 0.0) {
      mc_v.re = 0.0;
      mc_v.im = v_im / hamiltonian;
    } else {
      mc_v.re = lamX_re / hamiltonian;
      mc_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (lamX_re == 0.0) {
      mc_v.re = v_im / lamX_im;
      mc_v.im = 0.0;
    } else if (v_im == 0.0) {
      mc_v.re = 0.0;
      mc_v.im = -(lamX_re / lamX_im);
    } else {
      mc_v.re = v_im / lamX_im;
      mc_v.im = -(lamX_re / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(lamX_im);
    if (brm > bim) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      mc_v.re = (lamX_re + bim * v_im) / lamX_im;
      mc_v.im = (v_im - bim * lamX_re) / lamX_im;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (lamX_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      mc_v.re = (lamX_re * lamY_re + v_im * lamX_im) / brm;
      mc_v.im = (v_im * lamY_re - lamX_re * lamX_im) / brm;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      mc_v.re = (bim * lamX_re + v_im) / lamX_im;
      mc_v.im = (bim * v_im - lamX_re) / lamX_im;
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

  emlrtPushRtStackR2012b(&nb_emlrtRSI, emlrtRootTLSGlobal);
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
  nc_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  nc_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, nc_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax) * (1560.0 * muDoubleScalarSin(Ttrignew) +
    1860.0);
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  gc_const_mass.re = const_mass * xAndLambda_data[3];
  gc_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig)) *
                (const_g * const_mass + muDoubleScalarSin(const_alfamax) *
                 (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0)), gc_const_mass);
  nc_z.re = xAndLambda_data[2] + 50.0;
  nc_z.im = 0.0;
  v = b_mpower(nc_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * gc_v_re + ai * gc_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda_data[10] * (const_g * const_mass + muDoubleScalarSin
    (const_alfamax) * (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (const_g * const_mass + muDoubleScalarSin(const_alfamax) * (1560.0 *
      muDoubleScalarSin(Ttrignew) + 1860.0));
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        gc_const_mass_re = 0.5;
      } else {
        gc_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        gc_const_mass_im = 0.5;
      } else {
        gc_const_mass_im = -0.5;
      }

      const_mass_re = (ar * gc_const_mass_re + ai * gc_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  emlrtPopRtStackR2012b(&nb_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = 1.5707963267948966;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(-const_bankmax);
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(-const_bankmax);
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(-(2.0 * const_bankmax));
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(-(2.0 * const_bankmax));
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      hamiltonian = const_g_re / dc0.re;
      const_g_im = 0.0;
    } else if (const_g_re == 0.0) {
      hamiltonian = 0.0;
      const_g_im /= dc0.re;
    } else {
      hamiltonian = const_g_re / dc0.re;
      const_g_im /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = 0.0;
    } else if (const_g_im == 0.0) {
      hamiltonian = 0.0;
      const_g_im = -(const_g_re / dc0.im);
    } else {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = -(const_g_re / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      hamiltonian = (const_g_re + bim * const_g_im) / lamX_im;
      const_g_im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      hamiltonian = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      const_g_im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      hamiltonian = (bim * const_g_re + const_g_im) / lamX_im;
      const_g_im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -const_g_im;
  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  oc_z.re = xAndLambda_data[2] + 50.0;
  oc_z.im = 0.0;
  dc1 = b_mpower(oc_z);
  v_re = xAndLambda_data[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda_data[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda_data[9] * muDoubleScalarCos(const_alfamax *
          muDoubleScalarSin(alfatrig)));
  ai = -(0.0 * muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)));
  if (ai == 0.0) {
    Ttrignew = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    Ttrignew = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    Ttrignew = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    xAndLambda_data[11]) * muDoubleScalarCos(-const_bankmax);
  ai = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarCos(-const_bankmax);
  hamiltonian = const_mass * xAndLambda_data[3];
  lamX_im = const_mass * 0.0;
  if (lamX_im == 0.0) {
    if (ai == 0.0) {
      const_C1_re = ar / hamiltonian;
      lamY_im = 0.0;
    } else if (ar == 0.0) {
      const_C1_re = 0.0;
      lamY_im = ai / hamiltonian;
    } else {
      const_C1_re = ar / hamiltonian;
      lamY_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      const_C1_re = ai / lamX_im;
      lamY_im = 0.0;
    } else if (ai == 0.0) {
      const_C1_re = 0.0;
      lamY_im = -(ar / lamX_im);
    } else {
      const_C1_re = ai / lamX_im;
      lamY_im = -(ar / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > lamX_im) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      const_C1_re = (ar + bim * ai) / lamX_im;
      lamY_im = (ai - bim * ar) / lamX_im;
    } else if (lamX_im == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      const_C1_re = (ar * lamY_re + ai * -0.5) / 0.0;
      lamY_im = (ai * lamY_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      const_C1_re = (bim * ar + ai) / lamX_im;
      lamY_im = (bim * ai - ar) / lamX_im;
    }
  }

  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * a.re - const_mass_im * a.im;
  const_mass_im = hamiltonian * a.im + const_mass_im * a.re;
  ar = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    xAndLambda_data[10]) * muDoubleScalarSin(-const_bankmax);
  ai = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarSin(-const_bankmax);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      lamX_re = ar / const_mass_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      lamX_re = 0.0;
      hamiltonian = ai / const_mass_re;
    } else {
      lamX_re = ar / const_mass_re;
      hamiltonian = ai / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      lamX_re = ai / const_mass_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      lamX_re = 0.0;
      hamiltonian = -(ar / const_mass_im);
    } else {
      lamX_re = ai / const_mass_im;
      hamiltonian = -(ar / const_mass_im);
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      lamX_im = const_mass_re + bim * const_mass_im;
      lamX_re = (ar + bim * ai) / lamX_im;
      hamiltonian = (ai - bim * ar) / lamX_im;
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      lamX_re = (ar * lamY_re + ai * lamX_im) / brm;
      hamiltonian = (ai * lamY_re - ar * lamX_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      lamX_im = const_mass_im + bim * const_mass_re;
      lamX_re = (bim * ar + ai) / lamX_im;
      hamiltonian = (bim * ai - ar) / lamX_im;
    }
  }

  Ttrignew = (Ttrignew - const_C1_re) - lamX_re;
  const_C1_im = (const_C1_im - lamY_im) - hamiltonian;
  lamX_re = v_re * Ttrignew - v_im * const_C1_im;
  v_im = v_re * const_C1_im + v_im * Ttrignew;
  hamiltonian = 8112.0 * dc0.re;
  lamX_im = 8112.0 * dc0.im;
  if (lamX_im == 0.0) {
    if (v_im == 0.0) {
      oc_v.re = lamX_re / hamiltonian;
      oc_v.im = 0.0;
    } else if (lamX_re == 0.0) {
      oc_v.re = 0.0;
      oc_v.im = v_im / hamiltonian;
    } else {
      oc_v.re = lamX_re / hamiltonian;
      oc_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (lamX_re == 0.0) {
      oc_v.re = v_im / lamX_im;
      oc_v.im = 0.0;
    } else if (v_im == 0.0) {
      oc_v.re = 0.0;
      oc_v.im = -(lamX_re / lamX_im);
    } else {
      oc_v.re = v_im / lamX_im;
      oc_v.im = -(lamX_re / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(lamX_im);
    if (brm > bim) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      oc_v.re = (lamX_re + bim * v_im) / lamX_im;
      oc_v.im = (v_im - bim * lamX_re) / lamX_im;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (lamX_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      oc_v.re = (lamX_re * lamY_re + v_im * lamX_im) / brm;
      oc_v.im = (v_im * lamY_re - lamX_re * lamX_im) / brm;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      oc_v.re = (bim * lamX_re + v_im) / lamX_im;
      oc_v.im = (bim * v_im - lamX_re) / lamX_im;
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
  pc_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  pc_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, pc_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0);
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  hc_const_mass.re = const_mass * xAndLambda_data[3];
  hc_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(-const_bankmax) * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0)), hc_const_mass);
  pc_z.re = xAndLambda_data[2] + 50.0;
  pc_z.im = 0.0;
  v = b_mpower(pc_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * hc_v_re + ai * hc_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(-const_bankmax) * xAndLambda_data[10] * (const_g *
    const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(-const_bankmax) * 0.0 * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0));
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        hc_const_mass_re = 0.5;
      } else {
        hc_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        hc_const_mass_im = 0.5;
      } else {
        hc_const_mass_im = -0.5;
      }

      const_mass_re = (ar * hc_const_mass_re + ai * hc_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  emlrtPopRtStackR2012b(&ob_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = -1.5707963267948966;
    *alfatrigSave = alfatrig;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(const_bankmax);
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(const_bankmax);
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(2.0 * const_bankmax);
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(2.0 * const_bankmax);
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      hamiltonian = const_g_re / dc0.re;
      const_g_im = 0.0;
    } else if (const_g_re == 0.0) {
      hamiltonian = 0.0;
      const_g_im /= dc0.re;
    } else {
      hamiltonian = const_g_re / dc0.re;
      const_g_im /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = 0.0;
    } else if (const_g_im == 0.0) {
      hamiltonian = 0.0;
      const_g_im = -(const_g_re / dc0.im);
    } else {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = -(const_g_re / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      hamiltonian = (const_g_re + bim * const_g_im) / lamX_im;
      const_g_im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      hamiltonian = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      const_g_im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      hamiltonian = (bim * const_g_re + const_g_im) / lamX_im;
      const_g_im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -const_g_im;
  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  qc_z.re = xAndLambda_data[2] + 50.0;
  qc_z.im = 0.0;
  dc1 = b_mpower(qc_z);
  v_re = xAndLambda_data[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda_data[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda_data[9] * muDoubleScalarCos(const_alfamax *
          muDoubleScalarSin(alfatrig)));
  ai = -(0.0 * muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)));
  if (ai == 0.0) {
    Ttrignew = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    Ttrignew = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    Ttrignew = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    xAndLambda_data[11]) * muDoubleScalarCos(const_bankmax);
  ai = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarCos(const_bankmax);
  hamiltonian = const_mass * xAndLambda_data[3];
  lamX_im = const_mass * 0.0;
  if (lamX_im == 0.0) {
    if (ai == 0.0) {
      const_C1_re = ar / hamiltonian;
      lamY_im = 0.0;
    } else if (ar == 0.0) {
      const_C1_re = 0.0;
      lamY_im = ai / hamiltonian;
    } else {
      const_C1_re = ar / hamiltonian;
      lamY_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      const_C1_re = ai / lamX_im;
      lamY_im = 0.0;
    } else if (ai == 0.0) {
      const_C1_re = 0.0;
      lamY_im = -(ar / lamX_im);
    } else {
      const_C1_re = ai / lamX_im;
      lamY_im = -(ar / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > lamX_im) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      const_C1_re = (ar + bim * ai) / lamX_im;
      lamY_im = (ai - bim * ar) / lamX_im;
    } else if (lamX_im == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      const_C1_re = (ar * lamY_re + ai * -0.5) / 0.0;
      lamY_im = (ai * lamY_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      const_C1_re = (bim * ar + ai) / lamX_im;
      lamY_im = (bim * ai - ar) / lamX_im;
    }
  }

  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * a.re - const_mass_im * a.im;
  const_mass_im = hamiltonian * a.im + const_mass_im * a.re;
  ar = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    xAndLambda_data[10]) * muDoubleScalarSin(const_bankmax);
  ai = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarSin(const_bankmax);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      lamX_re = ar / const_mass_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      lamX_re = 0.0;
      hamiltonian = ai / const_mass_re;
    } else {
      lamX_re = ar / const_mass_re;
      hamiltonian = ai / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      lamX_re = ai / const_mass_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      lamX_re = 0.0;
      hamiltonian = -(ar / const_mass_im);
    } else {
      lamX_re = ai / const_mass_im;
      hamiltonian = -(ar / const_mass_im);
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      lamX_im = const_mass_re + bim * const_mass_im;
      lamX_re = (ar + bim * ai) / lamX_im;
      hamiltonian = (ai - bim * ar) / lamX_im;
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      lamX_re = (ar * lamY_re + ai * lamX_im) / brm;
      hamiltonian = (ai * lamY_re - ar * lamX_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      lamX_im = const_mass_im + bim * const_mass_re;
      lamX_re = (bim * ar + ai) / lamX_im;
      hamiltonian = (bim * ai - ar) / lamX_im;
    }
  }

  Ttrignew = (Ttrignew - const_C1_re) - lamX_re;
  const_C1_im = (const_C1_im - lamY_im) - hamiltonian;
  lamX_re = v_re * Ttrignew - v_im * const_C1_im;
  v_im = v_re * const_C1_im + v_im * Ttrignew;
  hamiltonian = 8112.0 * dc0.re;
  lamX_im = 8112.0 * dc0.im;
  if (lamX_im == 0.0) {
    if (v_im == 0.0) {
      qc_v.re = lamX_re / hamiltonian;
      qc_v.im = 0.0;
    } else if (lamX_re == 0.0) {
      qc_v.re = 0.0;
      qc_v.im = v_im / hamiltonian;
    } else {
      qc_v.re = lamX_re / hamiltonian;
      qc_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (lamX_re == 0.0) {
      qc_v.re = v_im / lamX_im;
      qc_v.im = 0.0;
    } else if (v_im == 0.0) {
      qc_v.re = 0.0;
      qc_v.im = -(lamX_re / lamX_im);
    } else {
      qc_v.re = v_im / lamX_im;
      qc_v.im = -(lamX_re / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(lamX_im);
    if (brm > bim) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      qc_v.re = (lamX_re + bim * v_im) / lamX_im;
      qc_v.im = (v_im - bim * lamX_re) / lamX_im;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (lamX_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      qc_v.re = (lamX_re * lamY_re + v_im * lamX_im) / brm;
      qc_v.im = (v_im * lamY_re - lamX_re * lamX_im) / brm;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      qc_v.re = (bim * lamX_re + v_im) / lamX_im;
      qc_v.im = (bim * v_im - lamX_re) / lamX_im;
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

  emlrtPushRtStackR2012b(&pb_emlrtRSI, emlrtRootTLSGlobal);
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
  rc_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  rc_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, rc_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0);
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  ic_const_mass.re = const_mass * xAndLambda_data[3];
  ic_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax) * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0)), ic_const_mass);
  rc_z.re = xAndLambda_data[2] + 50.0;
  rc_z.im = 0.0;
  v = b_mpower(rc_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * ic_v_re + ai * ic_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax) * xAndLambda_data[10] * (const_g *
    const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(const_bankmax) * 0.0 * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0));
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        ic_const_mass_re = 0.5;
      } else {
        ic_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        ic_const_mass_im = 0.5;
      } else {
        ic_const_mass_im = -0.5;
      }

      const_mass_re = (ar * ic_const_mass_re + ai * ic_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  emlrtPopRtStackR2012b(&pb_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = 1.5707963267948966;
    *alfatrigSave = alfatrig;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&qb_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = 3.1416 / (2.0 * const_bankmax);
  b_asin(&hamiltonian);
  banktrig = -hamiltonian;
  emlrtPopRtStackR2012b(&qb_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(-hamiltonian) || muDoubleScalarIsInf(-hamiltonian)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(2.0 * const_bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(2.0 * const_bankmax * muDoubleScalarSin
    (banktrig));
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      hamiltonian = const_g_re / dc0.re;
      const_g_im = 0.0;
    } else if (const_g_re == 0.0) {
      hamiltonian = 0.0;
      const_g_im /= dc0.re;
    } else {
      hamiltonian = const_g_re / dc0.re;
      const_g_im /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = 0.0;
    } else if (const_g_im == 0.0) {
      hamiltonian = 0.0;
      const_g_im = -(const_g_re / dc0.im);
    } else {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = -(const_g_re / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      hamiltonian = (const_g_re + bim * const_g_im) / lamX_im;
      const_g_im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      hamiltonian = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      const_g_im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      hamiltonian = (bim * const_g_re + const_g_im) / lamX_im;
      const_g_im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -const_g_im;
  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  sc_z.re = xAndLambda_data[2] + 50.0;
  sc_z.im = 0.0;
  dc1 = b_mpower(sc_z);
  v_re = xAndLambda_data[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda_data[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda_data[9] * muDoubleScalarCos(const_alfamax *
          muDoubleScalarSin(alfatrig)));
  ai = -(0.0 * muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)));
  if (ai == 0.0) {
    Ttrignew = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    Ttrignew = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    Ttrignew = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    xAndLambda_data[11]) * muDoubleScalarCos(const_bankmax * muDoubleScalarSin
    (banktrig));
  ai = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig));
  hamiltonian = const_mass * xAndLambda_data[3];
  lamX_im = const_mass * 0.0;
  if (lamX_im == 0.0) {
    if (ai == 0.0) {
      const_C1_re = ar / hamiltonian;
      lamY_im = 0.0;
    } else if (ar == 0.0) {
      const_C1_re = 0.0;
      lamY_im = ai / hamiltonian;
    } else {
      const_C1_re = ar / hamiltonian;
      lamY_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      const_C1_re = ai / lamX_im;
      lamY_im = 0.0;
    } else if (ai == 0.0) {
      const_C1_re = 0.0;
      lamY_im = -(ar / lamX_im);
    } else {
      const_C1_re = ai / lamX_im;
      lamY_im = -(ar / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > lamX_im) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      const_C1_re = (ar + bim * ai) / lamX_im;
      lamY_im = (ai - bim * ar) / lamX_im;
    } else if (lamX_im == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      const_C1_re = (ar * lamY_re + ai * -0.5) / 0.0;
      lamY_im = (ai * lamY_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      const_C1_re = (bim * ar + ai) / lamX_im;
      lamY_im = (bim * ai - ar) / lamX_im;
    }
  }

  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * a.re - const_mass_im * a.im;
  const_mass_im = hamiltonian * a.im + const_mass_im * a.re;
  ar = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    xAndLambda_data[10]) * muDoubleScalarSin(const_bankmax * muDoubleScalarSin
    (banktrig));
  ai = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig));
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      lamX_re = ar / const_mass_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      lamX_re = 0.0;
      hamiltonian = ai / const_mass_re;
    } else {
      lamX_re = ar / const_mass_re;
      hamiltonian = ai / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      lamX_re = ai / const_mass_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      lamX_re = 0.0;
      hamiltonian = -(ar / const_mass_im);
    } else {
      lamX_re = ai / const_mass_im;
      hamiltonian = -(ar / const_mass_im);
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      lamX_im = const_mass_re + bim * const_mass_im;
      lamX_re = (ar + bim * ai) / lamX_im;
      hamiltonian = (ai - bim * ar) / lamX_im;
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      lamX_re = (ar * lamY_re + ai * lamX_im) / brm;
      hamiltonian = (ai * lamY_re - ar * lamX_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      lamX_im = const_mass_im + bim * const_mass_re;
      lamX_re = (bim * ar + ai) / lamX_im;
      hamiltonian = (bim * ai - ar) / lamX_im;
    }
  }

  Ttrignew = (Ttrignew - const_C1_re) - lamX_re;
  const_C1_im = (const_C1_im - lamY_im) - hamiltonian;
  lamX_re = v_re * Ttrignew - v_im * const_C1_im;
  v_im = v_re * const_C1_im + v_im * Ttrignew;
  hamiltonian = 8112.0 * dc0.re;
  lamX_im = 8112.0 * dc0.im;
  if (lamX_im == 0.0) {
    if (v_im == 0.0) {
      sc_v.re = lamX_re / hamiltonian;
      sc_v.im = 0.0;
    } else if (lamX_re == 0.0) {
      sc_v.re = 0.0;
      sc_v.im = v_im / hamiltonian;
    } else {
      sc_v.re = lamX_re / hamiltonian;
      sc_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (lamX_re == 0.0) {
      sc_v.re = v_im / lamX_im;
      sc_v.im = 0.0;
    } else if (v_im == 0.0) {
      sc_v.re = 0.0;
      sc_v.im = -(lamX_re / lamX_im);
    } else {
      sc_v.re = v_im / lamX_im;
      sc_v.im = -(lamX_re / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(lamX_im);
    if (brm > bim) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      sc_v.re = (lamX_re + bim * v_im) / lamX_im;
      sc_v.im = (v_im - bim * lamX_re) / lamX_im;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (lamX_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      sc_v.re = (lamX_re * lamY_re + v_im * lamX_im) / brm;
      sc_v.im = (v_im * lamY_re - lamX_re * lamX_im) / brm;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      sc_v.re = (bim * lamX_re + v_im) / lamX_im;
      sc_v.im = (bim * v_im - lamX_re) / lamX_im;
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
  tc_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  tc_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, tc_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0);
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  jc_const_mass.re = const_mass * xAndLambda_data[3];
  jc_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig)) *
                (const_g * const_mass + muDoubleScalarSin(const_alfamax *
    muDoubleScalarSin(alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) +
    1860.0)), jc_const_mass);
  tc_z.re = xAndLambda_data[2] + 50.0;
  tc_z.im = 0.0;
  v = b_mpower(tc_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * jc_v_re + ai * jc_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda_data[10] * (const_g * const_mass + muDoubleScalarSin
    (const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 * muDoubleScalarSin
    (Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (const_g * const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin
      (alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0));
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        jc_const_mass_re = 0.5;
      } else {
        jc_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        jc_const_mass_im = 0.5;
      } else {
        jc_const_mass_im = -0.5;
      }

      const_mass_re = (ar * jc_const_mass_re + ai * jc_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  emlrtPopRtStackR2012b(&rb_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&sb_emlrtRSI, emlrtRootTLSGlobal);
  banktrig = 3.1416 / (2.0 * const_bankmax);
  b_asin(&banktrig);
  emlrtPopRtStackR2012b(&sb_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(banktrig) || muDoubleScalarIsInf(banktrig)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(2.0 * const_bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(2.0 * const_bankmax * muDoubleScalarSin
    (banktrig));
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      hamiltonian = const_g_re / dc0.re;
      const_g_im = 0.0;
    } else if (const_g_re == 0.0) {
      hamiltonian = 0.0;
      const_g_im /= dc0.re;
    } else {
      hamiltonian = const_g_re / dc0.re;
      const_g_im /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = 0.0;
    } else if (const_g_im == 0.0) {
      hamiltonian = 0.0;
      const_g_im = -(const_g_re / dc0.im);
    } else {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = -(const_g_re / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      hamiltonian = (const_g_re + bim * const_g_im) / lamX_im;
      const_g_im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      hamiltonian = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      const_g_im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      hamiltonian = (bim * const_g_re + const_g_im) / lamX_im;
      const_g_im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -const_g_im;
  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  uc_z.re = xAndLambda_data[2] + 50.0;
  uc_z.im = 0.0;
  dc1 = b_mpower(uc_z);
  v_re = xAndLambda_data[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda_data[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda_data[9] * muDoubleScalarCos(const_alfamax *
          muDoubleScalarSin(alfatrig)));
  ai = -(0.0 * muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)));
  if (ai == 0.0) {
    Ttrignew = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    Ttrignew = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    Ttrignew = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    xAndLambda_data[11]) * muDoubleScalarCos(const_bankmax * muDoubleScalarSin
    (banktrig));
  ai = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig));
  hamiltonian = const_mass * xAndLambda_data[3];
  lamX_im = const_mass * 0.0;
  if (lamX_im == 0.0) {
    if (ai == 0.0) {
      const_C1_re = ar / hamiltonian;
      lamY_im = 0.0;
    } else if (ar == 0.0) {
      const_C1_re = 0.0;
      lamY_im = ai / hamiltonian;
    } else {
      const_C1_re = ar / hamiltonian;
      lamY_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      const_C1_re = ai / lamX_im;
      lamY_im = 0.0;
    } else if (ai == 0.0) {
      const_C1_re = 0.0;
      lamY_im = -(ar / lamX_im);
    } else {
      const_C1_re = ai / lamX_im;
      lamY_im = -(ar / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > lamX_im) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      const_C1_re = (ar + bim * ai) / lamX_im;
      lamY_im = (ai - bim * ar) / lamX_im;
    } else if (lamX_im == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      const_C1_re = (ar * lamY_re + ai * -0.5) / 0.0;
      lamY_im = (ai * lamY_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      const_C1_re = (bim * ar + ai) / lamX_im;
      lamY_im = (bim * ai - ar) / lamX_im;
    }
  }

  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * a.re - const_mass_im * a.im;
  const_mass_im = hamiltonian * a.im + const_mass_im * a.re;
  ar = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    xAndLambda_data[10]) * muDoubleScalarSin(const_bankmax * muDoubleScalarSin
    (banktrig));
  ai = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig));
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      lamX_re = ar / const_mass_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      lamX_re = 0.0;
      hamiltonian = ai / const_mass_re;
    } else {
      lamX_re = ar / const_mass_re;
      hamiltonian = ai / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      lamX_re = ai / const_mass_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      lamX_re = 0.0;
      hamiltonian = -(ar / const_mass_im);
    } else {
      lamX_re = ai / const_mass_im;
      hamiltonian = -(ar / const_mass_im);
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      lamX_im = const_mass_re + bim * const_mass_im;
      lamX_re = (ar + bim * ai) / lamX_im;
      hamiltonian = (ai - bim * ar) / lamX_im;
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      lamX_re = (ar * lamY_re + ai * lamX_im) / brm;
      hamiltonian = (ai * lamY_re - ar * lamX_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      lamX_im = const_mass_im + bim * const_mass_re;
      lamX_re = (bim * ar + ai) / lamX_im;
      hamiltonian = (bim * ai - ar) / lamX_im;
    }
  }

  Ttrignew = (Ttrignew - const_C1_re) - lamX_re;
  const_C1_im = (const_C1_im - lamY_im) - hamiltonian;
  lamX_re = v_re * Ttrignew - v_im * const_C1_im;
  v_im = v_re * const_C1_im + v_im * Ttrignew;
  hamiltonian = 8112.0 * dc0.re;
  lamX_im = 8112.0 * dc0.im;
  if (lamX_im == 0.0) {
    if (v_im == 0.0) {
      uc_v.re = lamX_re / hamiltonian;
      uc_v.im = 0.0;
    } else if (lamX_re == 0.0) {
      uc_v.re = 0.0;
      uc_v.im = v_im / hamiltonian;
    } else {
      uc_v.re = lamX_re / hamiltonian;
      uc_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (lamX_re == 0.0) {
      uc_v.re = v_im / lamX_im;
      uc_v.im = 0.0;
    } else if (v_im == 0.0) {
      uc_v.re = 0.0;
      uc_v.im = -(lamX_re / lamX_im);
    } else {
      uc_v.re = v_im / lamX_im;
      uc_v.im = -(lamX_re / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(lamX_im);
    if (brm > bim) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      uc_v.re = (lamX_re + bim * v_im) / lamX_im;
      uc_v.im = (v_im - bim * lamX_re) / lamX_im;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (lamX_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      uc_v.re = (lamX_re * lamY_re + v_im * lamX_im) / brm;
      uc_v.im = (v_im * lamY_re - lamX_re * lamX_im) / brm;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      uc_v.re = (bim * lamX_re + v_im) / lamX_im;
      uc_v.im = (bim * v_im - lamX_re) / lamX_im;
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

  emlrtPushRtStackR2012b(&tb_emlrtRSI, emlrtRootTLSGlobal);
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
  vc_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  vc_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, vc_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0);
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  kc_const_mass.re = const_mass * xAndLambda_data[3];
  kc_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig)) *
                (const_g * const_mass + muDoubleScalarSin(const_alfamax *
    muDoubleScalarSin(alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) +
    1860.0)), kc_const_mass);
  vc_z.re = xAndLambda_data[2] + 50.0;
  vc_z.im = 0.0;
  v = b_mpower(vc_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * kc_v_re + ai * kc_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda_data[10] * (const_g * const_mass + muDoubleScalarSin
    (const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 * muDoubleScalarSin
    (Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (const_g * const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin
      (alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0));
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        kc_const_mass_re = 0.5;
      } else {
        kc_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        kc_const_mass_im = 0.5;
      } else {
        kc_const_mass_im = -0.5;
      }

      const_mass_re = (ar * kc_const_mass_re + ai * kc_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  emlrtPopRtStackR2012b(&tb_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(-const_bankmax);
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(-const_bankmax);
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(-(2.0 * const_bankmax));
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(-(2.0 * const_bankmax));
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      hamiltonian = const_g_re / dc0.re;
      const_g_im = 0.0;
    } else if (const_g_re == 0.0) {
      hamiltonian = 0.0;
      const_g_im /= dc0.re;
    } else {
      hamiltonian = const_g_re / dc0.re;
      const_g_im /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = 0.0;
    } else if (const_g_im == 0.0) {
      hamiltonian = 0.0;
      const_g_im = -(const_g_re / dc0.im);
    } else {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = -(const_g_re / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      hamiltonian = (const_g_re + bim * const_g_im) / lamX_im;
      const_g_im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      hamiltonian = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      const_g_im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      hamiltonian = (bim * const_g_re + const_g_im) / lamX_im;
      const_g_im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -const_g_im;
  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  wc_z.re = xAndLambda_data[2] + 50.0;
  wc_z.im = 0.0;
  dc1 = b_mpower(wc_z);
  v_re = xAndLambda_data[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda_data[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda_data[9] * muDoubleScalarCos(const_alfamax *
          muDoubleScalarSin(alfatrig)));
  ai = -(0.0 * muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)));
  if (ai == 0.0) {
    Ttrignew = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    Ttrignew = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    Ttrignew = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    xAndLambda_data[11]) * muDoubleScalarCos(-const_bankmax);
  ai = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarCos(-const_bankmax);
  hamiltonian = const_mass * xAndLambda_data[3];
  lamX_im = const_mass * 0.0;
  if (lamX_im == 0.0) {
    if (ai == 0.0) {
      const_C1_re = ar / hamiltonian;
      lamY_im = 0.0;
    } else if (ar == 0.0) {
      const_C1_re = 0.0;
      lamY_im = ai / hamiltonian;
    } else {
      const_C1_re = ar / hamiltonian;
      lamY_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      const_C1_re = ai / lamX_im;
      lamY_im = 0.0;
    } else if (ai == 0.0) {
      const_C1_re = 0.0;
      lamY_im = -(ar / lamX_im);
    } else {
      const_C1_re = ai / lamX_im;
      lamY_im = -(ar / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > lamX_im) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      const_C1_re = (ar + bim * ai) / lamX_im;
      lamY_im = (ai - bim * ar) / lamX_im;
    } else if (lamX_im == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      const_C1_re = (ar * lamY_re + ai * -0.5) / 0.0;
      lamY_im = (ai * lamY_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      const_C1_re = (bim * ar + ai) / lamX_im;
      lamY_im = (bim * ai - ar) / lamX_im;
    }
  }

  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * a.re - const_mass_im * a.im;
  const_mass_im = hamiltonian * a.im + const_mass_im * a.re;
  ar = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    xAndLambda_data[10]) * muDoubleScalarSin(-const_bankmax);
  ai = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarSin(-const_bankmax);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      lamX_re = ar / const_mass_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      lamX_re = 0.0;
      hamiltonian = ai / const_mass_re;
    } else {
      lamX_re = ar / const_mass_re;
      hamiltonian = ai / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      lamX_re = ai / const_mass_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      lamX_re = 0.0;
      hamiltonian = -(ar / const_mass_im);
    } else {
      lamX_re = ai / const_mass_im;
      hamiltonian = -(ar / const_mass_im);
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      lamX_im = const_mass_re + bim * const_mass_im;
      lamX_re = (ar + bim * ai) / lamX_im;
      hamiltonian = (ai - bim * ar) / lamX_im;
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      lamX_re = (ar * lamY_re + ai * lamX_im) / brm;
      hamiltonian = (ai * lamY_re - ar * lamX_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      lamX_im = const_mass_im + bim * const_mass_re;
      lamX_re = (bim * ar + ai) / lamX_im;
      hamiltonian = (bim * ai - ar) / lamX_im;
    }
  }

  Ttrignew = (Ttrignew - const_C1_re) - lamX_re;
  const_C1_im = (const_C1_im - lamY_im) - hamiltonian;
  lamX_re = v_re * Ttrignew - v_im * const_C1_im;
  v_im = v_re * const_C1_im + v_im * Ttrignew;
  hamiltonian = 8112.0 * dc0.re;
  lamX_im = 8112.0 * dc0.im;
  if (lamX_im == 0.0) {
    if (v_im == 0.0) {
      wc_v.re = lamX_re / hamiltonian;
      wc_v.im = 0.0;
    } else if (lamX_re == 0.0) {
      wc_v.re = 0.0;
      wc_v.im = v_im / hamiltonian;
    } else {
      wc_v.re = lamX_re / hamiltonian;
      wc_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (lamX_re == 0.0) {
      wc_v.re = v_im / lamX_im;
      wc_v.im = 0.0;
    } else if (v_im == 0.0) {
      wc_v.re = 0.0;
      wc_v.im = -(lamX_re / lamX_im);
    } else {
      wc_v.re = v_im / lamX_im;
      wc_v.im = -(lamX_re / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(lamX_im);
    if (brm > bim) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      wc_v.re = (lamX_re + bim * v_im) / lamX_im;
      wc_v.im = (v_im - bim * lamX_re) / lamX_im;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (lamX_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      wc_v.re = (lamX_re * lamY_re + v_im * lamX_im) / brm;
      wc_v.im = (v_im * lamY_re - lamX_re * lamX_im) / brm;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      wc_v.re = (bim * lamX_re + v_im) / lamX_im;
      wc_v.im = (bim * v_im - lamX_re) / lamX_im;
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
  xc_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  xc_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, xc_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0);
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  lc_const_mass.re = const_mass * xAndLambda_data[3];
  lc_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(-const_bankmax) * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0)), lc_const_mass);
  xc_z.re = xAndLambda_data[2] + 50.0;
  xc_z.im = 0.0;
  v = b_mpower(xc_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * lc_v_re + ai * lc_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(-const_bankmax) * xAndLambda_data[10] * (const_g *
    const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(-const_bankmax) * 0.0 * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0));
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        lc_const_mass_re = 0.5;
      } else {
        lc_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        lc_const_mass_im = 0.5;
      } else {
        lc_const_mass_im = -0.5;
      }

      const_mass_re = (ar * lc_const_mass_re + ai * lc_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  emlrtPopRtStackR2012b(&ub_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = -1.5707963267948966;
    *alfatrigSave = alfatrig;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(const_bankmax);
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(const_bankmax);
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(2.0 * const_bankmax);
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(2.0 * const_bankmax);
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      hamiltonian = const_g_re / dc0.re;
      const_g_im = 0.0;
    } else if (const_g_re == 0.0) {
      hamiltonian = 0.0;
      const_g_im /= dc0.re;
    } else {
      hamiltonian = const_g_re / dc0.re;
      const_g_im /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = 0.0;
    } else if (const_g_im == 0.0) {
      hamiltonian = 0.0;
      const_g_im = -(const_g_re / dc0.im);
    } else {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = -(const_g_re / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      hamiltonian = (const_g_re + bim * const_g_im) / lamX_im;
      const_g_im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      hamiltonian = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      const_g_im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      hamiltonian = (bim * const_g_re + const_g_im) / lamX_im;
      const_g_im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -const_g_im;
  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  yc_z.re = xAndLambda_data[2] + 50.0;
  yc_z.im = 0.0;
  dc1 = b_mpower(yc_z);
  v_re = xAndLambda_data[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda_data[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda_data[9] * muDoubleScalarCos(const_alfamax *
          muDoubleScalarSin(alfatrig)));
  ai = -(0.0 * muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)));
  if (ai == 0.0) {
    Ttrignew = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    Ttrignew = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    Ttrignew = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    xAndLambda_data[11]) * muDoubleScalarCos(const_bankmax);
  ai = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarCos(const_bankmax);
  hamiltonian = const_mass * xAndLambda_data[3];
  lamX_im = const_mass * 0.0;
  if (lamX_im == 0.0) {
    if (ai == 0.0) {
      const_C1_re = ar / hamiltonian;
      lamY_im = 0.0;
    } else if (ar == 0.0) {
      const_C1_re = 0.0;
      lamY_im = ai / hamiltonian;
    } else {
      const_C1_re = ar / hamiltonian;
      lamY_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      const_C1_re = ai / lamX_im;
      lamY_im = 0.0;
    } else if (ai == 0.0) {
      const_C1_re = 0.0;
      lamY_im = -(ar / lamX_im);
    } else {
      const_C1_re = ai / lamX_im;
      lamY_im = -(ar / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > lamX_im) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      const_C1_re = (ar + bim * ai) / lamX_im;
      lamY_im = (ai - bim * ar) / lamX_im;
    } else if (lamX_im == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      const_C1_re = (ar * lamY_re + ai * -0.5) / 0.0;
      lamY_im = (ai * lamY_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      const_C1_re = (bim * ar + ai) / lamX_im;
      lamY_im = (bim * ai - ar) / lamX_im;
    }
  }

  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * a.re - const_mass_im * a.im;
  const_mass_im = hamiltonian * a.im + const_mass_im * a.re;
  ar = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    xAndLambda_data[10]) * muDoubleScalarSin(const_bankmax);
  ai = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarSin(const_bankmax);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      lamX_re = ar / const_mass_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      lamX_re = 0.0;
      hamiltonian = ai / const_mass_re;
    } else {
      lamX_re = ar / const_mass_re;
      hamiltonian = ai / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      lamX_re = ai / const_mass_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      lamX_re = 0.0;
      hamiltonian = -(ar / const_mass_im);
    } else {
      lamX_re = ai / const_mass_im;
      hamiltonian = -(ar / const_mass_im);
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      lamX_im = const_mass_re + bim * const_mass_im;
      lamX_re = (ar + bim * ai) / lamX_im;
      hamiltonian = (ai - bim * ar) / lamX_im;
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      lamX_re = (ar * lamY_re + ai * lamX_im) / brm;
      hamiltonian = (ai * lamY_re - ar * lamX_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      lamX_im = const_mass_im + bim * const_mass_re;
      lamX_re = (bim * ar + ai) / lamX_im;
      hamiltonian = (bim * ai - ar) / lamX_im;
    }
  }

  Ttrignew = (Ttrignew - const_C1_re) - lamX_re;
  const_C1_im = (const_C1_im - lamY_im) - hamiltonian;
  lamX_re = v_re * Ttrignew - v_im * const_C1_im;
  v_im = v_re * const_C1_im + v_im * Ttrignew;
  hamiltonian = 8112.0 * dc0.re;
  lamX_im = 8112.0 * dc0.im;
  if (lamX_im == 0.0) {
    if (v_im == 0.0) {
      yc_v.re = lamX_re / hamiltonian;
      yc_v.im = 0.0;
    } else if (lamX_re == 0.0) {
      yc_v.re = 0.0;
      yc_v.im = v_im / hamiltonian;
    } else {
      yc_v.re = lamX_re / hamiltonian;
      yc_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (lamX_re == 0.0) {
      yc_v.re = v_im / lamX_im;
      yc_v.im = 0.0;
    } else if (v_im == 0.0) {
      yc_v.re = 0.0;
      yc_v.im = -(lamX_re / lamX_im);
    } else {
      yc_v.re = v_im / lamX_im;
      yc_v.im = -(lamX_re / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(lamX_im);
    if (brm > bim) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      yc_v.re = (lamX_re + bim * v_im) / lamX_im;
      yc_v.im = (v_im - bim * lamX_re) / lamX_im;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (lamX_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      yc_v.re = (lamX_re * lamY_re + v_im * lamX_im) / brm;
      yc_v.im = (v_im * lamY_re - lamX_re * lamX_im) / brm;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      yc_v.re = (bim * lamX_re + v_im) / lamX_im;
      yc_v.im = (bim * v_im - lamX_re) / lamX_im;
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

  emlrtPushRtStackR2012b(&vb_emlrtRSI, emlrtRootTLSGlobal);
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
  ad_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  ad_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, ad_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0);
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  mc_const_mass.re = const_mass * xAndLambda_data[3];
  mc_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax) * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0)), mc_const_mass);
  ad_z.re = xAndLambda_data[2] + 50.0;
  ad_z.im = 0.0;
  v = b_mpower(ad_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * mc_v_re + ai * mc_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax) * xAndLambda_data[10] * (const_g *
    const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(const_bankmax) * 0.0 * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0));
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        mc_const_mass_re = 0.5;
      } else {
        mc_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        mc_const_mass_im = 0.5;
      } else {
        mc_const_mass_im = -0.5;
      }

      const_mass_re = (ar * mc_const_mass_re + ai * mc_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  emlrtPopRtStackR2012b(&vb_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = 1.5707963267948966;
    *alfatrigSave = alfatrig;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&wb_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = 3.1416 / (2.0 * const_bankmax);
  b_asin(&hamiltonian);
  banktrig = -hamiltonian;
  emlrtPopRtStackR2012b(&wb_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(-hamiltonian) || muDoubleScalarIsInf(-hamiltonian)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(2.0 * const_bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(2.0 * const_bankmax * muDoubleScalarSin
    (banktrig));
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      hamiltonian = const_g_re / dc0.re;
      const_g_im = 0.0;
    } else if (const_g_re == 0.0) {
      hamiltonian = 0.0;
      const_g_im /= dc0.re;
    } else {
      hamiltonian = const_g_re / dc0.re;
      const_g_im /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = 0.0;
    } else if (const_g_im == 0.0) {
      hamiltonian = 0.0;
      const_g_im = -(const_g_re / dc0.im);
    } else {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = -(const_g_re / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      hamiltonian = (const_g_re + bim * const_g_im) / lamX_im;
      const_g_im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      hamiltonian = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      const_g_im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      hamiltonian = (bim * const_g_re + const_g_im) / lamX_im;
      const_g_im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -const_g_im;
  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  bd_z.re = xAndLambda_data[2] + 50.0;
  bd_z.im = 0.0;
  dc1 = b_mpower(bd_z);
  v_re = xAndLambda_data[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda_data[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda_data[9] * muDoubleScalarCos(const_alfamax *
          muDoubleScalarSin(alfatrig)));
  ai = -(0.0 * muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)));
  if (ai == 0.0) {
    Ttrignew = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    Ttrignew = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    Ttrignew = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    xAndLambda_data[11]) * muDoubleScalarCos(const_bankmax * muDoubleScalarSin
    (banktrig));
  ai = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig));
  hamiltonian = const_mass * xAndLambda_data[3];
  lamX_im = const_mass * 0.0;
  if (lamX_im == 0.0) {
    if (ai == 0.0) {
      const_C1_re = ar / hamiltonian;
      lamY_im = 0.0;
    } else if (ar == 0.0) {
      const_C1_re = 0.0;
      lamY_im = ai / hamiltonian;
    } else {
      const_C1_re = ar / hamiltonian;
      lamY_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      const_C1_re = ai / lamX_im;
      lamY_im = 0.0;
    } else if (ai == 0.0) {
      const_C1_re = 0.0;
      lamY_im = -(ar / lamX_im);
    } else {
      const_C1_re = ai / lamX_im;
      lamY_im = -(ar / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > lamX_im) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      const_C1_re = (ar + bim * ai) / lamX_im;
      lamY_im = (ai - bim * ar) / lamX_im;
    } else if (lamX_im == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      const_C1_re = (ar * lamY_re + ai * -0.5) / 0.0;
      lamY_im = (ai * lamY_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      const_C1_re = (bim * ar + ai) / lamX_im;
      lamY_im = (bim * ai - ar) / lamX_im;
    }
  }

  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * a.re - const_mass_im * a.im;
  const_mass_im = hamiltonian * a.im + const_mass_im * a.re;
  ar = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    xAndLambda_data[10]) * muDoubleScalarSin(const_bankmax * muDoubleScalarSin
    (banktrig));
  ai = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig));
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      lamX_re = ar / const_mass_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      lamX_re = 0.0;
      hamiltonian = ai / const_mass_re;
    } else {
      lamX_re = ar / const_mass_re;
      hamiltonian = ai / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      lamX_re = ai / const_mass_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      lamX_re = 0.0;
      hamiltonian = -(ar / const_mass_im);
    } else {
      lamX_re = ai / const_mass_im;
      hamiltonian = -(ar / const_mass_im);
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      lamX_im = const_mass_re + bim * const_mass_im;
      lamX_re = (ar + bim * ai) / lamX_im;
      hamiltonian = (ai - bim * ar) / lamX_im;
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      lamX_re = (ar * lamY_re + ai * lamX_im) / brm;
      hamiltonian = (ai * lamY_re - ar * lamX_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      lamX_im = const_mass_im + bim * const_mass_re;
      lamX_re = (bim * ar + ai) / lamX_im;
      hamiltonian = (bim * ai - ar) / lamX_im;
    }
  }

  Ttrignew = (Ttrignew - const_C1_re) - lamX_re;
  const_C1_im = (const_C1_im - lamY_im) - hamiltonian;
  lamX_re = v_re * Ttrignew - v_im * const_C1_im;
  v_im = v_re * const_C1_im + v_im * Ttrignew;
  hamiltonian = 8112.0 * dc0.re;
  lamX_im = 8112.0 * dc0.im;
  if (lamX_im == 0.0) {
    if (v_im == 0.0) {
      bd_v.re = lamX_re / hamiltonian;
      bd_v.im = 0.0;
    } else if (lamX_re == 0.0) {
      bd_v.re = 0.0;
      bd_v.im = v_im / hamiltonian;
    } else {
      bd_v.re = lamX_re / hamiltonian;
      bd_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (lamX_re == 0.0) {
      bd_v.re = v_im / lamX_im;
      bd_v.im = 0.0;
    } else if (v_im == 0.0) {
      bd_v.re = 0.0;
      bd_v.im = -(lamX_re / lamX_im);
    } else {
      bd_v.re = v_im / lamX_im;
      bd_v.im = -(lamX_re / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(lamX_im);
    if (brm > bim) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      bd_v.re = (lamX_re + bim * v_im) / lamX_im;
      bd_v.im = (v_im - bim * lamX_re) / lamX_im;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (lamX_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      bd_v.re = (lamX_re * lamY_re + v_im * lamX_im) / brm;
      bd_v.im = (v_im * lamY_re - lamX_re * lamX_im) / brm;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      bd_v.re = (bim * lamX_re + v_im) / lamX_im;
      bd_v.im = (bim * v_im - lamX_re) / lamX_im;
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
  cd_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  cd_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, cd_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0);
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  nc_const_mass.re = const_mass * xAndLambda_data[3];
  nc_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig)) *
                (const_g * const_mass + muDoubleScalarSin(const_alfamax *
    muDoubleScalarSin(alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) +
    1860.0)), nc_const_mass);
  cd_z.re = xAndLambda_data[2] + 50.0;
  cd_z.im = 0.0;
  v = b_mpower(cd_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * nc_v_re + ai * nc_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda_data[10] * (const_g * const_mass + muDoubleScalarSin
    (const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 * muDoubleScalarSin
    (Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (const_g * const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin
      (alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0));
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        nc_const_mass_re = 0.5;
      } else {
        nc_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        nc_const_mass_im = 0.5;
      } else {
        nc_const_mass_im = -0.5;
      }

      const_mass_re = (ar * nc_const_mass_re + ai * nc_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  emlrtPopRtStackR2012b(&xb_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&yb_emlrtRSI, emlrtRootTLSGlobal);
  banktrig = 3.1416 / (2.0 * const_bankmax);
  b_asin(&banktrig);
  emlrtPopRtStackR2012b(&yb_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(banktrig) || muDoubleScalarIsInf(banktrig)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(2.0 * const_bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(2.0 * const_bankmax * muDoubleScalarSin
    (banktrig));
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      hamiltonian = const_g_re / dc0.re;
      const_g_im = 0.0;
    } else if (const_g_re == 0.0) {
      hamiltonian = 0.0;
      const_g_im /= dc0.re;
    } else {
      hamiltonian = const_g_re / dc0.re;
      const_g_im /= dc0.re;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = 0.0;
    } else if (const_g_im == 0.0) {
      hamiltonian = 0.0;
      const_g_im = -(const_g_re / dc0.im);
    } else {
      hamiltonian = const_g_im / dc0.im;
      const_g_im = -(const_g_re / dc0.im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      hamiltonian = (const_g_re + bim * const_g_im) / lamX_im;
      const_g_im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      hamiltonian = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      const_g_im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      hamiltonian = (bim * const_g_re + const_g_im) / lamX_im;
      const_g_im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  dc0.re = -hamiltonian;
  dc0.im = -const_g_im;
  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  dd_z.re = xAndLambda_data[2] + 50.0;
  dd_z.im = 0.0;
  dc1 = b_mpower(dd_z);
  v_re = xAndLambda_data[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda_data[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda_data[9] * muDoubleScalarCos(const_alfamax *
          muDoubleScalarSin(alfatrig)));
  ai = -(0.0 * muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)));
  if (ai == 0.0) {
    Ttrignew = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    Ttrignew = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    Ttrignew = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    xAndLambda_data[11]) * muDoubleScalarCos(const_bankmax * muDoubleScalarSin
    (banktrig));
  ai = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig));
  hamiltonian = const_mass * xAndLambda_data[3];
  lamX_im = const_mass * 0.0;
  if (lamX_im == 0.0) {
    if (ai == 0.0) {
      const_C1_re = ar / hamiltonian;
      lamY_im = 0.0;
    } else if (ar == 0.0) {
      const_C1_re = 0.0;
      lamY_im = ai / hamiltonian;
    } else {
      const_C1_re = ar / hamiltonian;
      lamY_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      const_C1_re = ai / lamX_im;
      lamY_im = 0.0;
    } else if (ai == 0.0) {
      const_C1_re = 0.0;
      lamY_im = -(ar / lamX_im);
    } else {
      const_C1_re = ai / lamX_im;
      lamY_im = -(ar / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > lamX_im) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      const_C1_re = (ar + bim * ai) / lamX_im;
      lamY_im = (ai - bim * ar) / lamX_im;
    } else if (lamX_im == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      const_C1_re = (ar * lamY_re + ai * -0.5) / 0.0;
      lamY_im = (ai * lamY_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      const_C1_re = (bim * ar + ai) / lamX_im;
      lamY_im = (bim * ai - ar) / lamX_im;
    }
  }

  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * a.re - const_mass_im * a.im;
  const_mass_im = hamiltonian * a.im + const_mass_im * a.re;
  ar = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    xAndLambda_data[10]) * muDoubleScalarSin(const_bankmax * muDoubleScalarSin
    (banktrig));
  ai = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig));
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      lamX_re = ar / const_mass_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      lamX_re = 0.0;
      hamiltonian = ai / const_mass_re;
    } else {
      lamX_re = ar / const_mass_re;
      hamiltonian = ai / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      lamX_re = ai / const_mass_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      lamX_re = 0.0;
      hamiltonian = -(ar / const_mass_im);
    } else {
      lamX_re = ai / const_mass_im;
      hamiltonian = -(ar / const_mass_im);
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      lamX_im = const_mass_re + bim * const_mass_im;
      lamX_re = (ar + bim * ai) / lamX_im;
      hamiltonian = (ai - bim * ar) / lamX_im;
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      lamX_re = (ar * lamY_re + ai * lamX_im) / brm;
      hamiltonian = (ai * lamY_re - ar * lamX_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      lamX_im = const_mass_im + bim * const_mass_re;
      lamX_re = (bim * ar + ai) / lamX_im;
      hamiltonian = (bim * ai - ar) / lamX_im;
    }
  }

  Ttrignew = (Ttrignew - const_C1_re) - lamX_re;
  const_C1_im = (const_C1_im - lamY_im) - hamiltonian;
  lamX_re = v_re * Ttrignew - v_im * const_C1_im;
  v_im = v_re * const_C1_im + v_im * Ttrignew;
  hamiltonian = 8112.0 * dc0.re;
  lamX_im = 8112.0 * dc0.im;
  if (lamX_im == 0.0) {
    if (v_im == 0.0) {
      dd_v.re = lamX_re / hamiltonian;
      dd_v.im = 0.0;
    } else if (lamX_re == 0.0) {
      dd_v.re = 0.0;
      dd_v.im = v_im / hamiltonian;
    } else {
      dd_v.re = lamX_re / hamiltonian;
      dd_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (lamX_re == 0.0) {
      dd_v.re = v_im / lamX_im;
      dd_v.im = 0.0;
    } else if (v_im == 0.0) {
      dd_v.re = 0.0;
      dd_v.im = -(lamX_re / lamX_im);
    } else {
      dd_v.re = v_im / lamX_im;
      dd_v.im = -(lamX_re / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(lamX_im);
    if (brm > bim) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      dd_v.re = (lamX_re + bim * v_im) / lamX_im;
      dd_v.im = (v_im - bim * lamX_re) / lamX_im;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (lamX_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      dd_v.re = (lamX_re * lamY_re + v_im * lamX_im) / brm;
      dd_v.im = (v_im * lamY_re - lamX_re * lamX_im) / brm;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      dd_v.re = (bim * lamX_re + v_im) / lamX_im;
      dd_v.im = (bim * v_im - lamX_re) / lamX_im;
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

  emlrtPushRtStackR2012b(&ac_emlrtRSI, emlrtRootTLSGlobal);
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
  ed_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  ed_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, ed_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0);
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  oc_const_mass.re = const_mass * xAndLambda_data[3];
  oc_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig)) *
                (const_g * const_mass + muDoubleScalarSin(const_alfamax *
    muDoubleScalarSin(alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) +
    1860.0)), oc_const_mass);
  ed_z.re = xAndLambda_data[2] + 50.0;
  ed_z.im = 0.0;
  v = b_mpower(ed_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * oc_v_re + ai * oc_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda_data[10] * (const_g * const_mass + muDoubleScalarSin
    (const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 * muDoubleScalarSin
    (Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (const_g * const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin
      (alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0));
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        oc_const_mass_re = 0.5;
      } else {
        oc_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        oc_const_mass_im = 0.5;
      } else {
        oc_const_mass_im = -0.5;
      }

      const_mass_re = (ar * oc_const_mass_re + ai * oc_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  emlrtPopRtStackR2012b(&ac_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(-const_bankmax);
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(-const_bankmax);
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(-(2.0 * const_bankmax));
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(-(2.0 * const_bankmax));
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  Ttrignew = dc0.re;
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      dc0.re = const_g_re / dc0.re;
      dc0.im = 0.0;
    } else if (const_g_re == 0.0) {
      dc0.re = 0.0;
      dc0.im = const_g_im / Ttrignew;
    } else {
      dc0.re = const_g_re / dc0.re;
      dc0.im = const_g_im / Ttrignew;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      dc0.re = const_g_im / dc0.im;
      dc0.im = 0.0;
    } else if (const_g_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(const_g_re / const_C1_im);
    } else {
      dc0.re = const_g_im / dc0.im;
      dc0.im = -(const_g_re / const_C1_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      dc0.re = (const_g_re + bim * const_g_im) / lamX_im;
      dc0.im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      dc0.re = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      dc0.im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      dc0.re = (bim * const_g_re + const_g_im) / lamX_im;
      dc0.im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  fd_z.re = xAndLambda_data[2] + 50.0;
  fd_z.im = 0.0;
  dc1 = b_mpower(fd_z);
  v_re = xAndLambda_data[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda_data[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda_data[9] * muDoubleScalarCos(const_alfamax *
          muDoubleScalarSin(alfatrig)));
  ai = -(0.0 * muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)));
  if (ai == 0.0) {
    Ttrignew = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    Ttrignew = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    Ttrignew = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    xAndLambda_data[11]) * muDoubleScalarCos(-const_bankmax);
  ai = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarCos(-const_bankmax);
  hamiltonian = const_mass * xAndLambda_data[3];
  lamX_im = const_mass * 0.0;
  if (lamX_im == 0.0) {
    if (ai == 0.0) {
      const_C1_re = ar / hamiltonian;
      lamY_im = 0.0;
    } else if (ar == 0.0) {
      const_C1_re = 0.0;
      lamY_im = ai / hamiltonian;
    } else {
      const_C1_re = ar / hamiltonian;
      lamY_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      const_C1_re = ai / lamX_im;
      lamY_im = 0.0;
    } else if (ai == 0.0) {
      const_C1_re = 0.0;
      lamY_im = -(ar / lamX_im);
    } else {
      const_C1_re = ai / lamX_im;
      lamY_im = -(ar / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > lamX_im) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      const_C1_re = (ar + bim * ai) / lamX_im;
      lamY_im = (ai - bim * ar) / lamX_im;
    } else if (lamX_im == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      const_C1_re = (ar * lamY_re + ai * -0.5) / 0.0;
      lamY_im = (ai * lamY_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      const_C1_re = (bim * ar + ai) / lamX_im;
      lamY_im = (bim * ai - ar) / lamX_im;
    }
  }

  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * a.re - const_mass_im * a.im;
  const_mass_im = hamiltonian * a.im + const_mass_im * a.re;
  ar = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    xAndLambda_data[10]) * muDoubleScalarSin(-const_bankmax);
  ai = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarSin(-const_bankmax);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      lamX_re = ar / const_mass_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      lamX_re = 0.0;
      hamiltonian = ai / const_mass_re;
    } else {
      lamX_re = ar / const_mass_re;
      hamiltonian = ai / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      lamX_re = ai / const_mass_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      lamX_re = 0.0;
      hamiltonian = -(ar / const_mass_im);
    } else {
      lamX_re = ai / const_mass_im;
      hamiltonian = -(ar / const_mass_im);
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      lamX_im = const_mass_re + bim * const_mass_im;
      lamX_re = (ar + bim * ai) / lamX_im;
      hamiltonian = (ai - bim * ar) / lamX_im;
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      lamX_re = (ar * lamY_re + ai * lamX_im) / brm;
      hamiltonian = (ai * lamY_re - ar * lamX_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      lamX_im = const_mass_im + bim * const_mass_re;
      lamX_re = (bim * ar + ai) / lamX_im;
      hamiltonian = (bim * ai - ar) / lamX_im;
    }
  }

  Ttrignew = (Ttrignew - const_C1_re) - lamX_re;
  const_C1_im = (const_C1_im - lamY_im) - hamiltonian;
  lamX_re = v_re * Ttrignew - v_im * const_C1_im;
  v_im = v_re * const_C1_im + v_im * Ttrignew;
  hamiltonian = 8112.0 * dc0.re;
  lamX_im = 8112.0 * dc0.im;
  if (lamX_im == 0.0) {
    if (v_im == 0.0) {
      fd_v.re = lamX_re / hamiltonian;
      fd_v.im = 0.0;
    } else if (lamX_re == 0.0) {
      fd_v.re = 0.0;
      fd_v.im = v_im / hamiltonian;
    } else {
      fd_v.re = lamX_re / hamiltonian;
      fd_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (lamX_re == 0.0) {
      fd_v.re = v_im / lamX_im;
      fd_v.im = 0.0;
    } else if (v_im == 0.0) {
      fd_v.re = 0.0;
      fd_v.im = -(lamX_re / lamX_im);
    } else {
      fd_v.re = v_im / lamX_im;
      fd_v.im = -(lamX_re / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(lamX_im);
    if (brm > bim) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      fd_v.re = (lamX_re + bim * v_im) / lamX_im;
      fd_v.im = (v_im - bim * lamX_re) / lamX_im;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (lamX_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      fd_v.re = (lamX_re * lamY_re + v_im * lamX_im) / brm;
      fd_v.im = (v_im * lamY_re - lamX_re * lamX_im) / brm;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      fd_v.re = (bim * lamX_re + v_im) / lamX_im;
      fd_v.im = (bim * v_im - lamX_re) / lamX_im;
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
  gd_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  gd_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, gd_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0);
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  pc_const_mass.re = const_mass * xAndLambda_data[3];
  pc_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(-const_bankmax) * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0)), pc_const_mass);
  gd_z.re = xAndLambda_data[2] + 50.0;
  gd_z.im = 0.0;
  v = b_mpower(gd_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * pc_v_re + ai * pc_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(-const_bankmax) * xAndLambda_data[10] * (const_g *
    const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(-const_bankmax) * 0.0 * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0));
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        pc_const_mass_re = 0.5;
      } else {
        pc_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        pc_const_mass_im = 0.5;
      } else {
        pc_const_mass_im = -0.5;
      }

      const_mass_re = (ar * pc_const_mass_re + ai * pc_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  emlrtPopRtStackR2012b(&bc_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = -1.5707963267948966;
    *alfatrigSave = alfatrig;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(const_bankmax);
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(const_bankmax);
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(2.0 * const_bankmax);
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(2.0 * const_bankmax);
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  Ttrignew = dc0.re;
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      dc0.re = const_g_re / dc0.re;
      dc0.im = 0.0;
    } else if (const_g_re == 0.0) {
      dc0.re = 0.0;
      dc0.im = const_g_im / Ttrignew;
    } else {
      dc0.re = const_g_re / dc0.re;
      dc0.im = const_g_im / Ttrignew;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      dc0.re = const_g_im / dc0.im;
      dc0.im = 0.0;
    } else if (const_g_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(const_g_re / const_C1_im);
    } else {
      dc0.re = const_g_im / dc0.im;
      dc0.im = -(const_g_re / const_C1_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      dc0.re = (const_g_re + bim * const_g_im) / lamX_im;
      dc0.im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      dc0.re = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      dc0.im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      dc0.re = (bim * const_g_re + const_g_im) / lamX_im;
      dc0.im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  hd_z.re = xAndLambda_data[2] + 50.0;
  hd_z.im = 0.0;
  dc1 = b_mpower(hd_z);
  v_re = xAndLambda_data[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda_data[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda_data[9] * muDoubleScalarCos(const_alfamax *
          muDoubleScalarSin(alfatrig)));
  ai = -(0.0 * muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)));
  if (ai == 0.0) {
    Ttrignew = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    Ttrignew = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    Ttrignew = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    xAndLambda_data[11]) * muDoubleScalarCos(const_bankmax);
  ai = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarCos(const_bankmax);
  hamiltonian = const_mass * xAndLambda_data[3];
  lamX_im = const_mass * 0.0;
  if (lamX_im == 0.0) {
    if (ai == 0.0) {
      const_C1_re = ar / hamiltonian;
      lamY_im = 0.0;
    } else if (ar == 0.0) {
      const_C1_re = 0.0;
      lamY_im = ai / hamiltonian;
    } else {
      const_C1_re = ar / hamiltonian;
      lamY_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      const_C1_re = ai / lamX_im;
      lamY_im = 0.0;
    } else if (ai == 0.0) {
      const_C1_re = 0.0;
      lamY_im = -(ar / lamX_im);
    } else {
      const_C1_re = ai / lamX_im;
      lamY_im = -(ar / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > lamX_im) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      const_C1_re = (ar + bim * ai) / lamX_im;
      lamY_im = (ai - bim * ar) / lamX_im;
    } else if (lamX_im == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      const_C1_re = (ar * lamY_re + ai * -0.5) / 0.0;
      lamY_im = (ai * lamY_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      const_C1_re = (bim * ar + ai) / lamX_im;
      lamY_im = (bim * ai - ar) / lamX_im;
    }
  }

  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * a.re - const_mass_im * a.im;
  const_mass_im = hamiltonian * a.im + const_mass_im * a.re;
  ar = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    xAndLambda_data[10]) * muDoubleScalarSin(const_bankmax);
  ai = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarSin(const_bankmax);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      lamX_re = ar / const_mass_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      lamX_re = 0.0;
      hamiltonian = ai / const_mass_re;
    } else {
      lamX_re = ar / const_mass_re;
      hamiltonian = ai / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      lamX_re = ai / const_mass_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      lamX_re = 0.0;
      hamiltonian = -(ar / const_mass_im);
    } else {
      lamX_re = ai / const_mass_im;
      hamiltonian = -(ar / const_mass_im);
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      lamX_im = const_mass_re + bim * const_mass_im;
      lamX_re = (ar + bim * ai) / lamX_im;
      hamiltonian = (ai - bim * ar) / lamX_im;
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      lamX_re = (ar * lamY_re + ai * lamX_im) / brm;
      hamiltonian = (ai * lamY_re - ar * lamX_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      lamX_im = const_mass_im + bim * const_mass_re;
      lamX_re = (bim * ar + ai) / lamX_im;
      hamiltonian = (bim * ai - ar) / lamX_im;
    }
  }

  Ttrignew = (Ttrignew - const_C1_re) - lamX_re;
  const_C1_im = (const_C1_im - lamY_im) - hamiltonian;
  lamX_re = v_re * Ttrignew - v_im * const_C1_im;
  v_im = v_re * const_C1_im + v_im * Ttrignew;
  hamiltonian = 8112.0 * dc0.re;
  lamX_im = 8112.0 * dc0.im;
  if (lamX_im == 0.0) {
    if (v_im == 0.0) {
      hd_v.re = lamX_re / hamiltonian;
      hd_v.im = 0.0;
    } else if (lamX_re == 0.0) {
      hd_v.re = 0.0;
      hd_v.im = v_im / hamiltonian;
    } else {
      hd_v.re = lamX_re / hamiltonian;
      hd_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (lamX_re == 0.0) {
      hd_v.re = v_im / lamX_im;
      hd_v.im = 0.0;
    } else if (v_im == 0.0) {
      hd_v.re = 0.0;
      hd_v.im = -(lamX_re / lamX_im);
    } else {
      hd_v.re = v_im / lamX_im;
      hd_v.im = -(lamX_re / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(lamX_im);
    if (brm > bim) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      hd_v.re = (lamX_re + bim * v_im) / lamX_im;
      hd_v.im = (v_im - bim * lamX_re) / lamX_im;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (lamX_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      hd_v.re = (lamX_re * lamY_re + v_im * lamX_im) / brm;
      hd_v.im = (v_im * lamY_re - lamX_re * lamX_im) / brm;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      hd_v.re = (bim * lamX_re + v_im) / lamX_im;
      hd_v.im = (bim * v_im - lamX_re) / lamX_im;
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

  emlrtPushRtStackR2012b(&cc_emlrtRSI, emlrtRootTLSGlobal);
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
  id_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  id_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, id_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0);
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  qc_const_mass.re = const_mass * xAndLambda_data[3];
  qc_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax) * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0)), qc_const_mass);
  id_z.re = xAndLambda_data[2] + 50.0;
  id_z.im = 0.0;
  v = b_mpower(id_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * qc_v_re + ai * qc_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax) * xAndLambda_data[10] * (const_g *
    const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(const_bankmax) * 0.0 * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0));
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        qc_const_mass_re = 0.5;
      } else {
        qc_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        qc_const_mass_im = 0.5;
      } else {
        qc_const_mass_im = -0.5;
      }

      const_mass_re = (ar * qc_const_mass_re + ai * qc_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  emlrtPopRtStackR2012b(&cc_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = 1.5707963267948966;
    *alfatrigSave = alfatrig;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&dc_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = 3.1416 / (2.0 * const_bankmax);
  b_asin(&hamiltonian);
  banktrig = -hamiltonian;
  emlrtPopRtStackR2012b(&dc_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(-hamiltonian) || muDoubleScalarIsInf(-hamiltonian)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(2.0 * const_bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(2.0 * const_bankmax * muDoubleScalarSin
    (banktrig));
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  Ttrignew = dc0.re;
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      dc0.re = const_g_re / dc0.re;
      dc0.im = 0.0;
    } else if (const_g_re == 0.0) {
      dc0.re = 0.0;
      dc0.im = const_g_im / Ttrignew;
    } else {
      dc0.re = const_g_re / dc0.re;
      dc0.im = const_g_im / Ttrignew;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      dc0.re = const_g_im / dc0.im;
      dc0.im = 0.0;
    } else if (const_g_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(const_g_re / const_C1_im);
    } else {
      dc0.re = const_g_im / dc0.im;
      dc0.im = -(const_g_re / const_C1_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      dc0.re = (const_g_re + bim * const_g_im) / lamX_im;
      dc0.im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      dc0.re = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      dc0.im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      dc0.re = (bim * const_g_re + const_g_im) / lamX_im;
      dc0.im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  jd_z.re = xAndLambda_data[2] + 50.0;
  jd_z.im = 0.0;
  dc1 = b_mpower(jd_z);
  v_re = xAndLambda_data[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda_data[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda_data[9] * muDoubleScalarCos(const_alfamax *
          muDoubleScalarSin(alfatrig)));
  ai = -(0.0 * muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)));
  if (ai == 0.0) {
    Ttrignew = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    Ttrignew = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    Ttrignew = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    xAndLambda_data[11]) * muDoubleScalarCos(const_bankmax * muDoubleScalarSin
    (banktrig));
  ai = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig));
  hamiltonian = const_mass * xAndLambda_data[3];
  lamX_im = const_mass * 0.0;
  if (lamX_im == 0.0) {
    if (ai == 0.0) {
      const_C1_re = ar / hamiltonian;
      lamY_im = 0.0;
    } else if (ar == 0.0) {
      const_C1_re = 0.0;
      lamY_im = ai / hamiltonian;
    } else {
      const_C1_re = ar / hamiltonian;
      lamY_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      const_C1_re = ai / lamX_im;
      lamY_im = 0.0;
    } else if (ai == 0.0) {
      const_C1_re = 0.0;
      lamY_im = -(ar / lamX_im);
    } else {
      const_C1_re = ai / lamX_im;
      lamY_im = -(ar / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > lamX_im) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      const_C1_re = (ar + bim * ai) / lamX_im;
      lamY_im = (ai - bim * ar) / lamX_im;
    } else if (lamX_im == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      const_C1_re = (ar * lamY_re + ai * -0.5) / 0.0;
      lamY_im = (ai * lamY_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      const_C1_re = (bim * ar + ai) / lamX_im;
      lamY_im = (bim * ai - ar) / lamX_im;
    }
  }

  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * a.re - const_mass_im * a.im;
  const_mass_im = hamiltonian * a.im + const_mass_im * a.re;
  ar = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    xAndLambda_data[10]) * muDoubleScalarSin(const_bankmax * muDoubleScalarSin
    (banktrig));
  ai = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig));
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      lamX_re = ar / const_mass_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      lamX_re = 0.0;
      hamiltonian = ai / const_mass_re;
    } else {
      lamX_re = ar / const_mass_re;
      hamiltonian = ai / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      lamX_re = ai / const_mass_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      lamX_re = 0.0;
      hamiltonian = -(ar / const_mass_im);
    } else {
      lamX_re = ai / const_mass_im;
      hamiltonian = -(ar / const_mass_im);
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      lamX_im = const_mass_re + bim * const_mass_im;
      lamX_re = (ar + bim * ai) / lamX_im;
      hamiltonian = (ai - bim * ar) / lamX_im;
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      lamX_re = (ar * lamY_re + ai * lamX_im) / brm;
      hamiltonian = (ai * lamY_re - ar * lamX_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      lamX_im = const_mass_im + bim * const_mass_re;
      lamX_re = (bim * ar + ai) / lamX_im;
      hamiltonian = (bim * ai - ar) / lamX_im;
    }
  }

  Ttrignew = (Ttrignew - const_C1_re) - lamX_re;
  const_C1_im = (const_C1_im - lamY_im) - hamiltonian;
  lamX_re = v_re * Ttrignew - v_im * const_C1_im;
  v_im = v_re * const_C1_im + v_im * Ttrignew;
  hamiltonian = 8112.0 * dc0.re;
  lamX_im = 8112.0 * dc0.im;
  if (lamX_im == 0.0) {
    if (v_im == 0.0) {
      jd_v.re = lamX_re / hamiltonian;
      jd_v.im = 0.0;
    } else if (lamX_re == 0.0) {
      jd_v.re = 0.0;
      jd_v.im = v_im / hamiltonian;
    } else {
      jd_v.re = lamX_re / hamiltonian;
      jd_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (lamX_re == 0.0) {
      jd_v.re = v_im / lamX_im;
      jd_v.im = 0.0;
    } else if (v_im == 0.0) {
      jd_v.re = 0.0;
      jd_v.im = -(lamX_re / lamX_im);
    } else {
      jd_v.re = v_im / lamX_im;
      jd_v.im = -(lamX_re / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(lamX_im);
    if (brm > bim) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      jd_v.re = (lamX_re + bim * v_im) / lamX_im;
      jd_v.im = (v_im - bim * lamX_re) / lamX_im;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (lamX_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      jd_v.re = (lamX_re * lamY_re + v_im * lamX_im) / brm;
      jd_v.im = (v_im * lamY_re - lamX_re * lamX_im) / brm;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      jd_v.re = (bim * lamX_re + v_im) / lamX_im;
      jd_v.im = (bim * v_im - lamX_re) / lamX_im;
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
  kd_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  kd_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, kd_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0);
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  rc_const_mass.re = const_mass * xAndLambda_data[3];
  rc_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig)) *
                (const_g * const_mass + muDoubleScalarSin(const_alfamax *
    muDoubleScalarSin(alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) +
    1860.0)), rc_const_mass);
  kd_z.re = xAndLambda_data[2] + 50.0;
  kd_z.im = 0.0;
  v = b_mpower(kd_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * rc_v_re + ai * rc_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda_data[10] * (const_g * const_mass + muDoubleScalarSin
    (const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 * muDoubleScalarSin
    (Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (const_g * const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin
      (alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0));
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        rc_const_mass_re = 0.5;
      } else {
        rc_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        rc_const_mass_im = 0.5;
      } else {
        rc_const_mass_im = -0.5;
      }

      const_mass_re = (ar * rc_const_mass_re + ai * rc_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  emlrtPopRtStackR2012b(&ec_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&fc_emlrtRSI, emlrtRootTLSGlobal);
  banktrig = 3.1416 / (2.0 * const_bankmax);
  b_asin(&banktrig);
  emlrtPopRtStackR2012b(&fc_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(banktrig) || muDoubleScalarIsInf(banktrig)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(2.0 * const_bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(2.0 * const_bankmax * muDoubleScalarSin
    (banktrig));
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  Ttrignew = dc0.re;
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      dc0.re = const_g_re / dc0.re;
      dc0.im = 0.0;
    } else if (const_g_re == 0.0) {
      dc0.re = 0.0;
      dc0.im = const_g_im / Ttrignew;
    } else {
      dc0.re = const_g_re / dc0.re;
      dc0.im = const_g_im / Ttrignew;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      dc0.re = const_g_im / dc0.im;
      dc0.im = 0.0;
    } else if (const_g_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(const_g_re / const_C1_im);
    } else {
      dc0.re = const_g_im / dc0.im;
      dc0.im = -(const_g_re / const_C1_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      dc0.re = (const_g_re + bim * const_g_im) / lamX_im;
      dc0.im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      dc0.re = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      dc0.im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      dc0.re = (bim * const_g_re + const_g_im) / lamX_im;
      dc0.im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  ld_z.re = xAndLambda_data[2] + 50.0;
  ld_z.im = 0.0;
  dc1 = b_mpower(ld_z);
  v_re = xAndLambda_data[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda_data[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda_data[9] * muDoubleScalarCos(const_alfamax *
          muDoubleScalarSin(alfatrig)));
  ai = -(0.0 * muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)));
  if (ai == 0.0) {
    Ttrignew = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    Ttrignew = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    Ttrignew = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    xAndLambda_data[11]) * muDoubleScalarCos(const_bankmax * muDoubleScalarSin
    (banktrig));
  ai = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig));
  hamiltonian = const_mass * xAndLambda_data[3];
  lamX_im = const_mass * 0.0;
  if (lamX_im == 0.0) {
    if (ai == 0.0) {
      const_C1_re = ar / hamiltonian;
      lamY_im = 0.0;
    } else if (ar == 0.0) {
      const_C1_re = 0.0;
      lamY_im = ai / hamiltonian;
    } else {
      const_C1_re = ar / hamiltonian;
      lamY_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      const_C1_re = ai / lamX_im;
      lamY_im = 0.0;
    } else if (ai == 0.0) {
      const_C1_re = 0.0;
      lamY_im = -(ar / lamX_im);
    } else {
      const_C1_re = ai / lamX_im;
      lamY_im = -(ar / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > lamX_im) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      const_C1_re = (ar + bim * ai) / lamX_im;
      lamY_im = (ai - bim * ar) / lamX_im;
    } else if (lamX_im == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      const_C1_re = (ar * lamY_re + ai * -0.5) / 0.0;
      lamY_im = (ai * lamY_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      const_C1_re = (bim * ar + ai) / lamX_im;
      lamY_im = (bim * ai - ar) / lamX_im;
    }
  }

  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * a.re - const_mass_im * a.im;
  const_mass_im = hamiltonian * a.im + const_mass_im * a.re;
  ar = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    xAndLambda_data[10]) * muDoubleScalarSin(const_bankmax * muDoubleScalarSin
    (banktrig));
  ai = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig));
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      lamX_re = ar / const_mass_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      lamX_re = 0.0;
      hamiltonian = ai / const_mass_re;
    } else {
      lamX_re = ar / const_mass_re;
      hamiltonian = ai / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      lamX_re = ai / const_mass_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      lamX_re = 0.0;
      hamiltonian = -(ar / const_mass_im);
    } else {
      lamX_re = ai / const_mass_im;
      hamiltonian = -(ar / const_mass_im);
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      lamX_im = const_mass_re + bim * const_mass_im;
      lamX_re = (ar + bim * ai) / lamX_im;
      hamiltonian = (ai - bim * ar) / lamX_im;
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      lamX_re = (ar * lamY_re + ai * lamX_im) / brm;
      hamiltonian = (ai * lamY_re - ar * lamX_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      lamX_im = const_mass_im + bim * const_mass_re;
      lamX_re = (bim * ar + ai) / lamX_im;
      hamiltonian = (bim * ai - ar) / lamX_im;
    }
  }

  Ttrignew = (Ttrignew - const_C1_re) - lamX_re;
  const_C1_im = (const_C1_im - lamY_im) - hamiltonian;
  lamX_re = v_re * Ttrignew - v_im * const_C1_im;
  v_im = v_re * const_C1_im + v_im * Ttrignew;
  hamiltonian = 8112.0 * dc0.re;
  lamX_im = 8112.0 * dc0.im;
  if (lamX_im == 0.0) {
    if (v_im == 0.0) {
      ld_v.re = lamX_re / hamiltonian;
      ld_v.im = 0.0;
    } else if (lamX_re == 0.0) {
      ld_v.re = 0.0;
      ld_v.im = v_im / hamiltonian;
    } else {
      ld_v.re = lamX_re / hamiltonian;
      ld_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (lamX_re == 0.0) {
      ld_v.re = v_im / lamX_im;
      ld_v.im = 0.0;
    } else if (v_im == 0.0) {
      ld_v.re = 0.0;
      ld_v.im = -(lamX_re / lamX_im);
    } else {
      ld_v.re = v_im / lamX_im;
      ld_v.im = -(lamX_re / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(lamX_im);
    if (brm > bim) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      ld_v.re = (lamX_re + bim * v_im) / lamX_im;
      ld_v.im = (v_im - bim * lamX_re) / lamX_im;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (lamX_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      ld_v.re = (lamX_re * lamY_re + v_im * lamX_im) / brm;
      ld_v.im = (v_im * lamY_re - lamX_re * lamX_im) / brm;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      ld_v.re = (bim * lamX_re + v_im) / lamX_im;
      ld_v.im = (bim * v_im - lamX_re) / lamX_im;
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

  emlrtPushRtStackR2012b(&gc_emlrtRSI, emlrtRootTLSGlobal);
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
  md_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  md_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, md_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0);
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  sc_const_mass.re = const_mass * xAndLambda_data[3];
  sc_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig)) *
                (const_g * const_mass + muDoubleScalarSin(const_alfamax *
    muDoubleScalarSin(alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) +
    1860.0)), sc_const_mass);
  md_z.re = xAndLambda_data[2] + 50.0;
  md_z.im = 0.0;
  v = b_mpower(md_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * sc_v_re + ai * sc_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda_data[10] * (const_g * const_mass + muDoubleScalarSin
    (const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 * muDoubleScalarSin
    (Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (const_g * const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin
      (alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0));
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        sc_const_mass_re = 0.5;
      } else {
        sc_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        sc_const_mass_im = 0.5;
      } else {
        sc_const_mass_im = -0.5;
      }

      const_mass_re = (ar * sc_const_mass_re + ai * sc_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  emlrtPopRtStackR2012b(&gc_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(-const_bankmax);
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(-const_bankmax);
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(-(2.0 * const_bankmax));
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(-(2.0 * const_bankmax));
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  Ttrignew = dc0.re;
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      dc0.re = const_g_re / dc0.re;
      dc0.im = 0.0;
    } else if (const_g_re == 0.0) {
      dc0.re = 0.0;
      dc0.im = const_g_im / Ttrignew;
    } else {
      dc0.re = const_g_re / dc0.re;
      dc0.im = const_g_im / Ttrignew;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      dc0.re = const_g_im / dc0.im;
      dc0.im = 0.0;
    } else if (const_g_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(const_g_re / const_C1_im);
    } else {
      dc0.re = const_g_im / dc0.im;
      dc0.im = -(const_g_re / const_C1_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      dc0.re = (const_g_re + bim * const_g_im) / lamX_im;
      dc0.im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      dc0.re = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      dc0.im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      dc0.re = (bim * const_g_re + const_g_im) / lamX_im;
      dc0.im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  nd_z.re = xAndLambda_data[2] + 50.0;
  nd_z.im = 0.0;
  dc1 = b_mpower(nd_z);
  v_re = xAndLambda_data[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda_data[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda_data[9] * muDoubleScalarCos(const_alfamax *
          muDoubleScalarSin(alfatrig)));
  ai = -(0.0 * muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)));
  if (ai == 0.0) {
    Ttrignew = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    Ttrignew = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    Ttrignew = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    xAndLambda_data[11]) * muDoubleScalarCos(-const_bankmax);
  ai = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarCos(-const_bankmax);
  hamiltonian = const_mass * xAndLambda_data[3];
  lamX_im = const_mass * 0.0;
  if (lamX_im == 0.0) {
    if (ai == 0.0) {
      const_C1_re = ar / hamiltonian;
      lamY_im = 0.0;
    } else if (ar == 0.0) {
      const_C1_re = 0.0;
      lamY_im = ai / hamiltonian;
    } else {
      const_C1_re = ar / hamiltonian;
      lamY_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      const_C1_re = ai / lamX_im;
      lamY_im = 0.0;
    } else if (ai == 0.0) {
      const_C1_re = 0.0;
      lamY_im = -(ar / lamX_im);
    } else {
      const_C1_re = ai / lamX_im;
      lamY_im = -(ar / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > lamX_im) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      const_C1_re = (ar + bim * ai) / lamX_im;
      lamY_im = (ai - bim * ar) / lamX_im;
    } else if (lamX_im == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      const_C1_re = (ar * lamY_re + ai * -0.5) / 0.0;
      lamY_im = (ai * lamY_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      const_C1_re = (bim * ar + ai) / lamX_im;
      lamY_im = (bim * ai - ar) / lamX_im;
    }
  }

  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * a.re - const_mass_im * a.im;
  const_mass_im = hamiltonian * a.im + const_mass_im * a.re;
  ar = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    xAndLambda_data[10]) * muDoubleScalarSin(-const_bankmax);
  ai = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarSin(-const_bankmax);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      lamX_re = ar / const_mass_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      lamX_re = 0.0;
      hamiltonian = ai / const_mass_re;
    } else {
      lamX_re = ar / const_mass_re;
      hamiltonian = ai / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      lamX_re = ai / const_mass_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      lamX_re = 0.0;
      hamiltonian = -(ar / const_mass_im);
    } else {
      lamX_re = ai / const_mass_im;
      hamiltonian = -(ar / const_mass_im);
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      lamX_im = const_mass_re + bim * const_mass_im;
      lamX_re = (ar + bim * ai) / lamX_im;
      hamiltonian = (ai - bim * ar) / lamX_im;
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      lamX_re = (ar * lamY_re + ai * lamX_im) / brm;
      hamiltonian = (ai * lamY_re - ar * lamX_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      lamX_im = const_mass_im + bim * const_mass_re;
      lamX_re = (bim * ar + ai) / lamX_im;
      hamiltonian = (bim * ai - ar) / lamX_im;
    }
  }

  Ttrignew = (Ttrignew - const_C1_re) - lamX_re;
  const_C1_im = (const_C1_im - lamY_im) - hamiltonian;
  lamX_re = v_re * Ttrignew - v_im * const_C1_im;
  v_im = v_re * const_C1_im + v_im * Ttrignew;
  hamiltonian = 8112.0 * dc0.re;
  lamX_im = 8112.0 * dc0.im;
  if (lamX_im == 0.0) {
    if (v_im == 0.0) {
      nd_v.re = lamX_re / hamiltonian;
      nd_v.im = 0.0;
    } else if (lamX_re == 0.0) {
      nd_v.re = 0.0;
      nd_v.im = v_im / hamiltonian;
    } else {
      nd_v.re = lamX_re / hamiltonian;
      nd_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (lamX_re == 0.0) {
      nd_v.re = v_im / lamX_im;
      nd_v.im = 0.0;
    } else if (v_im == 0.0) {
      nd_v.re = 0.0;
      nd_v.im = -(lamX_re / lamX_im);
    } else {
      nd_v.re = v_im / lamX_im;
      nd_v.im = -(lamX_re / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(lamX_im);
    if (brm > bim) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      nd_v.re = (lamX_re + bim * v_im) / lamX_im;
      nd_v.im = (v_im - bim * lamX_re) / lamX_im;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (lamX_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      nd_v.re = (lamX_re * lamY_re + v_im * lamX_im) / brm;
      nd_v.im = (v_im * lamY_re - lamX_re * lamX_im) / brm;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      nd_v.re = (bim * lamX_re + v_im) / lamX_im;
      nd_v.im = (bim * v_im - lamX_re) / lamX_im;
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
  od_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  od_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, od_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0);
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  tc_const_mass.re = const_mass * xAndLambda_data[3];
  tc_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(-const_bankmax) * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0)), tc_const_mass);
  od_z.re = xAndLambda_data[2] + 50.0;
  od_z.im = 0.0;
  v = b_mpower(od_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * tc_v_re + ai * tc_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(-const_bankmax) * xAndLambda_data[10] * (const_g *
    const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(-const_bankmax) * 0.0 * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0));
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        tc_const_mass_re = 0.5;
      } else {
        tc_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        tc_const_mass_im = 0.5;
      } else {
        tc_const_mass_im = -0.5;
      }

      const_mass_re = (ar * tc_const_mass_re + ai * tc_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  emlrtPopRtStackR2012b(&hc_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = -1.5707963267948966;
    *alfatrigSave = alfatrig;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(const_bankmax);
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(const_bankmax);
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(2.0 * const_bankmax);
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(2.0 * const_bankmax);
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  Ttrignew = dc0.re;
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      dc0.re = const_g_re / dc0.re;
      dc0.im = 0.0;
    } else if (const_g_re == 0.0) {
      dc0.re = 0.0;
      dc0.im = const_g_im / Ttrignew;
    } else {
      dc0.re = const_g_re / dc0.re;
      dc0.im = const_g_im / Ttrignew;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      dc0.re = const_g_im / dc0.im;
      dc0.im = 0.0;
    } else if (const_g_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(const_g_re / const_C1_im);
    } else {
      dc0.re = const_g_im / dc0.im;
      dc0.im = -(const_g_re / const_C1_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      dc0.re = (const_g_re + bim * const_g_im) / lamX_im;
      dc0.im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      dc0.re = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      dc0.im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      dc0.re = (bim * const_g_re + const_g_im) / lamX_im;
      dc0.im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  pd_z.re = xAndLambda_data[2] + 50.0;
  pd_z.im = 0.0;
  dc1 = b_mpower(pd_z);
  v_re = xAndLambda_data[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda_data[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda_data[9] * muDoubleScalarCos(const_alfamax *
          muDoubleScalarSin(alfatrig)));
  ai = -(0.0 * muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)));
  if (ai == 0.0) {
    Ttrignew = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    Ttrignew = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    Ttrignew = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    xAndLambda_data[11]) * muDoubleScalarCos(const_bankmax);
  ai = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarCos(const_bankmax);
  hamiltonian = const_mass * xAndLambda_data[3];
  lamX_im = const_mass * 0.0;
  if (lamX_im == 0.0) {
    if (ai == 0.0) {
      const_C1_re = ar / hamiltonian;
      lamY_im = 0.0;
    } else if (ar == 0.0) {
      const_C1_re = 0.0;
      lamY_im = ai / hamiltonian;
    } else {
      const_C1_re = ar / hamiltonian;
      lamY_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      const_C1_re = ai / lamX_im;
      lamY_im = 0.0;
    } else if (ai == 0.0) {
      const_C1_re = 0.0;
      lamY_im = -(ar / lamX_im);
    } else {
      const_C1_re = ai / lamX_im;
      lamY_im = -(ar / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > lamX_im) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      const_C1_re = (ar + bim * ai) / lamX_im;
      lamY_im = (ai - bim * ar) / lamX_im;
    } else if (lamX_im == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      const_C1_re = (ar * lamY_re + ai * -0.5) / 0.0;
      lamY_im = (ai * lamY_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      const_C1_re = (bim * ar + ai) / lamX_im;
      lamY_im = (bim * ai - ar) / lamX_im;
    }
  }

  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * a.re - const_mass_im * a.im;
  const_mass_im = hamiltonian * a.im + const_mass_im * a.re;
  ar = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    xAndLambda_data[10]) * muDoubleScalarSin(const_bankmax);
  ai = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarSin(const_bankmax);
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      lamX_re = ar / const_mass_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      lamX_re = 0.0;
      hamiltonian = ai / const_mass_re;
    } else {
      lamX_re = ar / const_mass_re;
      hamiltonian = ai / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      lamX_re = ai / const_mass_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      lamX_re = 0.0;
      hamiltonian = -(ar / const_mass_im);
    } else {
      lamX_re = ai / const_mass_im;
      hamiltonian = -(ar / const_mass_im);
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      lamX_im = const_mass_re + bim * const_mass_im;
      lamX_re = (ar + bim * ai) / lamX_im;
      hamiltonian = (ai - bim * ar) / lamX_im;
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      lamX_re = (ar * lamY_re + ai * lamX_im) / brm;
      hamiltonian = (ai * lamY_re - ar * lamX_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      lamX_im = const_mass_im + bim * const_mass_re;
      lamX_re = (bim * ar + ai) / lamX_im;
      hamiltonian = (bim * ai - ar) / lamX_im;
    }
  }

  Ttrignew = (Ttrignew - const_C1_re) - lamX_re;
  const_C1_im = (const_C1_im - lamY_im) - hamiltonian;
  lamX_re = v_re * Ttrignew - v_im * const_C1_im;
  v_im = v_re * const_C1_im + v_im * Ttrignew;
  hamiltonian = 8112.0 * dc0.re;
  lamX_im = 8112.0 * dc0.im;
  if (lamX_im == 0.0) {
    if (v_im == 0.0) {
      pd_v.re = lamX_re / hamiltonian;
      pd_v.im = 0.0;
    } else if (lamX_re == 0.0) {
      pd_v.re = 0.0;
      pd_v.im = v_im / hamiltonian;
    } else {
      pd_v.re = lamX_re / hamiltonian;
      pd_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (lamX_re == 0.0) {
      pd_v.re = v_im / lamX_im;
      pd_v.im = 0.0;
    } else if (v_im == 0.0) {
      pd_v.re = 0.0;
      pd_v.im = -(lamX_re / lamX_im);
    } else {
      pd_v.re = v_im / lamX_im;
      pd_v.im = -(lamX_re / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(lamX_im);
    if (brm > bim) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      pd_v.re = (lamX_re + bim * v_im) / lamX_im;
      pd_v.im = (v_im - bim * lamX_re) / lamX_im;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (lamX_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      pd_v.re = (lamX_re * lamY_re + v_im * lamX_im) / brm;
      pd_v.im = (v_im * lamY_re - lamX_re * lamX_im) / brm;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      pd_v.re = (bim * lamX_re + v_im) / lamX_im;
      pd_v.im = (bim * v_im - lamX_re) / lamX_im;
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

  emlrtPushRtStackR2012b(&ic_emlrtRSI, emlrtRootTLSGlobal);
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
  qd_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  qd_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, qd_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0);
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  uc_const_mass.re = const_mass * xAndLambda_data[3];
  uc_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax) * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0)), uc_const_mass);
  qd_z.re = xAndLambda_data[2] + 50.0;
  qd_z.im = 0.0;
  v = b_mpower(qd_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * uc_v_re + ai * uc_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax) * xAndLambda_data[10] * (const_g *
    const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) *
    (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(const_bankmax) * 0.0 * (const_g * const_mass +
    muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0));
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        uc_const_mass_re = 0.5;
      } else {
        uc_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        uc_const_mass_im = 0.5;
      } else {
        uc_const_mass_im = -0.5;
      }

      const_mass_re = (ar * uc_const_mass_re + ai * uc_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  emlrtPopRtStackR2012b(&ic_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = 1.5707963267948966;
    *alfatrigSave = alfatrig;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&jc_emlrtRSI, emlrtRootTLSGlobal);
  hamiltonian = 3.1416 / (2.0 * const_bankmax);
  b_asin(&hamiltonian);
  banktrig = -hamiltonian;
  emlrtPopRtStackR2012b(&jc_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(-hamiltonian) || muDoubleScalarIsInf(-hamiltonian)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(2.0 * const_bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(2.0 * const_bankmax * muDoubleScalarSin
    (banktrig));
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  Ttrignew = dc0.re;
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      dc0.re = const_g_re / dc0.re;
      dc0.im = 0.0;
    } else if (const_g_re == 0.0) {
      dc0.re = 0.0;
      dc0.im = const_g_im / Ttrignew;
    } else {
      dc0.re = const_g_re / dc0.re;
      dc0.im = const_g_im / Ttrignew;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      dc0.re = const_g_im / dc0.im;
      dc0.im = 0.0;
    } else if (const_g_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(const_g_re / const_C1_im);
    } else {
      dc0.re = const_g_im / dc0.im;
      dc0.im = -(const_g_re / const_C1_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      dc0.re = (const_g_re + bim * const_g_im) / lamX_im;
      dc0.im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      dc0.re = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      dc0.im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      dc0.re = (bim * const_g_re + const_g_im) / lamX_im;
      dc0.im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  rd_z.re = xAndLambda_data[2] + 50.0;
  rd_z.im = 0.0;
  dc1 = b_mpower(rd_z);
  v_re = xAndLambda_data[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda_data[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda_data[9] * muDoubleScalarCos(const_alfamax *
          muDoubleScalarSin(alfatrig)));
  ai = -(0.0 * muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)));
  if (ai == 0.0) {
    Ttrignew = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    Ttrignew = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    Ttrignew = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    xAndLambda_data[11]) * muDoubleScalarCos(const_bankmax * muDoubleScalarSin
    (banktrig));
  ai = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig));
  hamiltonian = const_mass * xAndLambda_data[3];
  lamX_im = const_mass * 0.0;
  if (lamX_im == 0.0) {
    if (ai == 0.0) {
      const_C1_re = ar / hamiltonian;
      lamY_im = 0.0;
    } else if (ar == 0.0) {
      const_C1_re = 0.0;
      lamY_im = ai / hamiltonian;
    } else {
      const_C1_re = ar / hamiltonian;
      lamY_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      const_C1_re = ai / lamX_im;
      lamY_im = 0.0;
    } else if (ai == 0.0) {
      const_C1_re = 0.0;
      lamY_im = -(ar / lamX_im);
    } else {
      const_C1_re = ai / lamX_im;
      lamY_im = -(ar / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > lamX_im) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      const_C1_re = (ar + bim * ai) / lamX_im;
      lamY_im = (ai - bim * ar) / lamX_im;
    } else if (lamX_im == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      const_C1_re = (ar * lamY_re + ai * -0.5) / 0.0;
      lamY_im = (ai * lamY_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      const_C1_re = (bim * ar + ai) / lamX_im;
      lamY_im = (bim * ai - ar) / lamX_im;
    }
  }

  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * a.re - const_mass_im * a.im;
  const_mass_im = hamiltonian * a.im + const_mass_im * a.re;
  ar = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    xAndLambda_data[10]) * muDoubleScalarSin(const_bankmax * muDoubleScalarSin
    (banktrig));
  ai = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig));
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      lamX_re = ar / const_mass_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      lamX_re = 0.0;
      hamiltonian = ai / const_mass_re;
    } else {
      lamX_re = ar / const_mass_re;
      hamiltonian = ai / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      lamX_re = ai / const_mass_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      lamX_re = 0.0;
      hamiltonian = -(ar / const_mass_im);
    } else {
      lamX_re = ai / const_mass_im;
      hamiltonian = -(ar / const_mass_im);
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      lamX_im = const_mass_re + bim * const_mass_im;
      lamX_re = (ar + bim * ai) / lamX_im;
      hamiltonian = (ai - bim * ar) / lamX_im;
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      lamX_re = (ar * lamY_re + ai * lamX_im) / brm;
      hamiltonian = (ai * lamY_re - ar * lamX_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      lamX_im = const_mass_im + bim * const_mass_re;
      lamX_re = (bim * ar + ai) / lamX_im;
      hamiltonian = (bim * ai - ar) / lamX_im;
    }
  }

  Ttrignew = (Ttrignew - const_C1_re) - lamX_re;
  const_C1_im = (const_C1_im - lamY_im) - hamiltonian;
  lamX_re = v_re * Ttrignew - v_im * const_C1_im;
  v_im = v_re * const_C1_im + v_im * Ttrignew;
  hamiltonian = 8112.0 * dc0.re;
  lamX_im = 8112.0 * dc0.im;
  if (lamX_im == 0.0) {
    if (v_im == 0.0) {
      rd_v.re = lamX_re / hamiltonian;
      rd_v.im = 0.0;
    } else if (lamX_re == 0.0) {
      rd_v.re = 0.0;
      rd_v.im = v_im / hamiltonian;
    } else {
      rd_v.re = lamX_re / hamiltonian;
      rd_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (lamX_re == 0.0) {
      rd_v.re = v_im / lamX_im;
      rd_v.im = 0.0;
    } else if (v_im == 0.0) {
      rd_v.re = 0.0;
      rd_v.im = -(lamX_re / lamX_im);
    } else {
      rd_v.re = v_im / lamX_im;
      rd_v.im = -(lamX_re / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(lamX_im);
    if (brm > bim) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      rd_v.re = (lamX_re + bim * v_im) / lamX_im;
      rd_v.im = (v_im - bim * lamX_re) / lamX_im;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (lamX_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      rd_v.re = (lamX_re * lamY_re + v_im * lamX_im) / brm;
      rd_v.im = (v_im * lamY_re - lamX_re * lamX_im) / brm;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      rd_v.re = (bim * lamX_re + v_im) / lamX_im;
      rd_v.im = (bim * v_im - lamX_re) / lamX_im;
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

  emlrtPushRtStackR2012b(&kc_emlrtRSI, emlrtRootTLSGlobal);
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
  sd_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  sd_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  v = eml_div(const_C2, sd_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + v.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0);
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + v.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * dc7.re;
  ai = const_g * dc7.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  vc_const_mass.re = const_mass * xAndLambda_data[3];
  vc_const_mass.im = const_mass * 0.0;
  dc7 = eml_div(muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig)) *
                (const_g * const_mass + muDoubleScalarSin(const_alfamax *
    muDoubleScalarSin(alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) +
    1860.0)), vc_const_mass);
  sd_z.re = xAndLambda_data[2] + 50.0;
  sd_z.im = 0.0;
  v = b_mpower(sd_z);
  v_re = xAndLambda_data[3] * v.re - 0.0 * v.im;
  v_im = xAndLambda_data[3] * v.im + 0.0 * v.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * vc_v_re + ai * vc_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc5.re - const_mass_im * dc5.im;
  const_mass_im = hamiltonian * dc5.im + const_mass_im * dc5.re;
  ar = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda_data[10] * (const_g * const_mass + muDoubleScalarSin
    (const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 * muDoubleScalarSin
    (Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (const_g * const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin
      (alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0));
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        vc_const_mass_re = 0.5;
      } else {
        vc_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        vc_const_mass_im = 0.5;
      } else {
        vc_const_mass_im = -0.5;
      }

      const_mass_re = (ar * vc_const_mass_re + ai * vc_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc6.re) - 0.0 * (const_C1_im + const_g * dc6.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc7.re) - 0.0 * (const_g_im - dc7.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * dc4.re - (lamY_re * dc3.im + lamY_im * dc3.re) * dc4.im))
    + const_mass_re;
  emlrtPopRtStackR2012b(&kc_emlrtRSI, emlrtRootTLSGlobal);
  if (hamiltonian < *hamiltonianSave) {
    *banktrigSave = banktrig;
    *alfatrigSave = alfatrig;
    *TtrignewSave = Ttrignew;
    *hamiltonianSave = hamiltonian;
  }

  /*  Coefficients */
  emlrtPushRtStackR2012b(&lc_emlrtRSI, emlrtRootTLSGlobal);
  banktrig = 3.1416 / (2.0 * const_bankmax);
  b_asin(&banktrig);
  emlrtPopRtStackR2012b(&lc_emlrtRSI, emlrtRootTLSGlobal);
  if (muDoubleScalarIsNaN(banktrig) || muDoubleScalarIsInf(banktrig)) {
    banktrig = 0.0;
  }

  /*  Coefficients */
  hamiltonian = muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig));
  a = gam;
  sec(&a);
  lamX_re = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig));
  dc0 = gam;
  sec(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[9];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[9];
  v_re = xAndLambda_data[3] * xAndLambda_data[3];
  v_im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  const_mass_re = xAndLambda_data[10] * xAndLambda_data[10];
  lamX_im = xAndLambda_data[10] * 0.0 + 0.0 * xAndLambda_data[10];
  a_re = a.re * a.re - a.im * a.im;
  lamY_re = a.re * a.im + a.im * a.re;
  lamY_im = xAndLambda_data[11] * xAndLambda_data[10];
  const_C1_re = xAndLambda_data[11] * 0.0 + 0.0 * xAndLambda_data[10];
  const_C1_im = lamY_im * dc0.im + const_C1_re * dc0.re;
  dc0.re = (((const_g_re * v_re - const_g_im * v_im) + xAndLambda_data[11] *
             xAndLambda_data[11] * (hamiltonian * hamiltonian)) + (const_mass_re
             * a_re - lamX_im * lamY_re) * (lamX_re * lamX_re)) + (lamY_im *
    dc0.re - const_C1_re * dc0.im) * muDoubleScalarSin(2.0 * const_bankmax *
    muDoubleScalarSin(banktrig));
  dc0.im = (((const_g_re * v_im + const_g_im * v_re) + (xAndLambda_data[11] *
              0.0 + 0.0 * xAndLambda_data[11]) * (hamiltonian * hamiltonian)) +
            (const_mass_re * lamY_re + lamX_im * a_re) * (lamX_re * lamX_re)) +
    const_C1_im * muDoubleScalarSin(2.0 * const_bankmax * muDoubleScalarSin
    (banktrig));
  eml_scalar_sqrt(&dc0);
  const_g_re = xAndLambda_data[9] * xAndLambda_data[3];
  const_g_im = xAndLambda_data[9] * 0.0 + 0.0 * xAndLambda_data[3];
  Ttrignew = dc0.re;
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    if (const_g_im == 0.0) {
      dc0.re = const_g_re / dc0.re;
      dc0.im = 0.0;
    } else if (const_g_re == 0.0) {
      dc0.re = 0.0;
      dc0.im = const_g_im / Ttrignew;
    } else {
      dc0.re = const_g_re / dc0.re;
      dc0.im = const_g_im / Ttrignew;
    }
  } else if (dc0.re == 0.0) {
    if (const_g_re == 0.0) {
      dc0.re = const_g_im / dc0.im;
      dc0.im = 0.0;
    } else if (const_g_im == 0.0) {
      dc0.re = 0.0;
      dc0.im = -(const_g_re / const_C1_im);
    } else {
      dc0.re = const_g_im / dc0.im;
      dc0.im = -(const_g_re / const_C1_im);
    }
  } else {
    brm = muDoubleScalarAbs(dc0.re);
    bim = muDoubleScalarAbs(dc0.im);
    if (brm > bim) {
      bim = dc0.im / dc0.re;
      lamX_im = dc0.re + bim * dc0.im;
      dc0.re = (const_g_re + bim * const_g_im) / lamX_im;
      dc0.im = (const_g_im - bim * const_g_re) / lamX_im;
    } else if (bim == brm) {
      if (dc0.re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (dc0.im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      dc0.re = (const_g_re * lamY_re + const_g_im * lamX_im) / brm;
      dc0.im = (const_g_im * lamY_re - const_g_re * lamX_im) / brm;
    } else {
      bim = dc0.re / dc0.im;
      lamX_im = dc0.im + bim * dc0.re;
      dc0.re = (bim * const_g_re + const_g_im) / lamX_im;
      dc0.im = (bim * const_g_im - const_g_re) / lamX_im;
    }
  }

  b_acos(&dc0);
  const_C1_im = dc0.im;
  if (dc0.im == 0.0) {
    dc0.re /= const_alfamax;
    dc0.im = 0.0;
  } else if (dc0.re == 0.0) {
    dc0.re = 0.0;
    dc0.im = const_C1_im / const_alfamax;
  } else {
    dc0.re /= const_alfamax;
    dc0.im = const_C1_im / const_alfamax;
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
  td_z.re = xAndLambda_data[2] + 50.0;
  td_z.im = 0.0;
  dc1 = b_mpower(td_z);
  v_re = xAndLambda_data[3] * dc1.re - 0.0 * dc1.im;
  v_im = xAndLambda_data[3] * dc1.im + 0.0 * dc1.re;
  ar = -(1560.0 * xAndLambda_data[9] * muDoubleScalarCos(const_alfamax *
          muDoubleScalarSin(alfatrig)));
  ai = -(0.0 * muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)));
  if (ai == 0.0) {
    Ttrignew = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    Ttrignew = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    Ttrignew = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    xAndLambda_data[11]) * muDoubleScalarCos(const_bankmax * muDoubleScalarSin
    (banktrig));
  ai = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig));
  hamiltonian = const_mass * xAndLambda_data[3];
  lamX_im = const_mass * 0.0;
  if (lamX_im == 0.0) {
    if (ai == 0.0) {
      const_C1_re = ar / hamiltonian;
      lamY_im = 0.0;
    } else if (ar == 0.0) {
      const_C1_re = 0.0;
      lamY_im = ai / hamiltonian;
    } else {
      const_C1_re = ar / hamiltonian;
      lamY_im = ai / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (ar == 0.0) {
      const_C1_re = ai / lamX_im;
      lamY_im = 0.0;
    } else if (ai == 0.0) {
      const_C1_re = 0.0;
      lamY_im = -(ar / lamX_im);
    } else {
      const_C1_re = ai / lamX_im;
      lamY_im = -(ar / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    if (brm > lamX_im) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      const_C1_re = (ar + bim * ai) / lamX_im;
      lamY_im = (ai - bim * ar) / lamX_im;
    } else if (lamX_im == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      const_C1_re = (ar * lamY_re + ai * -0.5) / 0.0;
      lamY_im = (ai * lamY_re - ar * -0.5) / 0.0;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      const_C1_re = (bim * ar + ai) / lamX_im;
      lamY_im = (bim * ai - ar) / lamX_im;
    }
  }

  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * a.re - const_mass_im * a.im;
  const_mass_im = hamiltonian * a.im + const_mass_im * a.re;
  ar = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    xAndLambda_data[10]) * muDoubleScalarSin(const_bankmax * muDoubleScalarSin
    (banktrig));
  ai = muDoubleScalarSin(const_alfamax * muDoubleScalarSin(alfatrig)) * 0.0 *
    muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig));
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      lamX_re = ar / const_mass_re;
      hamiltonian = 0.0;
    } else if (ar == 0.0) {
      lamX_re = 0.0;
      hamiltonian = ai / const_mass_re;
    } else {
      lamX_re = ar / const_mass_re;
      hamiltonian = ai / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      lamX_re = ai / const_mass_im;
      hamiltonian = 0.0;
    } else if (ai == 0.0) {
      lamX_re = 0.0;
      hamiltonian = -(ar / const_mass_im);
    } else {
      lamX_re = ai / const_mass_im;
      hamiltonian = -(ar / const_mass_im);
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      lamX_im = const_mass_re + bim * const_mass_im;
      lamX_re = (ar + bim * ai) / lamX_im;
      hamiltonian = (ai - bim * ar) / lamX_im;
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      lamX_re = (ar * lamY_re + ai * lamX_im) / brm;
      hamiltonian = (ai * lamY_re - ar * lamX_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      lamX_im = const_mass_im + bim * const_mass_re;
      lamX_re = (bim * ar + ai) / lamX_im;
      hamiltonian = (bim * ai - ar) / lamX_im;
    }
  }

  Ttrignew = (Ttrignew - const_C1_re) - lamX_re;
  const_C1_im = (const_C1_im - lamY_im) - hamiltonian;
  lamX_re = v_re * Ttrignew - v_im * const_C1_im;
  v_im = v_re * const_C1_im + v_im * Ttrignew;
  hamiltonian = 8112.0 * dc0.re;
  lamX_im = 8112.0 * dc0.im;
  if (lamX_im == 0.0) {
    if (v_im == 0.0) {
      td_v.re = lamX_re / hamiltonian;
      td_v.im = 0.0;
    } else if (lamX_re == 0.0) {
      td_v.re = 0.0;
      td_v.im = v_im / hamiltonian;
    } else {
      td_v.re = lamX_re / hamiltonian;
      td_v.im = v_im / hamiltonian;
    }
  } else if (hamiltonian == 0.0) {
    if (lamX_re == 0.0) {
      td_v.re = v_im / lamX_im;
      td_v.im = 0.0;
    } else if (v_im == 0.0) {
      td_v.re = 0.0;
      td_v.im = -(lamX_re / lamX_im);
    } else {
      td_v.re = v_im / lamX_im;
      td_v.im = -(lamX_re / lamX_im);
    }
  } else {
    brm = muDoubleScalarAbs(hamiltonian);
    bim = muDoubleScalarAbs(lamX_im);
    if (brm > bim) {
      bim = lamX_im / hamiltonian;
      lamX_im = hamiltonian + bim * lamX_im;
      td_v.re = (lamX_re + bim * v_im) / lamX_im;
      td_v.im = (v_im - bim * lamX_re) / lamX_im;
    } else if (bim == brm) {
      if (hamiltonian > 0.0) {
        lamY_re = 0.5;
      } else {
        lamY_re = -0.5;
      }

      if (lamX_im > 0.0) {
        lamX_im = 0.5;
      } else {
        lamX_im = -0.5;
      }

      td_v.re = (lamX_re * lamY_re + v_im * lamX_im) / brm;
      td_v.im = (v_im * lamY_re - lamX_re * lamX_im) / brm;
    } else {
      bim = hamiltonian / lamX_im;
      lamX_im += bim * hamiltonian;
      td_v.re = (bim * lamX_re + v_im) / lamX_im;
      td_v.im = (bim * v_im - lamX_re) / lamX_im;
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

  emlrtPushRtStackR2012b(&mc_emlrtRSI, emlrtRootTLSGlobal);
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
  ud_v.re = xAndLambda_data[3] * xAndLambda_data[3];
  ud_v.im = xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3];
  dc6 = eml_div(const_C2, ud_v);
  ar = (const_C1 * (xAndLambda_data[3] * xAndLambda_data[3]) + dc6.re) -
    muDoubleScalarCos(const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 *
    muDoubleScalarSin(Ttrignew) + 1860.0);
  ai = const_C1 * (xAndLambda_data[3] * 0.0 + 0.0 * xAndLambda_data[3]) + dc6.im;
  if (ai == 0.0) {
    const_C1_re = ar / const_mass;
    const_C1_im = 0.0;
  } else if (ar == 0.0) {
    const_C1_re = 0.0;
    const_C1_im = ai / const_mass;
  } else {
    const_C1_re = ar / const_mass;
    const_C1_im = ai / const_mass;
  }

  ar = const_g * gam.re;
  ai = const_g * gam.im;
  if (ai == 0.0) {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = 0.0;
  } else if (ar == 0.0) {
    const_g_re = 0.0;
    const_g_im = ai / xAndLambda_data[3];
  } else {
    const_g_re = ar / xAndLambda_data[3];
    const_g_im = ai / xAndLambda_data[3];
  }

  wc_const_mass.re = const_mass * xAndLambda_data[3];
  wc_const_mass.im = const_mass * 0.0;
  dc6 = eml_div(muDoubleScalarCos(const_bankmax * muDoubleScalarSin(banktrig)) *
                (const_g * const_mass + muDoubleScalarSin(const_alfamax *
    muDoubleScalarSin(alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) +
    1860.0)), wc_const_mass);
  ud_z.re = xAndLambda_data[2] + 50.0;
  ud_z.im = 0.0;
  dc7 = b_mpower(ud_z);
  v_re = xAndLambda_data[3] * dc7.re - 0.0 * dc7.im;
  v_im = xAndLambda_data[3] * dc7.im + 0.0 * dc7.re;
  ar = a.re * hamiltonian;
  ai = a.im * hamiltonian;
  if (v_im == 0.0) {
    if (ai == 0.0) {
      a_re = ar / v_re;
    } else if (ar == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ar / v_re;
    }
  } else if (v_re == 0.0) {
    if (ar == 0.0) {
      a_re = ai / v_im;
    } else if (ai == 0.0) {
      a_re = 0.0;
    } else {
      a_re = ai / v_im;
    }
  } else {
    brm = muDoubleScalarAbs(v_re);
    bim = muDoubleScalarAbs(v_im);
    if (brm > bim) {
      bim = v_im / v_re;
      a_re = (ar + bim * ai) / (v_re + bim * v_im);
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

      a_re = (ar * wc_v_re + ai * wc_v_im) / brm;
    } else {
      bim = v_re / v_im;
      a_re = (bim * ar + ai) / (v_im + bim * v_re);
    }
  }

  lamX_re = xAndLambda_data[6] * xAndLambda_data[3];
  lamX_im = xAndLambda_data[6] * 0.0 + 0.0 * xAndLambda_data[3];
  lamY_re = xAndLambda_data[7] * xAndLambda_data[3];
  lamY_im = xAndLambda_data[7] * 0.0 + 0.0 * xAndLambda_data[3];
  hamiltonian = const_mass * xAndLambda_data[3];
  const_mass_im = const_mass * 0.0;
  const_mass_re = hamiltonian * dc4.re - const_mass_im * dc4.im;
  const_mass_im = hamiltonian * dc4.im + const_mass_im * dc4.re;
  ar = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) *
    xAndLambda_data[10] * (const_g * const_mass + muDoubleScalarSin
    (const_alfamax * muDoubleScalarSin(alfatrig)) * (1560.0 * muDoubleScalarSin
    (Ttrignew) + 1860.0));
  ai = muDoubleScalarSin(const_bankmax * muDoubleScalarSin(banktrig)) * 0.0 *
    (const_g * const_mass + muDoubleScalarSin(const_alfamax * muDoubleScalarSin
      (alfatrig)) * (1560.0 * muDoubleScalarSin(Ttrignew) + 1860.0));
  if (const_mass_im == 0.0) {
    if (ai == 0.0) {
      const_mass_re = ar / const_mass_re;
    } else if (ar == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ar / const_mass_re;
    }
  } else if (const_mass_re == 0.0) {
    if (ar == 0.0) {
      const_mass_re = ai / const_mass_im;
    } else if (ai == 0.0) {
      const_mass_re = 0.0;
    } else {
      const_mass_re = ai / const_mass_im;
    }
  } else {
    brm = muDoubleScalarAbs(const_mass_re);
    bim = muDoubleScalarAbs(const_mass_im);
    if (brm > bim) {
      bim = const_mass_im / const_mass_re;
      const_mass_re = (ar + bim * ai) / (const_mass_re + bim * const_mass_im);
    } else if (bim == brm) {
      if (const_mass_re > 0.0) {
        wc_const_mass_re = 0.5;
      } else {
        wc_const_mass_re = -0.5;
      }

      if (const_mass_im > 0.0) {
        wc_const_mass_im = 0.5;
      } else {
        wc_const_mass_im = -0.5;
      }

      const_mass_re = (ar * wc_const_mass_re + ai * wc_const_mass_im) / brm;
    } else {
      bim = const_mass_re / const_mass_im;
      const_mass_re = (bim * ar + ai) / (const_mass_im + bim * const_mass_re);
    }
  }

  hamiltonian = ((((((xAndLambda_data[8] * xAndLambda_data[3] * dc0.re -
                      (xAndLambda_data[8] * 0.0 + 0.0 * xAndLambda_data[3]) *
                      dc0.im) - (xAndLambda_data[9] * (const_C1_re + const_g *
    dc5.re) - 0.0 * (const_C1_im + const_g * dc5.im))) - (xAndLambda_data[11] *
                     (const_g_re - dc6.re) - 0.0 * (const_g_im - dc6.im))) +
                   a_re) + ((lamX_re * dc1.re - lamX_im * dc1.im) * dc2.re -
    (lamX_re * dc1.im + lamX_im * dc1.re) * dc2.im)) + ((lamY_re * dc3.re -
    lamY_im * dc3.im) * psii.re - (lamY_re * dc3.im + lamY_im * dc3.re) *
    psii.im)) + const_mass_re;
  emlrtPopRtStackR2012b(&mc_emlrtRSI, emlrtRootTLSGlobal);
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
