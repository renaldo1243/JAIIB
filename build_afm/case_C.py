from qb import S

# ===================== C2 Ratios =====================
S('C2', """Nova Engineering's balance sheet (₹ crore): current assets 24 (inventory 9, prepaid expenses 1), current liabilities 12. Before the year-end it uses ₹4 crore of cash to pay creditors. The MD says: "Our liquidity has improved, since both ratios went up." Which assessment is correct?""",
  "Current ratio rises from 2.0 to 2.5 and quick ratio from 1.17 to 1.25, but this is window dressing; actual liquid funds fell by ₹4 crore",
  ["Current ratio falls from 2.0 to 1.67, so liquidity has worsened",
   "Both ratios are unchanged, because equal amounts left both sides",
   "Current ratio rises to 2.5 but quick ratio falls to 0.83, so the MD is wrong"],
  "Before: CR 24/12 = 2.0; QR (24 − 9 − 1)/12 = 1.17. After paying 4: CR 20/8 = 2.5; QR 10/8 = 1.25. With CR above 1, paying current liabilities improves ratios without improving real liquidity, a classic window-dressing pattern.")

S('C2', """A term-loan borrower projects: PAT ₹42 lakh; depreciation ₹18 lakh; interest on term loan ₹12 lakh; principal instalment ₹30 lakh. The junior analyst computes DSCR as 1.43 and recommends rejection, as the bank's norm is 1.5. Which is correct?""",
  "DSCR is 1.71 because term-loan interest is added back in the numerator; the proposal meets the norm",
  ["DSCR is 1.43 and the proposal should be rejected", "DSCR is 2.00 because only principal is in the denominator",
   "DSCR is 1.38 because tax must also be added to the denominator"],
  "DSCR = (PAT + depreciation + interest on TL)/(interest on TL + instalment) = (42 + 18 + 12)/(12 + 30) = 72/42 = 1.71. The analyst left out interest from the numerator: (42 + 18)/42 = 1.43.")

S('C2', """Two borrowers seek identical term loans:
Company | LT debt | Shareholders' funds | Interest coverage | DSCR
X | ₹180 cr | ₹90 cr | 6.5 times | 2.1
Y | ₹120 cr | ₹160 cr | 1.4 times | 0.9
The credit officer recommends Y only because its debt-equity is lower. The senior manager disagrees. Which reasoning is sound?""",
  "Y's low leverage is outweighed by weak debt-servicing ability (DSCR below 1); X, though more leveraged, can service debt comfortably",
  ["Y is safer because a lower debt-equity ratio always means lower credit risk",
   "X must be rejected because debt-equity above 1 : 1 is never acceptable",
   "Both should be rejected because their ratios conflict"],
  "Capital-structure ratios show the cushion; coverage and DSCR show repayment capacity. A DSCR under 1 means cash accruals don't cover debt service.")

S('C2', """FY 2025 vs FY 2026 for a working-capital borrower:
• Current ratio 2.10 → 2.08
• Quick ratio 1.28 → 0.82
• Inventory holding 52 → 96 days
• Debtors collection 48 → 46 days
The borrower says liquidity is unchanged. Which conclusion is most appropriate?""",
  "Liquidity has deteriorated because funds are getting locked in slow-moving inventory, which the steady current ratio hides",
  ["Liquidity is satisfactory because the current ratio is above 2", "Liquidity has improved because debtors are collected faster",
   "Quick ratio is irrelevant once the current ratio exceeds 2"],
  "A stable current ratio with a sharply lower quick ratio and nearly doubled inventory days shows the composition of current assets has worsened.")

S('C2', """Sales ₹120 crore of which ₹20 crore are cash sales; opening debtors ₹18 crore; closing debtors ₹22 crore (including ₹2 crore bills receivable). The credit manager computes collection period as 61 days using total sales. What is the correct average collection period (365 days)?""",
  "73 days", ["61 days", "67 days", "80 days"],
  "Credit sales = 100; average receivables (debtors + B/R) = (18 + 22)/2 = 20; DTR = 5; collection period = 365/5 = 73 days. Using total sales: 120/20 = 6 → 61 days (wrong).")

S('C2', """Sigma Manufacturing reports COGS ₹840 crore, opening inventory ₹90 crore, closing inventory ₹120 crore, sales ₹1,050 crore. The Operations Manager says higher closing stock proves better inventory management. Which statement is correct?""",
  "Inventory turnover is 8 times (about 46 days); a higher closing stock alone does not show better management",
  ["Inventory turnover is 10 times, based on sales, and higher stock is good", "Inventory turnover is 7 times, using closing stock only",
   "Inventory turnover can't be computed without the gross profit ratio"],
  "ITR = COGS/average inventory = 840/105 = 8 times. Rising stock may signal slow-moving goods.")

S('C2', """Total outside liabilities ₹300 crore; share capital and reserves ₹150 crore, of which goodwill and other intangibles ₹30 crore. The bank's TOL/TNW norm is 3:1. The analyst computes 2.0 and approves. Which is correct?""",
  "TOL/TNW is 2.5, because tangible net worth excludes intangibles; it is within the 3:1 norm",
  ["TOL/TNW is 2.0, as computed, and within norm", "TOL/TNW is 3.3, so the proposal breaches the norm",
   "TOL/TNW is 1.5, since intangibles are added to net worth"],
  "TNW = 150 − 30 = 120; TOL/TNW = 300/120 = 2.5.")

S('C2', """Consider these statements on ratio analysis:
1. Debtors turnover uses net credit sales and includes bills receivable in debtors.
2. Inventory turnover normally uses cost of goods sold.
3. A bonus issue lowers the debt-equity ratio.
4. Return on capital employed needs figures from both the P&L and the balance sheet.
Which are correct?""",
  "1, 2 and 4 only", ["1, 2, 3 and 4", "2 and 3 only", "1 and 4 only"],
  "A bonus issue only reclassifies reserves into capital; net worth and D/E are unchanged (3 wrong).")

S('C2', """EBIT ₹36 crore; equity ₹120 crore; long-term debt ₹80 crore at 10%; tax 25%. The CFO says borrowing more at 10% will raise ROE. Which is correct?""",
  "ROCE is 18%, above the 10% cost of debt, so more debt (trading on equity) should raise ROE, though it adds financial risk",
  ["ROCE is 30%, so the company should stop borrowing", "ROCE is 18%, but more debt always reduces ROE",
   "ROCE can't be compared with the cost of debt"],
  "ROCE = 36/200 = 18%. When ROCE exceeds the cost of debt, leverage increases return to equity holders: favourable financial leverage.")

S('C2', """Company X: market price ₹480, DPS ₹18, EPS ₹32. Company Y: market price ₹360, DPS ₹12, EPS ₹30. Which statements are correct?
1. X's dividend yield (3.75%) is higher than Y's (3.33%).
2. Y has the lower P/E ratio (12) compared with X (15).
3. X has the higher payout ratio (56.25% vs 40%).
4. Higher DPS always means higher dividend yield.""",
  "1, 2 and 3 only", ["1 and 4 only", "2 and 3 only", "1, 2, 3 and 4"],
  "DY = 18/480, 12/360; P/E = 480/32 = 15, 360/30 = 12; payout = 18/32, 12/30. Statement 4 ignores price.")

