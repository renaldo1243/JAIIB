from qb import S

# ===================== A1 Accounting Standards =====================
S('A1', """Kaveri Textiles Ltd. closes its books on 31 March 2026; the Board approves the accounts on 22 May 2026. Between these dates:
1. A major customer owing ₹3.5 crore is admitted into insolvency on 12 April; its losses had been mounting since November 2025.
2. A court finalises damages of ₹1.2 crore in a suit filed against the company in 2024.
3. A flood on 2 May destroys raw material worth ₹80 lakh.
4. The Board proposes a final dividend of ₹2 per share on 22 May.
The Finance Manager adjusts all four events in the 2025-26 accounts, arguing that "anything known before approval must be adjusted". Which treatment is technically correct under AS 4?""",
  "Adjust events 1 and 2; disclose event 3 if material; event 4 is disclosed and not recognised as a liability",
  ["Adjust all four, since every event occurred before the Board approved the accounts",
   "Adjust events 1, 2 and 4; ignore event 3 since it relates to the next year",
   "Adjust only event 2, since only a court decree gives conclusive evidence"],
  "AS 4 distinguishes adjusting events (more evidence of conditions existing at the balance sheet date: the customer's insolvency rooted in losses since November, and settlement of a suit already pending) from non-adjusting events (the flood, a new condition). A dividend proposed after the balance sheet date is not a liability at that date; it is disclosed.")

S('A1', """Metro Infra Ltd. has a fixed-price flyover contract:
• Contract price: ₹220 crore
• Estimated total cost: ₹180 crore
• Cost incurred till 31 March: ₹72 crore (stage of completion measured by cost)
• Outcome can be estimated reliably
The Project Accountant wants to show no revenue until the final bill is raised. Applying AS 7, what revenue and profit should be recognised this year?""",
  "Revenue ₹88 crore and profit ₹16 crore, by reference to 40% completion",
  ["Nil revenue and nil profit until completion, as no bill has been raised",
   "Revenue ₹72 crore and nil profit, recognising revenue only to the extent of cost",
   "Revenue ₹88 crore and profit ₹40 crore, as total expected profit is assured"],
  "Stage of completion = 72/180 = 40%. Revenue = 40% × 220 = ₹88 crore; profit = 88 − 72 = ₹16 crore (40% of the expected ₹40 crore). Recognising revenue only up to cost applies when the outcome CANNOT be estimated reliably.")

S('A1', """GreenPower Equipments installed pollution-control machinery costing ₹12 crore (life 10 years). The State Government sanctioned a capital subsidy of ₹3 crore specifically for this machinery, received after commissioning. Separately, it received ₹2 crore under a scheme computed as 10% of total project investment, with no repayment obligation. The executive credits ₹5 crore to Other Income. Which treatment is most appropriate under AS 12?""",
  "₹3 crore: deduct from the machinery cost or treat as deferred income over 10 years; ₹2 crore: credit to capital reserve as promoters' contribution",
  ["Credit the entire ₹5 crore to Other Income because cash has been received this year",
   "Credit the entire ₹5 crore to capital reserve because both grants are capital receipts",
   "₹3 crore to capital reserve; ₹2 crore to Other Income because it is not linked to any asset"],
  "A grant tied to a depreciable asset is matched with depreciation (deduction from cost or deferred income). A grant in the nature of promoters' contribution, linked to total investment and not repayable, is credited to capital reserve as part of shareholders' funds.")

S('A1', """Alpha Biotech incurs, while developing a new drug:
• Laboratory research on molecules – ₹6 crore
• Development after technical feasibility, intention, resources and market are established – ₹9 crore
• Patent registration fees – ₹40 lakh
• Pre-launch advertising – ₹2 crore
• Training of medical representatives – ₹60 lakh
The Finance Manager proposes capitalising ₹18 crore "because every rupee builds future profit". What amount does AS 26 allow to be recognised as an intangible asset?""",
  "₹9.40 crore", ["₹18 crore", "₹15.40 crore", "₹11.40 crore"],
  "Research (₹6 crore), advertising (₹2 crore) and training (₹0.6 crore) are always expensed under AS 26. Qualifying development cost (₹9 crore) plus directly attributable patent fees (₹0.4 crore) = ₹9.40 crore.")

S('A1', """Orion Ltd. holds: (a) shares of a listed company bought 2 months ago to sell within the year, cost ₹50 lakh, market value ₹44 lakh; (b) shares of a supplier held for 5 years as a strategic long-term investment, cost ₹80 lakh, market value ₹74 lakh owing to a temporary market correction. The accountant writes down both to market value. Which is correct under AS 13?""",
  "Write down (a) to ₹44 lakh; keep (b) at ₹80 lakh, as its fall is temporary",
  ["Write down both, since all investments must be shown at market value",
   "Keep both at cost, since no investment has been sold during the year",
   "Keep (a) at cost and write down (b), since long-term holdings carry more risk"],
  "Current investments: lower of cost and fair value. Long-term investments: cost, less provision only for a decline other than temporary.")

S('A1', """Vardhan Ltd. and its related entities had the following transactions:
1. Sales to its wholly owned subsidiary.
2. Interest-free loan to the Managing Director's spouse.
3. Rent paid to a firm in which a director is a partner.
4. Purchases from Delta Ltd., which merely has one director in common with Vardhan.
The Finance Manager proposes to disclose only item 1. Which items require disclosure under AS 18?""",
  "1, 2 and 3 only", ["1 only", "1, 2, 3 and 4", "1 and 4 only"],
  "Subsidiaries, relatives of KMP and enterprises in which a director has significant influence (as partner) are related parties; disclosure is needed even if no price (interest) is charged. A common director alone does not make Delta a related party.")

S('A1', """Sterling Ltd. revises the estimated useful life of its plant from 12 to 8 years after a technical report, and separately discovers that depreciation of ₹40 lakh was omitted in last year's accounts due to a clerical mistake. The CFO wants to treat both as prior period items. Which statement correctly applies AS 5?""",
  "The life revision is a change in estimate (prospective); only the omitted ₹40 lakh is a prior period item",
  ["Both are prior period items and must be shown separately in the current P&L",
   "Both are changes in accounting estimate applied from the current year onwards",
   "The life revision is a change in accounting policy requiring retrospective restatement"],
  "Prior period items arise from errors or omissions in earlier years' accounts. A revised useful life is a new estimate, applied prospectively.")

S('A1', """An Indian company imported machinery for USD 2,00,000 when the rate was ₹82; the supplier is still unpaid at year-end when the rate is ₹84. It also holds an export receivable of USD 50,000 booked at ₹83. Under AS 11, what is the net exchange difference recognised in the P&L for the year?""",
  "Net loss of ₹3,50,000", ["Net loss of ₹4,00,000", "Net gain of ₹50,000", "No exchange difference, since both items are recorded at historical rates"],
  "Monetary items are restated at the closing rate. Payable: 2,00,000 × (84 − 82) = ₹4,00,000 loss. Receivable: 50,000 × (84 − 83) = ₹50,000 gain. Net loss ₹3,50,000, charged to P&L.")

