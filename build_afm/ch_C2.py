from qb import note, Q, money

note('C2', r'''
<p class="small">Syllabus: Meaning, classification, uses, limitations, calculation and interpretation of ratios, users of ratios. <b>Asked: 5–6 questions per session since May 2025</b>, the most-asked topic in Module C. May 2026 asked:</p>
<ul class="small"><li>debtors turnover with interpretation</li>
<li>inventory turnover</li>
<li>inventory from the current and quick ratios</li>
<li>quick ratio falling while the current ratio stays steady</li>
<li>debt-equity vs interest coverage</li>
<li>fixed-charge coverage</li>
<li>dividend yield</li>
<li>bonus issue and debt-equity</li>
<li>ROI</li>
<li>which ratio a term lender looks at</li></ul>

<h3>1. Formula bank</h3>
<table><tr><th>Group</th><th>Ratio</th><th>Formula</th><th>Benchmark / reading</th></tr>
<tr><td rowspan="3">Liquidity</td><td>Current ratio</td><td>Current assets ÷ Current liabilities</td><td>2 : 1 traditional. Banks: 1.33 : 1 (Tandon second method)</td></tr>
<tr><td>Quick (acid-test) ratio</td><td>(CA − Inventory − Prepaid expenses) ÷ CL</td><td>1 : 1</td></tr>
<tr><td>Absolute liquid / cash ratio</td><td>(Cash + Bank + Marketable securities) ÷ CL</td><td>0.5 : 1</td></tr>
<tr><td rowspan="5">Solvency / leverage</td><td>Debt-equity</td><td>Long-term debt ÷ Shareholders' funds (net worth)</td><td>2 : 1 is a common ceiling for term loans</td></tr>
<tr><td>TOL / TNW</td><td>Total outside liabilities ÷ Tangible net worth</td><td>Used by banks for working-capital limits</td></tr>
<tr><td>Proprietary ratio</td><td>Shareholders' funds ÷ Total assets</td><td>Higher means safer</td></tr>
<tr><td>Interest coverage</td><td>EBIT ÷ Interest</td><td>How many times interest is covered</td></tr>
<tr><td><b>DSCR</b></td><td>(PAT + Depreciation + Interest on term loan) ÷ (Interest on term loan + Principal instalment)</td><td><b>The key ratio for term lenders.</b> Average 1.5–2 is comfortable</td></tr>
<tr><td></td><td>Fixed-charge coverage</td><td>(EBIT + Lease rentals) ÷ (Interest + Lease rentals + Principal repayment)</td><td>Wider than ICR; includes all fixed commitments</td></tr>
<tr><td rowspan="6">Activity (turnover)</td><td>Inventory turnover</td><td>COGS ÷ Average inventory</td><td>Holding period = 365 ÷ ITR</td></tr>
<tr><td>Debtors turnover</td><td><b>Net credit sales</b> ÷ Average (debtors + bills receivable)</td><td>Collection period = 365 ÷ DTR</td></tr>
<tr><td>Creditors turnover</td><td>Net credit purchases ÷ Average (creditors + bills payable)</td><td>Payment period = 365 ÷ CTR</td></tr>
<tr><td>Fixed-asset turnover</td><td>Net sales ÷ Net fixed assets</td><td></td></tr>
<tr><td>Total asset turnover</td><td>Net sales ÷ Total assets</td><td></td></tr>
<tr><td>Working-capital turnover</td><td>Net sales ÷ Net working capital</td><td></td></tr>
<tr><td rowspan="5">Profitability</td><td>GP ratio</td><td>GP ÷ Net sales × 100</td><td></td></tr>
<tr><td>NP ratio</td><td>NP ÷ Net sales × 100</td><td></td></tr>
<tr><td>Operating ratio</td><td>(COGS + Operating expenses) ÷ Net sales × 100</td><td>Operating profit ratio = 100 − Operating ratio</td></tr>
<tr><td>ROI / ROCE</td><td>EBIT ÷ Capital employed × 100</td><td>Capital employed = equity + long-term debt (or total assets − current liabilities). Needs <b>both</b> the P&amp;L and the Balance Sheet</td></tr>
<tr><td>ROE</td><td>(PAT − Preference dividend) ÷ Equity shareholders' funds</td><td></td></tr>
<tr><td rowspan="5">Market</td><td>EPS</td><td>(PAT − Preference dividend) ÷ No. of equity shares</td><td></td></tr>
<tr><td>P/E ratio</td><td>Market price ÷ EPS</td><td>Earnings yield = EPS ÷ MP = 1 ÷ P/E</td></tr>
<tr><td>Dividend yield</td><td>DPS ÷ Market price</td><td>A higher DPS does <b>not</b> by itself mean a higher yield</td></tr>
<tr><td>Dividend payout</td><td>DPS ÷ EPS</td><td>Retention ratio = 1 − payout</td></tr>
<tr><td>Book value per share</td><td>Equity shareholders' funds ÷ No. of shares</td><td></td></tr></table>

<h3>2. Who uses which ratio</h3>
<ul><li><b>Short-term creditors and working-capital bankers:</b> liquidity ratios (current, quick), turnover ratios, TOL/TNW.</li>
<li><b>Long-term lenders (term-loan banker, debenture holders):</b> <b>DSCR</b>, debt-equity, interest coverage, fixed-charge coverage.</li>
<li><b>Equity investors:</b> EPS, P/E, ROE, dividend yield and payout.</li>
<li><b>Management:</b> all ratios, especially operating and turnover ratios for efficiency.</li></ul>

<h3>3. Reverse-working (examiner's favourite)</h3>
<ul><li><b>CA ₹18 crore, CR 2, QR 1.25.</b> CL = 18 ÷ 2 = 9. Quick assets = 1.25 × 9 = 11.25. <b>Inventory = 18 − 11.25 = ₹6.75 crore.</b></li>
<li><b>Working capital ₹6 lakh, CR 2.5.</b> CA − CL = 6 and CA = 2.5 CL, so 1.5 CL = 6 → CL = 4, <b>CA = 10</b>.</li>
<li><b>Opening debtors ₹2.4 lakh, closing ₹3.6 lakh, cash sales ₹5 lakh, total sales ₹20 lakh.</b> Credit sales = 15 lakh; average debtors = 3 lakh; <b>DTR = 5; collection period = 73 days</b>.</li>
<li><b>Sales ₹30 lakh, GP 25% on sales.</b> COGS = 22.5 lakh. With opening stock 2.5 and closing 3.5 (average 3), <b>ITR = 7.5 times</b> and the holding period is about 48.7 days.</li>
<li><b>DSCR:</b> PAT 30, depreciation 10, interest on term loan 8, instalment 20 → (30 + 10 + 8) ÷ (8 + 20) = <b>1.71</b>.</li></ul>

<h3>4. Effect of transactions</h3>
<table><tr><th>Transaction</th><th>Current ratio (if CR &gt; 1)</th><th>Other effect</th></tr>
<tr><td>Pay a creditor in cash</td><td><b>Rises</b> (e.g. 4/2 → 3/1). If CR &lt; 1 it falls.</td><td>Quick ratio also changes</td></tr>
<tr><td>Buy stock on credit</td><td><b>Falls</b> (equal increase in CA and CL)</td><td>Quick ratio falls</td></tr>
<tr><td>Issue shares for cash / raise long-term loan</td><td>Rises</td><td>D/E falls (shares) or rises (loan)</td></tr>
<tr><td>Buy a fixed asset for cash</td><td>Falls</td><td>—</td></tr>
<tr><td>Bonus shares</td><td>No change</td><td><b>D/E unchanged</b>: reserves become capital, net worth is the same</td></tr>
<tr><td>Convert a short-term loan into a long-term loan</td><td>Rises</td><td>D/E rises</td></tr></table>
<p><b>In bank credit appraisal</b>, redeemable preference shares with a maturity of up to 12 years are treated as debt (term liability) when computing debt-equity. Those redeemable after 12 years are treated as quasi-equity.</p>

<h3>5. Interpretation: one ratio never decides</h3>
<ul><li>A stable current ratio can hide falling liquidity if inventory is piling up. Watch the <b>quick ratio and the inventory holding period</b> together.</li>
<li>A higher debtors turnover may come from tighter credit that cuts sales, a seasonal effect or a change in sales mix. Read it with credit policy.</li>
<li>Low debt-equity alone doesn't make a borrower safe. A weak interest coverage or DSCR means poor repayment capacity.</li>
<li>A higher closing inventory raises the current ratio but may signal slow-moving stock.</li>
<li><b>Conditions for valid comparison:</b> same accounting policies, same period length, comparable firms of similar size and industry. Adjust for inflation where needed.</li>
<li><b>Limitations:</b> historical data, window dressing, different accounting methods, ignores qualitative factors, no universal standard.</li></ul>

<div class="box trap"><b>Traps:</b>
<ul><li>Debtors turnover uses <b>credit</b> sales only, and debtors include bills receivable.</li>
<li>Inventory turnover uses <b>COGS</b>, not sales, unless told otherwise.</li>
<li>Quick ratio removes <b>inventory and prepaid expenses</b>.</li>
<li>A bonus issue does not change debt-equity or net worth, but EPS falls (more shares).</li>
<li>DSCR uses <b>PAT + depreciation + interest</b> in the numerator, and interest is added again in the denominator.</li>
<li>A lower debt-equity ratio is not "always" safer, and a high current ratio is not always good (idle funds).</li></ul></div>
''')

