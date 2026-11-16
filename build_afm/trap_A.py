from qb import T

# ---------- A1 Accounting Standards ----------
T('A1', """After the balance sheet date but before approval of accounts, a fire destroys a warehouse (no doubt about going concern). The accountant reduces the year-end stock and assets because "the accounts are not yet approved". The correct treatment is:""",
  "Do not adjust; disclose the event in the report if it is material",
  ["Adjust the year-end figures because the accounts were not yet approved", "Adjust only if the loss exceeds 10% of net profit",
   "Ignore the event entirely because it happened after year-end"],
  "Trap: 'not yet approved' does not make every event adjusting. A fire is a new condition arising after the balance sheet date: non-adjusting under AS 4, disclosed if material.")

T('A1', """A company received a government grant of ₹10 lakh in cash this year towards a machine with a 10-year life. The accountant credits the full ₹10 lakh to P&L because "cash was received this year". Under AS 12 the grant should be:""",
  "Deducted from the machine's cost or released as income over its 10-year life",
  ["Credited fully to P&L this year because cash was received", "Credited to Share Capital as owners' funds",
   "Kept outside the books until the machine is sold"],
  "Trap: receipt of cash ≠ income. AS 12 matches a grant on a depreciable asset with the depreciation, either by reducing cost or as deferred income.")

T('A1', """Which of the following is TRUE under AS 26?""",
  "An internally generated brand cannot be recognised as an asset even if it is valuable",
  ["Pre-launch advertising can be capitalised if it builds the brand", "All research and development spend can be capitalised once a patent is filed",
   "Staff training on new software can be capitalised as part of the software"],
  "Trap: 'it adds value, so capitalise'. AS 26 bans internally generated brands, mastheads and customer lists, and always expenses advertising, training and research.")

T('A1', """A related-party question: two companies, X Ltd and Y Ltd, have one director in common and no other link. X sells goods to Y. Under AS 18:""",
  "No related-party disclosure is required merely because of a common director",
  ["Disclosure is required because they share a director", "Disclosure is required only if the sale was at a loss",
   "Disclosure is required only if payment was in cash"],
  "Trap: common director = related. AS 18 expressly excludes two companies related only through a common director.")

T('A1', """Under AS 7, a contract is 25% complete; total estimated cost now exceeds the contract price by ₹8 crore. How much loss is recognised this year?""",
  "₹8 crore — the full expected loss", ["₹2 crore — 25% of the expected loss", "Nil — loss is recognised only on completion",
   "₹6 crore — the loss on the remaining 75% only"],
  "Trap: applying percentage-of-completion to losses. Expected losses are recognised immediately in full (prudence).")

T('A1', """Under AS 2, which value is used for inventory: cost ₹50,000; NRV ₹46,000; replacement cost ₹44,000?""",
  "₹46,000", ["₹44,000", "₹50,000", "₹45,000"],
  "Trap: using replacement cost or the lowest number. AS 2 = lower of cost and NRV → ₹46,000. Replacement cost is relevant only for raw materials when the finished goods' NRV is below cost.")

T('A1', """Under AS 28, recoverable amount of an asset is:""",
  "The higher of net selling price and value in use", ["The lower of net selling price and value in use",
   "Always the net selling price", "The carrying amount less accumulated depreciation"],
  "Trap: 'lower of'. A rational owner would sell or use, whichever gives more, so recoverable amount is the HIGHER figure; impairment arises only if carrying amount exceeds it.")

T('A1', """A company's long-term investment in shares falls 5% below cost due to a temporary market dip. The accountant writes it down because "AS 13 requires market value". The correct view is:""",
  "Long-term investments stay at cost; only a decline other than temporary is provided for",
  ["All investments must be shown at market value every year", "Long-term investments are shown at the lower of cost and market value",
   "The fall must be credited to a revaluation reserve"],
  "Trap: mixing current and long-term rules. Lower of cost and fair value applies to CURRENT investments; long-term ones are at cost less permanent diminution.")

