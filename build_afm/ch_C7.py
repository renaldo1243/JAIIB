from qb import note, Q

note('C7', r'''
<p class="small">Syllabus: Discounted and non-discounted cash-flow methods for investment appraisal, basic concepts of term loans, deferred payment guarantees, project finance, term-loan vs project appraisal. <b>Asked: 2 questions every session on appraisal methods.</b> May 2026 asked NPV/IRR concepts, the PV comparison inside lease-vs-buy, and a ₹45 crore plant decision.</p>

<h3>1. Methods</h3>
<table><tr><th>Method</th><th>How</th><th>Decision rule</th><th>Weakness</th></tr>
<tr><td><b>Payback period</b> (non-discounted)</td><td>Time to recover the initial outlay from cash inflows</td><td>Accept if within the target period</td><td>Ignores time value and cash flows after payback</td></tr>
<tr><td><b>ARR</b> (non-discounted)</td><td>Average annual <b>accounting profit</b> ÷ average (or initial) investment</td><td>Accept if above the target</td><td>Uses profit, not cash; ignores time value</td></tr>
<tr><td><b>Discounted payback</b></td><td>Payback using discounted inflows</td><td>Accept if within the target</td><td>Still ignores flows after payback</td></tr>
<tr><td><b>NPV</b></td><td>PV of inflows − PV of outflows, at the cost of capital</td><td>Accept if NPV &gt; 0</td><td>Needs a discount rate. <b>Best for mutually exclusive projects.</b> Additive</td></tr>
<tr><td><b>IRR</b></td><td>The rate at which NPV = 0</td><td>Accept if IRR &gt; cost of capital</td><td>Multiple IRRs possible with non-conventional flows. Assumes reinvestment at the IRR</td></tr>
<tr><td><b>Profitability index (PI)</b></td><td>PV of inflows ÷ PV of outflow</td><td>Accept if PI &gt; 1</td><td>Useful under capital rationing</td></tr></table>
<p><b>Same signal:</b> NPV &gt; 0 ⇔ IRR &gt; k ⇔ PI &gt; 1, for a single conventional project.</p>
<p><b>Conflict</b> (mutually exclusive projects of different size or timing): follow <b>NPV</b>. NPV assumes reinvestment at the cost of capital, which is more realistic.</p>

<h3>2. Worked example</h3>
<p>Outlay ₹10 lakh; inflow ₹3 lakh a year for 5 years; k = 10% (PVAF 3.7908).</p>
<ul><li>PV of inflows = 11.37 → <b>NPV = +₹1.37 lakh</b>; <b>PI = 1.137</b>.</li>
<li>Payback = 10 ÷ 3 = <b>3.33 years</b>. Discounted payback ≈ <b>4.26 years</b>.</li>
<li><b>IRR ≈ 15.24%</b> (where PVAF = 10 ÷ 3 = 3.333).</li>
<li><b>ARR:</b> depreciation 2 a year, so profit 1 a year. Average investment 10 ÷ 2 = 5 → ARR = <b>20%</b>.</li></ul>
<p>Uneven flows: outlay 5; inflows 1.5, 2, 2.5, 1 → payback = 2 years + 1.5 ÷ 2.5 = <b>2.6 years</b>.</p>

<h3>3. Cash flows to use</h3>
<ul><li>Use <b>incremental, after-tax cash flows</b>.</li>
<li><b>Add back</b> depreciation (non-cash, but its tax shield counts).</li>
<li><b>Include:</b> working capital invested (and recovered at the end), salvage value, and <b>opportunity costs</b> (e.g. the rent forgone on our own building).</li>
<li><b>Ignore sunk costs</b> (a feasibility study already paid for).</li>
<li><b>Ignore financing costs</b> (interest). They are captured in the discount rate.</li></ul>

<h3>4. Term loans and project finance (banker's view)</h3>
<ul><li><b>Term loan:</b> more than 3 years (medium term 3–7, long term over 7) for fixed assets. Repaid from <b>cash accruals</b>, so the key test is <b>DSCR</b> (average 1.5–2).
<br>Other checks:
<ul><li>debt-equity (usually up to 2 : 1)</li>
<li>promoter's contribution</li>
<li>security cover</li>
<li>break-even</li>
<li>IRR</li>
<li>sensitivity</li></ul></li>
<li><b>Project appraisal</b> covers technical, economic or market, commercial, financial, managerial and environmental feasibility.
<br><b>Project finance</b> (non-recourse or limited-recourse) relies on the <b>project's own cash flows</b> through an SPV, not the sponsor's balance sheet.</li>
<li><b>Term loan appraisal vs project appraisal:</b> a term loan for an existing unit leans on its track record. A new project is appraised on projections and viability.</li>
<li><b>Deferred Payment Guarantee (DPG):</b> the bank guarantees payment of instalments to a <b>supplier of machinery</b> who sells on deferred terms. It is a non-fund facility, but carries the same credit risk as a term loan.</li></ul>

<div class="box trap"><b>Traps:</b>
<ul><li>Payback and ARR ignore time value. ARR uses <b>accounting profit</b>.</li>
<li>For mutually exclusive projects, rank by <b>NPV</b>, not IRR or PI.</li>
<li>Do not deduct interest from project cash flows.</li>
<li>Sunk costs are ignored; opportunity costs are included.</li>
<li>Comparing undiscounted totals (e.g. total lease rentals vs price) is wrong.</li></ul></div>
''')

