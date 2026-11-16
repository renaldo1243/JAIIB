from qb import note, Q

note('A3', r'''
<p class="small">Syllabus: Maintenance of cash/subsidiary books and ledger, record keeping, account categories, debit and credit, journalising. <b>Asked: 1–5 questions on golden rules/journal plus 1–2 on types of accounts per session.</b> May 2026 asked "Machinery is a real account so debit it every time?", classification of Goodwill and Outstanding Salary, petty cash under the imprest system, and journal entries for credit purchase and capital brought in.</p>

<h3>1. Traditional (British) classification and golden rules</h3>
<table><tr><th>Type</th><th>Examples</th><th>Rule</th></tr>
<tr><td><b>Personal</b>
<ul><li>Natural: persons</li>
<li>Artificial: firms, companies, banks, clubs</li>
<li>Representative: accounts standing for a person</li></ul></td><td>Ram, ABC Ltd, Bank, <b>Capital, Drawings</b>, Loan from bank. Representative: <b>Outstanding salary, Prepaid rent, Accrued interest, Income received in advance</b>.</td><td><b>Debit the receiver, credit the giver</b></td></tr>
<tr><td><b>Real</b>
<ul><li>Tangible</li>
<li>Intangible</li></ul></td><td>Cash, stock, machinery, building, furniture. Intangible: <b>Goodwill</b>, patents, trademarks.</td><td><b>Debit what comes in, credit what goes out</b></td></tr>
<tr><td><b>Nominal</b></td><td>Expenses, losses, incomes, gains: salary, rent, <b>discount allowed/received</b>, depreciation, interest, commission, bad debts.</td><td><b>Debit all expenses and losses, credit all incomes and gains</b></td></tr></table>

<h3>2. Modern (accounting-equation) classification</h3>
<table><tr><th>Account</th><th>Increase</th><th>Decrease</th><th>Normal balance</th></tr>
<tr><td>Assets</td><td>Debit</td><td>Credit</td><td>Debit</td></tr>
<tr><td>Expenses / losses</td><td>Debit</td><td>Credit</td><td>Debit</td></tr>
<tr><td>Liabilities</td><td>Credit</td><td>Debit</td><td>Credit</td></tr>
<tr><td>Capital</td><td>Credit</td><td>Debit</td><td>Credit</td></tr>
<tr><td>Revenue / gains</td><td>Credit</td><td>Debit</td><td>Credit</td></tr></table>
<p class="small">Memory line for a trial balance: assets and expenses have debit balances; liabilities, capital and income have credit balances. Drawings has a debit balance (it reduces capital).</p>

<h3>3. "It's a real account, so always debit it?" — capital vs revenue first</h3>
<ul><li>Golden rules tell you <b>which side</b>; capital-vs-revenue tells you <b>which account</b>.</li>
<li>Spending that brings or enhances future economic benefit (purchase price, installation, freight to bring a machine, major component replacement) → debit <b>Machinery</b>.</li>
<li>Routine repairs, lubricants and servicing → debit <b>Repairs / Maintenance (nominal)</b>, even though they relate to machinery.</li>
<li>Insurance claim received for damage to machinery: Dr Bank, Cr Insurance claim / Loss by damage. It is <b>not</b> a debit to Machinery.</li></ul>

<h3>4. Typical entries examiners twist</h3>
<table><tr><th>Transaction</th><th>Entry</th></tr>
<tr><td>Goods bought on credit from AA Ltd</td><td>Purchases A/c Dr; To AA Ltd</td></tr>
<tr><td>Furniture bought on credit</td><td>Furniture A/c Dr; To Supplier (<b>not</b> Purchases — Purchases is only for goods traded)</td></tr>
<tr><td>Owner brings additional cash</td><td>Cash/Bank Dr; To <b>Capital</b></td></tr>
<tr><td>Goods withdrawn by owner</td><td>Drawings Dr; To <b>Purchases</b> (at cost)</td></tr>
<tr><td>Goods given as free samples / charity</td><td>Advertisement / Charity Dr; To Purchases</td></tr>
<tr><td>Goods lost by fire (insured, claim partly admitted)</td><td>Insurance claim Dr + Loss by fire Dr; To Purchases</td></tr>
<tr><td>Cash received from debtor after discount</td><td>Cash Dr + Discount allowed Dr; To Debtor</td></tr>
<tr><td>Paid outstanding electricity</td><td>Outstanding electricity Dr; To Bank</td></tr>
<tr><td>Machinery bought by issuing shares</td><td>Machinery Dr; To Vendor; then Vendor Dr; To Share Capital</td></tr>
<tr><td>Rent for April paid on 28 March</td><td>Prepaid rent Dr; To Cash</td></tr>
<tr><td>Bad debt written off</td><td>Bad debts Dr; To Debtor</td></tr>
<tr><td>Bad debt recovered later</td><td>Cash Dr; To <b>Bad debts recovered</b> (income), not to the debtor</td></tr>
<tr><td>Interest on capital allowed</td><td>Interest on capital Dr; To Capital</td></tr>
<tr><td>Depreciation</td><td>Depreciation Dr; To Asset (or Provision for depreciation)</td></tr></table>

<h3>5. Books of original entry (subsidiary books)</h3>
<table><tr><th>Book</th><th>What goes in</th></tr>
<tr><td>Cash book (single/double/triple column)</td><td>All cash and bank receipts and payments. It is both a book of original entry <b>and</b> a ledger. Triple column: cash, bank, discount. The discount columns are memorandum only and are totalled and posted.</td></tr>
<tr><td>Purchases book</td><td>Only <b>credit purchases of goods</b> (not assets, not cash purchases)</td></tr>
<tr><td>Sales book</td><td>Only <b>credit sales of goods</b></td></tr>
<tr><td>Purchase returns (returns outward) book</td><td>Goods returned to suppliers; supported by a <b>debit note</b></td></tr>
<tr><td>Sales returns (returns inward) book</td><td>Goods returned by customers; supported by a <b>credit note</b></td></tr>
<tr><td>Bills receivable / payable books</td><td>Bills received / accepted</td></tr>
<tr><td>Journal proper</td><td>Opening and closing entries, adjustments, rectification, credit purchase of assets, and anything that fits no other book</td></tr></table>
<p><b>Petty cash, imprest system:</b></p>
<ul><li>The cashier gives the petty cashier a fixed float (the imprest).</li>
<li>At the end of the period the petty cashier is reimbursed exactly what was spent, so the float is restored.</li>
<li>Entry on giving or reimbursing: <b>Petty Cash A/c Dr; To Cash/Bank</b>.</li>
<li>Expenses are later posted from the analytical petty cash book: individual expense accounts Dr; To Petty Cash.</li></ul>
<p><b>Contra entry:</b> a transaction affecting both the cash and bank columns, e.g. cash deposited into bank or cash withdrawn. Mark it "C".</p>
<p><b>Ledger:</b> the book of final entry. Posting from the journal is followed by balancing. The trial balance is prepared from ledger balances.</p>

<div class="box trap"><b>Traps:</b>
<ul><li>Outstanding salary, prepaid rent and accrued interest are <b>representative personal</b> accounts, not nominal.</li>
<li>Goodwill is an intangible <b>real</b> account.</li>
<li>Capital and drawings are <b>personal</b> accounts (of the proprietor).</li>
<li>Discount allowed and discount received are <b>nominal</b> accounts. Trade discount is never recorded.</li>
<li>Credit purchase of furniture goes to the <b>journal proper</b>, not the purchases book.</li>
<li>A sales return wrongly entered as a purchase is an error of principle/commission. To fix it: Sales Return Dr; To Purchases.</li></ul></div>
''')