Q('C2', """Nova Engineering has current assets of ₹18 crore, a current ratio of 2 : 1 and a quick ratio of 1.25 : 1. There are no prepaid expenses. What is its inventory?""",
  "₹6.75 crore", ["₹4.50 crore", "₹9.00 crore", "₹7.20 crore"],
  "CL = 18 ÷ 2 = ₹9 crore. Quick assets = 1.25 × 9 = ₹11.25 crore. Inventory = CA − quick assets = 18 − 11.25 = ₹6.75 crore.")

Q('C2', """A firm's working capital is ₹6 lakh and its current ratio is 2.5 : 1. What are its current assets?""",
  "₹10 lakh", ["₹15 lakh", "₹8.4 lakh", "₹4 lakh"],
  "CA − CL = 6 and CA = 2.5 CL → 1.5 CL = 6 → CL = 4 and CA = 10. (4 lakh is CL, the trap.)")

dtr = 1500000 / 300000
Q('C2', """Opening debtors ₹2,40,000; closing debtors ₹3,60,000; cash sales ₹5,00,000; total sales ₹20,00,000; year of 365 days. What is the average collection period?""",
  "73 days", ["60.8 days", "54.75 days", "87.6 days"],
  "Credit sales = 20,00,000 − 5,00,000 = 15,00,000. Average debtors = (2,40,000 + 3,60,000)/2 = 3,00,000. DTR = 5 times. Collection period = 365/5 = 73 days. Using total sales gives 54.75 days (wrong).")

