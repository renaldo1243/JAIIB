from qb import note, Q

note('C4', r'''
<p class="small">Syllabus: Debt, bonds, terms, types, optionality, valuation (annual and semi-annual), current yield, YTM, bond theorems, duration, properties of duration, price volatility. <b>Asked: 4–6 questions every session</b> (features 2, theorems 1–2, CY/YTM/duration 2–3). May 2026 had 7 bond questions:</p>
<ul class="small"><li>lower coupon falls more</li>
<li>longer maturity falls more</li>
<li>YTM above or below coupon</li>
<li>CY vs YTM</li>
<li>modified duration in a portfolio case</li>
<li>bond trading at a premium</li>
<li>properties of duration</li></ul>

<h3>1. Terms</h3>
<ul><li><b>Face / par value</b>: amount on which the coupon is paid. Usually also the <b>redemption value</b>: the specified amount repaid at maturity.</li>
<li><b>Coupon</b>: periodic interest received by the investor (rate × face value).</li>
<li><b>Maturity</b>: term to redemption.</li>
<li><b>Market price</b>: present value of future cash flows at the market yield.</li>
<li>Coupon &gt; market yield → <b>premium</b> (price &gt; par). Coupon &lt; yield → <b>discount</b>. Coupon = yield → <b>par</b>.</li></ul>

<h3>2. Types</h3>
<table><tr><th>Type</th><th>Feature</th></tr>
<tr><td>Zero-coupon / deep discount</td><td>No coupon; issued at a discount, redeemed at par. <b>Duration = maturity.</b></td></tr>
<tr><td>Floating rate bond</td><td>Coupon reset to a benchmark (T-bill, MIBOR) + spread. Low price risk.</td></tr>
<tr><td>Convertible</td><td>Can be converted into equity shares on stated terms.</td></tr>
<tr><td><b>Callable</b></td><td><b>Issuer</b> may redeem early (used when rates fall). Investor demands a higher yield.</td></tr>
<tr><td><b>Puttable</b></td><td><b>Investor</b> may sell back to the issuer early (useful when rates rise). Lower yield.</td></tr>
<tr><td>Perpetual</td><td>No maturity. Price = coupon ÷ yield. (Banks' AT1 bonds are perpetual.)</td></tr>
<tr><td>Inflation-indexed</td><td>Principal and/or coupon linked to an inflation index.</td></tr>
<tr><td>STRIPS</td><td>Coupons and principal of a G-sec traded as separate zero-coupon securities.</td></tr>
<tr><td>Asset-backed security</td><td>Backed by a pool of loans (auto, credit-card, mortgage = MBS). A plain G-sec or corporate debenture is <b>not</b> an ABS.</td></tr></table>

<h3>3. Valuation and yields</h3>
<div class="box key">
<b>Price</b> = C × PVAF(y, n) + F ÷ (1 + y)<sup>n</sup>. For semi-annual coupons use C/2, y/2 and 2n.<br>
<b>Current yield</b> = Annual coupon ÷ Market price.<br>
<b>YTM</b> = the rate that equates price with the PV of all coupons and the redemption value: the IRR of holding to maturity.<br>
<b>Approximate YTM</b> = [C + (F − P) ÷ n] ÷ [(F + P) ÷ 2].</div>
<ul><li>9% coupon, ₹1,000, 5 years, market yield 10% → price ≈ <b>₹962.09</b> (discount).</li>
<li>12% coupon, 5 years, yield 10% → <b>₹1,075.82</b> (premium).</li>
<li>Coupon 15%, price ₹1,500 → current yield = 150 ÷ 1,500 = <b>10%</b>.</li>
<li>8% coupon, price ₹920, 6 years → approx YTM = (80 + 13.33) ÷ 960 = <b>9.72%</b> (exact 9.83%). <b>YTM &gt; current yield (8.70%) &gt; coupon (8%)</b> for a discount bond. For a premium bond the order reverses: coupon &gt; CY &gt; YTM.</li>
<li>Zero-coupon ₹1,000 in 5 years at 8% → <b>₹680.58</b>.</li>
<li>CY ignores capital gain or loss and time value; YTM includes both. They are equal only at par.</li></ul>

<h3>4. Bond theorems (Malkiel) — learn all six</h3>
<ol><li>Bond prices move <b>inversely</b> to yields.</li>
<li><b>Longer maturity → greater price sensitivity</b> to a given yield change.</li>
<li>That sensitivity rises with maturity but at a <b>decreasing rate</b>.</li>
<li>For the same size of change, the <b>price rise when yields fall is larger than the price fall when yields rise</b> (convexity).</li>
<li><b>Lower coupon → greater % price sensitivity</b> (more value sits in the distant redemption).</li>
<li>The price change is proportionally smaller for a bond with a higher initial yield.</li></ol>
<p><b>Example (same 4-year maturity):</b> yield rises 8% → 11%.</p>
<ul><li>8% coupon bond: falls from 1,000.00 to 906.93, i.e. <b>−9.31%</b>.</li>
<li>12% coupon bond: falls from 1,132.49 to 1,031.02, i.e. <b>−8.96%</b>.</li></ul>
<p>The lower coupon falls more.</p>

<h3>5. Duration</h3>
<ul><li><b>Macaulay duration:</b> weighted average time to receive the bond's cash flows (weights = PV of each flow ÷ price). Measured in years.</li>
<li><b>Modified duration</b> = Macaulay duration ÷ (1 + y/m).
<br><b>% price change ≈ −MD × Δyield.</b> MD 4.8 and yield +0.5% → price ≈ −2.4%.</li>
<li><b>Properties:</b>
<ul><li>A zero-coupon bond's duration = its maturity.</li>
<li>A coupon bond's duration is <b>less than</b> its maturity.</li>
<li>Higher coupon → lower duration.</li>
<li>Higher yield → lower duration.</li>
<li>Longer maturity → generally higher duration.</li>
<li>Duration of a perpetuity = (1 + y) ÷ y.</li></ul></li>
<li><b>Example:</b> 3-year 10% bond at 10% yield → D = <b>2.74 years</b>, MD = <b>2.49</b>.</li>
<li><b>Portfolio use:</b> expecting rates to rise → <b>shorten</b> duration (sell long bonds). Expecting rates to fall → lengthen. Banks use duration-gap analysis for ALM.</li></ul>

<div class="box trap"><b>Traps:</b>
<ul><li>"Higher coupon bonds are riskier, so they fall more": wrong. The <b>lower</b> coupon falls more.</li>
<li>"Short bond carries the most interest-rate risk because it matures first": wrong. The longest maturity carries the most.</li>
<li>Duration is in years; modified duration is % per 1% change in yield.</li>
<li>Callable = issuer's option. Puttable = investor's option.</li>
<li>Market yield &lt; coupon → bond is at a <b>premium</b>.</li></ul></div>
''')

