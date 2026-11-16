from qb import S

# ===================== D1 Income tax =====================
S('D1', """Dr Mehra receives: salary from a private hospital ₹18 lakh; fees from his evening clinic ₹9 lakh; FD interest ₹1.2 lakh; rent from a flat ₹3 lakh. He proposes to show everything under 'Profits and Gains of Business or Profession' as it all flows from his expertise. Which is correct?""",
  "Salary under Salaries, clinic fees under PGBP, rent under House Property and FD interest under Other Sources",
  ["Everything under PGBP, as all income flows from his profession",
   "Everything under Salaries, as salary is his main income",
   "He may choose any head, if applied consistently every year"],
  "Each income is taxed under the head matching its source; the taxpayer has no choice.")

S('D1', """Mr Arvind (52, old regime) paid in FY 2025-26: LIC premium ₹45,000; employee PF ₹72,000; tuition fees for two children ₹60,000; health insurance for self and family ₹28,000 (by cheque); health insurance for his senior-citizen parents ₹40,000 (by UPI); donation to an approved relief fund. His consultant claims ₹2.45 lakh under 80C. What are the correct 80C and 80D deductions?""",
  "80C ₹1,50,000 (capped); 80D ₹65,000 (₹25,000 self + ₹40,000 parents)",
  ["80C ₹2,45,000; 80D nil", "80C ₹1,77,000; 80D ₹68,000", "80C ₹1,50,000; 80D ₹50,000"],
  "80C items total 1.77 lakh, capped at 1.5 lakh. 80D: self/family capped at ₹25,000 (non-senior); parents (senior) up to ₹50,000, actual ₹40,000. Health insurance is not 80C; donation is 80G.")

S('D1', """A 66-year-old pensioner earns ₹62,000 FD interest and ₹9,000 savings interest from one bank in FY 2025-26 and has submitted PAN (old regime). Which statements are correct?
1. He can claim ₹50,000 under 80TTB.
2. He can also claim ₹9,000 under 80TTA.
3. The bank need not deduct TDS since interest is below ₹1 lakh.
4. He may submit Form 15H if his tax on total income is nil.""",
  "1, 3 and 4 only", ["1, 2, 3 and 4", "2 and 3 only", "1 and 2 only"],
  "Seniors get 80TTB (all deposit interest, up to ₹50,000) and cannot also claim 80TTA. From 1 April 2025 the 194A threshold for seniors is ₹1 lakh. Form 15H is for resident seniors with nil tax.")

S('D1', """A 40-year-old depositor without PAN earns FD interest of ₹75,000 from a bank in FY 2025-26. He submits Form 15G claiming nil tax. The branch accepts it and deducts no TDS. Which is correct?""",
  "TDS at 20% is required: Form 15G is invalid without PAN, and interest exceeds the ₹50,000 threshold",
  ["No TDS is needed since Form 15G was submitted", "TDS at 10% is required, PAN being optional",
   "TDS applies only above ₹1 lakh of interest"],
  "Section 206AA: without PAN, TDS is at 20%, and 15G/15H declarations need a valid PAN.")

S('D1', """A registered charitable trust earns ₹1 crore (donations, fees, interest). It applies ₹78 lakh to its objects and keeps ₹22 lakh in a bank FD without filing Form 10. A trustee says registration under Section 12AB guarantees full exemption. Which is correct?""",
  "Exemption needs at least 85% application (or accumulation under Form 10); ₹7 lakh beyond the permitted 15% accumulation becomes taxable",
  ["Registration alone guarantees exemption of the whole ₹1 crore", "All ₹22 lakh is exempt because it is kept in a bank FD",
   "The entire income becomes taxable because only 78% was spent"],
  "85% must be applied; 15% (₹15 lakh) may be accumulated freely; the extra ₹7 lakh not applied or accumulated under Form 10 is taxable.")

