from qb import T

# ---------- C2 Ratios ----------
T('C2', """Current assets ₹3 lakh, current liabilities ₹1.5 lakh. Goods of ₹50,000 are bought on credit. The current ratio becomes:""",
  "1.75 : 1", ["2 : 1 (unchanged)", "2.33 : 1", "1.5 : 1"],
  "(3 + 0.5)/(1.5 + 0.5) = 1.75. Trap: thinking equal additions leave the ratio unchanged. When CR > 1, adding equal amounts to both sides lowers it.")

T('C2', """Current assets ₹5 lakh include inventory ₹2 lakh and prepaid expenses ₹20,000; current liabilities ₹2.5 lakh. The quick ratio is:""",
  "1.12 : 1", ["1.20 : 1", "2.00 : 1", "1.28 : 1"],
  "Quick assets = 5 − 2 − 0.2 = 2.8; 2.8/2.5 = 1.12. Trap: removing only inventory gives 1.20.")

T('C2', """COGS ₹60 lakh; opening stock ₹8 lakh; closing stock ₹12 lakh; sales ₹80 lakh. The inventory holding period (365 days) is about:""",
  "61 days", ["46 days", "73 days", "55 days"],
  "ITR = 60/10 = 6 → 365/6 ≈ 61 days. Traps: using sales (80/10 = 8 → 46 days) or closing stock only (60/12 = 5 → 73 days).")

T('C2', """Credit purchases ₹24 lakh; opening creditors ₹3 lakh; closing creditors ₹5 lakh. The average payment period (365 days) is about:""",
  "61 days", ["76 days", "46 days", "91 days"],
  "Average creditors = 4; turnover = 24/4 = 6; 365/6 ≈ 61 days. Trap: using closing creditors (5) gives 76 days.")

T('C2', """For DEBTORS turnover, which figure is used in the numerator?""",
  "Net credit sales", ["Total sales including cash sales", "Cost of goods sold", "Gross profit"],
  "Only credit sales create debtors. Inventory turnover uses COGS.")

T('C2', """PAT ₹18 lakh; preference dividend ₹3 lakh; equity shareholders' funds ₹1 crore. Return on equity is:""",
  "15%", ["18%", "21%", "12%"],
  "ROE = (18 − 3)/100 = 15%. Trap: not deducting preference dividend (18%).")

T('C2', """In computing DSCR, which is the correct numerator?""",
  "PAT + depreciation + interest on term loan", ["PAT only", "EBIT − interest", "PAT + principal instalment"],
  "Cash available for debt service = profit after tax + non-cash depreciation + interest (added back because it is serviced from the same cash). Denominator = interest + instalment.")

T('C2', """Which transaction leaves the debt-equity ratio UNCHANGED?""",
  "Issue of bonus shares out of general reserve", ["Issue of fresh equity for cash", "Raising a new term loan",
   "Conversion of debentures into equity"],
  "Bonus shares only reclassify reserves into capital; total equity stays the same.")

T('C2', """A borrower's current ratio rose from 1.6 to 1.9 while quick ratio fell from 1.1 to 0.8. The best inference is:""",
  "Liquidity may have worsened, with funds getting locked in inventory",
  ["Liquidity has clearly improved because the current ratio rose", "The quick ratio is irrelevant when current ratio is above 1.33",
   "The firm must have repaid its creditors"],
  "Current ratio up but quick ratio down means the increase is in inventory. Trap: reading one ratio alone.")

T('C2', """Which ratio would a supplier giving 30-day credit look at FIRST?""",
  "Current / quick ratio", ["Debt Service Coverage Ratio", "Price-earnings ratio", "Return on equity"],
  "Short-term creditors care about short-term liquidity. DSCR is for term lenders; P/E and ROE for equity investors.")

T('C2', """EPS is ₹8 and market price ₹96. Which is correct?""",
  "P/E = 12 and earnings yield = 8.33%", ["P/E = 12 and earnings yield = 12%", "P/E = 0.083 and earnings yield = 12%",
   "P/E = 8.33 and earnings yield = 12%"],
  "P/E = 96/8 = 12; earnings yield = 8/96 = 8.33% (= 1/P/E).")

T('C2', """Proprietary ratio measures:""",
  "Shareholders' funds as a proportion of total assets", ["Debt as a proportion of equity", "Current assets to current liabilities",
   "Net profit to sales"],
  "Proprietary ratio = owners' funds ÷ total assets; the higher it is, the more assets are owner-financed.")

