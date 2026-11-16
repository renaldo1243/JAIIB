from qb import note, Q

note('B3', r'''
<p class="small">Syllabus: Company Accounts II: form of the balance sheet (Schedule III), impact of Ind AS. This chapter also gathers the corporate items the May 2026 paper tested heavily:</p>
<ul class="small"><li>bonus and rights issues</li>
<li>ESOP</li>
<li>EPS (basic and diluted)</li>
<li>deferred tax (asked 3 times)</li>
<li>reserves available for dividend</li>
<li>employee benefits expense</li>
<li>what forms part of the "financial statements"</li></ul>
<p class="small"><b>Asked: 3–4 questions per session on the form of the balance sheet and P&amp;L, plus 6–8 in May 2026 on these items.</b></p>

<h3>1. Schedule III (Companies Act 2013)</h3>
<ul><li>Division I = companies on AS. Division II = Ind AS companies. Division III = NBFCs on Ind AS.</li>
<li>Banks use the Third Schedule of the BR Act; insurers use their own.</li>
<li><b>Purpose:</b> a standard format for comparability, transparency and decision-usefulness. It does <b>not</b> replace accounting standards or prescribe accounting policies.</li></ul>
<table><tr><th>Equity and liabilities</th><th>Assets</th></tr>
<tr><td><b>Shareholders' funds:</b> share capital; reserves &amp; surplus; money received against share warrants<br>
Share application money pending allotment<br>
<b>Non-current liabilities:</b> long-term borrowings; deferred tax liabilities (net); other long-term liabilities; long-term provisions<br>
<b>Current liabilities:</b> short-term borrowings (<b>including current maturities of long-term debt</b>); trade payables (MSME separately, with ageing); other current liabilities; short-term provisions</td>
<td><b>Non-current assets:</b> PPE and intangible assets; capital WIP; intangibles under development; non-current investments; deferred tax assets (net); long-term loans and advances; other non-current assets<br>
<b>Current assets:</b> current investments; inventories; trade receivables (with ageing); cash and cash equivalents; short-term loans and advances; other current assets</td></tr></table>
<ul><li><b>Current vs non-current:</b>
<ul><li>An asset is current if it will be realised within <b>12 months</b> or the operating cycle, or is held for trading.</li>
<li>A liability is current if it is due within 12 months, or the company has <b>no unconditional right to defer</b> settlement for at least 12 months.</li>
<li>The operating cycle is assumed to be 12 months if it can't be identified.</li>
<li>A security deposit recoverable after 4 years → <b>non-current</b>.</li></ul></li>
<li><b>Statement of P&amp;L heads:</b>
<ul><li>revenue from operations; other income</li>
<li>cost of materials consumed; purchases of stock-in-trade; changes in inventories</li>
<li><b>employee benefits expense</b> (salaries and wages, contribution to provident and other funds, share-based payments/ESOP, staff welfare)</li>
<li>finance costs</li>
<li>depreciation and amortisation</li>
<li>other expenses</li></ul></li>
<li><b>2021 amendments added:</b> promoter shareholding, ageing of payables, receivables and CWIP, <b>key ratios</b> (current ratio, D/E, DSCR, ROE and others), crypto holdings, benami property, wilful-defaulter status, transactions with struck-off companies.</li>
<li><b>"Financial statements" (Sec 2(40))</b> = balance sheet, P&amp;L, <b>cash flow statement</b> (OPCs, small and dormant companies are exempt), statement of changes in equity (if applicable) and notes.
<br>The <b>Directors' Report and Auditor's Report are NOT</b> part of the financial statements.</li></ul>

<h3>2. Reserves and dividend</h3>
<ul><li><b>Dividend</b> is paid out of current or past profits <b>after depreciation</b> (Sec 123), or from <b>free reserves</b>.</li>
<li><b>Free reserves:</b> general reserve, surplus in P&amp;L.</li>
<li><b>Not usable for dividend:</b> capital reserve, <b>revaluation reserve</b>, securities premium, capital redemption reserve (CRR).</li>
<li><b>Bonus</b> (Sec 63) can be issued from <b>free reserves, securities premium and CRR</b>, but <b>not from revaluation reserve</b>.
<ul><li>Must be authorised by the Articles.</li>
<li>No default in deposits, debt or statutory dues.</li>
<li>Partly paid shares must be made fully paid first.</li>
<li>Cannot be issued <b>in lieu of dividend</b>.</li></ul></li></ul>

<h3>3. Bonus vs rights</h3>
<table><tr><th></th><th>Bonus issue</th><th>Rights issue</th></tr>
<tr><td>Cash to company</td><td>None. It capitalises reserves.</td><td>Fresh cash at the issue price</td></tr>
<tr><td>Shareholders' funds</td><td>Unchanged; paid-up capital rises</td><td>Increase</td></tr>
<tr><td>Ownership %</td><td>Unchanged</td><td>Unchanged if subscribed. Falls if the holder neither subscribes nor <b>renounces</b> (sells) the right.</td></tr>
<tr><td>EPS, D/E</td><td>EPS falls (more shares); D/E unchanged</td><td>EPS adjusted for the bonus element</td></tr>
<tr><td>Market</td><td>Price adjusts down; liquidity of the share improves</td><td>Theoretical ex-rights price (TERP)</td></tr></table>
<p><b>TERP</b> = (N × Market price + n × Issue price) ÷ (N + n).</p>
<ul><li>1-for-4 at ₹180 with market price ₹260 → TERP = (4 × 260 + 180) ÷ 5 = <b>₹244</b>.</li>
<li>Value of the right = 244 − 180 = ₹64 per new share, or <b>₹16 per existing share</b>.</li></ul>

<h3>4. EPS (AS 20 / Ind AS 33)</h3>
<ul><li><b>Basic EPS</b> = (PAT − preference dividend) ÷ weighted average equity shares.</li>
<li><b>Bonus issue:</b> treated as if outstanding from the start of the earliest period shown (restate previous EPS).</li>
<li><b>Diluted EPS</b> adds <b>potential equity shares</b> (convertibles, options):
<ul><li>Earnings + post-tax interest saved.</li>
<li>Shares + potential shares, for the period they were outstanding as potential shares.</li>
<li>Both the numerator and the denominator change.</li></ul></li>
<li><b>Example:</b> PAT ₹48 crore; 2 crore shares all year; ₹20 crore debentures (post-tax interest ₹1.2 crore a year) converted into 20 lakh shares on 1 October.
<ul><li>Basic: shares = 2 + 0.2 × 6/12 = 2.1 crore → <b>₹22.86</b>.</li>
<li>Diluted: earnings 48 + 0.6 (half-year interest) = 48.6; shares 2.2 crore → <b>₹22.09</b>.</li>
<li>So "Basic = Diluted because conversion happened during the year" is wrong.</li></ul></li></ul>

<h3>5. Deferred tax (AS 22; Ind AS 12)</h3>
<ul><li><b>Current tax</b> = tax on <b>taxable</b> income.</li>
<li><b>Deferred tax</b> arises from <b>timing differences</b>: income and expenses that enter accounting profit and taxable profit in different periods and <b>reverse later</b>.</li>
<li><b>DTL</b> (taxable now &lt; book profit now): tax depreciation (WDV 40%) higher than book depreciation (SLM).</li>
<li><b>DTA</b> (taxable now &gt; book now):
<ul><li>expenses disallowed now but allowed on payment (Sec 43B, e.g. bonus or leave encashment paid later)</li>
<li>provision for doubtful debts</li>
<li>carried-forward losses</li></ul></li>
<li><b>Permanent differences</b> never reverse, so there is <b>no</b> deferred tax:
<ul><li>penalties disallowed</li>
<li>exempt income</li>
<li>CSR spending disallowed</li></ul></li>
<li><b>Example:</b> book profit 96, taxable profit 82 (due to depreciation), tax 30%.
<ul><li>Current tax = 24.6</li>
<li>DTL = 14 × 30% = <b>4.2</b></li>
<li>Total tax expense = 28.8</li></ul></li>
<li><b>DTA recognition:</b> needs <b>reasonable certainty</b> of future taxable income. For unabsorbed depreciation and carried-forward losses, <b>virtual certainty</b> backed by convincing evidence.</li>
<li>Measured at enacted or substantively enacted rates; <b>not discounted</b>.</li>
<li>Ind AS 12 uses a balance-sheet approach (temporary differences).</li></ul>

<h3>6. ESOP accounting</h3>
<ul><li>The <b>fair value</b> of options at grant date (under Ind AS 102; under the Guidance Note, fair value or intrinsic value) is an <b>employee compensation expense spread over the vesting period</b>.</li>
<li>The credit goes to equity: Employee Stock Options Outstanding.</li>
<li>No entry waits until exercise. When employees exercise, the share capital (and premium) is recorded.</li></ul>

<div class="box trap"><b>Traps:</b>
<ul><li>Bonus: no cash, ownership % unchanged, EPS down, D/E unchanged.</li>
<li>Revaluation reserve can't fund bonus or dividend.</li>
<li>Diluted EPS adjusts <b>both</b> earnings and shares.</li>
<li>Deferred tax only on <b>timing</b> differences.</li>
<li>Current maturities of long-term debt → <b>short-term borrowings</b> (current), not non-current.</li>
<li>The Directors' Report is not part of the financial statements.</li></ul></div>
''')

