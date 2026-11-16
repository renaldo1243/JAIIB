from qb import note, Q

note('A7', r'''
<p class="small">Syllabus: Capital vs revenue expenditure, receipts. In the May 2026 paper it came with AS 10. <b>Asked: 1–2 questions every session, plus 2–3 hidden inside golden-rule and error questions.</b> May 2026 asked:</p>
<ul class="small"><li>Is every machinery cost debited to Machinery?</li>
<li>Major inspection cost (AS 10)</li>
<li>Kiln: freight, installation, maintenance, major part replacement</li>
<li>₹5,000 replacement of a worn-out part</li></ul>

<h3>1. The test</h3>
<table><tr><th></th><th>Capital expenditure</th><th>Revenue expenditure</th></tr>
<tr><td>Benefit</td><td>Lasts more than one year</td><td>Used up within the year</td></tr>
<tr><td>Purpose</td><td>Acquire, extend, improve or enhance a fixed asset (capacity, life, efficiency, cost reduction)</td><td>Maintain the asset in its existing condition; day-to-day running</td></tr>
<tr><td>Shown in</td><td>Balance Sheet (asset), then depreciated</td><td>P&amp;L of the year</td></tr>
<tr><td>Recurrence</td><td>Non-recurring generally</td><td>Recurring</td></tr></table>

<h3>2. AS 10 — what goes into the cost of PPE</h3>
<table><tr><th>Capitalise (include in cost)</th><th>Do NOT capitalise (expense)</th></tr>
<tr><td>
<ul><li>Purchase price, import duties, <b>non-refundable</b> taxes, less trade discounts and rebates</li>
<li>Site preparation</li>
<li>Initial delivery and handling (freight inward)</li>
<li>Installation and assembly, including <b>wages of own staff</b> for installation</li>
<li>Testing, less net proceeds of samples produced during testing</li>
<li>Professional fees (architects, engineers)</li>
<li>Initial estimate of dismantling and site-restoration cost</li>
<li>Borrowing cost on a qualifying asset (AS 16)</li></ul></td>
<td>
<ul><li>Costs of opening a new facility</li>
<li>Introducing a new product (advertising, promotion)</li>
<li>Doing business in a new location or with a new class of customers (staff training)</li>
<li>Administration and general overheads</li>
<li>Costs after the asset is ready (initial operating losses, idle time)</li>
<li>Relocation or reorganisation</li>
<li><b>Refundable</b> GST / input tax credit available</li></ul></td></tr></table>

<h3>3. Subsequent costs (after the asset is in use)</h3>
<ul><li><b>Day-to-day servicing</b> (labour, consumables, small parts, lubricants, AMC): expense.</li>
<li><b>Replacement of a significant part</b> (kiln lining, aircraft seats, engine): capitalise if the recognition criteria are met, and <b>derecognise</b> the carrying amount of the replaced part (component approach).</li>
<li><b>Major inspection</b> (e.g. a statutory overhaul every 5 years, without which the asset cannot operate): <b>capitalise</b> as a component if the recognition criteria are met, even though no new part is fitted. Derecognise any remaining cost of the previous inspection.</li>
<li><b>Repairs to a second-hand asset</b> to make it usable at purchase: capital. Later regular repairs: revenue.</li>
<li><b>Spare parts and stand-by equipment</b> used for more than one period: PPE. Others are inventory.</li></ul>

<h3>4. Classic examples</h3>
<table><tr><th>Item</th><th>Nature</th></tr>
<tr><td>Freight and cartage on a new machine</td><td>Capital</td></tr>
<tr><td>Freight on goods purchased</td><td>Revenue (part of cost of goods, Trading A/c)</td></tr>
<tr><td>Legal fees for buying land; registration and stamp duty</td><td>Capital</td></tr>
<tr><td>White-washing / painting an existing building annually</td><td>Revenue</td></tr>
<tr><td>Addition of a new floor; extension of building</td><td>Capital</td></tr>
<tr><td>Replacing a worn-out small part to keep the machine running</td><td>Revenue</td></tr>
<tr><td>Overhaul raising capacity or extending life</td><td>Capital</td></tr>
<tr><td>Interest on loan for construction until ready</td><td>Capital (AS 16); after that, revenue</td></tr>
<tr><td>Preliminary expenses (company formation)</td><td>Now expensed when incurred (AS 26). Can be written off against Securities Premium (Sec 52).</td></tr>
<tr><td>Heavy advertising for a new product</td><td>Traditionally "deferred revenue expenditure". Now expensed (AS 26 does not allow carry-forward).</td></tr>
<tr><td>Development of software / patent registration</td><td>Capital if AS 26 criteria are met</td></tr></table>

<h3>5. Receipts</h3>
<ul><li><b>Capital receipts:</b>
<ul><li>issue of shares or debentures</li>
<li>loans raised</li>
<li>sale proceeds of fixed assets</li>
<li>insurance claim for loss of a <b>fixed asset</b></li>
<li>capital subsidy</li></ul></li>
<li><b>Revenue receipts:</b>
<ul><li>sales</li>
<li>interest, dividend, rent and commission received</li>
<li>insurance claim for loss of <b>stock</b></li>
<li>discount received</li>
<li>bad debts recovered</li></ul></li>
<li><b>Profit on sale of a fixed asset</b> is a capital profit. In practice it is shown in P&amp;L as other income, but it is not sales.</li></ul>

<h3>6. Why the distinction matters</h3>
<ul><li>If capital expenditure is treated as revenue: profit understated, assets understated (secret reserve).</li>
<li>If revenue expenditure is capitalised: profit and assets overstated (window dressing).</li>
<li>Either way it is an <b>error of principle</b>, and the Trial Balance still agrees (chapter A4).</li></ul>

<div class="box trap"><b>Traps:</b>
<ul><li>"It relates to machinery, so debit Machinery": wrong if it is routine maintenance or lubricants.</li>
<li>Major statutory inspection with no new part → can still be capitalised (AS 10).</li>
<li>Installation wages paid to own employees → capital, not Wages A/c.</li>
<li>Refundable GST is not part of cost; non-refundable duties are.</li>
<li>Training staff on a new machine → revenue.</li></ul></div>
''')

