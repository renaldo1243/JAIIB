from qb import note, Q

note('C9', r'''
<p class="small">Syllabus: Working capital cycle, cash and marketable securities, accruals, trade credit, bank finance (methods, cash budget), regulation of bank finance, CP, factoring and forfaiting. <b>Asked: 1 question on the WC cycle and 1 on sources every session.</b> May 2026 asked: "when is WC requirement higher", internal sources of finance, liquidity ratios banks use, CP. Public deposits, ICDs and rights debentures are left out (not asked).</p>

<h3>1. Concepts</h3>
<ul><li><b>Gross working capital</b> = total current assets.<br><b>Net working capital</b> = CA − CL. It is the part of current assets financed by long-term funds (the margin).</li>
<li><b>Permanent (core) WC:</b> the minimum always needed, so finance it long-term.<br><b>Temporary (fluctuating) WC:</b> seasonal, so finance it short-term.</li>
<li><b>Operating cycle</b> = RM holding + WIP + FG holding + debtors' collection period − <b>creditors' payment period</b> (net cycle).
<br>A longer cycle means a <b>higher</b> WC requirement.</li>
<li><b>WC need is higher when:</b>
<ul><li>production is long (heavy engineering)</li>
<li>the business is seasonal</li>
<li>generous credit is given to buyers and little received from suppliers</li>
<li>growth is rapid</li>
<li>inflation is high</li></ul>
It is lower for cash businesses and service firms (restaurants, utilities).</li>
<li><b>Sources:</b>
<ul><li><b>Internal:</b> retained earnings, depreciation provision, accruals (outstanding wages and taxes).</li>
<li><b>External:</b> trade credit, bank finance, CP, factoring, ICDs, public deposits.</li></ul></li></ul>

<h3>2. Bank finance for working capital</h3>
<table><tr><th>Method</th><th>Content</th></tr>
<tr><td><b>Tandon Committee (1975) — MPBF</b></td><td>Working-capital gap (WCG) = CA − CL other than bank borrowings.
<ul><li>Method I: MPBF = 75% of WCG (borrower brings 25% of WCG).</li>
<li><b>Method II: MPBF = 75% of CA − other CL</b> (borrower brings 25% of CA), so the minimum current ratio is <b>1.33 : 1</b>.</li>
<li>Method III: like II but excluding core current assets, which the borrower finances fully.</li></ul></td></tr>
<tr><td><b>Nayak Committee — turnover method</b></td><td>For small borrowers (MSEs with limits up to <b>₹5 crore</b>): WC need = <b>25% of projected annual turnover</b>. Bank finances <b>20%</b>; the borrower's margin is <b>5%</b> of turnover.</td></tr>
<tr><td><b>Cash budget method</b></td><td>For seasonal industries (sugar, tea) and large borrowers: limits fixed from monthly cash-flow deficits.</td></tr>
<tr><td><b>Loan system for delivery of bank credit</b></td><td>RBI 2018: for borrowers with aggregate fund-based WC limits of ₹150 crore and above, at least <b>40%</b> must be a WC <b>loan</b> (from 1 Oct 2018), raised to <b>60%</b> from 1 April 2019. The rest can be cash credit. This forces credit discipline.</td></tr></table>
<p><b>Drawing power</b> = (stock + eligible receivables) − margin, capped by the sanctioned limit. Banks monitor it through stock statements and stock audits.</p>

<h3>3. Commercial Paper (CP)</h3>
<ul><li>A short-term <b>unsecured</b> money-market instrument issued as a <b>promissory note at a discount</b>, in <b>demat</b> form.</li>
<li><b>Tenor:</b> 7 days to 1 year.</li>
<li><b>Denomination:</b> ₹5 lakh and multiples.</li>
<li><b>Issuers:</b> companies, NBFCs (including HFCs), all-India financial institutions and other eligible body corporates. Credit rating required.</li>
<li><b>Banks do not issue CP</b>; they raise short-term funds through <b>Certificates of Deposit (CD)</b>.</li>
<li>Regulated by RBI. CP is cheaper than bank credit for highly rated firms.</li></ul>

<h3>4. Factoring vs forfaiting</h3>
<table><tr><th></th><th>Factoring</th><th>Forfaiting</th></tr>
<tr><td>Receivables</td><td>Ongoing, short-term (up to 180 days), domestic and export, open account</td><td>One-off <b>export</b> receivables, medium-term (often 1–5 years), backed by bills / LC / aval</td></tr>
<tr><td>Recourse</td><td>With or without recourse</td><td><b>Without recourse</b></td></tr>
<tr><td>Finance</td><td>Advance of 75–90%</td><td><b>100%</b> of the value (discounted)</td></tr>
<tr><td>Services</td><td>Also sales-ledger management and collection</td><td>Pure financing</td></tr>
<tr><td>Law</td><td>Factoring Regulation Act 2011</td><td>—</td></tr></table>
<p><b>TReDS:</b> an electronic platform where MSME invoices on large buyers are financed by multiple financiers, <b>without recourse</b> to the MSME.</p>

<div class="box trap"><b>Traps:</b>
<ul><li>A longer operating cycle means <b>more</b> working capital. A longer creditors' period means <b>less</b>.</li>
<li>Tandon Method II → minimum current ratio 1.33.</li>
<li>Nayak: 25% of turnover, of which 20% is bank finance and 5% margin.</li>
<li>CP is unsecured, at a discount, and not for banks.</li>
<li>Forfaiting is without recourse, 100% finance, export-only.</li></ul></div>
''')