S('C2', """A company needs a current ratio of at least 1.33 for its working-capital limit. Current assets ₹36 lakh; current liabilities ₹28 lakh (ratio 1.29). Which single action of ₹5 lakh brings it into compliance?""",
  "Raising a ₹5 lakh long-term loan and keeping the cash", ["Buying stock of ₹5 lakh on credit",
   "Buying a machine for ₹5 lakh in cash", "Converting a ₹5 lakh long-term loan into a short-term loan"],
  "Long-term loan: 41/28 = 1.46 (complies). Credit purchase of stock: 41/33 = 1.24. Machine for cash: 31/28 = 1.11. Converting long-term debt to short-term: 36/33 = 1.09. Only fresh long-term funds raise current assets without raising current liabilities.")

S('C2', """Which ratio does each user look at FIRST?
P. A supplier giving 60-day credit
Q. A bank financing a 7-year term loan
R. An equity investor""",
  "P – quick/current ratio; Q – DSCR; R – EPS/ROE", ["P – DSCR; Q – current ratio; R – debt-equity",
   "P – ROE; Q – quick ratio; R – DSCR", "P – inventory turnover; Q – P/E; R – current ratio"],
  "Short-term creditors look at liquidity; term lenders at debt-service capacity; equity investors at returns.")

S('C2', """Net sales ₹200 crore; gross profit ₹50 crore; operating expenses (admin + selling) ₹26 crore; interest ₹6 crore; tax ₹4.5 crore. The analyst reports an operating ratio of 13%. Which is correct?""",
  "Operating ratio is 88% and operating profit ratio 12%", ["Operating ratio is 13% and operating profit ratio 87%",
   "Operating ratio is 75% and operating profit ratio 25%", "Operating ratio is 91% and operating profit ratio 9%"],
  "Operating ratio = (COGS 150 + operating expenses 26)/200 = 88%. Interest and tax are excluded.")

S('C2', """A borrower's debtors turnover improved from 5 to 8 times. Which information would MOST help judge whether credit management really improved?""",
  "Changes in credit policy, sales mix, seasonality and whether receivables were factored",
  ["The company's dividend payout ratio", "The market price of the company's shares",
   "The ratio of fixed assets to long-term funds"],
  "A higher turnover may come from cutting credit (and sales), factoring receivables, or a seasonal year-end.")

# ===================== C3 Interest & annuity =====================
S('C3', """A borrower takes a home loan of ₹30 lakh at 9% p.a. for 20 years (monthly reducing). The relationship manager says total interest will be about ₹54 lakh "because 9% × 20 years = 180%". What are the EMI and total interest, approximately?""",
  "EMI ≈ ₹26,992; total interest ≈ ₹34.8 lakh", ["EMI ≈ ₹35,000; total interest ≈ ₹54 lakh",
   "EMI ≈ ₹12,500; total interest ≈ ₹0", "EMI ≈ ₹26,992; total interest ≈ ₹54 lakh"],
  "EMI = P·i(1+i)ⁿ/((1+i)ⁿ − 1) with i = 0.75%, n = 240 ≈ ₹26,992; total paid ≈ 64.78 lakh → interest ≈ 34.78 lakh. Flat-rate thinking (9% × 20 years) overstates interest because the balance reduces.")

S('C3', """Mr Anil invests ₹1 lakh at the BEGINNING of each year for 10 years at 8% p.a. compounded annually (FVAF 8%, 10 = 14.4866). His adviser quotes ₹14.49 lakh as the maturity value. What is correct?""",
  "About ₹15.65 lakh, since payments at the beginning earn one extra year of interest", ["₹14.49 lakh, as quoted",
   "₹10 lakh, as interest is paid out each year", "About ₹21.59 lakh"],
  "Annuity due = ordinary FV × (1 + r) = 14.4866 × 1.08 = 15.65 lakh.")

S('C3', """A customer wants ₹50 lakh in 15 years for his child's education. A deposit scheme gives 9% compounded annually (FVAF 9%, 15 = 29.3609). How much must he deposit at the END of each year?""",
  "About ₹1.70 lakh", ["₹3.33 lakh", "About ₹1.56 lakh", "About ₹2.17 lakh"],
  "Annual deposit = 50,00,000 ÷ 29.3609 ≈ 1,70,294. Dividing 50 lakh by 15 years ignores interest.")

S('C3', """A retiring officer can take a lump sum of ₹60 lakh or a pension of ₹6 lakh a year for 20 years paid at the BEGINNING of each year. At 8% (PVAF 8%, 20 = 9.8181), which is financially better?""",
  "The pension: its present value is about ₹63.6 lakh, more than ₹60 lakh", ["The lump sum, because ₹60 lakh is received at once",
   "The pension, because ₹1.2 crore is received in total", "Both are equal, because the pension is fixed"],
  "PV of annuity due = 6 × 9.8181 × 1.08 = 63.62 lakh > 60 lakh. Comparing totals (₹1.2 crore) is the trap.")

S('C3', """Bank A offers 10% compounded quarterly; Bank B offers 10.3% compounded annually on deposits. The customer chooses B "because 10.3 > 10". Which is correct?""",
  "A is better: its effective annual rate is about 10.38%", ["B is better because its nominal rate is higher",
   "They are identical", "A is better because quarterly interest is always higher than any annual rate"],
  "EAR of A = (1.025)⁴ − 1 = 10.38% > 10.3%.")

S('C3', """Mr Rakesh invests ₹8 lakh at 9% compounded annually for 4 years (1.09⁴ = 1.4116). An alternative pays 10% simple interest for 4 years. Which statement is correct?""",
  "Compound option gives about ₹11.29 lakh, more than the simple-interest option's ₹11.20 lakh",
  ["Simple interest is better because 10% exceeds 9%", "Both give ₹11.20 lakh", "Compound interest helps only after 5 years"],
  "8 × 1.4116 = 11.29 lakh; 8 × (1 + 0.40) = 11.20 lakh.")

S('C3', """A company considers leasing a warehouse at ₹10 lakh payable at the END of each year for 3 years, or buying it for ₹24.50 lakh. Required return 12% (PVAF 2.4018). The finance executive says: "Lease costs ₹30 lakh, so buy." Which conclusion is justified?""",
  "Lease, because the present value of the rentals (₹24.02 lakh) is lower than the purchase price",
  ["Buy, because total rentals of ₹30 lakh exceed ₹24.50 lakh", "Buy, because time value doesn't apply to fixed assets",
   "Indifferent, because rentals are fixed"],
  "10 × 2.4018 = 24.02 lakh < 24.50 lakh.")

S('C3', """In the same case, if the ₹10 lakh rentals were payable at the BEGINNING of each year, which conclusion follows?""",
  "Buy, because the PV of rentals rises to about ₹26.90 lakh", ["Lease, since the PV is still ₹24.02 lakh",
   "Lease, because advance payments reduce the cost", "Indifferent, since total rentals are ₹30 lakh either way"],
  "Annuity due PV = 24.02 × 1.12 = 26.90 lakh > 24.50 lakh.")

S('C3', """A ₹10 lakh loan at 12% p.a. is offered on (a) reducing balance with monthly EMI for 1 year, or (b) 'flat' 12% for 1 year, repaid in 12 equal instalments of ₹93,333. Which statement is correct?""",
  "Flat 12% costs much more: its effective rate is roughly 21–22% because interest is charged on the full principal throughout",
  ["Both cost exactly 12%", "Flat rate is cheaper, as instalments are fixed",
   "Reducing balance costs more because interest is compounded monthly"],
  "Under a flat rate, interest ₹1.2 lakh is charged on ₹10 lakh although on average only about half is outstanding; the effective rate is close to double.")

