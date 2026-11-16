from qb import note, Q

note('D5', r'''
<p class="small">Syllabus: Standard costing: definition, significance, types of standards, installation, variance analysis (material, labour, overhead), accounting and reporting. <b>Asked: 2 variance questions per session since Nov 2025, plus 1 on types of standards in older papers.</b> May 2026 asked:</p>
<ul class="small"><li>favourable price vs adverse usage</li>
<li>step-wise procedure</li>
<li>which is not a type of standard</li>
<li>direct material cost variance numerical</li>
<li>material usage definition</li></ul>

<h3>1. Basics</h3>
<ul><li><b>Standard cost:</b> a predetermined cost (quantity × price) of what a unit <b>should</b> cost under efficient conditions.</li>
<li><b>Variance</b> = Standard − Actual. Actual cost below standard = <b>Favourable (F)</b>; above = <b>Adverse (A)</b>.</li>
<li><b>Step-wise procedure:</b>
<ol><li>set standards</li>
<li>record actual costs</li>
<li>compare and compute variances</li>
<li>analyse causes</li>
<li>report to management and take corrective action</li></ol>
This is <b>management by exception</b>.</li>
<li><b>Types of standards:</b>
<ul><li><b>ideal</b> (perfect conditions)</li>
<li><b>normal</b> (average over a period)</li>
<li><b>basic</b> (base year, kept unchanged for trends)</li>
<li><b>current / expected / attainable</b> (achievable with effort; the most useful)</li></ul>
A "historical" or "budgeted-profit" standard is not one of the standard categories.</li>
<li><b>Benchmarking</b> sets standards by comparison with the best performers.</li></ul>

<h3>2. Material variances</h3>
<table><tr><th>Variance</th><th>Formula</th><th>Responsibility</th></tr>
<tr><td>Material cost variance (MCV)</td><td>(SQ × SP) − (AQ × AP)</td><td></td></tr>
<tr><td>Material price variance (MPV)</td><td>(SP − AP) × AQ</td><td>Purchase department</td></tr>
<tr><td>Material usage (quantity) variance (MUV)</td><td>(SQ − AQ) × SP</td><td>Production department</td></tr></table>
<p>SQ = standard quantity <b>for the actual output</b>. MCV = MPV + MUV.</p>
<p><b>Example:</b> 1,000 units at a standard of 2 kg × ₹10. Actual: 2,200 kg at ₹9.</p>
<ul><li>MPV = (10 − 9) × 2,200 = <b>₹2,200 F</b>.</li>
<li>MUV = (2,000 − 2,200) × 10 = <b>₹2,000 A</b>.</li>
<li>MCV = 20,000 − 19,800 = <b>₹200 F</b>.</li>
<li>So a cheap purchase was almost wiped out by wastage. "Price is lower, so overall performance is good" is wrong; both variances must be read.</li></ul>
<p class="small">The usage variance splits further into a mix variance and a yield variance when several materials are used.</p>

<h3>3. Labour variances</h3>
<table><tr><th>Variance</th><th>Formula</th></tr>
<tr><td>Labour cost variance</td><td>(SH × SR) − (AH × AR)</td></tr>
<tr><td>Labour rate variance</td><td>(SR − AR) × AH</td></tr>
<tr><td>Labour efficiency variance</td><td>(SH − AH) × SR (idle time is separated out where given)</td></tr></table>
<p><b>Example:</b> 500 units at a standard of 2 hours × ₹50. Actual: 1,100 hours at ₹48.</p>
<ul><li>Rate variance = ₹2,200 F.</li>
<li>Efficiency variance = (1,000 − 1,100) × 50 = ₹5,000 A.</li>
<li>Cost variance = ₹2,800 A.</li></ul>

<h3>4. Overheads (in brief)</h3>
<ul><li><b>Variable OH:</b> expenditure variance and efficiency variance.</li>
<li><b>Fixed OH:</b> expenditure (budget) variance and volume variance (capacity, efficiency, calendar).</li>
<li><b>Accounting treatment:</b> variances are usually written off to Costing P&amp;L at period end, or prorated if material.</li></ul>

<div class="box trap"><b>Traps:</b>
<ul><li>Price variance uses <b>actual quantity</b>; usage variance uses <b>standard price</b>.</li>
<li>SQ is for the <b>actual</b> output, not the budgeted output.</li>
<li>A favourable price variance can come with an adverse usage variance (cheap, poor-quality material).</li>
<li>Rate variance uses actual hours paid; efficiency uses the standard rate.</li></ul></div>
''')