S('A1', """Consider these statements on Indian Accounting Standards:
1. Ind AS are notified by the Central Government under the Companies Act after recommendation of NFRA.
2. Scheduled commercial banks follow Ind AS from FY 2018-19 under RBI directions.
3. A company that has adopted Ind AS cannot revert to the earlier AS.
4. US GAAP permits LIFO for inventory, whereas IFRS and Ind AS do not.
Which are correct?""",
  "1, 3 and 4 only", ["1, 2, 3 and 4", "2 and 4 only", "1 and 3 only"],
  "RBI has deferred Ind AS for scheduled commercial banks until further notice (2 wrong). The rest are correct.")

S('A1', """Under AS 28, Nova Ltd.'s plant has a carrying amount of ₹90 lakh. Its net selling price is ₹62 lakh and the present value of future cash flows from continued use is ₹74 lakh. The Finance Manager books an impairment loss of ₹28 lakh "on a prudent basis". Which is correct?""",
  "Impairment loss is ₹16 lakh, because recoverable amount is the higher figure of ₹74 lakh",
  ["Impairment loss is ₹28 lakh, because prudence requires the lower figure",
   "No impairment is needed, because value in use is positive",
   "Impairment loss is ₹22 lakh, being the average of the two shortfalls"],
  "Recoverable amount = higher of net selling price and value in use = ₹74 lakh. Impairment = 90 − 74 = ₹16 lakh.")

S('A1', """Ganga Ltd. borrowed ₹50 crore on 1 April specifically to build a new plant (expected to take 20 months). Work stopped for 4 months due to a dispute with the contractor; the plant was substantially ready on 31 January the following year but production began only on 1 April. The accountant capitalises all interest up to 1 April. Which is correct under AS 16?""",
  "Interest for the dispute period and for the period after the plant was substantially ready must be expensed",
  ["All interest till production begins is capitalised, since the plant was not producing",
   "No interest can be capitalised, since the plant was financed by a loan",
   "Interest is capitalised only for the dispute period, since work was interrupted"],
  "Capitalisation is suspended during extended interruption of active development and ceases when the asset is substantially ready for its intended use, even if production starts later.")

S('A1', """ABC India Pvt. Ltd. buys components from its UK parent at prices 25% above those charged by unrelated suppliers, cutting Indian taxable profit. The CFO argues group policy is binding and customs authorities have already accepted the invoice value. Which statement is correct?""",
  "The Transfer Pricing Officer can adjust income to the arm's length price; neither group policy nor customs valuation binds the income-tax authorities",
  ["Group policy prevails because the parent and subsidiary are under common control",
   "Customs acceptance automatically fixes the value for income-tax purposes",
   "Transfer pricing applies only to transactions between two Indian companies"],
  "Sections 92–92F require international transactions between associated enterprises to be at arm's length price (CUP, resale price, cost plus, profit split, TNMM).")

# ===================== A2 Concepts & equation =====================
S('A2', """Mr Raj, a sole proprietor, during the year:
• Paid his personal life-insurance premium from the business bank account.
• Brought office furniture worth ₹60,000 from home for the shop.
• Withdrew ₹15 lakh to build his residence.
• Paid business loan instalments from the business account.
The accountant books the first and third items as business expenses because "the owner and the business are one in law". Which concept is violated and what is the correct effect?""",
  "Business entity concept; the premium and the withdrawal are drawings, while the furniture increases capital",
  ["Going concern concept; all four items are business expenses of the year",
   "Money measurement concept; the furniture brought from home is not recorded at all",
   "Matching concept; the premium is a prepaid expense of the business"],
  "Accounting treats the business as separate from the owner. Personal payments are drawings (reduce capital); assets the owner brings in add to capital.")

S('A2', """A consulting firm on cash basis reports March profit of ₹2.4 lakh. It has:
• Fees earned in March but unpaid – ₹1.6 lakh
• April rent paid in March – ₹40,000
• March electricity unpaid – ₹15,000
• Advance received in March for April work – ₹50,000 (included in cash receipts)
What would March profit be under accrual accounting?""",
  "₹3.75 lakh", ["₹4.75 lakh", ["₹2.85 lakh"][0], "₹4.25 lakh"],
  "Accrual: 2.40 + 1.60 (fees earned) + 0.40 (April rent removed) − 0.15 (electricity) − 0.50 (advance not earned) = ₹3.75 lakh.")

S('A2', """The Finance Manager states: "Whenever a company earns profit, its liabilities must increase because the profit belongs to someone." The Chief Accountant examines profit that is (i) retained, (ii) declared as dividend, (iii) used to repay a bank loan, (iv) invested in machinery. Which statement is sound?""",
  "Profit first raises owners' equity; it creates a liability only when a dividend is declared and reduces liabilities if used to repay debt",
  ["Profit always increases liabilities because it is owed to shareholders",
   "Profit always reduces liabilities because it is used to repay creditors",
   "Profit affects only the Statement of Profit and Loss and never the Balance Sheet"],
  "Retained profit sits in reserves (equity). Declaring dividend moves it to a liability; repaying a loan reduces liabilities; buying machinery changes only the asset mix.")

S('A2', """Consider these statements about accounting concepts:
1. Showing assets at cost less depreciation rather than at forced-sale value rests on the going concern assumption.
2. Recording a building at ₹50 lakh though its market value is ₹80 lakh reflects conservatism.
3. Treating capital as a liability of the business reflects the business entity concept.
4. Expensing a ₹400 calculator that lasts 3 years reflects materiality.
Which are correct?""",
  "1, 3 and 4 only", ["1, 2, 3 and 4", "2 and 4 only", "1 and 2 only"],
  "Keeping a fixed asset at cost despite a higher market value is the cost concept (supported by going concern), not conservatism. The others are correct.")

S('A2', """A business shows: Cash ₹60,000; Debtors ₹1,40,000; Stock ₹2,00,000; Machinery ₹4,00,000; Prepaid insurance ₹20,000; Creditors ₹1,80,000; Bank overdraft ₹70,000; Outstanding wages ₹30,000; Long-term loan ₹2,00,000. During the year the owner introduced ₹1,00,000 and withdrew ₹60,000; opening capital was ₹2,40,000. What was the profit for the year?""",
  "₹60,000", ["₹1,60,000", "₹1,00,000", "₹2,00,000"],
  "Assets = 8,20,000; liabilities = 4,80,000; closing capital = 3,40,000. Profit = Closing − Opening − Fresh capital + Drawings = 3,40,000 − 2,40,000 − 1,00,000 + 60,000 = ₹60,000. Traps: forgetting fresh capital (1,60,000) or ignoring drawings.")

