import React, { useState } from "react";
import {
  User,
  Lock,
  Eye,
  EyeOff,
  ShieldCheck,
  Activity,
  Building2,
  ChevronRight,
} from "lucide-react";

/**
 * B 端登录 / 认证页代码模板（Login Page Template）
 * 遵循本技能 02 篇「登录 / 认证页」骨架与 05 篇 W11 / W12 门禁：
 * - 宽屏左右分栏：左侧行业场景视觉，右侧集中登录表单
 * - 表单控件统一沿用既有输入框 / 按钮 / 字体 / 间距 Token，不另起样式
 * - 一屏仅一个实心登录主按钮；错误紧贴输入框行内校验
 * - 场景侧元素贴合业务，不堆砌粒子、霓虹与大面积炫光
 * - 窄屏隐藏场景面板，表单单列全宽居中
 *
 * 接入真实业务时：替换场景插画与品牌文案，对接账号密码 / 验证码校验与登录态写入，
 * 并按项目既有组件库复用输入框、按钮与校验规则。
 */

export const LoginPageTemplate: React.FC = () => {
  const [account, setAccount] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [rememberMe, setRememberMe] = useState(true);
  const [loading, setLoading] = useState(false);
  const [errors, setErrors] = useState<Record<string, string>>({});

  const handleBlurValidate = (field: "account" | "password") => {
    if (field === "account" && !account.trim()) {
      setErrors((prev) => ({ ...prev, account: "请输入账号或手机号" }));
    }
    if (field === "password" && !password) {
      setErrors((prev) => ({ ...prev, password: "请输入密码" }));
    }
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const next: Record<string, string> = {};
    if (!account.trim()) next.account = "请输入账号或手机号";
    if (!password) next.password = "请输入密码";
    setErrors(next);
    if (Object.keys(next).length > 0) return;

    setLoading(true);
    // 此处替换为真实登录请求；成功后写入登录态并跳转工作台
    window.setTimeout(() => {
      setLoading(false);
      alert("登录成功，正在进入工作台");
    }, 800);
  };

  return (
    <div className="min-h-screen flex bg-slate-50/60 text-slate-900">
      {/* 左侧：行业场景面板（窄屏隐藏） */}
      <aside className="hidden lg:flex lg:flex-1 relative overflow-hidden bg-gradient-to-br from-blue-600 via-blue-500 to-cyan-500 text-white">
        {/* 克制的氛围色块，不使用粒子 / 霓虹炫光 */}
        <div className="absolute -top-24 -right-24 w-96 h-96 rounded-full bg-white/10 blur-2xl" />
        <div className="absolute -bottom-32 -left-16 w-80 h-80 rounded-full bg-cyan-300/20 blur-2xl" />

        <div className="relative z-10 flex flex-col justify-between p-12 w-full">
          <div className="flex items-center gap-2">
            <Building2 className="w-5 h-5" />
            <span className="text-sm font-semibold tracking-wide">智慧运营平台</span>
          </div>

          <div className="space-y-6 max-w-md">
            <h1 className="text-3xl font-bold leading-snug tracking-tight">
              一个入口，
              <br />
              接入你的全部业务数据。
            </h1>
            <p className="text-sm text-white/80 leading-relaxed">
              面向医疗、安防、物流与能源等场景的统一工作台，行业化视觉氛围，配合一致的表单规范，登录即进入业务现场。
            </p>
            <div className="flex items-center gap-6 text-white/85">
              <div className="flex items-center gap-2">
                <ShieldCheck className="w-4 h-4" />
                <span className="text-xs">数据安全合规</span>
              </div>
              <div className="flex items-center gap-2">
                <Activity className="w-4 h-4" />
                <span className="text-xs">业务实时调度</span>
              </div>
            </div>
          </div>

          <p className="text-xs text-white/60">© 2026 智慧运营平台 · 仅供登录页版式参考</p>
        </div>
      </aside>

      {/* 右侧：登录表单面板 */}
      <main className="flex-1 flex items-center justify-center px-6 py-12">
        <div className="w-full max-w-sm">
          <div className="mb-8">
            <h2 className="text-xl font-bold tracking-tight">欢迎登录</h2>
            <p className="text-xs text-slate-500 mt-1">请使用业务账号登录后进入工作台</p>
          </div>

          <form onSubmit={handleSubmit} className="space-y-5" noValidate>
            {/* 账号 */}
            <div>
              <label className="block text-xs font-medium text-slate-700 mb-1">账号 / 手机号</label>
              <div className="relative">
                <User className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400" />
                <input
                  type="text"
                  placeholder="请输入账号或手机号"
                  value={account}
                  onChange={(e) => {
                    setAccount(e.target.value);
                    if (errors.account) setErrors((p) => ({ ...p, account: "" }));
                  }}
                  onBlur={() => handleBlurValidate("account")}
                  className={`w-full pl-9 pr-3 py-2.5 text-sm bg-white border rounded-lg focus:outline-none focus:ring-2 transition ${
                    errors.account
                      ? "border-rose-400 focus:ring-rose-200"
                      : "border-slate-200 focus:ring-blue-500/20 focus:border-blue-500"
                  }`}
                />
              </div>
              {errors.account ? (
                <p className="mt-1 text-xs text-rose-500">{errors.account}</p>
              ) : null}
            </div>

            {/* 密码 */}
            <div>
              <label className="block text-xs font-medium text-slate-700 mb-1">密码</label>
              <div className="relative">
                <Lock className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400" />
                <input
                  type={showPassword ? "text" : "password"}
                  placeholder="请输入密码"
                  value={password}
                  onChange={(e) => {
                    setPassword(e.target.value);
                    if (errors.password) setErrors((p) => ({ ...p, password: "" }));
                  }}
                  onBlur={() => handleBlurValidate("password")}
                  className={`w-full pl-9 pr-10 py-2.5 text-sm bg-white border rounded-lg focus:outline-none focus:ring-2 transition ${
                    errors.password
                      ? "border-rose-400 focus:ring-rose-200"
                      : "border-slate-200 focus:ring-blue-500/20 focus:border-blue-500"
                  }`}
                />
                <button
                  type="button"
                  onClick={() => setShowPassword((v) => !v)}
                  aria-label={showPassword ? "隐藏密码" : "显示密码"}
                  className="absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-600 transition"
                >
                  {showPassword ? <EyeOff className="w-4 h-4" /> : <Eye className="w-4 h-4" />}
                </button>
              </div>
              {errors.password ? (
                <p className="mt-1 text-xs text-rose-500">{errors.password}</p>
              ) : null}
            </div>

            {/* 记住我 + 忘记密码 */}
            <div className="flex items-center justify-between">
              <label className="flex items-center gap-2 cursor-pointer text-xs text-slate-600">
                <input
                  type="checkbox"
                  checked={rememberMe}
                  onChange={(e) => setRememberMe(e.target.checked)}
                  className="rounded border-slate-300 text-blue-600 focus:ring-blue-500"
                />
                记住账号
              </label>
              <button type="button" className="text-xs text-blue-600 hover:text-blue-700 transition">
                忘记密码？
              </button>
            </div>

            {/* 登录主按钮：一屏唯一 Primary，加载期锁定防重复提交 */}
            <button
              type="submit"
              disabled={loading}
              className="w-full inline-flex items-center justify-center gap-1.5 px-4 py-2.5 text-sm font-medium text-white bg-blue-600 rounded-lg hover:bg-blue-700 transition shadow-sm disabled:opacity-60 disabled:cursor-not-allowed"
            >
              {loading ? "正在登录…" : "登 录"}
              {!loading && <ChevronRight className="w-4 h-4" />}
            </button>

            {/* 注册入口：次级文字链接 */}
            <p className="text-center text-xs text-slate-500">
              还没有账号？
              <button type="button" className="ml-1 text-blue-600 hover:text-blue-700 transition">
                申请开通
              </button>
            </p>
          </form>
        </div>
      </main>
    </div>
  );
};
