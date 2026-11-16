from qb import note, Q

note('A1', r'''
<p class="small">Syllabus: Accounting Standards in India, Ind AS, IFRS, US GAAP, GAAP vs IFRS, transfer pricing. <b>Asked: 4–6 questions every session</b> (highest in Module A). Old papers asked "AS 18 relates to…". The May 2026 paper instead gave a <b>business situation</b> and asked which treatment the standard requires (AS 3, 4, 7, 10, 12, 18, 22, 26, Ind AS 116). Learn each standard as a <b>rule + its exceptions</b>.</p>

<h3>1. Who makes the standards</h3>
<ul>
<li><b>ICAI's Accounting Standards Board (ASB)</b> formulates standards. The Central Government <b>notifies</b> them under the Companies Act 2013 (Sec 133) after advice from <b>NFRA</b> (National Financial Reporting Authority, which replaced NACAS).</li>
<li>Two sets exist side by side:
<ul><li><b>AS</b> (Companies (Accounting Standards) Rules 2021) for companies not on Ind AS.</li>
<li><b>Ind AS</b> (Companies (Indian Accounting Standards) Rules 2015) converged with IFRS.</li></ul></li>
<li><b>Ind AS road map</b>:
<ul><li>Phase I: FY 2016-17, listed or unlisted companies with net worth ≥ ₹500 crore.</li>
<li>Phase II: FY 2017-18, all listed companies, and unlisted companies with net worth ≥ ₹250 crore.</li>
<li>Holding, subsidiary, JV and associate companies of these follow too.</li>
<li>NBFCs: net worth ≥ ₹500 crore from 2018-19; others ≥ ₹250 crore from 2019-20.</li>
<li><b>Banks:</b> RBI has deferred Ind AS for scheduled commercial banks <b>until further notice</b>, so banks still follow AS plus RBI norms.</li></ul></li>
<li>Once a company follows Ind AS it <b>cannot switch back</b> to AS.</li>
<li><b>IFRS</b> are issued by the IASB, London. <b>US GAAP</b> is issued by FASB.</li>
</ul>

<h3>2. IFRS vs US GAAP (asked as statements)</h3>
<table><tr><th>Point</th><th>IFRS / Ind AS</th><th>US GAAP</th></tr>
<tr><td>Approach</td><td><b>Principles-based</b></td><td><b>Rules-based</b> (detailed guidance)</td></tr>
<tr><td>LIFO for inventory</td><td>Prohibited</td><td>Permitted</td></tr>
<tr><td>Revaluation of PPE</td><td>Allowed (revaluation model)</td><td>Not allowed (cost only)</td></tr>
<tr><td>Development cost</td><td>Capitalised if criteria met</td><td>Generally expensed</td></tr>
<tr><td>Reversal of impairment</td><td>Allowed (not for goodwill)</td><td>Not allowed</td></tr>
<tr><td>Extraordinary items</td><td>Prohibited</td><td>Also eliminated (since 2015)</td></tr></table>
<div class="box key"><b>Indian AS 2</b> also prohibits LIFO. The allowed cost formulas are FIFO, weighted average, and specific identification (for items not ordinarily interchangeable).</div>

<h3>3. The standards — number, name, and the rule examiners test</h3>
<table><tr><th>AS</th><th>Subject</th><th>The point that gets tested</th></tr>
<tr><td>1</td><td>Disclosure of Accounting Policies</td><td>Fundamental assumptions: <b>going concern, consistency, accrual</b>. If followed, no disclosure is needed. If not followed, disclose. Policy selection: prudence, substance over form, materiality.</td></tr>
<tr><td>2</td><td>Valuation of Inventories</td><td>Lower of <b>cost and NRV</b>, item by item.
<ul><li>Cost excludes: abnormal waste, storage (unless needed in production), admin overheads, selling costs.</li>
<li>Not covered by AS 2: WIP under construction contracts (AS 7), financial instruments, livestock/agri/forest produce and mineral ores held at NRV by trade practice.</li></ul></td></tr>
<tr><td>3</td><td>Cash Flow Statements</td><td>Operating / Investing / Financing classification. See chapter B4.</td></tr>
<tr><td>4</td><td>Events after the Balance Sheet Date</td><td><b>Adjusting</b> events give evidence of conditions that existed at BS date → adjust. <b>Non-adjusting</b> events → disclose only. A proposed dividend declared after BS date is <b>not</b> a liability, only disclosed. If going concern fails after BS date, the whole basis changes.</td></tr>
<tr><td>5</td><td>Net Profit, Prior Period Items, Change in Policies</td><td><b>Prior period items</b> (errors/omissions of earlier years found now) → shown separately in current P&amp;L. <b>Change in estimate</b> (useful life, residual value) → <b>prospective</b>. <b>Change in policy</b> only if required by statute or AS, or for better presentation.</td></tr>
<tr><td>7</td><td>Construction Contracts</td><td><b>Percentage of completion</b> when outcome is reliable. <b>Expected loss is recognised immediately</b>. If the outcome is not reliable, recognise revenue only up to recoverable cost.</td></tr>
<tr><td>9</td><td>Revenue Recognition</td><td>Goods: when <b>significant risks and rewards</b> are transferred and there is no significant uncertainty. Interest: time basis. Royalty: accrual. Dividend: when the right to receive is established.</td></tr>
<tr><td>10</td><td>Property, Plant &amp; Equipment</td><td>Cost and capitalisation rules, component approach, major inspection. See chapter A7. (AS 6 Depreciation was merged into AS 10.)</td></tr>
<tr><td>11</td><td>Changes in Foreign Exchange Rates</td><td>Monetary items at <b>closing rate</b>. Exchange difference goes to P&amp;L. Non-monetary items at historical rate.</td></tr>
<tr><td>12</td><td>Government Grants</td><td>See section 4.</td></tr>
<tr><td>13</td><td>Investments</td><td><b>Current</b>: lower of cost and fair value. <b>Long-term</b>: cost less <b>permanent</b> decline.</td></tr>
<tr><td>14</td><td>Amalgamations</td><td>Pooling of interests (merger) vs purchase method.</td></tr>
<tr><td>15</td><td>Employee Benefits</td><td>Short-term, post-employment (defined contribution vs defined benefit), termination benefits.</td></tr>
<tr><td>16</td><td>Borrowing Costs</td><td>Capitalise for a <b>qualifying asset</b> (one that takes a substantial period, normally 12 months or more, to get ready). <b>Suspend</b> capitalisation during extended interruption. <b>Stop</b> when the asset is substantially ready.</td></tr>
<tr><td>17</td><td>Segment Reporting</td><td>Business and geographical segments; 10% thresholds.</td></tr>
<tr><td>18</td><td>Related Party Disclosures</td><td>See section 5.</td></tr>
<tr><td>19</td><td>Leases</td><td>Finance vs operating lease by substance (risks and rewards). Does <b>not</b> cover land leases or natural-resource leases. Ind AS 116 replaced the distinction for lessees. See chapter C8.</td></tr>
<tr><td>20</td><td>Earnings Per Share</td><td>Basic and diluted EPS. A bonus issue is adjusted <b>retrospectively</b>. See chapter B3.</td></tr>
<tr><td>21</td><td>Consolidated Financial Statements</td><td>Parent + subsidiaries.</td></tr>
<tr><td>22</td><td>Taxes on Income</td><td>Deferred tax on <b>timing</b> differences only, not permanent ones. See chapter B3.</td></tr>
<tr><td>23 / 27</td><td>Associates in CFS / Joint Ventures</td><td>Equity method / proportionate consolidation.</td></tr>
<tr><td>24</td><td>Discontinuing Operations</td><td>Disclosure from the initial disclosure event.</td></tr>
<tr><td>25</td><td>Interim Financial Reporting</td><td>Each interim period is part of the annual period.</td></tr>
<tr><td>26</td><td>Intangible Assets</td><td>See section 6.</td></tr>
<tr><td>28</td><td>Impairment of Assets</td><td>Impairment loss = carrying amount − <b>recoverable amount</b>, where recoverable amount is the <b>higher</b> of net selling price and value in use.</td></tr>
<tr><td>29</td><td>Provisions, Contingent Liabilities &amp; Assets</td><td><b>Provision</b>: present obligation from a past event + probable outflow + reliable estimate. <b>Contingent liability</b>: disclose. <b>Contingent asset</b>: neither recognised nor disclosed in the financial statements.</td></tr></table>
<p class="small">Withdrawn numbers: AS 6 (merged into AS 10), AS 8 (into AS 26), AS 30–32. A question like "AS 6 deals with…" is a trap.</p>

<h3>4. AS 12 Government Grants — the four cases</h3>
<table><tr><th>Grant type</th><th>Treatment</th></tr>
<tr><td>Related to a <b>specific depreciable asset</b></td><td>Either <b>deduct</b> from the asset's cost (depreciation is then on the net amount), or treat as <b>deferred income</b> and release to P&amp;L over useful life in proportion to depreciation.</td></tr>
<tr><td>Related to a <b>non-depreciable</b> asset (e.g. land), no obligation</td><td>Credit to <b>capital reserve</b>. If conditions require obligations, release to income over the period of those costs.</td></tr>
<tr><td><b>Promoters' contribution</b> type (e.g. based on total investment, no repayment)</td><td><b>Capital reserve</b>, as part of shareholders' funds.</td></tr>
<tr><td><b>Revenue</b> grant (to meet costs)</td><td>P&amp;L, either as income or deducted from the related expense, matched with the cost.</td></tr></table>
<ul><li>Recognise a grant only when there is <b>reasonable assurance</b> that the conditions will be met and the grant will be received. Receiving cash alone is not the test.</li>
<li><b>Refund</b> of a grant is shown as an <b>extraordinary item</b>.</li>
<li>Grant in the form of a non-monetary asset given free: record at <b>nominal value</b>. If given at concessional rate: at acquisition cost.</li></ul>

<h3>5. AS 18 Related Parties</h3>
<ul>
<li><b>Related</b> means one party can <b>control</b> or exercise <b>significant influence</b> over the other. Significant influence is participation in financial and operating policy, not control. Shareholding of 20% or more is presumed significant influence.</li>
<li><b>Covered:</b>
<ul><li>holding, subsidiary and fellow-subsidiary companies</li>
<li>associates and joint ventures</li>
<li>individuals with voting power giving control or significant influence, and their relatives</li>
<li><b>Key Management Personnel (KMP)</b> and their relatives</li>
<li>enterprises over which any of these have significant influence (e.g. a firm in which a director is a partner)</li></ul></li>
<li><b>NOT related merely because of:</b>
<ul><li>two companies having a <b>common director</b></li>
<li>providers of finance, trade unions, public utilities, government departments in normal dealings</li>
<li>a single customer, supplier or agent with whom there is a large volume of business</li></ul></li>
<li>Disclose even if <b>no price is charged</b> (e.g. an interest-free loan to the MD). The test is the relationship, not cash or profit.</li>
<li><b>Exemptions:</b>
<ul><li>intra-group transactions eliminated in consolidated statements</li>
<li>a state-controlled enterprise's transactions with other state-controlled enterprises</li>
<li>where disclosure would conflict with a <b>duty of confidentiality</b> (e.g. a bank's duty to customers)</li></ul></li>
</ul>

<h3>6. AS 26 Intangible Assets</h3>
<ul>
<li>Intangible asset: identifiable, non-monetary, without physical substance, controlled, and expected to give future benefits.</li>
<li><b>Research phase</b> → always <b>expense</b>.</li>
<li><b>Development phase</b> → capitalise only if <b>all six</b> are shown:
<ol><li>technical feasibility</li>
<li>intention to complete</li>
<li>ability to use or sell</li>
<li>how it will generate future benefits (a market exists)</li>
<li>adequate resources</li>
<li>cost can be measured reliably</li></ol></li>
<li>If research and development can't be separated, treat everything as research.</li>
<li><b>Never recognised</b> as an asset: internally generated goodwill, brands, mastheads, publishing titles and customer lists.</li>
<li><b>Always expensed:</b> start-up costs, training, advertising and promotion, relocation.</li>
<li>Patent <b>registration fees</b> directly attributable to an asset are capitalised.</li>
<li>Amortisation: rebuttable presumption that useful life is <b>not more than 10 years</b> from the date the asset is available for use. Residual value is presumed nil.</li>
</ul>

<h3>7. Transfer pricing</h3>
<ul>
<li>Price charged between <b>associated enterprises</b> (e.g. an Indian subsidiary buying from its foreign parent).</li>
<li>Tax law requires the <b>Arm's Length Price (ALP)</b>: the price unrelated parties would charge. Without this rule, groups would shift profit to low-tax countries by over- or under-pricing.</li>
<li>Income-tax Act 1961, <b>Sections 92–92F</b>. Covers international transactions and specified domestic transactions.</li>
<li><b>Methods (Rule 10B):</b>
<ul><li>Comparable Uncontrolled Price (CUP)</li>
<li>Resale Price Method</li>
<li>Cost Plus Method</li>
<li>Profit Split Method</li>
<li>Transactional Net Margin Method (TNMM)</li>
<li>any other method</li></ul></li>
<li>An accountant's report is required in Form 3CEB.</li>
<li>Transfer pricing <b>cannot</b> be set freely by "group policy". The Transfer Pricing Officer can adjust income up to ALP.</li>
</ul>

<div class="box trap"><b>Traps:</b>
<ul>
<li>"Cash received, so take the grant to income": wrong. Grants follow AS 12 matching, not receipt.</li>
<li>Change in useful life or residual value = change in <b>estimate</b> → prospective (AS 5). It is not a prior-period item and is not restated.</li>
<li>A customer becoming insolvent after the BS date, from difficulties that existed before → <b>adjusting</b>. A fire after the BS date → <b>non-adjusting</b> (disclose if material).</li>
<li>AS 7: recognise a foreseeable loss on the whole contract at once, even if work is only 10% done.</li>
<li>AS 26: advertising before launch is never an intangible. Development after feasibility can be.</li>
<li>Common director alone ≠ related party. A firm in which a director is a partner = related party.</li>
<li>Contingent <b>asset</b> is not disclosed in the financial statements. Contingent <b>liability</b> is disclosed unless the outflow is remote.</li>
</ul></div>
''')

