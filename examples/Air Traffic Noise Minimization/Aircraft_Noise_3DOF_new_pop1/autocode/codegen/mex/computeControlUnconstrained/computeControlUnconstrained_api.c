/*
 * computeControlUnconstrained_api.c
 *
 * Code generation for function 'computeControlUnconstrained_api'
 *
 * C source code generated on: Sat Jan 21 02:01:21 2017
 *
 */

/* Include files */
#include "rt_nonfinite.h"
#include "computeControlUnconstrained.h"
#include "computeControlUnconstrained_api.h"

/* Function Declarations */
static real_T (*b_emlrt_marshallIn(const mxArray *u, const emlrtMsgIdentifier
  *parentId))[12];
static const mxArray *b_emlrt_marshallOut(real_T u);
static void b_info_helper(ResolvedFunctionInfo info[87]);
static void c_emlrt_marshallIn(const mxArray *b_const, const char_T *identifier,
  struct_T *y);
static void d_emlrt_marshallIn(const mxArray *u, const emlrtMsgIdentifier
  *parentId, struct_T *y);
static real_T e_emlrt_marshallIn(const mxArray *u, const emlrtMsgIdentifier
  *parentId);
static real_T (*emlrt_marshallIn(const mxArray *xAndLambda, const char_T
  *identifier))[12];
static const mxArray *emlrt_marshallOut(ResolvedFunctionInfo u[87]);
static void f_emlrt_marshallIn(const mxArray *constraint, const char_T
  *identifier);
static void g_emlrt_marshallIn(const mxArray *u, const emlrtMsgIdentifier
  *parentId);
static real_T h_emlrt_marshallIn(const mxArray *numArcs, const char_T
  *identifier);
static real_T (*i_emlrt_marshallIn(const mxArray *src, const emlrtMsgIdentifier *
  msgId))[12];
static void info_helper(ResolvedFunctionInfo info[87]);
static real_T j_emlrt_marshallIn(const mxArray *src, const emlrtMsgIdentifier
  *msgId);

/* Function Definitions */
static real_T (*b_emlrt_marshallIn(const mxArray *u, const emlrtMsgIdentifier
  *parentId))[12]
{
  real_T (*y)[12];
  y = i_emlrt_marshallIn(emlrtAlias(u), parentId);
  emlrtDestroyArray(&u);
  return y;
}
  static const mxArray *b_emlrt_marshallOut(real_T u)
{
  const mxArray *y;
  const mxArray *m1;
  y = NULL;
  m1 = mxCreateDoubleScalar(u);
  emlrtAssign(&y, m1);
  return y;
}

