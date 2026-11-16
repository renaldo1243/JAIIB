from qb import T

# ---------- B1 Final accounts ----------
T('B1', """Opening stock ₹20,000; purchases ₹80,000; wages ₹6,000; freight inward ₹4,000; freight outward ₹3,000; sales ₹1,50,000; sales returns ₹10,000; closing stock ₹25,000. Gross profit is:""",
  "₹55,000", ["₹52,000", "₹65,000", "₹45,000"],
  "COGS = 20 + 80 + 6 + 4 − 25 = 85 (thousand). Net sales = 140. GP = 55. Traps: putting freight outward in COGS (52) or ignoring returns (65).")

T('B1', """Debtors ₹60,000; further bad debts ₹1,000; provision 5% on debtors; old provision ₹2,000; bad debts in TB ₹1,200. Debtors shown in the Balance Sheet:""",
  "₹56,050", ["₹57,000", "₹55,100", "₹59,000"],
  "Good debtors = 59,000; provision 5% = 2,950; net = 56,050. (P&L charge = 1,200 + 1,000 + 2,950 − 2,000 = 3,150.)")

T('B1', """Insurance of ₹24,000 paid on 1 January for one year; year ends 31 March. The Balance Sheet shows prepaid insurance of:""",
  "₹18,000", ["₹6,000", "₹24,000", "₹12,000"],
  "Only Jan–Mar (3 months = ₹6,000) is this year's expense; 9 months (₹18,000) is prepaid. Trap: showing the expired part as prepaid.")

T('B1', """Carriage outward is shown in the:""",
  "Profit & Loss Account (debit side)", ["Trading Account (debit side)", "Balance Sheet as an asset", "Trading Account (credit side)"],
  "Carriage outward is a selling expense; carriage inward is a direct expense for the Trading A/c.")

T('B1', """Goods costing ₹10,000 taken by the proprietor for personal use are:""",
  "Deducted from purchases and added to drawings", ["Added to sales", "Ignored, as they are the owner's own goods",
   "Added to closing stock"],
  "Entry: Drawings Dr; To Purchases (at cost).")

T('B1', """Interest on a partner's LOAN to the firm is:""",
  "Debited to the Profit & Loss Account as a charge", ["Debited to the P&L Appropriation Account", "Credited to the partner's capital as profit share",
   "Ignored if the firm makes a loss"],
  "A partner's loan is like an outsider's loan; its interest is a charge payable even in loss years. Interest on CAPITAL is an appropriation.")

T('B1', """Commission received in advance ₹5,000 is shown:""",
  "Deducted from income; shown as a liability", ["Added to commission in P&L and shown as an asset",
   "Only in the Balance Sheet as income", "Only in the Trading Account"],
  "Income received in advance is not yet earned: reduce the income and show the liability.")

T('B1', """Which item appears on the CREDIT side of a partnership's P&L Appropriation Account?""",
  "Interest on drawings", ["Interest on capital", "Partner's salary", "Transfer to reserve"],
  "Interest on drawings is charged to partners, so it adds to divisible profit; the others are appropriations (debits).")

T('B1', """Stock costing ₹40,000 was lost in fire; the insurance claim was admitted for ₹25,000 (not yet received). In the final accounts:""",
  "Trading Cr ₹40,000; P&L Dr ₹15,000; claim ₹25,000 an asset",
  ["Only ₹15,000 is debited to the Trading A/c", "₹40,000 debited to P&L and nothing else recorded", "Closing stock increased by ₹25,000"],
  "The loss of goods is removed from Trading at cost; the uninsured loss is in P&L; the claim is a receivable.")

T('B1', """Accrued interest on investments ₹3,000 is shown:""",
  "Added to income; shown as a current asset", ["Deducted from interest income in P&L", "As a liability",
   "Only in a note to accounts"],
  "Income earned but not received: add to income and show as receivable.")

T('B1', """Gross profit is 20% on COST. Sales are ₹1,20,000. Gross profit is:""",
  "₹20,000", ["₹24,000", "₹30,000", "₹16,000"],
  "20% on cost = 1/6 on sales: 1,20,000 × 1/6 = 20,000 (cost 1,00,000). Trap: 20% of sales (24,000).")

T('B1', """Closing stock appears in the Trading Account and Balance Sheet. When it also appears INSIDE the Trial Balance it is shown:""",
  "Only in the Balance Sheet", ["Only in the Trading Account", "In both the Trading Account and the Balance Sheet", "In the P&L Account"],
  "If it is already in the TB (adjusted purchases), it has been accounted through purchases; it goes only to the Balance Sheet.")

