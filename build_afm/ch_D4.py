from qb import note, Q

note('D4', r'''
<p class="small">Syllabus: Marginal costing (meaning, advantages, limitations, applications), break-even analysis, CVP, P/V ratio, margin of safety, absorption costing, income under marginal vs absorption costing. <b>Asked: 2–3 questions on marginal costing plus 1–3 on CVP every session, and absorption costing twice in May 2026.</b> May 2026 asked:</p>
<ul class="small"><li>special export order (twice)</li>
<li>margin of safety</li>
<li>marginal vs absorption statements</li>
<li>marginal vs standard costing</li></ul>

<h3>1. Marginal costing</h3>
<ul><li>Only <b>variable</b> costs are charged to products. <b>Fixed costs</b> are period costs, written off fully against the period's contribution.</li>
<li><b>Contribution</b> = Sales − Variable cost = Fixed cost + Profit.</li>
<li><b>P/V ratio</b> = Contribution ÷ Sales = ΔProfit ÷ ΔSales.</li>
<li><b>Break-even point:</b>
<ul><li>units = Fixed cost ÷ Contribution per unit</li>
<li>sales = Fixed cost ÷ P/V ratio</li></ul></li>
<li><b>Sales for a target profit</b> = (Fixed cost + Target profit) ÷ P/V (or ÷ contribution per unit for units).</li>
<li><b>Margin of safety (MoS)</b> = Actual (or budgeted) sales − BEP sales. MoS % = MoS ÷ Sales.
<br>Profit = MoS × P/V ratio. MoS is the <b>cushion before losses begin</b>.</li>
<li><b>Angle of incidence:</b> the angle between the sales and total-cost lines on a break-even chart. A wider angle means a higher rate of profit.</li></ul>

<h3>2. Worked numbers</h3>
<ul><li>SP ₹200, VC ₹120, fixed cost ₹1,60,000.
<ul><li>Contribution ₹80; P/V 40%.</li>
<li><b>BEP = 2,000 units = ₹4,00,000</b>.</li>
<li>For a profit of ₹2,00,000 → (1,60,000 + 2,00,000) ÷ 80 = <b>4,500 units</b>.</li></ul></li>
<li>Sales ₹15 crore, VC ratio 60%, FC ₹4.2 crore.
<ul><li>P/V 40%; BEP sales = ₹10.5 crore.</li>
<li><b>MoS = ₹4.5 crore (30%)</b>; profit = ₹1.8 crore.</li>
<li>If the price is cut 8% with the same volume: new sales 13.8, VC 9, contribution 4.8, P/V 34.8%, BEP rises to ₹12.075 crore, profit falls to ₹0.6 crore. That is why the CFO checks MoS first.</li></ul></li>
<li>Two periods: sales ₹1,00,000 with profit ₹10,000; sales ₹1,50,000 with profit ₹25,000.
<ul><li>P/V = 15,000 ÷ 50,000 = <b>30%</b>.</li>
<li>FC = 30,000 − 10,000 = 20,000.</li>
<li>BEP = ₹66,667.</li></ul></li></ul>

<h3>3. Decisions using contribution</h3>
<ul><li><b>Special or export order with idle capacity:</b> accept if price &gt; <b>variable cost</b> (positive contribution) and regular sales aren't affected.
<ul><li>SP ₹920, VC ₹610, allocated fixed ₹180; order at ₹700 → contribution ₹90, so <b>accept</b>.</li>
<li>"Price below total cost" is irrelevant when fixed costs are already covered.</li></ul></li>
<li><b>Make or buy:</b> compare the buy price with the <b>variable</b> cost of making (plus any avoidable fixed cost).</li>
<li><b>Key or limiting factor:</b> rank products by <b>contribution per unit of the limiting factor</b> (e.g. per machine-hour), not per unit.</li>
<li><b>Shut down or continue:</b> continue in the short run while contribution covers avoidable fixed costs.</li></ul>

<h3>4. Marginal vs absorption costing</h3>
<table><tr><th></th><th>Marginal</th><th>Absorption (full) costing</th></tr>
<tr><td>Fixed production overhead</td><td>Period cost (to P&amp;L)</td><td>Product cost (absorbed into units and stock)</td></tr>
<tr><td>Stock valuation</td><td>At variable cost (lower)</td><td>At full production cost. Required for <b>statutory financial statements</b> (AS 2)</td></tr>
<tr><td>Profit when production &gt; sales (stock rises)</td><td>Lower</td><td><b>Higher</b>: part of fixed OH is carried forward in stock</td></tr>
<tr><td>Profit when sales &gt; production (stock falls)</td><td>Higher</td><td>Lower</td></tr>
<tr><td>Production = sales</td><td colspan="2">Same profit</td></tr></table>
<ul><li><b>Difference in profit</b> = change in stock units × fixed OH rate per unit.
<br>Example: production 10,000, sales 8,000, fixed OH ₹50,000 (₹5 a unit) → absorption profit is higher by <b>₹10,000</b>.</li>
<li><b>Limitations of marginal costing:</b>
<ul><li>splitting semi-variable costs is hard</li>
<li>it ignores fixed costs in long-term pricing</li>
<li>stock is undervalued for external reporting</li></ul></li>
<li><b>Marginal costing vs standard costing:</b> different purposes. Marginal costing supports <b>decisions</b>; standard costing supports <b>control and performance evaluation</b>. They can run together.</li></ul>

<div class="box trap"><b>Traps:</b>
<ul><li>Accept a special order when price &gt; variable cost (with idle capacity), not when price &gt; total cost.</li>
<li>BEP in sales = FC ÷ <b>P/V</b>, not FC ÷ contribution per unit.</li>
<li>MoS shows the cushion, not profit. Profit = MoS × P/V.</li>
<li>A price cut lowers the P/V ratio, raises BEP and shrinks MoS.</li>
<li>Rising stock → absorption profit is higher.</li></ul></div>
''')