S('C3', """Consider these statements:
1. In an ordinary annuity, payments are made at the end of each period.
2. The future value of an annuity due equals that of an ordinary annuity multiplied by (1 + r).
3. Under the Rule of 72, money doubles in about 9 years at 8%.
4. The present value of a perpetuity of ₹5,000 at 10% is ₹5,500.""",
  "1, 2 and 3 only", ["1, 2, 3 and 4", "1 and 4 only", "2 and 3 only"],
  "Perpetuity PV = 5,000/0.10 = ₹50,000 (4 wrong).")

S('C3', """A municipality has 8 lakh residents, growing at 10% compounded annually. The planning department needs the projection after 5 years (1.1⁵ = 1.6105). An officer estimates 12 lakh using simple growth. What is the closest projection?""",
  "12.88 lakh", ["12.00 lakh", "13.52 lakh", "11.73 lakh"],
  "8 × 1.6105 = 12.88 lakh. Simple growth (8 × 1.5) understates it.")

S('C3', """A bank discounts a 1-year ₹5 lakh loan at 11% (interest deducted upfront). A competitor charges 12% payable at maturity. Which is cheaper for the borrower?""",
  "The 12% back-end loan; the discounted loan's effective rate is about 12.36%", ["The 11% discounted loan because 11 < 12",
   "Both cost the same", "The discounted loan, because interest is paid immediately"],
  "Discounted: borrower receives 4.45 lakh and repays 5 lakh → 0.55/4.45 = 12.36%.")

# ===================== C4 Bonds =====================
S('C4', """An investor holds three 12-year bonds with coupons of 6% (X), 10% (Y) and 14% (Z). Market yields rise by 2%. The portfolio manager expects Z to fall most "because high-coupon bonds are riskier". Which conclusion is correct?""",
  "X falls the most in percentage terms, because lower-coupon bonds are more price-sensitive",
  ["Z falls the most, because higher coupons carry more risk", "All three fall by the same %, as maturity is identical",
   "Only Z falls; X and Y rise"],
  "For the same maturity, a lower coupon puts more value in the distant redemption, increasing sensitivity.")

S('C4', """A pension fund compares 7% G-secs with 3, 8 and 18 years to maturity, ahead of an expected policy-rate hike. The committee notes:
1. The 18-year bond should show the largest % fall.
2. The 3-year bond has the highest interest-rate risk, being nearest to maturity.
3. Longer maturity generally increases price sensitivity, at a decreasing rate.
4. Equal coupons mean maturity does not affect volatility.
Which are correct?""",
  "1 and 3 only", ["2 and 4 only", "1, 2 and 3 only", "1, 3 and 4 only"],
  "Malkiel's theorems: longer maturity → greater sensitivity, increasing at a decreasing rate.")

S('C4', """A bond (face ₹1,000, 10% coupon, 5 years to maturity) is bought at ₹1,080. An analyst says its YTM is 9.26% (its current yield). Using the approximation formula, what is the YTM and how does it compare?""",
  "About 8.08%: lower than both the coupon (10%) and current yield (9.26%), as expected for a premium bond",
  ["9.26%, since current yield equals YTM", "10%, since YTM equals coupon for all bonds held to maturity",
   "About 11.6%, higher than coupon because the bond is at a premium"],
  "Approx YTM = [100 + (1,000 − 1,080)/5]/[(1,000 + 1,080)/2] = 84/1,040 = 8.08%. For a premium bond: coupon > CY > YTM.")

S('C4', """A bank's treasury holds a ₹500 crore portfolio:
Bond | Coupon | Maturity | Modified duration
A | 7.5% | 3 yrs | 2.6
B | 8.0% | 6 yrs | 4.8
C | 8.5% | 10 yrs | 7.2
Yields are expected to rise. Which statements are correct?
1. Bond C carries the highest interest-rate risk.
2. MD gives the approximate % price change for a 1% change in yield.
3. For a 1% rise, A falls more than C.
4. Managers usually shorten duration when they expect rates to rise.""",
  "1, 2 and 4 only", ["2 and 3 only", "1 and 3 only", "1, 2, 3 and 4"],
  "%ΔP ≈ −MD × Δy, so C falls about 7.2% and A about 2.6% for a 1% rise.")

S('C4', """A 2-year bond with a 10% annual coupon is priced at a 12% yield. The analyst says its duration is 2 years "because it matures in 2 years". What are its price, Macaulay duration and modified duration?""",
  "Price ≈ ₹966.20; duration ≈ 1.91 years; MD ≈ 1.70", ["Price ₹1,000; duration 2 years; MD 2",
   "Price ≈ ₹966.20; duration 2 years; MD 1.79", "Price ≈ ₹1,033.80; duration 1.91 years; MD 2.14"],
  "Price = 100/1.12 + 1,100/1.12² = 89.29 + 876.91 = 966.20. D = (1 × 89.29 + 2 × 876.91)/966.20 = 1.91. MD = 1.91/1.12 = 1.70. Only a zero-coupon bond's duration equals its maturity.")

S('C4', """A 12% bond (face ₹1,000) has 3 years to maturity; market yield is 9%. A trainee says it should trade below par "because yields are positive". What is its approximate price?""",
  "₹1,075.94, a premium, because the coupon exceeds the market yield", ["₹1,000, at par", "₹924.06, at a discount",
   "₹1,120, the face value plus one coupon"],
  "Price = 120 × PVAF(9%, 3) + 1,000/1.09³ = 120 × 2.5313 + 772.18 = 1,075.94.")

S('C4', """A portfolio has a modified duration of 3.8. RBI unexpectedly cuts rates and yields fall 60 basis points. The treasury head expects a gain of 3.8%. What is the approximate change?""",
  "A gain of about 2.28%", ["A gain of 3.8%", "A loss of 2.28%", "A gain of 0.228%"],
  "%ΔP ≈ −MD × Δy = −3.8 × (−0.60%) = +2.28%.")

S('C4', """Bonds X (9%, bought at ₹960) and Y (9%, bought at ₹1,050), both maturing at par in 5 years. Which statements are correct?
1. X's YTM exceeds 9%.
2. Y's YTM is below 9%.
3. Gain or loss on redemption affects YTM.
4. Coupon and YTM are always equal.""",
  "1, 2 and 3 only", ["1 and 4 only", "2 and 3 only", "1, 2, 3 and 4"],
  "Discount bond: YTM > coupon; premium bond: YTM < coupon; equal only at par.")

S('C4', """Consider these statements on bond types:
1. A callable bond gives the issuer the right to redeem early, so investors demand a higher yield.
2. A puttable bond gives the investor the right to sell it back early.
3. A floating-rate bond has high price sensitivity because its coupon is fixed.
4. A zero-coupon bond's duration equals its maturity.
Which are correct?""",
  "1, 2 and 4 only", ["1, 2, 3 and 4", "2 and 3 only", "1 and 3 only"],
  "Floating-rate bonds reset coupons to market rates, so their prices are stable.")

S('C4', """Market yields fall by 1% and then rise by 1%. A trader expects price changes of equal size in both directions. Which bond theorem shows he is wrong?""",
  "The price rise from a fall in yield exceeds the price fall from an equal rise in yield (convexity)",
  ["Bond prices move in the same direction as yields", "Higher-coupon bonds are more price-sensitive",
   "Shorter bonds are more sensitive than longer bonds"],
  "The price–yield curve is convex, so price changes are asymmetric.")

S('C4', """A 9% bond (₹1,000) maturing in 4 years pays coupons SEMI-ANNUALLY; the market yield is 10% p.a. A trainee discounts annual coupons of ₹90 at 10% for 4 years. Which is correct?""",
  "Use ₹45 coupons, 5% per half-year and 8 periods: price ≈ ₹967.68", ["The trainee's method is correct: price ≈ ₹968.30",
   "Use ₹90 coupons at 5% for 8 periods: price ≈ ₹1,290", "Price is ₹1,000 because coupon and yield are close"],
  "Semi-annual valuation halves the coupon and the yield and doubles the periods; the result differs slightly from the annual approximation.")