S('A2', """At year-end, Delta Traders values closing stock (cost ₹9 lakh, NRV ₹7.5 lakh) at ₹7.5 lakh, creates a 5% provision for doubtful debts, but refuses to create a provision for discount on creditors. A partner objects that the treatment is "inconsistent". Which explanation is correct?""",
  "All three follow conservatism: anticipate losses, but do not anticipate gains",
  ["The discount on creditors must also be provided for, to be consistent",
   "Stock should be at cost, as the cost concept overrides conservatism",
   "Provision for doubtful debts violates the accrual concept"],
  "Prudence provides for probable losses (stock below cost, doubtful debts) but does not recognise expected gains (discount from creditors).")

S('A2', """A company converts ₹50 lakh of its equity share capital into a long-term loan from the promoter, and on the same day repays a ₹20 lakh bank loan in cash. What is the combined effect on the accounting equation?""",
  "Assets −₹20 lakh; liabilities +₹30 lakh; capital −₹50 lakh", ["Assets −₹20 lakh; liabilities −₹20 lakh; capital unchanged",
   "Assets unchanged; liabilities +₹50 lakh; capital −₹50 lakh", "Assets +₹30 lakh; liabilities +₹30 lakh; capital unchanged"],
  "Conversion: liabilities +50, capital −50, assets unchanged. Repayment: assets −20, liabilities −20. Net: assets −20, liabilities +30, capital −50.")

S('A2', """Under AS 1, which statement is correct?""",
  "Going concern, consistency and accrual are fundamental assumptions; disclosure is needed only if they are not followed",
  ["Prudence, substance over form and materiality are fundamental assumptions that must always be disclosed",
   "Every accounting policy must be disclosed only when it differs from the previous year",
   "Fundamental assumptions apply only to companies listed on a stock exchange"],
  "AS 1 names three fundamental assumptions; prudence, substance over form and materiality guide the selection of policies.")

# ===================== A3 Golden rules & journal =====================
S('A3', """Vertex Manufacturing had these transactions:
1. Purchased machinery through bank.
2. Paid installation wages for the new machine.
3. Bought lubricants for routine servicing.
4. Received an insurance claim for damage to a machine.
The Accounts Executive debits Machinery Account in all four cases, arguing "Machinery is a real account – debit what comes in". Which statement is technically correct?""",
  "Only 1 and 2 are debited to Machinery; 3 is a revenue expense and 4 debits Bank and credits the claim/loss account",
  ["All four are correct, because every transaction involving machinery is a real-account debit",
   "Only 1 is correct; installation wages are always charged to Wages Account",
   "1, 2 and 3 are correct; only the insurance claim is wrongly recorded"],
  "Golden rules decide the side; capital-vs-revenue decides the account. Installation is part of cost; routine servicing is revenue; a claim received is a receipt (Dr Bank).")

S('A3', """A trainee classifies: Factory building – Real; Bank loan – Personal; Outstanding salary – Nominal; Goodwill – Nominal; Drawings – Personal; Discount allowed – Nominal. How many classifications are WRONG under the traditional approach?""",
  "Two", ["One", "Three", "Four"],
  "Outstanding salary is a representative personal account, and goodwill is an intangible real account. The other four are correct.")

S('A3', """The following independent transactions are recorded by a trainee:
1. Furniture bought on credit – Purchases A/c Dr; To Supplier.
2. Goods worth ₹8,000 (cost) taken by the proprietor – Drawings A/c Dr; To Sales A/c.
3. Free samples distributed (cost ₹5,000) – Advertisement A/c Dr; To Purchases A/c.
4. Bad debt written off last year now recovered – Cash A/c Dr; To Debtor's A/c.
Which entries are correct?""",
  "3 only", ["1 and 3 only", "2 and 3 only", "3 and 4 only"],
  "Furniture → Furniture A/c (not Purchases). Goods taken by owner → credit Purchases (not Sales). Recovery of written-off debt → credit Bad Debts Recovered (the debtor's account is closed). Only 3 is correct.")

S('A3', """A shop keeps a petty-cash float of ₹10,000 on the imprest system. This week the petty cashier spent ₹2,400 on postage, ₹3,100 on conveyance and ₹1,700 on stationery. The main cashier proposes to give him ₹10,000 'to restart the week'. Which is correct?""",
  "Reimburse ₹7,200 by debiting Petty Cash A/c, restoring the float to ₹10,000",
  ["Give ₹10,000 by debiting the three expense accounts directly",
   "Give ₹2,800, the balance left with the petty cashier",
   "Give ₹10,000 and credit the expense accounts with ₹7,200"],
  "Under the imprest system the petty cashier is reimbursed exactly the amount spent (2,400 + 3,100 + 1,700 = 7,200), so the float returns to ₹10,000.")

S('A3', """Which entry correctly records 'Goods costing ₹60,000 destroyed by fire; insurance company admits a claim of ₹45,000'?""",
  "Insurance Claim A/c Dr ₹45,000; Loss by Fire A/c Dr ₹15,000; To Purchases A/c ₹60,000",
  ["Loss by Fire A/c Dr ₹60,000; To Stock A/c ₹60,000",
   "Insurance Company A/c Dr ₹60,000; To Purchases A/c ₹60,000",
   "Cash A/c Dr ₹45,000; Loss by Fire A/c Dr ₹15,000; To Sales A/c ₹60,000"],
  "Goods lost are removed from purchases at cost; the admitted claim is a receivable and the balance is a loss. Cash is debited only when the claim is actually received.")

S('A3', """In a triple-column cash book, the accountant: (i) records ₹50,000 cash deposited into bank only in the bank column; (ii) balances the discount columns and carries forward the balances; (iii) records a trade discount of ₹2,000 in the discount column. Which of these are errors?""",
  "All three", ["(i) only", "(ii) and (iii) only", "(i) and (iii) only"],
  "A deposit of cash is a contra entry affecting both cash and bank columns; discount columns are totalled (not balanced) and posted; trade discount is never recorded.")

S('A3', """Machinery worth ₹5 lakh is bought from Vikas Ltd., which accepts 50,000 equity shares of ₹10 each in settlement. Which pair of entries is correct?""",
  "Machinery Dr; To Vikas Ltd ₹5 lakh, and then Vikas Ltd Dr; To Equity Share Capital ₹5 lakh",
  ["Machinery Dr; To Bank ₹5 lakh, and then Bank Dr; To Equity Share Capital ₹5 lakh",
   "Equity Share Capital Dr; To Machinery ₹5 lakh only",
   "Purchases Dr; To Vikas Ltd ₹5 lakh, and then Vikas Ltd Dr; To Share Capital ₹5 lakh"],
  "The asset is debited and the vendor credited; the vendor's claim is then settled by issuing shares. No cash is involved; Purchases is only for goods dealt in.")

S('A3', """Consider these statements:
1. Credit purchase of goods for resale is recorded in the Purchases Book.
2. Credit purchase of a computer for office use is recorded in the Purchases Book.
3. Goods returned to a supplier are supported by a debit note and recorded in the Purchase Returns Book.
4. Opening and rectification entries are recorded in the Journal Proper.
Which are correct?""",
  "1, 3 and 4 only", ["1, 2, 3 and 4", "1 and 2 only", "2, 3 and 4 only"],
  "The Purchases Book is only for credit purchases of goods dealt in; a computer for office use goes to the Journal Proper.")