# ---------------- questions ----------------
Q('A1', """Sun Ltd. finalises its accounts for the year ended 31 March 2026; the Board approves them on 20 May 2026. Between these dates:
1. A debtor owing ₹80 lakh at 31 March is declared insolvent on 15 April; its business had been failing since January.
2. Floods on 10 April destroy stock worth ₹1.2 crore.
3. The Board recommends a final dividend on 20 May.
4. A court case pending on 31 March is decided against the company on 5 May, fixing the damages.
Under AS 4, which events require ADJUSTMENT of the 2025-26 accounts?""",
  "1 and 4 only", ["1, 2 and 4 only", "1, 3 and 4 only", "4 only"],
  "Adjusting events give more evidence about conditions that existed at the balance sheet date: the debtor's failing business (1) and the lawsuit already pending (4). The flood (2) is a new condition after the date: disclose if material, don't adjust. A dividend proposed after the date is not a liability at the balance sheet date; it is only disclosed (3).")

Q('A1', """A company changes the estimated useful life of its machines from 10 to 6 years on the basis of a technical report. The Accounts Manager wants to recompute depreciation of the past 4 years and show the shortfall as a prior period item. Which is correct under AS 5?""",
  "The revision is a change in accounting estimate and is applied prospectively over the remaining revised life",
  ["The shortfall is a prior period item and must be shown separately in the current Profit and Loss Account",
   "The revision is a change in accounting policy and must be applied retrospectively with restatement",
   "The shortfall must be adjusted directly against General Reserve without passing through Profit and Loss"],
  "Useful life and residual value are estimates. Revising them is a change in accounting estimate: the effect goes to the current and future periods (prospective). Prior period items arise only from errors or omissions in earlier years' accounts, which is not the case here.")