# ---------- C3 Interest & annuity ----------
T('C3', """₹5,000 invested for 2 years at 8% p.a. compounded QUARTERLY grows to about:""",
  "₹5,858", ["₹5,832", "₹5,849", "₹5,800"],
  "5,000 × 1.02⁸ = 5,858. Traps: annual compounding 5,832; half-yearly 5,849; simple interest 5,800.")

T('C3', """Rent of ₹1 lakh is payable at the BEGINNING of each year for 4 years. At 10%, its present value is about:""",
  "₹3.49 lakh", ["₹3.17 lakh", "₹4.00 lakh", "₹4.64 lakh"],
  "Annuity due PV = 1 × PVAF(10%, 4) × 1.1 = 3.1699 × 1.1 = 3.487. Trap: ordinary annuity (3.17) or no discounting (4.00).")

T('C3', """A ₹5 lakh loan at 12% p.a. is repaid in 36 equal monthly instalments. The EMI is closest to:""",
  "₹16,607", ["₹13,889", "₹18,889", "₹19,000"],
  "i = 1%, n = 36: EMI = 5,00,000 × 0.01 × 1.01³⁶/(1.01³⁶ − 1) ≈ 16,607. Traps: principal only (13,889) or flat interest (18,889).")

T('C3', """How much must be set aside at the end of each year for 5 years at 8% to accumulate ₹10 lakh (FVAF = 5.8666)?""",
  "About ₹1,70,456", ["₹2,00,000", "About ₹1,85,185", "About ₹1,36,110"],
  "Instalment = 10,00,000 ÷ 5.8666 = 1,70,456. Trap: 10 lakh ÷ 5 ignores interest.")

T('C3', """What is the present value of a perpetuity of ₹5,000 a year at 8%?""",
  "₹62,500", ["₹40,000", "₹5,400", "Infinite"],
  "PV = A/r = 5,000/0.08 = 62,500. Trap: 'infinite payments → infinite value'.")

T('C3', """Using the Rule of 72, at 6% compound interest money doubles in about:""",
  "12 years", ["16.7 years", "6 years", "10 years"],
  "72/6 = 12 years. Trap: simple interest (100/6 = 16.7 years).")

T('C3', """Which statement on EMIs (reducing balance) is correct?""",
  "The interest portion falls and the principal portion rises with each instalment",
  ["Interest and principal portions remain equal throughout", "The principal portion falls with each instalment",
   "Interest is charged on the original loan amount throughout"],
  "Interest is on the outstanding balance, which reduces every month. Trap: flat-rate thinking.")

T('C3', """A borrower must choose between 10% compounded annually and 9.6% compounded monthly. The cheaper one is:""",
  "10% compounded annually", ["9.6% compounded monthly, because its nominal rate is lower",
   "Both cost exactly the same", "Cannot be decided without the loan amount"],
  "EAR of 9.6% monthly = (1.008)¹² − 1 ≈ 10.03%, slightly above 10%. So 10% annual is (marginally) cheaper. Trap: comparing nominal rates.", fixed=False)

T('C3', """In an ORDINARY annuity, payments occur:""",
  "At the end of each period", ["At the beginning of each period", "In the middle of each period", "Only at the end of the whole term"],
  "Ordinary = end; annuity due = beginning.")

T('C3', """A bank deducts interest upfront on a 1-year ₹2 lakh loan at 12%. The borrower's effective rate is:""",
  "About 13.64%", ["12.00%", "10.71%", "24.00%"],
  "Receives 1,76,000, repays 2,00,000: 24,000/1,76,000 = 13.64%. Front-end interest raises the effective cost.")

T('C3', """Savings bank interest in India is calculated on:""",
  "The daily closing balance, credited at least quarterly", ["The minimum balance between the 10th and last day of the month",
   "The average annual balance, credited yearly", "The opening balance of each quarter"],
  "Since 2010 RBI requires interest on daily products. Trap: the old 10th-to-end-of-month minimum balance rule.")

# ---------- C4 Bonds ----------
T('C4', """A ₹1,000 bond carries an 8% annual coupon, 5 years to maturity, and the market yield is also 8%. Its price is:""",
  "₹1,000", ["₹920", "₹1,080", "₹681"],
  "Coupon = yield → price = par. Trap: computing unnecessarily; 681 is just the PV of the redemption alone.")