S('D1', """An employee (old regime) writes a book and earns royalty of ₹4.5 lakh; his disabled son (severe disability) is dependent on him; he himself has no disability. His consultant claims deductions under 80U and 80RRB. Which is correct?""",
  "80QQB up to ₹3 lakh for the book royalty and 80DD of ₹1,25,000 for the dependant; 80U and 80RRB don't apply",
  ["80U ₹1,25,000 and 80RRB ₹3 lakh", "80QQB ₹4.5 lakh and 80U ₹75,000", "80DD ₹75,000 and 80RRB ₹3 lakh"],
  "80QQB = authors' royalty (cap ₹3 lakh); 80RRB = patents; 80DD = dependant with disability (₹1.25 lakh if severe); 80U = taxpayer himself disabled.")

S('D1', """A salaried officer earns ₹12.6 lakh gross salary in FY 2025-26 under the new regime with no other income. A colleague says he must pay tax because income exceeds ₹12 lakh. Which is correct?""",
  "After the ₹75,000 standard deduction, taxable income is ₹11.85 lakh; the Section 87A rebate makes tax nil",
  ["He must pay tax on ₹12.6 lakh at slab rates", "He must pay tax on ₹60,000, the excess over ₹12 lakh",
   "Standard deduction is not available in the new regime"],
  "New regime: standard deduction ₹75,000; rebate under 87A makes taxable income up to ₹12 lakh tax-free.")

S('D1', """Prime Metals Ltd. sells scrap on which income-tax TCS applies. The buyer argues that because GST is charged on the invoice, TCS cannot apply. The Accounts Manager seeks advice. Which statement is technically correct?""",
  "TCS under the Income-tax Act and GST are under separate laws; each obligation must be examined independently",
  ["Once GST is charged, income-tax TCS cannot apply", "TCS is collected only by Government departments",
   "TCS applies only to exports"],
  "The two statutes operate independently; GST on an invoice doesn't remove an income-tax TCS obligation.")

S('D1', """Which statements about the Income-tax Act 2025 are correct?
1. It replaced the 1961 Act with effect from 1 April 2026.
2. 'Previous year' and 'assessment year' are replaced by a single 'tax year'.
3. It abolished the ₹1.5 lakh deduction for PPF and LIC premium in the old regime.
4. Old Section 80C now corresponds to Section 123.""",
  "1, 2 and 4 only", ["1, 2, 3 and 4", "1 and 3 only", "2 and 3 only"],
  "The new Act mainly renumbers and simplifies; deductions continue with the same limits.")

S('D1', """A bank customer withdraws ₹1.4 crore in cash from his current account during the year; he has filed income-tax returns for the last three years. Which is correct?""",
  "TDS of 2% under Section 194N applies on ₹40 lakh, the amount exceeding ₹1 crore",
  ["TDS of 2% applies on the full ₹1.4 crore", "No TDS applies because he files returns",
   "TDS of 5% applies on amounts above ₹20 lakh"],
  "194N: 2% on cash withdrawals exceeding ₹1 crore in a year from one bank (lower thresholds and higher rates for non-filers).")

S('D1', """A Hindu Undivided Family runs a business. Which statements are correct?
1. HUF is a separate 'person' under Section 2(31).
2. Coparceners acquire an interest in ancestral property by birth.
3. Daughters are coparceners since the 2005 amendment.
4. Members other than the Karta have unlimited personal liability for HUF business debts.""",
  "1, 2 and 3 only", ["1, 2, 3 and 4", "2 and 4 only", "1 and 4 only"],
  "Only the Karta has unlimited liability; other members are liable to the extent of their share in HUF property.")

# ===================== D2 GST =====================
S('D2', """ABC Constructions bought in FY 2025-26: (1) steel and cement to build its own factory building; (2) a CNC machine installed in the factory; (3) a motor car for the MD; (4) office laptops; (5) raw materials used in taxable supplies; (6) gifts to distributors at Diwali. The executive claims ITC on all. On which items is ITC available?""",
  "2, 4 and 5 only", ["All six, since GST was paid", "2, 3, 4 and 5 only", "1, 2, 4 and 5 only"],
  "Sec 17(5) blocks ITC on construction of own immovable property (except plant and machinery), motor vehicles for persons, and gifts. Machinery, laptops and raw materials qualify.")