# ---------- A2 Concepts & Equation ----------
T('A2', """Which concept explains why a proprietor's capital is shown as a liability of the business?""",
  "Business entity concept", ["Going concern concept", "Money measurement concept", "Dual aspect concept alone"],
  "Trap: 'dual aspect'. Because the business is a separate entity from its owner, it owes the capital to the owner, which is why capital appears among liabilities.")

T('A2', """Closing stock is valued at ₹4.8 lakh (cost) though its market value is ₹5.6 lakh. Which convention is applied?""",
  "Conservatism (prudence)", ["Cost concept", "Consistency", "Materiality"],
  "Trap: 'cost concept'. Choosing the LOWER of cost and market for stock is conservatism: don't anticipate the unrealised gain.")

T('A2', """A firm bought a building for ₹50 lakh; it is now worth ₹80 lakh. Keeping it at ₹50 lakh (less depreciation) applies:""",
  "Cost concept, supported by going concern", ["Conservatism, because gains are never recorded", "Realisation concept",
   "Money measurement concept"],
  "Trap: confusing with conservatism. Fixed assets stay at historical cost because the business will use them, not sell them (going concern).")

T('A2', """Which transaction INCREASES total assets but does NOT change capital?""",
  "Goods purchased on credit", ["Owner introducing cash", "Cash sales at a profit", "Furniture bought for cash"],
  "Trap: furniture for cash (assets unchanged, one up one down). Credit purchase raises stock and creditors equally.")

T('A2', """Profit for the year is ₹4 lakh; drawings ₹1 lakh; fresh capital ₹2 lakh; closing capital ₹15 lakh. Opening capital was:""",
  "₹10 lakh", ["₹12 lakh", ["₹8 lakh"][0], "₹16 lakh"],
  "Closing = Opening + Fresh + Profit − Drawings → 15 = O + 2 + 4 − 1 → O = ₹10 lakh. Trap: adding drawings instead of subtracting gives ₹8 lakh.")

T('A2', """Income received in advance is recorded as a liability mainly because of:""",
  "The accrual (and matching) concept: it is not yet earned", ["The conservatism convention only", "The cost concept",
   "The going concern concept only"],
  "Trap: 'conservatism'. Income is recognised when earned; cash received early is a liability until the service is rendered.")

T('A2', """Which statement is correct?""",
  "Consistency allows a change in method if a better presentation results, with disclosure",
  ["Consistency means a method can never be changed once adopted", "Materiality means every item must be shown separately",
   "Conservatism requires creating secret reserves wherever possible"],
  "Trap words: 'never', 'every', 'wherever possible'. Consistency permits justified change with disclosure; materiality allows insignificant items to be grouped; conservatism does not allow secret reserves.")

T('A2', """Capital ₹6 lakh; liabilities ₹4 lakh. The firm repays ₹1 lakh of a loan and the owner withdraws ₹50,000. Total assets now are:""",
  "₹8.5 lakh", ["₹10 lakh", "₹9 lakh", "₹9.5 lakh"],
  "Assets = 10 lakh at start. Loan repayment: assets −1. Drawings: assets −0.5. 10 − 1.5 = ₹8.5 lakh (liabilities 3, capital 5.5).")

# ---------- A3 Golden rules / journal ----------
T('A3', """Discount Allowed is a:""",
  "Nominal account", ["Personal account", "Real account", "Representative personal account"],
  "Trap: 'personal' because it relates to a debtor. Discount allowed is a loss/expense, so it is nominal.")

T('A3', """Goodwill purchased is classified as:""",
  "Intangible real account", ["Nominal account", "Personal account", "Fictitious asset"],
  "Trap: 'nominal' because it is not physical. Goodwill is a (intangible) real account.")

T('A3', """Salary outstanding is classified as:""",
  "Representative personal account", ["Nominal account", "Real account", "Artificial personal account"],
  "Trap: 'nominal' because salary is an expense. The outstanding salary account represents the employees to whom it is owed.")

T('A3', """Office furniture is bought on credit from Modern Furnishers. Debit:""",
  "Furniture A/c; credit Modern Furnishers", ["Purchases A/c; credit Modern Furnishers", "Furniture A/c; credit Cash A/c",
   "Modern Furnishers; credit Furniture A/c"],
  "Trap: 'Purchases'. Purchases is only for goods meant for resale; furniture is a fixed asset (real account: debit what comes in).")