static void b_info_helper(ResolvedFunctionInfo info[87])
{
  info[64].context =
    "[E]/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m";
  info[64].name = "acos";
  info[64].dominantType = "double";
  info[64].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/acos.m";
  info[64].fileTimeLo = 1343851966U;
  info[64].fileTimeHi = 0U;
  info[64].mFileTimeLo = 0U;
  info[64].mFileTimeHi = 0U;
  info[65].context = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/acos.m";
  info[65].name = "eml_scalar_acos";
  info[65].dominantType = "double";
  info[65].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_acos.m";
  info[65].fileTimeLo = 1343851976U;
  info[65].fileTimeHi = 0U;
  info[65].mFileTimeLo = 0U;
  info[65].mFileTimeHi = 0U;
  info[66].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_acos.m";
  info[66].name = "abs";
  info[66].dominantType = "double";
  info[66].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/abs.m";
  info[66].fileTimeLo = 1343851966U;
  info[66].fileTimeHi = 0U;
  info[66].mFileTimeLo = 0U;
  info[66].mFileTimeHi = 0U;
  info[67].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_acos.m";
  info[67].name = "eml_scalar_sqrt";
  info[67].dominantType = "double";
  info[67].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_sqrt.m";
  info[67].fileTimeLo = 1286840338U;
  info[67].fileTimeHi = 0U;
  info[67].mFileTimeLo = 0U;
  info[67].mFileTimeHi = 0U;
  info[68].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_acos.m";
  info[68].name = "eml_scalar_asinh";
  info[68].dominantType = "double";
  info[68].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_asinh.m";
  info[68].fileTimeLo = 1286840318U;
  info[68].fileTimeHi = 0U;
  info[68].mFileTimeLo = 0U;
  info[68].mFileTimeHi = 0U;
  info[69].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_asinh.m";
  info[69].name = "eml_scalar_log1p";
  info[69].dominantType = "double";
  info[69].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_log1p.m";
  info[69].fileTimeLo = 1286840328U;
  info[69].fileTimeHi = 0U;
  info[69].mFileTimeLo = 0U;
  info[69].mFileTimeHi = 0U;
  info[70].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_log1p.m";
  info[70].name = "abs";
  info[70].dominantType = "double";
  info[70].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/abs.m";
  info[70].fileTimeLo = 1343851966U;
  info[70].fileTimeHi = 0U;
  info[70].mFileTimeLo = 0U;
  info[70].mFileTimeHi = 0U;
  info[71].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_log1p.m";
  info[71].name = "eps";
  info[71].dominantType = "char";
  info[71].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elmat/eps.m";
  info[71].fileTimeLo = 1326749596U;
  info[71].fileTimeHi = 0U;
  info[71].mFileTimeLo = 0U;
  info[71].mFileTimeHi = 0U;
  info[72].context = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elmat/eps.m";
  info[72].name = "eml_is_float_class";
  info[72].dominantType = "char";
  info[72].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_is_float_class.m";
  info[72].fileTimeLo = 1286840382U;
  info[72].fileTimeHi = 0U;
  info[72].mFileTimeLo = 0U;
  info[72].mFileTimeHi = 0U;
  info[73].context = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elmat/eps.m";
  info[73].name = "eml_eps";
  info[73].dominantType = "char";
  info[73].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_eps.m";
  info[73].fileTimeLo = 1326749596U;
  info[73].fileTimeHi = 0U;
  info[73].mFileTimeLo = 0U;
  info[73].mFileTimeHi = 0U;
  info[74].context = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_eps.m";
  info[74].name = "eml_float_model";
  info[74].dominantType = "char";
  info[74].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_float_model.m";
  info[74].fileTimeLo = 1326749596U;
  info[74].fileTimeHi = 0U;
  info[74].mFileTimeLo = 0U;
  info[74].mFileTimeHi = 0U;
  info[75].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_log1p.m";
  info[75].name = "isfinite";
  info[75].dominantType = "double";
  info[75].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elmat/isfinite.m";
  info[75].fileTimeLo = 1286840358U;
  info[75].fileTimeHi = 0U;
  info[75].mFileTimeLo = 0U;
  info[75].mFileTimeHi = 0U;
  info[76].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elmat/isfinite.m";
  info[76].name = "isinf";
  info[76].dominantType = "double";
  info[76].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elmat/isinf.m";
  info[76].fileTimeLo = 1286840360U;
  info[76].fileTimeHi = 0U;
  info[76].mFileTimeLo = 0U;
  info[76].mFileTimeHi = 0U;
  info[77].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elmat/isfinite.m";
  info[77].name = "isnan";
  info[77].dominantType = "double";
  info[77].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elmat/isnan.m";
  info[77].fileTimeLo = 1286840360U;
  info[77].fileTimeHi = 0U;
  info[77].mFileTimeLo = 0U;
  info[77].mFileTimeHi = 0U;
  info[78].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_log1p.m";
  info[78].name = "eml_scalar_log";
  info[78].dominantType = "double";
  info[78].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_log.m";
  info[78].fileTimeLo = 1286840328U;
  info[78].fileTimeHi = 0U;
  info[78].mFileTimeLo = 0U;
  info[78].mFileTimeHi = 0U;
  info[79].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_acos.m";
  info[79].name = "mrdivide";
  info[79].dominantType = "double";
  info[79].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/mrdivide.p";
  info[79].fileTimeLo = 1357973148U;
  info[79].fileTimeHi = 0U;
  info[79].mFileTimeLo = 1319751566U;
  info[79].mFileTimeHi = 0U;
  info[80].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_acos.m";
  info[80].name = "eml_scalar_abs";
  info[80].dominantType = "double";
  info[80].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_abs.m";
  info[80].fileTimeLo = 1286840312U;
  info[80].fileTimeHi = 0U;
  info[80].mFileTimeLo = 0U;
  info[80].mFileTimeHi = 0U;
  info[81].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_acos.m";
  info[81].name = "eml_scalar_atan2";
  info[81].dominantType = "double";
  info[81].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_atan2.m";
  info[81].fileTimeLo = 1286840320U;
  info[81].fileTimeHi = 0U;
  info[81].mFileTimeLo = 0U;
  info[81].mFileTimeHi = 0U;
  info[82].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_acos.m";
  info[82].name = "mtimes";
  info[82].dominantType = "double";
  info[82].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/mtimes.m";
  info[82].fileTimeLo = 1289541292U;
  info[82].fileTimeHi = 0U;
  info[82].mFileTimeLo = 0U;
  info[82].mFileTimeHi = 0U;
  info[83].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_asin.m";
  info[83].name = "abs";
  info[83].dominantType = "double";
  info[83].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/abs.m";
  info[83].fileTimeLo = 1343851966U;
  info[83].fileTimeHi = 0U;
  info[83].mFileTimeLo = 0U;
  info[83].mFileTimeHi = 0U;
  info[84].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_asin.m";
  info[84].name = "eml_scalar_sqrt";
  info[84].dominantType = "double";
  info[84].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_sqrt.m";
  info[84].fileTimeLo = 1286840338U;
  info[84].fileTimeHi = 0U;
  info[84].mFileTimeLo = 0U;
  info[84].mFileTimeHi = 0U;
  info[85].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_asin.m";
  info[85].name = "eml_scalar_atan2";
  info[85].dominantType = "double";
  info[85].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_atan2.m";
  info[85].fileTimeLo = 1286840320U;
  info[85].fileTimeHi = 0U;
  info[85].mFileTimeLo = 0U;
  info[85].mFileTimeHi = 0U;
  info[86].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_asin.m";
  info[86].name = "eml_scalar_asinh";
  info[86].dominantType = "double";
  info[86].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_asinh.m";
  info[86].fileTimeLo = 1286840318U;
  info[86].fileTimeHi = 0U;
  info[86].mFileTimeLo = 0U;
  info[86].mFileTimeHi = 0U;
}

