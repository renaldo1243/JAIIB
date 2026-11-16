from qb import note, Q

note('C6', r'''
<p class="small">Syllabus: Capital structure, leverage, factors, theories (NI, NOI, traditional, MM), tax, cost of debt, preference and equity, WACC, factors affecting WACC, marginal cost of capital. <b>Asked: 1–2 questions on WACC/cost each session, plus about 1 on theories.</b> May 2026 asked:</p>
<ul class="small"><li>CAPM alpha (twice) and CAPM components</li>
<li>financial leverage</li>
<li>"WACC is only a hurdle"</li>
<li>internal factors affecting WACC</li></ul>
<p class="small">Weighted marginal cost of capital, divisional cost of capital and floatation-cost detail are left out (not asked).</p>

<h3>1. Cost of each source</h3>
<table><tr><th>Source</th><th>Formula</th><th>Note</th></tr>
<tr><td>Debt (irredeemable)</td><td>K<sub>d</sub> = I(1 − t) ÷ NP</td><td>NP = net proceeds. Interest is tax-deductible, so debt is the cheapest source</td></tr>
<tr><td>Debt (redeemable)</td><td>K<sub>d</sub> = [I(1 − t) + (RV − NP) ÷ n] ÷ [(RV + NP) ÷ 2]</td><td>10% debenture of ₹100 issued at ₹95, redeemable at par in 5 years, tax 30%: (7 + 1) ÷ 97.5 = <b>8.21%</b></td></tr>
<tr><td>Preference</td><td>K<sub>p</sub> = D ÷ NP (redeemable: like debt but no tax shield)</td><td>Dividend is not tax-deductible</td></tr>
<tr><td>Equity: dividend growth (Gordon)</td><td>K<sub>e</sub> = D<sub>1</sub> ÷ P<sub>0</sub> + g</td><td>D<sub>0</sub> ₹4, g 6%, P ₹53 → 4.24 ÷ 53 + 6% = <b>14%</b></td></tr>
<tr><td>Equity: <b>CAPM</b></td><td>K<sub>e</sub> = R<sub>f</sub> + β (R<sub>m</sub> − R<sub>f</sub>)</td><td>R<sub>f</sub> 6.5%, β 1.2, R<sub>m</sub> 13% → <b>14.3%</b>. (R<sub>m</sub> − R<sub>f</sub>) is the market risk premium</td></tr>
<tr><td>Retained earnings</td><td>K<sub>r</sub> ≈ K<sub>e</sub> (opportunity cost, no floatation cost)</td><td>Not free</td></tr></table>

<h3>2. CAPM and alpha</h3>
<ul><li>β measures <b>systematic (market) risk</b>, which can't be diversified away.
<ul><li>β &gt; 1: aggressive</li>
<li>β &lt; 1: defensive</li>
<li>β = 1: moves with the market</li></ul></li>
<li>The security market line (SML) plots required return against β.</li>
<li><b>Alpha = actual (expected) return − CAPM required return.</b> Positive alpha = the security lies above the SML (undervalued, outperforming) → buy.</li>
<li><b>Example:</b> R<sub>f</sub> 6%, R<sub>m</sub> 14%.
<ul><li>A (β 0.8, 12%): required 12.4% → α −0.4</li>
<li>B (β 1.1, 16%): required 14.8% → <b>α +1.2</b></li>
<li>C (β 1.6, 18%): required 18.8% → α −0.8</li></ul>
Only B has positive alpha.</li></ul>

<h3>3. WACC</h3>
<ul><li>WACC = Σ (weight × after-tax cost).</li>
<li>Market-value weights are preferred; book-value weights are easier.</li>
<li><b>Example:</b> equity 50% at 15%, preference 10% at 11%, debt 40% at 10% pre-tax, tax 25%.
<br>WACC = 7.5 + 1.1 + 0.4 × 7.5 = <b>11.6%</b>.</li>
<li><b>WACC is the minimum hurdle rate</b> for an average-risk project. A project much riskier than the firm needs a higher, risk-adjusted rate. "Accept every project above WACC" ignores project-specific risk.</li>
<li><b>Factors:</b>
<ul><li><b>External</b> (beyond the firm's control): level of interest rates, tax rates, market risk premium.</li>
<li><b>Internal</b> (the firm's choice): capital-structure policy, dividend policy, investment policy.</li></ul></li></ul>

<h3>4. Leverage</h3>
<table><tr><th>Leverage</th><th>Formula</th><th>Source of risk</th></tr>
<tr><td>Operating (DOL)</td><td>Contribution ÷ EBIT</td><td>Fixed <b>operating</b> costs</td></tr>
<tr><td>Financial (DFL)</td><td>EBIT ÷ EBT (= EBIT ÷ (EBIT − Interest))</td><td>Fixed-cost <b>funds</b> (debt, preference)</td></tr>
<tr><td>Combined (DCL)</td><td>DOL × DFL = Contribution ÷ EBT</td><td>Both</td></tr></table>
<ul><li><b>Example:</b> contribution 80, EBIT 50, interest 10 → DOL 1.6, DFL 1.25, <b>DCL 2.0</b>. A 10% rise in sales lifts EPS by 20%.</li>
<li><b>Trading on equity:</b> using debt raises EPS when the return on investment exceeds the cost of debt. It magnifies losses when it doesn't.</li></ul>

<h3>5. Capital structure theories</h3>
<table><tr><th>Approach</th><th>Claim</th></tr>
<tr><td><b>Net Income (NI)</b> (Durand)</td><td>More debt lowers WACC and raises firm value; K<sub>d</sub> and K<sub>e</sub> stay constant. So 100% debt is best.</td></tr>
<tr><td><b>Net Operating Income (NOI)</b> (Durand)</td><td>WACC and firm value are <b>independent</b> of capital structure. K<sub>e</sub> rises with debt and offsets the cheaper debt.</td></tr>
<tr><td><b>Traditional</b></td><td>A moderate amount of debt lowers WACC up to a point, then risk raises it. An <b>optimal capital structure exists</b>.</td></tr>
<tr><td><b>Modigliani–Miller</b> (no taxes)</td><td>Same as NOI, with arbitrage proof: value is independent of leverage.
<br><b>With corporate tax:</b> V<sub>L</sub> = V<sub>U</sub> + tD, because the interest tax shield raises value. Example: V<sub>U</sub> 100, debt 40, tax 30% → V<sub>L</sub> = 112.</td></tr></table>
<p><b>Assumptions</b> (NI/NOI/MM): no taxes (basic versions), no transaction costs, all earnings paid out, constant EBIT, perfect markets, and investors can borrow on the same terms as firms.</p>
<p><b>Factors in practice:</b> cost, risk, control (debt avoids dilution), flexibility, tax, nature of business (stable cash flows can carry more debt), market conditions.</p>

<div class="box trap"><b>Traps:</b>
<ul><li>K<sub>d</sub> uses the <b>after-tax</b> rate. Preference dividend has <b>no</b> tax shield.</li>
<li>"Retained earnings have no cost": wrong. Their cost is the opportunity cost ≈ K<sub>e</sub>.</li>
<li>Financial leverage comes from fixed-cost <b>financing</b>; operating leverage from fixed operating costs.</li>
<li>NI = debt helps; NOI = irrelevant; traditional = optimum exists.</li>
<li>Interest rates and tax rates are <b>external</b> factors affecting WACC.</li></ul></div>
''')

