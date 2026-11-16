from qb import note, Q, money

note('A6', r'''
<p class="small">Syllabus: Meaning, causes, need and factors of depreciation; entries; SLM, WDV, units of production, sum-of-years'-digits; replacement and sinking fund; amortisation. <b>Asked: 4–5 questions every session from May 2025 onwards</b> (it was 1–2 earlier). May 2026 asked:</p>
<ul class="small"><li>SLM carrying amount</li>
<li>WDV book value after 3 years</li>
<li>choosing a method to match the benefit pattern</li>
<li>revision of life or residual value</li>
<li>zero carrying amount under SLM</li>
<li>sinking fund</li></ul>

<h3>1. Basics</h3>
<ul><li>Depreciation = allocation of the <b>depreciable amount</b> (cost − residual value) over the useful life. It is <b>allocation of cost, not valuation</b>.</li>
<li>It is a <b>non-cash</b> expense: it reduces profit but no cash goes out. That is why it is added back in the cash flow statement.</li>
<li><b>Causes:</b> wear and tear, efflux of time (leases, patents), obsolescence (technology), depletion (mines).</li>
<li><b>Factors:</b> cost, residual (salvage) value, useful life, method.</li>
<li>Starts when the asset is <b>available for use</b>, even if not yet used.</li>
<li><b>Land is not depreciated</b> (unlimited life), except quarries and mines, which are depleted.</li>
<li><b>Companies Act Schedule II</b> gives useful lives. Residual value is normally <b>not more than 5% of original cost</b>; a higher figure must be justified. Each significant component is depreciated separately (component approach, AS 10).</li>
<li>Depreciation is also called <b>amortisation</b> for intangibles and <b>depletion</b> for wasting assets.</li></ul>

<h3>2. Methods</h3>
<table><tr><th>Method</th><th>Formula</th><th>Pattern / suits</th></tr>
<tr><td><b>Straight line (SLM)</b></td><td>(Cost − Residual) ÷ Useful life</td><td>Equal charge each year. Suits assets giving even benefit (buildings, furniture, leases). Book value can reach <b>zero</b> (or the residual value).</td></tr>
<tr><td><b>Written down value (WDV)</b></td><td>Fixed % on the opening book value. Rate r = 1 − (S/C)<sup>1/n</sup></td><td>Higher charge early, lower later. Suits assets whose benefit is front-loaded and whose repairs rise later (plant, vehicles). Book value <b>never reaches zero</b>. The Income-tax Act uses WDV on blocks of assets.</td></tr>
<tr><td><b>Units of production</b></td><td>(Cost − Residual) × Units this year ÷ Total estimated units</td><td>Charge varies with use (machines, mines).</td></tr>
<tr><td><b>Sum of years' digits (SYD)</b></td><td>(Cost − Residual) × Remaining life at start of the year ÷ [n(n+1)/2]</td><td>Accelerated: declining charge.</td></tr>
<tr><td>Sinking fund</td><td>Equal annual amount is set aside and invested, so that with interest it accumulates to the replacement cost.</td><td>Provides <b>cash</b> for replacement (also used for debenture redemption).</td></tr></table>
<p><b>Combined effect:</b> under SLM, depreciation is constant and repairs rise, so the total burden rises. Under WDV, depreciation falls as repairs rise, so the total is more even. That is the classic argument for WDV.</p>

<h3>3. Worked numbers (practise until automatic)</h3>
<ol><li><b>SLM with installation and residual:</b> machine ₹48 lakh + installation ₹2 lakh, residual ₹5 lakh, life 9 years.
<ul><li>Annual depreciation = (50 − 5) ÷ 9 = ₹5 lakh.</li>
<li>After 3 years: 50 − 15 = <b>₹35 lakh</b>.</li></ul></li>
<li><b>WDV:</b> ₹3,00,000 at 20% for 3 years → 3,00,000 × 0.8³ = <b>₹1,53,600</b>. ₹4,00,000 at 20%, end of year 2 = <b>₹2,56,000</b>.</li>
<li><b>Part year, SLM:</b> ₹5,00,000 bought 1 Oct 2020, life 5 years, nil salvage. Depreciation is ₹1,00,000 a year. To 31 Mar 2024 that is 3.5 years = <b>₹3,50,000</b>.</li>
<li><b>Part year, WDV:</b> ₹2,40,000 bought 1 Jul 2024 at 15%.
<ul><li>FY 24-25: 2,40,000 × 15% × 9/12 = 27,000.</li>
<li>FY 25-26: (2,40,000 − 27,000) × 15% = <b>31,950</b>.</li></ul></li>
<li><b>Units:</b> cost ₹12 lakh, residual ₹2 lakh, total capacity 1,00,000 units, year-1 output 18,000 units → 10,00,000 × 18% = <b>₹1,80,000</b>.</li>
<li><b>SYD:</b> cost ₹6,50,000, salvage ₹50,000, life 5 years. Sum of digits = 15.
<ul><li>Year 1 = 5/15 × 6,00,000 = 2,00,000.</li>
<li>Year 2 = 4/15 × 6,00,000 = <b>1,60,000</b>.</li></ul></li>
<li><b>Sale of asset:</b> ₹5,00,000 bought 1 Apr 2023, WDV 20%, sold 30 Sep 2025 for ₹2,80,000.
<ul><li>Book value: 4,00,000 (end FY 23-24) → 3,20,000 (end FY 24-25) → less half-year 32,000 = 2,88,000.</li>
<li><b>Loss ₹8,000</b>, charged to P&amp;L.</li></ul></li>
<li><b>Revision of estimate (AS 10 / AS 5):</b> cost ₹1.80 crore, life 10 years, residual ₹20 lakh, so depreciation is ₹16 lakh a year.
<ul><li>After 5 years the carrying amount is ₹1 crore.</li>
<li>The residual value is revised to ₹8 lakh with the same remaining life of 5 years.</li>
<li>New charge = (100 − 8) ÷ 5 = <b>₹18.4 lakh a year</b>. Past years are not restated.</li></ul></li></ol>

<h3>4. Accounting entries</h3>
<ul><li><b>Without provision:</b> Depreciation Dr; To Asset A/c. The asset is shown at WDV.</li>
<li><b>With provision for depreciation (accumulated depreciation):</b> Depreciation Dr; To Provision for Depreciation. The asset stays at cost, and the provision is deducted in the Balance Sheet.</li>
<li><b>On sale with a provision:</b> transfer cost to an Asset Disposal A/c, transfer the accumulated depreciation, credit the sale proceeds; the balance is profit or loss.</li>
<li><b>Sinking fund:</b>
<ul><li>Each year: Depreciation Dr; To Sinking Fund. Then Sinking Fund Investment Dr; To Bank.</li>
<li>Interest received: Bank Dr; To Sinking Fund (reinvested).</li>
<li>The fund only provides money. It does not remove the obligation to repay or replace.</li></ul></li></ul>

<h3>5. Changes</h3>
<ul><li>Under AS 10, the <b>method, useful life and residual value</b> are reviewed at least at each financial year-end.</li>
<li>Any change is a <b>change in accounting estimate</b> and is applied <b>prospectively</b>: the remaining carrying amount less the new residual value is spread over the remaining life.</li>
<li>No restatement of past years.</li>
<li><b>Revaluation:</b> depreciation is then charged on the revalued amount. An increase goes to revaluation surplus; a decrease goes to P&amp;L (unless it reverses an earlier surplus).</li></ul>

<div class="box trap"><b>Traps:</b>
<ul><li>Installation, freight and trial-run costs are added to cost <b>before</b> computing depreciation.</li>
<li>WDV can never bring an asset to exactly zero. SLM with nil residual can.</li>
<li>"Higher early benefits, rising maintenance later" → <b>WDV</b>. "Benefits even over time" → SLM. "Benefits depend on output" → units of production.</li>
<li>Depreciation is not a source of funds. It only avoids an outflow of profit as dividend (retains funds).</li>
<li>A change of method is now a change in <b>estimate</b> (AS 10), not a change in policy.</li>
<li>Depreciation on an asset bought mid-year: SLM and WDV are both time-proportionate unless told "full year's depreciation in the year of purchase".</li></ul></div>
''')

