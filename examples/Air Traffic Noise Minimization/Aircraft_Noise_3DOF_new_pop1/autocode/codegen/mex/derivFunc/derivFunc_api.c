/*
 * derivFunc_api.c
 *
 * Code generation for function 'derivFunc_api'
 *
 * C source code generated on: Sat Jan 21 02:02:08 2017
 *
 */

/* Include files */
#include "rt_nonfinite.h"
#include "derivFunc.h"
#include "derivFunc_api.h"

/* Function Declarations */
static real_T b_emlrt_marshallIn(const mxArray *u, const emlrtMsgIdentifier
  *parentId);
static const mxArray *b_emlrt_marshallOut(real_T u[12]);
static void b_info_helper(ResolvedFunctionInfo info[95]);
static real_T (*c_emlrt_marshallIn(const mxArray *X, const char_T *identifier))
  [12];
static real_T (*d_emlrt_marshallIn(const mxArray *u, const emlrtMsgIdentifier
  *parentId))[12];
static void e_emlrt_marshallIn(const mxArray *p, const char_T *identifier,
  real_T (**y_data)[19], int32_T y_size[1]);
static real_T emlrt_marshallIn(const mxArray *t, const char_T *identifier);
static const mxArray *emlrt_marshallOut(ResolvedFunctionInfo u[95]);
static void f_emlrt_marshallIn(const mxArray *u, const emlrtMsgIdentifier
  *parentId, real_T (**y_data)[19], int32_T y_size[1]);
static void g_emlrt_marshallIn(const mxArray *b_const, const char_T *identifier,
  struct_T *y);
static void h_emlrt_marshallIn(const mxArray *u, const emlrtMsgIdentifier
  *parentId, struct_T *y);
static void i_emlrt_marshallIn(const mxArray *constraint, const char_T
  *identifier);
static void info_helper(ResolvedFunctionInfo info[95]);
static void j_emlrt_marshallIn(const mxArray *u, const emlrtMsgIdentifier
  *parentId);
static void k_emlrt_marshallIn(const mxArray *interiorPointConstraintSequence,
  const char_T *identifier);
static void l_emlrt_marshallIn(const mxArray *u, const emlrtMsgIdentifier
  *parentId);
static real_T (*m_emlrt_marshallIn(const mxArray *x0, const char_T *identifier))
  [6];
static real_T (*n_emlrt_marshallIn(const mxArray *u, const emlrtMsgIdentifier
  *parentId))[6];
static real_T o_emlrt_marshallIn(const mxArray *src, const emlrtMsgIdentifier
  *msgId);
static real_T (*p_emlrt_marshallIn(const mxArray *src, const emlrtMsgIdentifier *
  msgId))[12];
static void q_emlrt_marshallIn(const mxArray *src, const emlrtMsgIdentifier
  *msgId, real_T (**ret_data)[19], int32_T ret_size[1]);
static void r_emlrt_marshallIn(const mxArray *src, const emlrtMsgIdentifier
  *msgId);
static real_T (*s_emlrt_marshallIn(const mxArray *src, const emlrtMsgIdentifier *
  msgId))[6];

/* Function Definitions */
static real_T b_emlrt_marshallIn(const mxArray *u, const emlrtMsgIdentifier
  *parentId)
{
  real_T y;
  y = o_emlrt_marshallIn(emlrtAlias(u), parentId);
  emlrtDestroyArray(&u);
  return y;
}

static const mxArray *b_emlrt_marshallOut(real_T u[12])
{
  const mxArray *y;
  static const int32_T iv1[1] = { 0 };

  const mxArray *m1;
  static const int32_T iv2[1] = { 12 };

  y = NULL;
  m1 = mxCreateNumericArray(1, (int32_T *)&iv1, mxDOUBLE_CLASS, mxREAL);
  mxSetData((mxArray *)m1, (void *)u);
  mxSetDimensions((mxArray *)m1, iv2, 1);
  emlrtAssign(&y, m1);
  return y;
}