# ---------- B2 Companies & share capital ----------
T('B2', """A company offered 50,000 shares; applications 80,000; applications for 10,000 rejected; rest allotted pro-rata. Mr X applied for 1,400 shares. He gets:""",
  "1,000 shares", ["875 shares", "1,120 shares", "1,400 shares"],
  "Accepted applications = 70,000 for 50,000 → 5/7. 1,400 × 5/7 = 1,000. Trap: ratio 50/80 gives 875.")

T('B2', """500 shares of ₹10 (issued at par): application ₹3, allotment ₹4, call ₹3. Holder paid application and allotment; shares forfeited. Entry:""",
  "Share Capital Dr 5,000; To Calls 1,500; To Forfeiture 3,500",
  ["Share Capital Dr ₹3,500; To Share Forfeiture ₹3,500", "Share Capital Dr ₹5,000; To Share Forfeiture ₹5,000",
   "Share Forfeiture Dr ₹3,500; To Share Capital ₹3,500"],
  "Debit Share Capital with called-up ₹10 × 500; credit unpaid call; credit forfeiture with the amount received (₹7 × 500).")

T('B2', """Those 500 forfeited shares (forfeiture ₹3,500) are reissued at ₹6 per share fully paid. Capital Reserve:""",
  "₹1,500", ["₹3,500", "₹2,000", "Nil"],
  "Discount on reissue = ₹4 × 500 = 2,000, adjusted against forfeiture; balance 3,500 − 2,000 = 1,500 → Capital Reserve.")

T('B2', """Shares can be issued at a discount under the Companies Act, 2013:""",
  "Only as sweat equity; otherwise void", ["Freely, with a special resolution",
   "Up to 10% discount with RBI approval", "Never, not even as sweat equity"],
  "Sec 53 prohibits issue at a discount except sweat equity (Sec 54).")

T('B2', """Interest payable on calls-in-advance (Table F default) is up to:""",
  "12% p.a.", ["10% p.a.", "6% p.a.", "18% p.a."],
  "Table F: interest on calls in arrears up to 10%; on calls in advance up to 12%.")

T('B2', """Preference shareholders get voting rights on ALL resolutions when:""",
  "Their dividend is unpaid for 2 years or more", ["The company makes a loss in any year",
   "They hold more than 10% of total capital", "The company issues bonus shares"],
  "Otherwise they vote only on matters affecting their rights.")

T('B2', """A government company is one in which the government holds at least:""",
  "51% of the paid-up share capital", ["26% of the paid-up share capital", "74% of the paid-up share capital", "100% of the share capital"],
  "Sec 2(45): not less than 51% held by Central and/or State Governments.")

T('B2', """'Subscribed capital' is that part of issued capital which:""",
  "Has been taken up by the public", ["Has been called up by the company", "Has been paid up by shareholders",
   "Is mentioned in the Memorandum as the maximum"],
  "Authorised (maximum) → issued (offered) → subscribed (taken up) → called-up → paid-up.")

# ---------- B3 Schedule III, EPS, deferred tax ----------
T('B3', """PAT ₹60 lakh; 10 lakh equity shares; bonus 1 : 4 issued during the year. Basic EPS reported for the year is:""",
  "₹4.80", ["₹6.00", "₹5.33", "₹4.00"],
  "Bonus shares are treated as outstanding from the beginning: 12.5 lakh shares → 60/12.5 = ₹4.80 (and last year's EPS is restated). Trap: weighting bonus shares from issue date.")

T('B3', """Rights issue 1 for 3 at ₹120; market price before the issue ₹200. The theoretical ex-rights price is:""",
  "₹180", ["₹160", "₹200", "₹140"],
  "(3 × 200 + 120)/4 = 720/4 = ₹180.")

T('B3', """Tax depreciation exceeds book depreciation by ₹20 lakh this year; tax rate 25%. Deferred tax:""",
  "Liability of ₹5 lakh", ["Asset of ₹5 lakh", "Liability of ₹20 lakh", "Nil, as depreciation is a non-cash item"],
  "Higher tax deduction now → lower tax now, more later → DTL = 20 × 25% = ₹5 lakh.")

T('B3', """A penalty of ₹2 lakh paid for violating pollution law is disallowed for tax. Deferred tax on it is:""",
  "Nil, because it is a permanent difference", ["A deferred tax asset", "A deferred tax liability",
   "Recognised only when the penalty is reversed"],
  "Permanent differences never reverse, so no deferred tax.")

T('B3', """Which reserve CAN be used for issuing fully paid bonus shares?""",
  "Capital Redemption Reserve", ["Revaluation Reserve", "Reserve created on revaluation of land", "Provision for doubtful debts"],
  "Sec 63: free reserves, securities premium and CRR. Revaluation reserve is barred; a provision is not a reserve.")