T('A3', """Goods worth ₹5,000 (cost) are distributed as free samples. The entry is:""",
  "Advertisement A/c Dr; To Purchases A/c", ["Advertisement A/c Dr; To Sales A/c", "Drawings A/c Dr; To Purchases A/c",
   "Purchases A/c Dr; To Advertisement A/c"],
  "Trap: crediting Sales. Samples are not sold; their cost is removed from purchases and treated as advertisement expense.")

T('A3', """Cash ₹50,000 withdrawn from bank for office use. In a double-column cash book this is:""",
  "A contra entry, recorded in both cash and bank columns", ["Recorded only in the cash column",
   "Recorded only in the journal proper", "Recorded in the petty cash book"],
  "Trap: one-column thinking. Both cash and bank are affected, so it is a contra entry marked 'C'.")

T('A3', """Under the imprest system, the petty cashier spent ₹3,800 out of a float of ₹5,000. The main cashier will give him:""",
  "₹3,800", ["₹5,000", "₹1,200", "₹8,800"],
  "Trap: giving the full float again. Imprest = reimburse exactly what was spent so the float returns to ₹5,000.")

T('A3', """A credit purchase of a computer for office use is recorded in:""",
  "Journal proper", ["Purchases book", "Cash book", "Bills payable book"],
  "Trap: 'Purchases book'. The purchases book is only for credit purchases of goods for resale; credit purchase of assets goes to the journal proper.")

# ---------- A4 Errors & suspense ----------
T('A4', """Errors found: (a) Purchases Book undercast by ₹3,000; (b) ₹1,500 paid to Ram debited to Shyam; (c) a sales return of ₹700 from Hari posted to the DEBIT of Hari's account. The Suspense Account was opened with:""",
  "₹1,600 on the debit side", ["₹3,700 on the debit side", "₹2,300 on the credit side", "₹5,200 on the debit side"],
  "(a) debit side short 3,000. (b) no effect (two-sided). (c) Hari should be credited 700 but was debited 700 → debit side excess 1,400. Net debit short = 3,000 − 1,400 = 1,600 → suspense debited ₹1,600.")

T('A4', """For the same errors [(a) purchases book undercast ₹3,000; (b) Ram/Shyam; (c) Hari's account], rectification will change net profit by:""",
  "−₹3,000", ["−₹1,600", "−₹4,400", "Nil, as all are posting errors"],
  "Only (a) touches a nominal account (purchases up by 3,000 → profit down 3,000). (b) and (c) affect personal accounts only. Trap: equating profit effect with the suspense balance.")

T('A4', """A credit sale of ₹6,000 to Anil was entered in the Sales Book as ₹600. This error:""",
  "Does not affect the Trial Balance; sales and Anil are both understated by ₹5,400",
  ["Affects the Trial Balance by ₹5,400", "Is an error of principle", "Is a compensating error"],
  "Trap: thinking every wrong amount disturbs the TB. A wrong amount in the book of original entry is posted wrongly to both sides.")

T('A4', """Which error must be corrected through the Suspense Account?""",
  "Sales Book overcast by ₹2,000", ["Repairs debited to Machinery A/c", "Credit sale to Mohan omitted completely",
   "Purchase from Ravi credited to Ravindra's account"],
  "Only one-sided errors go through suspense. Overcasting a book affects only the sales account. The others are two-sided or complete omissions.")

T('A4', """₹2,500 received from Sita was correctly entered in the cash book but posted to the DEBIT of Sita's account. The rectifying entry is:""",
  "Suspense A/c Dr ₹5,000; To Sita ₹5,000", ["Suspense A/c Dr ₹2,500; To Sita ₹2,500", "Sita Dr ₹5,000; To Suspense ₹5,000",
   "Cash A/c Dr ₹2,500; To Sita ₹2,500"],
  "Trap: correcting with the single amount. Wrong side means cancel the wrong debit AND record the correct credit: double.")