Q('C6', """A fund manager evaluates: A (β 0.80, expected return 12%), B (β 1.10, 16%), C (β 1.60, 18%). Risk-free rate 6%, market return 14%. Which has the highest positive alpha?""",
  "Company B, with alpha of +1.2%", ["Company C, with alpha of +2.0% because its return is highest", "Company A, with alpha of +0.4%",
   "All three have identical alpha because all lie on the security market line"],
  "Required = 6 + β × 8: A 12.4 (α −0.4), B 14.8 (α +1.2), C 18.8 (α −0.8). Only B earns more than CAPM requires.")

Q('C6', """Risk-free rate 6.5%, market return 13%, beta 1.2. The cost of equity under CAPM is:""",
  "14.3%", ["15.6%", "22.1%", "13.0%"], "Ke = 6.5 + 1.2 × (13 − 6.5) = 6.5 + 7.8 = 14.3%. 15.6% wrongly multiplies β by Rm.")

Q('C6', """A share's last dividend was ₹4, dividends grow at 6% a year, and the share price is ₹53. The cost of equity (Gordon model) is:""",
  "14%", ["13.5%", "7.5%", "12%"], "D1 = 4 × 1.06 = 4.24. Ke = 4.24/53 + 0.06 = 0.08 + 0.06 = 14%. Using D0 gives 13.5%.")

Q('C6', """10% debentures of face value ₹100 are issued at ₹95 and are redeemable at par after 5 years. Tax rate 30%. The approximate after-tax cost of debt is:""",
  "8.21%", ["7.00%", "10.53%", "7.37%"],
  "Kd = [10(1 − 0.3) + (100 − 95)/5] ÷ [(100 + 95)/2] = (7 + 1)/97.5 = 8.21%.")

