from qb import note, Q

note('A4', r'''
<p class="small">Syllabus: Trial balance (meaning, features, types, disagreement), classification and location of errors, rectification, suspense account, rectification after books are closed, adjusting and closing entries. <b>Asked: 2–5 questions every session, always among the top Module A topics.</b> May 2026 gave 5 case questions: machine entered in the purchases book (effect on fixed assets, profit and TB), a full sale omitted, errors of principle, suspense corrections and profit, and "which errors affect TB".</p>

<h3>1. Trial balance (TB)</h3>
<ul><li>A <b>statement</b> (not an account) of ledger balances on a date, to check <b>arithmetical accuracy</b> of posting.</li>
<li>Types:
<ul><li>Balance method (most common)</li>
<li>Totals method</li>
<li>Totals-cum-balances</li></ul></li>
<li>A TB that agrees is <b>not conclusive proof</b> of correct accounts. Errors of omission, principle, compensating errors and posting to the wrong account on the correct side all pass unnoticed.</li>
<li>Normal balances: assets, expenses, drawings, purchases, sales returns and opening stock are <b>debit</b>. Liabilities, capital, income, sales, purchase returns and provisions are <b>credit</b>.</li>
<li><b>Closing stock</b> usually appears <b>outside</b> the TB and is given as an adjustment. It appears inside only when adjusted through purchases (then it is not shown again in the Trading A/c).</li></ul>

<h3>2. Classification of errors</h3>
<table><tr><th>Error</th><th>Meaning / example</th><th>TB affected?</th></tr>
<tr><td><b>Omission — complete</b></td><td>Transaction not recorded at all (credit sale omitted from the sales book).</td><td><b>No</b></td></tr>
<tr><td><b>Omission — partial</b></td><td>Recorded in the book of original entry but one side not posted (e.g. not posted to the customer's account).</td><td><b>Yes</b></td></tr>
<tr><td><b>Commission</b> (clerical)</td><td>
<ul><li>Wrong amount in the <b>original book</b> (₹4,500 recorded as ₹5,400 on both sides): TB <b>not</b> affected.</li>
<li>Wrong amount <b>posted</b> to one ledger account, wrong side, or casting / carry-forward / balancing errors: TB <b>affected</b>.</li>
<li>Posting to the <b>wrong account of the same class</b> on the correct side (Ram instead of Shyam): TB <b>not</b> affected.</li></ul></td><td>Depends</td></tr>
<tr><td><b>Principle</b></td><td>Violating capital/revenue distinction or accounting principle: furniture debited to Purchases, repairs capitalised, freight on new machine debited to freight outward, sale of old asset credited to Sales.</td><td><b>No</b></td></tr>
<tr><td><b>Compensating</b></td><td>Two errors cancel each other (Ram's account debited ₹100 short, Shyam's credited ₹100 short).</td><td><b>No</b></td></tr></table>
<div class="box key"><b>One-sided errors</b> (affect only one account) disturb the TB and go through the <b>Suspense Account</b>.<br><b>Two-sided errors</b> (both accounts affected) do not disturb the TB and are rectified by a direct entry between the two accounts.</div>

<h3>3. Suspense account</h3>
<ul><li>A temporary account opened for the TB difference so that final accounts can be prepared. If the debit total is short, the suspense account goes on the <b>debit</b> side.</li>
<li>When one-sided errors are found, rectifying entries go through suspense. When all errors are found, suspense closes to nil.</li>
<li>If a suspense balance remains at year-end, it is shown in the Balance Sheet: <b>debit balance</b> under other current assets, <b>credit balance</b> under other current liabilities.</li>
<li>Not every suspense correction changes profit. Correcting a debtor's or creditor's personal account changes only ledger balances.</li></ul>

<h3>4. Rectification method</h3>
<p><b>Rule:</b> compare (a) the entry that was made and (b) the entry that should have been made. Pass the difference.</p>
<table><tr><th>Error</th><th>Rectifying entry</th></tr>
<tr><td>Furniture ₹50,000 bought on credit, debited to Purchases</td><td>Furniture Dr; To Purchases (profit was understated by 50,000; correction raises profit)</td></tr>
<tr><td>Repairs ₹8,000 debited to Machinery</td><td>Repairs Dr; To Machinery (profit was overstated)</td></tr>
<tr><td>Sales book undercast ₹1,000</td><td>Suspense Dr; To Sales</td></tr>
<tr><td>Credit sale ₹5,000 to Ram not posted to Ram's account</td><td>Ram Dr; To Suspense</td></tr>
<tr><td>₹500 received from Mohan posted to the debit of his account</td><td>Suspense Dr; To Mohan ₹1,000 (twice the amount)</td></tr>
<tr><td>Credit sale ₹4,500 recorded in the sales book as ₹5,400</td><td>Sales Dr; To Customer ₹900 (two-sided, no suspense)</td></tr>
<tr><td>Sold old machine ₹20,000 credited to Sales</td><td>Sales Dr; To Machinery</td></tr></table>

<h3>5. Worked case (exam pattern)</h3>
<p>A TB disagrees and the difference goes to suspense. Errors found:</p>
<ol type="a"><li>Sales book overcast ₹10,000.</li>
<li>Purchase of ₹7,500 from Ravi posted to his account as ₹5,700.</li>
<li>Discount allowed ₹600 posted to the credit of Discount Received.</li>
<li>Repairs ₹2,000 debited to Building.</li></ol>
<ul><li><b>TB effect:</b>
<ul><li>(a) credit side excess 10,000</li>
<li>(b) credit side short 1,800</li>
<li>(c) debit side short 600 and credit side excess 600</li>
<li>(d) no effect</li></ul>
Credit total exceeds debit by 10,000 − 1,800 + 1,200 = <b>₹9,400</b>, so suspense opens on the <b>debit side ₹9,400</b>.</li>
<li><b>Profit effect of rectification:</b>
<ul><li>(a) sales reduced → profit −10,000</li>
<li>(b) none (personal account)</li>
<li>(c) discount allowed +600 expense and discount received −600 income → profit −1,200</li>
<li>(d) repairs expensed → −2,000</li></ul>
Net profit falls by <b>₹13,200</b>.</li></ul>

<h3>6. Effect on financial statements (case questions)</h3>
<ul><li><b>Capital item debited to an expense</b> (machine bought, entered in the purchases book):
<ul><li>Profit understated; fixed assets understated; TB agrees.</li>
<li>Depreciation for the period is also missing, which partly offsets the understatement.</li>
<li>Example: ₹18 lakh machine bought 1 Jan, 10% SLM → missing depreciation ₹45,000; profit understated by ₹17.55 lakh.</li></ul></li>
<li><b>Credit sale completely omitted</b> while stock records are correct: sales and debtors understated, so gross profit and receivables are understated. TB still agrees.</li>
<li><b>Expense capitalised:</b> profit and assets overstated.</li>
<li><b>Rectification after books are closed</b> (next year): nominal accounts are already closed, so use <b>Profit &amp; Loss Adjustment A/c</b> instead of the nominal account (or a prior period item under AS 5). Real and personal accounts are rectified directly.</li></ul>

<h3>7. Adjusting and closing entries</h3>
<ul><li><b>Adjusting entries</b> (accrual basis) at year-end: outstanding expenses, prepaid expenses, accrued income, income received in advance, depreciation, bad debts and provision, interest on capital/drawings, closing stock. They are required even if the TB agrees.</li>
<li><b>Closing entries</b> transfer nominal accounts to the Trading and P&amp;L A/c. Real and personal accounts are carried forward.</li></ul>

<div class="box trap"><b>Traps:</b>
<ul><li>Wrong amount in the <b>book of original entry</b> → both sides wrong → TB agrees. Wrong amount <b>posted</b> to one ledger account → TB disagrees.</li>
<li>Posting to the <b>wrong side</b> → double the amount to rectify.</li>
<li>Legal expenses for acquiring land debited to Land is <b>correct</b>, not an error of principle.</li>
<li>Error of principle never affects the TB but often affects profit and assets.</li>
<li>A suspense account is <b>not</b> opened for errors that don't affect the TB.</li></ul></div>
''')