T('C4', """A perpetual bond pays a 9% coupon on ₹1,000; the market yield is 12%. Its price is:""",
  "₹750", ["₹1,333", "₹1,000", "₹900"],
  "Perpetuity price = coupon/yield = 90/0.12 = ₹750. Trap: inverting (1,333).")

T('C4', """A 7% bond (face ₹1,000) is quoted at ₹875. Its current yield is:""",
  "8%", ["7%", "8.75%", "12.5%"],
  "CY = 70/875 = 8%. Trap: coupon rate (7%).")

T('C4', """A portfolio has modified duration 6.5. If yields rise by 75 basis points, the value falls by about:""",
  "4.9%", ["6.5%", "0.49%", "8.7%"],
  "%ΔP ≈ −6.5 × 0.75% = −4.875%. Trap: forgetting to multiply by the yield change.")

T('C4', """Which bond has the LOWEST duration?""",
  "5-year bond with a 12% coupon", ["5-year zero-coupon bond", "10-year bond with a 12% coupon", "10-year zero-coupon bond"],
  "Shorter maturity and higher coupon both lower duration. A zero-coupon bond's duration equals its maturity.")

T('C4', """Market yields FALL by 1%. Which bond gains the MOST in percentage terms?""",
  "20-year 6% bond", ["5-year 6% bond", "20-year 12% bond", "5-year 12% bond"],
  "Longest maturity + lowest coupon = most price sensitive.")

T('C4', """For a bond trading at a PREMIUM, the correct order is:""",
  "Coupon rate > current yield > YTM", ["YTM > current yield > coupon rate", "Current yield > coupon > YTM", "All three are equal"],
  "Premium means the buyer loses (price − par) at maturity, so YTM is lowest. For a discount bond the order reverses.")

T('C4', """An investor expects interest rates to RISE. To protect his bond portfolio he should:""",
  "Shorten the portfolio's duration", ["Lengthen the portfolio's duration", "Buy long-dated zero-coupon bonds",
   "Sell floating-rate bonds and buy fixed-rate bonds"],
  "Lower duration = smaller loss when rates rise. Floating-rate bonds are the safer ones in rising rates.")

T('C4', """A bond whose holder can sell it back to the issuer before maturity is a:""",
  "Puttable bond", ["Callable bond", "Convertible bond", "Zero-coupon bond"],
  "Put = investor's option; call = issuer's option.")

T('C4', """The duration of a perpetual bond at a yield of 10% is:""",
  "11 years", ["Infinite", "10 years", "1.1 years"],
  "Perpetuity duration = (1 + y)/y = 1.1/0.1 = 11 years. Trap: 'infinite' because it never matures.")

# ---------- C5 Forex ----------
T('C5', """Spot USD/INR 83.10/83.18; 1-month forward margin 25/30 paise. The forward rate quoted to an IMPORTER is:""",
  "83.48", ["83.35", "82.88", "83.43"],
  "Ascending margin = premium → add. Importer buys USD at the bank's selling rate: 83.18 + 0.30 = 83.48. Trap: 83.35 is the exporter's (buying) rate.")

T('C5', """A student remits USD 20,000 for fees. Quote USD/INR 83.48/83.56. The rupee amount debited is:""",
  "₹16,71,200", ["₹16,69,600", "₹16,70,400", "₹16,76,000"],
  "Customer buys USD → bank's selling rate 83.56 × 20,000 = 16,71,200. Trap: using 83.48.")

T('C5', """USD/INR 83.20/83.30 and EUR/USD 1.0850/1.0860. The EUR/INR quote is:""",
  "90.27 / 90.46", ["90.46 / 90.27", "76.68 / 76.77", "90.36 / 90.37"],
  "Bid = 83.20 × 1.0850 = 90.27; ask = 83.30 × 1.0860 = 90.46. Bid must be lower than ask.")

T('C5', """Spot USD/INR 83.00; 6-month forward 82.70. The USD is at an annualised:""",
  "Discount of about 0.72%", ["Premium of about 0.72%", "Discount of about 0.36%", "Premium of about 1.45%"],
  "(82.70 − 83.00)/83 × 12/6 × 100 = −0.72%. Forward below spot = discount. Trap: forgetting to annualise (0.36%).")

T('C5', """Which rate does a bank apply when it purchases an export bill (paying the exporter before realisation)?""",
  "Bill buying rate", ["TT buying rate", "TT selling rate", "Bill selling rate"],
  "Bank buys the bill and pays out before reimbursement: bill buying rate, which is lower than TT buying.")

