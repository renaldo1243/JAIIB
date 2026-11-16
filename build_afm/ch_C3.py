from qb import note, Q, money

note('C3', r'''
<p class="small">Syllabus: Simple and compound interest, fixed and floating rates, front-end and back-end rates, interest on products/balances, ordinary annuity and annuity due (FV and PV), repayment of debt. <b>Asked: 2 questions on SI/CI, 1–2 on annuity and 1 on PV/FV every session.</b> May 2026 asked:</p>
<ul class="small"><li>growth compounding</li>
<li>FV at 9% and 11%</li>
<li>quarterly compounding</li>
<li>lease vs purchase by PV of annuity (three times)</li>
<li>EAR</li>
<li>EMI with a processing fee</li>
<li>timing of ordinary annuity payments</li></ul>

<h3>1. Formula bank</h3>
<table><tr><th>What</th><th>Formula</th><th>Note</th></tr>
<tr><td>Simple interest</td><td>SI = P × r × t</td><td>t in years (9 months = 0.75)</td></tr>
<tr><td>Compound amount</td><td>A = P (1 + r/m)<sup>m×n</sup></td><td>m = compounding periods per year</td></tr>
<tr><td>Effective annual rate</td><td>EAR = (1 + r/m)<sup>m</sup> − 1</td><td>Compare loans with different compounding by EAR, not nominal rate</td></tr>
<tr><td>Present value</td><td>PV = A ÷ (1 + r)<sup>n</sup></td><td>Discounting</td></tr>
<tr><td>FV of ordinary annuity</td><td>A × [(1 + r)<sup>n</sup> − 1] ÷ r</td><td>Payments at the <b>end</b> of each period</td></tr>
<tr><td>PV of ordinary annuity</td><td>A × [1 − (1 + r)<sup>−n</sup>] ÷ r = A × PVAF</td><td></td></tr>
<tr><td>Annuity due (FV or PV)</td><td>Ordinary-annuity value × (1 + r)</td><td>Payments at the <b>beginning</b> (rent, insurance premium, lease paid in advance)</td></tr>
<tr><td>Perpetuity</td><td>PV = A ÷ r</td><td></td></tr>
<tr><td>EMI</td><td>P × i × (1 + i)<sup>n</sup> ÷ [(1 + i)<sup>n</sup> − 1]</td><td>i = monthly rate, n = months</td></tr>
<tr><td>Rule of 72</td><td>Years to double ≈ 72 ÷ rate%</td><td>Rule of 114 to triple, 144 to quadruple. Rule of 69 for continuous compounding</td></tr></table>

<h3>2. Worked numbers</h3>
<ul><li>₹24,000 for 9 months at 8% simple interest → 24,000 × 0.08 × 0.75 = <b>₹1,440</b>.</li>
<li>₹10,000 for 1 year at 12% compounded quarterly → 10,000 × 1.03<sup>4</sup> = <b>₹11,255</b>. EAR at 12% monthly = <b>12.68%</b>.</li>
<li>₹8 lakh at 9% compound for 4 years (1.09<sup>4</sup> = 1.4116) → <b>₹11.29 lakh</b>. At 10% simple interest → ₹11.20 lakh. Compound wins.</li>
<li>Population of 10 lakh growing at 5% → after 3 years <b>11,57,625</b>.</li>
<li>₹50,000 at the end of each year for 20 years at 8% → FV = <b>₹22,88,098</b>.</li>
<li>₹2 lakh at the end of each year for 10 years at 9% → FV = <b>₹30,38,586</b>.</li>
<li>₹10,000 a year for 5 years at 8%: ordinary FV = 58,666; annuity due FV = <b>63,359</b>.</li>
<li><b>Lease vs buy:</b> lease ₹12 lakh at the end of each year for 5 years, PVAF(10%, 5) = 3.7908 → PV = <b>₹45.49 lakh</b>. That is less than the ₹47.5 lakh purchase price, so lease. Comparing totals (₹60 lakh vs ₹47.5 lakh) is the trap.</li>
<li><b>EMI:</b> ₹10 lakh, 9% p.a., 5 years → i = 0.75%, n = 60 → <b>₹20,758</b>.
<ul><li>First month's interest = ₹7,500, so ₹13,258 of the EMI goes to principal.</li>
<li>Interest share falls each month (reducing balance).</li></ul></li>
<li>Rule of 72 at 9% → 8 years (exact 8.04). Money doubling in 6 years → about 12%.</li></ul>

<h3>3. Interest concepts banks use</h3>
<ul><li><b>Fixed rate:</b> constant for the tenure. <b>Floating rate:</b> linked to an external benchmark (repo-linked EBLR for retail and MSME floating loans since Oct 2019) plus a spread, and reset at least once in 3 months.</li>
<li><b>Front-end rate:</b> interest is collected at the start (discounting), so the borrower gets less money and the effective rate is higher. ₹1 lakh at 10% discounted for a year → ₹90,000 received → effective rate <b>11.11%</b>.
<br><b>Back-end rate:</b> interest is paid at the end.</li>
<li><b>Interest on products:</b> savings accounts → interest on the <b>daily closing balance</b>, credited at least quarterly. Cash credit → interest on daily debit balances, charged monthly. The product method sums balance × days, then applies rate ÷ 365.</li>
<li><b>Compounding on loans:</b> at monthly rests the EAR is higher than the quoted rate.</li>
<li><b>Processing fee:</b> raises the effective cost. Compare the all-in cost (IRR of net cash flows), not just the EMI.</li></ul>

<div class="box trap"><b>Traps:</b>
<ul><li>Ordinary annuity = payment at the <b>end</b> of each period. Annuity due = at the <b>beginning</b>, value × (1 + r).</li>
<li>Monthly EMI: use the <b>monthly</b> rate and the number of <b>months</b>.</li>
<li>11.70% compounded monthly (EAR ≈ 12.35%) is <b>costlier</b> than 12% compounded annually.</li>
<li>Never compare total nominal lease payments with a purchase price. Discount them first.</li>
<li>Rule of 72 is an approximation, and is less accurate at high rates.</li></ul></div>
''')

