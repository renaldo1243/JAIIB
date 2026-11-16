from qb import T

# ---------- D1 Income tax ----------
T('D1', """Interest of ₹9,000 on a savings account and ₹40,000 on FDs is earned by a 45-year-old (old regime). Deduction under 80TTA:""",
  "₹9,000", ["₹10,000", "₹49,000", "₹50,000"],
  "80TTA covers savings-account interest only, up to ₹10,000; here actual is ₹9,000. FD interest gets nothing. Trap: 80TTB (₹50,000) is for seniors.")

T('D1', """A disabled DEPENDANT of the taxpayer is maintained by him. The deduction is under:""",
  "Section 80DD", ["Section 80U", "Section 80D", "Section 80DDB"],
  "80DD = dependant with disability; 80U = the taxpayer himself; 80D = health insurance; 80DDB = treatment of specified diseases.")

T('D1', """An author earns ₹4 lakh royalty on a book. Deduction under 80QQB is limited to:""",
  "₹3 lakh", ["₹4 lakh", "₹1.5 lakh", "₹50,000"],
  "80QQB (and 80RRB for patents) cap the deduction at ₹3 lakh.")

T('D1', """Under the NEW tax regime for FY 2025-26, which deduction is still available to a salaried employee?""",
  "Standard deduction of ₹75,000", ["Section 80C up to ₹1.5 lakh", "Section 80D for health insurance", "Section 80TTA for savings interest"],
  "The new regime removes most Chapter VI-A deductions; standard deduction (₹75,000) and employer NPS (80CCD(2)) remain.")

T('D1', """Health insurance premium of ₹20,000 paid in CASH for self:""",
  "Is not deductible under 80D", ["Is fully deductible under 80D", "Is deductible under 80C", "Is deductible up to ₹5,000 only"],
  "80D needs a non-cash mode; only preventive check-up (up to ₹5,000) may be paid in cash.")

T('D1', """Rent received by an individual from letting out a house is taxed under:""",
  "Income from house property", ["Income from other sources", "Profits and gains of business", "Capital gains"],
  "Annual value of house property is a separate head.")

T('D1', """A bank pays FD interest of ₹60,000 in a year to a 50-year-old customer who has submitted PAN. TDS under 194A:""",
  "Is deductible at 10%, as interest exceeds ₹50,000", ["Is not deductible, as the limit is ₹1 lakh",
   "Is deductible at 20%", "Is never deductible on FD interest"],
  "Threshold ₹50,000 for non-seniors (₹1 lakh for seniors) from 1 April 2025; rate 10% with PAN, 20% without.")

T('D1', """Form 15H is submitted by:""",
  "A resident senior citizen with nil tax", ["Any person below 60 years with nil tax", "A company with losses",
   "A non-resident depositor"],
  "15H = senior citizens; 15G = others (individuals below 60, HUFs) with nil tax.")

T('D1', """For a charitable trust to keep its exemption, it must apply to its objects at least:""",
  "85% of its income", ["50% of its income", "100% of its income every year", "15% of its income"],
  "15% can be accumulated freely; the rest must be applied or accumulated under Form 10 conditions.")

# ---------- D2 GST ----------
T('D2', """Which of the following is NOT a blocked credit under GST?""",
  "Machinery purchased for use in the factory", ["Motor car for the Managing Director", "Food and beverages for staff",
   "Steel used to build the factory building"],
  "Capital goods like plant and machinery get ITC; the others are blocked under Sec 17(5).")

T('D2', """A trader in Rajasthan supplies only services. GST registration is mandatory when aggregate turnover exceeds:""",
  "₹20 lakh", ["₹40 lakh", "₹10 lakh", "₹1.5 crore"],
  "₹40 lakh applies to exclusive suppliers of GOODS; services ₹20 lakh (₹10 lakh in some special-category States).")

T('D2', """A supplier gives a post-sale discount that reduces the taxable value. He should issue a:""",
  "Credit note", ["Debit note", "Fresh tax invoice", "Payment voucher"],
  "Credit note reduces value/tax; debit note increases it.")