S('D2', """Aarav Handicrafts (Rajasthan, goods only) has: taxable intra-State supplies ₹31 lakh; exempt supplies ₹6 lakh; sale of old office furniture ₹3 lakh; plus a single inter-State taxable sale of ₹1 lakh. The proprietor says no registration is needed as taxable turnover is ₹32 lakh. Which is correct?""",
  "Registration is required: aggregate turnover is about ₹41 lakh, and an inter-State taxable supply of goods requires registration anyway",
  ["No registration, as taxable turnover is below ₹40 lakh", "Registration only when turnover crosses ₹1.5 crore",
   "Registration only for the inter-State sale, not for intra-State supplies"],
  "Aggregate turnover includes exempt and all other supplies (31 + 6 + 3 + 1 = 41 > 40 lakh). Inter-State taxable supply of goods also triggers compulsory registration.")

S('D2', """Mr Rajesh removes goods for supply on 15 July; they are delivered on 16 July; the invoice is issued on 18 July; payment arrives on 28 July. His accountant pays GST in August's return treating 28 July as the time of supply. Which is correct?""",
  "Time of supply is 15 July (date by which the invoice should have been issued); the liability falls in July, payable by 20 August in GSTR-3B",
  ["Time of supply is 28 July, the date of payment", "Time of supply is 18 July, the invoice date",
   "Time of supply is 16 July, the delivery date"],
  "For goods, time of supply = earlier of the invoice date and the last date for issuing it (at or before removal). July liability is paid in the July GSTR-3B, due 20 August.")

S('D2', """A supplier issued an invoice for ₹12 lakh + 18% GST. The buyer returned goods worth ₹1.5 lakh and later a post-sale discount of ₹50,000 (agreed in the contract) was given. The executive wants to issue a payment voucher and a revised invoice. Which is correct?""",
  "Issue credit notes for both, reducing taxable value by ₹2 lakh and output GST by ₹36,000",
  ["Issue debit notes for both", "Issue a payment voucher; GST is not adjusted for returns",
   "Revise the original invoice for the return and ignore the discount"],
  "Sec 34: a credit note reduces taxable value and tax for returns or agreed post-sale discounts. 2,00,000 × 18% = 36,000.")

S('D2', """Classify the GST on each transaction of a Jaipur trader:
1. Sale to a customer in Kota (Rajasthan)
2. Sale to a customer in Ahmedabad (Gujarat)
3. Import of machinery from Japan
4. Supply to a unit in an SEZ in Jaipur
Which attract IGST?""",
  "2, 3 and 4 only", ["2 only", "1 and 2 only", "3 only"],
  "Inter-State supplies, imports and supplies to SEZ units are treated as inter-State and attract IGST; the Kota sale attracts CGST + SGST.")

S('D2', """A trader with turnover of ₹1.2 crore opts for the composition scheme. Which statements are correct?
1. He can charge GST separately on his invoices.
2. He cannot claim input tax credit.
3. He cannot make inter-State outward supplies.
4. He pays tax at a low flat rate on turnover and files a quarterly statement (CMP-08).""",
  "2, 3 and 4 only", ["1, 2, 3 and 4", "1 and 2 only", "3 and 4 only"],
  "Composition dealers issue a bill of supply without charging tax.")

S('D2', """A registered person paid July's GST of ₹2 lakh on 20 September instead of the due date of 20 August. A clerk says only a late fee applies. Which is correct?""",
  "Interest at 18% p.a. on ₹2 lakh for the delay (about ₹2,960 for 30 days) is payable, besides any late fee for late filing",
  ["Only a late fee applies; no interest", "Interest at 24% p.a. applies on all late payments",
   "Interest applies only if the delay exceeds 90 days"],
  "Sec 50: interest at 18% p.a. on tax paid late, for the period of delay (2,00,000 × 18% × 30/365 ≈ 2,959).")

S('D2', """An online seller sells ₹10 lakh of goods through an e-commerce platform in a month. Which is correct about TCS under GST?""",
  "The e-commerce operator collects TCS (0.5% of net taxable supplies) and the seller can claim credit for it",
  ["The seller collects TCS from each buyer", "No TCS applies to goods sold online",
   "The bank collects TCS when the buyer pays online"],
  "Sec 52: e-commerce operators collect TCS (reduced to 0.5% from 10 July 2024) and file GSTR-8; sellers get credit in their cash ledger.")