S('C4', """A perpetual bond pays ₹90 a year; market yield rises from 9% to 12%. The investor expects a 3% fall. What happens?""",
  "Price falls from ₹1,000 to ₹750, a 25% fall", ["Price falls by 3% to ₹970", "Price rises to ₹1,333",
   "Price is unchanged because there is no maturity"],
  "Perpetuity price = coupon/yield: 90/0.09 = 1,000; 90/0.12 = 750. Perpetuals are extremely rate-sensitive.")

S('C4', """Which statement about current yield (CY) and YTM is correct for a bond bought at ₹920 (8% coupon, 6 years, redeemable at par)?""",
  "CY ≈ 8.70% ignores the ₹80 gain at redemption; YTM ≈ 9.7% includes it and the time value of money",
  ["CY and YTM are both 8% because the coupon is 8%", "YTM ignores the redemption value and uses only coupons",
   "CY is higher than YTM for bonds bought at a discount"],
  "CY = 80/920 = 8.70%; approx YTM = (80 + 13.33)/960 = 9.72%. For a discount bond: YTM > CY > coupon.")

S('C4', """A bank invests in a pool of auto loans securitised into pass-through certificates (PTCs), and also holds G-secs and corporate debentures. Which holding is an asset-backed security?""",
  "The PTCs backed by the pool of auto loans", ["The dated G-secs", "The unsecured corporate debentures", "All three"],
  "ABS are securities backed by pools of loans or receivables; G-secs and plain debentures are direct obligations of the issuer.")

# ===================== C5 Forex =====================
S('C5', """An exporter will receive USD 50,000 in three months. Spot USD/INR 83.20/83.28; 3-month forward margin 15/12 paise. The dealer quotes 83.35, adding the margin. Which is correct?""",
  "Margins are descending, so the USD is at a discount: forward buying rate 83.05, rupee proceeds ₹41,52,500",
  ["Margins are added: forward buying rate 83.35", "The selling rate 83.16 applies because it is a forward contract",
   "The spot rate 83.20 applies because the amount is small"],
  "Descending margin (15/12) = discount → subtract: buying 83.20 − 0.15 = 83.05; 50,000 × 83.05 = 41,52,500. The exporter gets the bank's buying rate.")

S('C5', """An importer must remit USD 5,00,000 immediately. Quote: USD/INR 83.48/83.56. A trainee applies 83.48 "because it is a spot deal". Which statement is correct?""",
  "The importer buys USD from the bank, so the selling rate 83.56 applies: ₹4,17,80,000",
  ["Spot deals always use the buying rate: ₹4,17,40,000", "The mid-rate 83.52 applies to all spot deals",
   "Buying and selling rates are the same in spot deals"],
  "Who buys the foreign currency decides the rate, not whether the deal is spot or forward.")

S('C5', """Spot USD/INR 83.42/83.48; 3-month forward margin +18/+22 paise. Two customers approach together: an exporter receiving USD and an importer paying USD, both in 3 months. A probationary officer suggests the same forward rate for both. Which is correct?""",
  "Exporter 83.60 (forward buying); importer 83.70 (forward selling)", ["Both at the forward mid-rate 83.65",
   "Exporter 83.70; importer 83.60", "Both at spot, since forward margins apply only to exporters"],
  "Ascending margin = premium → add: buying 83.42 + 0.18; selling 83.48 + 0.22.")

S('C5', """GBP/USD 1.2650/1.2660 and USD/INR 83.10/83.18. A customer wants to buy GBP 10,000 against rupees. What rate applies and what is the rupee cost?""",
  "GBP/INR ask 105.31; about ₹10,53,059", ["GBP/INR bid 105.12; about ₹10,51,215",
   "GBP/INR 65.69; about ₹6,56,900", "GBP/INR 105.21 (mid); about ₹10,52,100"],
  "Customer buys GBP → bank's selling (ask) rate = 1.2660 × 83.18 = 105.306. 10,000 × 105.306 ≈ ₹10,53,059.")

S('C5', """Spot USD/INR is 84.00. Six-month interest rates: INR 6.5% p.a., USD 4.5% p.a. A dealer quotes a 6-month forward of 83.20 "because the rupee earns more". Using interest rate parity, which is correct?""",
  "Forward should be about 84.82: the higher-interest rupee trades at a forward discount, so the USD is at a premium",
  ["83.20 is correct: the higher-interest currency appreciates forward", "Forward equals spot (84.00) under parity",
   "Forward should be about 85.68"],
  "F = 84 × (1 + 0.0325)/(1 + 0.0225) = 84.82.")

S('C5', """Which rate does a bank apply in each case?
P. Purchasing an exporter's bill under LC before realisation
Q. An inward remittance already credited to the bank's nostro account
R. An importer retiring an import bill""",
  "P – Bill buying; Q – TT buying; R – Bill selling", ["P – TT buying; Q – Bill buying; R – TT selling",
   "P – Bill selling; Q – TT selling; R – Bill buying", "P – TT selling; Q – TT buying; R – Bill buying"],
  "Bill buying is used when the bank pays before reimbursement (lower than TT buying); bill selling for import bills (higher than TT selling).")

S('C5', """An exporter booked a forward contract to sell USD 1,00,000 at 83.00 for March. On maturity spot is 84.10. He asks the bank to pay at spot. Which is correct?""",
  "He must deliver at the contracted 83.00, receiving ₹83 lakh; the forward removed both downside risk and upside gain",
  ["He receives ₹84.10 lakh because forwards settle at spot", "He can cancel the contract and pocket ₹1.10 lakh from the bank",
   "He receives ₹83 lakh plus the ₹1.10 lakh difference"],
  "A forward is an obligation on both parties at the agreed rate.")

S('C5', """Spot USD/INR 83.00; 3-month forward 83.60. A treasury officer reports a forward premium of 0.72%. Which is correct?""",
  "Annualised premium is about 2.89%; 0.72% is only the 3-month figure", ["0.72% p.a. is correct",
   "It is a discount of 2.89% because the forward is higher", "Premium is 7.2% p.a."],
  "(83.60 − 83.00)/83 × 12/3 × 100 = 2.89% p.a.")

S('C5', """Consider these statements on the Indian forex market:
1. India follows the direct method of quotation.
2. A spot deal settles on the second working day.
3. TT buying rate is lower than the bill buying rate.
4. The Indian bank's USD account with a New York bank is its nostro account.
Which are correct?""",
  "1, 2 and 4 only", ["1, 2, 3 and 4", "3 and 4 only", "1 and 3 only"],
  "Bill buying is lower than TT buying (3 wrong).")

S('C5', """An Indian company has USD 2 lakh receivable and USD 1.5 lakh payable, both due in 3 months. The CFO wants to book two separate forward contracts. A treasury adviser suggests a better approach. Which is it?""",
  "Net the exposures and hedge only the net USD 50,000 receivable, saving spreads (natural hedge)",
  ["Hedge both separately, since netting is not allowed for companies", "Do nothing, since receivables and payables always cancel exactly",
   "Hedge USD 3.5 lakh, the gross exposure"],
  "Matching inflows and outflows in the same currency and period reduces exposure; only the net amount needs hedging.")