Q('C9', """In which case will the working-capital requirement be HIGHER?""",
  "A heavy engineering firm with a long production cycle that sells on long credit",
  ["A restaurant that sells only for cash and buys on 30 days' credit", "An electricity utility that bills customers monthly in advance",
   "A firm whose suppliers give longer credit than it allows its own customers"],
  "A longer operating cycle (long production plus long debtor period) ties up more funds. Cash sales and generous supplier credit reduce WC needs.")

Q('C9', """Raw-material holding 40 days, WIP 15 days, finished goods 25 days, debtors 50 days, creditors 45 days. What is the net operating cycle?""",
  "85 days", ["130 days", "175 days", "60 days"], "Gross cycle = 40 + 15 + 25 + 50 = 130 days; net = 130 − 45 = 85 days.")

Q('C9', """A firm has current assets of ₹400 lakh and current liabilities (other than bank borrowings) of ₹100 lakh. Under Tandon Method II, what is the maximum permissible bank finance?""",
  "₹200 lakh", ["₹225 lakh", "₹300 lakh", "₹250 lakh"],
  "Method II: MPBF = 75% of CA − other CL = 300 − 100 = ₹200 lakh. (Method I: 75% of WCG = 0.75 × 300 = ₹225 lakh.)")

Q('C9', """A small enterprise projects annual turnover of ₹3.2 crore. Under the Nayak Committee turnover method, its working-capital requirement and the minimum bank finance are:""",
  "Requirement ₹80 lakh; bank finance ₹64 lakh, with the borrower bringing ₹16 lakh",
  ["Requirement ₹64 lakh; bank finance ₹48 lakh, with the borrower bringing ₹16 lakh", "Requirement ₹80 lakh; bank finance ₹80 lakh with no margin",
   "Requirement ₹96 lakh; bank finance ₹80 lakh, with the borrower bringing ₹16 lakh"],
  "WC need = 25% of 3.2 crore = ₹80 lakh. Bank finance = 20% of turnover = ₹64 lakh; margin = 5% = ₹16 lakh.")

Q('C9', """Which of the following CANNOT issue Commercial Paper in India?""",
  "A scheduled commercial bank, which raises such funds through Certificates of Deposit instead",
  ["A listed manufacturing company with a good credit rating", "A housing finance company registered with the regulator",
   "An all-India financial institution such as EXIM Bank"],
  "CP is for companies, NBFCs/HFCs, AIFIs and eligible body corporates. Banks raise short-term money through CDs.")

Q('C9', """Which statements about Commercial Paper are correct?
1. It is an unsecured promissory note issued at a discount.
2. Its tenor ranges from 7 days to 1 year.
3. It is issued in multiples of ₹1 lakh in physical form.
4. Issuers need a credit rating.""",
  "1, 2 and 4 only", ["1, 2, 3 and 4", "1 and 3 only", "2 and 3 only"],
  "CP is issued in ₹5 lakh denominations and only in dematerialised form (3 wrong).")

Q('C9', """Which is an INTERNAL source of finance?""",
  "Retained earnings", ["Commercial paper", "Trade credit from suppliers", "Cash credit from a bank"],
  "Retained earnings (and depreciation provisions) are generated inside the firm. The rest come from outsiders.")

Q('C9', """Which statements comparing factoring and forfaiting are correct?
1. Factoring suits ongoing open-account sales; forfaiting suits one-off export receivables backed by bills or LC.
2. Factoring is normally medium- to long-term; forfaiting is short-term.
3. Factoring may be with or without recourse; forfaiting is without recourse.
4. Forfaiting usually provides 100% finance of the receivable value.""",
  "1, 3 and 4 only", ["1, 2, 3 and 4", "2 and 3 only", "1 and 2 only"],
  "Factoring is short-term (up to about 180 days); forfaiting is medium-term (often 1–5 years), so statement 2 is reversed.")

Q('C9', """Under RBI's loan system for delivery of bank credit, for a borrower with aggregate fund-based working-capital limits of ₹200 crore, from April 2019 at least what portion must be drawn as a working-capital loan?""",
  "60%", ["40%", "25%", "75%"],
  "For aggregate limits of ₹150 crore and above, the minimum loan component was 40% from 1 October 2018 and 60% from 1 April 2019; the rest may be cash credit.")

Q('C9', """Net working capital represents:""",
  "The excess of current assets over current liabilities, i.e. the part of current assets financed by long-term funds",
  ["Total current assets, also known as gross working capital of the firm", "The part of current liabilities that is financed by bank borrowings",
   "Fixed assets less long-term liabilities, i.e. the firm's long-term surplus"],
  "Net WC = CA − CL. It is the borrower's long-term contribution (margin) to working capital. Gross WC = total current assets.")