T('C5', """A spot deal done on Monday (no holidays) is settled on:""",
  "Wednesday", ["Monday", "Tuesday", "Friday"],
  "Spot = T+2 working days. Cash = same day; TOM = next day.")

T('C5', """If Indian interest rates are higher than US rates, by interest rate parity the USD will trade at a:""",
  "Forward premium against the rupee", ["Forward discount against the rupee", "Forward rate equal to spot", "Spot premium only"],
  "The higher-interest currency (INR) trades at a forward discount; the lower-interest currency (USD) at a premium.")

T('C5', """An exporter hedged with a forward contract to sell USD at 83.00. On maturity spot is 82.40. Result:""",
  "He sells at 83.00, protected from the fall in the rupee value of his dollars",
  ["He must sell at 82.40, the spot rate on maturity", "He gets 83.00 plus the 0.60 difference",
   "The contract lapses because spot moved against the bank"],
  "A forward fixes the rate for both sides; here the hedge saved him 60 paise per dollar.")

T('C5', """In India, the quotation 'USD/INR 83.25' is an example of a:""",
  "Direct quote", ["Indirect quote", "Cross rate", "Forward quote"],
  "Home currency per unit of foreign currency = direct quote, used in India since 1993.")

T('C5', """Our bank's US dollar account maintained with Citibank, New York, is our:""",
  "Nostro account", ["Vostro account", "Loro account", "Mirror account"],
  "Nostro = 'ours with you'. Our internal record of it is the mirror account.")

# ---------- C6 Cost of capital ----------
T('C6', """Equity 60% at 14%; debt 40% at 9% pre-tax; tax 30%. WACC is:""",
  "10.92%", ["12.00%", "11.52%", "13.20%"],
  "0.6 × 14 + 0.4 × 9 × 0.7 = 8.40 + 2.52 = 10.92%. Trap: ignoring the tax shield (12.00%).")

T('C6', """12% irredeemable debentures are issued at ₹96 (face ₹100); tax 25%. The after-tax cost of debt is:""",
  "9.38%", ["12.50%", "9.00%", "12.00%"],
  "Kd = 12 × (1 − 0.25)/96 = 9/96 = 9.375%. Traps: using face value (9.00%) or pre-tax (12.50%).")

T('C6', """10% preference shares (face ₹100) are issued at ₹95; tax rate 30%. The cost of preference capital is:""",
  "10.53%", ["7.37%", "10.00%", "7.00%"],
  "Kp = 10/95 = 10.53%. Trap: applying a tax shield (preference dividend is not tax-deductible).")

T('C6', """Rf = 7%, Rm = 15%, β = 0.8. Required return by CAPM is:""",
  "13.4%", ["12.0%", "19.0%", "15.0%"],
  "7 + 0.8 × (15 − 7) = 13.4%. Trap: β × Rm = 12%.")

T('C6', """A stock with beta 0.6 is best described as:""",
  "Defensive: it tends to move less than the market", ["Aggressive: it moves more than the market",
   "Risk-free, since beta is below 1", "Negatively correlated with the market"],
  "β < 1 = defensive; β > 1 = aggressive; β = 0 risk-free; only a negative β moves opposite to the market.")

T('C6', """Which is FALSE about retained earnings?""",
  "They have no cost because no fresh money is raised", ["Their cost is broadly the shareholders' opportunity cost",
   "They save floatation costs compared with a new equity issue", "Their cost is generally taken close to the cost of equity"],
  "Retained earnings belong to shareholders who could invest elsewhere: they have an opportunity cost.")

T('C6', """EBIT ₹40 lakh; interest ₹10 lakh; preference dividend ₹4.5 lakh; tax 25%. The degree of financial leverage is:""",
  "1.67", ["1.33", "1.18", "2.00"],
  "DFL = EBIT/[EBIT − I − Pref div/(1 − t)] = 40/(40 − 10 − 6) = 40/24 = 1.67. Trap: ignoring preference dividend (1.33).")

T('C6', """Operating leverage arises from:""",
  "Fixed operating costs", ["Fixed interest charges", "Preference dividend", "Variable selling costs"],
  "Operating leverage = fixed operating costs (DOL = contribution/EBIT). Financial leverage = fixed financing costs.")