Q('D5', """Standard: 2 kg per unit at ₹10 per kg. For an actual output of 1,000 units, 2,200 kg were used, bought at ₹9 per kg. What are the material price and usage variances?""",
  "Price ₹2,200 Favourable; Usage ₹2,000 Adverse", ["Price ₹2,000 Favourable; Usage ₹2,200 Adverse", "Price ₹2,200 Adverse; Usage ₹2,000 Favourable",
   "Price ₹200 Favourable; Usage nil"],
  "MPV = (SP − AP) × AQ = (10 − 9) × 2,200 = 2,200 F. MUV = (SQ − AQ) × SP = (2,000 − 2,200) × 10 = 2,000 A. Net MCV = 200 F.")

Q('D5', """Actual purchase price is lower than standard, but actual material consumption exceeds the standard quantity. The Production Manager says overall material performance is favourable because the price is lower. The correct view is:""",
  "A favourable price variance may be offset by an adverse usage variance",
  ["The material price variance alone decides efficiency", "Standard costing ignores the quantity of material consumed",
   "Usage variance is relevant only when production is below budget"],
  "Price variance is the buyer's responsibility; usage variance is production's. Cheap material often leads to more wastage.")

Q('D5', """Under standard costing, the difference between the standard quantity of material allowed for the actual output and the actual quantity used, valued at standard price, is the:""",
  "Material usage (quantity) variance", ["Material price variance", "Material cost variance", "Material yield variance only"],
  "MUV = (SQ − AQ) × SP. Price variance compares prices on actual quantity; cost variance is the total of both.")

Q('D5', """Standard: 2 labour hours per unit at ₹50 per hour. Actual output 500 units; actual hours 1,100 paid at ₹48 per hour. What is the labour efficiency variance?""",
  "₹5,000 Adverse", ["₹2,200 Favourable", "₹4,800 Adverse", "₹2,800 Adverse"],
  "Standard hours for actual output = 1,000. Efficiency variance = (SH − AH) × SR = (1,000 − 1,100) × 50 = 5,000 A. Rate variance = (50 − 48) × 1,100 = 2,200 F; total = 2,800 A.")

Q('D5', """Which is NOT normally a category of standards in standard costing?""",
  "Historical standard based on last year's actual cost", ["Ideal standard of perfect efficiency", "Basic standard kept unchanged for years", "Current (attainable) standard"],
  "Standards are classified as ideal, normal, basic and current/expected/attainable. Last year's actual cost is history, not a standard.")

Q('D5', """Which is the correct step-wise sequence in a standard costing system?""",
  "Set standards → record actuals → compute variances → analyse causes → report and take action",
  ["Record actuals → set standards from actuals → report → compute variances", "Compute variances → set standards → record actuals → analyse causes",
   "Set standards → report to management → record actuals → close the books"],
  "Standards are fixed first; actuals are compared, variances computed and investigated, and exceptions reported for corrective action.")

Q('D5', """Which standard is generally considered most useful for control and motivation?""",
  "Current (expected or attainable) standard", ["Ideal standard, because it shows perfect performance", "Basic standard, because it never changes",
   "Normal standard based only on past actuals"],
  "Attainable standards are achievable with efficient effort. Ideal standards demotivate; basic standards become outdated.")