static void b_info_helper(ResolvedFunctionInfo info[95])
{
  info[64].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_sqrt.m!eml_complex_scalar_sqrt";
  info[64].name = "mrdivide";
  info[64].dominantType = "double";
  info[64].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/mrdivide.p";
  info[64].fileTimeLo = 1357973148U;
  info[64].fileTimeHi = 0U;
  info[64].mFileTimeLo = 1319751566U;
  info[64].mFileTimeHi = 0U;
  info[65].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_sqrt.m!eml_complex_scalar_sqrt";
  info[65].name = "mtimes";
  info[65].dominantType = "double";
  info[65].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/mtimes.m";
  info[65].fileTimeLo = 1289541292U;
  info[65].fileTimeHi = 0U;
  info[65].mFileTimeLo = 0U;
  info[65].mFileTimeHi = 0U;
  info[66].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_sqrt.m!eml_complex_scalar_sqrt";
  info[66].name = "eml_scalar_hypot";
  info[66].dominantType = "double";
  info[66].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_hypot.m";
  info[66].fileTimeLo = 1286840326U;
  info[66].fileTimeHi = 0U;
  info[66].mFileTimeLo = 0U;
  info[66].mFileTimeHi = 0U;
  info[67].context =
    "[E]/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m";
  info[67].name = "acos";
  info[67].dominantType = "double";
  info[67].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/acos.m";
  info[67].fileTimeLo = 1343851966U;
  info[67].fileTimeHi = 0U;
  info[67].mFileTimeLo = 0U;
  info[67].mFileTimeHi = 0U;
  info[68].context = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/acos.m";
  info[68].name = "eml_scalar_acos";
  info[68].dominantType = "double";
  info[68].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_acos.m";
  info[68].fileTimeLo = 1343851976U;
  info[68].fileTimeHi = 0U;
  info[68].mFileTimeLo = 0U;
  info[68].mFileTimeHi = 0U;
  info[69].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_acos.m";
  info[69].name = "abs";
  info[69].dominantType = "double";
  info[69].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/abs.m";
  info[69].fileTimeLo = 1343851966U;
  info[69].fileTimeHi = 0U;
  info[69].mFileTimeLo = 0U;
  info[69].mFileTimeHi = 0U;
  info[70].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_acos.m";
  info[70].name = "eml_scalar_sqrt";
  info[70].dominantType = "double";
  info[70].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_sqrt.m";
  info[70].fileTimeLo = 1286840338U;
  info[70].fileTimeHi = 0U;
  info[70].mFileTimeLo = 0U;
  info[70].mFileTimeHi = 0U;
  info[71].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_acos.m";
  info[71].name = "eml_scalar_asinh";
  info[71].dominantType = "double";
  info[71].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_asinh.m";
  info[71].fileTimeLo = 1286840318U;
  info[71].fileTimeHi = 0U;
  info[71].mFileTimeLo = 0U;
  info[71].mFileTimeHi = 0U;
  info[72].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_asinh.m";
  info[72].name = "eml_scalar_log1p";
  info[72].dominantType = "double";
  info[72].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_log1p.m";
  info[72].fileTimeLo = 1286840328U;
  info[72].fileTimeHi = 0U;
  info[72].mFileTimeLo = 0U;
  info[72].mFileTimeHi = 0U;
  info[73].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_log1p.m";
  info[73].name = "abs";
  info[73].dominantType = "double";
  info[73].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/abs.m";
  info[73].fileTimeLo = 1343851966U;
  info[73].fileTimeHi = 0U;
  info[73].mFileTimeLo = 0U;
  info[73].mFileTimeHi = 0U;
  info[74].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_log1p.m";
  info[74].name = "eps";
  info[74].dominantType = "char";
  info[74].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elmat/eps.m";
  info[74].fileTimeLo = 1326749596U;
  info[74].fileTimeHi = 0U;
  info[74].mFileTimeLo = 0U;
  info[74].mFileTimeHi = 0U;
  info[75].context = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elmat/eps.m";
  info[75].name = "eml_is_float_class";
  info[75].dominantType = "char";
  info[75].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_is_float_class.m";
  info[75].fileTimeLo = 1286840382U;
  info[75].fileTimeHi = 0U;
  info[75].mFileTimeLo = 0U;
  info[75].mFileTimeHi = 0U;
  info[76].context = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elmat/eps.m";
  info[76].name = "eml_eps";
  info[76].dominantType = "char";
  info[76].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_eps.m";
  info[76].fileTimeLo = 1326749596U;
  info[76].fileTimeHi = 0U;
  info[76].mFileTimeLo = 0U;
  info[76].mFileTimeHi = 0U;
  info[77].context = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_eps.m";
  info[77].name = "eml_float_model";
  info[77].dominantType = "char";
  info[77].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_float_model.m";
  info[77].fileTimeLo = 1326749596U;
  info[77].fileTimeHi = 0U;
  info[77].mFileTimeLo = 0U;
  info[77].mFileTimeHi = 0U;
  info[78].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_log1p.m";
  info[78].name = "isfinite";
  info[78].dominantType = "double";
  info[78].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elmat/isfinite.m";
  info[78].fileTimeLo = 1286840358U;
  info[78].fileTimeHi = 0U;
  info[78].mFileTimeLo = 0U;
  info[78].mFileTimeHi = 0U;
  info[79].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elmat/isfinite.m";
  info[79].name = "isinf";
  info[79].dominantType = "double";
  info[79].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elmat/isinf.m";
  info[79].fileTimeLo = 1286840360U;
  info[79].fileTimeHi = 0U;
  info[79].mFileTimeLo = 0U;
  info[79].mFileTimeHi = 0U;
  info[80].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elmat/isfinite.m";
  info[80].name = "isnan";
  info[80].dominantType = "double";
  info[80].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elmat/isnan.m";
  info[80].fileTimeLo = 1286840360U;
  info[80].fileTimeHi = 0U;
  info[80].mFileTimeLo = 0U;
  info[80].mFileTimeHi = 0U;
  info[81].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_log1p.m";
  info[81].name = "eml_scalar_log";
  info[81].dominantType = "double";
  info[81].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_log.m";
  info[81].fileTimeLo = 1286840328U;
  info[81].fileTimeHi = 0U;
  info[81].mFileTimeLo = 0U;
  info[81].mFileTimeHi = 0U;
  info[82].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_acos.m";
  info[82].name = "mrdivide";
  info[82].dominantType = "double";
  info[82].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/mrdivide.p";
  info[82].fileTimeLo = 1357973148U;
  info[82].fileTimeHi = 0U;
  info[82].mFileTimeLo = 1319751566U;
  info[82].mFileTimeHi = 0U;
  info[83].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_acos.m";
  info[83].name = "eml_scalar_abs";
  info[83].dominantType = "double";
  info[83].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_abs.m";
  info[83].fileTimeLo = 1286840312U;
  info[83].fileTimeHi = 0U;
  info[83].mFileTimeLo = 0U;
  info[83].mFileTimeHi = 0U;
  info[84].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_acos.m";
  info[84].name = "eml_scalar_atan2";
  info[84].dominantType = "double";
  info[84].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_atan2.m";
  info[84].fileTimeLo = 1286840320U;
  info[84].fileTimeHi = 0U;
  info[84].mFileTimeLo = 0U;
  info[84].mFileTimeHi = 0U;
  info[85].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_acos.m";
  info[85].name = "mtimes";
  info[85].dominantType = "double";
  info[85].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/mtimes.m";
  info[85].fileTimeLo = 1289541292U;
  info[85].fileTimeHi = 0U;
  info[85].mFileTimeLo = 0U;
  info[85].mFileTimeHi = 0U;
  info[86].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_asin.m";
  info[86].name = "abs";
  info[86].dominantType = "double";
  info[86].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/abs.m";
  info[86].fileTimeLo = 1343851966U;
  info[86].fileTimeHi = 0U;
  info[86].mFileTimeLo = 0U;
  info[86].mFileTimeHi = 0U;
  info[87].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_asin.m";
  info[87].name = "eml_scalar_sqrt";
  info[87].dominantType = "double";
  info[87].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_sqrt.m";
  info[87].fileTimeLo = 1286840338U;
  info[87].fileTimeHi = 0U;
  info[87].mFileTimeLo = 0U;
  info[87].mFileTimeHi = 0U;
  info[88].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_asin.m";
  info[88].name = "eml_scalar_atan2";
  info[88].dominantType = "double";
  info[88].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_atan2.m";
  info[88].fileTimeLo = 1286840320U;
  info[88].fileTimeHi = 0U;
  info[88].mFileTimeLo = 0U;
  info[88].mFileTimeHi = 0U;
  info[89].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_asin.m";
  info[89].name = "eml_scalar_asinh";
  info[89].dominantType = "double";
  info[89].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_asinh.m";
  info[89].fileTimeLo = 1286840318U;
  info[89].fileTimeHi = 0U;
  info[89].mFileTimeLo = 0U;
  info[89].mFileTimeHi = 0U;
  info[90].context =
    "[E]/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/derivFunc.m";
  info[90].name = "cos";
  info[90].dominantType = "double";
  info[90].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/cos.m";
  info[90].fileTimeLo = 1343851972U;
  info[90].fileTimeHi = 0U;
  info[90].mFileTimeLo = 0U;
  info[90].mFileTimeHi = 0U;
  info[91].context =
    "[E]/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/derivFunc.m";
  info[91].name = "mtimes";
  info[91].dominantType = "double";
  info[91].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/mtimes.m";
  info[91].fileTimeLo = 1289541292U;
  info[91].fileTimeHi = 0U;
  info[91].mFileTimeLo = 0U;
  info[91].mFileTimeHi = 0U;
  info[92].context =
    "[E]/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/derivFunc.m";
  info[92].name = "sin";
  info[92].dominantType = "double";
  info[92].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/sin.m";
  info[92].fileTimeLo = 1343851986U;
  info[92].fileTimeHi = 0U;
  info[92].mFileTimeLo = 0U;
  info[92].mFileTimeHi = 0U;
  info[93].context =
    "[E]/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/derivFunc.m";
  info[93].name = "mpower";
  info[93].dominantType = "double";
  info[93].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/mpower.m";
  info[93].fileTimeLo = 1286840442U;
  info[93].fileTimeHi = 0U;
  info[93].mFileTimeLo = 0U;
  info[93].mFileTimeHi = 0U;
  info[94].context =
    "[E]/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/derivFunc.m";
  info[94].name = "mrdivide";
  info[94].dominantType = "double";
  info[94].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/mrdivide.p";
  info[94].fileTimeLo = 1357973148U;
  info[94].fileTimeHi = 0U;
  info[94].mFileTimeLo = 1319751566U;
  info[94].mFileTimeHi = 0U;
}