S('D2', """Which statements about GST returns are correct?
1. GSTR-1 contains invoice-wise details of outward supplies.
2. GSTR-3B is a summary return with payment of tax.
3. GSTR-2B is an auto-drafted input-credit statement.
4. GSTR-9 is the monthly return of a composition dealer.""",
  "1, 2 and 3 only", ["1, 2, 3 and 4", "2 and 4 only", "1 and 4 only"],
  "GSTR-9 is the annual return; composition dealers use CMP-08 (quarterly) and GSTR-4 (annual).")

S('D2', """Which statement about the GST framework is correct?""",
  "GST came into force on 1 July 2017 under the 101st Constitutional Amendment; the GST Council functions under Article 279A",
  ["GST was introduced under the 122nd Amendment Act and came into force in 2016", "The GST Council is chaired by the RBI Governor",
   "GST replaced income tax and customs duty"],
  "The 122nd Amendment Bill became the 101st Amendment Act, 2016. The Union Finance Minister chairs the Council. GST subsumed indirect taxes like excise, service tax and VAT, not income tax or basic customs duty.")

# ===================== D3 Costing methods =====================
S('D3', """4,000 units enter a process at total cost ₹3,44,000. Normal loss is 10% of input (scrap value ₹20 per unit). Actual output is 3,450 units. The production manager wants to charge the extra loss to the good units. What is the abnormal loss and the value of output?""",
  "Abnormal loss 150 units = ₹14,000 to Costing P&L; output 3,450 units = ₹3,22,000",
  ["Abnormal loss nil; all 550 lost units absorbed by output at ₹99.71 each", "Abnormal loss 150 units = ₹12,900; output ₹3,31,100",
   "Abnormal loss 550 units = ₹51,333; output ₹2,92,667"],
  "Normal cost per unit = (3,44,000 − 400 × 20)/3,600 = ₹93.33. Normal output 3,600; actual 3,450 → abnormal loss 150 × 93.33 = 14,000; output 3,450 × 93.33 = 3,22,000.")

S('D3', """Omega Engineering makes AC systems: compressors by continuous processing, coils in batches, installation per customer, and AMCs tracked customer-wise. The Finance Director wants one uniform costing method. The cost accountant objects. The strongest justification is:""",
  "Different stages consume resources differently, so combining process, batch and job costing (multiple costing) gives accurate costs",
  ["Process costing alone is most accurate because everything ends up in one system", "Marginal costing eliminates the need for product costing",
   "Uniform costing is prohibited whenever installation services are involved"],
  "Multiple costing combines methods suited to each activity.")

S('D3', """In a process, 5,000 units were introduced; 4,000 were completed; 1,000 remain in closing WIP, 100% complete for materials and 60% for conversion. Material cost ₹2,50,000; conversion ₹1,84,000. A trainee divides total cost by 5,000 units. What is the correct cost per completed unit?""",
  "₹90 (₹50 material + ₹40 conversion)", ["₹86.80 (total cost ÷ 5,000)", "₹108.50 (total cost ÷ 4,000)", "₹96.80"],
  "Equivalent units: material 5,000; conversion 4,000 + 600 = 4,600. Material per EU = 50; conversion per EU = 40. Completed unit cost = ₹90.")

S('D3', """Match each business with its costing method:
P. A city bus service
Q. A sugar mill producing sugar and molasses
R. A shipyard building a vessel over three years
S. A printing press doing customers' orders""",
  "P – operating; Q – process (with by-product); R – contract; S – job", ["P – job; Q – batch; R – process; S – contract",
   "P – process; Q – job; R – operating; S – batch", "P – contract; Q – process; R – job; S – operating"],
  "Services use operating costing (passenger-km); continuous production uses process costing (molasses is a by-product); long site work uses contract costing; distinct orders use job costing.")