def wdv(c, r, n): return c * (1 - r) ** n

Q('A6', f"""A machine costs ₹48 lakh plus ₹2 lakh installation; residual value ₹5 lakh; useful life 9 years; SLM. The company plans to sell it after 3 years. What is its carrying amount just before sale?""",
  "₹35 lakh", ["₹36.50 lakh", "₹33 lakh", "₹38.50 lakh"],
  "Cost = 48 + 2 = ₹50 lakh. Annual depreciation = (50 − 5)/9 = ₹5 lakh. After 3 years: 50 − 15 = ₹35 lakh. Ignoring installation gives a wrong answer.")

Q('A6', f"""A machine costing ₹4,00,000 is depreciated at 20% p.a. under the WDV method. What is its book value at the end of Year 2?""",
  f"₹{money(wdv(400000,0.2,2))}", ["₹2,40,000", "₹3,20,000", "₹2,88,000"],
  "Year 1: 4,00,000 − 80,000 = 3,20,000. Year 2: 3,20,000 − 64,000 = 2,56,000. (SLM at 20% of cost would give 2,40,000, which is the trap.)")

Q('A6', """A machine was bought for ₹5,00,000 on 1 October 2020; useful life 5 years; nil salvage; SLM; accounts close on 31 March. What is the total depreciation charged up to 31 March 2024?""",
  "₹3,50,000", ["₹4,00,000", "₹3,00,000", "₹3,75,000"],
  "Annual depreciation = 5,00,000/5 = 1,00,000. Period 1 Oct 2020 to 31 Mar 2024 = 3.5 years → ₹3,50,000.")