T('D2', """Invoice-wise details of outward supplies are furnished in:""",
  "GSTR-1", ["GSTR-3B", "GSTR-2B", "GSTR-9"],
  "GSTR-1 = outward supplies; GSTR-3B = summary + payment; GSTR-2B = auto ITC statement; GSTR-9 = annual.")

T('D2', """A composition dealer:""",
  "Can neither collect GST nor claim ITC", ["Can claim ITC on all purchases", "Can make inter-State outward supplies freely",
   "Pays GST at 18% on turnover"],
  "Composition: low flat rate, no ITC, no tax collection, no inter-State outward supply.")

T('D2', """Interest on delayed payment of GST is charged at:""",
  "18% per annum", ["12% per annum", "24% per annum", "2% per month"],
  "Sec 50: 18% p.a. on tax paid late.")

T('D2', """The GST Council is constituted under:""",
  "Article 279A of the Constitution", ["Article 246A of the Constitution", "Section 22 of the CGST Act", "Article 280 of the Constitution"],
  "279A = GST Council; 246A = concurrent power to levy GST; 280 = Finance Commission.")

T('D2', """For GOODS, the time of supply is generally:""",
  "Earlier of invoice date and due invoice date",
  ["The date payment is received", "The later of invoice date and delivery date", "The end of the month of supply"],
  "Sec 12; GST on advances for goods is not payable since 2017.")

# ---------- D3 Costing methods ----------
T('D3', """2,000 units enter a process at total cost ₹1,64,000; normal loss 10% with scrap value ₹10 per unit; actual output 1,850 units. Abnormal gain is valued at:""",
  "₹4,500", ["₹4,100", ["₹3,500"][0], "₹9,000"],
  "Normal cost per unit = (1,64,000 − 200 × 10)/1,800 = ₹90. Normal output 1,800; actual 1,850 → gain 50 units × 90 = ₹4,500 (net of scrap forgone ₹500, Costing P&L gets ₹4,000).")

T('D3', """A hospital computes cost per patient-day. This is:""",
  "Service costing", ["Job costing", "Process costing", "Batch costing"],
  "Services use composite cost units like passenger-km, patient-day, kWh.")

T('D3', """A sugar mill produces sugar (main) and molasses (minor). Molasses is a:""",
  "By-product", ["Joint product", "Scrap", "Abnormal gain"],
  "Joint products are of comparable value; a by-product has small relative value.")

T('D3', """Which method suits a shipbuilder constructing a vessel over three years at a customer's site?""",
  "Contract costing", ["Process costing", "Batch costing", "Unit costing"],
  "Large, long, site-based work = contract costing.")

T('D3', """In process costing, abnormal LOSS is:""",
  "Valued like good units; to Costing P&L", ["Absorbed by good units", "Ignored as it is unavoidable",
   "Valued at scrap value only"],
  "Abnormal loss is controllable; it shouldn't burden good output.")

T('D3', """Which statement is correct?""",
  "Marginal costing can be used along with process costing", ["Marginal costing replaces job and process costing",
   "Standard costing is a method only for job shops", "Batch costing cannot be used with standard costing"],
  "Techniques (marginal, standard) are used with methods (job, process, batch).")

T('D3', """Prime cost consists of:""",
  "Direct material + direct labour + direct expenses", ["Prime cost + factory overheads", "Works cost + office overheads",
   "Cost of production + selling overheads"],
  "Prime → works (+ factory OH) → cost of production (+ office OH) → cost of sales (+ selling OH).")

T('D3', """A fixed cost per unit, as output rises:""",
  "Falls", ["Rises", "Stays constant", "Becomes variable"],
  "Total fixed cost is constant, spread over more units.")

T('D3', """Escalation clause in a contract allows:""",
  "A price rise if input costs rise", ["The contractee to withhold retention money",
   "The contractor to stop work without notice", "Profit to be recognised only on completion"],
  "It protects the contractor from price rises during long contracts.")