S('A3', """Under the modern (accounting-equation) approach, a trainee lists normal balances: Drawings – Credit; Prepaid rent – Debit; Income received in advance – Debit; Provision for depreciation – Credit. Which are correctly stated?""",
  "Prepaid rent and Provision for depreciation only", ["Drawings and Prepaid rent only",
   "Income received in advance and Provision for depreciation only", "All four"],
  "Drawings reduce capital → debit balance. Income received in advance is a liability → credit balance. Prepaid rent (asset) is debit; provision for depreciation is credit.")

S('A3', """Cash ₹19,600 received from a debtor in full settlement of ₹20,000 is posted by the trainee as: Cash Dr ₹19,600; To Debtor ₹19,600. The senior says the debtor's account will show a false balance. Which correction is needed?""",
  "Discount Allowed A/c Dr ₹400; To Debtor ₹400", ["Debtor Dr ₹400; To Discount Received ₹400",
   "Discount Received A/c Dr ₹400; To Cash ₹400", "No correction, since cash received is correctly recorded"],
  "Full settlement means ₹400 was allowed as discount (a loss). The debtor must be credited with the full ₹20,000.")

# ===================== A4 Errors & suspense =====================
S('A4', """The Trial Balance of Indus Ltd. agreed. During audit:
1. A machine costing ₹12 lakh bought on 1 October on credit was entered in the Purchases Book (supplier correctly credited). Depreciation is 10% p.a. SLM.
2. Repairs of ₹2 lakh to the office were debited to Building Account.
What is the combined effect on net profit before rectification?""",
  "Profit understated by ₹9.40 lakh", ["Profit understated by ₹10 lakh", "Profit overstated by ₹2 lakh", "Profit understated by ₹11.40 lakh"],
  "Error 1: purchases overstated by 12 lakh, depreciation of 0.60 lakh (6 months) not charged → profit understated by 11.40. Error 2: repairs capitalised → profit overstated by 2.00. Net understatement = ₹9.40 lakh. Both are errors of principle, so the TB agreed.")

S('A4', """A Trial Balance did not agree and the difference was put to Suspense. Found later:
(a) Sales Book undercast by ₹12,000.
(b) Cash ₹8,000 received from Mohan posted to the debit of his account.
(c) Purchase of furniture ₹25,000 debited to Purchases.
(d) Discount received ₹1,500 posted to the debit of Discount Allowed.
The Suspense Account originally had a balance of:""",
  "₹31,000 credit", ["₹31,000 debit", "₹22,000 credit", "₹56,000 credit"],
  "Debits exceed credits by: (a) 12,000 (sales under-credited); (b) 16,000 (Mohan debited 8,000 instead of credited 8,000); (c) nil (two-sided); (d) 3,000 (debit 1,500 wrongly made, credit 1,500 missing). Total 31,000 excess debit, so Suspense is opened on the CREDIT side with ₹31,000.")

S('A4', """Which group contains ONLY errors that will NOT affect the agreement of the Trial Balance?""",
  "Error of principle; complete omission; wrong amount in the Sales Book; posting to Ram instead of Shyam (same side)",
  ["Error of principle; undercasting of Purchases Book; complete omission; compensating error",
   "Wrong balancing of Wages Account; error of principle; complete omission; compensating error",
   "Posting to the wrong side; wrong amount in the Sales Book; error of principle; complete omission"],
  "Undercasting a book, wrong balancing and posting to the wrong side are one-sided errors that disturb the TB. Principle, complete omission, wrong amount in a book of original entry and posting to a wrong account of the same class do not.")

S('A4', """Credit sale of ₹4,80,000 (cost ₹3,20,000) was completely omitted from the Sales Book; the goods left the warehouse and were excluded from closing stock; the customer confirms the balance. The Finance Manager says "net profit is unaffected because both sale and cost are missing". Which is correct?""",
  "Sales and debtors are understated by ₹4.8 lakh, so gross and net profit are understated by ₹4.8 lakh; the TB still agrees",
  ["Net profit is unaffected because sale and cost are both missing",
   "Profit is understated by only ₹1.6 lakh, the margin on the sale",
   "The TB will disagree because debtors are understated"],
  "Cost of the goods is already reflected (lower closing stock); only the sale is missing, so the whole ₹4.8 lakh is understated. Complete omission does not disturb the TB.")

S('A4', """The Audit Committee reviews four errors found after the TB agreed:
1. Purchase of machinery ₹9.8 lakh debited to Repairs.
2. Credit purchase from Rahul ₹2,10,000 entered in the Purchases Book as ₹1,20,000.
3. Goods sold to Ravi ₹15,000 posted to Ravindra's account.
4. Rent ₹6,000 paid debited to the landlord's personal account.
Which errors affect reported profit?""",
  "1, 2 and 4 only", ["1 only", "1, 2, 3 and 4", "2 and 3 only"],
  "1: expense overstated (profit understated). 2: purchases understated by 90,000 (profit overstated). 4: rent expense missing (profit overstated). 3 affects only personal accounts.")

S('A4', """An error discovered next year after the books were closed: an old machine sold for ₹40,000 (book value ₹35,000) had been credited to Sales Account. The accountant proposes 'Sales A/c Dr ₹40,000; To Machinery A/c ₹40,000' this year. The auditor disagrees. The correct rectification is:""",
  "P&L Adjustment A/c Dr ₹35,000; To Machinery A/c ₹35,000",
  ["Sales A/c Dr ₹40,000; To Machinery A/c ₹40,000, as proposed",
   "Machinery A/c Dr ₹40,000; To Suspense A/c ₹40,000",
   "No entry is needed because last year's books are closed"],
  "After closing, last year's Sales (nominal) is no longer open; its effect on profit is corrected through P&L Adjustment. Last year: Sales was credited 40,000, but only a profit of 5,000 should have reached P&L, so profit was overstated by 35,000; Machinery is still carried at its book value of 35,000. Both are corrected by one entry.")

S('A4', """Rectification entries passed through a Suspense Account at Bharat Ltd. are:
1. Suspense Dr; To Sales ₹10,000 (sales book undercast).
2. Arun Dr; To Suspense ₹6,000 (sale not posted to Arun).
3. Suspense Dr; To Purchase Returns ₹4,000 (returns book undercast).
4. Mohan Dr ₹2,000; To Suspense (wrong posting in Mohan's account).
What is the net effect on profit?""",
  "Increase of ₹14,000", ["Increase of ₹6,000", "Increase of ₹22,000", "No effect, as suspense entries only balance the TB"],
  "Only nominal accounts change profit: Sales +10,000 and Purchase Returns +4,000 → +14,000. Arun and Mohan are personal accounts.")

