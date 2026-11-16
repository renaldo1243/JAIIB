from qb import note, Q

note('A2', r'''
<p class="small">Syllabus: Basic accountancy procedures (concepts, going concern, double entry, conservatism, revenue recognition, accrual vs cash) + <b>Balance Sheet Equation</b> (Module B). <b>Asked: 3–4 questions on concepts plus 1–3 on the equation every session.</b> May 2026: "which concept contradicts this view", "match the concept with its use", "profit always increases liabilities?", "cash basis vs accrual".</p>

<h3>1. Concepts (assumptions) vs conventions</h3>
<table><tr><th>Concept</th><th>Meaning</th><th>Where it shows up in questions</th></tr>
<tr><td><b>Business entity</b></td><td>Business is separate from the owner, even in a sole proprietorship (where it is not legally separate).</td><td>Owner's personal insurance paid from business = <b>drawings</b>. Capital is a liability of the business to the owner. Profit added to capital.</td></tr>
<tr><td><b>Money measurement</b></td><td>Only events measurable in money are recorded.</td><td>Staff morale, a CEO's skill and a strike threat are not recorded.</td></tr>
<tr><td><b>Going concern</b></td><td>Business will continue for the foreseeable future.</td><td>Basis for showing assets at cost less depreciation (not liquidation value), prepaid expenses as assets, and classifying current and non-current items.</td></tr>
<tr><td><b>Accounting period</b></td><td>Life is split into periods (FY April–March).</td><td>Basis for accruals and adjustments.</td></tr>
<tr><td><b>Cost (historical cost)</b></td><td>Assets are recorded at acquisition cost, not market value.</td><td>Car bought for ₹10 lakh, now worth ₹12 lakh → still ₹10 lakh.</td></tr>
<tr><td><b>Dual aspect</b></td><td>Every transaction has two equal effects: Assets = Liabilities + Capital.</td><td>Basis of double entry.</td></tr>
<tr><td><b>Realisation / revenue recognition</b></td><td>Revenue is recognised when earned (goods transferred, service rendered), not when cash is received.</td><td>Goods on approval are not revenue until approved.</td></tr>
<tr><td><b>Accrual</b></td><td>Record income when earned and expense when incurred, regardless of cash. It distinguishes the <b>right to receive</b> cash from the <b>receipt</b> of cash.</td><td>Outstanding and prepaid expenses, accrued income.</td></tr>
<tr><td><b>Matching</b></td><td>Expenses of a period are matched with that period's revenue.</td><td>Depreciation, closing stock, unexpired insurance.</td></tr>
<tr><td><b>Objectivity / verifiability</b></td><td>Entries are supported by vouchers and evidence.</td><td>—</td></tr></table>
<table><tr><th>Convention</th><th>Meaning</th></tr>
<tr><td><b>Conservatism (prudence)</b></td><td>"Anticipate no profit, provide for all possible losses." Examples: stock at lower of cost or NRV; provision for doubtful debts; no provision for discount on creditors. It is applied with care: no secret reserves.</td></tr>
<tr><td><b>Consistency</b></td><td>Same methods year to year for comparability. Change only for valid reasons (AS 5).</td></tr>
<tr><td><b>Materiality</b></td><td>Insignificant items need not be shown separately (e.g. a stapler bought is expensed even if it lasts years).</td></tr>
<tr><td><b>Full disclosure</b></td><td>All material information is disclosed (notes, contingent liabilities).</td></tr></table>
<p class="small">AS 1 names three <b>fundamental accounting assumptions</b>: going concern, consistency and accrual. If they are followed, no disclosure is needed; if not followed, disclose.</p>

<h3>2. Cash basis vs accrual basis</h3>
<ul><li>Cash basis records only receipts and payments. It ignores outstanding fees, prepaid rent and unpaid bills, so profit is distorted.</li>
<li>The Companies Act (Sec 128) <b>requires accrual basis and double entry</b> for companies.</li>
<li>Some professionals and small entities may use the cash basis, so it is not prohibited for every entity.</li></ul>

<h3>3. Stages of accounting</h3>
<p>Recording (journal, subsidiary books) → Classifying (ledger) → Summarising (trial balance, final accounts) → Analysing and interpreting → Communicating (reporting).</p>
<ul><li>Concepts like <b>dual aspect, money measurement and objectivity</b> work at the recording stage.</li>
<li><b>Going concern, consistency, conservatism, materiality and full disclosure</b> are reporting-stage concepts.</li>
<li>Accounting is called the <b>language of business</b>.</li>
<li>Book-keeping is the recording part only; accounting is wider.</li>
<li><b>Limitations of accounting:</b> it ignores non-monetary facts, is based on historical cost (price changes ignored), and relies on estimates (depreciation, provisions).</li></ul>

<h3>4. Balance Sheet (accounting) equation</h3>
<div class="box key"><b>Assets = Liabilities + Capital</b><br>
Capital = Assets − Liabilities.<br>
Closing capital = Opening capital + Fresh capital + Profit − Drawings (profit raises capital; loss and drawings reduce it).</div>
<table><tr><th>Transaction</th><th>Assets</th><th>Liabilities</th><th>Capital</th></tr>
<tr><td>Owner introduces cash</td><td>↑</td><td>—</td><td>↑</td></tr>
<tr><td>Buy furniture for cash</td><td>↑↓ (no change in total)</td><td>—</td><td>—</td></tr>
<tr><td>Buy goods on credit</td><td>↑</td><td>↑</td><td>—</td></tr>
<tr><td>Pay a creditor / repay a loan</td><td>↓</td><td>↓</td><td>—</td></tr>
<tr><td>Pay salary (expense)</td><td>↓</td><td>—</td><td>↓</td></tr>
<tr><td>Expense outstanding</td><td>—</td><td>↑</td><td>↓</td></tr>
<tr><td>Owner withdraws cash</td><td>↓</td><td>—</td><td>↓</td></tr>
<tr><td>Sale of goods (cost 60) for 100 cash</td><td>↑40 net</td><td>—</td><td>↑40</td></tr>
<tr><td>Convert a creditor's dues into a loan</td><td>—</td><td>one ↑ one ↓</td><td>—</td></tr>
<tr><td>Equity converted into a loan</td><td>—</td><td>↑</td><td>↓</td></tr>
<tr><td>Dividend declared (not yet paid)</td><td>—</td><td>↑</td><td>↓</td></tr></table>
<p><b>Profit and liabilities:</b> profit first increases <b>capital (owners' equity)</b> through retained earnings. It touches liabilities only when management later declares a dividend (liability ↑) or uses the cash to repay debt (liability ↓). So "profit always increases liabilities" is wrong.</p>
<p><b>Worked example:</b> Cash ₹40,000, debtors ₹60,000, stock ₹50,000, machinery ₹1,50,000, creditors ₹70,000, bank loan ₹1,00,000. Assets = 3,00,000; liabilities = 1,70,000; capital = ₹1,30,000.</p>

<div class="box trap"><b>Traps:</b>
<ul><li>Capital is a <b>liability</b> of the business (business entity concept), even though it belongs to the owner.</li>
<li>Asset bought for ₹10 lakh, market value ₹12 lakh → record at ₹10 lakh (cost concept, not conservatism).</li>
<li>"Anticipate no profit, provide for all losses" = conservatism. "Same method every year" = consistency.</li>
<li>Prepaid expense being an asset rests on accrual plus going concern.</li>
<li>Purchase of an asset for cash does <b>not</b> change total assets.</li></ul></div>
''')