Q('A1', """Which of the following correctly lists the situations in which AS 5 permits a change in accounting policy?""",
  "When required by statute, by an accounting standard, or when it results in a more appropriate presentation of financial statements",
  ["Whenever the Board considers that profit for the year will improve, provided the change is disclosed in the notes",
   "Only when the statutory auditor certifies that the existing policy has become inconsistent with income-tax law",
   "When required by statute only; accounting standards and better presentation are not valid grounds for a change"],
  "AS 5 allows a change in accounting policy only if (a) a statute requires it, (b) an accounting standard requires it, or (c) it gives a more appropriate presentation. Improving profit is never a ground. The impact of a material change must be disclosed.")

Q('A1', """Build-Right Ltd. has a fixed-price contract: price ₹200 crore, total estimated cost ₹160 crore, cost incurred till year-end ₹48 crore. The outcome can be estimated reliably and stage of completion is measured by cost incurred. What contract revenue and profit should be recognised for the year under AS 7?""",
  "Revenue ₹60 crore and profit ₹12 crore",
  ["Revenue ₹48 crore and profit nil until completion", "Revenue ₹60 crore and profit ₹40 crore", "Revenue ₹200 crore and profit ₹40 crore"],
  "Stage of completion = 48/160 = 30%. Revenue = 30% × 200 = ₹60 crore; cost = ₹48 crore; profit = ₹12 crore (= 30% of total expected profit of ₹40 crore). Waiting for completion is the old completed-contract method, which AS 7 does not allow when the outcome is reliable.")