static void c_emlrt_marshallIn(const mxArray *b_const, const char_T *identifier,
  struct_T *y)
{
  emlrtMsgIdentifier thisId;
  thisId.fIdentifier = identifier;
  thisId.fParent = NULL;
  d_emlrt_marshallIn(emlrtAlias(b_const), &thisId, y);
  emlrtDestroyArray(&b_const);
}

static void d_emlrt_marshallIn(const mxArray *u, const emlrtMsgIdentifier
  *parentId, struct_T *y)
{
  emlrtMsgIdentifier thisId;
  static const char * fieldNames[14] = { "Aref", "C1", "C2", "H", "Tmax", "Tmin",
    "alfamax", "bankmax", "epsilon", "g", "mass", "mu", "re", "rho0" };

  thisId.fParent = parentId;
  emlrtCheckStructR2012b(emlrtRootTLSGlobal, parentId, u, 14, fieldNames, 0U, 0);
  thisId.fIdentifier = "Aref";
  y->Aref = e_emlrt_marshallIn(emlrtAlias(emlrtGetFieldR2013a(emlrtRootTLSGlobal,
    u, 0, "Aref")), &thisId);
  thisId.fIdentifier = "C1";
  y->C1 = e_emlrt_marshallIn(emlrtAlias(emlrtGetFieldR2013a(emlrtRootTLSGlobal,
    u, 0, "C1")), &thisId);
  thisId.fIdentifier = "C2";
  y->C2 = e_emlrt_marshallIn(emlrtAlias(emlrtGetFieldR2013a(emlrtRootTLSGlobal,
    u, 0, "C2")), &thisId);
  thisId.fIdentifier = "H";
  y->H = e_emlrt_marshallIn(emlrtAlias(emlrtGetFieldR2013a(emlrtRootTLSGlobal, u,
    0, "H")), &thisId);
  thisId.fIdentifier = "Tmax";
  y->Tmax = e_emlrt_marshallIn(emlrtAlias(emlrtGetFieldR2013a(emlrtRootTLSGlobal,
    u, 0, "Tmax")), &thisId);
  thisId.fIdentifier = "Tmin";
  y->Tmin = e_emlrt_marshallIn(emlrtAlias(emlrtGetFieldR2013a(emlrtRootTLSGlobal,
    u, 0, "Tmin")), &thisId);
  thisId.fIdentifier = "alfamax";
  y->alfamax = e_emlrt_marshallIn(emlrtAlias(emlrtGetFieldR2013a
    (emlrtRootTLSGlobal, u, 0, "alfamax")), &thisId);
  thisId.fIdentifier = "bankmax";
  y->bankmax = e_emlrt_marshallIn(emlrtAlias(emlrtGetFieldR2013a
    (emlrtRootTLSGlobal, u, 0, "bankmax")), &thisId);
  thisId.fIdentifier = "epsilon";
  y->epsilon = e_emlrt_marshallIn(emlrtAlias(emlrtGetFieldR2013a
    (emlrtRootTLSGlobal, u, 0, "epsilon")), &thisId);
  thisId.fIdentifier = "g";
  y->g = e_emlrt_marshallIn(emlrtAlias(emlrtGetFieldR2013a(emlrtRootTLSGlobal, u,
    0, "g")), &thisId);
  thisId.fIdentifier = "mass";
  y->mass = e_emlrt_marshallIn(emlrtAlias(emlrtGetFieldR2013a(emlrtRootTLSGlobal,
    u, 0, "mass")), &thisId);
  thisId.fIdentifier = "mu";
  y->mu = e_emlrt_marshallIn(emlrtAlias(emlrtGetFieldR2013a(emlrtRootTLSGlobal,
    u, 0, "mu")), &thisId);
  thisId.fIdentifier = "re";
  y->re = e_emlrt_marshallIn(emlrtAlias(emlrtGetFieldR2013a(emlrtRootTLSGlobal,
    u, 0, "re")), &thisId);
  thisId.fIdentifier = "rho0";
  y->rho0 = e_emlrt_marshallIn(emlrtAlias(emlrtGetFieldR2013a(emlrtRootTLSGlobal,
    u, 0, "rho0")), &thisId);
  emlrtDestroyArray(&u);
}

static real_T e_emlrt_marshallIn(const mxArray *u, const emlrtMsgIdentifier
  *parentId)
{
  real_T y;
  y = j_emlrt_marshallIn(emlrtAlias(u), parentId);
  emlrtDestroyArray(&u);
  return y;
}

