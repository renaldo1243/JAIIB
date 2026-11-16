from qb import note, Q

note('B4', r'''
<p class="small">Syllabus: Cash flow statement; fund flow statement; analysis. <b>Asked: 1–3 cash-flow questions per session. The fund flow statement has had zero questions in six sessions, so it is left out.</b> May 2026 asked:</p>
<ul class="small"><li>sale of machinery → investing</li>
<li>classify five flows</li>
<li>indirect-method adjustments</li>
<li>classify five inflows</li>
<li>disclosure of components of cash equivalents</li>
<li>which companies must prepare a cash flow statement</li></ul>

<h3>1. AS 3 / Ind AS 7 — the three activities</h3>
<table><tr><th>Activity</th><th>Examples (non-financial company)</th></tr>
<tr><td><b>Operating</b>: principal revenue-producing activities</td><td>
<ul><li>Cash from customers</li>
<li>Payments to suppliers and employees</li>
<li><b>Income tax paid</b> (unless specifically identifiable with investing or financing)</li>
<li>Royalties and commissions</li></ul></td></tr>
<tr><td><b>Investing</b>: buying and selling long-term assets and investments</td><td>
<ul><li>Purchase or <b>sale of machinery</b>, land, investments</li>
<li>Loans given to others</li>
<li><b>Interest and dividend received</b></li></ul></td></tr>
<tr><td><b>Financing</b>: changes in owners' capital and borrowings</td><td>
<ul><li>Issue of shares or debentures</li>
<li>Borrowing and repayment of loans</li>
<li><b>Interest paid, dividend paid</b></li>
<li>Buy-back</li></ul></td></tr></table>
<div class="box key">For a <b>financial enterprise (bank, NBFC)</b>, interest paid, interest received and dividends received are <b>operating</b> activities, because lending and borrowing are its main business.</div>
<ul><li>Classification follows the <b>nature</b> of the transaction, not the fact that it changes cash.</li>
<li><b>Non-cash transactions</b> are excluded from the statement but disclosed. Examples:
<ul><li>buying an asset by issuing shares</li>
<li>bonus issue</li>
<li>converting debentures into shares</li>
<li>acquiring an asset on a finance lease</li></ul></li>
<li><b>Cash equivalents:</b> short-term, highly liquid investments convertible into known cash with insignificant risk. Normally a maturity of <b>3 months or less from acquisition</b>.
<ul><li>Equity shares are excluded.</li>
<li>A bank overdraft repayable on demand may be part of cash and cash equivalents.</li>
<li>The <b>components</b> of cash and cash equivalents must be disclosed and <b>reconciled</b> with the balance sheet.</li></ul></li>
<li><b>Who prepares:</b> every company except a One Person Company, small company and dormant company (Sec 2(40)).</li></ul>

<h3>2. Direct vs indirect method (operating activities)</h3>
<ul><li><b>Direct:</b> gross receipts and payments (cash from customers − cash to suppliers − expenses). AS 3 encourages it.</li>
<li><b>Indirect:</b> start with <b>net profit before tax</b>, then:
<ol><li>add <b>non-cash and non-operating charges</b>: depreciation, amortisation, loss on sale of assets, interest expense (financing), provisions</li>
<li>deduct <b>non-operating income</b>: profit on sale of assets, interest and dividend received (investing)</li>
<li>adjust working capital: <b>increase in current assets → deduct</b>; decrease → add. <b>Increase in current liabilities → add</b>; decrease → deduct</li>
<li>= cash generated from operations − taxes paid = net cash from operating activities</li></ol></li></ul>
<p><b>Example:</b> NPBT ₹12 crore; depreciation ₹1.8 crore; profit on sale of machinery ₹0.75 crore; receivables up ₹1.5 crore; payables up ₹0.9 crore.
<br>Cash generated from operations = 12 + 1.8 − 0.75 − 1.5 + 0.9 = <b>₹12.45 crore</b>.</p>
<p><b>Investing example:</b> bought machinery ₹2,00,000 and sold old machine for ₹50,000 → net cash <b>used</b> in investing ₹1,50,000. Only the sale <b>proceeds</b> are investing inflow; the profit on sale is removed from operating.</p>

<h3>3. Why it matters</h3>
<ul><li>Profit ≠ cash: accruals, credit sales and capex create the gap.</li>
<li>Bankers read <b>operating cash flow</b> to judge repayment capacity.</li>
<li>Consistently negative operating cash flow with reported profits is a <b>red flag</b> (aggressive revenue recognition, rising receivables).</li></ul>

<div class="box trap"><b>Traps:</b>
<ul><li>Sale of machinery = <b>investing</b>, even though it "generated cash".</li>
<li>Interest paid = financing for a company but <b>operating for a bank</b>.</li>
<li>Indirect method: increase in debtors is <b>deducted</b>; increase in creditors is <b>added</b>.</li>
<li>Depreciation is added back because it is non-cash. It does <b>not</b> generate cash.</li>
<li>Bonus shares and assets bought for shares never appear in the cash flow statement.</li></ul></div>
''')