static real_T (*c_emlrt_marshallIn(const mxArray *X, const char_T *identifier))
  [12]
{
  real_T (*y)[12];
  emlrtMsgIdentifier thisId;
  thisId.fIdentifier = identifier;
  thisId.fParent = NULL;
  y = d_emlrt_marshallIn(emlrtAlias(X), &thisId);
  emlrtDestroyArray(&X);
  return y;
}
  static real_T (*d_emlrt_marshallIn(const mxArray *u, const emlrtMsgIdentifier *
  parentId))[12]
{
  real_T (*y)[12];
  y = p_emlrt_marshallIn(emlrtAlias(u), parentId);
  emlrtDestroyArray(&u);
  return y;
}

static void e_emlrt_marshallIn(const mxArray *p, const char_T *identifier,
  real_T (**y_data)[19], int32_T y_size[1])
{
  emlrtMsgIdentifier thisId;
  thisId.fIdentifier = identifier;
  thisId.fParent = NULL;
  f_emlrt_marshallIn(emlrtAlias(p), &thisId, y_data, y_size);
  emlrtDestroyArray(&p);
}

static real_T emlrt_marshallIn(const mxArray *t, const char_T *identifier)
{
  real_T y;
  emlrtMsgIdentifier thisId;
  thisId.fIdentifier = identifier;
  thisId.fParent = NULL;
  y = b_emlrt_marshallIn(emlrtAlias(t), &thisId);
  emlrtDestroyArray(&t);
  return y;
}

static const mxArray *emlrt_marshallOut(ResolvedFunctionInfo u[95])
{
  const mxArray *y;
  int32_T iv0[1];
  int32_T i1;
  ResolvedFunctionInfo *r0;
  const char * b_u;
  const mxArray *b_y;
  const mxArray *m0;
  const mxArray *c_y;
  const mxArray *d_y;
  const mxArray *e_y;
  uint32_T c_u;
  const mxArray *f_y;
  const mxArray *g_y;
  const mxArray *h_y;
  const mxArray *i_y;
  y = NULL;
  iv0[0] = 95;
  emlrtAssign(&y, mxCreateStructArray(1, iv0, 0, NULL));
  for (i1 = 0; i1 < 95; i1++) {
    r0 = &u[i1];
    b_u = r0->context;
    b_y = NULL;
    m0 = mxCreateString(b_u);
    emlrtAssign(&b_y, m0);
    emlrtAddField(y, b_y, "context", i1);
    b_u = r0->name;
    c_y = NULL;
    m0 = mxCreateString(b_u);
    emlrtAssign(&c_y, m0);
    emlrtAddField(y, c_y, "name", i1);
    b_u = r0->dominantType;
    d_y = NULL;
    m0 = mxCreateString(b_u);
    emlrtAssign(&d_y, m0);
    emlrtAddField(y, d_y, "dominantType", i1);
    b_u = r0->resolved;
    e_y = NULL;
    m0 = mxCreateString(b_u);
    emlrtAssign(&e_y, m0);
    emlrtAddField(y, e_y, "resolved", i1);
    c_u = r0->fileTimeLo;
    f_y = NULL;
    m0 = mxCreateNumericMatrix(1, 1, mxUINT32_CLASS, mxREAL);
    *(uint32_T *)mxGetData(m0) = c_u;
    emlrtAssign(&f_y, m0);
    emlrtAddField(y, f_y, "fileTimeLo", i1);
    c_u = r0->fileTimeHi;
    g_y = NULL;
    m0 = mxCreateNumericMatrix(1, 1, mxUINT32_CLASS, mxREAL);
    *(uint32_T *)mxGetData(m0) = c_u;
    emlrtAssign(&g_y, m0);
    emlrtAddField(y, g_y, "fileTimeHi", i1);
    c_u = r0->mFileTimeLo;
    h_y = NULL;
    m0 = mxCreateNumericMatrix(1, 1, mxUINT32_CLASS, mxREAL);
    *(uint32_T *)mxGetData(m0) = c_u;
    emlrtAssign(&h_y, m0);
    emlrtAddField(y, h_y, "mFileTimeLo", i1);
    c_u = r0->mFileTimeHi;
    i_y = NULL;
    m0 = mxCreateNumericMatrix(1, 1, mxUINT32_CLASS, mxREAL);
    *(uint32_T *)mxGetData(m0) = c_u;
    emlrtAssign(&i_y, m0);
    emlrtAddField(y, i_y, "mFileTimeHi", i1);
  }

  return y;
}

static void f_emlrt_marshallIn(const mxArray *u, const emlrtMsgIdentifier
  *parentId, real_T (**y_data)[19], int32_T y_size[1])
{
  q_emlrt_marshallIn(emlrtAlias(u), parentId, y_data, y_size);
  emlrtDestroyArray(&u);
}

static void g_emlrt_marshallIn(const mxArray *b_const, const char_T *identifier,
  struct_T *y)
{
  emlrtMsgIdentifier thisId;
  thisId.fIdentifier = identifier;
  thisId.fParent = NULL;
  h_emlrt_marshallIn(emlrtAlias(b_const), &thisId, y);
  emlrtDestroyArray(&b_const);
}