T('C6', """Under the Net Income approach, increasing debt in the capital structure:""",
  "Reduces WACC and increases firm value", ["Leaves WACC and firm value unchanged", "Increases WACC and reduces firm value",
   "First reduces then increases WACC"],
  "NI: debt helps. NOI/MM (no tax): irrelevant. Traditional: U-shaped WACC with an optimum.")

T('C6', """Which is an EXTERNAL factor affecting WACC?""",
  "Tax rate", ["Dividend policy", "Capital-structure policy", "Investment policy"],
  "Interest rates, tax rates and market risk premium are outside the firm's control.")

# ---------- C7 Capital budgeting ----------
T('C7', """Project cost ₹100 lakh; inflows ₹30 lakh a year for 5 years; k = 12% (PVAF 3.6048). NPV is about:""",
  "₹8.14 lakh", ["₹50 lakh", "₹−8.14 lakh", "₹30 lakh"],
  "PV = 30 × 3.6048 = 108.14; NPV = 8.14. Trap: undiscounted surplus 150 − 100 = 50.")

T('C7', """For the same project (₹100 lakh outlay, ₹30 lakh a year for 5 years), payback period and PI at 12% are:""",
  "3.33 years and 1.08", ["3.33 years and 1.50", "5 years and 1.08", "3 years and 0.92"],
  "Payback = 100/30 = 3.33 years; PI = 108.14/100 = 1.08. 1.50 is undiscounted.")

T('C7', """Which method ignores the time value of money?""",
  "Payback period", ["Net present value", "Internal rate of return", "Profitability index"],
  "Payback (and ARR) don't discount cash flows. Discounted payback does.")

T('C7', """ARR is calculated using:""",
  "Average accounting profit after depreciation", ["Discounted cash inflows", "Cash flows before depreciation",
   "The IRR of the project"],
  "ARR = average profit ÷ average (or initial) investment. Trap: using cash flows.")

T('C7', """A project's NPV at the firm's cost of capital is negative. Then:""",
  "Its IRR is below the cost of capital", ["Its IRR is above the cost of capital", "Its PI is above 1",
   "Its payback must be longer than its life"],
  "NPV < 0 ⇔ IRR < k ⇔ PI < 1.")

T('C7', """Which should be EXCLUDED from project cash flows?""",
  "Interest on the loan used to finance the project", ["Depreciation tax shield", "Working capital released at the end",
   "Salvage value of the plant"],
  "Financing costs are reflected in the discount rate; including interest would double-count.")

T('C7', """Two mutually exclusive projects rank differently by NPV and IRR. Choose by:""",
  "NPV", ["IRR", "Payback period", "Whichever has the higher initial investment"],
  "NPV measures the absolute increase in wealth and assumes reinvestment at the cost of capital.")

T('C7', """A project has cash flows −100, +250, −160. A problem with using IRR here is:""",
  "There may be more than one IRR because the cash flows change sign twice",
  ["IRR cannot be computed for projects longer than one year", "The IRR will always be zero",
   "NPV cannot be computed for such cash flows"],
  "Non-conventional cash flows (sign changes more than once) can produce multiple IRRs; NPV still works.")

T('C7', """Under a Deferred Payment Guarantee, the bank guarantees:""",
  "Payment of instalments of the purchase price to the machinery supplier",
  ["Performance of a contract by the borrower", "Payment of customs duty on imports",
   "Repayment of a cash credit limit"],
  "DPG supports purchase of machinery on deferred credit; appraised like a term loan.")

# ---------- C8 Leasing ----------
T('C8', """Lease rentals of ₹15 lakh are payable at the BEGINNING of each year for 4 years; discount rate 10% (PVAF 4 yrs = 3.1699). PV of rentals is about:""",
  "₹52.30 lakh", ["₹47.55 lakh", "₹60.00 lakh", "₹43.23 lakh"],
  "Annuity due: 15 × 3.1699 × 1.1 = 52.30. Trap: ordinary annuity 47.55.")

T('C8', """In which lease does the lessor bear the risk of obsolescence?""",
  "Operating lease", ["Finance lease", "Leveraged lease", "Sale and leaseback treated as a finance lease"],
  "Operating leases are short, cancellable, and the lessor keeps the risks and rewards.")