Q('B3', """Sigma Ltd. (share capital ₹25 crore, securities premium ₹18 crore, general reserve ₹40 crore, cash ₹3 crore) plans fully paid bonus shares instead of a cash dividend. Which statements are correct?
1. Proportionate ownership remains unchanged.
2. Liquidity improves because bonus shares bring in cash.
3. Paid-up capital rises without any increase in total shareholders' funds.
4. EPS may fall immediately if profits remain the same.""",
  "1, 3 and 4 only", ["2 and 3 only", "1 and 2 only", "1, 2, 3 and 4"],
  "Bonus capitalises reserves: no cash comes in, total equity is unchanged, every holder gets shares in proportion, and the larger share count dilutes EPS.")

Q('B3', """A listed company makes a rights issue of 1 share for every 4 held at ₹180; the market price before the issue is ₹260. What is the theoretical ex-rights price and the value of one right per existing share?""",
  "TERP ₹244; value of right ₹16 per existing share", ["TERP ₹220; value of right ₹40 per existing share", "TERP ₹244; value of right ₹64 per existing share",
   "TERP ₹260; rights have no value because the price is unchanged"],
  "TERP = (4 × 260 + 180)/5 = 1,220/5 = 244. Value per new share = 244 − 180 = 64; as 4 existing shares give one right, value per existing share = 64/4 = ₹16.")