Q('A7', """Neptune Cements Ltd. buys a kiln. Related costs: freight to site, installation, a 3-day trial run (output sold for ₹50,000), staff training on the kiln, and routine maintenance in the first month. Which costs are capitalised under AS 10?""",
  "Freight, installation and the trial-run cost net of ₹50,000 sale proceeds",
  ["Freight, installation, trial run, staff training and maintenance", "Freight and installation only; trial-run cost is always expensed",
   "Only the invoice price of the kiln"],
  "Directly attributable costs (delivery, installation, testing less net proceeds of test output) are capitalised. Staff training and routine maintenance are expensed.")

Q('A7', """Nova Petrochem spends ₹2.80 crore on a statutory major inspection of its turbine, done every 5 years. No part is replaced, but the turbine cannot legally run without it. The Accounts Manager wants to expense it because 'no new asset is bought'. Which treatment is right under AS 10?""",
  "Capitalise the inspection cost as a component if recognition criteria are met, and derecognise any remaining cost of the previous inspection",
  ["Expense it fully in the current year as a repair, because no new part has been installed", "Show it as deferred revenue expenditure and write it off equally over the next 5 years",
   "Debit it directly to General Reserve because it is not a normal operating expense of the year"],
  "AS 10 treats a major inspection that is a condition for continued operation as a component of the asset, capitalised when performed, with the remaining carrying amount of the previous inspection derecognised.")

