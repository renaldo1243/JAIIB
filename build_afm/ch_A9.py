from qb import note, Q

note('A9', r'''
<p class="small">Syllabus: Bank audit, emergence of risk-based internal audit, types of bank audit (concurrent, internal, statutory), role of audit and inspection; back-office functions; reconciliation of inter-branch / office entries; peculiar features of bank accounting. <b>Asked: 2–3 audit questions plus about 1 back-office question per session.</b> May 2026 asked:</p>
<ul class="small"><li>A forensic audit approach</li>
<li>RBI audit reports</li>
<li>Inter-branch reconciliation</li>
<li>Functions to ensure compliance</li></ul>

<h3>1. Types of bank audit</h3>
<table><tr><th>Audit</th><th>By whom</th><th>Purpose / features</th></tr>
<tr><td><b>Statutory audit</b> (central + branch)</td><td>External CA firms; appointment needs <b>RBI approval</b> (Sec 30, BR Act). For PSBs the bank appoints from RBI's approved list.</td><td>True-and-fair opinion on annual accounts. Also gives the <b>Long Form Audit Report (LFAR)</b> to management and RBI on advances, deposits, internal controls and NPAs.
<ul><li>RBI 2021 guidelines: SCA/SA term of <b>3 continuous years</b>, then a <b>6-year cooling-off</b>.</li></ul></td></tr>
<tr><td><b>Concurrent audit</b></td><td>External CAs or the bank's own (retired/serving) officers</td><td>Examines transactions <b>at the same time or soon after</b> they occur. It is a <b>part of the internal audit</b> system, an early-warning tool.
<ul><li>Covers treasury, large branches and high-risk areas.</li>
<li>Reports go to the controlling office / Audit Committee.</li></ul></td></tr>
<tr><td><b>Internal audit / inspection</b></td><td>The bank's Inspection &amp; Audit Department</td><td>Periodic review of compliance, controls and risk management.
<ul><li>Since 2002, banks have moved to <b>Risk-Based Internal Audit (RBIA)</b>: audit frequency and depth depend on each branch's risk rating.</li>
<li>RBI made RBIA compulsory for large NBFCs and UCBs in 2021.</li></ul></td></tr>
<tr><td><b>RBI inspection / supervision</b></td><td>RBI under <b>Sec 35, BR Act</b></td><td>Earlier CAMELS-based Annual Financial Inspection. Now <b>Risk-Based Supervision</b> (RBS, from 2013; SPARC model). Covers capital, asset quality, management, earnings, liquidity and systems. Includes the Risk Assessment Report.</td></tr>
<tr><td><b>Revenue / income audit</b></td><td>Internal or external</td><td>Checks leakage of income: interest, charges, commission.</td></tr>
<tr><td><b>Credit / stock audit</b></td><td>External auditors appointed by the bank</td><td>Physical verification of a borrower's stock and receivables, drawing power, end use (for large working-capital limits).</td></tr>
<tr><td><b>IS / IT audit</b></td><td>Specialists</td><td>Security and integrity of CBS and data, access controls.</td></tr>
<tr><td><b>Forensic audit</b></td><td>Forensic specialists</td><td>Investigates suspected fraud with evidence that can stand in court:
<ul><li>trace funds (end-use)</li>
<li>verify the existence of suppliers and buyers</li>
<li>examine digital evidence</li>
<li>rebuild the transaction trail</li>
<li>then fix responsibility</li></ul>
Ratio comparisons or reworking drawing power cannot prove a coordinated fraud.</td></tr></table>
<p><b>Audit Committee of the Board (ACB)</b> oversees the audit function and follows up on inspection and LFAR findings. <b>Audit vs inspection:</b> audit checks that the books are accurate and fair; inspection is wider (management, compliance, risk, systems).</p>

<h3>2. Peculiar features of bank accounting</h3>
<ul><li>Transactions are recorded <b>first in the customer's (personal) ledger through vouchers</b> on the same day. The day book and general ledger are built from them. Every transaction is supported by a <b>voucher</b>.</li>
<li><b>Voucher system:</b>
<ul><li>debit and credit vouchers</li>
<li><b>composite / transfer voucher</b> (a single voucher with several debits and credits, used when one debit/credit affects many accounts)</li>
<li>clearing vouchers</li>
<li>Vouchers are verified and authorised by an officer other than the maker (maker–checker).</li></ul></li>
<li><b>Slip system / cash book slip system:</b>
<ul><li>Pay-in slips filled by customers act as vouchers.</li>
<li>The cash book is maintained through slips sorted by type.</li>
<li>This saves posting time.</li></ul></li>
<li><b>Daily balancing:</b> general ledger and subsidiary ledgers are balanced every day. CBS does this automatically, end of day.</li>
<li><b>Accrual for interest</b> and <b>income recognition norms</b> for NPAs (no accrual of interest on NPAs).</li></ul>

<h3>3. Back-office functions</h3>
<ul><li>The back office supports the front office (customer-facing). Its work:
<ul><li>transaction processing and settlement (clearing, NEFT/RTGS)</li>
<li>reconciliation</li>
<li>account maintenance and KYC data</li>
<li>MIS and regulatory returns</li>
<li>loan documentation and limit monitoring</li>
<li>compliance checks</li></ul></li>
<li>In treasury: <b>front office</b> (dealing), <b>mid office</b> (risk management, limits), <b>back office</b> (deal confirmation, settlement, accounting, reconciliation). These are kept separate for internal control.</li></ul>

<h3>4. Reconciliation in banks</h3>
<ul><li><b>Inter-branch / inter-office accounts:</b>
<ul><li>Branches transact with each other on behalf of customers through Inter-Branch (IB) / Head Office accounts.</li>
<li>The <b>originating</b> branch sends an advice and the <b>responding</b> branch records the matching entry.</li>
<li>Entries without a matching response are <b>unreconciled</b>.</li></ul></li>
<li><b>Why it matters:</b> long-pending unreconciled debits can hide frauds or losses.</li>
<li><b>RBI's rule on inter-branch accounts:</b>
<ul><li>banks must eliminate old outstanding entries</li>
<li>banks must provide <b>100% for net debit balances outstanding for more than one year</b></li>
<li>credit balances are not taken to income</li></ul></li>
<li>Also reconciled:
<ul><li><b>Nostro accounts</b>: our account with a foreign bank, in foreign currency. Matched with our <b>mirror</b> account.</li>
<li>Vostro accounts</li>
<li>ATM and card settlement, clearing differences</li>
<li>suspense and sundry accounts</li></ul></li>
<li>With CBS, centralised reconciliation cells match entries using automated tools.</li></ul>

<div class="box trap"><b>Traps:</b>
<ul><li>Concurrent audit is a <b>part of internal audit</b>. It is not a statutory audit.</li>
<li>LFAR is given by <b>statutory</b> auditors.</li>
<li>RBI inspection is under <b>Sec 35</b>; auditors and their RBI approval under <b>Sec 30</b>; accounts and Third Schedule format under <b>Sec 29</b> (all BR Act).</li>
<li>Unreconciled inter-branch <b>debits</b> are the risk. The 100% provision is on net debit balances older than 1 year.</li>
<li>Forensic audit = tracing evidence and money trail, not profitability review.</li></ul></div>
''')