static real_T (*emlrt_marshallIn(const mxArray *xAndLambda, const char_T
  *identifier))[12]
{
  real_T (*y)[12];
  emlrtMsgIdentifier thisId;
  thisId.fIdentifier = identifier;
  thisId.fParent = NULL;
  y = b_emlrt_marshallIn(emlrtAlias(xAndLambda), &thisId);
  emlrtDestroyArray(&xAndLambda);
  return y;
}
  static const mxArray *emlrt_marshallOut(ResolvedFunctionInfo u[87])
{
  const mxArray *y;
  int32_T iv0[1];
  int32_T i0;
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
  iv0[0] = 87;
  emlrtAssign(&y, mxCreateStructArray(1, iv0, 0, NULL));
  for (i0 = 0; i0 < 87; i0++) {
    r0 = &u[i0];
    b_u = r0->context;
    b_y = NULL;
    m0 = mxCreateString(b_u);
    emlrtAssign(&b_y, m0);
    emlrtAddField(y, b_y, "context", i0);
    b_u = r0->name;
    c_y = NULL;
    m0 = mxCreateString(b_u);
    emlrtAssign(&c_y, m0);
    emlrtAddField(y, c_y, "name", i0);
    b_u = r0->dominantType;
    d_y = NULL;
    m0 = mxCreateString(b_u);
    emlrtAssign(&d_y, m0);
    emlrtAddField(y, d_y, "dominantType", i0);
    b_u = r0->resolved;
    e_y = NULL;
    m0 = mxCreateString(b_u);
    emlrtAssign(&e_y, m0);
    emlrtAddField(y, e_y, "resolved", i0);
    c_u = r0->fileTimeLo;
    f_y = NULL;
    m0 = mxCreateNumericMatrix(1, 1, mxUINT32_CLASS, mxREAL);
    *(uint32_T *)mxGetData(m0) = c_u;
    emlrtAssign(&f_y, m0);
    emlrtAddField(y, f_y, "fileTimeLo", i0);
    c_u = r0->fileTimeHi;
    g_y = NULL;
    m0 = mxCreateNumericMatrix(1, 1, mxUINT32_CLASS, mxREAL);
    *(uint32_T *)mxGetData(m0) = c_u;
    emlrtAssign(&g_y, m0);
    emlrtAddField(y, g_y, "fileTimeHi", i0);
    c_u = r0->mFileTimeLo;
    h_y = NULL;
    m0 = mxCreateNumericMatrix(1, 1, mxUINT32_CLASS, mxREAL);
    *(uint32_T *)mxGetData(m0) = c_u;
    emlrtAssign(&h_y, m0);
    emlrtAddField(y, h_y, "mFileTimeLo", i0);
    c_u = r0->mFileTimeHi;
    i_y = NULL;
    m0 = mxCreateNumericMatrix(1, 1, mxUINT32_CLASS, mxREAL);
    *(uint32_T *)mxGetData(m0) = c_u;
    emlrtAssign(&i_y, m0);
    emlrtAddField(y, i_y, "mFileTimeHi", i0);
  }

  return y;
}

static void f_emlrt_marshallIn(const mxArray *constraint, const char_T
  *identifier)
{
  emlrtMsgIdentifier thisId;
  thisId.fIdentifier = identifier;
  thisId.fParent = NULL;
  g_emlrt_marshallIn(emlrtAlias(constraint), &thisId);
  emlrtDestroyArray(&constraint);
}

static void g_emlrt_marshallIn(const mxArray *u, const emlrtMsgIdentifier
  *parentId)
{
  emlrtCheckStructR2012b(emlrtRootTLSGlobal, parentId, u, 0, NULL, 0U, 0);
  emlrtDestroyArray(&u);
}

static real_T h_emlrt_marshallIn(const mxArray *numArcs, const char_T
  *identifier)
{
  real_T y;
  emlrtMsgIdentifier thisId;
  thisId.fIdentifier = identifier;
  thisId.fParent = NULL;
  y = e_emlrt_marshallIn(emlrtAlias(numArcs), &thisId);
  emlrtDestroyArray(&numArcs);
  return y;
}