Q('A7', """An amount of ₹5,000 is spent on replacing a small worn-out part of a machine in use, so that the machine keeps working at its existing capacity. This is:""",
  "Revenue expenditure", ["Capital expenditure", "Deferred revenue expenditure", "Capital loss"],
  "Replacing a small part only maintains the asset's existing condition; it neither increases capacity nor extends life. So it is charged to P&L as repairs.")

Q('A7', """Which of the following is a capital expenditure?""",
  "Wages paid to the company's own workers for installing a new machine",
  ["Wages paid to factory workers for producing goods for sale", "Carriage paid on goods purchased for resale to customers", "Annual white-washing and painting of the factory building"],
  "Installation wages are a directly attributable cost of bringing the machine into working condition, so they are added to its cost.")

Q('A7', """A firm buys a second-hand truck for ₹6 lakh and spends ₹80,000 on overhauling the engine before putting it on the road. Six months later it spends ₹12,000 on routine servicing. Correct treatment?""",
  "₹80,000 capitalised; ₹12,000 expensed", ["Both capitalised", "Both expensed", "₹80,000 expensed; ₹12,000 capitalised"],
  "Repairs needed to make a second-hand asset usable at the time of purchase are part of its cost. Routine servicing after it is in use is revenue expenditure.")

Q('A7', """Which of the following is a revenue receipt?""",
  "Insurance claim received for stock destroyed by fire", ["Sale proceeds of old machinery", "Loan received from a bank",
   "Insurance claim received for a building destroyed by fire"],
  "A claim for stock replaces revenue-type assets, so it is a revenue receipt (shown in P&L). Proceeds from fixed assets, loans and claims on fixed assets are capital receipts.")

Q('A7', """A company capitalised ₹10 lakh of routine maintenance on its plant. Effect if not corrected?""",
  "Profit and fixed assets are both overstated by ₹10 lakh (less any depreciation on it), and the Trial Balance agrees",
  ["Profit understated and assets overstated by ₹10 lakh, and the Trial Balance will disagree", "No effect on profit, since the money was spent anyway and only its classification differs",
   "Profit overstated by ₹10 lakh, and the Trial Balance will disagree by the same amount"],
  "Treating revenue expenditure as capital is an error of principle: expenses fall (profit up) and the asset rises. Both sides were posted, so the TB agrees.")

Q('A7', """Under AS 10, which of these is NOT included in the cost of an item of PPE?""",
  "Cost of advertising the new product the machine will make", ["Import duty that cannot be refunded",
   "Initial estimate of the cost of dismantling the asset at the end of its life", "Professional fees of the engineer who designed the installation"],
  "Costs of introducing a new product or service, including advertising and promotion, are excluded. Non-refundable duties, decommissioning estimates and directly attributable professional fees are included.")

Q('A7', """GST of ₹1.8 lakh is paid on purchase of a machine of ₹10 lakh, and full input tax credit is available. Freight is ₹20,000. At what amount is the machine capitalised?""",
  "₹10,20,000", ["₹11,80,000", "₹12,00,000", "₹10,00,000"],
  "Refundable or creditable taxes (GST with ITC) are excluded from cost. Freight is included. Cost = 10,00,000 + 20,000 = ₹10,20,000.")

Q('A7', """Consider the following:
1. Heavy advertising for launching a new product can be carried forward as deferred revenue expenditure under current accounting standards.
2. Interest on a loan taken to construct a factory, for the construction period, is capital expenditure.
3. Profit on sale of an old machine is a capital profit.
4. Replacement of a major component that extends the asset's life is capital expenditure.
Which are correct?""",
  "2, 3 and 4 only", ["1, 2, 3 and 4", "1 and 4 only", "2 and 3 only"],
  "AS 26 requires advertising and promotion costs to be expensed when incurred, so they can't be carried forward (1 wrong). Borrowing cost on a qualifying asset during construction is capitalised (AS 16), profit on sale of a fixed asset is a capital profit, and replacing a major component that extends life is capitalised.")