T('B3', """In Schedule III, a security deposit recoverable after three years is shown under:""",
  "Non-current assets", ["Current assets", "Cash and cash equivalents",
   "Current investments"],
  "Realisable after 12 months → non-current.")

T('B3', """Diluted EPS is lower than basic EPS when convertible debentures exist because:""",
  "Potential shares rise more than the earnings added back",
  ["Only the number of shares is adjusted, never earnings", "Diluted EPS ignores convertible instruments",
   "Interest on debentures is deducted twice"],
  "Both numerator and denominator are adjusted; the instrument is dilutive when the incremental EPS is below basic EPS.")

T('B3', """Which document is part of a company's 'financial statements' under Sec 2(40)?""",
  "Statement of changes in equity", ["Directors' Report", "Auditor's Report", "Notice of AGM"],
  "Balance sheet, P&L, cash flow statement, SOCE (if applicable) and notes.")

# ---------- B4 Cash flow ----------
T('B4', """NPBT ₹25 lakh; depreciation ₹5 lakh; profit on sale of asset ₹2 lakh; decrease in inventory ₹3 lakh; increase in debtors ₹4 lakh; increase in creditors ₹6 lakh; tax paid ₹1.5 lakh. Net cash from operating activities:""",
  "₹31.5 lakh", ["₹35.5 lakh", "₹33.5 lakh", "₹27.5 lakh"],
  "25 + 5 − 2 + 3 − 4 + 6 = 33 cash generated; − 1.5 tax = 31.5. Trap: forgetting tax paid (33.0) or reversing signs.")

T('B4', """Purchase of machinery ₹12 lakh; sale of old machinery ₹3 lakh; interest received on investments ₹0.5 lakh (non-financial company). Net cash from investing activities:""",
  "−₹8.5 lakh", ["−₹9 lakh", "−₹12 lakh", "−₹15.5 lakh"],
  "−12 + 3 + 0.5 = −8.5. Interest received is investing for a non-financial company. Trap: leaving it out (−9).")

T('B4', """Dividend PAID by a manufacturing company is classified as:""",
  "Financing activity", ["Operating activity", "Investing activity", "Not shown in the cash flow statement"],
  "Payments to owners are financing. Dividend RECEIVED is investing.")

T('B4', """A company issues shares to a vendor in exchange for land. In the cash flow statement this is:""",
  "Excluded, but disclosed as a non-cash transaction", ["Investing outflow and financing inflow", "Operating activity",
   "Shown as a financing inflow only"],
  "No cash moves, so it is not in the statement.")

T('B4', """Bank overdraft repayable on demand that forms an integral part of cash management is:""",
  "Included in cash and cash equivalents", ["Always shown as a financing inflow",
   "Shown as an investing activity", "Ignored completely"],
  "AS 3 allows such overdrafts to be included in cash and cash equivalents.")

T('B4', """Income tax paid that cannot be specifically identified with investing or financing is classified as:""",
  "Operating activity", ["Financing activity", "Investing activity", "Extraordinary item"],
  "Taxes on income are operating unless specifically identified otherwise.")

T('B4', """Under the indirect method, 'loss on sale of machinery' is:""",
  "Added back to net profit", ["Deducted from net profit", "Shown as an operating outflow", "Ignored"],
  "The loss reduced profit but is not an operating cash outflow; the sale proceeds appear under investing.")

T('B4', """A 6-month fixed deposit with a bank, made at the start of the year, is:""",
  "Not a cash equivalent (over 3 months)", ["A cash equivalent because it is with a bank",
   "Cash on hand", "An operating activity"],
  "Cash equivalents generally mature within three months of acquisition.")

T('B4', """For a bank, dividend received on investments is classified as:""",
  "Operating activity", ["Investing activity", "Financing activity", "Not shown"],
  "For financial enterprises, interest and dividend received are operating.")

T('B4', """Which statement is correct?""",
  "A profitable company can have negative operating cash flow",
  ["Net profit always equals operating cash flow", "Depreciation is a cash inflow",
   "Increase in creditors reduces operating cash flow"],
  "Credit sales, rising stock and receivables can absorb cash despite profits.")

# ---------- B5 Bank final accounts ----------
T('B5', """A loan of ₹20 lakh, doubtful for 4 years (D3), has realisable security of ₹12 lakh. Provision required:""",
  "₹20 lakh", ["₹8 lakh", "₹12.8 lakh", "₹14 lakh"],
  "D3 (over 3 years in doubtful): 100% of the secured portion + 100% of the unsecured portion = whole outstanding.")