Q('C4', """Two bonds of the same company: Bond A (8% coupon, 4 years) and Bond B (12% coupon, 4 years). Market yields jump from 8% to 11%. Which statement is correct?""",
  "Bond A falls by about 9.3% and Bond B by about 9.0%; the lower-coupon bond is more sensitive",
  ["Bond B falls more, because higher-coupon bonds always carry more interest-rate risk", "Both fall by exactly the same percentage, because maturity is identical",
   "Bond B's price rises, because investors prefer higher coupons when rates rise"],
  "A: 1,000 → 906.93 (−9.31%). B: 1,132.49 → 1,031.02 (−8.96%). For the same maturity, the lower coupon puts more value in the distant redemption, so its price is more sensitive.")

Q('C4', """A pension fund holds three 7% G-secs maturing in 3, 8 and 18 years. RBI is expected to raise rates. Which statements are correct?
1. The 18-year bond should show the largest percentage fall.
2. The 3-year bond carries the highest interest-rate risk because it matures first.
3. Longer maturity generally means greater price sensitivity.
4. Since coupons are equal, maturity does not affect volatility.""",
  "1 and 3 only", ["2 and 4 only", "1, 2 and 3 only", "1, 3 and 4 only"],
  "Bond theorem: for a given yield change, longer maturity → bigger % change. The short bond has the least rate risk; maturity matters even with equal coupons.")

Q('C4', """A ₹1,000 bond carries a 9% annual coupon and matures in 5 years at par. If the market yield is 10%, its price is closest to:""",
  "₹962", ["₹1,000", "₹1,038", "₹909"],
  "Price = 90 × PVAF(10%, 5) + 1,000/1.1^5 = 90 × 3.7908 + 620.92 = 341.17 + 620.92 = ₹962.09. Coupon below yield → discount.")

Q('C4', """When the current market yield is LOWER than a bond's coupon rate, the bond trades at:""",
  "A premium to its face value", ["A discount to its face value", "Exactly its face value", "Its redemption value plus accrued interest only"],
  "Investors pay more than par for a coupon above the going yield. Price falls back to par as maturity nears (pull to par).")

Q('C4', """A bond of face value ₹1,000 with a 15% coupon is quoted at ₹1,500. Its current yield is:""",
  "10%", ["15%", "22.5%", "5%"], "Current yield = annual coupon ÷ market price = 150 ÷ 1,500 = 10%.")

Q('C4', """An 8% bond (face ₹1,000, redeemable at par in 6 years) is bought at ₹920. Using the approximation formula, its YTM is about:""",
  "9.72%", ["8.70%", "8.00%", "10.43%"],
  "Approx YTM = [80 + (1,000 − 920)/6] ÷ [(1,000 + 920)/2] = (80 + 13.33)/960 = 9.72%. 8.70% is the current yield (80/920). For a discount bond: YTM > CY > coupon.")