Q('A6', """Machinery costing ₹12,00,000 has an estimated residual value of ₹2,00,000 and a total production capacity of 1,00,000 units. In Year 1 it produced 18,000 units. Depreciation for Year 1 under the units-of-production method is:""",
  "₹1,80,000", ["₹2,16,000", "₹1,00,000", "₹2,00,000"],
  "Depreciable amount = 10,00,000. Per unit = ₹10. Year 1 = 18,000 × 10 = ₹1,80,000.")

Q('A6', """An asset costs ₹6,50,000, salvage value ₹50,000, life 5 years. Depreciation for Year 2 under the sum-of-the-years'-digits method is:""",
  "₹1,60,000", ["₹2,00,000", "₹1,20,000", "₹1,73,333"],
  "Sum of digits = 1+2+3+4+5 = 15. Year 2 uses the remaining life at the start of year 2, which is 4: 4/15 × 6,00,000 = ₹1,60,000.")

Q('A6', """A vehicle costing ₹2,40,000 was bought on 1 July 2024. Depreciation is 15% p.a. WDV, charged on a time basis; the year ends on 31 March. What is depreciation for FY 2025-26?""",
  "₹31,950", ["₹36,000", ["₹27,000"][0], "₹30,600"],
  "FY 24-25: 2,40,000 × 15% × 9/12 = 27,000 → WDV 2,13,000. FY 25-26: 2,13,000 × 15% = ₹31,950.")

Q('A6', """A machine bought on 1 April 2023 for ₹5,00,000 (WDV 20% p.a.) is sold on 30 September 2025 for ₹2,80,000. What is the profit or loss on sale?""",
  "Loss of ₹8,000", ["Profit of ₹40,000", "Loss of ₹40,000", "Profit of ₹8,000"],
  "WDV: 31-3-24 → 4,00,000; 31-3-25 → 3,20,000; depreciation for 6 months of FY 25-26 = 32,000 → 2,88,000 on 30-9-25. Sale 2,80,000 − 2,88,000 = loss ₹8,000.")

Q('A6', """Machinery cost ₹1.80 crore; useful life 10 years; residual value ₹20 lakh; SLM. After 5 years the residual value is revised to ₹8 lakh; remaining life unchanged. What is the annual depreciation from Year 6?""",
  "₹18.40 lakh", ["₹16 lakh", "₹17.20 lakh", "₹20.80 lakh"],
  "Old charge = (180 − 20)/10 = 16 lakh; carrying amount after 5 years = 180 − 80 = 100 lakh. Revised (prospective): (100 − 8)/5 = ₹18.40 lakh. Past depreciation is not recomputed (change in estimate).")

