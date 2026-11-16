from qb import note, Q

note('B1', r'''
<p class="small">Syllabus: Preparation of trial balance, adjustment entries, preparation of financial statements from the trial balance. <b>Asked: 4–5 questions every session, the biggest Module B topic.</b> Recent papers asked:</p>
<ul class="small"><li>GP from data</li>
<li>items on the debit side of the Trading A/c</li>
<li>goods on approval in closing stock</li>
<li>year-end adjustments</li>
<li>items not debited to the P&amp;L Appropriation A/c</li>
<li>cash balance from receipts and payments</li></ul>

<h3>1. Trading Account (gross profit)</h3>
<table><tr><th>Debit side</th><th>Credit side</th></tr>
<tr><td>
<ul><li>Opening stock</li>
<li>Purchases less returns outward</li>
<li><b>Direct expenses</b>: wages, carriage/freight <b>inward</b>, octroi, import duty, power and fuel, factory rent and lighting, royalty on production</li></ul></td>
<td>
<ul><li>Sales less returns inward</li>
<li>Closing stock</li></ul></td></tr></table>
<div class="box key">COGS = Opening stock + Net purchases + Direct expenses − Closing stock.<br>
<b>GP = Net sales − COGS</b>.<br>
GP % on sales vs mark-up on cost: 25% on sales = 33⅓% on cost.</div>
<p><b>Example:</b> opening stock 17,000; purchases 52,000; wages 8,000; carriage inward 2,000; sales 1,10,000; returns inward 5,000; closing stock 20,000.
<br>COGS = 17,000 + 52,000 + 8,000 + 2,000 − 20,000 = 59,000; net sales = 1,05,000; <b>GP = 46,000</b>.</p>
<p><b>Closing stock from the GP ratio:</b> sales ₹18 crore, GP 25% → COGS 13.5. Opening 2.10 + purchases 11.80 + carriage 0.40 = 14.30, so <b>closing stock = 0.80 crore</b>.</p>
<p><b>Goods sent on approval</b> and not yet approved:</p>
<ul><li>If wrongly recorded as sales, reverse the sale.</li>
<li>Include the goods in closing stock <b>at cost</b> (or NRV if lower), not at sale price.</li></ul>

<h3>2. Profit &amp; Loss Account (net profit)</h3>
<ul><li><b>Debit side (indirect expenses):</b>
<ul><li>salaries, office rent, carriage <b>outward</b>, advertisement</li>
<li>bad debts, provision for doubtful debts</li>
<li>depreciation, interest on loan, discount allowed</li>
<li>loss by fire (uninsured part)</li></ul></li>
<li><b>Credit side:</b> gross profit, discount received, commission, interest and rent received, bad debts recovered, profit on sale of assets.</li></ul>

<h3>3. Adjustments — each has two effects</h3>
<table><tr><th>Adjustment</th><th>P&amp;L</th><th>Balance Sheet</th></tr>
<tr><td>Closing stock</td><td>Credit Trading A/c</td><td>Current asset</td></tr>
<tr><td>Outstanding expense</td><td>Add to the expense</td><td>Current liability</td></tr>
<tr><td>Prepaid expense</td><td>Deduct from the expense</td><td>Current asset</td></tr>
<tr><td>Accrued income</td><td>Add to the income</td><td>Current asset</td></tr>
<tr><td>Income received in advance</td><td>Deduct from the income</td><td>Current liability</td></tr>
<tr><td>Depreciation</td><td>Debit</td><td>Deduct from the asset</td></tr>
<tr><td>Further bad debts + new provision</td><td>Bad debts (TB + new) + new provision − old provision</td><td>Debtors − further bad debts − new provision</td></tr>
<tr><td>Interest on capital</td><td>Debit (P&amp;L Appropriation for a firm)</td><td>Add to capital</td></tr>
<tr><td>Interest on drawings</td><td>Credit</td><td>Deduct from capital</td></tr>
<tr><td>Goods taken by the owner</td><td>Reduce purchases</td><td>Add to drawings</td></tr>
<tr><td>Abnormal loss (fire), insured</td><td>Credit Trading with the full loss; debit P&amp;L with the uninsured part</td><td>Claim receivable is a current asset</td></tr></table>
<p><b>Provision example:</b> debtors 1,00,000; further bad debts 2,000; new provision 5% of remaining debtors (98,000) = 4,900; old provision 3,000; bad debts in TB 1,500.</p>
<ul><li>P&amp;L charge = 1,500 + 2,000 + 4,900 − 3,000 = <b>5,400</b>.</li>
<li>Debtors in the Balance Sheet = 98,000 − 4,900 = <b>93,100</b>.</li></ul>

<h3>4. Partnership P&amp;L Appropriation Account</h3>
<ul><li><b>Debited:</b>
<ul><li>interest on partners' capital</li>
<li>partners' salary and commission</li>
<li>transfer to reserve</li>
<li>share of profit</li></ul></li>
<li><b>Credited:</b> net profit b/d, interest on drawings.</li>
<li><b>NOT in the Appropriation A/c:</b> interest on a <b>partner's loan</b>, rent paid to a partner, managers' commission. These are <b>charges</b> against profit and go to the P&amp;L A/c.</li></ul>

<h3>5. Other formats</h3>
<ul><li><b>Balance Sheet (sole trader):</b> liabilities = capital (+ profit − drawings), loans, creditors, outstanding expenses. Assets = fixed assets (less depreciation), investments, stock, debtors (less provision), cash, prepaid expenses.</li>
<li><b>Cash balance check:</b> opening cash + receipts − payments = closing cash. Cash can never be credit (negative); bank can (overdraft).</li></ul>

<div class="box trap"><b>Traps:</b>
<ul><li>Carriage <b>inward</b> → Trading. Carriage <b>outward</b> → P&amp;L.</li>
<li>Goods on approval → closing stock at <b>cost</b>, not sale price.</li>
<li>Interest on a partner's <b>loan</b> → P&amp;L, not appropriation.</li>
<li>Bad debts recovered is income. The old provision reduces the new charge.</li>
<li>Adjustments given outside the TB affect two places. Items inside the TB affect one.</li></ul></div>
''')