Q('A4', """Which of the following errors will cause the Trial Balance to disagree?
1. A credit sale of ₹4,500 recorded in the Sales Book as ₹5,400.
2. The Purchases Book total undercast by ₹1,000.
3. Repairs to building debited to Building Account.
4. Cash received from Ram ₹2,000 posted to the debit of Ram's account.
5. A credit purchase from Shyam completely omitted from the books.""",
  "2 and 4 only", ["1, 2 and 4 only", "2, 3 and 4 only", "1, 2, 4 and 5 only"],
  "Undercasting a subsidiary book (2) and posting to the wrong side (4) are one-sided errors. An error in the book of original entry (1) affects both sides equally; an error of principle (3) and complete omission (5) leave both sides balanced.")

Q('A4', """A Trial Balance did not agree and the difference was put to Suspense. Errors found:
(a) Sales Book overcast by ₹10,000;
(b) a purchase of ₹7,500 from Ravi posted to his account as ₹5,700;
(c) discount allowed ₹600 posted to the credit of Discount Received Account;
(d) repairs ₹2,000 debited to Building Account.
On which side and for what amount was the Suspense Account opened?""",
  "Debit side, ₹9,400", ["Credit side, ₹9,400", "Debit side, ₹11,400", "Credit side, ₹13,200"],
  "Credit excess: (a) +10,000; (b) Ravi credited 1,800 short → −1,800; (c) discount received credited 600 and discount allowed not debited 600 → credit +600, debit −600 → net 1,200. Total credit excess = 10,000 − 1,800 + 1,200 = 9,400, so suspense is debited ₹9,400. (d) does not affect the TB.")