T('A4', """Repairs of ₹40,000 to a building were debited to the Building Account. Effect if not corrected:""",
  "Profit overstated, assets overstated, Trial Balance agrees", ["Profit understated, assets overstated, Trial Balance agrees",
   "Profit overstated, Trial Balance disagrees by ₹40,000", "No effect, since the amount was correctly paid"],
  "Revenue expenditure capitalised (error of principle): expense missing → profit up; building inflated; both sides posted → TB agrees.")

T('A4', """A purchase of ₹9,000 from Gopal was entered correctly in the Purchases Book but posted to Gopal's account as ₹900. The error is:""",
  "An error of commission that disturbs the Trial Balance", ["An error of omission that does not disturb the Trial Balance",
   "An error of principle that does not disturb the Trial Balance", "A compensating error"],
  "Purchases debited 9,000 but Gopal credited only 900: one-sided posting error → TB credit side short by 8,100.")

T('A4', """Which statement is correct?""",
  "A Trial Balance can agree even when errors exist in the books",
  ["Agreement of the Trial Balance proves the accounts are correct", "A suspense account is opened for errors of principle",
   "Compensating errors always cause disagreement of the Trial Balance"],
  "Errors of omission, principle and compensating errors don't disturb TB totals.")

T('A4', """An error discovered after closing the books: sale of an old machine ₹30,000 was credited to Sales last year. The correction this year is:""",
  "Profit & Loss Adjustment A/c Dr; To Machinery A/c", ["Sales A/c Dr; To Machinery A/c", "Machinery A/c Dr; To Sales A/c",
   "Suspense A/c Dr; To Machinery A/c"],
  "Trap: debiting Sales, which was already closed. Last year's sales were overstated (profit overstated), so the adjustment goes through P&L Adjustment; Machinery is still overstated, so it is credited.")

T('A4', """A Trial Balance is NOT used to detect which of the following?""",
  "An error of principle", ["A one-sided posting error", "A casting error in the sales book", "Wrong balancing of an account"],
  "Errors of principle record both sides correctly in amount, so totals still agree. The others are one-sided.")

# ---------- A5 BRS ----------
T('A5', """Cash book shows an OVERDRAFT of ₹50,000. Cheques deposited but not credited ₹8,000; cheques issued not presented ₹12,000; interest on overdraft ₹1,500 not in the cash book. Overdraft as per pass book is:""",
  "₹47,500", ["₹52,500", "₹55,500", "₹44,500"],
  "Treat as −50,000: uncredited deposits −8,000; unpresented cheques +12,000; OD interest −1,500 → −47,500. Trap: using favourable-balance signs gives 52,500.")

T('A5', """Pass book shows a credit balance of ₹30,000. Cheques issued not presented ₹5,000; a customer's direct deposit of ₹2,000 not in cash book; bank charges ₹300 not in cash book. Balance as per cash book is:""",
  "₹23,300", ["₹36,700", "₹22,700", "₹27,300"],
  "From pass book: less unpresented cheques 5,000 (cash book already reduced) = 25,000; less direct deposit 2,000 = 23,000; add bank charges 300 = 23,300. Trap: using cash-book-start signs.")

T('A5', """Which item requires NO entry in the cash book?""",
  "A cheque issued to a supplier that is not yet presented", ["Bank charges debited by the bank",
   "Interest credited by the bank", "A customer's cheque returned dishonoured"],
  "Only timing differences (unpresented / uncollected cheques) need no cash-book entry. Bank-originated items must be recorded.")

T('A5', """While preparing the BRS starting from a favourable cash-book balance, a dishonoured cheque not yet recorded in the cash book is:""",
  "Deducted", ["Added", "Ignored", "Added and then deducted"],
  "The bank has already reduced the balance, so the pass book is lower: deduct.")

T('A5', """The bank wrongly debited ₹4,000 belonging to another customer to our account. The correct action is:""",
  "Show it in the BRS and ask the bank to reverse it; make no cash-book entry",
  ["Record it in the cash book as a bank charge", "Record it in the cash book and claim later",
   "Write it off as a bad debt"],
  "A bank's error is not our transaction. Our cash book is correct; the item appears only in the BRS.")