# ---------- D4 Marginal costing & CVP ----------
T('D4', """SP ₹50; VC ₹30; fixed cost ₹60,000. BEP in units and sales:""",
  "3,000 units; ₹1,50,000", ["2,000 units; ₹1,00,000", "1,200 units; ₹60,000", "3,000 units; ₹90,000"],
  "Contribution ₹20 → 60,000/20 = 3,000 units; × ₹50 = ₹1,50,000 (or 60,000/0.4).")

T('D4', """Same data (SP 50, VC 30, FC 60,000). If fixed costs rise by 10%, the new BEP is:""",
  "3,300 units", ["3,000 units", "2,727 units", "3,600 units"],
  "66,000/20 = 3,300. BEP rises in proportion to fixed cost.")

T('D4', """Sales ₹2,00,000; BEP sales ₹1,50,000; P/V ratio 40%. Profit is:""",
  "₹20,000", ["₹50,000", "₹80,000", "₹60,000"],
  "Profit = MoS × P/V = 50,000 × 40% = 20,000. Trap: MoS itself (50,000) is not profit.")

T('D4', """With SP ₹50, VC ₹30 and FC ₹60,000, units needed for profit of ₹40,000 are:""",
  "5,000", ["3,000", "2,000", "4,000"],
  "(60,000 + 40,000)/20 = 5,000.")

T('D4', """A component can be made at variable cost ₹46 plus allocated fixed overhead ₹10 (which continues anyway), or bought at ₹52. Decision:""",
  "Make, since the relevant cost is ₹46", ["Buy, since ₹52 is below ₹56", "Buy, since buying is always cheaper",
   "Indifferent"],
  "Unavoidable fixed overhead is irrelevant. Compare 46 vs 52 → make.")

T('D4', """If variable cost per unit rises while SP is unchanged, the P/V ratio:""",
  "Falls and BEP rises", ["Rises and BEP falls", "Stays the same", "Falls and BEP falls"],
  "Lower contribution per unit → lower P/V → more units needed to break even.")

T('D4', """When closing stock is HIGHER than opening stock, profit under absorption costing compared with marginal costing is:""",
  "Higher", ["Lower", "Equal", "Always zero"],
  "Part of fixed overhead is carried forward in the higher closing stock.")

T('D4', """Margin of safety can be improved by:""",
  "Raising price or cutting fixed costs", ["Increasing fixed costs", "Reducing sales volume",
   "Increasing variable cost per unit"],
  "Anything that lowers BEP or raises sales widens MoS.")

T('D4', """At break-even point:""",
  "Contribution equals fixed cost", ["Contribution equals variable cost", "Sales equal fixed cost", "Profit equals fixed cost"],
  "Profit = contribution − fixed cost = 0.")

T('D4', """P/V ratio is 25% and fixed costs are ₹1,00,000. Sales required to break even:""",
  "₹4,00,000", ["₹1,25,000", "₹25,000", "₹1,00,000"],
  "BEP sales = FC/P/V = 1,00,000/0.25.")

T('D4', """Which is a LIMITATION of marginal costing?""",
  "Semi-variable costs are hard to split", ["It helps in make-or-buy decisions",
   "It shows the effect of volume on profit", "It avoids carrying fixed cost in stock"],
  "The other options are advantages.")

# ---------- D5 Standard costing ----------
T('D5', """Standard: 5,000 kg at ₹20. Actual: 4,800 kg at ₹22 (for the same output). Material price variance:""",
  "₹9,600 Adverse", ["₹10,000 Adverse", "₹9,600 Favourable", "₹4,000 Favourable"],
  "MPV = (SP − AP) × AQ = (20 − 22) × 4,800 = −9,600 (adverse). Trap: using standard quantity (10,000).")

T('D5', """Same data (std 5,000 kg at ₹20; actual 4,800 kg at ₹22). Material usage variance:""",
  "₹4,000 Favourable", ["₹4,400 Favourable", "₹4,000 Adverse", "₹5,600 Adverse"],
  "MUV = (SQ − AQ) × SP = (5,000 − 4,800) × 20 = +4,000 (favourable). Trap: valuing at actual price (4,400).")