static void h_emlrt_marshallIn(const mxArray *u, const emlrtMsgIdentifier
  *parentId, struct_T *y)
{
  emlrtMsgIdentifier thisId;
  static const char * fieldNames[14] = { "Aref", "C1", "C2", "H", "Tmax", "Tmin",
    "alfamax", "bankmax", "epsilon", "g", "mass", "mu", "re", "rho0" };

  thisId.fParent = parentId;
  emlrtCheckStructR2012b(emlrtRootTLSGlobal, parentId, u, 14, fieldNames, 0U, 0);
  thisId.fIdentifier = "Aref";
  y->Aref = b_emlrt_marshallIn(emlrtAlias(emlrtGetFieldR2013a(emlrtRootTLSGlobal,
    u, 0, "Aref")), &thisId);
  thisId.fIdentifier = "C1";
  y->C1 = b_emlrt_marshallIn(emlrtAlias(emlrtGetFieldR2013a(emlrtRootTLSGlobal,
    u, 0, "C1")), &thisId);
  thisId.fIdentifier = "C2";
  y->C2 = b_emlrt_marshallIn(emlrtAlias(emlrtGetFieldR2013a(emlrtRootTLSGlobal,
    u, 0, "C2")), &thisId);
  thisId.fIdentifier = "H";
  y->H = b_emlrt_marshallIn(emlrtAlias(emlrtGetFieldR2013a(emlrtRootTLSGlobal, u,
    0, "H")), &thisId);
  thisId.fIdentifier = "Tmax";
  y->Tmax = b_emlrt_marshallIn(emlrtAlias(emlrtGetFieldR2013a(emlrtRootTLSGlobal,
    u, 0, "Tmax")), &thisId);
  thisId.fIdentifier = "Tmin";
  y->Tmin = b_emlrt_marshallIn(emlrtAlias(emlrtGetFieldR2013a(emlrtRootTLSGlobal,
    u, 0, "Tmin")), &thisId);
  thisId.fIdentifier = "alfamax";
  y->alfamax = b_emlrt_marshallIn(emlrtAlias(emlrtGetFieldR2013a
    (emlrtRootTLSGlobal, u, 0, "alfamax")), &thisId);
  thisId.fIdentifier = "bankmax";
  y->bankmax = b_emlrt_marshallIn(emlrtAlias(emlrtGetFieldR2013a
    (emlrtRootTLSGlobal, u, 0, "bankmax")), &thisId);
  thisId.fIdentifier = "epsilon";
  y->epsilon = b_emlrt_marshallIn(emlrtAlias(emlrtGetFieldR2013a
    (emlrtRootTLSGlobal, u, 0, "epsilon")), &thisId);
  thisId.fIdentifier = "g";
  y->g = b_emlrt_marshallIn(emlrtAlias(emlrtGetFieldR2013a(emlrtRootTLSGlobal, u,
    0, "g")), &thisId);
  thisId.fIdentifier = "mass";
  y->mass = b_emlrt_marshallIn(emlrtAlias(emlrtGetFieldR2013a(emlrtRootTLSGlobal,
    u, 0, "mass")), &thisId);
  thisId.fIdentifier = "mu";
  y->mu = b_emlrt_marshallIn(emlrtAlias(emlrtGetFieldR2013a(emlrtRootTLSGlobal,
    u, 0, "mu")), &thisId);
  thisId.fIdentifier = "re";
  y->re = b_emlrt_marshallIn(emlrtAlias(emlrtGetFieldR2013a(emlrtRootTLSGlobal,
    u, 0, "re")), &thisId);
  thisId.fIdentifier = "rho0";
  y->rho0 = b_emlrt_marshallIn(emlrtAlias(emlrtGetFieldR2013a(emlrtRootTLSGlobal,
    u, 0, "rho0")), &thisId);
  emlrtDestroyArray(&u);
}

static void i_emlrt_marshallIn(const mxArray *constraint, const char_T
  *identifier)
{
  emlrtMsgIdentifier thisId;
  thisId.fIdentifier = identifier;
  thisId.fParent = NULL;
  j_emlrt_marshallIn(emlrtAlias(constraint), &thisId);
  emlrtDestroyArray(&constraint);
}