T('C8', """A dry lease of an aircraft means:""",
  "Only the aircraft is leased; the lessee provides crew, maintenance and insurance",
  ["The aircraft is leased with crew, maintenance and insurance", "The aircraft is leased without fuel only",
   "The lessor buys the aircraft back at the end of the lease"],
  "Dry = aircraft only; wet = ACMI (aircraft, crew, maintenance, insurance).")

T('C8', """Under Ind AS 116, a 9-month lease of office equipment may be:""",
  "Expensed on a straight-line basis using the short-term lease exemption",
  ["Must be recognised as a right-of-use asset in all cases", "Shown only as a contingent liability",
   "Capitalised only if ownership passes"],
  "Leases of 12 months or less (and low-value assets) can be exempted.")

T('C8', """Three parties — lessor, lessee and a lender who finances most of the asset's cost — are involved in a:""",
  "Leveraged lease", ["Direct lease", "Sale and leaseback", "Operating lease"],
  "The lessor 'leverages' its investment by borrowing from the lender.")

T('C8', """Which is a feature of hire purchase but NOT of a lease?""",
  "Ownership passes to the user on payment of the last instalment", ["The user gets possession immediately",
   "Payments are made periodically", "The owner can repossess on default"],
  "In a lease ownership stays with the lessor; in hire purchase it passes to the hirer at the end.")

T('C8', """Total lease rentals are ₹60 lakh against a cash price of ₹50 lakh. The correct conclusion is:""",
  "Cannot decide until the rentals are discounted to present value", ["Buy, because ₹60 lakh exceeds ₹50 lakh",
   "Lease, because payments are spread over time", "The two are equal over the asset's life"],
  "Lease-vs-buy compares present values, never undiscounted totals.")

# ---------- C9 Working capital ----------
T('C9', """CA ₹500 lakh; current liabilities other than bank borrowings ₹150 lakh. Under Tandon Method II, MPBF is:""",
  "₹225 lakh", ["₹262.5 lakh", "₹350 lakh", "₹375 lakh"],
  "Method II: 75% of CA − other CL = 375 − 150 = 225. Trap: Method I = 75% of WCG (350) = 262.5.")

T('C9', """Projected turnover ₹4 crore (MSE). Under the Nayak Committee method, minimum bank finance is:""",
  "₹80 lakh", ["₹1 crore", "₹20 lakh", "₹60 lakh"],
  "WC need = 25% (₹1 crore); bank finance = 20% of turnover = ₹80 lakh; margin 5% = ₹20 lakh.")

T('C9', """Raw material 30 days, WIP 10 days, finished goods 20 days, debtors 45 days, creditors 40 days. Net operating cycle:""",
  "65 days", ["105 days", "145 days", "25 days"],
  "30 + 10 + 20 + 45 − 40 = 65 days. Trap: not deducting creditors (105).")

T('C9', """Which REDUCES working-capital requirement?""",
  "Longer credit period from suppliers", ["Longer credit period to customers", "Longer production cycle", "Rapid growth in sales"],
  "Supplier credit finances current assets; the others lengthen the cycle or raise current assets.")

T('C9', """Commercial Paper is issued:""",
  "At a discount to face value, as an unsecured instrument", ["At par with a fixed coupon, secured by stock",
   "By banks to raise short-term deposits", "For a minimum tenor of one year"],
  "CP: unsecured, discounted, 7 days to 1 year, ₹5 lakh multiples; banks issue CDs instead.")

T('C9', """Which is TRUE of forfaiting?""",
  "It is without recourse and usually finances 100% of an export receivable",
  ["It is with recourse and finances 80% of domestic receivables", "It is a short-term domestic service including sales-ledger management",
   "It is identical to factoring"],
  "Forfaiting: export, medium-term, without recourse, 100%. Factoring: ongoing, short-term, with/without recourse, 75–90%, plus services.")

T('C9', """Tandon Method II implies a minimum current ratio of:""",
  "1.33 : 1", ["2 : 1", "1 : 1", "1.5 : 1"],
  "Borrower funds 25% of CA from long-term sources → CL at most 75% of CA → CR = 1/0.75 = 1.33.")

T('C9', """Permanent (core) working capital should ideally be financed by:""",
  "Long-term funds", ["Short-term bank overdraft", "Trade credit only", "Commercial paper rolled over every week"],
  "The core never goes away, so match it with long-term sources; seasonal needs with short-term funds.")