Q('A1', """In the same type of contract, estimated total cost is revised to ₹215 crore against a contract price of ₹200 crore when the work is only 20% complete. What does AS 7 require?""",
  "The entire expected loss of ₹15 crore is recognised as an expense immediately",
  ["Only 20% of the expected loss, i.e. ₹3 crore, is recognised this year",
   "No loss is recognised until the contract is completed and the final bill is raised",
   "The expected loss is shown as a contingent liability in the notes"],
  "When it is probable that total contract costs will exceed total contract revenue, AS 7 requires the expected loss to be recognised as an expense immediately, whatever the stage of completion. This follows prudence.")

Q('A1', """GreenTech Ltd. receives three grants during 2025-26:
1. ₹2 crore towards the cost of an effluent-treatment plant (life 10 years).
2. ₹50 lakh towards the cost of land for the plant, with no further conditions.
3. A State subsidy of ₹5 crore computed as 15% of total investment, not linked to any asset and not repayable.
Which treatment under AS 12 is correct?""",
  "1: deduct from asset cost or treat as deferred income; 2: capital reserve; 3: capital reserve (promoters' contribution type)",
  ["1: credit to P&L in the year received; 2: deduct from land; 3: other income",
   "1: capital reserve; 2: deferred income over 10 years; 3: deduct from plant cost",
   "All three are credited to Capital Reserve because they are capital receipts"],
  "Grants related to a depreciable asset: deduct from cost or show as deferred income over the asset's life. Grants for non-depreciable assets like land with no obligations: capital reserve. Grants in the nature of promoters' contribution (linked to total investment, not to a specific asset): capital reserve, as part of shareholders' funds.")