S('D3', """A contractor's contract price is ₹50 crore. Work certified ₹30 crore; work uncertified ₹2 crore; cost to date ₹26 crore; cash received ₹27 crore (90% of certified). The contract is about 60% complete. What notional profit is there and how much is taken to P&L using 2/3 × notional profit × cash received/work certified?""",
  "Notional profit ₹6 crore; profit taken ₹3.6 crore", ["Notional profit ₹4 crore; profit taken ₹2.4 crore",
   "Notional profit ₹6 crore; profit taken ₹6 crore", "Notional profit ₹24 crore; profit taken ₹14.4 crore"],
  "Notional profit = (work certified + uncertified) − cost = 32 − 26 = 6. Profit to P&L = 2/3 × 6 × 27/30 = 3.6 crore.")

S('D3', """Consider these statements on costing:
1. Normal loss is absorbed by good units; abnormal loss goes to Costing P&L.
2. Marginal costing is a method suited only to process industries.
3. Batch costing treats each batch as a cost unit.
4. Retention money is the part of certified value held back by the contractee.
Which are correct?""",
  "1, 3 and 4 only", ["1, 2, 3 and 4", "2 and 3 only", "1 and 2 only"],
  "Marginal costing is a technique usable with any method.")

S('D3', """An Indian tyre unit produces 1,000 tyres in a lot: rubber 3 kg per tyre at ₹80/kg; labour and overheads for the lot ₹60,000; packing ₹10 per tyre. A customer asks for a quote at cost plus 20%. What price per tyre should be quoted?""",
  "₹372", ["₹310", "₹288", "₹360"],
  "Batch cost = 2,40,000 + 60,000 + 10,000 = 3,10,000 → ₹310 per tyre; + 20% = ₹372.")

S('D3', """Which statements on cost classification are correct?
1. Fixed cost per unit falls as output rises.
2. Variable cost per unit stays constant within the relevant range.
3. Factory rent is a direct cost of each product.
4. Prime cost = direct material + direct labour + direct expenses.""",
  "1, 2 and 4 only", ["1, 2, 3 and 4", "3 and 4 only", "1 and 3 only"],
  "Factory rent is shared by all products, so it is an indirect cost (overhead).")

# ===================== D4 Marginal costing & CVP =====================
S('D4', """A firm sells 80,000 units at ₹250; variable cost ₹150; fixed cost ₹50 lakh. Marketing proposes cutting the price by 10% expecting volume to rise 20%. Which conclusion is correct?""",
  "Reject: profit falls from ₹30 lakh to ₹22 lakh because contribution per unit drops from ₹100 to ₹75",
  ["Accept: higher volume always increases profit", "Accept: profit rises to ₹40 lakh",
   "Indifferent: fixed costs are unchanged"],
  "Now: 80,000 × 100 − 50 lakh = 30 lakh. Proposed: 96,000 × 75 − 50 lakh = 22 lakh.")

S('D4', """A company sells at ₹920 (variable cost ₹610, allocated fixed cost ₹180). It has idle capacity. A foreign buyer offers ₹700 for 5,000 units; domestic sales are unaffected and no extra fixed cost arises. The Marketing Director rejects it as below total cost of ₹790. What is the effect of accepting?""",
  "Profit rises by ₹4.5 lakh (₹90 contribution × 5,000), so accept", ["Profit falls by ₹4.5 lakh because the price is below total cost",
   "Profit falls by ₹11 lakh because the price is ₹220 below domestic price", "No effect, as fixed costs are already covered"],
  "Relevant cost is variable cost; allocated fixed cost doesn't change. Contribution = 700 − 610 = 90 per unit.")

S('D4', """Sales ₹15 crore; variable cost ratio 60%; fixed cost ₹4.2 crore. Which statements are correct?
1. P/V ratio is 40%.
2. Break-even sales are ₹10.5 crore.
3. Margin of safety is 30% of sales.
4. Profit equals margin of safety × variable cost ratio.""",
  "1, 2 and 3 only", ["1, 2, 3 and 4", "2 and 4 only", "1 and 3 only"],
  "Profit = MoS × P/V ratio = 4.5 × 40% = 1.8 crore, not × the variable cost ratio.")