Q('B3', """Mr Arjun holds 8,000 shares; the company makes a 1-for-4 rights issue at ₹180 when the market price is ₹260. He neither subscribes nor renounces his rights. What is the most likely consequence?""",
  "His ownership percentage falls and he loses the value of the rights he let lapse",
  ["His existing shares become invalid until he exercises the rights", "He loses all voting rights on his existing shares",
   "His wealth necessarily rises because prices always go up after a rights issue"],
  "Others subscribe, so his percentage falls; and the market price falls towards TERP (₹244) while he gets nothing for his entitlement. Renouncing (selling) the rights would have preserved value.")

Q('B3', """ABC Technologies: PAT ₹48 crore; 2 crore equity shares all year; ₹20 crore convertible debentures (post-tax interest ₹1.2 crore a year) converted into 20 lakh shares on 1 October. What are basic and diluted EPS?""",
  "Basic ₹22.86; Diluted ₹22.09", ["Basic ₹24.00; Diluted ₹21.82", "Basic ₹22.86; Diluted ₹22.86", "Basic ₹21.82; Diluted ₹22.09"],
  "Weighted shares = 2 + 0.2 × 6/12 = 2.1 crore; basic = 48/2.1 = 22.86. Diluted treats the debentures as converted from the start: earnings 48 + 0.6 (half-year interest saved) = 48.6; shares 2.2 crore → 22.09.")

Q('B3', """Vardhman Chemicals buys machinery for ₹1.20 crore; books use SLM over 10 years and tax uses WDV at 40%; tax rate 30%. What deferred tax arises at the end of year 1?""",
  "Deferred tax liability of ₹10.8 lakh", ["Deferred tax asset of ₹10.8 lakh", "Deferred tax liability of ₹36 lakh", "No deferred tax, as it is a permanent difference"],
  "Book depreciation 12 lakh; tax depreciation 48 lakh; timing difference 36 lakh makes taxable profit lower now → DTL = 36 × 30% = ₹10.8 lakh, reversing in later years.")

Q('B3', """Orion Industries: accounting profit before tax ₹96 crore; taxable profit ₹82 crore, the difference being entirely due to higher tax depreciation; tax rate 30%. What is the total tax expense in the P&L?""",
  "₹28.8 crore (current tax ₹24.6 crore + deferred tax ₹4.2 crore)", ["₹24.6 crore, being current tax only", "₹33.0 crore (current ₹28.8 + deferred ₹4.2)",
   "₹20.4 crore (current ₹24.6 − deferred ₹4.2)"],
  "Current tax = 82 × 30% = 24.6. Timing difference 14 → DTL 4.2. Total = 28.8 = 96 × 30%, matching tax to book profit.")