T('D5', """Material cost variance in the same case is:""",
  "₹5,600 Adverse", ["₹5,600 Favourable", "₹13,600 Adverse", "₹4,000 Favourable"],
  "MCV = SQ × SP − AQ × AP = 1,00,000 − 1,05,600 = −5,600 = MPV (−9,600) + MUV (+4,000).")

T('D5', """The purchase department is usually responsible for:""",
  "Material price variance", ["Material usage variance", "Labour efficiency variance", "Fixed overhead volume variance"],
  "Price → purchasing; usage and efficiency → production.")

T('D5', """Labour rate variance is calculated on:""",
  "Actual hours paid", ["Standard hours for actual output", "Budgeted hours", "Idle hours only"],
  "Rate variance = (SR − AR) × AH; efficiency = (SH − AH) × SR.")

T('D5', """'Standard quantity' in variance analysis refers to:""",
  "Quantity allowed for the actual output", ["Quantity budgeted for the budgeted output",
   "Average quantity used in the last year", "Quantity purchased during the period"],
  "Variances compare actual input with what the actual output should have consumed.")

T('D5', """Which statement is correct?""",
  "Variances are analysed to find causes and fix responsibility",
  ["Only adverse variances need to be reported", "A favourable variance always indicates efficiency",
   "Standard costing cannot be used with budgetary control"],
  "Large favourable variances may also signal poor standards or quality problems.")

T('D5', """A standard that can be achieved under efficient operating conditions, allowing normal losses, is:""",
  "Attainable standard", ["Ideal standard", "Basic standard", "Historical standard"],
  "Ideal = perfect; basic = unchanged base; attainable = realistic and most used.")

T('D5', """Std labour 1,000 hours at ₹50; actual 1,100 hours at ₹48 for the same output. Labour cost variance:""",
  "₹2,800 Adverse", ["₹2,200 Favourable", "₹5,000 Adverse", "₹2,800 Favourable"],
  "50,000 − 52,800 = −2,800 = rate +2,200 and efficiency −5,000.")

# ---------- D6 Budgets ----------
T('D6', """At 15,000 units: variable cost ₹8 per unit; fixed cost ₹90,000. A flexible budget at 15,000 units allows total cost of:""",
  "₹2,10,000", ["₹1,20,000", "₹2,25,000", "₹1,95,000"],
  "8 × 15,000 + 90,000 = 2,10,000.")

T('D6', """Which budget is the summary of all functional budgets?""",
  "Master budget", ["Cash budget", "Flexible budget", "Sales budget"],
  "The master budget includes budgeted P&L and balance sheet.")

T('D6', """A budget that is continuously updated by adding one more period as each period ends is a:""",
  "Rolling budget", ["Zero-based budget", "Fixed budget", "Performance budget"],
  "Also called continuous budget.")

T('D6', """Which is a DISADVANTAGE of zero-based budgeting?""",
  "It is time-consuming and paper-heavy", ["It removes wasteful spending",
   "It links spending to objectives", "It questions every activity's need"],
  "The other options are advantages.")

T('D6', """Performance budgeting focuses on:""",
  "Outputs and results achieved for the money spent", ["Only the amount spent by each department",
   "Last year's budget plus inflation", "Cash receipts and payments"],
  "It links inputs (money) to physical outputs/outcomes.")

T('D6', """The 'principal budget factor' is:""",
  "The factor that limits activity", ["The largest item of expenditure",
   "The total of all budgets", "The cash balance at the year-end"],
  "Usually sales demand; sometimes capacity or materials.")

T('D6', """A fixed (static) budget is unsuitable for control when:""",
  "Actual output differs widely from budget", ["Output is exactly as budgeted",
   "All costs are fixed", "The budget period is one year"],
  "Flexible budgets adjust cost allowances to actual activity.")

T('D6', """Budgetary control involves:""",
  "Setting budgets, comparing actuals and acting", ["Only preparing budgets",
   "Only recording actual costs", "Auditing the financial statements"],
  "Planning + comparison + corrective action.")