S('D4', """A factory has only 8,000 machine-hours. Product A: contribution ₹60/unit, 2 hours/unit, demand 3,000 units. Product B: contribution ₹45/unit, 1 hour/unit, demand 4,000 units. The manager prioritises A "because it earns more per unit". What is the maximum total contribution?""",
  "₹3,00,000: all 4,000 B first, then 2,000 A", ["₹2,70,000: all 3,000 A first, then 2,000 B", "₹3,60,000: full demand of both products",
   "₹1,80,000: only A, as it earns more per unit"],
  "Contribution per machine-hour: A 30, B 45, so B first: 4,000 h → 1,80,000; remaining 4,000 h → 2,000 A → 1,20,000. Total 3,00,000. A first gives 1,80,000 + 2,000 B × 45 = 2,70,000. Full demand needs 10,000 hours.")

S('D4', """A product line has sales ₹20 lakh, variable costs ₹14 lakh and allocated fixed costs ₹8 lakh (of which ₹6 lakh will continue even if the line is dropped). The board wants to drop it because it shows a loss of ₹2 lakh. What is the effect of dropping it?""",
  "Company profit falls by ₹4 lakh, since contribution of ₹6 lakh exceeds avoidable fixed cost of ₹2 lakh",
  ["Profit rises by ₹2 lakh", "Profit is unchanged", "Profit falls by ₹6 lakh"],
  "Dropping loses contribution 6 and saves only avoidable fixed cost 2 → net loss of 4.")

S('D4', """Production 10,000 units; sales 8,000 units; fixed production overhead ₹50,000; no opening stock. A manager prefers absorption costing "because it always shows higher profit". Which is correct?""",
  "Absorption profit is ₹10,000 higher this year only because stock rose; when stock falls, it will be lower",
  ["Absorption costing always shows higher profit", "Both methods always give the same profit",
   "Marginal costing shows ₹10,000 higher profit this year"],
  "₹5 per unit of fixed overhead is carried forward in 2,000 units of closing stock; the effect reverses when stock is sold.")

S('D4', """Sales ₹1,00,000 give profit ₹10,000; sales ₹1,50,000 give profit ₹25,000. The firm targets profit of ₹40,000. Which is correct?""",
  "P/V 30%, fixed cost ₹20,000; required sales ₹2,00,000", ["P/V 10%, fixed cost nil; required sales ₹4,00,000",
   "P/V 30%, fixed cost ₹30,000; required sales ₹2,33,333", "P/V 25%, fixed cost ₹15,000; required sales ₹2,20,000"],
  "P/V = 15,000/50,000 = 30%; FC = 30,000 − 10,000 = 20,000; sales = (20,000 + 40,000)/0.3 = 2,00,000.")

S('D4', """A component costs ₹46 to make (variable) plus ₹10 of allocated fixed overhead that continues anyway; an outside supplier quotes ₹52. The purchase manager wants to buy because ₹52 < ₹56. Which is correct?""",
  "Make it: the relevant cost of making is ₹46, so buying adds ₹6 per unit",
  ["Buy it: ₹52 is cheaper than the full cost of ₹56", "Indifferent: both cost about the same",
   "Buy it: fixed costs must always be recovered"],
  "Unavoidable fixed cost is irrelevant to make-or-buy.")

S('D4', """Which statements are correct?
1. At break-even, contribution equals fixed cost.
2. An increase in fixed cost raises the break-even point but not the P/V ratio.
3. An increase in variable cost per unit lowers the P/V ratio.
4. Margin of safety is a measure of profit.""",
  "1, 2 and 3 only", ["1, 2, 3 and 4", "2 and 4 only", "1 and 3 only"],
  "MoS is the cushion of sales above break-even; profit = MoS × P/V.")

S('D4', """SP ₹50; VC ₹30; FC ₹60,000. Fixed costs rise by 10% and the selling price is raised to ₹52. What is the new break-even point?""",
  "3,000 units", ["3,300 units", "2,727 units", "3,143 units"],
  "New contribution = 52 − 30 = 22; FC = 66,000; BEP = 66,000/22 = 3,000 units (unchanged).")