Q('D4', """A company sells at ₹200 per unit; variable cost is ₹120 per unit; fixed costs are ₹1,60,000. What is the break-even point?""",
  "2,000 units, i.e. sales of ₹4,00,000", ["1,333 units, i.e. sales of ₹2,66,667", "800 units, i.e. sales of ₹1,60,000", "2,000 units, i.e. sales of ₹2,40,000"],
  "Contribution = 80 per unit; BEP = 1,60,000/80 = 2,000 units. In sales: 1,60,000/0.40 = ₹4,00,000.")

Q('D4', """Same data (SP ₹200, VC ₹120, FC ₹1,60,000). How many units must be sold to earn a profit of ₹2,00,000?""",
  "4,500 units", ["2,500 units", "4,000 units", "3,000 units"],
  "Required contribution = 1,60,000 + 2,00,000 = 3,60,000; ÷ 80 = 4,500 units.")

Q('D4', """Sales ₹15 crore; variable cost ratio 60%; fixed cost ₹4.20 crore. What is the margin of safety?""",
  "₹4.5 crore, i.e. 30% of sales", ["₹10.5 crore, i.e. 70% of sales", "₹1.8 crore, i.e. 12% of sales", "₹6 crore, i.e. 40% of sales"],
  "P/V = 40%. BEP sales = 4.2/0.4 = ₹10.5 crore. MoS = 15 − 10.5 = ₹4.5 crore (30%). Profit = 4.5 × 40% = ₹1.8 crore.")

Q('D4', """In the same business (sales ₹15 crore, VC 60%, FC ₹4.2 crore), management cuts the price by 8% to gain market share, with volume unchanged. What happens to profit?""",
  "Profit falls from ₹1.8 crore to ₹0.6 crore as the P/V ratio drops to about 34.8%",
  ["Profit stays at ₹1.8 crore because fixed costs are unchanged", "Profit rises because the lower price increases contribution",
   "Profit falls by ₹0.12 crore, i.e. 8% of the earlier ₹1.8 crore"],
  "New sales = 13.8; VC stays 9.0; contribution = 4.8; profit = 4.8 − 4.2 = 0.6. The whole price cut (₹1.2 crore) comes straight out of profit unless volume rises.")

Q('D4', """A firm operates at 72% capacity: SP ₹580, VC ₹360, fixed costs already covered. A foreign buyer offers ₹410 per unit for extra units; domestic sales unaffected. What should the firm do?""",
  "Accept, because each unit adds ₹50 contribution without affecting existing business",
  ["Reject, because the price is below the normal selling price of ₹580", "Reject, because export prices must never be below domestic prices",
   "Accept only if depreciation is excluded from fixed costs"],
  "With idle capacity and fixed costs already recovered, any price above variable cost raises total profit: 410 − 360 = ₹50 per unit.")

Q('D4', """Sales ₹1,00,000 give a profit of ₹10,000; sales ₹1,50,000 give a profit of ₹25,000. What are the P/V ratio and fixed cost?""",
  "P/V 30%; fixed cost ₹20,000", ["P/V 10%; fixed cost ₹0", "P/V 30%; fixed cost ₹30,000", "P/V 16.7%; fixed cost ₹6,667"],
  "P/V = change in profit ÷ change in sales = 15,000/50,000 = 30%. Contribution at ₹1,00,000 = 30,000; FC = 30,000 − 10,000 = ₹20,000.")

Q('D4', """A company produced 10,000 units and sold 8,000; fixed production overhead is ₹50,000; no opening stock. Compared with marginal costing, profit under absorption costing will be:""",
  "Higher by ₹10,000", ["Lower by ₹10,000", "Higher by ₹50,000", "The same"],
  "Fixed OH per unit = ₹5. Under absorption costing, 2,000 units in closing stock carry ₹10,000 of fixed OH to the next period, so this period's profit is ₹10,000 higher.")

Q('D4', """Which statements on marginal vs absorption costing are correct?
1. Under marginal costing, fixed production overhead is treated as a period cost.
2. Absorption costing values closing stock at full production cost, as required for statutory financial statements.
3. When production exceeds sales, absorption costing shows lower profit than marginal costing.
4. When production equals sales, both show the same profit.""",
  "1, 2 and 4 only", ["1, 2, 3 and 4", "1 and 3 only", "2, 3 and 4 only"],
  "When stock builds up, absorption costing defers part of fixed OH in stock, so it shows HIGHER profit (3 wrong).")

Q('D4', """Products A and B both use a scarce machine. A: contribution ₹60/unit using 3 machine-hours. B: contribution ₹45/unit using 1.5 machine-hours. Which should be preferred when machine-hours are the limiting factor?""",
  "B, because it earns ₹30 per machine-hour against A's ₹20", ["A, because it earns more contribution per unit",
   "Both equally, because both have positive contribution", "A, because it uses more machine time and absorbs more overhead"],
  "Rank by contribution per unit of the limiting factor: A = 60/3 = 20; B = 45/1.5 = 30.")

Q('D4', """The Production Director wants standard costing for performance evaluation; the Marketing Director wants marginal costing for a special-order decision. The MD thinks adopting one removes the need for the other. Which is correct?""",
  "They serve different purposes and can be used together",
  ["Standard costing completely replaces marginal costing", "Marginal costing is compulsory for statutory financial reporting",
   "Both systems always give identical product costs"],
  "Standard costing sets benchmarks and analyses variances; marginal costing separates fixed and variable costs for short-term decisions. They complement each other.")