Q('B4', """During the year Delta Ltd. (a manufacturer) had: cash from customers, purchase of plant, sale of old machinery, dividend received on investments and issue of equity shares. A trainee puts the sale of old machinery under operating activities because it generated cash. Correct classification?""",
  "Investing activity", ["Operating activity", "Financing activity", "Extraordinary activity shown separately below financing"],
  "Purchase or sale of long-term assets is investing. Classification depends on the nature of the transaction, not merely on cash movement.")

Q('B4', """NPBT ₹12 crore; depreciation ₹1.8 crore; profit on sale of machinery ₹0.75 crore; increase in trade receivables ₹1.5 crore; increase in trade payables ₹0.9 crore. Cash generated from operations (indirect method) is:""",
  "₹12.45 crore", ["₹13.95 crore", ["₹15.45 crore"][0], "₹10.95 crore"],
  "12 + 1.8 − 0.75 − 1.5 + 0.9 = ₹12.45 crore. Depreciation added (non-cash), profit on sale removed (investing), increase in receivables deducted, increase in payables added.")

Q('B4', """For a NON-financial company, how are 'interest paid on long-term borrowings' and 'dividend received on investments' classified under AS 3?""",
  "Interest paid – financing; dividend received – investing", ["Both – operating", "Interest paid – operating; dividend received – financing",
   "Interest paid – investing; dividend received – operating"],
  "For non-financial enterprises, interest and dividends paid are financing cash flows (cost of funds); interest and dividends received are investing (returns on investments).")

Q('B4', """For a commercial BANK, interest paid on deposits and interest received on advances are classified as:""",
  "Operating activities", ["Financing and investing activities respectively", "Investing activities", "Financing activities"],
  "For financial enterprises, borrowing and lending are the main revenue-producing activities, so interest paid and received are operating cash flows.")

Q('B4', """Which of these transactions will NOT appear in the cash flow statement but should be disclosed?
1. Purchase of land by issuing equity shares to the seller.
2. Issue of bonus shares.
3. Conversion of debentures into equity shares.
4. Purchase of machinery for cash.""",
  "1, 2 and 3 only", ["4 only", "1 and 4 only", "2 and 3 only"],
  "Non-cash investing and financing transactions are excluded from the statement and disclosed elsewhere. A cash purchase of machinery is an investing outflow.")

Q('B4', """A company bought new machinery for ₹2,00,000 and sold an old machine (book value ₹40,000) for ₹50,000. The net cash flow from investing activities is:""",
  "Outflow of ₹1,50,000", ["Outflow of ₹1,60,000", "Outflow of ₹2,00,000", "Inflow of ₹50,000"],
  "Investing shows actual proceeds: −2,00,000 + 50,000 = −1,50,000. The ₹10,000 profit is deducted from operating activities under the indirect method.")

Q('B4', """Under the indirect method, which adjustment is correct?""",
  "A decrease in inventory is added to net profit", ["An increase in trade receivables is added to net profit",
   "A decrease in trade payables is added to net profit", "Profit on sale of an investment is added to net profit"],
  "Lower inventory releases cash (add). Higher receivables tie up cash (deduct), lower payables use cash (deduct), and profit on sale of investments is investing (deduct).")

Q('B4', """Which statement on cash equivalents under AS 3 is correct?""",
  "They generally mature within three months of acquisition, and their components must be disclosed",
  ["Equity shares of listed companies are treated as cash equivalents because they are liquid", "Any fixed deposit, whatever its maturity, is a cash equivalent",
   "Cash equivalents need not be reconciled with balance sheet items"],
  "Cash equivalents carry insignificant risk of change in value; equity investments are excluded. The enterprise discloses the components and reconciles them with the balance sheet.")

Q('B4', """Which companies are exempt from preparing a cash flow statement under the Companies Act, 2013?""",
  "One Person Companies, small companies and dormant companies", ["All private companies", "All unlisted companies",
   "Companies whose turnover is below ₹500 crore"],
  "Sec 2(40) proviso: the financial statements of an OPC, a small company and a dormant company may exclude the cash flow statement.")