Q('A2', """Mr Raj, a sole proprietor, pays from the business bank account: (i) his personal life-insurance premium, (ii) school fees of his son, and (iii) the shop's electricity bill. The accountant debits all three to expenses, saying "the proprietor and the business are legally the same person". Which concept is violated and what is the correct treatment of (i) and (ii)?""",
  "Business entity concept; (i) and (ii) are debited to Drawings Account",
  ["Going concern concept; (i) and (ii) are debited to Capital Reserve", "Money measurement concept; (i) and (ii) are not recorded at all",
   "Matching concept; (i) and (ii) are shown as prepaid expenses"],
  "Accounting treats the business as separate from the owner even when the law does not (sole proprietorship). Personal payments are drawings, reducing the owner's capital. Only the shop's electricity is a business expense.")

Q('A2', """A company bought land for ₹2 crore five years ago. A valuer now says it is worth ₹3.5 crore. The CFO wants to show it at ₹3.5 crore "to reflect reality". Under traditional accounting (no revaluation policy), the land stays at ₹2 crore mainly because of:""",
  "The historical cost concept", ["The conservatism convention", "The materiality convention", "The money measurement concept"],
  "Assets are recorded at acquisition cost and not at current market value: the cost concept. Conservatism concerns anticipating losses, not ignoring gains on an asset. Revaluation is possible only as a deliberate policy under AS 10 / Ind AS 16.")