Q('A1', """Under AS 12, a company receives an asset free of cost from the Government as a grant. At what value is it recorded?""",
  "At a nominal value", ["At its fair market value with credit to P&L", "At replacement cost with credit to Capital Reserve", "It is not recorded at all as no cost is incurred"],
  "AS 12 requires a non-monetary asset given free of cost to be recorded at a nominal value (e.g. ₹1). Assets given at a concessional rate are recorded at acquisition cost.")

Q('A1', """A grant related to a depreciable asset becomes refundable because the company broke a condition. Under AS 12, how is the refund shown in the Profit and Loss Account?""",
  "As an extraordinary item", ["As a prior period item", "As a change in accounting estimate", "As a normal operating expense under 'Other expenses'"],
  "AS 12 states that a government grant that becomes refundable is treated as an extraordinary item.")

Q('A1', """Pharma Ltd. spends on a new drug:
1. Laboratory research to discover new compounds – ₹4 crore
2. Pilot plant work after technical feasibility is established, with resources and a market identified – ₹6 crore
3. Fees for registering the patent – ₹20 lakh
4. Advertising in medical journals before launch – ₹1 crore
5. Training the sales force – ₹40 lakh
How much can be recognised as an intangible asset under AS 26?""",
  "₹6.20 crore", ["₹10.20 crore", "₹6 crore", "₹11.60 crore"],
  "Research (₹4 crore) is always expensed. Development meeting all recognition criteria (₹6 crore) plus directly attributable patent registration fees (₹0.20 crore) are capitalised. Advertising and staff training are always expensed under AS 26. Total = ₹6.20 crore.")

Q('A1', """Consider these statements on AS 26:
1. Internally generated brands and customer lists can be capitalised if their value can be measured by a valuer.
2. If the research phase cannot be separated from the development phase, the whole expenditure is treated as research.
3. There is a rebuttable presumption that the useful life of an intangible asset does not exceed 10 years from the date it is available for use.
4. Expenditure on an intangible item that was once expensed can later be reinstated as an asset.
Which are correct?""",
  "2 and 3 only", ["1, 2 and 3 only", "2, 3 and 4 only", "1 and 4 only"],
  "Internally generated brands, mastheads, publishing titles and customer lists are never recognised (1 wrong). If phases can't be separated, all of it is research (2 correct). The 10-year rebuttable presumption applies (3 correct). Once expensed, an item cannot later be capitalised (4 wrong).")