S('D4', """A company uses standard costing for performance evaluation; the marketing team wants marginal costing for a special export order. The MD says one system makes the other unnecessary. Which is correct?""",
  "They serve different purposes, control versus decision-making, and can run side by side",
  ["Standard costing completely replaces marginal costing", "Marginal costing is mandatory for statutory accounts",
   "Both always give identical product costs"],
  "Standard costing sets benchmarks and analyses variances; marginal costing supports short-term decisions.")

# ===================== D5 Standard costing =====================
S('D5', """Standard: 3 labour hours per unit at ₹60/hour. Output 2,000 units. Actual: 6,400 hours paid at ₹58/hour, of which 200 hours were idle due to a power cut. Which set of variances is correct?""",
  "Rate ₹12,800 F; idle time ₹12,000 A; efficiency ₹12,000 A; total ₹11,200 A", ["Rate ₹12,800 F; efficiency ₹24,000 A; total ₹11,200 A, with no idle-time variance",
   "Rate ₹12,400 F; idle time ₹11,600 A; efficiency ₹11,600 A; total ₹10,800 A", "Rate ₹12,800 A; idle time ₹12,000 A; efficiency ₹12,000 F; total ₹12,800 A"],
  "Rate = (60 − 58) × 6,400 = 12,800 F. Idle = 200 × 60 = 12,000 A. Efficiency = (6,000 − 6,200) × 60 = 12,000 A. Total = 3,60,000 − 3,71,200 = 11,200 A.")

S('D5', """Standard: 5,000 kg at ₹20 for the actual output. Actual: 4,800 kg bought and used at ₹22. The purchase manager says material performance was poor because cost rose; the production manager says it was good because less was used. Which is correct?""",
  "Price variance ₹9,600 A (purchase) and usage variance ₹4,000 F (production); net cost variance ₹5,600 A",
  ["Price variance ₹10,000 A and usage ₹4,400 F", "Total variance ₹5,600 F, so both performed well", "Price variance ₹9,600 F and usage ₹4,000 A"],
  "MPV = (20 − 22) × 4,800 = 9,600 A; MUV = (5,000 − 4,800) × 20 = 4,000 F; MCV = 1,00,000 − 1,05,600 = 5,600 A.")

S('D5', """A company sets standards that assume no breakdowns, no wastage and peak efficiency. Workers consistently show large adverse variances and morale falls. The best remedy is:""",
  "Replace ideal standards with attainable (current) standards that allow normal losses and idle time",
  ["Keep ideal standards and penalise workers for variances", "Switch to basic standards that never change",
   "Stop computing variances"],
  "Ideal standards demotivate; attainable standards are realistic and best for control.")

S('D5', """A purchase manager bought cheaper, lower-grade material, producing a favourable price variance but heavy wastage on the shop floor (adverse usage variance). Who should be held responsible for the usage variance?""",
  "The purchase manager, since the cause of excess usage was the poor-quality material he bought",
  ["Always the production manager, as usage variance is a production variance", "Nobody, since the two variances cancel",
   "The cost accountant who set the standards"],
  "Responsibility follows the cause, not the label; variance analysis must investigate causes.")

S('D5', """Consider these statements:
1. Standard quantity means the quantity that should have been used for the actual output.
2. Material price variance is computed on actual quantity.
3. Labour efficiency variance is valued at the actual rate.
4. Standard costing supports management by exception.
Which are correct?""",
  "1, 2 and 4 only", ["1, 2, 3 and 4", "2 and 3 only", "1 and 3 only"],
  "Efficiency variance is valued at the standard rate: (SH − AH) × SR (3 wrong).")

S('D5', """The correct sequence in a standard costing system is:""",
  "Set standards → record actual costs → compute variances → analyse causes → report and act",
  ["Record actuals → set standards from actuals → compute variances → report",
   "Compute variances → set standards → record actuals → analyse causes",
   "Set standards → report to management → record actuals → close books"],
  "Standards are set before actuals are compared.")