S('A4', """Before rectification, Sun Ltd.'s TB showed debit ₹8,45,000 and credit ₹8,62,000. The only error is that the Purchases Book was overcast. Which conclusion is correct?""",
  "Impossible: an overcast Purchases Book would make the debit total HIGHER, but here debits are lower",
  ["Purchases Book was overcast by ₹17,000", "Purchases Book was overcast by ₹8,500",
   "The suspense account should be credited with ₹17,000"],
  "Overcasting purchases inflates the debit side. Here the debit side is ₹17,000 SHORT, so the single error must reduce debits (e.g. undercasting purchases or overcasting a credit-side book).")

S('A4', """Which statement about the Suspense Account is technically correct?""",
  "It is opened only for one-sided errors, and a balance left at year-end is shown in the Balance Sheet as an other current asset or liability",
  ["It is opened for every error, including errors of principle, to reach a correct profit",
   "Every rectification through it changes the profit of the year",
   "It must always be closed before the Trial Balance is drawn up"],
  "Two-sided errors are rectified directly. Many suspense corrections touch only personal or real accounts. An unresolved balance is carried in the Balance Sheet.")

S('A4', """A credit sale of ₹4,500 was recorded in the Sales Book as ₹5,400 and posted from there. The trainee rectifies with 'Suspense Dr ₹900; To Sales ₹900'. The auditor objects. Why?""",
  "The error is two-sided (sales and the customer both overstated); rectify by Sales Dr; To Customer ₹900, with no suspense",
  ["The rectification must be for ₹1,800, double the difference", "The customer should be debited and Sales credited by ₹900",
   "The entry is correct but must be passed in the next year"],
  "An error in the book of original entry is carried to both sides, so the TB agreed and no suspense exists. Both accounts are overstated by ₹900.")

S('A4', """Year-end adjusting entries are required for which of these, even though the Trial Balance has agreed?
1. Salary for March unpaid.
2. Insurance paid for the next year.
3. Interest accrued on investments but not due.
4. Depreciation on plant.
5. A cheque from a customer received and banked on 31 March.""",
  "1, 2, 3 and 4 only", ["4 only", "1 and 4 only", "1, 2, 3, 4 and 5"],
  "Accrual accounting needs adjustments for outstanding, prepaid and accrued items and depreciation. A banked cheque is an ordinary transaction already recorded.")

# ===================== A5 BRS =====================
S('A5', """On 31 March, Sagar Traders' cash book shows a debit balance of ₹3,60,000. Analysis reveals:
• Cheques issued but not presented – ₹72,000
• Cheques deposited but not credited – ₹41,000
• Bank charges not in cash book – ₹1,800
• NEFT receipt from a customer not in cash book – ₹25,000
• A cheque issued for ₹14,600 was entered in the cash book as ₹16,400
What are the adjusted cash-book balance and the pass-book balance?""",
  "Adjusted cash book ₹3,85,000; pass book ₹4,16,000", ["Adjusted cash book ₹3,83,200; pass book ₹4,14,200",
   "Adjusted cash book ₹3,85,000; pass book ₹3,54,000", "Adjusted cash book ₹3,60,000; pass book ₹4,16,000"],
  "Adjusted CB = 3,60,000 − 1,800 + 25,000 + 1,800 (over-recorded payment written back) = 3,85,000. PB = 3,85,000 + 72,000 − 41,000 = 4,16,000.")

S('A5', """The cash book of Ravi & Co. shows an overdraft of ₹1,20,000. Cheques issued not presented ₹30,000; cheques deposited not credited ₹45,000; interest on overdraft debited by bank ₹4,500; a customer paid ₹20,000 directly into the bank. The trainee calculates the pass-book overdraft as ₹1,49,500. The correct figure is:""",
  "₹1,19,500", ["₹1,49,500", "₹1,39,500", "₹1,09,500"],
  "Treat overdraft as −1,20,000: +30,000 (unpresented) − 45,000 (uncredited) − 4,500 (interest) + 20,000 (direct deposit) = −1,19,500. The trainee reversed the signs of the unpresented cheques and direct deposit.")

S('A5', """While reconciling, Nova Enterprises finds:
1. A cheque received ₹1,80,000 recorded in the cash book as ₹18,000.
2. A dividend of ₹95,000 collected and credited by the bank.
3. A cheque of ₹42,000 issued remains unpresented.
4. The bank debited ₹12,000 belonging to another customer.
5. Insurance premium ₹48,000 paid under standing instructions.
Which items need an entry in the cash book?""",
  "1, 2 and 5 only", ["1, 2, 4 and 5 only", "2 and 5 only", "All five"],
  "Our own error (1) and bank-originated items we have not recorded (2, 5) need cash-book entries. The unpresented cheque is a timing difference; the bank's wrong debit is shown in the BRS and the bank asked to reverse it.")

S('A5', """Pass book shows a credit balance of ₹2,40,000. Cheques deposited but not credited ₹36,000; cheques issued not presented ₹58,000; bank charges ₹2,000 and interest credited ₹6,500, neither in the cash book. Balance as per cash book is:""",
  "₹2,13,500", ["₹2,66,500", "₹2,22,500", "₹2,17,500"],
  "From PB: + 36,000 (cash book already has the deposit) − 58,000 (cash book already reduced) + 2,000 (charges not yet in CB) − 6,500 (interest not yet in CB) = 2,13,500.")

S('A5', """The accountant of a firm wants to show the pass-book balance of ₹4,16,000 in the Balance Sheet "because the bank's records are independent and reliable". The adjusted cash-book balance is ₹3,85,000, with the difference due to unpresented and uncleared cheques. Which is correct?""",
  "Show ₹3,85,000, since timing differences don't change the firm's true position and the adjusted cash book reflects it",
  ["Show ₹4,16,000, since the bank's figure is more reliable", "Show the average of the two balances",
   "Show ₹3,85,000 and disclose ₹31,000 as a contingent asset"],
  "The firm's true balance is the adjusted cash-book figure; unpresented cheques are already owed to payees and uncleared cheques are already the firm's funds.")

S('A5', """Starting from a FAVOURABLE cash-book balance, which items are DEDUCTED to arrive at the pass-book balance?
1. Cheques deposited but not yet collected.
2. Interest credited by the bank.
3. A cheque received and dishonoured, not yet recorded in the cash book.
4. Payment by the bank under a standing instruction.
5. Cheques issued but not presented.""",
  "1, 3 and 4 only", ["1, 2 and 3 only", "2 and 5 only", "1, 3, 4 and 5 only"],
  "Items that make the bank balance LOWER than the cash book are deducted: uncollected deposits, unrecorded dishonour and SI payments. Interest credited and unpresented cheques make the bank balance higher.")

S('A5', """A firm's cash book shows a debit balance of ₹50,000 and its pass book an overdraft of ₹10,000 on the same date. The only differences are cheques deposited but not collected and bank charges of ₹1,500. The amount of uncollected cheques is:""",
  "₹58,500", ["₹61,500", "₹38,500", "₹48,500"],
  "From CB +50,000 to PB −10,000 is a fall of 60,000 = uncollected cheques + bank charges. Uncollected cheques = 60,000 − 1,500 = 58,500.")