static void info_helper(ResolvedFunctionInfo info[95])
{
  info[0].context =
    "[E]/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/derivFunc.m";
  info[0].name = "all";
  info[0].dominantType = "logical";
  info[0].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/all.m";
  info[0].fileTimeLo = 1286840434U;
  info[0].fileTimeHi = 0U;
  info[0].mFileTimeLo = 0U;
  info[0].mFileTimeHi = 0U;
  info[1].context = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/all.m";
  info[1].name = "eml_all_or_any";
  info[1].dominantType = "char";
  info[1].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_all_or_any.m";
  info[1].fileTimeLo = 1286840294U;
  info[1].fileTimeHi = 0U;
  info[1].mFileTimeLo = 0U;
  info[1].mFileTimeHi = 0U;
  info[2].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_all_or_any.m";
  info[2].name = "isequal";
  info[2].dominantType = "double";
  info[2].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elmat/isequal.m";
  info[2].fileTimeLo = 1286840358U;
  info[2].fileTimeHi = 0U;
  info[2].mFileTimeLo = 0U;
  info[2].mFileTimeHi = 0U;
  info[3].context = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elmat/isequal.m";
  info[3].name = "eml_isequal_core";
  info[3].dominantType = "double";
  info[3].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_isequal_core.m";
  info[3].fileTimeLo = 1286840386U;
  info[3].fileTimeHi = 0U;
  info[3].mFileTimeLo = 0U;
  info[3].mFileTimeHi = 0U;
  info[4].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_all_or_any.m";
  info[4].name = "eml_const_nonsingleton_dim";
  info[4].dominantType = "logical";
  info[4].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_const_nonsingleton_dim.m";
  info[4].fileTimeLo = 1286840296U;
  info[4].fileTimeHi = 0U;
  info[4].mFileTimeLo = 0U;
  info[4].mFileTimeHi = 0U;
  info[5].context =
    "[E]/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/derivFunc.m";
  info[5].name = "length";
  info[5].dominantType = "double";
  info[5].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elmat/length.m";
  info[5].fileTimeLo = 1303167806U;
  info[5].fileTimeHi = 0U;
  info[5].mFileTimeLo = 0U;
  info[5].mFileTimeHi = 0U;
  info[6].context =
    "[E]/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/derivFunc.m";
  info[6].name = "computeControlUnconstrained";
  info[6].dominantType = "struct";
  info[6].resolved =
    "[E]/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m";
  info[6].fileTimeLo = 1484982035U;
  info[6].fileTimeHi = 0U;
  info[6].mFileTimeLo = 0U;
  info[6].mFileTimeHi = 0U;
  info[7].context =
    "[E]/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m";
  info[7].name = "all";
  info[7].dominantType = "logical";
  info[7].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/all.m";
  info[7].fileTimeLo = 1286840434U;
  info[7].fileTimeHi = 0U;
  info[7].mFileTimeLo = 0U;
  info[7].mFileTimeHi = 0U;
  info[8].context =
    "[E]/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m";
  info[8].name = "mrdivide";
  info[8].dominantType = "double";
  info[8].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/mrdivide.p";
  info[8].fileTimeLo = 1357973148U;
  info[8].fileTimeHi = 0U;
  info[8].mFileTimeLo = 1319751566U;
  info[8].mFileTimeHi = 0U;
  info[9].context = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/mrdivide.p";
  info[9].name = "rdivide";
  info[9].dominantType = "double";
  info[9].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/rdivide.m";
  info[9].fileTimeLo = 1346531988U;
  info[9].fileTimeHi = 0U;
  info[9].mFileTimeLo = 0U;
  info[9].mFileTimeHi = 0U;
  info[10].context = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/rdivide.m";
  info[10].name = "eml_scalexp_compatible";
  info[10].dominantType = "double";
  info[10].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_scalexp_compatible.m";
  info[10].fileTimeLo = 1286840396U;
  info[10].fileTimeHi = 0U;
  info[10].mFileTimeLo = 0U;
  info[10].mFileTimeHi = 0U;
  info[11].context = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/rdivide.m";
  info[11].name = "eml_div";
  info[11].dominantType = "double";
  info[11].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_div.m";
  info[11].fileTimeLo = 1313369410U;
  info[11].fileTimeHi = 0U;
  info[11].mFileTimeLo = 0U;
  info[11].mFileTimeHi = 0U;
  info[12].context =
    "[E]/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m";
  info[12].name = "isnan";
  info[12].dominantType = "double";
  info[12].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elmat/isnan.m";
  info[12].fileTimeLo = 1286840360U;
  info[12].fileTimeHi = 0U;
  info[12].mFileTimeLo = 0U;
  info[12].mFileTimeHi = 0U;
  info[13].context =
    "[E]/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m";
  info[13].name = "isinf";
  info[13].dominantType = "double";
  info[13].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elmat/isinf.m";
  info[13].fileTimeLo = 1286840360U;
  info[13].fileTimeHi = 0U;
  info[13].mFileTimeLo = 0U;
  info[13].mFileTimeHi = 0U;
  info[14].context =
    "[E]/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m";
  info[14].name = "mtimes";
  info[14].dominantType = "double";
  info[14].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/mtimes.m";
  info[14].fileTimeLo = 1289541292U;
  info[14].fileTimeHi = 0U;
  info[14].mFileTimeLo = 0U;
  info[14].mFileTimeHi = 0U;
  info[15].context =
    "[E]/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m";
  info[15].name = "sin";
  info[15].dominantType = "double";
  info[15].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/sin.m";
  info[15].fileTimeLo = 1343851986U;
  info[15].fileTimeHi = 0U;
  info[15].mFileTimeLo = 0U;
  info[15].mFileTimeHi = 0U;
  info[16].context = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/sin.m";
  info[16].name = "eml_scalar_sin";
  info[16].dominantType = "double";
  info[16].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_sin.m";
  info[16].fileTimeLo = 1286840336U;
  info[16].fileTimeHi = 0U;
  info[16].mFileTimeLo = 0U;
  info[16].mFileTimeHi = 0U;
  info[17].context =
    "[E]/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m";
  info[17].name = "mpower";
  info[17].dominantType = "double";
  info[17].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/mpower.m";
  info[17].fileTimeLo = 1286840442U;
  info[17].fileTimeHi = 0U;
  info[17].mFileTimeLo = 0U;
  info[17].mFileTimeHi = 0U;
  info[18].context = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/mpower.m";
  info[18].name = "power";
  info[18].dominantType = "double";
  info[18].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/power.m";
  info[18].fileTimeLo = 1348213530U;
  info[18].fileTimeHi = 0U;
  info[18].mFileTimeLo = 0U;
  info[18].mFileTimeHi = 0U;
  info[19].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/power.m!fltpower";
  info[19].name = "eml_scalar_eg";
  info[19].dominantType = "double";
  info[19].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_scalar_eg.m";
  info[19].fileTimeLo = 1286840396U;
  info[19].fileTimeHi = 0U;
  info[19].mFileTimeLo = 0U;
  info[19].mFileTimeHi = 0U;
  info[20].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/power.m!fltpower";
  info[20].name = "eml_scalexp_alloc";
  info[20].dominantType = "double";
  info[20].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_scalexp_alloc.m";
  info[20].fileTimeLo = 1352446460U;
  info[20].fileTimeHi = 0U;
  info[20].mFileTimeLo = 0U;
  info[20].mFileTimeHi = 0U;
  info[21].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/power.m!scalar_float_power";
  info[21].name = "eml_scalar_eg";
  info[21].dominantType = "double";
  info[21].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_scalar_eg.m";
  info[21].fileTimeLo = 1286840396U;
  info[21].fileTimeHi = 0U;
  info[21].mFileTimeLo = 0U;
  info[21].mFileTimeHi = 0U;
  info[22].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/power.m!scalar_float_power";
  info[22].name = "mtimes";
  info[22].dominantType = "double";
  info[22].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/mtimes.m";
  info[22].fileTimeLo = 1289541292U;
  info[22].fileTimeHi = 0U;
  info[22].mFileTimeLo = 0U;
  info[22].mFileTimeHi = 0U;
  info[23].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_div.m!eml_fldiv";
  info[23].name = "eml_scalar_eg";
  info[23].dominantType = "double";
  info[23].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_scalar_eg.m";
  info[23].fileTimeLo = 1286840396U;
  info[23].fileTimeHi = 0U;
  info[23].mFileTimeLo = 0U;
  info[23].mFileTimeHi = 0U;
  info[24].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_div.m!eml_fldiv";
  info[24].name = "eml_scalexp_alloc";
  info[24].dominantType = "double";
  info[24].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_scalexp_alloc.m";
  info[24].fileTimeLo = 1352446460U;
  info[24].fileTimeHi = 0U;
  info[24].mFileTimeLo = 0U;
  info[24].mFileTimeHi = 0U;
  info[25].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_div.m!eml_fldiv";
  info[25].name = "abs";
  info[25].dominantType = "double";
  info[25].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/abs.m";
  info[25].fileTimeLo = 1343851966U;
  info[25].fileTimeHi = 0U;
  info[25].mFileTimeLo = 0U;
  info[25].mFileTimeHi = 0U;
  info[26].context = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/abs.m";
  info[26].name = "eml_scalar_abs";
  info[26].dominantType = "double";
  info[26].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_abs.m";
  info[26].fileTimeLo = 1286840312U;
  info[26].fileTimeHi = 0U;
  info[26].mFileTimeLo = 0U;
  info[26].mFileTimeHi = 0U;
  info[27].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_div.m!eml_fldiv";
  info[27].name = "mtimes";
  info[27].dominantType = "double";
  info[27].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/mtimes.m";
  info[27].fileTimeLo = 1289541292U;
  info[27].fileTimeHi = 0U;
  info[27].mFileTimeLo = 0U;
  info[27].mFileTimeHi = 0U;
  info[28].context =
    "[E]/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m";
  info[28].name = "cos";
  info[28].dominantType = "double";
  info[28].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/cos.m";
  info[28].fileTimeLo = 1343851972U;
  info[28].fileTimeHi = 0U;
  info[28].mFileTimeLo = 0U;
  info[28].mFileTimeHi = 0U;
  info[29].context = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/cos.m";
  info[29].name = "eml_scalar_cos";
  info[29].dominantType = "double";
  info[29].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_cos.m";
  info[29].fileTimeLo = 1286840322U;
  info[29].fileTimeHi = 0U;
  info[29].mFileTimeLo = 0U;
  info[29].mFileTimeHi = 0U;
  info[30].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/power.m!fltpower";
  info[30].name = "floor";
  info[30].dominantType = "double";
  info[30].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/floor.m";
  info[30].fileTimeLo = 1343851980U;
  info[30].fileTimeHi = 0U;
  info[30].mFileTimeLo = 0U;
  info[30].mFileTimeHi = 0U;
  info[31].context = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/floor.m";
  info[31].name = "eml_scalar_floor";
  info[31].dominantType = "double";
  info[31].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_floor.m";
  info[31].fileTimeLo = 1286840326U;
  info[31].fileTimeHi = 0U;
  info[31].mFileTimeLo = 0U;
  info[31].mFileTimeHi = 0U;
  info[32].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/power.m!fltpower";
  info[32].name = "eml_error";
  info[32].dominantType = "char";
  info[32].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_error.m";
  info[32].fileTimeLo = 1343851958U;
  info[32].fileTimeHi = 0U;
  info[32].mFileTimeLo = 0U;
  info[32].mFileTimeHi = 0U;
  info[33].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/power.m!scalar_float_power";
  info[33].name = "log";
  info[33].dominantType = "double";
  info[33].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/log.m";
  info[33].fileTimeLo = 1343851980U;
  info[33].fileTimeHi = 0U;
  info[33].mFileTimeLo = 0U;
  info[33].mFileTimeHi = 0U;
  info[34].context = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/log.m";
  info[34].name = "eml_scalar_log";
  info[34].dominantType = "double";
  info[34].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_log.m";
  info[34].fileTimeLo = 1286840328U;
  info[34].fileTimeHi = 0U;
  info[34].mFileTimeLo = 0U;
  info[34].mFileTimeHi = 0U;
  info[35].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_log.m";
  info[35].name = "realmax";
  info[35].dominantType = "char";
  info[35].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elmat/realmax.m";
  info[35].fileTimeLo = 1307672842U;
  info[35].fileTimeHi = 0U;
  info[35].mFileTimeLo = 0U;
  info[35].mFileTimeHi = 0U;
  info[36].context = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elmat/realmax.m";
  info[36].name = "eml_realmax";
  info[36].dominantType = "char";
  info[36].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_realmax.m";
  info[36].fileTimeLo = 1326749596U;
  info[36].fileTimeHi = 0U;
  info[36].mFileTimeLo = 0U;
  info[36].mFileTimeHi = 0U;
  info[37].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_realmax.m";
  info[37].name = "eml_float_model";
  info[37].dominantType = "char";
  info[37].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_float_model.m";
  info[37].fileTimeLo = 1326749596U;
  info[37].fileTimeHi = 0U;
  info[37].mFileTimeLo = 0U;
  info[37].mFileTimeHi = 0U;
  info[38].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_realmax.m";
  info[38].name = "mtimes";
  info[38].dominantType = "double";
  info[38].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/mtimes.m";
  info[38].fileTimeLo = 1289541292U;
  info[38].fileTimeHi = 0U;
  info[38].mFileTimeLo = 0U;
  info[38].mFileTimeHi = 0U;
  info[39].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_log.m";
  info[39].name = "mrdivide";
  info[39].dominantType = "double";
  info[39].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/mrdivide.p";
  info[39].fileTimeLo = 1357973148U;
  info[39].fileTimeHi = 0U;
  info[39].mFileTimeLo = 1319751566U;
  info[39].mFileTimeHi = 0U;
  info[40].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_log.m";
  info[40].name = "isnan";
  info[40].dominantType = "double";
  info[40].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elmat/isnan.m";
  info[40].fileTimeLo = 1286840360U;
  info[40].fileTimeHi = 0U;
  info[40].mFileTimeLo = 0U;
  info[40].mFileTimeHi = 0U;
  info[41].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_log.m";
  info[41].name = "eml_scalar_hypot";
  info[41].dominantType = "double";
  info[41].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_hypot.m";
  info[41].fileTimeLo = 1286840326U;
  info[41].fileTimeHi = 0U;
  info[41].mFileTimeLo = 0U;
  info[41].mFileTimeHi = 0U;
  info[42].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_hypot.m";
  info[42].name = "eml_scalar_eg";
  info[42].dominantType = "double";
  info[42].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_scalar_eg.m";
  info[42].fileTimeLo = 1286840396U;
  info[42].fileTimeHi = 0U;
  info[42].mFileTimeLo = 0U;
  info[42].mFileTimeHi = 0U;
  info[43].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_hypot.m";
  info[43].name = "eml_dlapy2";
  info[43].dominantType = "double";
  info[43].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_dlapy2.m";
  info[43].fileTimeLo = 1350432254U;
  info[43].fileTimeHi = 0U;
  info[43].mFileTimeLo = 0U;
  info[43].mFileTimeHi = 0U;
  info[44].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_log.m";
  info[44].name = "eml_scalar_atan2";
  info[44].dominantType = "double";
  info[44].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_atan2.m";
  info[44].fileTimeLo = 1286840320U;
  info[44].fileTimeHi = 0U;
  info[44].mFileTimeLo = 0U;
  info[44].mFileTimeHi = 0U;
  info[45].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_log.m";
  info[45].name = "eml_scalar_abs";
  info[45].dominantType = "double";
  info[45].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_abs.m";
  info[45].fileTimeLo = 1286840312U;
  info[45].fileTimeHi = 0U;
  info[45].mFileTimeLo = 0U;
  info[45].mFileTimeHi = 0U;
  info[46].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_abs.m";
  info[46].name = "eml_dlapy2";
  info[46].dominantType = "double";
  info[46].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_dlapy2.m";
  info[46].fileTimeLo = 1350432254U;
  info[46].fileTimeHi = 0U;
  info[46].mFileTimeLo = 0U;
  info[46].mFileTimeHi = 0U;
  info[47].context =
    "[E]/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m";
  info[47].name = "asin";
  info[47].dominantType = "double";
  info[47].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/asin.m";
  info[47].fileTimeLo = 1343851970U;
  info[47].fileTimeHi = 0U;
  info[47].mFileTimeLo = 0U;
  info[47].mFileTimeHi = 0U;
  info[48].context = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/asin.m";
  info[48].name = "eml_error";
  info[48].dominantType = "char";
  info[48].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_error.m";
  info[48].fileTimeLo = 1343851958U;
  info[48].fileTimeHi = 0U;
  info[48].mFileTimeLo = 0U;
  info[48].mFileTimeHi = 0U;
  info[49].context = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/asin.m";
  info[49].name = "eml_scalar_asin";
  info[49].dominantType = "double";
  info[49].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_asin.m";
  info[49].fileTimeLo = 1343851976U;
  info[49].fileTimeHi = 0U;
  info[49].mFileTimeLo = 0U;
  info[49].mFileTimeHi = 0U;
  info[50].context =
    "[E]/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m";
  info[50].name = "sec";
  info[50].dominantType = "double";
  info[50].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/sec.m";
  info[50].fileTimeLo = 1343851984U;
  info[50].fileTimeHi = 0U;
  info[50].mFileTimeLo = 0U;
  info[50].mFileTimeHi = 0U;
  info[51].context = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/sec.m";
  info[51].name = "eml_scalar_sec";
  info[51].dominantType = "double";
  info[51].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_sec.m";
  info[51].fileTimeLo = 1286840336U;
  info[51].fileTimeHi = 0U;
  info[51].mFileTimeLo = 0U;
  info[51].mFileTimeHi = 0U;
  info[52].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_sec.m";
  info[52].name = "eml_scalar_cos";
  info[52].dominantType = "double";
  info[52].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_cos.m";
  info[52].fileTimeLo = 1286840322U;
  info[52].fileTimeHi = 0U;
  info[52].mFileTimeLo = 0U;
  info[52].mFileTimeHi = 0U;
  info[53].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_sec.m";
  info[53].name = "eml_div";
  info[53].dominantType = "double";
  info[53].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_div.m";
  info[53].fileTimeLo = 1313369410U;
  info[53].fileTimeHi = 0U;
  info[53].mFileTimeLo = 0U;
  info[53].mFileTimeHi = 0U;
  info[54].context =
    "[E]/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m";
  info[54].name = "sqrt";
  info[54].dominantType = "double";
  info[54].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/sqrt.m";
  info[54].fileTimeLo = 1343851986U;
  info[54].fileTimeHi = 0U;
  info[54].mFileTimeLo = 0U;
  info[54].mFileTimeHi = 0U;
  info[55].context = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/sqrt.m";
  info[55].name = "eml_scalar_sqrt";
  info[55].dominantType = "double";
  info[55].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_sqrt.m";
  info[55].fileTimeLo = 1286840338U;
  info[55].fileTimeHi = 0U;
  info[55].mFileTimeLo = 0U;
  info[55].mFileTimeHi = 0U;
  info[56].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_sqrt.m!eml_complex_scalar_sqrt";
  info[56].name = "rdivide";
  info[56].dominantType = "double";
  info[56].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/rdivide.m";
  info[56].fileTimeLo = 1346531988U;
  info[56].fileTimeHi = 0U;
  info[56].mFileTimeLo = 0U;
  info[56].mFileTimeHi = 0U;
  info[57].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_sqrt.m!eml_complex_scalar_sqrt";
  info[57].name = "isnan";
  info[57].dominantType = "double";
  info[57].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elmat/isnan.m";
  info[57].fileTimeLo = 1286840360U;
  info[57].fileTimeHi = 0U;
  info[57].mFileTimeLo = 0U;
  info[57].mFileTimeHi = 0U;
  info[58].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_sqrt.m!eml_complex_scalar_sqrt";
  info[58].name = "eml_guarded_nan";
  info[58].dominantType = "char";
  info[58].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_guarded_nan.m";
  info[58].fileTimeLo = 1286840376U;
  info[58].fileTimeHi = 0U;
  info[58].mFileTimeLo = 0U;
  info[58].mFileTimeHi = 0U;
  info[59].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_guarded_nan.m";
  info[59].name = "eml_is_float_class";
  info[59].dominantType = "char";
  info[59].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_is_float_class.m";
  info[59].fileTimeLo = 1286840382U;
  info[59].fileTimeHi = 0U;
  info[59].mFileTimeLo = 0U;
  info[59].mFileTimeHi = 0U;
  info[60].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_sqrt.m!eml_complex_scalar_sqrt";
  info[60].name = "isinf";
  info[60].dominantType = "double";
  info[60].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elmat/isinf.m";
  info[60].fileTimeLo = 1286840360U;
  info[60].fileTimeHi = 0U;
  info[60].mFileTimeLo = 0U;
  info[60].mFileTimeHi = 0U;
  info[61].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_sqrt.m!eml_complex_scalar_sqrt";
  info[61].name = "eml_guarded_inf";
  info[61].dominantType = "char";
  info[61].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_guarded_inf.m";
  info[61].fileTimeLo = 1286840376U;
  info[61].fileTimeHi = 0U;
  info[61].mFileTimeLo = 0U;
  info[61].mFileTimeHi = 0U;
  info[62].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_guarded_inf.m";
  info[62].name = "eml_is_float_class";
  info[62].dominantType = "char";
  info[62].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_is_float_class.m";
  info[62].fileTimeLo = 1286840382U;
  info[62].fileTimeHi = 0U;
  info[62].mFileTimeLo = 0U;
  info[62].mFileTimeHi = 0U;
  info[63].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_sqrt.m!eml_complex_scalar_sqrt";
  info[63].name = "realmax";
  info[63].dominantType = "char";
  info[63].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elmat/realmax.m";
  info[63].fileTimeLo = 1307672842U;
  info[63].fileTimeHi = 0U;
  info[63].mFileTimeLo = 0U;
  info[63].mFileTimeHi = 0U;
}