Q('A4', """For the errors in the previous case [(a) sales book overcast ₹10,000; (b) Ravi's account posted ₹5,700 instead of ₹7,500; (c) discount allowed ₹600 posted to credit of discount received; (d) repairs ₹2,000 debited to Building], what is the effect of the rectification on net profit?""",
  "Net profit decreases by ₹13,200", ["Net profit decreases by ₹9,400", "Net profit decreases by ₹11,200", "Net profit increases by ₹13,200"],
  "(a) sales reduced by 10,000; (b) personal account only, no effect; (c) adds 600 expense and removes 600 income = −1,200; (d) 2,000 charged to repairs. Total = −13,200. Note that the profit effect differs from the suspense amount.")

Q('A4', """A machine bought on credit for ₹18,00,000 on 1 January 2026 was entered in the Purchases Day Book; the supplier was correctly credited. Depreciation is 10% p.a. SLM. If not rectified before the 31 March 2026 accounts are finalised:""",
  "Fixed assets understated by ₹17,55,000, net profit understated by ₹17,55,000, Trial Balance agrees",
  ["Fixed assets understated by ₹18,00,000, net profit overstated by ₹18,00,000, Trial Balance disagrees",
   "Fixed assets overstated by ₹17,55,000, net profit understated by ₹18,00,000, Trial Balance agrees",
   "Only the classification is wrong; profit and assets are unaffected"],
  "Purchases is overstated by ₹18,00,000 (profit understated) but 3 months' depreciation ₹45,000 was not charged (profit overstated by that). Net profit understated = ₹17,55,000. Machine net book value missing = 18,00,000 − 45,000 = ₹17,55,000. Both debit and credit were made, so the TB agrees: an error of principle.")

Q('A4', """A credit sale of goods (cost ₹3,20,000, price ₹4,80,000) was completely omitted from the Sales Day Book; stock records were updated correctly. Before rectification:""",
  "Gross profit and trade receivables are understated by ₹4,80,000 each, and the Trial Balance agrees",
  ["Gross profit is understated by ₹1,60,000 and the Trial Balance disagrees", "Closing stock is overstated by ₹4,80,000",
   "Net profit is unaffected because both sales and cost of sales are omitted"],
  "Stock records were updated (goods excluded from closing stock), so cost of sales already reflects the goods. Only the sale is missing: sales and debtors are both understated by ₹4,80,000. Complete omission affects neither side of the TB.")

Q('A4', """Which of the following are errors of principle?
1. Purchase of office furniture debited to Purchases Account.
2. Annual maintenance expenditure capitalised.
3. Legal expenses for acquiring land debited to Land Account.
4. Freight on a new machine debited to Freight Outward Account.
5. Sale of an old typewriter credited to Sales Account.""",
  "1, 2, 4 and 5 only", ["1, 2 and 4 only", "1, 3 and 5 only", "All five"],
  "1, 2, 4 and 5 confuse capital and revenue items. Legal expenses to acquire land are part of land's cost, so debiting Land is correct (3).")