S('C5', """A customer wants to buy 1,000 units of a foreign bond quoted at USD 92 each. USD/INR is 83.04/83.14. What rupee amount is debited?""",
  "₹76,48,880", ["₹76,39,680", "₹76,44,280", "₹92,000"],
  "1,000 × 92 = USD 92,000, bought from the bank at its selling rate 83.14 = ₹76,48,880.")

# ===================== C6 Cost of capital, CAPM, leverage =====================
S('C6', """Equity: 8 crore shares, market price ₹150 (market value ₹1,200 crore), cost 15%. Debt: book value ₹800 crore, market value ₹750 crore, pre-tax cost 10%; tax 25%. The CFO computes WACC using book values of ₹800 crore each as 11.25%. Using market-value weights, WACC is about:""",
  "12.12%", ["11.25%", "12.50%", "13.85%"],
  "(1,200 × 15% + 750 × 7.5%)/1,950 = (180 + 56.25)/1,950 = 12.12%. Market weights reflect current investor expectations.")

S('C6', """A fund manager evaluates: P (β 0.80, expected return 11%), Q (β 1.20, 16%), R (β 1.60, 17%). Risk-free rate 6%; market return 14%. He wants only positive-alpha stocks. Which qualify?""",
  "Q only", ["R only, as it has the highest expected return", "P and Q", "All three, as all beat the risk-free rate"],
  "Required = 6 + β × 8: P 12.4 (α −1.4), Q 15.6 (α +0.4), R 18.8 (α −1.8).")

S('C6', """A share's last dividend was ₹5, dividends grow at 8%, and the price is ₹60. An analyst computes Ke = 5/60 + 8% = 16.33%. Which is correct?""",
  "17%, because the Gordon model uses next year's dividend (₹5.40)", ["16.33%, as computed", "8.33%, ignoring growth",
   "13%, using β of 1"],
  "Ke = D1/P0 + g = 5.40/60 + 8% = 9% + 8% = 17%.")

S('C6', """Two projects: A returns 13%, B returns 15%. Company WACC is 12%. B's business risk is far higher than the company's average. The CEO wants to accept both because both beat WACC. Which observation is most appropriate?""",
  "WACC suits average-risk projects; B needs a higher risk-adjusted hurdle, and if mutually exclusive only one can be taken",
  ["Every project above WACC must be accepted", "WACC applies only to debt-financed projects",
   "A must be rejected because B earns more"],
  "Using a single WACC for all projects favours risky ones; project-specific risk must be reflected.")

S('C6', """Vertex needs ₹150 crore: Option I all equity (₹10 shares); Option II ₹75 crore equity + ₹75 crore debt at 9%. Expected EBIT ₹30 crore; tax 25%. Which statement is correct?""",
  "Option II gives higher EPS (about ₹2.33 vs ₹1.50) because the 20% return on capital exceeds the 9% cost of debt, but it raises financial risk",
  ["Option I gives higher EPS because it has no interest", "Both give the same EPS because EBIT is the same",
   "Option II gives higher EPS only if EBIT is below ₹13.5 crore"],
  "I: 30 × 0.75/15 crore shares = 1.50. II: (30 − 6.75) × 0.75/7.5 = 2.33. Trading on equity works when return exceeds the cost of debt.")

S('C6', """Sales ₹100 crore; variable costs ₹60 crore; fixed operating costs ₹20 crore; interest ₹8 crore. If sales rise by 10%, EPS will rise by about:""",
  "33%", ["10%", "20%", "16.7%"],
  "DOL = 40/20 = 2; DFL = 20/12 = 1.67; DCL = 3.33. EPS change ≈ 3.33 × 10% = 33%.")

S('C6', """12% debentures (face ₹100) are issued at ₹95, redeemable at ₹105 after 5 years; tax 30%. The finance executive uses 12% as the cost of debt. The approximate after-tax cost is:""",
  "10.4%", ["12.0%", "8.4%", "12.6%"],
  "Kd = [12 × 0.7 + (105 − 95)/5]/[(105 + 95)/2] = (8.4 + 2)/100 = 10.4%.")

S('C6', """Consider these statements about capital-structure theories:
1. Under the Net Income approach, more debt lowers WACC and raises firm value.
2. Under the Net Operating Income approach, firm value is independent of capital structure.
3. The traditional approach says an optimal capital structure exists.
4. MM with corporate taxes says the levered firm's value equals the unlevered firm's value.
Which are correct?""",
  "1, 2 and 3 only", ["1, 2, 3 and 4", "2 and 4 only", "1 and 3 only"],
  "MM with taxes: VL = VU + tD, so leverage adds value through the tax shield (4 wrong).")

S('C6', """Which factors affecting WACC are EXTERNAL to the firm?
1. Level of interest rates
2. Tax rates
3. Dividend policy
4. Market risk premium
5. Capital-structure policy""",
  "1, 2 and 4 only", ["3 and 5 only", "1, 2, 3, 4 and 5", "1 and 5 only"],
  "Dividend and capital-structure policies are the firm's choices (internal).")

S('C6', """A company's 10% preference shares (₹100) are issued at ₹95 with 2% floatation cost; tax rate 30%. The CFO applies a tax shield as for debt. Cost of preference capital is about:""",
  "10.74%", ["7.52%", "10.00%", "10.53%"],
  "Net proceeds = 95 − 1.9 = 93.1; Kp = 10/93.1 = 10.74%. Preference dividend is paid from post-tax profit, so there is no tax shield.")

S('C6', """Under CAPM, which statements are correct?
1. Beta measures systematic risk.
2. Investors are rewarded for unsystematic risk.
3. A security plotting above the SML has positive alpha.
4. A beta of 1.4 means the stock is expected to move more than the market.""",
  "1, 3 and 4 only", ["1, 2, 3 and 4", "2 and 3 only", "1 and 2 only"],
  "Unsystematic risk can be diversified away, so CAPM gives no premium for it.")

S('C6', """An unlevered firm is worth ₹200 crore. An identical firm has ₹80 crore of perpetual debt; tax rate 25%. A director says the levered firm must be worth ₹200 crore too. Under MM with corporate tax, its value is:""",
  "₹220 crore", ["₹200 crore", "₹280 crore", "₹180 crore"],
  "VL = VU + tD = 200 + 0.25 × 80 = 220.")

S('C6', """Rf 7%, market return 15%, beta 0.8. The company's own estimate of its cost of equity is 19% (β × Rm + Rf). The correct CAPM cost of equity is:""",
  "13.4%", ["19.0%", "12.0%", "15.0%"],
  "Ke = 7 + 0.8 × (15 − 7) = 13.4%. Multiplying β by Rm (not by the premium) is the error.")

# ===================== C7 Capital budgeting =====================
S('C7', """A project costs ₹50 lakh with inflows of ₹15, 20, 25 and 10 lakh in Years 1–4; cost of capital 12%. Which set of results is correct?""",
  "Payback 2.6 years; discounted payback about 3.45 years; NPV ≈ ₹3.49 lakh", ["Payback 2.6 years; discounted payback 2.6 years; NPV ₹20 lakh",
   "Payback 3 years; discounted payback 4 years; NPV −₹3.49 lakh", "Payback 2.6 years; discounted payback 3.45 years; NPV ₹20 lakh"],
  "Payback: 15 + 20 = 35, then 15/25 = 0.6 → 2.6 years. PVs: 13.39, 15.94, 17.79, 6.36 = 53.49 → NPV 3.49; discounted payback = 3 + (50 − 47.13)/6.36 = 3.45.")