S('A5', """Which statement on Bank Reconciliation is NOT correct?""",
  "Once a BRS is prepared, no entries are needed in the cash book",
  ["The pass book is a mirror image of the cash book only in the absence of timing differences and errors",
   "A BRS helps detect frauds and errors by either party",
   "Errors committed by the bank are shown in the BRS and the bank is asked to correct them"],
  "Bank-originated items and the firm's own errors must be recorded in the cash book; only timing differences and bank errors stay in the BRS.")

S('A5', """Bank's statement shows an overdraft of ₹70,000. The cash book shows a favourable balance of ₹5,000. Which single set of items could explain this, with no other differences?""",
  "Cheques deposited but not credited ₹75,000", ["Cheques issued but not presented ₹75,000",
   "Interest credited by bank ₹75,000", "Direct deposits by customers ₹75,000"],
  "The bank balance is lower by ₹75,000. Only uncredited deposits make the bank side lower; the other three make it higher.")

S('A5', """Payments of ₹6,800 (bank charges ₹800 and SI insurance ₹6,000) appear in the pass book but not in the cash book. A trainee lists them only in the BRS for three months. What is the consequence?""",
  "Bank balance in the books is overstated and expenses (charges, insurance) are understated, so profit is overstated",
  ["No consequence, since they are timing differences that will clear automatically",
   "Bank balance is understated and profit is understated",
   "Only the BRS is affected; the Balance Sheet is correct"],
  "These are real payments; until recorded in the cash book, the bank asset is overstated and expenses are understated.")

# ===================== A6 Depreciation =====================
S('A6', """Zenith Logistics buys a sorting machine: price ₹80 lakh, installation ₹4 lakh, freight ₹1 lakh, residual value ₹5 lakh, life 8 years, SLM. After 3 years a technical report revises the remaining life to 3 years and the residual value to ₹9 lakh. The Finance Executive proposes recomputing depreciation from the date of purchase. What is the correct depreciation for Year 4?""",
  "₹15.33 lakh, applying the revision prospectively", ["₹10 lakh, as the original method continues",
   "₹21.33 lakh, after recomputing and catching up past years", "₹13.33 lakh, ignoring the revised residual value"],
  "Original charge = (85 − 5)/8 = 10 lakh; carrying amount after 3 years = 55 lakh. Revised: (55 − 9)/3 = 15.33 lakh. A change in estimate is prospective; past years are not recomputed.")

S('A6', """A vehicle costing ₹32 lakh was bought on 1 April 2024; WDV 25% p.a. It is sold on 30 September 2025 for ₹22 lakh. What is the profit or loss on sale?""",
  "Profit of ₹1 lakh", ["Loss of ₹2 lakh", "Profit of ₹4 lakh", "Loss of ₹1 lakh"],
  "31-3-2025: 32 − 8 = 24 lakh. FY 25-26 for 6 months: 24 × 25% × 6/12 = 3 lakh → 21 lakh on 30-9-2025. Sale 22 − 21 = profit ₹1 lakh. Trap: charging a full year (18 lakh → profit 4).")

S('A6', """A transport company buys 500 electric buses. The technical report says: utilisation is highest in the first four years; maintenance cost rises sharply later; management wants depreciation to reflect how benefits are consumed. Which method and reasoning are most appropriate?""",
  "WDV, because higher early charges match higher early benefits and offset rising later repairs",
  ["SLM, because equal charges every year always give the fairest matching",
   "Sinking fund method, because it sets aside cash for replacement",
   "No depreciation in the first year, because the buses are new"],
  "WDV front-loads depreciation; total of depreciation plus repairs stays more even. A sinking fund provides cash, not a pattern of consumption.")

S('A6', """Machinery costs ₹50 lakh (residual ₹5 lakh) with an estimated output of 9 lakh units. Year 1 output is 2.25 lakh units. The accountant charges ₹12.5 lakh, applying 25% of cost. Which is correct?""",
  "₹11.25 lakh under the units-of-production method", ["₹12.5 lakh, as output is 25% of capacity",
   "₹5.625 lakh, being half of the units-based charge", "₹9 lakh, as under SLM over 5 years"],
  "Units method uses the depreciable amount: (50 − 5) × 2.25/9 = 11.25 lakh. Using cost ignores the residual value.")

S('A6', """Consider these statements on depreciation:
1. Depreciation begins when an asset is available for use, even if not yet used.
2. Under Schedule II, residual value is ordinarily not more than 5% of original cost.
3. A change in depreciation method is a change in accounting policy applied retrospectively.
4. Freehold land used for a factory is not depreciated.
Which are correct?""",
  "1, 2 and 4 only", ["1, 2, 3 and 4", "2 and 3 only", "1 and 4 only"],
  "Under revised AS 10, a change in depreciation method is a change in accounting estimate applied prospectively (3 wrong).")

S('A6', """Two identical machines cost ₹25 lakh each, purchased the same day. Machine A: SLM over 5 years, nil residual. Machine B: WDV at 20%. At the end of Year 3, the CFO claims B must have the lower carrying amount "because WDV always writes off more". Which is correct?""",
  "A has ₹10 lakh and B ₹12.8 lakh, so the CFO is wrong here; the comparison depends on the life and rate used",
  ["B has ₹12.8 lakh and A ₹15 lakh, so the CFO is right", "Both have ₹12.8 lakh",
   "A has ₹10 lakh and B ₹10 lakh, so they are equal"],
  "A: 5 lakh a year → 25 − 15 = 10 lakh. B: 25 × 0.8³ = 12.8 lakh. A short SLM life can write off faster than a WDV rate.")

S('A6', """ABC Ltd. has issued ₹60 crore debentures redeemable after 6 years and creates a Sinking Fund, investing a fixed sum yearly in G-secs. The CFO lists:
1. The fund spreads the burden of redemption over several years.
2. Income on the investments is added to the fund.
3. Creating the fund removes the legal obligation to redeem on maturity.
4. Its main purpose is to have cash available at redemption.
Which are correct?""",
  "1, 2 and 4 only", ["1, 2, 3 and 4", "2 and 3 only", "1 and 3 only"],
  "A sinking fund only provides money; the company must still redeem the debentures.")

S('A6', """A robotic arm costs ₹2.40 crore with an 8-year life and nil residual value. The Finance Controller says: "At the end of the useful life the carrying amount must become zero under any method." Which statement is correct?""",
  "Only SLM (with nil residual) brings it to zero; WDV always leaves a balance",
  ["Any method reduces it to zero if the residual value is nil", "WDV reaches zero faster than SLM",
   "No method can reduce the carrying amount below 5% of cost"],
  "WDV applies a fixed % to a declining balance, so it never reaches exactly zero.")