Q('A9', """A bank finds that five unrelated borrowers submitted invoices from suppliers that do not exist on GSTN, funds were withdrawn within 48 hours, and stock statements were identical across industries; concurrent audit flagged nothing. The Board appoints a forensic auditor. Which approach best establishes a coordinated fraud?""",
  "Trace end-use of funds, verify supplier existence, examine digital evidence and rebuild the transaction trail before fixing responsibility",
  ["Compare each account's interest yield with industry averages and quantify the revenue leakage", "Recompute drawing power from stock statements and increase provisioning under IRAC norms",
   "Review branch profitability, staff appraisal ratings and whether sanctions exceeded delegated powers"],
  "A forensic audit gathers evidence that can be used in legal proceedings: money trail, document genuineness, digital trail, and links between parties. Provisioning or profitability reviews don't prove fraud.")

Q('A9', """Which statement about concurrent audit in banks is correct?""",
  "It examines transactions at or close to the time they take place and is a part of the bank's internal audit system",
  ["It is a statutory audit whose auditors need RBI approval under Section 30 of the BR Act", "It is conducted only once a year, after the balance sheet date, by the central auditors",
   "It is an inspection carried out by RBI officials under Section 35 of the BR Act"],
  "Concurrent audit is a continuous, early-warning check that forms part of internal audit. Statutory auditors (Sec 30) give the year-end opinion; RBI inspects under Sec 35.")