Q('C4', """Bond X (9% coupon) is bought at ₹960 and Bond Y (9% coupon) at ₹1,050; both mature at par in 5 years. Which statements are correct?
1. X's YTM is higher than 9%.
2. Y's YTM is lower than 9%.
3. The gap between purchase price and redemption value affects YTM.
4. Coupon rate and YTM are always equal.""",
  "1, 2 and 3 only", ["1 and 4 only", "2 and 3 only", "1, 2, 3 and 4"],
  "Buying below par adds a capital gain (YTM > coupon); buying above par adds a capital loss (YTM < coupon). They are equal only when bought at par.")

Q('C4', """A trainee says the current yield of a bond bought at ₹920 is the total return if held to maturity. What is wrong?""",
  "Current yield considers only coupon versus price; YTM also includes the gain on redemption and the time value of money",
  ["Nothing is wrong: current yield and YTM are always identical for any bond held to maturity", "YTM ignores the redemption value and uses only the coupon received during the holding period",
   "Current yield applies only to Government securities and not to corporate bonds"],
  "CY = 80/920 = 8.70% captures income only; the ₹80 gain on redemption at par and its timing are captured only in YTM.")

Q('C4', """A treasury portfolio has Bond A (MD 2.6), Bond B (MD 4.8) and Bond C (MD 7.2). Rates are expected to rise. Which statements are correct?
1. Bond C has the highest interest-rate risk.
2. Modified duration approximates the % price change for a 1% change in yield.
3. If yields rise 1%, Bond A will fall more than Bond C.
4. Managers usually shorten portfolio duration when they expect rates to rise.""",
  "1, 2 and 4 only", ["2 and 3 only", "1 and 3 only", "1, 2, 3 and 4"],
  "%ΔP ≈ −MD × Δy, so C (7.2) falls about 7.2% and A about 2.6% for a 1% rise. Shortening duration reduces losses when rates rise.")

Q('C4', """A bond has a modified duration of 4.8. If its yield rises by 50 basis points, its price will change by approximately:""",
  "−2.4%", ["+2.4%", "−4.8%", "−9.6%"], "%ΔP ≈ −MD × Δy = −4.8 × 0.5% = −2.4%.")

Q('C4', """Which of the following is NOT a property of bond duration?""",
  "A coupon bond's duration is always greater than its maturity",
  ["A zero-coupon bond's duration equals its maturity", "The higher the coupon rate, the lower the duration",
   "The higher the yield, the lower the duration"],
  "A coupon bond pays cash before maturity, so its weighted-average time (duration) is less than maturity. The others are standard properties.")

Q('C4', """For a 3-year bond with a 10% annual coupon priced at par (yield 10%), the Macaulay duration and modified duration are about:""",
  "2.74 years and 2.49", ["3.00 years and 2.73", "2.49 years and 2.74", "2.74 years and 3.01"],
  "Weights: 100/1.1 = 90.91, 100/1.21 = 82.64, 1,100/1.331 = 826.45. D = (1×90.91 + 2×82.64 + 3×826.45)/1,000 = 2.7355. MD = 2.7355/1.10 = 2.487.")

Q('C4', """Which statements on bond theorems are correct?
1. Bond prices move inversely to market yields.
2. For a given change in yield, the price rise when yields fall exceeds the price fall when yields rise by the same amount.
3. Price sensitivity increases with maturity, but at a decreasing rate.
4. Higher-coupon bonds show larger percentage price changes than lower-coupon bonds of the same maturity.""",
  "1, 2 and 3 only", ["1, 2, 3 and 4", "1 and 4 only", "2, 3 and 4 only"],
  "Statement 4 reverses theorem 5: lower-coupon bonds are more sensitive. The convexity property (2) and decreasing-rate sensitivity (3) are part of Malkiel's theorems.")

Q('C4', """A company issues a bond that gives the ISSUER the right to redeem it before maturity. Such a bond is called a:""",
  "Callable bond", ["Puttable bond", "Convertible bond", "Perpetual bond"],
  "Callable = issuer's option to redeem early (typically when rates fall). Puttable = investor's option to sell back. Convertible = option to convert into equity.")

Q('C4', """Which of the following is NOT an asset-backed security?""",
  "A plain dated Government of India security", ["A mortgage-backed security", "A security backed by a pool of auto loans",
   "A pass-through certificate on credit-card receivables"],
  "ABS are created by securitising pools of loans or receivables. A G-sec is a direct sovereign obligation with no pool of assets behind it.")

Q('C4', """The price of a zero-coupon bond of face value ₹1,000 maturing in 5 years, at a yield of 8%, is closest to:""",
  "₹681", ["₹600", "₹920", "₹735"],
  "Price = 1,000/1.08^5 = 1,000/1.4693 = ₹680.58. Its duration equals 5 years.")