Q('A3', """A trainee classifies: Goodwill – Nominal; Outstanding Salary – Personal; Drawings – Personal; Discount Received – Real. How many are correct under the traditional classification?""",
  "Two", ["One", "Three", "All four"],
  "Goodwill is an intangible real account (wrong). Outstanding salary is a representative personal account (correct). Drawings is the proprietor's personal account (correct). Discount received is a nominal account, an income (wrong). So two are correct.")

Q('A3', """Which of these is a 'representative personal account'?""",
  "Prepaid Insurance Account", ["Insurance Expense Account", "Furniture Account", "Patents Account"],
  "Prepaid insurance represents the insurance company, which owes service for the unexpired period, so it is a representative personal account. Insurance expense is nominal; furniture and patents are real.")

Q('A3', """Vertex Ltd. made these entries:
1. Purchased office furniture on credit – debited Purchases.
2. Paid outstanding electricity through bank – debited Outstanding Electricity.
3. Received cash from a debtor after allowing discount – debited Cash and Discount Allowed.
4. Bought machinery by issuing equity shares – debited Machinery.
Which evaluation is correct?""",
  "Only entry 1 is wrong; furniture is a fixed asset and must be debited to Furniture Account",
  ["Entries 1 and 3 are wrong, because discount allowed should be credited to the debtor only", "Entries 2 and 4 are wrong, because no cash or bank is involved in entry 4", "All four entries are correct under the traditional golden rules"],
  "Purchases Account is only for goods dealt in. Furniture (a capital asset) is debited to Furniture A/c. Paying an outstanding liability debits the liability; discount to a debtor is a loss (Dr Discount Allowed); asset received for shares debits the asset.")