S('C7', """Projects P and Q are mutually exclusive:
Project | Outlay | NPV at 12% | IRR
P | ₹20 lakh | ₹4 lakh | 22%
Q | ₹60 lakh | ₹9 lakh | 17%
The CEO picks P "because its IRR is higher". Which decision is correct?""",
  "Q, because NPV measures the absolute addition to shareholder wealth and assumes reinvestment at the cost of capital",
  ["P, because a higher IRR always shows the better project", "Both, because both have positive NPV",
   "Neither, because the methods conflict"],
  "For mutually exclusive projects of different scale, NPV prevails.")

S('C7', """In appraising a new plant, a trainee includes: (1) ₹6 lakh paid last year for a feasibility study; (2) interest on the loan that will finance the plant; (3) rent the firm will forgo by using its own vacant shed; (4) additional working capital of ₹10 lakh recovered at the end. Which items should be in the project's cash flows?""",
  "3 and 4 only", ["1, 2, 3 and 4", "1 and 2 only", "2, 3 and 4 only"],
  "Sunk costs are ignored; financing costs are captured in the discount rate; opportunity costs and working capital are included.")

S('C7', """A project costs ₹100 lakh; annual cash inflows (after tax, before depreciation) ₹30 lakh for 5 years; nil salvage; SLM. The analyst reports ARR of 30%. Which is correct?""",
  "ARR on average investment is 20%: average profit ₹10 lakh ÷ average investment ₹50 lakh", ["30% is correct",
   "ARR is 10%, based on initial investment", "ARR is 60%, based on cash inflows over average investment"],
  "ARR uses accounting profit after depreciation (30 − 20 = 10). On average investment (100/2 = 50) it is 20%; on initial investment 10%.")

S('C7', """Consider these statements:
1. NPV > 0 implies IRR > cost of capital and PI > 1 for a conventional project.
2. Payback considers all cash flows over the project's life.
3. Projects with cash flows changing sign more than once may have multiple IRRs.
4. IRR assumes intermediate cash flows are reinvested at the IRR.
Which are correct?""",
  "1, 3 and 4 only", ["1, 2, 3 and 4", "2 and 3 only", "1 and 2 only"],
  "Payback ignores cash flows after the payback date.")

S('C7', """A project with outlay ₹10 lakh earns ₹3 lakh a year for 5 years; k = 10%. PVAF(10%, 5) = 3.7908; PVAF(15%, 5) = 3.3522; PVAF(16%, 5) = 3.2743. The manager says IRR must be 30% "because 3/10 = 30%". What is the IRR approximately?""",
  "About 15.2%", ["30%", "10%, the cost of capital", "About 13.7%"],
  "IRR is where PVAF = 10/3 = 3.333, between 15% (3.3522) and 16% (3.2743) → about 15.2%.")

S('C7', """Under capital rationing (only ₹100 lakh available) a firm has independent projects:
A: outlay 60, NPV 18 | B: outlay 40, NPV 14 | C: outlay 50, NPV 16
Which combination maximises NPV?""",
  "A and B, total NPV ₹32 lakh", ["A and C, total NPV ₹34 lakh but exceeds the budget", "B and C, total NPV ₹30 lakh", "A only, NPV ₹18 lakh"],
  "Feasible combinations within ₹100: A + B (100, NPV 32) or B + C (90, NPV 30). A + C needs 110. Best = A + B.")

S('C7', """A bank appraises a new ₹40 crore project to be housed in an SPV, repaid only from the project's toll revenue, with no recourse to the sponsor's balance sheet. Which key test and structure apply?""",
  "Project finance: viability of projected cash flows (DSCR, IRR, sensitivity) drives the decision, not the sponsor's net worth",
  ["Term-loan appraisal based mainly on the sponsor's existing balance sheet", "Working-capital assessment using Tandon Method II",
   "Collateral value alone, since revenue is uncertain"],
  "Non-recourse project finance relies on the SPV's own cash flows; lenders stress-test them.")

S('C7', """A machinery supplier sells equipment worth ₹12 crore on 5-year deferred terms; the buyer's bank guarantees payment of the instalments to the supplier. A credit officer treats it as risk-free since no funds are disbursed. Which is correct?""",
  "It is a Deferred Payment Guarantee; though non-fund-based, it carries term-loan-like credit risk and needs similar appraisal",
  ["It is risk-free because no money leaves the bank", "It is a performance guarantee with no credit risk",
   "It is a cash credit facility secured by the machinery"],
  "If the buyer defaults, the bank must pay the supplier, so DPGs are appraised like term loans (DSCR, security).")

S('C7', """The finance manager evaluates a project using cash flows after deducting interest on the project loan, and then discounts them at the WACC. The auditor objects because:""",
  "Interest is double-counted: it is already reflected in the discount rate (WACC)",
  ["Interest must be added to the cash flows, not deducted", "WACC should never be used for discounting",
   "Interest is a sunk cost"],
  "Project cash flows are taken before financing costs; the cost of finance enters through the discount rate.")

S('C7', """A one-year project costs ₹100 lakh and returns ₹115 lakh at year-end; cost of capital 10%. An analyst says NPV is ₹15 lakh. Which is correct?""",
  "NPV ≈ ₹4.55 lakh; IRR = 15%", ["NPV = ₹15 lakh; IRR = 10%", "NPV ≈ ₹4.55 lakh; IRR = 4.55%", "NPV = ₹5 lakh; IRR = 15%"],
  "NPV = 115/1.1 − 100 = 4.55. IRR is where 115/(1 + r) = 100 → 15%.")

# ===================== C8 Leasing =====================
S('C8', """Zen Motors signs a 7-year lease of an identified automated facility; it directs the asset's use and gets almost all its benefits; legal title stays with the lessor. The executive books rentals as rent expense "because ownership doesn't pass". Under Ind AS 116 the lessee should:""",
  "Recognise a right-of-use asset and a lease liability, unless the short-term or low-value exemption applies",
  ["Expense rentals, because legal ownership never passes", "Capitalise the asset only if ownership transfers at the end",
   "Disclose the lease only as a contingent liability"],
  "Ind AS 116 removed the operating/finance distinction for lessees.")

S('C8', """An airline needs extra capacity for six weeks during the festival season and hires an aircraft along with the lessor's crew, maintenance and insurance. For its long-term fleet it leases aircraft for 12 years, arranging its own crew and maintenance. Which pair is correct?""",
  "Short hire is a wet lease; the 12-year lease is a dry lease", ["Both are wet leases", "Short hire is a dry lease; the 12-year lease is a wet lease",
   "Both are leveraged leases"],
  "Wet lease = ACMI (aircraft, crew, maintenance, insurance), short-term. Dry lease = aircraft only, usually long-term.")

S('C8', """ABC Manufacturing: buy a packaging line for ₹1.52 crore, or lease at ₹36 lakh at the end of each year for 5 years; cost of capital 10% (PVAF 3.7908). The executive says total rentals of ₹1.80 crore make buying cheaper. Which is correct?""",
  "Lease, because the PV of rentals is about ₹1.365 crore, below ₹1.52 crore", ["Buy, because ₹1.80 crore exceeds ₹1.52 crore",
   "They are financially identical", "Buy, because leases never carry time value"],
  "36 × 3.7908 = 136.47 lakh < 152 lakh.")

S('C8', """Which statements correctly distinguish a finance lease from an operating lease?
1. A finance lease transfers substantially all risks and rewards of ownership.
2. An operating lease is usually cancellable and the lessor bears obsolescence.
3. In a finance lease, PV of minimum lease payments is close to the asset's fair value.
4. In an operating lease, the lease term covers almost the whole economic life.""",
  "1, 2 and 3 only", ["1, 2, 3 and 4", "2 and 4 only", "1 and 4 only"],
  "A lease covering most of the asset's life is a finance-lease indicator (4 wrong).")

