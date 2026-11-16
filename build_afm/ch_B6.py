from qb import note, Q

note('B6', r'''
<p class="small">Syllabus: Computerised accounting (meaning, features, terms, vs manual, advantages, functions, software), computerisation in banking, core banking components, information security. <b>Asked: 2–3 questions per session.</b> May 2026 asked:</p>
<ul class="small"><li>analog computer (twice)</li>
<li>manual vs computerised accounting</li>
<li>online vs batch processing</li>
<li>neo banks (three times)</li>
<li>CBS architecture</li></ul>

<h3>1. Computerised accounting</h3>
<ul><li>Software records transactions once (data entry, usually through vouchers). Ledgers, the trial balance and financial statements are generated <b>automatically</b>.</li>
<li><b>Features:</b>
<ul><li>speed and accuracy</li>
<li>real-time reports and MIS</li>
<li>automatic posting and balancing</li>
<li>security through passwords and access levels</li>
<li>audit trail</li>
<li>scalability, backups</li></ul></li></ul>
<table><tr><th>Manual</th><th>Computerised</th></tr>
<tr><td>Journal → ledger → trial balance done by hand</td><td>Only data entry is manual; posting and statements are automatic</td></tr>
<tr><td>Trial balance prepared to check arithmetic</td><td>Trial balance always tallies (posting errors are eliminated). Errors of principle and data-entry errors remain</td></tr>
<tr><td>Reports take time</td><td>Instant reports, any period</td></tr>
<tr><td>Physical books</td><td>Database: needs backups and IT controls</td></tr></table>
<ul><li><b>Disadvantages:</b> cost, need for trained staff, system failure, virus and cyber risk, data loss without backup, over-dependence.</li>
<li><b>Software:</b> Tally, SAP, Oracle, QuickBooks, Busy, Zoho. In banks: CBS such as Finacle, Flexcube, BaNCS.</li>
<li><b>Terms:</b>
<ul><li><b>Master files</b>: static data such as the account master</li>
<li><b>Transaction files</b></li>
<li><b>Codification</b>: account codes</li>
<li><b>Grouping</b></li>
<li><b>Audit trail</b></li>
<li><b>Data validation</b></li></ul></li></ul>

<h3>2. Processing modes</h3>
<ul><li><b>Batch processing:</b> transactions are collected and processed together later (e.g. end-of-day interest run). Efficient for volume, but data is not current.</li>
<li><b>Online / real-time processing:</b> each transaction updates the database immediately. Balances are always current and customers can transact anywhere (ATM, internet banking, any-branch banking).</li></ul>

<h3>3. Types of computers</h3>
<ul><li><b>Analog:</b> processes <b>continuously varying</b> physical quantities (temperature, pressure, voltage, speed). Used in scientific and engineering fields: speedometers, thermostats, power-station monitoring.</li>
<li><b>Digital:</b> discrete binary data (0/1). Business computers.</li>
<li><b>Hybrid:</b> both, e.g. hospital ICU monitors, petrol pumps.</li>
<li>By size: supercomputer, mainframe (bank data centres), mini, micro/PC.</li></ul>

<h3>4. Core Banking Solution (CBS)</h3>
<ul><li>Centralised database at a <b>data centre</b> (with a disaster recovery site). Each branch connects to the <b>central server</b> through a network, so any-branch banking works and the bank becomes the customer's bank, not the branch's.</li>
<li><b>Components:</b>
<ul><li>central database and application server</li>
<li>network (WAN/VSAT)</li>
<li>delivery channels (branch, ATM, internet and mobile banking)</li>
<li>interfaces (payment systems, SWIFT, treasury)</li></ul></li>
<li><b>Information security:</b>
<ul><li>CIA = confidentiality, integrity, availability</li>
<li>access controls, maker–checker</li>
<li>password policies, encryption, firewalls</li>
<li>BCP/DR</li></ul></li></ul>

<h3>5. Neo banks</h3>
<ul><li>Digital-only, app-based platforms with <b>no physical branches</b>. Examples: instant account opening, virtual cards, API payments, expense tools.</li>
<li>In India, neo banks <b>do not hold a banking licence</b>. They work in <b>partnership with RBI-licensed banks</b>, which hold the deposits, do the lending and maintain CRR/SLR. The neo bank provides the technology front end.</li>
<li>They are not exempt from regulation: the partner bank is accountable, and RBI's digital-lending and outsourcing rules apply.</li></ul>

<div class="box trap"><b>Traps:</b>
<ul><li>Continuous signals (voltage, temperature) = <b>analog</b>, even if numbers are displayed.</li>
<li>Computerised accounting removes posting and totalling errors, <b>not</b> errors of principle or wrong data entry.</li>
<li>Under CBS, branch servers connect to the central data-centre server; branches don't hold separate databases linked to each other.</li>
<li>A neo bank cannot independently accept deposits or maintain CRR/SLR.</li></ul></div>
''')