static real_T (*i_emlrt_marshallIn(const mxArray *src, const emlrtMsgIdentifier *
  msgId))[12]
{
  real_T (*ret)[12];
  int32_T iv1[1];
  iv1[0] = 12;
  emlrtCheckBuiltInR2012b(emlrtRootTLSGlobal, msgId, src, "double", FALSE, 1U,
    iv1);
  ret = (real_T (*)[12])mxGetData(src);
  emlrtDestroyArray(&src);
  return ret;
}
  static void info_helper(ResolvedFunctionInfo info[87])
{
  info[0].context =
    "[E]/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m";
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
    "[E]/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m";
  info[5].name = "mrdivide";
  info[5].dominantType = "double";
  info[5].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/mrdivide.p";
  info[5].fileTimeLo = 1357973148U;
  info[5].fileTimeHi = 0U;
  info[5].mFileTimeLo = 1319751566U;
  info[5].mFileTimeHi = 0U;
  info[6].context = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/mrdivide.p";
  info[6].name = "rdivide";
  info[6].dominantType = "double";
  info[6].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/rdivide.m";
  info[6].fileTimeLo = 1346531988U;
  info[6].fileTimeHi = 0U;
  info[6].mFileTimeLo = 0U;
  info[6].mFileTimeHi = 0U;
  info[7].context = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/rdivide.m";
  info[7].name = "eml_scalexp_compatible";
  info[7].dominantType = "double";
  info[7].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_scalexp_compatible.m";
  info[7].fileTimeLo = 1286840396U;
  info[7].fileTimeHi = 0U;
  info[7].mFileTimeLo = 0U;
  info[7].mFileTimeHi = 0U;
  info[8].context = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/rdivide.m";
  info[8].name = "eml_div";
  info[8].dominantType = "double";
  info[8].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_div.m";
  info[8].fileTimeLo = 1313369410U;
  info[8].fileTimeHi = 0U;
  info[8].mFileTimeLo = 0U;
  info[8].mFileTimeHi = 0U;
  info[9].context =
    "[E]/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m";
  info[9].name = "isnan";
  info[9].dominantType = "double";
  info[9].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elmat/isnan.m";
  info[9].fileTimeLo = 1286840360U;
  info[9].fileTimeHi = 0U;
  info[9].mFileTimeLo = 0U;
  info[9].mFileTimeHi = 0U;
  info[10].context =
    "[E]/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m";
  info[10].name = "isinf";
  info[10].dominantType = "double";
  info[10].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elmat/isinf.m";
  info[10].fileTimeLo = 1286840360U;
  info[10].fileTimeHi = 0U;
  info[10].mFileTimeLo = 0U;
  info[10].mFileTimeHi = 0U;
  info[11].context =
    "[E]/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m";
  info[11].name = "mtimes";
  info[11].dominantType = "double";
  info[11].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/mtimes.m";
  info[11].fileTimeLo = 1289541292U;
  info[11].fileTimeHi = 0U;
  info[11].mFileTimeLo = 0U;
  info[11].mFileTimeHi = 0U;
  info[12].context =
    "[E]/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m";
  info[12].name = "sin";
  info[12].dominantType = "double";
  info[12].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/sin.m";
  info[12].fileTimeLo = 1343851986U;
  info[12].fileTimeHi = 0U;
  info[12].mFileTimeLo = 0U;
  info[12].mFileTimeHi = 0U;
  info[13].context = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/sin.m";
  info[13].name = "eml_scalar_sin";
  info[13].dominantType = "double";
  info[13].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_sin.m";
  info[13].fileTimeLo = 1286840336U;
  info[13].fileTimeHi = 0U;
  info[13].mFileTimeLo = 0U;
  info[13].mFileTimeHi = 0U;
  info[14].context =
    "[E]/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m";
  info[14].name = "mpower";
  info[14].dominantType = "double";
  info[14].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/mpower.m";
  info[14].fileTimeLo = 1286840442U;
  info[14].fileTimeHi = 0U;
  info[14].mFileTimeLo = 0U;
  info[14].mFileTimeHi = 0U;
  info[15].context = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/mpower.m";
  info[15].name = "power";
  info[15].dominantType = "double";
  info[15].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/power.m";
  info[15].fileTimeLo = 1348213530U;
  info[15].fileTimeHi = 0U;
  info[15].mFileTimeLo = 0U;
  info[15].mFileTimeHi = 0U;
  info[16].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/power.m!fltpower";
  info[16].name = "eml_scalar_eg";
  info[16].dominantType = "double";
  info[16].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_scalar_eg.m";
  info[16].fileTimeLo = 1286840396U;
  info[16].fileTimeHi = 0U;
  info[16].mFileTimeLo = 0U;
  info[16].mFileTimeHi = 0U;
  info[17].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/power.m!fltpower";
  info[17].name = "eml_scalexp_alloc";
  info[17].dominantType = "double";
  info[17].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_scalexp_alloc.m";
  info[17].fileTimeLo = 1352446460U;
  info[17].fileTimeHi = 0U;
  info[17].mFileTimeLo = 0U;
  info[17].mFileTimeHi = 0U;
  info[18].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/power.m!scalar_float_power";
  info[18].name = "eml_scalar_eg";
  info[18].dominantType = "double";
  info[18].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_scalar_eg.m";
  info[18].fileTimeLo = 1286840396U;
  info[18].fileTimeHi = 0U;
  info[18].mFileTimeLo = 0U;
  info[18].mFileTimeHi = 0U;
  info[19].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/power.m!scalar_float_power";
  info[19].name = "mtimes";
  info[19].dominantType = "double";
  info[19].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/mtimes.m";
  info[19].fileTimeLo = 1289541292U;
  info[19].fileTimeHi = 0U;
  info[19].mFileTimeLo = 0U;
  info[19].mFileTimeHi = 0U;
  info[20].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_div.m!eml_fldiv";
  info[20].name = "eml_scalar_eg";
  info[20].dominantType = "double";
  info[20].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_scalar_eg.m";
  info[20].fileTimeLo = 1286840396U;
  info[20].fileTimeHi = 0U;
  info[20].mFileTimeLo = 0U;
  info[20].mFileTimeHi = 0U;
  info[21].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_div.m!eml_fldiv";
  info[21].name = "eml_scalexp_alloc";
  info[21].dominantType = "double";
  info[21].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_scalexp_alloc.m";
  info[21].fileTimeLo = 1352446460U;
  info[21].fileTimeHi = 0U;
  info[21].mFileTimeLo = 0U;
  info[21].mFileTimeHi = 0U;
  info[22].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_div.m!eml_fldiv";
  info[22].name = "abs";
  info[22].dominantType = "double";
  info[22].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/abs.m";
  info[22].fileTimeLo = 1343851966U;
  info[22].fileTimeHi = 0U;
  info[22].mFileTimeLo = 0U;
  info[22].mFileTimeHi = 0U;
  info[23].context = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/abs.m";
  info[23].name = "eml_scalar_abs";
  info[23].dominantType = "double";
  info[23].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_abs.m";
  info[23].fileTimeLo = 1286840312U;
  info[23].fileTimeHi = 0U;
  info[23].mFileTimeLo = 0U;
  info[23].mFileTimeHi = 0U;
  info[24].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_div.m!eml_fldiv";
  info[24].name = "mtimes";
  info[24].dominantType = "double";
  info[24].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/mtimes.m";
  info[24].fileTimeLo = 1289541292U;
  info[24].fileTimeHi = 0U;
  info[24].mFileTimeLo = 0U;
  info[24].mFileTimeHi = 0U;
  info[25].context =
    "[E]/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m";
  info[25].name = "cos";
  info[25].dominantType = "double";
  info[25].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/cos.m";
  info[25].fileTimeLo = 1343851972U;
  info[25].fileTimeHi = 0U;
  info[25].mFileTimeLo = 0U;
  info[25].mFileTimeHi = 0U;
  info[26].context = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/cos.m";
  info[26].name = "eml_scalar_cos";
  info[26].dominantType = "double";
  info[26].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_cos.m";
  info[26].fileTimeLo = 1286840322U;
  info[26].fileTimeHi = 0U;
  info[26].mFileTimeLo = 0U;
  info[26].mFileTimeHi = 0U;
  info[27].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/power.m!fltpower";
  info[27].name = "floor";
  info[27].dominantType = "double";
  info[27].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/floor.m";
  info[27].fileTimeLo = 1343851980U;
  info[27].fileTimeHi = 0U;
  info[27].mFileTimeLo = 0U;
  info[27].mFileTimeHi = 0U;
  info[28].context = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/floor.m";
  info[28].name = "eml_scalar_floor";
  info[28].dominantType = "double";
  info[28].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_floor.m";
  info[28].fileTimeLo = 1286840326U;
  info[28].fileTimeHi = 0U;
  info[28].mFileTimeLo = 0U;
  info[28].mFileTimeHi = 0U;
  info[29].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/power.m!fltpower";
  info[29].name = "eml_error";
  info[29].dominantType = "char";
  info[29].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_error.m";
  info[29].fileTimeLo = 1343851958U;
  info[29].fileTimeHi = 0U;
  info[29].mFileTimeLo = 0U;
  info[29].mFileTimeHi = 0U;
  info[30].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/power.m!scalar_float_power";
  info[30].name = "log";
  info[30].dominantType = "double";
  info[30].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/log.m";
  info[30].fileTimeLo = 1343851980U;
  info[30].fileTimeHi = 0U;
  info[30].mFileTimeLo = 0U;
  info[30].mFileTimeHi = 0U;
  info[31].context = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/log.m";
  info[31].name = "eml_scalar_log";
  info[31].dominantType = "double";
  info[31].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_log.m";
  info[31].fileTimeLo = 1286840328U;
  info[31].fileTimeHi = 0U;
  info[31].mFileTimeLo = 0U;
  info[31].mFileTimeHi = 0U;
  info[32].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_log.m";
  info[32].name = "realmax";
  info[32].dominantType = "char";
  info[32].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elmat/realmax.m";
  info[32].fileTimeLo = 1307672842U;
  info[32].fileTimeHi = 0U;
  info[32].mFileTimeLo = 0U;
  info[32].mFileTimeHi = 0U;
  info[33].context = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elmat/realmax.m";
  info[33].name = "eml_realmax";
  info[33].dominantType = "char";
  info[33].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_realmax.m";
  info[33].fileTimeLo = 1326749596U;
  info[33].fileTimeHi = 0U;
  info[33].mFileTimeLo = 0U;
  info[33].mFileTimeHi = 0U;
  info[34].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_realmax.m";
  info[34].name = "eml_float_model";
  info[34].dominantType = "char";
  info[34].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_float_model.m";
  info[34].fileTimeLo = 1326749596U;
  info[34].fileTimeHi = 0U;
  info[34].mFileTimeLo = 0U;
  info[34].mFileTimeHi = 0U;
  info[35].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_realmax.m";
  info[35].name = "mtimes";
  info[35].dominantType = "double";
  info[35].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/mtimes.m";
  info[35].fileTimeLo = 1289541292U;
  info[35].fileTimeHi = 0U;
  info[35].mFileTimeLo = 0U;
  info[35].mFileTimeHi = 0U;
  info[36].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_log.m";
  info[36].name = "mrdivide";
  info[36].dominantType = "double";
  info[36].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/mrdivide.p";
  info[36].fileTimeLo = 1357973148U;
  info[36].fileTimeHi = 0U;
  info[36].mFileTimeLo = 1319751566U;
  info[36].mFileTimeHi = 0U;
  info[37].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_log.m";
  info[37].name = "isnan";
  info[37].dominantType = "double";
  info[37].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elmat/isnan.m";
  info[37].fileTimeLo = 1286840360U;
  info[37].fileTimeHi = 0U;
  info[37].mFileTimeLo = 0U;
  info[37].mFileTimeHi = 0U;
  info[38].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_log.m";
  info[38].name = "eml_scalar_hypot";
  info[38].dominantType = "double";
  info[38].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_hypot.m";
  info[38].fileTimeLo = 1286840326U;
  info[38].fileTimeHi = 0U;
  info[38].mFileTimeLo = 0U;
  info[38].mFileTimeHi = 0U;
  info[39].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_hypot.m";
  info[39].name = "eml_scalar_eg";
  info[39].dominantType = "double";
  info[39].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_scalar_eg.m";
  info[39].fileTimeLo = 1286840396U;
  info[39].fileTimeHi = 0U;
  info[39].mFileTimeLo = 0U;
  info[39].mFileTimeHi = 0U;
  info[40].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_hypot.m";
  info[40].name = "eml_dlapy2";
  info[40].dominantType = "double";
  info[40].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_dlapy2.m";
  info[40].fileTimeLo = 1350432254U;
  info[40].fileTimeHi = 0U;
  info[40].mFileTimeLo = 0U;
  info[40].mFileTimeHi = 0U;
  info[41].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_log.m";
  info[41].name = "eml_scalar_atan2";
  info[41].dominantType = "double";
  info[41].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_atan2.m";
  info[41].fileTimeLo = 1286840320U;
  info[41].fileTimeHi = 0U;
  info[41].mFileTimeLo = 0U;
  info[41].mFileTimeHi = 0U;
  info[42].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_log.m";
  info[42].name = "eml_scalar_abs";
  info[42].dominantType = "double";
  info[42].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_abs.m";
  info[42].fileTimeLo = 1286840312U;
  info[42].fileTimeHi = 0U;
  info[42].mFileTimeLo = 0U;
  info[42].mFileTimeHi = 0U;
  info[43].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_abs.m";
  info[43].name = "eml_dlapy2";
  info[43].dominantType = "double";
  info[43].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_dlapy2.m";
  info[43].fileTimeLo = 1350432254U;
  info[43].fileTimeHi = 0U;
  info[43].mFileTimeLo = 0U;
  info[43].mFileTimeHi = 0U;
  info[44].context =
    "[E]/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m";
  info[44].name = "asin";
  info[44].dominantType = "double";
  info[44].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/asin.m";
  info[44].fileTimeLo = 1343851970U;
  info[44].fileTimeHi = 0U;
  info[44].mFileTimeLo = 0U;
  info[44].mFileTimeHi = 0U;
  info[45].context = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/asin.m";
  info[45].name = "eml_error";
  info[45].dominantType = "char";
  info[45].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_error.m";
  info[45].fileTimeLo = 1343851958U;
  info[45].fileTimeHi = 0U;
  info[45].mFileTimeLo = 0U;
  info[45].mFileTimeHi = 0U;
  info[46].context = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/asin.m";
  info[46].name = "eml_scalar_asin";
  info[46].dominantType = "double";
  info[46].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_asin.m";
  info[46].fileTimeLo = 1343851976U;
  info[46].fileTimeHi = 0U;
  info[46].mFileTimeLo = 0U;
  info[46].mFileTimeHi = 0U;
  info[47].context =
    "[E]/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m";
  info[47].name = "sec";
  info[47].dominantType = "double";
  info[47].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/sec.m";
  info[47].fileTimeLo = 1343851984U;
  info[47].fileTimeHi = 0U;
  info[47].mFileTimeLo = 0U;
  info[47].mFileTimeHi = 0U;
  info[48].context = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/sec.m";
  info[48].name = "eml_scalar_sec";
  info[48].dominantType = "double";
  info[48].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_sec.m";
  info[48].fileTimeLo = 1286840336U;
  info[48].fileTimeHi = 0U;
  info[48].mFileTimeLo = 0U;
  info[48].mFileTimeHi = 0U;
  info[49].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_sec.m";
  info[49].name = "eml_scalar_cos";
  info[49].dominantType = "double";
  info[49].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_cos.m";
  info[49].fileTimeLo = 1286840322U;
  info[49].fileTimeHi = 0U;
  info[49].mFileTimeLo = 0U;
  info[49].mFileTimeHi = 0U;
  info[50].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_sec.m";
  info[50].name = "eml_div";
  info[50].dominantType = "double";
  info[50].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_div.m";
  info[50].fileTimeLo = 1313369410U;
  info[50].fileTimeHi = 0U;
  info[50].mFileTimeLo = 0U;
  info[50].mFileTimeHi = 0U;
  info[51].context =
    "[E]/home/mall/mjgrant/trajProblems/Friends/Janav/Aircraft_Noise_3DOF_new_pop1/autocode/computeControlUnconstrained.m";
  info[51].name = "sqrt";
  info[51].dominantType = "double";
  info[51].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/sqrt.m";
  info[51].fileTimeLo = 1343851986U;
  info[51].fileTimeHi = 0U;
  info[51].mFileTimeLo = 0U;
  info[51].mFileTimeHi = 0U;
  info[52].context = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/sqrt.m";
  info[52].name = "eml_scalar_sqrt";
  info[52].dominantType = "double";
  info[52].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_sqrt.m";
  info[52].fileTimeLo = 1286840338U;
  info[52].fileTimeHi = 0U;
  info[52].mFileTimeLo = 0U;
  info[52].mFileTimeHi = 0U;
  info[53].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_sqrt.m!eml_complex_scalar_sqrt";
  info[53].name = "rdivide";
  info[53].dominantType = "double";
  info[53].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/rdivide.m";
  info[53].fileTimeLo = 1346531988U;
  info[53].fileTimeHi = 0U;
  info[53].mFileTimeLo = 0U;
  info[53].mFileTimeHi = 0U;
  info[54].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_sqrt.m!eml_complex_scalar_sqrt";
  info[54].name = "isnan";
  info[54].dominantType = "double";
  info[54].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elmat/isnan.m";
  info[54].fileTimeLo = 1286840360U;
  info[54].fileTimeHi = 0U;
  info[54].mFileTimeLo = 0U;
  info[54].mFileTimeHi = 0U;
  info[55].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_sqrt.m!eml_complex_scalar_sqrt";
  info[55].name = "eml_guarded_nan";
  info[55].dominantType = "char";
  info[55].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_guarded_nan.m";
  info[55].fileTimeLo = 1286840376U;
  info[55].fileTimeHi = 0U;
  info[55].mFileTimeLo = 0U;
  info[55].mFileTimeHi = 0U;
  info[56].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_guarded_nan.m";
  info[56].name = "eml_is_float_class";
  info[56].dominantType = "char";
  info[56].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_is_float_class.m";
  info[56].fileTimeLo = 1286840382U;
  info[56].fileTimeHi = 0U;
  info[56].mFileTimeLo = 0U;
  info[56].mFileTimeHi = 0U;
  info[57].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_sqrt.m!eml_complex_scalar_sqrt";
  info[57].name = "isinf";
  info[57].dominantType = "double";
  info[57].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elmat/isinf.m";
  info[57].fileTimeLo = 1286840360U;
  info[57].fileTimeHi = 0U;
  info[57].mFileTimeLo = 0U;
  info[57].mFileTimeHi = 0U;
  info[58].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_sqrt.m!eml_complex_scalar_sqrt";
  info[58].name = "eml_guarded_inf";
  info[58].dominantType = "char";
  info[58].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_guarded_inf.m";
  info[58].fileTimeLo = 1286840376U;
  info[58].fileTimeHi = 0U;
  info[58].mFileTimeLo = 0U;
  info[58].mFileTimeHi = 0U;
  info[59].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/eml/eml_guarded_inf.m";
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
  info[60].name = "realmax";
  info[60].dominantType = "char";
  info[60].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elmat/realmax.m";
  info[60].fileTimeLo = 1307672842U;
  info[60].fileTimeHi = 0U;
  info[60].mFileTimeLo = 0U;
  info[60].mFileTimeHi = 0U;
  info[61].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_sqrt.m!eml_complex_scalar_sqrt";
  info[61].name = "mrdivide";
  info[61].dominantType = "double";
  info[61].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/mrdivide.p";
  info[61].fileTimeLo = 1357973148U;
  info[61].fileTimeHi = 0U;
  info[61].mFileTimeLo = 1319751566U;
  info[61].mFileTimeHi = 0U;
  info[62].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_sqrt.m!eml_complex_scalar_sqrt";
  info[62].name = "mtimes";
  info[62].dominantType = "double";
  info[62].resolved = "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/ops/mtimes.m";
  info[62].fileTimeLo = 1289541292U;
  info[62].fileTimeHi = 0U;
  info[62].mFileTimeLo = 0U;
  info[62].mFileTimeHi = 0U;
  info[63].context =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_sqrt.m!eml_complex_scalar_sqrt";
  info[63].name = "eml_scalar_hypot";
  info[63].dominantType = "double";
  info[63].resolved =
    "[ILXE]$matlabroot$/toolbox/eml/lib/matlab/elfun/eml_scalar_hypot.m";
  info[63].fileTimeLo = 1286840326U;
  info[63].fileTimeHi = 0U;
  info[63].mFileTimeLo = 0U;
  info[63].mFileTimeHi = 0U;
}