T('B5', """A loan of ₹10 lakh has been a sub-standard asset for 8 months (secured). Provision:""",
  "15% = ₹1.5 lakh", ["25% = ₹2.5 lakh", "100% = ₹10 lakh", "0.40% = ₹4,000"],
  "Sub-standard (NPA up to 12 months) = 15%; unsecured exposure 25%; standard 0.40%.")

T('B5', """'Guarantees given on behalf of constituents' appear in a bank's:""",
  "Contingent liabilities (Schedule 12)", ["Other liabilities and provisions (Schedule 5)", "Borrowings (Schedule 4)",
   "Advances (Schedule 9)"],
  "Guarantees, LCs, acceptances and forward contracts are contingent liabilities.")

T('B5', """Commission earned on letters of credit is shown under:""",
  "Other income (Schedule 14)", ["Interest earned (Schedule 13)", "Interest expended (Schedule 15)", "Operating expenses (Schedule 16)"],
  "Commission, exchange and brokerage are other income; interest/discount on advances and bills is interest earned.")

T('B5', """Balance held by the bank in its current account with another bank is shown in:""",
  "Schedule 7 – Balances with banks", ["Schedule 6 – Cash and balances with RBI",
   "Schedule 8 – Investments", "Schedule 9 – Advances"],
  "Balances with RBI → Sch 6; with other banks → Sch 7.")

T('B5', """Non-banking assets acquired in satisfaction of claims are shown under:""",
  "Other assets (Schedule 11)", ["Fixed assets (Schedule 10)", "Advances (Schedule 9)", "Investments (Schedule 8)"],
  "They are listed as a separate item under Other Assets.")

T('B5', """Printing and stationery expenses of a bank appear in:""",
  "Operating expenses (Schedule 16)", ["Other liabilities (Schedule 5)", "Interest expended (Schedule 15)", "Provisions and contingencies"],
  "Schedule 16 includes rent, taxes and lighting, printing and stationery, advertisement, depreciation etc.")

T('B5', """Under Section 17 of the BR Act, and RBI's stricter rule, a scheduled commercial bank transfers to reserve fund at least:""",
  "25% of profit (law minimum 20%)", ["10% of profit", "50% of profit", "20% only, as RBI has no separate rule"],
  "BR Act Sec 17 says 20%; RBI requires 25% for SCBs.")

T('B5', """Bills sent by customers to the bank for collection are shown:""",
  "Below the balance sheet as a memo item", ["As advances", "As contingent liabilities", "As other liabilities"],
  "The bank is only an agent; no asset or liability arises.")

T('B5', """Interest on an NPA account that has been charged but not realised is:""",
  "Not taken to income until realised", ["Taken to income on accrual basis", "Taken to income if security is adequate",
   "Credited to the statutory reserve"],
  "Income recognition norms: income on NPAs is booked on realisation only.")

# ---------- B6 Computerised accounting ----------
T('B6', """Which error can STILL occur in computerised accounting?""",
  "Entering a transaction with a wrong amount or wrong account", ["Wrong totalling of the ledger", "Posting to the wrong side automatically",
   "Trial balance not tallying because of a posting mistake"],
  "Software posts and totals correctly; data-entry errors and errors of principle remain.")

T('B6', """A speedometer showing continuously varying speed works on the principle of a:""",
  "Analog computer", ["Digital computer", "Mainframe computer", "Supercomputer"],
  "Continuous physical quantities = analog.")

T('B6', """Interest application for all savings accounts at month-end in a single run is an example of:""",
  "Batch processing", ["Online real-time processing", "Distributed processing by branches", "Manual processing"],
  "Transactions collected and processed together = batch.")

T('B6', """In CBS, 'anywhere banking' is possible mainly because:""",
  "All branches access a centralised database at the data centre", ["Each branch keeps a full copy of all customer data",
   "Customers carry their passbooks to every branch", "Branches exchange data by courier daily"],
  "Centralisation makes the customer the bank's, not the branch's.")

T('B6', """A neo bank in India can:""",
  "Offer digital banking services through a partner licensed bank", ["Accept public deposits on its own licence automatically",
   "Maintain CRR/SLR directly with RBI", "Issue currency through digital wallets"],
  "Neo banks have no banking licence of their own; the partner bank does the regulated activities.")

T('B6', """'Maker–checker' in bank systems means:""",
  "One person enters; another verifies and authorises",
  ["The same officer enters and authorises to save time", "The customer checks every entry", "The auditor makes all entries"],
  "Dual control prevents unauthorised or erroneous entries.")