Q('B3', """Which of the following gives rise to a deferred tax ASSET under AS 22?""",
  "Bonus provided in the books but allowed for tax only when paid next year",
  ["Tax depreciation exceeding book depreciation in the early years", "A penalty paid for violating a law, which is never allowed for tax",
   "Dividend income that is exempt from tax"],
  "Disallowed now, allowed later → taxable profit higher now → DTA. Higher tax depreciation creates a DTL. Penalties and exempt income are permanent differences: no deferred tax.")

Q('B3', """Which statements about deferred tax are correct?
1. Current tax is based on taxable profit.
2. Deferred tax arises because depreciation differences are timing differences that reverse.
3. Deferred tax is recognised on permanent differences.
4. A DTA on carried-forward business losses needs virtual certainty supported by convincing evidence.""",
  "1, 2 and 4 only", ["1, 2 and 3 only", "2, 3 and 4 only", "1, 2, 3 and 4"],
  "Permanent differences never reverse, so no deferred tax (3 wrong). Unabsorbed depreciation and carried-forward losses need virtual certainty (AS 22).")

Q('B3', """TechNova grants 2,50,000 options vesting after 3 years; exercise price ₹220, market price at grant ₹310. HR says no entry is needed until exercise. Which is correct?""",
  "Option value is expensed over the 3-year vesting period, with a credit to equity",
  ["No entry is needed until the options are exercised and cash is received", "The ₹90 difference is recorded immediately as goodwill",
   "ESOP expense is recognised only if the company declares a dividend"],
  "Share-based payments are employee cost for services received over the vesting period; the credit goes to 'Employee Stock Options Outstanding' within equity.")

Q('B3', """Under Section 63 of the Companies Act, 2013, fully paid bonus shares may be issued out of:""",
  "Free reserves, securities premium account and capital redemption reserve", ["Revaluation reserve, free reserves and securities premium",
   "Capital reserve arising on revaluation of fixed assets only", "Profits of the current year that have not yet been audited"],
  "Bonus shares cannot be issued out of reserves created by revaluation of assets. Free reserves, securities premium and CRR are permitted sources.")

Q('B3', """Which reserve can a company use to declare dividend?""",
  "General Reserve (a free reserve)", ["Revaluation Reserve", "Capital Redemption Reserve", "Securities Premium Account"],
  "Dividend can come from current/past profits after depreciation or free reserves. Revaluation reserve, CRR and securities premium are not free reserves.")

Q('B3', """While preparing Nova Industries' Schedule III balance sheet, which classification is correct?""",
  "Current maturities of long-term debt are shown under short-term borrowings in current liabilities",
  ["A security deposit recoverable after four years is shown under current assets", "Short-term and long-term borrowings are clubbed under non-current liabilities",
   "Trade receivables are shown without any ageing information"],
  "Since the 2021 amendment, current maturities of long-term borrowings appear under short-term borrowings. Deposits recoverable after 12 months are non-current; receivables and payables need ageing.")

Q('B3', """As per Section 2(40) of the Companies Act, which document is NOT part of a company's 'financial statements'?""",
  "Directors' Report", ["Cash Flow Statement", "Statement of Profit and Loss", "Notes to accounts"],
  "Financial statements = balance sheet, P&L, cash flow statement, statement of changes in equity and explanatory notes. The Directors' Report and Auditor's Report accompany them but are not part of them.")

Q('B3', """Which items are included under 'Employee Benefits Expense' in the Statement of Profit and Loss?
1. Wages and salaries.
2. Contribution to provident and other funds.
3. Share-based payment (ESOP) expense.
4. Staff welfare expenses.""",
  "1, 2, 3 and 4", ["1 and 2 only", "1, 2 and 4 only", "1 and 4 only"],
  "Schedule III lists all four under employee benefits expense.")

Q('B3', """If a company converts part of its equity into a loan from shareholders, the balance sheet shows:""",
  "A decrease in shareholders' funds and an increase in borrowings, with total assets unchanged",
  ["An increase in both assets and shareholders' funds", "A decrease in cash and in shareholders' funds",
   "No change in any component, since it is only a reclassification within equity"],
  "Equity moves to debt; no cash moves, so total assets stay the same.")