static void j_emlrt_marshallIn(const mxArray *u, const emlrtMsgIdentifier
  *parentId)
{
  emlrtCheckStructR2012b(emlrtRootTLSGlobal, parentId, u, 0, NULL, 0U, 0);
  emlrtDestroyArray(&u);
}

static void k_emlrt_marshallIn(const mxArray *interiorPointConstraintSequence,
  const char_T *identifier)
{
  emlrtMsgIdentifier thisId;
  thisId.fIdentifier = identifier;
  thisId.fParent = NULL;
  l_emlrt_marshallIn(emlrtAlias(interiorPointConstraintSequence), &thisId);
  emlrtDestroyArray(&interiorPointConstraintSequence);
}

static void l_emlrt_marshallIn(const mxArray *u, const emlrtMsgIdentifier
  *parentId)
{
  r_emlrt_marshallIn(emlrtAlias(u), parentId);
  emlrtDestroyArray(&u);
}

static real_T (*m_emlrt_marshallIn(const mxArray *x0, const char_T *identifier))
  [6]
{
  real_T (*y)[6];
  emlrtMsgIdentifier thisId;
  thisId.fIdentifier = identifier;
  thisId.fParent = NULL;
  y = n_emlrt_marshallIn(emlrtAlias(x0), &thisId);
  emlrtDestroyArray(&x0);
  return y;
}
  static real_T (*n_emlrt_marshallIn(const mxArray *u, const emlrtMsgIdentifier *
  parentId))[6]
{
  real_T (*y)[6];
  y = s_emlrt_marshallIn(emlrtAlias(u), parentId);
  emlrtDestroyArray(&u);
  return y;
}