Q('C2', """A firm has credit sales of ₹10,00,000 and average accounts receivable of ₹1,60,000. Taking 365 days, the average collection period is closest to:""",
  "58 days", ["63 days", "6.25 days", "44 days"],
  "DTR = 10,00,000/1,60,000 = 6.25 times. Collection period = 365/6.25 = 58.4 days.")

Q('C2', """Sales are ₹30 lakh with a gross profit of 25% on sales. Opening stock is ₹2.5 lakh and closing stock ₹3.5 lakh. What is the inventory turnover ratio?""",
  "7.5 times", ["10 times", "8.57 times", "6.43 times"],
  "COGS = 30 − 25% of 30 = 22.5 lakh. Average stock = (2.5 + 3.5)/2 = 3 lakh. ITR = 22.5/3 = 7.5 times. Using sales (30/3 = 10) is the common mistake.")

Q('C2', """A borrower's PAT is ₹30 lakh, depreciation ₹10 lakh, interest on term loan ₹8 lakh and the term-loan instalment due ₹20 lakh. What is the DSCR?""",
  "1.71", ["2.00", "1.43", "1.50"],
  "DSCR = (PAT + Depreciation + Interest on TL) ÷ (Interest on TL + Instalment) = (30 + 10 + 8) ÷ (8 + 20) = 48/28 = 1.71. Forgetting to add back interest gives 40/28 = 1.43.")