static real_T j_emlrt_marshallIn(const mxArray *src, const emlrtMsgIdentifier
  *msgId)
{
  real_T ret;
  emlrtCheckBuiltInR2012b(emlrtRootTLSGlobal, msgId, src, "double", FALSE, 0U, 0);
  ret = *(real_T *)mxGetData(src);
  emlrtDestroyArray(&src);
  return ret;
}

void computeControlUnconstrained_api(const mxArray * const prhs[4], const
  mxArray *plhs[4])
{
  real_T (*xAndLambda)[12];
  struct_T b_const;
  real_T numArcs;
  real_T hamiltonianSave;
  real_T TtrignewSave;
  real_T alfatrigSave;
  real_T banktrigSave;

  /* Marshall function inputs */
  xAndLambda = emlrt_marshallIn(emlrtAlias(prhs[0]), "xAndLambda");
  c_emlrt_marshallIn(emlrtAliasP(prhs[1]), "const", &b_const);
  f_emlrt_marshallIn(emlrtAliasP(prhs[2]), "constraint");
  numArcs = h_emlrt_marshallIn(emlrtAliasP(prhs[3]), "numArcs");

  /* Invoke the target function */
  computeControlUnconstrained(*xAndLambda, &b_const, numArcs, &banktrigSave,
    &alfatrigSave, &TtrignewSave, &hamiltonianSave);

  /* Marshall function outputs */
  plhs[0] = b_emlrt_marshallOut(banktrigSave);
  plhs[1] = b_emlrt_marshallOut(alfatrigSave);
  plhs[2] = b_emlrt_marshallOut(TtrignewSave);
  plhs[3] = b_emlrt_marshallOut(hamiltonianSave);
}

const mxArray *emlrtMexFcnResolvedFunctionsInfo(void)
{
  const mxArray *nameCaptureInfo;
  ResolvedFunctionInfo info[87];
  nameCaptureInfo = NULL;
  info_helper(info);
  b_info_helper(info);
  emlrtAssign(&nameCaptureInfo, emlrt_marshallOut(info));
  emlrtNameCapturePostProcessR2012a(emlrtAlias(nameCaptureInfo));
  return nameCaptureInfo;
}

/* End of code generation (computeControlUnconstrained_api.c) */