Q('A2', """Which of the following is an application of the conservatism (prudence) convention?
1. Valuing closing stock at the lower of cost and net realisable value.
2. Creating a provision for doubtful debts.
3. Creating a provision for discount on creditors.
4. Ignoring an expected profit on a contract not yet executed.""",
  "1, 2 and 4 only", ["1, 2, 3 and 4", "1 and 2 only", "2, 3 and 4 only"],
  "Prudence anticipates losses but not gains. Stock at lower of cost/NRV, provision for doubtful debts and ignoring unrealised profit apply it. A provision for discount on creditors anticipates a gain, so it is NOT made under conservatism.")

Q('A2', """Going concern assumption justifies which of the following?""",
  "Showing fixed assets at cost less depreciation rather than at their forced-sale value",
  ["Recording only those transactions that can be measured in terms of money", "Treating the proprietor's withdrawals for personal use as drawings",
   "Recording revenue only when the cash is actually received from customers"],
  "Because the business is expected to continue, assets are shown at cost less depreciation (used over their life), not at liquidation value. Prepaid expenses and long-term liabilities also rest on going concern.")

Q('A2', """A consulting firm on cash basis has, for March: fees earned but unpaid ₹3 lakh, April rent paid in March ₹50,000, March electricity unpaid ₹20,000. By how much does accrual-basis profit for March differ from cash-basis profit (assuming nothing else)?""",
  "Accrual profit is higher by ₹3.30 lakh", ["Accrual profit is higher by ₹2.30 lakh", "Accrual profit is lower by ₹0.70 lakh", "Accrual profit is higher by ₹3.70 lakh"],
  "Accrual adds unpaid fees (+3,00,000), removes April rent paid in March from March expense (+50,000), and adds unpaid March electricity (−20,000). Net: +3,30,000.")

Q('A2', """Which concept distinguishes the receipt of cash from the right to receive cash, and the payment of cash from the legal obligation to pay?""",
  "Accrual concept", ["Cost concept", "Dual aspect concept", "Money measurement concept"],
  "Under the accrual concept income is recorded when the right to receive arises (earned) and expense when the obligation arises (incurred), regardless of the timing of cash.")

Q('A2', """Under AS 1, which are the fundamental accounting assumptions whose observance need NOT be disclosed?""",
  "Going concern, consistency and accrual", ["Prudence, substance over form and materiality", "Going concern, prudence and accrual",
   "Consistency, materiality and full disclosure"],
  "AS 1 names going concern, consistency and accrual as fundamental assumptions. If followed, no disclosure is needed; if not followed, the fact must be disclosed. Prudence, substance over form and materiality guide the choice of policies.")

Q('A2', """A business has: Cash ₹40,000; Debtors ₹65,000; Stock ₹85,000; Machinery ₹2,10,000; Creditors ₹90,000; Bank loan ₹1,20,000; Outstanding wages ₹10,000; Prepaid rent ₹5,000. What is the owner's capital?""",
  "₹1,85,000", ["₹1,75,000", "₹1,95,000", "₹2,85,000"],
  "Assets = 40,000 + 65,000 + 85,000 + 2,10,000 + 5,000 = 4,05,000. Liabilities = 90,000 + 1,20,000 + 10,000 = 2,20,000. Capital = 4,05,000 − 2,20,000 = ₹1,85,000. Prepaid rent is an asset; outstanding wages are a liability.")