T('A5', """The balance of bank to be shown in the Balance Sheet is:""",
  "The adjusted cash-book balance", ["The pass-book balance", "The unadjusted cash-book balance", "The higher of the two balances"],
  "After recording bank-originated items, the adjusted cash book shows the true balance. Trap: 'pass book because bank prepares it'.")

T('A5', """Starting from the pass-book balance, 'cheques deposited but not yet credited' are:""",
  "Added to arrive at the cash-book balance", ["Deducted to arrive at the cash-book balance", "Ignored",
   "Added only in an overdraft situation"],
  "The cash book already includes them, the pass book doesn't, so the cash book is higher: add.")

T('A5', """In the cash book, a deposit of ₹56,000 was wrongly recorded as ₹65,000. Starting from the cash-book balance, this error is:""",
  "Deducted by ₹9,000 (and the cash book corrected)", ["Added by ₹9,000", "Deducted by ₹65,000", "Ignored as a timing difference"],
  "The cash book is overstated by 9,000. Deduct it in the BRS and correct the cash book; it is our error, not a timing difference.")

T('A5', """Which pair is correctly matched?""",
  "Favourable balance – debit in cash book, credit in pass book",
  ["Favourable balance – credit in cash book, debit in pass book", "Overdraft – debit in cash book, credit in pass book",
   "Overdraft – debit in both cash book and pass book"],
  "Mirror image: our asset (debit) is the bank's liability (credit). An overdraft is the reverse.")

T('A5', """An insurance premium of ₹6,000 was paid by the bank under standing instructions; not in the cash book. In the adjusted cash book:""",
  "Credit Bank ₹6,000 (debit Insurance)", ["Debit Bank ₹6,000", "No entry; show only in the BRS", "Debit Bank and credit Insurance"],
  "It is a real payment we have not recorded: insurance expense debit, bank credit.")

# ---------- A6 Depreciation ----------
T('A6', """A machine costs ₹1,00,000; freight ₹5,000; installation ₹5,000; residual value ₹10,000; life 5 years; SLM. Annual depreciation is:""",
  "₹20,000", ["₹18,000", "₹22,000", "₹16,000"],
  "Depreciable amount = (1,00,000 + 5,000 + 5,000) − 10,000 = 1,00,000 ÷ 5 = 20,000. Traps: ignoring freight/installation (18,000) or residual (22,000).")

T('A6', """An asset costing ₹2,00,000 is bought on 1 October; WDV 15%; the year ends 31 March. First year's depreciation is:""",
  "₹15,000", ["₹30,000", "₹7,500", "₹22,500"],
  "6 months: 2,00,000 × 15% × 6/12 = 15,000. Trap: charging a full year (30,000).")

T('A6', """A company changes its depreciation method from SLM to WDV after a review of the pattern of benefits. Under AS 10 this is:""",
  "A change in accounting estimate, applied prospectively", ["A change in accounting policy, applied retrospectively",
   "A prior period item", "Not permitted once a method is adopted"],
  "Trap: 'policy, retrospective' (old AS 6 view). Under revised AS 10 a change in depreciation method is a change in estimate.")

T('A6', """Which statement about depreciation is correct?""",
  "It is a non-cash charge that reduces profit but does not create cash",
  ["It is a source of funds because it is added back in the cash flow statement", "It values the asset at its market price",
   "It is charged only when the asset is actually used"],
  "Trap: 'source of funds'. It is added back only because it was deducted without cash outflow. Depreciation starts when the asset is available for use.")

T('A6', """₹6,00,000 asset, WDV 20%. Which is the book value at the end of Year 3?""",
  "₹3,07,200", ["₹2,40,000", "₹2,88,000", "₹3,84,000"],
  "6,00,000 × 0.8³ = 6,00,000 × 0.512 = 3,07,200. 2,40,000 would be SLM at 20% of cost; 3,84,000 is the value after only 2 years.")

