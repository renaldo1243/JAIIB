from qb import note, Q

note('B5', r'''
<p class="small">Syllabus: Final accounts of banking companies: requirements as to accounts and audit, features, principal books, preparation and presentation, specific items, P&amp;L and balance sheet items, disclosures (notes to accounts, Basel III), Ind AS for banks. <b>Asked: about 1 question each on features and disclosures per session, plus bank questions hidden elsewhere.</b> May 2026 asked:</p>
<ul class="small"><li>staff advances</li>
<li>bills purchased and discounted (twice)</li>
<li>acceptances and endorsements</li>
<li>interest earned schedule</li>
<li>NPA provisioning</li>
<li>Schedule 18</li>
<li>items in Schedule 16</li>
<li>transfer to reserve fund</li></ul>

<h3>1. Legal framework</h3>
<ul><li><b>Sec 29, BR Act:</b> every bank prepares its balance sheet and P&amp;L as on 31 March in the forms of the <b>Third Schedule</b>.
<ul><li>Form A = balance sheet</li>
<li>Form B = P&amp;L</li></ul></li>
<li><b>Sec 30:</b> audit by qualified auditors, with RBI approval for appointment.</li>
<li><b>Sec 31:</b> accounts, with the auditor's report, are published and filed with RBI within 3 months of the year-end (extendable by 3 months).</li>
<li><b>Sec 17:</b> transfer at least <b>20%</b> of profit to the <b>Statutory Reserve</b> before any dividend. RBI requires <b>25%</b> for scheduled commercial banks.</li>
<li><b>Sec 15:</b> no dividend until all capitalised expenses are written off.</li>
<li>Banks follow notified AS and RBI's instructions. <b>Ind AS for banks is deferred.</b></li></ul>

<h3>2. Schedules (as in the IIBF book)</h3>
<table><tr><th>Balance sheet</th><th>Schedule</th><th>P&amp;L</th><th>Schedule</th></tr>
<tr><td>Capital</td><td>1</td><td><b>Interest earned</b>: interest/discount on advances and bills; income on investments; interest on balances with RBI and inter-bank funds; others</td><td>13</td></tr>
<tr><td>Reserves &amp; surplus: statutory reserve, capital reserve, share premium, revenue reserves, P&amp;L balance</td><td>2</td><td><b>Other income</b>: commission, exchange and brokerage; profit on sale or revaluation of investments; profit on sale of assets; dividends from subsidiaries</td><td>14</td></tr>
<tr><td>Deposits: demand (from banks and others), savings, term</td><td>3</td><td>Interest expended: on deposits, on RBI/inter-bank borrowings, others</td><td>15</td></tr>
<tr><td>Borrowings: from RBI, other banks, institutions; outside India</td><td>4</td><td><b>Operating expenses</b>: payments to employees; <b>rent, taxes and lighting</b>; <b>printing and stationery</b>; advertisement; depreciation; directors' fees; auditors' fees; law charges; postage; repairs; insurance; other</td><td>16</td></tr>
<tr><td>Other liabilities &amp; provisions: bills payable, inter-office adjustments (net), interest accrued, others</td><td>5</td><td>Provisions and contingencies (NPA provision, investment depreciation, tax)</td><td>shown in P&amp;L</td></tr>
<tr><td>Cash &amp; balances with RBI</td><td>6</td><td><b>Significant accounting policies</b></td><td>17</td></tr>
<tr><td>Balances with banks &amp; money at call and short notice</td><td>7</td><td><b>Notes to accounts</b></td><td>18</td></tr>
<tr><td>Investments: in India (G-secs, other approved, shares, debentures, subsidiaries, others) / outside India</td><td>8</td><td></td><td></td></tr>
<tr><td><b>Advances</b>: (A) <b>bills purchased and discounted</b>; cash credits, overdrafts and demand loans; term loans. (B) secured by tangible assets / covered by bank or government guarantees / unsecured. (C) in India (priority, public sector, banks, others) / outside India</td><td>9</td><td></td><td></td></tr>
<tr><td>Fixed assets: premises, other fixed assets</td><td>10</td><td></td><td></td></tr>
<tr><td>Other assets: inter-office adjustments (net), interest accrued, tax paid in advance, stationery and stamps, <b>non-banking assets acquired in satisfaction of claims</b>, non-interest-bearing staff advances, others</td><td>11</td><td></td><td></td></tr>
<tr><td><b>Contingent liabilities</b>:
<ul><li>claims not acknowledged as debts</li>
<li>liability on partly paid investments</li>
<li>outstanding forward exchange contracts</li>
<li>guarantees given</li>
<li><b>acceptances, endorsements and other obligations</b> (LCs, bills accepted on behalf of customers)</li>
<li>others</li></ul></td><td>12</td><td></td><td></td></tr></table>
<p><b>Bills for collection</b> are shown <b>below the balance sheet</b>, not as a contingent liability (the bank is only an agent).</p>
<p class="small">RBI's 2025 directions on financial statements (for some bank categories) are revising these formats, e.g. separate schedules for PPE and intangible assets. For the exam, learn the IIBF numbering above and focus on <b>which head</b> an item goes to.</p>

<h3>3. Classification rules examiners test</h3>
<ul><li><b>Staff loans:</b> interest-bearing ones (housing, vehicle) → <b>Advances (Sch 9)</b>. Non-interest-bearing ones (festival advance) → <b>Other Assets (Sch 11)</b>.</li>
<li><b>Bills purchased and discounted</b> → <b>Advances</b>, not investments.</li>
<li><b>Refinance</b> from RBI, NABARD or SIDBI → <b>Borrowings</b>. Advances are shown gross.</li>
<li><b>Balances in current accounts with other banks</b> → Sch 7. <b>Cash reserve with RBI</b> → Sch 6.</li>
<li><b>Interest on NPAs is not taken to income</b> until realised. Unrealised interest already credited when the account turns NPA is <b>reversed</b>.</li>
<li><b>Investments</b> classified HTM / AFS / FVTPL (under the 2023 norms, from 1 April 2024).</li></ul>

<h3>4. NPA provisioning (IRAC) in brief</h3>
<table><tr><th>Category</th><th>Provision</th></tr>
<tr><td>Standard</td><td>0.40% generally (agriculture and SME 0.25%; CRE 1%)</td></tr>
<tr><td>Sub-standard (NPA ≤ 12 months)</td><td>15% (unsecured exposure 25%)</td></tr>
<tr><td>Doubtful D1 (up to 1 year in doubtful)</td><td>Secured portion 25% + <b>unsecured portion 100%</b></td></tr>
<tr><td>D2 (1–3 years)</td><td>Secured 40% + unsecured 100%</td></tr>
<tr><td>D3 (over 3 years)</td><td>100%</td></tr>
<tr><td>Loss</td><td>100%</td></tr></table>
<p><b>Example:</b> ₹12 crore loan, doubtful for 2 years (D2), realisable security ₹7 crore.
<br>Provision = 40% × 7 + 100% × 5 = <b>₹7.8 crore</b>.</p>

<h3>5. Disclosures (Schedule 18 — notes to accounts)</h3>
<p>Required notes include:</p>
<ul><li>capital adequacy (<b>Basel III</b> CRAR, CET1, AT1, Tier 2)</li>
<li>asset quality (gross and net NPAs, movement, provisions)</li>
<li>maturity pattern of assets and liabilities</li>
<li>exposures (real estate, capital market)</li>
<li>concentration of deposits, advances and NPAs</li>
<li>business ratios (interest income to working funds, return on assets, profit per employee)</li>
<li>penalties imposed by RBI, divergence in NPA assessment</li>
<li>related party disclosures, provisions and contingencies</li></ul>
<p>Basel III <b>Pillar 3</b> disclosures are published on the website.</p>

<div class="box trap"><b>Traps:</b>
<ul><li>Acceptances, endorsements and LCs → <b>contingent liabilities</b>, not other liabilities.</li>
<li>Bills for collection → below the balance sheet, not contingent.</li>
<li>Rent, taxes, lighting, printing and stationery → <b>operating expenses (Sch 16)</b>.</li>
<li>Statutory reserve: law says 20%, RBI says <b>25%</b>.</li>
<li>Provide 100% on the <b>unsecured</b> portion of any doubtful asset; the secured portion depends on age.</li></ul></div>
''')