S('C8', """A company sells its head-office building to a leasing company for ₹80 crore and takes it back on a 15-year lease. Another company buys a ₹100 crore turbine through a lessor who borrows ₹80 crore from a bank to fund it. Which pair is correct?""",
  "Sale and leaseback; leveraged lease", ["Leveraged lease; sale and leaseback", "Operating lease; direct lease", "Cross-border lease; hire purchase"],
  "Sale and leaseback releases cash from an owned asset; a leveraged lease involves a lender funding most of the lessor's cost.")

S('C8', """A trader wants a delivery van. Under hire purchase (HP) or a finance lease, which statement is correct?""",
  "Under HP ownership passes to the hirer on the last instalment; under a lease it stays with the lessor",
  ["Under both, ownership passes on the last payment", "Under a lease the user always becomes owner at the end",
   "Under HP the vendor claims depreciation throughout"],
  "HP is a purchase on instalments; a lease is a contract for use (bailment).")

S('C8', """Under Ind AS 116, Bharat Ltd. leases (a) laptops worth ₹40,000 each, (b) a warehouse for 9 months, and (c) office space for 10 years. Which can it expense straight-line without recognising a right-of-use asset?""",
  "(a) and (b) only", ["(c) only", "(a), (b) and (c)", "(b) only"],
  "Low-value assets and short-term leases (12 months or less) qualify for the recognition exemption.")

S('C8', """Leasing is often attractive to a growing company because it:""",
  "Provides 100% financing for the asset and preserves working capital and bank limits",
  ["Always costs less than buying, whatever the discount rate", "Transfers ownership immediately to the lessee",
   "Avoids any obligation to pay rentals if business is poor"],
  "Leases conserve funds but are not automatically cheaper; rentals are binding.")

# ===================== C9 Working capital =====================
S('C9', """A manufacturer's annual data (₹ lakh): average raw material stock 30, consumption 180; average WIP 20, cost of production 240; average finished goods 25, COGS 300; average debtors 50, credit sales 400; average creditors 36, credit purchases 216. Using 360 days, what is the net operating cycle?""",
  "105 days", ["165 days", "45 days", "75 days"],
  "RM 60 + WIP 30 + FG 30 + debtors 45 = 165 days gross; less creditors 60 = 105 days net.")

S('C9', """A borrower has current assets of ₹500 lakh and current liabilities other than bank borrowings of ₹150 lakh. It asks for ₹262.5 lakh, quoting the MPBF. The bank uses Tandon Method II. What is the MPBF?""",
  "₹225 lakh", ["₹262.5 lakh", "₹350 lakh", "₹375 lakh"],
  "Method II: 75% of CA − other CL = 375 − 150 = 225. The borrower used Method I (75% of WCG 350 = 262.5).")

S('C9', """An MSE projects annual turnover of ₹4 crore and requests ₹1 crore of working-capital finance under the Nayak (turnover) method. Which is correct?""",
  "Working-capital need is ₹1 crore (25%); the bank finances ₹80 lakh (20%) and the borrower brings ₹20 lakh (5%)",
  ["The bank finances the full ₹1 crore", "The bank finances ₹75 lakh (75% of need)", "The need is ₹80 lakh, all financed by the bank"],
  "Turnover method: requirement 25% of turnover; minimum bank finance 20%; margin 5%.")

S('C9', """Which changes INCREASE a firm's working-capital requirement?
1. Customers are given 60 days' credit instead of 30.
2. Suppliers extend credit from 30 to 60 days.
3. Production cycle lengthens due to a new process.
4. Sales grow rapidly.""",
  "1, 3 and 4 only", ["1, 2, 3 and 4", "2 and 3 only", "1 and 2 only"],
  "Longer supplier credit reduces the working-capital need (2 wrong).")

S('C9', """A group company wants to raise ₹200 crore for 90 days. Its bank says it can't issue commercial paper itself but suggests another instrument for banks. Which statements are correct?
1. CP is an unsecured promissory note issued at a discount.
2. CP can be issued for 7 days to 1 year.
3. Banks raise short-term funds through Certificates of Deposit, not CP.
4. CP is issued in physical form in multiples of ₹1 lakh.""",
  "1, 2 and 3 only", ["1, 2, 3 and 4", "1 and 4 only", "2 and 3 only"],
  "CP is issued only in demat form, in multiples of ₹5 lakh (4 wrong).")

S('C9', """An exporter has a one-off USD 5 million receivable due in 3 years from a buyer abroad, backed by an avalised bill. A domestic trader has continuous credit sales to many buyers. Which financing fits each?""",
  "Forfaiting for the exporter (without recourse, 100%); factoring for the trader (ongoing, short-term)",
  ["Factoring for both", "Forfaiting for the trader; factoring for the exporter", "Cash credit for the exporter; forfaiting for the trader"],
  "Forfaiting: one-off, medium-term export receivables, without recourse. Factoring: ongoing short-term receivables, with or without recourse, plus ledger and collection services.")

S('C9', """A borrower with aggregate fund-based working-capital limits of ₹400 crore from banks draws the entire amount as cash credit. Under RBI's loan system for delivery of bank credit (from April 2019), which is correct?""",
  "At least 60% (₹240 crore) must be drawn as a working-capital loan; at most 40% can be cash credit",
  ["The entire amount may remain cash credit", "At least 40% must be a loan component", "At least 25% must be a loan component"],
  "For limits of ₹150 crore and above, the minimum loan component rose from 40% (Oct 2018) to 60% (April 2019).")

S('C9', """Which financing policy is most prudent for a manufacturer whose working capital has a stable core of ₹40 crore and seasonal peaks of ₹25 crore?""",
  "Finance the core ₹40 crore from long-term sources and the seasonal ₹25 crore from short-term bank finance",
  ["Finance the entire ₹65 crore from short-term overdraft", "Finance the entire ₹65 crore with long-term debt",
   "Finance the core with commercial paper rolled over weekly"],
  "Matching principle: permanent needs with long-term funds, temporary needs with short-term funds.")

S('C9', """An MSME sells to a large PSU on 90 days' credit. It wants funds now without recourse to itself. The best channel is:""",
  "TReDS, where the invoice is discounted by financiers without recourse to the MSME",
  ["Commercial paper issued by the MSME", "Forfaiting through an export bank", "A cash credit limit with full recourse"],
  "TReDS platforms auction MSME receivables on large buyers to financiers, without recourse.")

S('C9', """A firm's current ratio is exactly 1.33 and it meets Tandon Method II. Which statement explains why?""",
  "The borrower funds 25% of current assets from long-term sources, so CL ≤ 75% of CA",
  ["The bank funds 33% of current assets", "Current liabilities equal current assets", "The borrower funds 25% of the WC gap only"],
  "If 25% of CA comes from long-term sources, CL ≤ 75% of CA → CR ≥ 1/0.75 = 1.33.")

# ===================== C10 Derivatives =====================
S('C10', """A company borrowed ₹500 crore at a floating rate (MIBOR + 1%). It fears rates will rise sharply over 3 years. Which hedge fits and what is its cash-flow effect?""",
  "Enter an interest rate swap paying fixed and receiving floating; net cost becomes roughly fixed",
  ["Enter a swap receiving fixed and paying floating", "Sell an FRA, which gains when rates rise",
   "Buy a call option on bonds, which gains when rates rise"],
  "Paying fixed/receiving floating offsets the floating loan payments. Selling an FRA or buying bond calls profits from falling rates.")