Q('A2', """Opening capital ₹5,00,000; additional capital introduced ₹1,00,000; drawings ₹60,000; closing capital ₹6,90,000. What was the profit for the year?""",
  "₹1,50,000", ["₹90,000", "₹1,90,000", "₹2,50,000"],
  "Closing capital = Opening + additional capital + profit − drawings. 6,90,000 = 5,00,000 + 1,00,000 + P − 60,000 → P = 6,90,000 − 5,40,000 = ₹1,50,000.")

Q('A2', """Which transaction changes BOTH total assets and total liabilities but leaves capital unchanged?""",
  "Repayment of a bank loan by cheque", ["Purchase of furniture for cash", "Payment of salary in cash", "Withdrawal of cash by the proprietor for personal use"],
  "Loan repayment reduces bank (asset) and loan (liability) equally. Furniture for cash only swaps assets. Salary and drawings reduce assets and capital.")

Q('A2', """A company converts part of its equity share capital into a loan from the promoter. The effect on the accounting equation is:""",
  "Liabilities increase and capital decreases; total assets are unchanged",
  ["Assets and liabilities both increase, because the loan brings in fresh funds", "Assets decrease and capital decreases, because equity is paid out", "No element of the equation changes, because no cash moves"],
  "No cash moves, so assets are unchanged. Owners' funds fall and outside liabilities rise by the same amount.")

Q('A2', """The Finance Manager says: "Whenever the company earns a profit, its liabilities must go up." Which response is correct?""",
  "Profit first increases owners' equity through retained earnings; liabilities change only if a dividend is declared or debt is repaid later",
  ["Correct, because profit is always owed to shareholders and must be shown as a current liability", "Correct, because a profit always results in higher trade creditors and outstanding expenses",
   "Profit has no effect on the Balance Sheet at all; it affects only the Statement of Profit and Loss"],
  "Profit raises capital (reserves). Declaring a dividend creates a liability; using profit to repay a loan reduces liabilities; reinvesting it in assets changes asset mix. So there is no automatic increase in liabilities.")

Q('A2', """A stapler costing ₹350 that will last three years is charged to expenses in the year of purchase. Which convention justifies this?""",
  "Materiality", ["Consistency", "Conservatism", "Full disclosure"],
  "Materiality allows insignificant items to be treated in the simplest way. Capitalising and depreciating a ₹350 item would not change any user's decision.")

Q('A2', """Consider the following statements:
1. Accounting is often called the 'language of business'.
2. Book-keeping covers recording, classifying, summarising and interpreting.
3. Accounting records only events that can be expressed in money.
4. A limitation of accounting is that it is based on historical cost and ignores price-level changes.
Which are correct?""",
  "1, 3 and 4 only", ["1, 2 and 3 only", "2 and 4 only", "1, 2, 3 and 4"],
  "Book-keeping is only the recording (and posting) stage. Analysis and interpretation are part of accounting, not book-keeping. The rest are correct.")

Q('A2', """Goods sent to a customer on approval on 28 March (cost ₹60,000, price ₹80,000) were recorded as sales; the customer had not approved by 31 March. Which concept is breached, and what is the correction?""",
  "Revenue recognition (realisation); reverse the sale and include the goods at cost in closing stock",
  ["Going concern; show the debtor at ₹80,000 with a provision of ₹20,000 against it", "Consistency; keep the sale as recorded but disclose the approval terms in notes",
   "Materiality; no correction is needed since the goods have already left the warehouse"],
  "Revenue is recognised only when risks and rewards pass. Goods on approval still belong to the seller until approved, so the sale is reversed and the goods are included in stock at cost (₹60,000), not at sale price.")