Q('B5', """ABC Bank sanctioned a ₹12 crore term loan; it has been in the Doubtful category for two years (D2). Realisable value of security is ₹7 crore. What is the required provision under IRAC norms?""",
  "₹7.8 crore", ["₹5 crore", "₹12 crore", "₹4.6 crore"],
  "Unsecured portion ₹5 crore → 100% = 5.0. Secured portion ₹7 crore in D2 → 40% = 2.8. Total ₹7.8 crore.")

Q('B5', """Under the Third Schedule, 'Bills Purchased and Discounted' by a bank are shown under:""",
  "Advances (Schedule 9)", ["Investments (Schedule 8)", "Other Assets (Schedule 11)", "Contingent Liabilities (Schedule 12)"],
  "Bills purchased and discounted are a form of credit to customers, so they appear as the first item of Advances.")

Q('B5', """Under which head does a bank show 'Acceptances, endorsements and other obligations' (e.g. LCs, bills accepted on behalf of customers)?""",
  "Contingent liabilities (Schedule 12)", ["Other liabilities and provisions (Schedule 5)", "Borrowings (Schedule 4)", "Deposits (Schedule 3)"],
  "The bank becomes liable only if the customer fails, so these are contingent liabilities, not actual liabilities.")

Q('B5', """A bank has given a festival advance (interest-free) and a housing loan (interest-bearing) to its staff. As per RBI's instructions, they are shown as:""",
  "Housing loan under Advances; festival advance under Other Assets", ["Both under Advances", "Both under Other Assets",
   "Housing loan under Fixed Assets; festival advance under Other Assets"],
  "All interest-bearing staff loans go into Advances (Schedule 9); non-interest-bearing staff advances go into Other Assets (Schedule 11).")