Q('C3', """A customer deposits ₹24,000 for 9 months at 8% p.a. simple interest. What interest does he earn?""",
  "₹1,440", ["₹1,920", "₹1,080", "₹1,520"], "SI = 24,000 × 8% × 9/12 = ₹1,440. (1,920 is the full-year figure.)")

Q('C3', """What is the future value of ₹10,000 after one year at 12% p.a. compounded quarterly?""",
  "₹11,255", ["₹11,200", "₹11,268", "₹11,236"],
  "10,000 × (1 + 0.12/4)^4 = 10,000 × 1.03^4 = 11,255.09. (11,268 is monthly compounding; 11,236 is half-yearly.)")

Q('C3', """Loan offers: Bank A 12% p.a. compounded annually; Bank B 11.70% p.a. compounded monthly. Which is cheaper and why?""",
  "Bank A, because Bank B's effective annual rate is about 12.35%",
  ["Bank B, because its quoted nominal rate is 0.30% lower than Bank A's", "Both cost exactly the same, because the difference in compounding is negligible",
   "Bank B, because monthly compounding benefits the borrower through smaller payments"],
  "EAR(B) = (1 + 0.117/12)^12 − 1 ≈ 12.35% > 12%. Compounding frequency raises the true cost, so nominal rates can't be compared directly.")

Q('C3', """Mr Raj invests ₹50,000 at the END of each year for 20 years at 8% compounded annually. The maturity value is closest to:""",
  f"₹{money(2288098)}", ["₹24,71,146", "₹10,00,000", "₹21,18,610"],
  "FV of ordinary annuity = 50,000 × [(1.08)^20 − 1]/0.08 = 50,000 × 45.762 = ₹22,88,098. (24,71,146 would be an annuity due; 10,00,000 ignores interest.)")

Q('C3', """₹10,000 is invested every year for 5 years at 8%. The future value is ₹58,666 if each payment is at the year-end. If each payment is made at the BEGINNING of the year instead, the future value is:""",
  "₹63,359", ["₹58,666", "₹54,320", "₹68,428"],
  "Annuity due = ordinary annuity × (1 + r) = 58,666 × 1.08 = ₹63,359. Each payment earns interest for one extra year.")

Q('C3', """A company can buy a production line for ₹47.50 lakh or lease it for ₹12 lakh payable at the end of each year for 5 years. Cost of capital 10%; PVAF (10%, 5) = 3.7908. The Finance Manager rejects the lease because total payments are ₹60 lakh. The correct decision is:""",
  "Lease, because the present value of lease payments (about ₹45.49 lakh) is below ₹47.50 lakh",
  ["Buy, because total lease payments of ₹60 lakh exceed the purchase price", "Indifferent, because both options cost the same once spread over 5 years",
   "Buy, because time value of money does not apply to the purchase of fixed assets"],
  "PV of lease = 12 × 3.7908 = ₹45.49 lakh < ₹47.50 lakh, so leasing is cheaper in today's money.")