Q('B6', """A hydroelectric station uses an old device that continuously measures temperature, pressure and voltage, with output as continuously varying signals. A trainee calls it a digital computer because numbers are shown. It is actually:""",
  "An analog computer, because it processes continuously varying physical quantities",
  ["A digital computer, because every computer processes binary data", "A hybrid computer, because all engineering devices are hybrid",
   "A mainframe computer, because it runs continuously without stopping"],
  "Analog computers work on continuous physical quantities; digital computers on discrete binary data; hybrids combine both.")

Q('B6', """In the core banking system of a large bank:""",
  "Each branch connects through the network to a central server at the bank's data centre",
  ["Each branch has its own database server connected directly to every other branch", "There is no central server; each branch works offline and uploads data monthly",
   "Two central servers are kept at each branch for redundancy"],
  "CBS centralises the database at the data centre (with a DR site); branches access it online, enabling anywhere banking.")

Q('B6', """Which is a fundamental difference between manual and computerised accounting?""",
  "Posting, balancing and statements are automatic once data is entered",
  ["Computerised accounting eliminates the need for vouchers and source documents", "Manual accounting cannot follow the double-entry system",
   "Computerised accounting automatically detects errors of principle"],
  "Software automates everything after data entry. Source documents are still needed, and errors of principle or wrong entries are not detected.")

Q('B6', """The main benefit of online (real-time) processing over batch processing in banking is that:""",
  "Each transaction updates the database immediately, so balances are always current",
  ["Transactions are grouped and processed at the end of the day at lower cost", "It needs no network connectivity at the branches",
   "It eliminates the need for data backups"],
  "Real-time processing posts each transaction at once, which supports ATMs, internet banking and any-branch banking. Batch processing accumulates transactions for later processing.")

Q('B6', """A fintech markets itself as a 'Neo Bank' offering instant accounts, virtual debit cards and API payments. Can it independently accept public deposits, lend from them and maintain CRR/SLR?""",
  "No; they work through partner licensed banks, which hold deposits and do regulated functions",
  ["Yes; neo banks get a banking licence automatically after three years of operation", "Yes; neo banks function exactly like scheduled commercial banks",
   "No; but they may issue currency through digital wallets instead"],
  "Indian neo banks are technology platforms without their own banking licence; the partner bank holds deposits, lends and maintains CRR/SLR.")

Q('B6', """Which statement about computerised accounting is NOT correct?""",
  "It guarantees that financial statements are free from all errors",
  ["It provides an audit trail of entries and changes", "It enables reports for any period to be generated instantly",
   "It needs regular data backups and access controls"],
  "Wrong data entry or errors of principle still flow into the statements: 'garbage in, garbage out'. The other statements are correct.")

Q('B6', """The three core objectives of information security in a bank's CBS are:""",
  "Confidentiality, integrity and availability", ["Speed, cost and accuracy", "Authorisation, accounting and auditing",
   "Encryption, firewalls and passwords"],
  "The CIA triad. Encryption, firewalls and passwords are controls used to achieve these objectives.")