Q('C2', """For a term-lending banker, which ratio is the most important for judging repayment capacity?""",
  "Debt Service Coverage Ratio", ["Current ratio", "Inventory turnover ratio", "Gross profit ratio"],
  "Term loans are repaid from cash accruals over years. DSCR shows how many times instalment plus interest is covered by accruals. Current ratio is a working-capital banker's tool.")

Q('C2', """Company X: long-term debt ₹180 crore, shareholders' funds ₹90 crore, interest coverage 6.5 times. Company Y: debt ₹120 crore, funds ₹160 crore, interest coverage 3.2 times. The credit officer prefers Y only because its debt-equity is lower. Which view is sound?""",
  "Debt-equity must be read with repayment capacity: X is more leveraged (2 : 1) but covers interest far better than Y (0.75 : 1)",
  ["Y is always safer, because a lower debt-equity ratio by itself guarantees lower credit risk for the lender",
   "X should be rejected outright, because any debt-equity above 1 : 1 is unacceptable",
   "The two ratios measure the same aspect of strength, so X's higher interest coverage can be safely ignored"],
  "Debt-equity shows structure (X 2:1, Y 0.75:1); interest coverage and DSCR show ability to service debt. A lending decision weighs both along with cash flows and profitability.")

Q('C2', """A company issues bonus shares in the ratio 2 : 1 by capitalising general reserve. Its debt-equity ratio will:""",
  "Remain unchanged, because total shareholders' funds do not change",
  ["Increase, because the number of equity shares increases", "Decrease, because share capital increases threefold",
   "Become zero, because reserves are fully capitalised"],
  "Bonus issue only transfers reserves to share capital; net worth (equity) stays the same, so D/E is unchanged. EPS and book value per share fall.")

Q('C2', """Current assets ₹4 lakh and current liabilities ₹2 lakh. The firm pays ₹1 lakh to creditors in cash. The new current ratio is:""",
  "3 : 1", ["2 : 1", "1.5 : 1", "4 : 1"],
  "CA = 3, CL = 1 → 3 : 1. When CR is above 1, paying off a current liability raises the ratio. (If CR were below 1, it would fall.)")

Q('C2', """FY 2025: current ratio 2.10, quick ratio 1.28, inventory holding 52 days. FY 2026: current ratio 2.08, quick ratio 0.82, inventory holding 96 days. The borrower says liquidity hasn't changed. Your conclusion:""",
  "Liquidity has weakened: funds are increasingly locked in slow-moving stock, which the stable current ratio hides",
  ["Liquidity is satisfactory because the current ratio is still above the 2 : 1 benchmark",
   "Quick ratio is irrelevant whenever the current ratio exceeds 2 : 1, so no further analysis is needed",
   "Inventory has no impact on liquidity because it is part of current assets anyway"],
  "Same current ratio but a sharply lower quick ratio and nearly doubled holding period show that inventory is rising as a share of current assets; liquid assets have fallen.")

Q('C2', """EBIT ₹24 crore, interest ₹4 crore, lease rentals ₹2 crore, principal repayment ₹5 crore. Using the simplified formula (EBIT + Lease rentals) ÷ (Interest + Lease rentals + Principal), the fixed-charge coverage ratio is about:""",
  "2.36 times", ["6.00 times", "4.33 times", "2.18 times"],
  "(24 + 2) ÷ (4 + 2 + 5) = 26/11 = 2.36. Interest coverage alone (24/4 = 6) overstates comfort because it ignores lease and principal commitments.")