Q('C7', """A project costs ₹10 lakh and yields ₹3 lakh a year for 5 years. Cost of capital 10% (PVAF = 3.7908). Its NPV and PI are:""",
  "NPV ₹1.37 lakh; PI 1.14", ["NPV ₹5 lakh; PI 1.50", "NPV ₹1.37 lakh; PI 0.88", "NPV −₹1.37 lakh; PI 0.86"],
  "PV of inflows = 3 × 3.7908 = 11.37. NPV = 11.37 − 10 = 1.37; PI = 11.37/10 = 1.137. ₹5 lakh is the undiscounted surplus.")

Q('C7', """For the same project (outlay ₹10 lakh, ₹3 lakh a year for 5 years), the IRR lies:""",
  "Between 15% and 16% (about 15.2%)", ["Between 10% and 11%, close to the cost of capital", "Exactly at 30%, the inflow-to-outlay ratio",
   "Below 10%, because NPV at 10% is small"],
  "IRR is where PVAF = 10/3 = 3.333. PVAF(15%, 5) = 3.352 and PVAF(16%, 5) = 3.274, so IRR ≈ 15.2%. A positive NPV at 10% already tells you IRR > 10%.")

Q('C7', """A project costing ₹5 lakh generates inflows of ₹1.5 lakh, ₹2 lakh, ₹2.5 lakh and ₹1 lakh in years 1–4. Its payback period is:""",
  "2.6 years", ["3 years", "2.5 years", "2.86 years"], "After 2 years: 3.5 recovered; 1.5 more needed out of 2.5 in year 3 → 0.6 year. Payback = 2.6 years.")

Q('C7', """An asset costs ₹10 lakh, has no salvage value and a 5-year life (SLM). It yields cash inflows of ₹3 lakh a year before depreciation; ignore tax. What is the ARR on average investment?""",
  "20%", ["30%", "10%", "60%"],
  "Annual profit = 3 − depreciation 2 = ₹1 lakh. Average investment = 10/2 = ₹5 lakh. ARR = 1/5 = 20%. Using cash flow instead of profit (3/5 = 60%) is the trap.")

Q('C7', """Projects P and Q are mutually exclusive. P: NPV ₹12 lakh, IRR 18%. Q: NPV ₹15 lakh, IRR 16%. Cost of capital 12%. Which should be chosen?""",
  "Q, because NPV directly measures the addition to shareholders' wealth",
  ["P, because a higher IRR always means the better project", "Both, because both have positive NPV and IRR above 12%",
   "Neither, because the two methods give conflicting signals"],
  "When NPV and IRR rank mutually exclusive projects differently, NPV prevails: it measures absolute value added and assumes reinvestment at the cost of capital.")

Q('C7', """In estimating cash flows of a new plant, which item should be EXCLUDED?""",
  "₹5 lakh already spent on a feasibility study last year", ["Rent the company will forgo by using its own vacant building",
   "Additional working capital needed at the start", "Tax saved because of depreciation on the plant"],
  "Sunk costs can't be recovered whatever the decision, so they are ignored. Opportunity costs, working capital and the depreciation tax shield are relevant.")

Q('C7', """Which statements are correct?
1. NPV and IRR give the same accept/reject decision for an independent conventional project.
2. IRR assumes intermediate cash flows are reinvested at the IRR.
3. The payback method considers all cash flows over the project's life.
4. A project with PI greater than 1 has positive NPV.""",
  "1, 2 and 4 only", ["1, 2, 3 and 4", "2 and 3 only", "1 and 4 only"],
  "Payback ignores cash flows after the payback date (and time value). The others are correct.")

Q('C7', """While appraising a term loan for a new project, the banker's primary test of repayment capacity is:""",
  "Debt Service Coverage Ratio based on projected cash accruals", ["Current ratio of the promoter's existing business",
   "Gross profit ratio of the first year of operations", "Market value of the collateral offered"],
  "Term loans are repaid out of cash accruals over several years; DSCR measures this. Security is a fallback, not the source of repayment.")

Q('C7', """A bank gives a guarantee to a machinery supplier that the buyer will pay the instalments of the price over 5 years. This facility is a:""",
  "Deferred Payment Guarantee, a non-fund facility with credit risk like a term loan",
  ["Bank guarantee for performance, with no credit risk to the bank", "Letter of credit for import of raw materials",
   "Cash credit facility secured by hypothecation of machinery"],
  "Under a DPG the bank guarantees deferred instalments to the supplier. No funds move upfront, but if the buyer defaults the bank pays, so it is appraised like a term loan.")

Q('C7', """In project finance (non-recourse), the lender relies mainly on:""",
  "The cash flows of the project itself, generally housed in a special purpose vehicle",
  ["The personal guarantees and net worth of the sponsors, enforced if the project fails", "The sponsor company's consolidated balance sheet and its other businesses",
   "Government budget support for the sector concerned, through viability-gap funding"],
  "Project finance is repaid from the project's own revenues; lenders have no (or limited) recourse to the sponsors.")