Q('A9', """The Long Form Audit Report (LFAR) in banks is submitted by:""",
  "Statutory auditors, in addition to their audit report on the accounts", ["Concurrent auditors, to the branch manager every month", "RBI inspectors, to the bank's Board after inspection",
   "Internal auditors, to the Audit Committee of the Board only"],
  "LFAR is prepared by statutory central and branch auditors in RBI-prescribed format, covering advances, deposits, internal controls and other areas, alongside the main audit report.")

Q('A9', """Under RBI's 2021 guidelines on appointment of statutory auditors of banks, an audit firm can be appointed for:""",
  "A continuous period of three years, after which it is not eligible for re-appointment for six years",
  ["One year at a time, renewable indefinitely as long as RBI approves each year", "A continuous period of five years, followed by a cooling-off period of two years", "Ten years, subject to fresh RBI approval and a performance review every year"],
  "RBI's April 2021 guidelines fix the tenure of SCAs/SAs at three continuous years, subject to satisfying eligibility norms each year, followed by a cooling-off period of six years.")

Q('A9', """Match the legal provisions of the Banking Regulation Act:
P. Form of balance sheet and P&L of banks
Q. Audit of banks; approval of auditors
R. Inspection by RBI""",
  "P – Section 29; Q – Section 30; R – Section 35", ["P – Section 30; Q – Section 29; R – Section 35",
   "P – Section 29; Q – Section 35; R – Section 30", "P – Section 35; Q – Section 30; R – Section 29"],
  "Sec 29 requires accounts in the Third Schedule forms; Sec 30 deals with audit and RBI approval of auditors; Sec 35 empowers RBI to inspect banks.")

Q('A9', """What is the primary feature of Risk-Based Internal Audit (RBIA)?""",
  "The frequency and depth of audit of each unit depend on its assessed risk, not a uniform calendar",
  ["Every branch is audited every month regardless of its size or business profile", "Only branches showing losses or rising NPAs are audited during the year",
   "Audit is replaced by quarterly self-certification of controls by branch managers"],
  "RBIA allocates audit resources to high-risk branches and activities (business risk and control risk), as guided by RBI since 2002.")

Q('A9', """Regarding inter-branch accounts in banks, which statement is correct?""",
  "Banks must make 100% provision for net debit balances in inter-branch accounts outstanding for more than one year",
  ["Unreconciled credit balances must be taken to income after six months of being outstanding", "Inter-branch accounts need to be reconciled only at the year-end, before the statutory audit",
   "Unreconciled debit entries carry no risk as both branches belong to the same bank"],
  "Long-pending debits in inter-branch accounts can conceal frauds or losses. RBI requires full provision for net debit balances outstanding beyond one year; credit balances are not taken to income.")

Q('A9', """In bank treasury, why are front office, mid office and back office kept separate?""",
  "To ensure internal control: dealers deal, the mid office monitors risk and limits, and the back office independently confirms, settles and accounts",
  ["To give each office the power to approve and settle its own deals without delay", "Because RBI requires the three offices to be located in different cities for safety",
   "To allow the back office to take trading positions whenever the dealers are absent"],
  "Separation of duties prevents one person both dealing and settling or recording; that segregation is a key control against fraud.")

Q('A9', """In bank accounting, a 'composite voucher' is used when:""",
  "One debit or credit is matched by several entries, so a single voucher records multiple accounts",
  ["Cash is deposited by a single customer into his own savings account", "The voucher has to be signed by two officers under maker–checker", "The day book does not balance and a difference has to be carried"],
  "A composite (transfer) voucher records a transaction affecting several accounts in one voucher, e.g. salary credit to many staff accounts from one debit.")

Q('A9', """Which of the following is NOT a typical back-office function in a bank?""",
  "Meeting walk-in customers to sell new products", ["Reconciliation of nostro and inter-branch accounts", "Settlement of NEFT, RTGS and clearing",
   "Preparing MIS and regulatory returns"],
  "Selling to customers is a front-office function. Reconciliation, settlement, accounting and reporting are back-office functions.")