S('D5', """Standard cost of 1,000 units: material 2 kg × ₹10. Actual output 900 units using 1,900 kg at ₹10. A supervisor compares 1,900 kg with the budget of 2,000 kg and reports a favourable usage variance of ₹1,000. Which is correct?""",
  "Usage variance is ₹1,000 adverse, since standard for 900 units is 1,800 kg",
  ["Usage variance is ₹1,000 favourable, as reported", "Usage variance is nil, since price was at standard",
   "Usage variance is ₹2,000 adverse"],
  "SQ must be for actual output: 900 × 2 = 1,800 kg; (1,800 − 1,900) × 10 = 1,000 A.")

# ===================== D6 Budgets =====================
S('D6', """At 70% capacity (14,000 units) a factory budgets: variable cost ₹7/unit; semi-variable cost ₹40,000 fixed plus ₹2/unit; fixed cost ₹1,20,000. Actual output reached 90% (18,000 units) at a cost of ₹3,30,000. The manager compares it with the original budget of ₹2,86,000 and reports a ₹44,000 overspend. Which is correct?""",
  "The flexible budget at 18,000 units is ₹3,22,000; the real overspend is only ₹8,000",
  ["The overspend is ₹44,000, as reported", "There is a saving of ₹36,000",
   "The flexible budget is ₹3,67,714 (scaling the whole budget)"],
  "Flexible budget = (7 + 2) × 18,000 + 40,000 + 1,20,000 = 3,22,000. Comparing actual with a fixed budget at a different activity level is misleading.")

S('D6', """A government department's budget for each programme is rebuilt from zero every year; managers must justify each activity in 'decision packages' ranked by priority. A critic says this is the same as incremental budgeting. Which is correct?""",
  "It is zero-based budgeting: no activity is carried forward automatically, unlike incremental budgeting",
  ["It is incremental budgeting with an inflation adjustment", "It is performance budgeting, which only lists physical targets",
   "It is a rolling budget, updated every quarter"],
  "ZBB requires fresh justification each period.")

S('D6', """A firm's opening cash is ₹50,000; expected receipts ₹3,20,000; expected payments ₹4,10,000; it wants a minimum cash balance of ₹30,000. How much must it arrange as short-term finance?""",
  "₹70,000", ["₹40,000", "₹90,000", "₹30,000"],
  "Closing before finance = 50,000 + 3,20,000 − 4,10,000 = −40,000; to reach +30,000 it needs 70,000.")

S('D6', """Consider these statements on budgeting:
1. The principal budget factor limits activity and is budgeted first.
2. A budget centre is a unit with its own budget and a responsible manager.
3. A rolling budget adds a new period as each period ends.
4. The master budget is prepared before the functional budgets.
Which are correct?""",
  "1, 2 and 3 only", ["1, 2, 3 and 4", "2 and 4 only", "1 and 4 only"],
  "The master budget summarises the functional budgets, so it comes last.")

S('D6', """A ministry links its ₹500 crore allocation for rural roads to physical targets (km built) and outcomes (villages connected) rather than only line-item heads. This approach is:""",
  "Performance (outcome) budgeting", ["Zero-based budgeting", "Fixed budgeting", "Capital budgeting"],
  "Performance budgeting ties spending to outputs and results.")

S('D6', """A company prepares one budget for 10,000 units. Actual production is 7,000 units because of a strike. Which statement is correct?""",
  "A fixed budget is unsuitable for control here; a flexible budget at 7,000 units is needed for meaningful comparison",
  ["The fixed budget is ideal because it never changes", "Variances against the fixed budget correctly measure efficiency",
   "Budgetary control is not possible when output changes"],
  "Variable-cost allowances must be adjusted to actual activity.")

S('D6', """Which is a LIMITATION of budgetary control?""",
  "Budgets rest on estimates and can become rigid or encourage padding",
  ["It improves coordination among departments", "It fixes responsibility for performance",
   "It provides a basis for comparing actual results"],
  "The others are advantages.")

S('D6', """In a company, sales demand is limited, but the purchase manager prepares the materials budget first and the production budget is then set to use all materials bought. What is wrong?""",
  "The principal budget factor (sales) should be budgeted first; production and materials budgets should follow from it",
  ["Nothing; materials must always be budgeted first", "The cash budget should be prepared before every other budget",
   "The master budget should be prepared first and the sales budget last"],
  "Budgets start from the limiting factor, usually sales demand.")