S('A6', """An asset is bought on 1 July for ₹8 lakh. The company charges WDV at 15% on a time basis and the year ends 31 March. In Year 2 the accountant charges ₹1.2 lakh. What should the Year-2 depreciation be?""",
  "₹1.065 lakh", ["₹1.20 lakh", "₹0.90 lakh", "₹1.02 lakh"],
  "Year 1 (9 months): 8 × 15% × 9/12 = 0.90 → WDV 7.10. Year 2: 7.10 × 15% = ₹1.065 lakh. The trainee's 1.20 is 15% of the original cost, which is not WDV.")

# ===================== A7 Capital vs revenue =====================
S('A7', """Neptune Cements incurs on its kiln during the year:
• Freight and installation of a new kiln – ₹14 lakh
• Routine relining and maintenance – ₹3 lakh
• Replacement of the main drive, extending life by 6 years – ₹22 lakh
• Training staff on the new kiln – ₹1.5 lakh
The Accounts Executive capitalises all ₹40.5 lakh. How much should be capitalised under AS 10?""",
  "₹36 lakh", ["₹40.5 lakh", "₹14 lakh", "₹37.5 lakh"],
  "Capitalise freight and installation (14) and the major replacement extending life (22) = 36. Routine maintenance and training are expensed.")

S('A7', """Nova Petrochem must carry out a statutory major inspection of its turbine every five years; without it the turbine cannot legally operate. This year it spent ₹2.8 crore; no part was replaced. The Accounts Manager wants to expense it "because no new asset is bought". Which treatment is most appropriate?""",
  "Capitalise it as a component if recognition criteria are met, and derecognise the balance of the previous inspection cost",
  ["Expense it fully, as inspection never increases capacity",
   "Carry it as deferred revenue expenditure and write it off over 3 years",
   "Debit it to General Reserve, since it is unusual"],
  "AS 10 recognises major inspections as part of the asset's carrying amount when they enable continued use and meet recognition criteria.")

S('A7', """A firm buys a second-hand truck for ₹9 lakh, spends ₹1.2 lakh on an engine overhaul before putting it on the road, pays ₹40,000 for registration, and later ₹15,000 on routine servicing and ₹35,000 on a new paint job after an accident. What is the truck's capitalised cost?""",
  "₹10.60 lakh", ["₹11.10 lakh", "₹10.20 lakh", "₹10.95 lakh"],
  "Purchase 9 + overhaul to make it usable 1.2 + registration 0.4 = 10.6 lakh. Later servicing and accident repairs are revenue.")

S('A7', """Which set contains ONLY capital receipts?""",
  "Issue of debentures; sale proceeds of old machinery; insurance claim for a building destroyed by fire",
  ["Sale of goods; interest received; issue of shares", "Insurance claim for stock; loan raised; rent received",
   "Bad debts recovered; sale of furniture; capital subsidy"],
  "Receipts from owners, lenders, sale of fixed assets and claims on fixed assets are capital. Claims on stock, sales, interest, rent and bad-debt recoveries are revenue.")

S('A7', """A company spends ₹1.2 crore on an advertising campaign to launch a new product, expecting benefits for three years. The CFO wants to show it as deferred revenue expenditure written off over 3 years. Which is correct under current standards?""",
  "Expense it in the year incurred, since AS 26 does not allow advertising to be carried forward",
  ["Carry ₹80 lakh forward as deferred revenue expenditure", "Capitalise it as an intangible asset (brand)",
   "Debit it to securities premium"],
  "Advertising and promotional costs are expensed when incurred; 'deferred revenue expenditure' is no longer an acceptable treatment for them.")

S('A7', """GST of ₹3.6 lakh is paid on a machine of ₹20 lakh; ITC is fully available. Basic customs duty (non-refundable) on an imported part is ₹1 lakh; a trade discount of ₹50,000 is received; site preparation costs ₹70,000. The machine's cost under AS 10 is:""",
  "₹21.20 lakh", ["₹24.80 lakh", "₹21.70 lakh", "₹20.70 lakh"],
  "20 − 0.5 (trade discount) + 1 (non-refundable duty) + 0.7 (site preparation) = 21.2 lakh. Creditable GST is excluded.")

S('A7', """Which statement about the effect of misclassification is correct?""",
  "Treating capital expenditure as revenue understates both profit and assets, creating a secret reserve",
  ["Treating capital expenditure as revenue overstates profit and assets",
   "Treating revenue expenditure as capital understates profit but overstates assets",
   "Misclassification never affects profit since the cash spent is the same"],
  "Expensing a capital item lowers profit and leaves the asset out; capitalising a revenue item does the opposite (window dressing). Both are errors of principle.")

S('A7', """Interest on a ₹30 crore loan taken to build a hotel: ₹2.4 crore for the construction period of 18 months and ₹0.8 crore for the 4 months after the hotel was ready but before it opened. The accountant capitalises ₹3.2 crore. Which is correct?""",
  "Capitalise ₹2.4 crore; expense ₹0.8 crore", ["Capitalise ₹3.2 crore", "Expense ₹3.2 crore", "Capitalise ₹0.8 crore only"],
  "Under AS 16, capitalisation stops when the asset is substantially ready for use, even if operations start later.")

# ===================== A8 Bills of exchange =====================
S('A8', """A bill drawn on 1 February 2026 is payable 90 days after sight; it is accepted on 5 February 2026. The accountant records the due date as 2 May 2026 (90 days from the date of drawing). Ignoring holidays, the correct due date is:""",
  "9 May 2026", ["2 May 2026", "5 May 2026", "6 May 2026"],
  "After-sight bills run from acceptance: 5 Feb + 90 days = 6 May; + 3 days of grace = 9 May 2026.")

S('A8', """A bill drawn on 23 November 2024 is payable two months after date. The clerk computes 23 January + 3 days = 26 January 2025. 26 January is a public holiday. When must the bill be paid?""",
  "25 January 2025, the preceding business day", ["26 January 2025, as holidays are ignored",
   "27 January 2025, the next business day", "23 January 2025, without grace days"],
  "Section 25 of the NI Act: if the maturity date is a public holiday, the instrument is payable on the preceding business day.")

S('A8', """Three companies controlled by the same promoter face a year-end cash crunch. X draws a bill on Y; Y accepts though no goods are sold; X discounts it with a bank and remits the proceeds to Y. The credit officer argues that because the bill is legally accepted it represents a genuine trade transaction. Which conclusion is correct?""",
  "It is an accommodation bill; legally enforceable by a holder in due course, but with no trade behind it, so the credit risk is higher",
  ["It is a genuine trade bill, since legal acceptance establishes the commercial transaction",
   "It automatically becomes a demand bill since no goods were supplied",
   "It turns into factoring after discounting and the bank bears no risk"],
  "Accommodation bills lack consideration and are not self-liquidating; banks are cautioned against discounting them.")