Q('B1', """Opening stock ₹17,000; purchases ₹52,000; wages ₹8,000; carriage inward ₹2,000; sales ₹1,10,000; returns inward ₹5,000; carriage outward ₹3,000; closing stock ₹20,000. What is the gross profit?""",
  "₹46,000", ["₹43,000", "₹51,000", "₹41,000"],
  "COGS = 17,000 + 52,000 + 8,000 + 2,000 − 20,000 = 59,000. Net sales = 1,10,000 − 5,000 = 1,05,000. GP = 46,000. Carriage outward is a selling expense (P&L), not in COGS.")

Q('B1', """Net sales ₹18 crore; GP ratio 25% on sales; opening stock ₹2.10 crore; net purchases ₹11.80 crore; carriage inward ₹40 lakh. What is the closing stock?""",
  "₹0.80 crore", ["₹1.20 crore", "₹1.50 crore", "₹0.40 crore"],
  "COGS = 75% of 18 = 13.50. Goods available = 2.10 + 11.80 + 0.40 = 14.30. Closing stock = 14.30 − 13.50 = ₹0.80 crore.")

Q('B1', """Goods costing ₹32 lakh (price ₹40 lakh) were sent on approval on 28 March and recorded as sales; the customer had neither approved nor rejected them by 31 March. The correct treatment is:""",
  "Reverse the ₹40 lakh sale and include the goods in closing stock at ₹32 lakh (cost)",
  ["Keep the sale, because the goods physically left the warehouse before 31 March", "Reverse the sale and include the goods in closing stock at ₹40 lakh (sale price)",
   "Keep the sale but create a provision of ₹8 lakh for the unrealised profit margin"],
  "Risks and rewards have not passed, so it is not a sale. The goods are still the seller's stock, valued at cost (or NRV if lower), not at sale price.")