Q('A4', """₹500 received from Mohan was posted to the debit of his account. The rectifying entry is:""",
  "Suspense A/c Dr ₹1,000; To Mohan ₹1,000", ["Suspense A/c Dr ₹500; To Mohan ₹500", "Mohan Dr ₹1,000; To Suspense A/c ₹1,000",
   "Cash A/c Dr ₹500; To Mohan ₹500"],
  "Mohan should have been credited ₹500 but was debited ₹500. Crediting him ₹1,000 cancels the wrong debit and records the correct credit. The other side goes to suspense because the original error was one-sided.")

Q('A4', """The Finance Executive says: "Every correction passed through the Suspense Account changes the company's profit." Which response is correct?""",
  "Incorrect; corrections to personal or real accounts through suspense change only ledger balances, while those involving nominal accounts change profit",
  ["Correct, because the suspense account is opened only for errors in revenue items such as sales and expenses", "Correct, because every posting error ultimately flows into the Profit and Loss Account",
   "Incorrect, because the suspense account is used only while preparing the bank reconciliation statement"],
  "Suspense absorbs one-sided errors of any account type. Correcting a debtor's or creditor's account through suspense has no P&L effect; correcting sales, purchases or expenses does.")

Q('A4', """A credit sale of ₹123 to Mr M was posted to his account as ₹321. This error will:""",
  "Affect the Trial Balance and be a clerical error of commission", ["Not affect the Trial Balance, being a compensating error",
   "Not affect the Trial Balance, being an error of principle", "Not affect the Trial Balance, being an error of omission"],
  "The sales book shows ₹123 (sales credited ₹123) but Mr M is debited ₹321. Debit side exceeds by ₹198, so the TB disagrees. Wrong amount posting is an error of commission.")

Q('A4', """An error found next year after the accounts were closed: wages of ₹15,000 paid for installing a new machine were debited to Wages Account. The rectifying entry in the new year is:""",
  "Machinery A/c Dr ₹15,000; To Profit & Loss Adjustment A/c ₹15,000", ["Machinery A/c Dr ₹15,000; To Wages A/c ₹15,000",
   "Wages A/c Dr ₹15,000; To Machinery A/c ₹15,000", "Machinery A/c Dr ₹15,000; To Suspense A/c ₹15,000"],
  "After closing, the Wages account (nominal) of last year has been closed to P&L. The correction to last year's profit goes through Profit & Loss Adjustment A/c (or as a prior period item). Machinery (real) is corrected directly.")

Q('A4', """Which statement about the Trial Balance is correct?""",
  "It is a statement, not an account; its agreement shows arithmetical accuracy but not freedom from all errors",
  ["It is an account in the general ledger that must always agree before the books are closed", "It proves that the books of account are free from all errors once its two totals agree",
   "It is prepared only after the final accounts are drawn up, to verify the Balance Sheet"],
  "A TB is a list (statement) of balances prepared before final accounts. Agreement shows only arithmetical accuracy: omissions, principle errors and compensating errors still remain.")

Q('A4', """Which pair contains one error that disturbs the Trial Balance and one that does not?""",
  "Wrong balancing of the Wages Account / Goods bought from Arun posted to Varun's account",
  ["Error of principle / Compensating error", "Complete omission of a credit sale / Wrong amount in the Purchases Book",
   "Undercasting of the Sales Book / Overcasting of the Purchases Returns Book"],
  "Wrong balancing affects one account, so the TB disagrees. Posting to the wrong personal account on the correct side does not affect the TB. The other pairs are both non-disturbing or both disturbing.")

Q('A4', """Closing stock appears inside the Trial Balance in which situation?""",
  "When closing stock has been adjusted through the Purchases Account before preparing the Trial Balance",
  ["Always, since closing stock is an asset that must appear among the debit balances", "Only when stock is valued at market price instead of at cost", "Never, since closing stock is always an adjustment shown outside the Trial Balance"],
  "Normally closing stock is an adjustment outside the TB, recorded in both the Trading A/c and the Balance Sheet. If it was already deducted from purchases (adjusted purchases), it appears in the TB and goes only to the Balance Sheet.")