T('A6', """A machine bought for ₹50 lakh is depreciated by SLM over 10 years (nil residual). After 4 years its remaining life is revised to 3 years. Depreciation from Year 5 is:""",
  "₹10 lakh a year", ["₹5 lakh a year", "₹7.14 lakh a year", "₹16.67 lakh a year"],
  "Carrying amount after 4 years = 50 − 20 = 30 lakh. Spread over 3 remaining years = ₹10 lakh. Traps: keeping 5 lakh, or using total cost ÷ 3.")

T('A6', """Which of the following can reduce an asset's book value to exactly zero?""",
  "SLM with nil residual value", ["WDV at any rate", "WDV at a very high rate such as 90%", "Units of production with a residual value"],
  "WDV applies a % to a declining balance, so a balance always remains; SLM with nil residual writes off fully.")

T('A6', """A transport operator's buses earn most in early years and need heavy repairs later. Choose the method:""",
  "WDV", ["SLM", "Sinking fund", "Annuity"],
  "WDV gives high early charges and lower later charges, balancing rising repairs. Trap: SLM because it is simple.")

# ---------- A7 Capital vs revenue ----------
T('A7', """Which is REVENUE expenditure?""",
  "Lubricants for routine servicing of a machine", ["Freight paid to bring a new machine to the factory",
   "Wages to own staff for installing a new machine", "Overhaul that extends a machine's life by 5 years"],
  "Trap: 'it relates to machinery, so capital'. Routine servicing maintains; the others bring the asset into use or extend its life.")

T('A7', """Which is CAPITAL expenditure?""",
  "Legal fees paid to buy land", ["Annual painting of the office", "Repairs to a delivery van", "Carriage on goods purchased"],
  "Costs to acquire an asset are capitalised. Painting, routine repairs and freight on stock are revenue.")

T('A7', """GST paid on a machine is ₹1.8 lakh and full ITC is available. It should be:""",
  "Excluded from the machine's cost and taken as input tax credit", ["Added to the machine's cost", "Charged to P&L as an expense",
   "Added to cost and depreciated over the machine's life"],
  "Only NON-refundable taxes are part of cost under AS 10. Creditable GST is recovered, so it is not a cost.")

T('A7', """Insurance claim received for a building destroyed by fire is a:""",
  "Capital receipt", ["Revenue receipt", "Revenue expenditure", "Deferred revenue receipt"],
  "Claim relating to a fixed asset is capital; for stock it is revenue.")

T('A7', """Cost of training staff to operate a newly installed machine is:""",
  "Revenue expenditure", ["Capital expenditure", "Part of the machine's cost", "Deferred revenue expenditure to be capitalised"],
  "AS 10 excludes training costs from the cost of PPE.")

T('A7', """Replacement of a worn-out roof of a factory with a similar roof (no improvement) is generally:""",
  "Revenue expenditure (repairs and maintenance)", ["Capital expenditure as it is large", "Capital loss",
   "Deferred revenue expenditure"],
  "Size doesn't decide. Restoring the existing condition is maintenance; improving capacity or life would be capital. (Under the component approach a significant separately-identified component may be capitalised with derecognition of the old one.)")

T('A7', """Interest paid on a loan taken to construct a factory, for the period AFTER the factory started production, is:""",
  "Revenue expenditure", ["Capital expenditure", "Part of the factory's cost", "Deferred revenue expenditure"],
  "AS 16 stops capitalisation when the asset is ready for use. Interest during construction is capital; after that, revenue.")

# ---------- A8 Bills ----------
T('A8', """A bill dated 15 March 2026 is payable 60 days after date. Ignoring holidays, its due date is:""",
  "17 May 2026", ["14 May 2026", "15 May 2026", "18 May 2026"],
  "Exclude the date of drawing: 16–31 Mar = 16 days, April = 30 (46), 14 days of May = 60 → 14 May; + 3 grace days = 17 May. Trap: forgetting grace days (14 May).")

T('A8', """A bill dated 29 January 2026 is payable one month after date. Its due date is:""",
  "3 March 2026", ["1 March 2026", "28 February 2026", "4 March 2026"],
  "February 2026 has no 29th, so take its last day, 28 February, + 3 days of grace = 3 March.")