static real_T o_emlrt_marshallIn(const mxArray *src, const emlrtMsgIdentifier
  *msgId)
{
  real_T ret;
  emlrtCheckBuiltInR2012b(emlrtRootTLSGlobal, msgId, src, "double", FALSE, 0U, 0);
  ret = *(real_T *)mxGetData(src);
  emlrtDestroyArray(&src);
  return ret;
}

static real_T (*p_emlrt_marshallIn(const mxArray *src, const emlrtMsgIdentifier *
  msgId))[12]
{
  real_T (*ret)[12];
  int32_T iv3[1];
  iv3[0] = 12;
  emlrtCheckBuiltInR2012b(emlrtRootTLSGlobal, msgId, src, "double", FALSE, 1U,
    iv3);
  ret = (real_T (*)[12])mxGetData(src);
  emlrtDestroyArray(&src);
  return ret;
}
  static void q_emlrt_marshallIn(const mxArray *src, const emlrtMsgIdentifier
  *msgId, real_T (**ret_data)[19], int32_T ret_size[1])
{
  int32_T iv4[1];
  boolean_T bv0[1];
  int32_T iv5[1];
  iv4[0] = 19;
  bv0[0] = TRUE;
  emlrtCheckVsBuiltInR2012b(emlrtRootTLSGlobal, msgId, src, "double", FALSE, 1U,
    iv4, bv0, iv5);
  ret_size[0] = iv5[0];
  *ret_data = (real_T (*)[19])mxGetData(src);
  emlrtDestroyArray(&src);
}