Q('A3', """The proprietor withdraws goods costing ₹12,000 (sale price ₹15,000) for personal use. The correct entry is:""",
  "Drawings A/c Dr ₹12,000; To Purchases A/c ₹12,000", ["Drawings A/c Dr ₹15,000; To Sales A/c ₹15,000", "Capital A/c Dr ₹12,000; To Stock A/c ₹12,000",
   "Drawings A/c Dr ₹12,000; To Sales A/c ₹12,000"],
  "Goods taken by the owner are recorded at cost and reduce purchases (they were never sold). Debit Drawings (reduces capital), credit Purchases.")

Q('A3', """Under the imprest system of petty cash, the main cashier reimburses the petty cashier ₹4,750 spent during the week. Which account is debited in the main books when the reimbursement is made?""",
  "Petty Cash Account", ["Each expense account directly", "Suspense Account", "Cash Account"],
  "Under the imprest system the cash given to the petty cashier, both initially and as reimbursement, is debited to Petty Cash A/c (credit Cash/Bank). Individual expenses are posted from the petty cash book later.")

Q('A3', """Which of the following is recorded in the Purchases Day Book?""",
  "Goods bought on credit for resale", ["Machinery bought on credit", "Goods bought for cash", "Stationery bought on credit for office use"],
  "The purchases book records only credit purchases of goods in which the business deals. Credit purchases of assets or office supplies go to the journal proper; cash purchases go to the cash book.")

Q('A3', """A business records a sales return of ₹4,000 as a purchase of ₹4,000. Which single rectifying entry corrects it (books not closed)?""",
  "Sales Returns A/c Dr ₹4,000; To Purchases A/c ₹4,000", ["Purchases A/c Dr ₹4,000; To Sales Returns A/c ₹4,000",
   "Sales Returns A/c Dr ₹8,000; To Purchases A/c ₹8,000", "Debtors A/c Dr ₹4,000; To Purchases A/c ₹4,000"],
  "Purchases was wrongly debited, so credit it to remove the debit. Sales Returns should have been debited, so debit it. The party's account side was the same in both cases (credited), so it needs no change.")

Q('A3', """Which entry is correct when goods costing ₹50,000 are destroyed by fire and the insurer admits a claim of ₹35,000?""",
  "Insurance Claim A/c Dr ₹35,000 and Loss by Fire A/c Dr ₹15,000; To Purchases A/c ₹50,000",
  ["Loss by Fire A/c Dr ₹50,000; To Stock A/c ₹50,000", "Insurance Company A/c Dr ₹50,000; To Purchases A/c ₹50,000",
   "Cash A/c Dr ₹35,000 and Loss by Fire A/c Dr ₹15,000; To Sales A/c ₹50,000"],
  "Goods lost are removed from purchases at cost. The admitted claim is an amount receivable (insurance company / claim account), and the balance is a loss charged to P&L.")

Q('A3', """A debt of ₹20,000 written off as bad last year is recovered this year. The correct entry is:""",
  "Cash A/c Dr; To Bad Debts Recovered A/c", ["Cash A/c Dr; To Debtor's Personal A/c", "Debtor's A/c Dr; To Bad Debts A/c", "Cash A/c Dr; To Bad Debts A/c"],
  "The debtor's account was closed when the debt was written off. The recovery is an income/gain of the current year, credited to Bad Debts Recovered (a nominal account).")

Q('A3', """In a triple-column cash book, which statement is correct?""",
  "The discount columns are not balanced; their totals are posted to Discount Allowed and Discount Received accounts",
  ["The discount columns are balanced like the cash and bank columns and the balances carried forward", "Trade discount and cash discount are both recorded in the discount columns",
   "A contra entry is recorded only in the cash column and never in the bank column"],
  "Discount columns are memorandum columns: they are totalled, not balanced, and the totals are posted to the ledger. Trade discount is never recorded. A contra entry (cash deposited/withdrawn) affects both cash and bank columns.")

Q('A3', """Under the modern approach, which pair of accounts both normally carry a CREDIT balance?""",
  "Outstanding wages and Commission received", ["Drawings and Capital introduced", "Prepaid rent and Trade creditors", "Discount allowed and Net sales"],
  "Liabilities (outstanding wages) and incomes (commission received) have credit balances. Drawings, prepaid rent and discount allowed have debit balances.")

Q('A3', """Which of the following statements on double entry is correct?""",
  "Every transaction affects at least two accounts, with equal debit and credit amounts",
  ["Every transaction is recorded twice in the same account", "Every transaction has one debit and one credit only, never more",
   "Double entry ensures that all errors are automatically detected"],
  "Double entry means equal debits and credits for every transaction (a compound entry can have several accounts). It makes the trial balance agree but does not catch errors like omission, principle or compensating errors.")