S('C10', """Consider these statements:
1. Exchange-traded futures are standardised and marked to market daily.
2. Forward contracts carry counterparty risk.
3. The buyer of an option has an obligation to exercise it.
4. In a currency swap, principal is usually exchanged; in an interest rate swap it is not.
Which are correct?""",
  "1, 2 and 4 only", ["1, 2, 3 and 4", "3 and 4 only", "1 and 3 only"],
  "An option buyer has a right, not an obligation; only the writer is obliged (3 wrong).")

S('C10', """A trader buys a call option on a stock with strike ₹500, paying premium ₹20. At expiry the stock is ₹540. What is the trader's net profit per share, and what if the stock were ₹480?""",
  "₹20 profit at ₹540; loss limited to the ₹20 premium at ₹480", ["₹40 profit at ₹540; ₹20 profit at ₹480",
   "₹20 profit at ₹540; ₹40 loss at ₹480", "₹60 profit at ₹540; nil at ₹480"],
  "At 540: payoff 40 − premium 20 = 20. At 480 the option lapses; loss = premium 20.")

S('C10', """A company will borrow ₹100 crore for 6 months starting 3 months from now and wants to lock today's rate without exchanging principal. Which instrument fits?""",
  "Buy a 3×9 forward rate agreement", ["Sell a 3×6 forward rate agreement", "Enter a currency swap",
   "Buy a put option on the rupee"],
  "A '3×9' FRA covers a 6-month period starting in 3 months; the buyer is protected against rising rates; only the difference is settled.")

S('C10', """A currency futures contract and a forex forward are compared by a CFO. Which statement is correct?""",
  "Futures are exchange-traded with daily margins and clearing-house guarantee; forwards are OTC, customised and carry counterparty risk",
  ["Both are OTC contracts regulated only by RBI", "Forwards are marked to market daily; futures settle only at maturity",
   "Futures give a right but no obligation, like options"],
  "ETDs are SEBI-regulated and novated to the clearing corporation; OTC forex forwards are RBI-regulated.")

S('C10', """A put option on a stock has a strike of ₹300; the stock trades at ₹270. A trainee calls it 'out of the money'. Which is correct?""",
  "It is in the money by ₹30, since the right to sell at ₹300 is valuable when the price is ₹270",
  ["It is out of the money because spot is below strike", "It is at the money", "Moneyness depends only on the premium"],
  "Put: in the money when spot < strike; call: in the money when spot > strike.")

S('C10', """Which users are matched correctly?
P. An exporter selling USD forward to remove exchange risk
Q. A trader buying futures expecting prices to rise
R. A dealer buying in one market and selling in another to lock a riskless gain""",
  "P – hedger; Q – speculator; R – arbitrageur", ["P – speculator; Q – hedger; R – arbitrageur",
   "P – arbitrageur; Q – speculator; R – hedger", "P – hedger; Q – arbitrageur; R – speculator"],
  "Hedgers reduce risk, speculators take it, arbitrageurs exploit price differences.")

S('C10', """A bank writes (sells) a call option on USD to a customer and receives a premium. The bank's risk is:""",
  "Potentially unlimited loss if USD rises sharply, offset only by the premium received",
  ["Limited to the premium received", "Nil, because the customer pays the premium", "Limited to the strike price"],
  "The writer of a call must deliver at the strike however high the price goes; the buyer's loss is limited to the premium.")

S('C10', """An American option differs from a European option because it:""",
  "Can be exercised on any day up to expiry, not only on the expiry date", ["Is traded only in the USA",
   "Gives the writer, not the buyer, the right to exercise", "Has no premium"],
  "American style allows early exercise; European style only at expiry.")

# ===================== C1 Business org & dividend =====================
S('C1', """Omega Ltd. reports PAT ₹180 crore, free cash flow −₹25 crore, debt-equity 2.8 : 1 and large term-loan instalments due in six months; past payout was 45%. Institutional investors press for the same dividend. The CFO advises a lower payout. Which reasoning supports the CFO?""",
  "Dividends must balance profit with liquidity, debt obligations and future funding needs; accounting profit is not cash",
  ["Dividends depend only on accounting profit, so 45% should be maintained",
   "Companies must legally pay at least last year's dividend", "A dividend once declared can never be reduced later"],
  "Paying a large dividend with negative free cash flow and imminent repayments would strain liquidity and covenants.")

S('C1', """Kaveri Ltd. had net profit of ₹6 crore in FY 2024-25 (turnover ₹300 crore, net worth ₹200 crore). Net profits for the last three years were ₹2, 4 and 6 crore. The company secretary says CSR does not apply because average profit is below ₹5 crore. Which is correct?""",
  "CSR applies (net profit above ₹5 crore last year); minimum spend is 2% of ₹4 crore average = ₹8 lakh",
  ["CSR does not apply because the 3-year average is below ₹5 crore", "CSR applies; minimum spend is 2% of ₹6 crore = ₹12 lakh",
   "CSR applies only when turnover crosses ₹1,000 crore"],
  "Applicability uses the preceding year (any one criterion); the spend uses the 3-year average.")

S('C1', """A company's management pays itself large bonuses linked to short-term sales while delaying necessary investment; shareholders' long-term value suffers. Lenders separately fear the owners will take on risky projects. Which statements are correct?
1. This illustrates the agency problem between shareholders and managers.
2. A conflict can also arise between shareholders and lenders.
3. Audit and independent directors are monitoring costs.
4. The agency problem can be eliminated completely by hiring professional managers.""",
  "1, 2 and 3 only", ["1, 2, 3 and 4", "1 and 4 only", "2 and 3 only"],
  "Professional managers are themselves agents; incentives and monitoring reduce, not eliminate, the problem.")

S('C1', """Five professionals want limited liability, perpetual succession, the ability to own property in the firm's name and flexibility without share capital. One proposes a partnership firm. Which is correct?""",
  "An LLP meets all these needs; a partnership firm has unlimited liability and no separate legal entity",
  ["A partnership firm meets all these needs", "Only a public company can meet these needs",
   "An LLP must issue share capital before commencing business"],
  "LLP Act 2008: body corporate, perpetual succession, limited liability, no share capital required.")

S('C1', """The CSR Committee of Shakti Engineering considers: (1) toilets in government schools; (2) a foreign holiday for top distributors; (3) a contribution to an approved disaster-relief fund; (4) skill training for unemployed youth; (5) sponsoring a cricket event with its brand on jerseys. Which qualify as CSR?""",
  "1, 3 and 4 only", ["1, 2, 3, 4 and 5", "3 and 5 only", "1, 4 and 5 only"],
  "Activities for business benefit or brand promotion (2, 5) are excluded from CSR.")

S('C1', """A company's CSR obligation is ₹30 lakh; it has spent ₹18 lakh on an ongoing three-year project by year-end. The Board proposes to carry the balance in General Reserve. Which is correct?""",
  "Transfer ₹12 lakh to an Unspent CSR Account in a scheduled bank within 30 days of year-end and spend it within 3 years",
  ["Carry ₹12 lakh in General Reserve as proposed", "Pay ₹12 lakh as a penalty to the Government",
   "Credit ₹12 lakh back to the P&L"],
  "Sec 135(6) applies to unspent amounts for ongoing projects.")

S('C1', """Which statements about the objective of financial management are correct?
1. Wealth maximisation considers the timing and risk of returns.
2. Profit maximisation ignores the time value of money.
3. Wealth maximisation means maximising this year's accounting profit.
4. The three core decisions are investment, financing and dividend.""",
  "1, 2 and 4 only", ["1, 2, 3 and 4", "2 and 3 only", "1 and 3 only"],
  "Wealth maximisation means maximising the market value of shares (NPV), not current-year profit.")