static void r_emlrt_marshallIn(const mxArray *src, const emlrtMsgIdentifier
  *msgId)
{
  int32_T iv6[2];
  int32_T i;
  for (i = 0; i < 2; i++) {
    iv6[i] = 0;
  }

  emlrtCheckBuiltInR2012b(emlrtRootTLSGlobal, msgId, src, "double", FALSE, 2U,
    iv6);
  mxGetData(src);
  emlrtDestroyArray(&src);
}

static real_T (*s_emlrt_marshallIn(const mxArray *src, const emlrtMsgIdentifier *
  msgId))[6]
{
  real_T (*ret)[6];
  int32_T iv7[1];
  iv7[0] = 6;
  emlrtCheckBuiltInR2012b(emlrtRootTLSGlobal, msgId, src, "double", FALSE, 1U,
    iv7);
  ret = (real_T (*)[6])mxGetData(src);
  emlrtDestroyArray(&src);
  return ret;
}
  void derivFunc_api(const mxArray * const prhs[10], const mxArray *plhs[1])
{
  real_T (*xDotOut)[12];
  real_T t;
  real_T (*X)[12];
  int32_T p_size[1];
  real_T (*p_data)[19];
  struct_T b_const;
  real_T arcSequence;
  real_T (*x0)[6];
  real_T (*xf)[6];
  xDotOut = (real_T (*)[12])mxMalloc(sizeof(real_T [12]));

  /* Marshall function inputs */
  t = emlrt_marshallIn(emlrtAliasP(prhs[0]), "t");
  X = c_emlrt_marshallIn(emlrtAlias(prhs[1]), "X");
  e_emlrt_marshallIn(emlrtAlias(prhs[2]), "p", &p_data, p_size);
  g_emlrt_marshallIn(emlrtAliasP(prhs[3]), "const", &b_const);
  i_emlrt_marshallIn(emlrtAliasP(prhs[4]), "constraint");
  arcSequence = emlrt_marshallIn(emlrtAliasP(prhs[5]), "arcSequence");
  k_emlrt_marshallIn(emlrtAlias(prhs[6]), "interiorPointConstraintSequence");
  k_emlrt_marshallIn(emlrtAlias(prhs[7]), "interiorPointNumLagrangeMultipliers");
  x0 = m_emlrt_marshallIn(emlrtAlias(prhs[8]), "x0");
  xf = m_emlrt_marshallIn(emlrtAlias(prhs[9]), "xf");

  /* Invoke the target function */
  derivFunc(t, *X, *p_data, p_size, &b_const, arcSequence, *x0, *xf, *xDotOut);

  /* Marshall function outputs */
  plhs[0] = b_emlrt_marshallOut(*xDotOut);
}

const mxArray *emlrtMexFcnResolvedFunctionsInfo(void)
{
  const mxArray *nameCaptureInfo;
  ResolvedFunctionInfo info[95];
  nameCaptureInfo = NULL;
  info_helper(info);
  b_info_helper(info);
  emlrtAssign(&nameCaptureInfo, emlrt_marshallOut(info));
  emlrtNameCapturePostProcessR2012a(emlrtAlias(nameCaptureInfo));
  return nameCaptureInfo;
}

/* End of code generation (derivFunc_api.c) */