Q('C2', """Company X: market price ₹480, DPS ₹18. Company Y: market price ₹360, DPS ₹12. Which statements are correct?
1. X's dividend yield is 3.75%.
2. Y's dividend yield is 3.33%.
3. Dividend yield relates dividend to the current market price.
4. A higher DPS always means a higher dividend yield.""",
  "1, 2 and 3 only", ["1, 2, 3 and 4", "1 and 4 only", "2 and 3 only"],
  "18/480 = 3.75%; 12/360 = 3.33%. Yield depends on both DPS and price, so a higher DPS doesn't always mean a higher yield.")

Q('C2', """PAT ₹12 lakh; preference dividend ₹2 lakh; 5 lakh equity shares; market price ₹30. What are EPS and P/E?""",
  "EPS ₹2; P/E 15 times", ["EPS ₹2.40; P/E 12.5 times", "EPS ₹2; P/E 6.67 times", "EPS ₹2.40; P/E 15 times"],
  "EPS = (12 − 2)/5 = ₹2. P/E = 30/2 = 15. Not deducting preference dividend gives 2.40.")

Q('C2', """Which financial statements are needed to compute Return on Investment (ROCE)?""",
  "Both the Profit and Loss Account (for EBIT) and the Balance Sheet (for capital employed)",
  ["Only the Profit and Loss Account, since return is a profit figure", "Only the Balance Sheet, since investment is a balance sheet figure",
   "Only the Cash Flow Statement, since return means cash generated"],
  "ROI = EBIT ÷ capital employed: the numerator comes from the P&L and the denominator from the Balance Sheet.")

Q('C2', """Which is an essential condition for a meaningful comparison of ratios between two firms or periods?""",
  "The firms or periods must follow comparable accounting policies and similar bases",
  ["Both firms must have exactly the same sales turnover every year", "Ratios must be calculated by the same analyst for both firms",
   "Only firms listed on the same stock exchange can be compared"],
  "Different depreciation or inventory methods, period lengths or classifications distort ratios. Comparable policies and bases matter, not identical size.")

Q('C2', """The Credit Manager boasts that debtors turnover improved from 5 to 8 times. The CRO is not convinced credit management improved. Why?""",
  "The ratio must be read with credit policy, customer mix, seasonality and sales trends; for example, tighter credit may have cut sales",
  ["A higher debtors turnover always shows weaker collection efficiency, so the CRO is right to worry", "Debtors turnover has no link with working-capital management, so the change is irrelevant here",
   "Ratio analysis is meaningful only for banking companies and not for manufacturing borrowers like this one"],
  "A ratio in isolation can mislead; a jump may come from lower credit sales, factoring of receivables, or a seasonal year-end, not better collection.")

Q('C2', """In bank credit appraisal, redeemable preference shares with a residual maturity of 8 years are treated, while computing debt-equity, as:""",
  "Debt (term liability)", ["Equity, since they are share capital", "Current liabilities", "Ignored altogether"],
  "Banks treat redeemable preference shares maturing within 12 years as term debt; those redeemable after 12 years are treated as quasi-equity.")

Q('C2', """Net sales ₹50 lakh; COGS ₹35 lakh; operating expenses ₹7.5 lakh. What are the operating ratio and the operating profit ratio?""",
  "85% and 15%", ["70% and 30%", "85% and 30%", "15% and 85%"],
  "Operating ratio = (35 + 7.5)/50 = 85%. Operating profit ratio = 100 − 85 = 15%.")

Q('C2', """Which pair of transactions REDUCES the current ratio when it is currently 1.8 : 1?
1. Purchase of stock on credit.
2. Payment of a current liability in cash.
3. Purchase of machinery for cash.
4. Issue of equity shares for cash.""",
  "1 and 3", ["1 and 2", "2 and 4", "3 and 4"],
  "With CR above 1, adding equal amounts to CA and CL (1) lowers it; paying a current liability (2) raises it; spending cash on a fixed asset (3) lowers CA; issuing shares (4) raises CA.")