Q('A1', """Which of the following is NOT a related party relationship requiring disclosure under AS 18?""",
  "Two companies that have one director in common, with no other link",
  ["A partnership firm in which the company's Managing Director is a partner",
   "A fellow subsidiary of the same holding company",
   "A relative of a Key Management Person who supplies goods to the company"],
  "AS 18 specifically states that two companies are not related merely because they have a director in common. A firm in which KMP has significant influence, fellow subsidiaries and relatives of KMP are related parties.")

Q('A1', """A bank gives an interest-free loan to its whole-time director's son and also lends to many customers. Regarding AS 18 disclosure, which statement is correct?""",
  "Related-party transactions are disclosed even if no price is charged, but the bank need not disclose details that would breach its duty of confidentiality to ordinary customers",
  ["No disclosure is needed because no interest income arose from the loan, so no transaction value exists to report",
   "Only transactions resulting in profit or loss to the bank are disclosed, and interest-free loans are therefore excluded",
   "Every loan to every customer must be disclosed individually, because a bank owes a duty of transparency to the public"],
  "AS 18 requires disclosure of related-party transactions whether or not a price is charged. It also exempts disclosures that would conflict with a statutory duty of confidentiality, which is relevant for banks' dealings with customers.")

Q('A1', """Under AS 2, which of these costs is INCLUDED in the cost of inventories of a manufacturer?""",
  "Fixed production overheads allocated on the basis of normal capacity",
  ["Abnormal wastage of materials due to a fire in the store", "Selling and distribution costs of finished goods",
   "Administrative overheads of the head office not related to production"],
  "AS 2 includes costs of purchase, costs of conversion (direct labour and systematically allocated fixed and variable production overheads, on normal capacity) and other costs to bring inventory to its present location and condition. Abnormal wastage, selling costs and unrelated admin overheads are excluded and expensed.")

Q('A1', """A trader holds an item of stock: cost ₹1,20,000; expected selling price ₹1,30,000; estimated selling expenses ₹16,000; replacement cost ₹1,10,000. At what value should it appear in the Balance Sheet under AS 2?""",
  "₹1,14,000", ["₹1,10,000", "₹1,20,000", "₹1,30,000"],
  "Inventory is valued at the lower of cost and net realisable value. NRV = selling price − costs to sell = 1,30,000 − 16,000 = 1,14,000. Lower of 1,20,000 and 1,14,000 = ₹1,14,000. Replacement cost is not the test for finished goods.")

Q('A1', """Which statement about AS 2 is NOT correct?""",
  "LIFO may be used if it is applied consistently from year to year",
  ["Specific identification is used for items that are not ordinarily interchangeable",
   "Work-in-progress under construction contracts is outside the scope of AS 2",
   "Inventory is written down to NRV on an item-by-item basis in normal cases"],
  "AS 2 allows FIFO or weighted average (and specific identification where items aren't interchangeable). LIFO is not permitted, even if applied consistently. Construction WIP is covered by AS 7.")

Q('A1', """Alpha Ltd. holds shares of Beta Ltd. bought as a long-term investment for ₹10 crore. Their market value fell to ₹9.6 crore due to a temporary market fall. Under AS 13, at what value are they shown?""",
  "₹10 crore, because only a permanent decline is provided for in long-term investments",
  ["₹9.6 crore, because investments are always shown at market value", "₹9.6 crore, with ₹0.4 crore credited to revaluation reserve",
   "₹9.8 crore, being the average of cost and market value"],
  "Long-term investments are carried at cost; provision is made only for a decline that is other than temporary. Current investments are carried at the lower of cost and fair value.")

Q('A1', """A company borrows specifically to build a factory that will take 18 months to construct. Construction is halted for 3 months because of a labour strike. Under AS 16:""",
  "Borrowing cost for the strike period is expensed because capitalisation is suspended during an extended interruption",
  ["All borrowing costs till the factory is ready are capitalised, including the strike period",
   "No borrowing cost can be capitalised as the factory is not a qualifying asset",
   "Borrowing cost is capitalised only after the factory starts commercial production"],
  "A factory taking 18 months is a qualifying asset, so borrowing costs are capitalised. Capitalisation is suspended during extended periods when active development is interrupted (like a strike) and stops when the asset is substantially ready for use.")

Q('A1', """Under AS 28, an asset has carrying amount ₹50 lakh, net selling price ₹38 lakh and value in use ₹44 lakh. What is the impairment loss?""",
  "₹6 lakh", ["₹12 lakh", "₹9 lakh", "Nil, because value in use is positive"],
  "Recoverable amount = higher of net selling price (38) and value in use (44) = ₹44 lakh. Impairment loss = 50 − 44 = ₹6 lakh.")