Q('A6', """A transport company buys electric buses. Utilisation is highest in the early years, maintenance rises in later years, and management wants the charge to follow how benefits are consumed. Which method fits, and why?""",
  "WDV, because it charges more in early years and less later, so depreciation plus repairs stays roughly even",
  ["SLM, because equal charges every year give the most accurate matching for vehicles", "Units of production, because the number of passengers carried decides the charge",
   "Sinking fund method, because it sets aside cash so the buses can be replaced later"],
  "WDV front-loads depreciation, matching higher early benefits and offsetting rising later repair costs. Units-of-production fits only if usage (km/units) is the driver and can be estimated; the facts here point to WDV.")

Q('A6', """Consider the following statements:
1. Under WDV, the book value of an asset never becomes zero.
2. Under SLM with nil residual value, the book value becomes zero at the end of useful life.
3. Depreciation is a process of valuation of fixed assets at market price.
4. Depreciation provides cash for replacement of assets.
Which are correct?""",
  "1 and 2 only", ["1, 2 and 3 only", "2 and 4 only", "1, 2 and 4 only"],
  "WDV applies a % to a falling balance, so it never reaches zero (1). SLM with nil residual writes off fully (2). Depreciation allocates cost; it does not value assets at market (3 wrong). It is a non-cash charge and does not by itself create cash; a sinking fund investment does (4 wrong).")

Q('A6', """Two identical machines cost ₹25 lakh each. Machine A: SLM over 10 years (nil residual). Machine B: WDV at 20%. Carrying amounts at the end of Year 3?""",
  "A ₹17.5 lakh; B ₹12.8 lakh", ["A ₹15 lakh; B ₹12.8 lakh", "A ₹17.5 lakh; B ₹15 lakh", "Both ₹17.5 lakh"],
  "SLM: 2.5 lakh a year × 3 = 7.5 → 17.5 lakh. WDV: 25 × 0.8³ = 12.8 lakh. WDV writes off more in the early years.")

Q('A6', """Under Schedule II of the Companies Act, 2013, the residual value of an asset is ordinarily:""",
  "Not more than 5% of the original cost, unless a higher value is justified and disclosed",
  ["Exactly 10% of the original cost in all cases, without exception", "Not less than 15% of the original cost, for all asset classes", "Nil, since Schedule II does not permit any residual value at all"],
  "Schedule II states that the residual value of an asset shall not ordinarily be more than 5% of its original cost. A different estimate needs justification and disclosure.")

Q('A6', """A company creates a sinking fund to replace a machine after 5 years. Which statements are correct?
1. Annual instalments are invested outside the business so that cash is available on replacement.
2. Interest received on sinking-fund investments is credited to the Sinking Fund Account.
3. Once the fund is created, depreciation is no longer charged to Profit and Loss.
4. The sinking fund removes the need to replace the asset.""",
  "1 and 2 only", ["1, 2 and 3 only", "2 and 3 only", "1, 2, 3 and 4"],
  "A sinking fund sets aside and invests a fixed amount each year; investment income is added to the fund. The annual amount is still charged to P&L as depreciation (3 wrong), and it only provides funds; it doesn't replace the asset (4 wrong).")

Q('A6', """Depreciation on a newly constructed factory should start from:""",
  "The date the factory is available for use, even if production has not begun",
  ["The date commercial production actually starts in the factory", "The date the first payment is made to the building contractor", "The beginning of the financial year following completion"],
  "Depreciation begins when the asset is available for use, i.e. in the location and condition needed to operate as intended (AS 10).")

Q('A6', """Which item is NOT depreciated?""",
  "Freehold land used for a factory", ["Leasehold land with a 30-year lease", "Factory building", "A mine (through depletion)"],
  "Freehold land has an unlimited useful life, so it is not depreciated. Leasehold land is written off over the lease period; buildings are depreciated; mines are depleted.")

Q('A6', """The WDV rate that reduces a ₹1,00,000 asset to a residual value of ₹10,000 in 5 years is closest to (given 0.1^(1/5) ≈ 0.631):""",
  "36.9%", ["18%", "20%", "63.1%"],
  "r = 1 − (S/C)^(1/n) = 1 − (10,000/1,00,000)^(1/5) = 1 − 0.631 = 0.369, i.e. about 36.9%.")