Q('B1', """Which of the following appears on the DEBIT side of the Trading Account?""",
  "Carriage inward on raw materials", ["Carriage outward on goods sold", "Salaries of office staff", "Discount allowed to customers"],
  "Direct expenses that bring goods to saleable condition and location (carriage inward, wages, factory power) go to Trading. The others are indirect expenses for the P&L.")

Q('B1', """Debtors ₹1,00,000; further bad debts ₹2,000; provision for doubtful debts to be 5% of debtors; existing provision ₹3,000; bad debts already in the trial balance ₹1,500. What is the total charge to the P&L for bad and doubtful debts?""",
  "₹5,400", ["₹8,400", "₹6,900", "₹4,900"],
  "New provision = 5% × (1,00,000 − 2,000) = 4,900. Charge = 1,500 + 2,000 + 4,900 − 3,000 = ₹5,400. Forgetting the old provision gives 8,400.")

Q('B1', """Which item is NOT debited to a partnership firm's Profit & Loss Appropriation Account?""",
  "Interest on a loan advanced by a partner to the firm", ["Interest on partners' capital", "Salary payable to a working partner",
   "Amount transferred to General Reserve"],
  "Interest on a partner's loan is a charge against profit (debited to the P&L A/c), payable even if there is a loss. The others are appropriations of profit.")

Q('B1', """At year-end Delta Ltd. has outstanding salary, prepaid insurance, interest accrued but not due on investments, and depreciation on plant. The accountant wants to adjust only depreciation because the others involve no cash this year. Which is correct?""",
  "All four need adjustment entries under the accrual basis, whatever the timing of cash",
  ["Only depreciation needs adjustment, because the others involve no immediate cash flow", "Adjustments are optional if the trial balance has already agreed",
   "Only outstanding salary needs adjustment, because it is a legal liability to employees"],
  "Accrual accounting records income and expenses in the period they relate to. Outstanding and prepaid expenses and accrued income are all adjusted at year-end, not just depreciation.")

Q('B1', """Rent of ₹60,000 is paid for 15 months from 1 January 2025; the year ends 31 March 2025. How much rent is charged to the P&L for the year and how much is prepaid?""",
  "₹12,000 to P&L; ₹48,000 prepaid", ["₹60,000 to P&L; nil prepaid", "₹48,000 to P&L; ₹12,000 prepaid", "₹36,000 to P&L; ₹24,000 prepaid"],
  "Monthly rent = 60,000/15 = 4,000. Jan–Mar = 3 months = ₹12,000 expense. The remaining 12 months (₹48,000) is a prepaid expense (current asset).")

Q('B1', """A firm has opening cash of ₹50,000, cash receipts from sales ₹2,50,000, cash expenses ₹1,80,000 and drawings ₹30,000. Closing cash is:""",
  "₹90,000", ["₹1,20,000", "₹70,000", "₹1,50,000"], "50,000 + 2,50,000 − 1,80,000 − 30,000 = ₹90,000.")

Q('B1', """Stock costing ₹1,00,000 was destroyed by fire; the insurer admitted a claim of ₹70,000. How is this shown in the final accounts?""",
  "Trading A/c Cr ₹1,00,000; P&L Dr ₹30,000; claim ₹70,000 as an asset",
  ["Only ₹30,000 is debited to the Trading A/c and nothing else is recorded", "₹1,00,000 is debited to the P&L A/c and ₹70,000 credited to Capital",
   "Closing stock is increased by ₹70,000 and the loss is ignored"],
  "The goods are removed from the Trading A/c (credited at cost), the uninsured part is a loss in the P&L, and the admitted claim is a current asset until received.")

Q('B1', """GP is 25% on sales. What is the equivalent mark-up on cost?""",
  "33⅓%", ["25%", "20%", "40%"], "If sales are 100, GP 25, cost 75: 25/75 = 33⅓% on cost. (A 25% mark-up on cost would be 20% on sales.)")