T('A8', """Which instrument is NOT entitled to days of grace?""",
  "A bill payable on demand", ["A bill payable 3 months after date", "A bill payable 60 days after sight",
   "A promissory note payable 90 days after date"],
  "Days of grace apply only to instruments payable after a fixed period, not to demand or sight instruments or cheques.")

T('A8', """A bill that the drawer had ENDORSED to his creditor Ram is dishonoured. In the drawer's books:""",
  "Debit the acceptor (drawee); credit Ram", ["Debit the acceptor; credit Bills Receivable", "Debit the acceptor; credit Bank",
   "Debit Ram; credit the acceptor"],
  "Trap: crediting B/R. The bill left the drawer's B/R account on endorsement; Ram now has a claim back on the drawer, who in turn charges the acceptor.")

T('A8', """Rebate allowed on a bill retired before maturity is, for the holder (drawer):""",
  "An expense (loss)", ["An income", "A capital receipt", "Added to the bill's value"],
  "The holder accepts less than face value for early payment: loss for the holder, income for the acceptor.")

T('A8', """When a drawer discounts a bill with the bank, the discount is:""",
  "A finance cost debited to Discount A/c; sales are not affected", ["Deducted from Sales A/c", "Credited to Discount A/c as income",
   "Added to the cost of goods sold"],
  "The sale was recorded when goods were sold; discounting is a financing act, so the discount is a finance cost.")

T('A8', """Which statement about an accommodation bill is correct?""",
  "It is drawn and accepted without consideration to help raise funds",
  ["It always arises from a genuine sale of goods", "It cannot be discounted with any bank", "It is void and unenforceable by anyone"],
  "No trade behind it; but a holder in due course for value can enforce it. Banks avoid it as it is not self-liquidating.")

T('A8', """In the drawee's books, acceptance of a bill drawn by a creditor is recorded as:""",
  "Creditor A/c Dr; To Bills Payable A/c", ["Bills Payable A/c Dr; To Creditor A/c", "Bills Receivable A/c Dr; To Creditor A/c",
   "Purchases A/c Dr; To Bills Payable A/c"],
  "The debt to the creditor is replaced by a bill payable (liability).")

# ---------- A9 Audit & back office ----------
T('A9', """Which audit in banks is carried out at or near the time of the transaction?""",
  "Concurrent audit", ["Statutory audit", "RBI inspection", "Long Form Audit Report"],
  "Concurrent audit is the continuous, early-warning part of internal audit. Statutory audit is year-end; RBI inspects periodically; LFAR is a statutory auditor's report.")

T('A9', """Approval of a bank's statutory auditors by RBI is under which section of the BR Act?""",
  "Section 30", ["Section 29", "Section 35", "Section 17"],
  "Sec 29 = accounts format; Sec 30 = audit; Sec 35 = inspection; Sec 17 = reserve fund.")

T('A9', """In bank inter-branch accounts, which balances are the main risk?""",
  "Long-pending unreconciled DEBIT entries", ["Long-pending unreconciled credit entries", "Entries reconciled within a week",
   "Entries originated by the head office"],
  "Old unmatched debits can hide frauds or losses; RBI requires 100% provision on net debits outstanding over one year.")

T('A9', """The Long Form Audit Report is submitted by:""",
  "Statutory central and branch auditors", ["Concurrent auditors", "RBI inspection team", "Internal inspectors of the bank"],
  "LFAR accompanies the statutory audit report.")

T('A9', """Risk-Based Internal Audit means:""",
  "Audit frequency and depth depend on the assessed risk of each unit", ["Every branch is audited every month",
   "Only loss-making branches are audited", "Audit is replaced by branch self-certification"],
  "RBIA concentrates audit effort on high-risk branches and activities.")

T('A9', """In treasury, confirmation and settlement of deals are done by the:""",
  "Back office", ["Front office (dealers)", "Mid office", "Branch manager"],
  "Dealers deal (front), mid office monitors risk and limits, back office confirms, settles and accounts: separation of duties.")