Q('A1', """Consider the following under AS 29:
1. A provision is recognised when there is a present obligation from a past event, an outflow is probable and a reliable estimate can be made.
2. A contingent liability is disclosed in the notes unless the possibility of outflow is remote.
3. A contingent asset is recognised when its realisation is probable.
4. A contingent asset is ordinarily disclosed in the notes to accounts.
Which are correct?""",
  "1 and 2 only", ["1, 2 and 3 only", "1, 2 and 4 only", "2 and 4 only"],
  "AS 29: a provision needs all three conditions (1). Contingent liabilities are disclosed unless remote (2). A contingent asset is neither recognised nor disclosed in the financial statements; it is recognised only when realisation is virtually certain, and then it is no longer contingent (3 and 4 wrong).")

Q('A1', """An Indian subsidiary buys components from its UK parent at prices well above those charged to unrelated buyers, reducing Indian taxable profit. The tax officer adjusts income. Which concept and law apply?""",
  "Arm's Length Price under the transfer pricing provisions (Sections 92–92F) of the Income-tax Act",
  ["Fair value under Ind AS 113, applied by the Companies Act", "Customs valuation, which automatically decides income-tax value",
   "Group transfer price, which is binding because it follows internal group policy"],
  "Transactions between associated enterprises must be at arm's length price. Methods include CUP, resale price, cost plus, profit split and TNMM. A group's internal pricing policy does not bind the tax authorities.")

Q('A1', """Which statement about the Indian accounting framework is correct?""",
  "Scheduled commercial banks still follow AS with RBI norms because RBI has deferred Ind AS for them until further notice",
  ["All listed companies and all scheduled commercial banks moved to Ind AS together from 1 April 2016",
   "A company that adopts Ind AS voluntarily may revert to the old AS after three years with Board approval",
   "Ind AS are notified by RBI under the Banking Regulation Act and apply first to banks and NBFCs"],
  "Ind AS applied to companies in phases from 2016-17 (net worth ≥ ₹500 crore, then all listed and ≥ ₹250 crore). RBI deferred Ind AS for scheduled commercial banks until further notice. Once Ind AS is adopted, a company cannot revert. Ind AS are notified by the Central Government under the Companies Act.")

Q('A1', """Which TWO features distinguish IFRS from US GAAP?
1. IFRS is principles-based; US GAAP is more rules-based.
2. IFRS permits LIFO; US GAAP prohibits it.
3. IFRS permits revaluation of property, plant and equipment; US GAAP does not.
4. Both prohibit reversal of impairment losses on all assets.""",
  "1 and 3", ["1 and 2", "2 and 4", "3 and 4"],
  "IFRS is principles-based and allows PPE revaluation; US GAAP is rules-based and cost-only for PPE. It is US GAAP that permits LIFO (IFRS prohibits it). IFRS allows reversal of impairment (except goodwill); US GAAP does not.")

Q('A1', """Under AS 9, when is revenue from a sale of goods recognised?""",
  "When the seller has transferred the significant risks and rewards of ownership and no significant uncertainty exists about collection",
  ["When the goods are physically dispatched from the seller's warehouse, whatever the terms",
   "When the buyer pays the price in full", "When the sale invoice is raised, even if goods are sent on approval"],
  "AS 9 links revenue to transfer of significant risks and rewards with no significant uncertainty about consideration. Goods sent on approval are not sold until the buyer approves or the time for rejection lapses. Cash receipt alone does not decide it.")

Q('A1', """Under AS 11, a company has a foreign-currency trade payable of USD 10,000 recorded at ₹83 when the goods were bought. At year-end the rate is ₹85 and it is still unpaid. What is the treatment?""",
  "Restate the payable at ₹8,50,000 and charge the ₹20,000 exchange loss to the Profit and Loss Account",
  ["Keep the payable at ₹8,30,000 until it is paid, since it arose from a historical transaction",
   "Restate the payable at ₹8,50,000 and add the ₹20,000 loss to the cost of the goods purchased",
   "Restate the payable at ₹8,50,000 and debit the ₹20,000 exchange loss to Capital Reserve"],
  "A trade payable is a monetary item. AS 11 requires monetary items to be reported at the closing rate, with exchange differences recognised in P&L of the period.")