S('A8', """Horizon Traders discounts a ₹2,00,000 bill with 73 days to run at 10% p.a. The trainee passes: Bank A/c Dr ₹2,00,000; To Bills Receivable ₹2,00,000; and Discount A/c Dr ₹4,000; To Sales ₹4,000. Which is correct?""",
  "Bank Dr ₹1,96,000 and Discount Dr ₹4,000; To Bills Receivable ₹2,00,000",
  ["The trainee's entries are correct", "Bank Dr ₹2,00,000; To Bills Receivable ₹1,96,000; To Discount ₹4,000",
   "Bank Dr ₹1,96,000; To Bills Receivable ₹1,96,000"],
  "Discount = 2,00,000 × 10% × 73/365 = ₹4,000. The bank pays the net amount; discount is a finance cost; Sales is not touched.")

S('A8', """Ram drew a bill of ₹50,000 on Shyam and ENDORSED it to his creditor Mohan. On maturity Shyam dishonours it; Mohan pays noting charges of ₹200. The entry in Ram's books is:""",
  "Shyam Dr ₹50,200; To Mohan ₹50,200", ["Shyam Dr ₹50,200; To Bills Receivable ₹50,200",
   "Shyam Dr ₹50,200; To Bank ₹50,200", "Mohan Dr ₹50,200; To Shyam ₹50,200"],
  "The bill left Ram's B/R account when endorsed; Mohan now claims from Ram (credit Mohan), and Ram charges Shyam for the bill and noting charges.")

S('A8', """Consider these statements on bills:
1. Three days of grace are added to a bill payable on demand.
2. A bill must be accepted to bind the drawee, but a promissory note needs no acceptance.
3. Rebate on retiring a bill is income for the acceptor.
4. When a bill sent for collection is collected, the drawer debits Bank and credits Bills Sent for Collection.
Which are correct?""",
  "2, 3 and 4 only", ["1, 2, 3 and 4", "1 and 2 only", "3 and 4 only"],
  "No grace days for demand or sight bills (1 wrong).")

S('A8', """Shyam cannot meet a ₹40,000 bill accepted in favour of Ram and requests renewal for 3 months with interest at 12% p.a. Ram agrees. In Ram's books, what is the value of the new bill and what is credited to Interest?""",
  "New bill ₹41,200; Interest credited ₹1,200", ["New bill ₹40,000; Interest credited ₹1,200",
   "New bill ₹44,800; Interest credited ₹4,800", "New bill ₹41,200; Interest credited ₹4,800"],
  "Interest = 40,000 × 12% × 3/12 = 1,200. The old bill is cancelled (Shyam Dr; To B/R), interest is charged (Shyam Dr; To Interest), and a new bill for ₹41,200 is received.")

S('A8', """A bill dated 31 January 2026 is drawn for one month. The clerk records the due date as 3 March 2026; a senior says it should be 2 March because '31 days + 3'. Which is correct?""",
  "3 March 2026: one calendar month gives 28 February (no 31st), plus 3 days of grace",
  ["2 March 2026, counting 31 days plus 3 days of grace", "28 February 2026, without grace days",
   "4 March 2026, as February has 28 days"],
  "Months are calendar months; if the corresponding date doesn't exist, the last day of that month is taken.")

# ===================== A9 Audit & back office =====================
S('A9', """A bank sanctioned working-capital limits to five unrelated companies. During inspection: GSTIN checks show three suppliers do not exist; funds were withdrawn within 48 hours through several accounts; monthly stock statements show identical quantities across different industries; concurrent audit reported nothing. The Board appoints a forensic auditor. Which approach best establishes whether a coordinated fraud occurred?""",
  "Trace end-use of funds, verify suppliers, examine digital evidence and rebuild the transaction trail before fixing responsibility",
  ["Compare interest income from each account with industry averages and quantify leakage",
   "Recompute drawing power from stock statements and raise provisions under IRAC norms",
   "Review branch profitability and staff appraisal ratings for the period"],
  "Forensic audit gathers legally usable evidence: money trail, genuineness of documents and parties, and digital trail.")

S('A9', """Consider these statements about bank audits:
1. Concurrent audit examines transactions at or soon after the time they occur and is part of internal audit.
2. The Long Form Audit Report is submitted by concurrent auditors.
3. RBI's 2021 guidelines allow statutory auditors a tenure of three continuous years, followed by a six-year cooling-off.
4. RBI inspects banks under Section 35 of the BR Act.
Which are correct?""",
  "1, 3 and 4 only", ["1, 2, 3 and 4", "2 and 4 only", "1 and 3 only"],
  "LFAR is submitted by statutory (central and branch) auditors, not concurrent auditors.")

S('A9', """A bank's inter-branch account shows net debit entries of ₹6 crore outstanding for over a year and net credit entries of ₹4 crore outstanding for over a year. The CFO proposes netting them and providing nothing. Which is correct per RBI's approach?""",
  "Provide fully for the net debit position outstanding beyond one year; credit balances are not taken to income",
  ["Net the two and provide nothing, since the net position is only ₹2 crore",
   "Take the ₹4 crore credits to income and provide for ₹6 crore",
   "Ignore both until the statutory auditor reports on them"],
  "Old unreconciled debits may hide frauds; RBI requires 100% provision on net debits outstanding over one year, and unmatched credits are not credited to P&L.")

S('A9', """In a bank's treasury, a dealer both executes forex deals and confirms and settles them because the back-office officer is on leave. The internal auditor objects. Why?""",
  "It breaks segregation of duties between dealing (front office) and confirmation/settlement (back office), a key fraud control",
  ["Dealers are not allowed to deal in forex at all", "Only RBI can confirm forex deals",
   "Back-office work must always be done by the branch manager"],
  "Front, mid and back offices are separated so that no one person can both take and settle positions.")

S('A9', """Which statement best describes Risk-Based Internal Audit in banks?""",
  "Audit coverage, frequency and depth are decided by the assessed business and control risk of each unit",
  ["Every branch is audited monthly irrespective of its risk profile",
   "Only branches with rising NPAs are audited in a year",
   "It replaces statutory audit for branches below a size threshold"],
  "RBIA (RBI guidance since 2002) focuses audit resources on high-risk areas; it does not replace statutory audit.")

S('A9', """A branch processes salary credits for 400 employees of a corporate client from one debit to the company's account. Which voucher type and control are appropriate?""",
  "A composite (transfer) voucher, entered by one officer and verified by another",
  ["Separate cash vouchers for each employee, signed only by the clerk", "A clearing voucher passed without verification",
   "No voucher, since the CBS posts it automatically"],
  "One debit with many credits is recorded on a composite voucher; maker–checker control applies to every voucher.")

S('A9', """Which pair of BR Act sections is correctly matched?""",
  "Section 29 – form of accounts (Third Schedule); Section 30 – audit and RBI approval of auditors",
  ["Section 29 – audit; Section 30 – form of accounts", "Section 35 – reserve fund; Section 17 – inspection",
   "Section 30 – inspection by RBI; Section 35 – audit"],
  "Sec 17 reserve fund, Sec 29 accounts, Sec 30 audit, Sec 35 inspection.")