Q('C6', """Capital structure: equity 50% (cost 15%), preference 10% (cost 11%), debt 40% (pre-tax cost 10%), tax 25%. The WACC is:""",
  "11.6%", ["12.6%", "13.0%", "10.6%"],
  "WACC = 0.5 × 15 + 0.1 × 11 + 0.4 × 10 × (1 − 0.25) = 7.5 + 1.1 + 3.0 = 11.6%. Ignoring the tax shield gives 12.6%.")

Q('C6', """Two mutually exclusive projects return 13% (A) and 15% (B); WACC is 12%; B carries much higher business risk. The CEO wants to accept both. Which observation is most appropriate?""",
  "WACC is only a minimum hurdle for average risk; project-specific risk and cash-flow certainty must also be weighed",
  ["Every project earning more than WACC must be accepted, whatever its risk or the other options available", "WACC is relevant only for projects financed by debt, so it cannot decide equity-funded projects",
   "Project A must be rejected because its return is lower than Project B's, whatever the risk difference"],
  "Mutually exclusive projects can't both be accepted, and a much riskier project needs a risk-adjusted hurdle above the firm's WACC.")

Q('C6', """Which of the following is NOT an internal factor affecting a firm's WACC?""",
  "The prevailing level of interest rates in the economy", ["The firm's capital-structure policy", "The firm's dividend policy", "The firm's investment policy"],
  "Interest rates, tax rates and the market risk premium are external factors the firm cannot control. Capital-structure, dividend and investment policies are internal.")

Q('C6', """Vertex needs ₹150 crore. Option I: all equity. Option II: ₹75 crore equity + ₹75 crore debt at 9%. EBIT is expected to grow strongly. The Finance Director says Option II may raise shareholders' returns despite more risk. This reflects:""",
  "Financial leverage from fixed-cost debt (trading on equity)", ["Operating leverage from fixed operating costs", "Working-capital leverage from short-term creditors",
   "Dividend leverage from paying out all profits"],
  "When return on capital exceeds the cost of debt, debt magnifies EPS: financial leverage. It also magnifies the fall in EPS if EBIT falls.")

Q('C6', """Contribution ₹80 lakh, EBIT ₹50 lakh, interest ₹10 lakh. If sales rise by 10%, EPS will rise by about:""",
  "20%", ["16%", "12.5%", "10%"],
  "DOL = 80/50 = 1.6; DFL = 50/40 = 1.25; DCL = 2.0. EPS change ≈ 2.0 × 10% = 20%.")

Q('C6', """Which capital-structure approach holds that firm value and WACC are independent of the debt-equity mix, because the cost of equity rises to offset cheaper debt?""",
  "Net Operating Income approach", ["Net Income approach", "Traditional approach", "Pecking order theory"],
  "NOI (and MM without taxes): the benefit of cheap debt is exactly offset by a rising Ke, so WACC stays constant. NI says debt lowers WACC; the traditional view says an optimum exists.")

Q('C6', """Under Modigliani–Miller with corporate taxes, an unlevered firm is worth ₹100 crore. An identical firm has ₹40 crore of debt; tax rate 30%. The levered firm's value is:""",
  "₹112 crore", ["₹100 crore", "₹140 crore", "₹88 crore"],
  "VL = VU + tD = 100 + 0.30 × 40 = ₹112 crore. The interest tax shield adds value.")

Q('C6', """Which statements about CAPM are correct?
1. Beta measures systematic (non-diversifiable) risk.
2. (Rm − Rf) is the market risk premium.
3. A security with positive alpha plots above the security market line.
4. CAPM rewards investors for unsystematic (firm-specific) risk.""",
  "1, 2 and 3 only", ["1, 2, 3 and 4", "1 and 4 only", "2 and 4 only"],
  "Unsystematic risk can be diversified away, so CAPM gives no reward for it. The other three statements are correct.")

Q('C6', """Why is debt normally the cheapest source of long-term finance for a profitable company?""",
  "Interest is tax-deductible and debt holders take less risk than shareholders, so they accept a lower return",
  ["Debt carries no obligation to pay interest in years when the company makes losses", "Debt holders get voting rights in the company that compensate them for a lower return",
   "Interest is paid out of profit after tax, so it reduces the tax liability available on equity dividends"],
  "Fixed claim, priority in repayment and the tax shield (Kd × (1 − t)) make debt cheaper. Interest must be paid even in losses, which is the risk to the firm.")