T('C9', """Under TReDS, MSME invoices are financed:""",
  "Without recourse to the MSME seller", ["With full recourse to the MSME seller", "Only by the buyer's bank",
   "Only after the buyer pays"],
  "TReDS platforms let multiple financiers discount MSME receivables on large buyers without recourse to the MSME.")

# ---------- C10 Derivatives ----------
T('C10', """Which derivative has NO counterparty default risk for the participants because a clearing corporation guarantees it?""",
  "Exchange-traded futures", ["Forward contracts", "OTC interest rate swaps", "Forward rate agreements"],
  "Exchange-traded contracts are novated to the clearing corporation; OTC contracts carry counterparty risk.")

T('C10', """The writer of a call option:""",
  "Receives the premium and must sell if the buyer exercises", ["Pays the premium and has the right to buy",
   "Has no obligation once the premium is received", "Can lose at most the premium"],
  "The writer is obliged; the buyer has the right. A call writer's loss can be unlimited.")

T('C10', """A put option is 'in the money' when:""",
  "Spot price is below the strike price", ["Spot price is above the strike price", "Spot equals strike",
   "The premium exceeds the strike price"],
  "A put lets you sell at the strike; it has value when the market price is lower.")

T('C10', """In a currency swap, unlike an interest rate swap:""",
  "Principal amounts in two currencies are exchanged at the start and end", ["Only interest on a notional amount is exchanged",
   "No cash flows are exchanged", "The contract is always exchange-traded"],
  "IRS: notional never exchanged. Currency swap: principal exchanged.")

T('C10', """A borrower worried about RISING rates on a future loan should:""",
  "Buy an FRA (or pay fixed in an interest rate swap)", ["Sell an FRA", "Receive fixed in an interest rate swap",
   "Write a put option on bonds"],
  "Buying an FRA locks the borrowing rate; if rates rise, the FRA pays the difference.")

T('C10', """Exchange-traded currency futures in India are regulated by:""",
  "SEBI (with RBI framing the eligibility norms for currency derivatives)", ["Only RBI", "IRDAI", "FEDAI"],
  "ETDs are SEBI-regulated; OTC forex and interest-rate derivatives are under RBI.")

T('C10', """Which is a feature of a FORWARD contract?""",
  "It is customised and settled on maturity", ["It is marked to market daily", "It is standardised by the exchange",
   "The buyer has a right but no obligation"],
  "Forwards: OTC, customised, one settlement, obligation on both sides.")

# ---------- C1 Business organisation ----------
T('C1', """Which form of organisation gives limited liability WITHOUT share capital?""",
  "Limited Liability Partnership", ["Partnership firm", "Sole proprietorship", "Hindu Undivided Family business (for the Karta)"],
  "LLPs have no share capital requirement but offer limited liability; partners and the Karta have unlimited liability.")

T('C1', """A company had net profit of ₹6 crore last year (turnover ₹300 crore, net worth ₹200 crore). Average net profit of the last 3 years is ₹4 crore. CSR obligation:""",
  "Applies; minimum spend ₹8 lakh", ["Does not apply, as turnover is below ₹1,000 crore", "Applies; minimum spend ₹12 lakh",
   "Does not apply, as average profit is below ₹5 crore"],
  "Any one trigger (net profit ≥ ₹5 crore in the preceding year) applies. Spend 2% of the 3-year average: 2% × 4 crore = ₹8 lakh. Traps: 2% of last year (12 lakh) or testing the average against ₹5 crore.")

T('C1', """Which is NOT an agency cost?""",
  "Interest paid on bank loans", ["Cost of audit to monitor managers", "Cost of independent directors",
   "Loss from managers' value-reducing decisions"],
  "Agency costs: monitoring, bonding, residual loss. Interest is a financing cost.")

T('C1', """The maximum number of members in a private company (excluding employee members) is:""",
  "200", ["50", "100", "No limit"],
  "Private company: 200. Partnership firm: 50 (rules).")

T('C1', """Wealth maximisation is preferred over profit maximisation because it:""",
  "Considers the timing and risk of returns", ["Ignores risk to keep decisions simple", "Focuses on this year's accounting profit",
   "Maximises dividends every year"],
  "Profit maximisation ignores time value and risk.")

T('C1', """Which CSR spending qualifies under Schedule VII?""",
  "Funding a skill-training centre for unemployed youth", ["Sponsoring a cricket match to advertise the company's brand",
   "Bonus paid to the company's own employees", "Donation to a political party"],
  "Brand promotion, employee benefits and political contributions are excluded.")