Q('B5', """In a bank's P&L, items such as 'Rent, taxes and lighting' and 'Printing and stationery' are shown under:""",
  "Operating expenses (Schedule 16)", ["Interest expended (Schedule 15)", "Provisions and contingencies", "Other income (Schedule 14), net of recoveries"],
  "Schedule 16 Operating Expenses covers employee costs, rent, taxes and lighting, printing and stationery, advertisement, depreciation, directors' and auditors' fees, law charges, postage, repairs, insurance and others.")

Q('B5', """Before declaring a dividend, a scheduled commercial bank must transfer to the statutory reserve:""",
  "At least 25% of net profit, as RBI requires (the BR Act says 20%)",
  ["Exactly 10% of net profit as per Section 17 of the BR Act", "At least 50% of net profit as per the Companies Act",
   "No transfer is required if CRAR exceeds 9%"],
  "Section 17(1) requires at least 20%; RBI has directed scheduled commercial banks to transfer at least 25% of net profit.")

Q('B5', """In a bank's financial statements, Schedule 18 generally contains:""",
  "Notes to accounts", ["Contingent liabilities", "Interest earned", "Significant accounting policies"],
  "Schedule 17 = significant accounting policies; Schedule 18 = notes to accounts (Basel III, NPAs, maturity pattern, exposures and other RBI-required disclosures).")

Q('B5', """A loan becomes NPA on 31 December. Interest of ₹2 lakh for October–December had been credited to income but not realised. The bank should:""",
  "Reverse the unrealised ₹2 lakh and stop accruing interest to income",
  ["Keep the ₹2 lakh in income and also accrue interest for January–March", "Keep the ₹2 lakh but stop accrual from January",
   "Transfer the ₹2 lakh to the statutory reserve"],
  "Income on NPAs is recognised only on realisation. Interest already taken to income but not realised when the account becomes NPA must be reversed.")

Q('B5', """Which item is shown under 'Interest earned' (Schedule 13)?""",
  "Income on investments in government securities", ["Commission on letters of credit", "Profit on sale of investments",
   "Dividend received from a subsidiary"],
  "Schedule 13: interest/discount on advances and bills, income on investments, interest on balances with RBI and other inter-bank funds. Commission, profit on sale of investments and dividends from subsidiaries are Other Income (Schedule 14).")

Q('B5', """Refinance obtained by a bank from NABARD against agricultural loans is shown:""",
  "Under Borrowings, with the advances shown gross",
  ["As a deduction from the related Advances", "Under Deposits from other institutions", "As a contingent liability in Schedule 12"],
  "RBI's instructions: refinance is shown under 'Borrowings' and advances are shown at the gross amount.")

Q('B5', """Which of the following is shown below the balance sheet total of a bank rather than as a contingent liability?""",
  "Bills for collection", ["Guarantees given on behalf of constituents", "Liability on partly paid investments",
   "Outstanding forward exchange contracts"],
  "Bills for collection are shown as a memorandum item below the balance sheet; the bank acts only as an agent and has no liability.")