Q('C3', """A ₹10 lakh loan at 9% p.a. is repayable in 60 equal monthly instalments. The EMI is closest to:""",
  "₹20,758", ["₹16,667", "₹24,167", "₹25,000"],
  "i = 0.75% per month, n = 60. EMI = 10,00,000 × 0.0075 × 1.0075^60/(1.0075^60 − 1) ≈ ₹20,758. 16,667 ignores interest; 24,167 adds flat interest.")

Q('C3', """In the first EMI of ₹20,758 on a ₹10 lakh loan at 9% p.a. (monthly reducing balance), how much goes towards principal?""",
  "₹13,258", ["₹7,500", "₹20,758", "₹16,667"],
  "Interest for month 1 = 10,00,000 × 0.75% = ₹7,500; principal = 20,758 − 7,500 = ₹13,258. The principal share rises every month as the balance falls.")

Q('C3', """The population of a city is 10 lakh and grows at 5% p.a. compounded. What is it after 3 years?""",
  "11,57,625", ["11,50,000", "11,55,000", "11,62,500"],
  "10,00,000 × 1.05^3 = 11,57,625. Simple growth would give 11,50,000.")

Q('C3', """A bank lends ₹1,00,000 for one year at 10% but deducts the interest upfront (front-end/discounted). What is the effective rate for the borrower?""",
  "11.11%", ["10.00%", "9.09%", "10.50%"],
  "Borrower gets ₹90,000 and repays ₹1,00,000: 10,000/90,000 = 11.11%. Collecting interest in advance raises the effective cost.")

Q('C3', """Using the Rule of 72, at what annual compound rate will money double in about 6 years?""",
  "About 12%", ["About 16.7%", "About 8%", "About 6%"],
  "Rate ≈ 72 ÷ 6 = 12%. Check: 1.12^6 = 1.97. Simple interest would need 16.7%.")

Q('C3', """Which statements about annuities are correct?
1. In an ordinary annuity, payments are made at the end of each period.
2. Rent paid in advance at the start of each month is an annuity due.
3. The present value of an annuity due is lower than that of an ordinary annuity with the same payments and rate.
4. The present value of a perpetuity is the periodic payment divided by the rate.""",
  "1, 2 and 4 only", ["1, 2, 3 and 4", "1 and 3 only", "2, 3 and 4 only"],
  "An annuity due receives each payment one period earlier, so its PV is HIGHER (× (1 + r)). The rest are correct.")

Q('C3', """₹8 lakh is invested for 4 years at 9% compounded annually (1.09⁴ = 1.4116). Another option pays 10% simple interest. Which is correct?""",
  "Compound option ≈ ₹11.29 lakh, higher than the simple-interest option's ₹11.20 lakh",
  ["Compound option ≈ ₹11.29 lakh, lower than the simple-interest option's ₹11.60 lakh", "Both give exactly ₹11.20 lakh after 4 years",
   "Compound option ≈ ₹11.60 lakh, higher than the simple-interest option's ₹11.29 lakh"],
  "8 × 1.4116 = 11.29 lakh; 8 + 8 × 0.10 × 4 = 11.20 lakh. Compounding at 9% beats 10% simple over 4 years.")

Q('C3', """What is the present value of ₹1,00,000 receivable after 3 years at 10% compound?""",
  "₹75,131", ["₹70,000", ["₹76,923"][0], "₹1,33,100"],
  "PV = 1,00,000/1.1^3 = 1,00,000/1.331 = ₹75,131. 70,000 deducts simple interest; 1,33,100 is the future value of 1 lakh.")

Q('C3', """A borrower compares two term loans of ₹48 lakh for 5 years. Bank A: 9.00%, EMI ₹99,640, no fee. Bank B: 8.60%, EMI ₹98,890, processing fee ₹1,20,000. Total EMI saving with Bank B over 60 months is ₹45,000. What should guide the choice?""",
  "Effective all-in cost: Bank B's upfront fee of ₹1.2 lakh exceeds its EMI saving, so Bank A is cheaper",
  ["Lowest EMI, so Bank B should be chosen because it saves ₹750 every month", "Processing fee is a one-time cost and should be ignored in comparing loans",
   "Interest rate alone, so Bank B should be chosen because 8.60% is less than 9.00%"],
  "B saves (99,640 − 98,890) × 60 = ₹45,000 in EMIs but charges ₹1,20,000 upfront (paid today, so worth even more). The effective cost of B is higher.")
