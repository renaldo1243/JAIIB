from qb import note, Q

note('D6', r'''
<p class="small">Syllabus: Budget concept, budget manual, fixed and flexible budgets, types of budgets, budgetary control (advantages, limitations, installation), zero-based budgeting, programme and performance budgeting. <b>Asked: 1–2 on types of budgets plus about 1 on ZBB per session.</b> May 2026 asked: budget centre, a management-accounting match, ZBB and budgetary control.</p>

<h3>1. Concepts</h3>
<ul><li><b>Budget:</b> a quantitative plan for a future period, prepared and approved in advance.</li>
<li><b>Budgetary control:</b> setting budgets, comparing actuals, and acting on variances.</li>
<li><b>Budget centre:</b> a section of the organisation (department or function) for which a budget is prepared and a manager is <b>responsible</b> for its performance.</li>
<li><b>Budget manual:</b> a written document of procedures, responsibilities and the timetable.</li>
<li><b>Budget committee:</b> coordinates the process. The <b>budget officer</b> is its secretary.</li>
<li><b>Principal (key or limiting) budget factor:</b> the factor that limits activity (often sales demand, or capacity). It is budgeted first.</li></ul>

<h3>2. Types</h3>
<table><tr><th>Basis</th><th>Types</th></tr>
<tr><td>Function</td><td>Sales (usually first), production, materials, labour, overheads, cash, capital expenditure. These lead to the <b>master budget</b> (budgeted P&amp;L and balance sheet).</td></tr>
<tr><td>Time</td><td>Long-term, short-term, current, <b>rolling (continuous)</b>: add a new period as one ends.</td></tr>
<tr><td>Flexibility</td><td><b>Fixed (static)</b>: one activity level, so it is a poor control tool if output changes.<br><b>Flexible</b>: cost allowances for different activity levels. It separates fixed and variable costs and gives a meaningful comparison with actuals.</td></tr></table>
<p><b>Flexible budget example:</b> at 10,000 units, variable cost is ₹5 a unit and fixed cost ₹40,000.</p>
<ul><li>At 12,000 units the allowance = 60,000 + 40,000 = <b>₹1,00,000</b>, not ₹90,000 × 1.2.</li></ul>
<p><b>Cash budget:</b> shows month-wise surpluses and deficits. Banks use it to set limits for seasonal businesses.</p>

<h3>3. Zero-based budgeting (ZBB)</h3>
<ul><li>Every activity is justified <b>from scratch (zero)</b> each period, as if new. Nothing is carried forward from the last budget.</li>
<li>Activities are grouped into <b>decision packages</b> and ranked by cost-benefit.</li>
<li>Pioneered by Peter Pyhrr at Texas Instruments. Adopted by the Government of India in 1986–87.</li>
<li><b>Advantages:</b> removes waste and obsolete activities, links spending to objectives.</li>
<li><b>Disadvantages:</b> time-consuming, needs skilled managers, paperwork.</li>
<li>Contrast with <b>incremental budgeting</b>: last year's budget + an adjustment.</li></ul>

<h3>4. Performance and programme budgeting</h3>
<ul><li><b>Performance budgeting:</b> links money spent to <b>outputs and results</b> (physical targets). Used in Government, and now "outcome budgeting".</li>
<li><b>Programme budgeting:</b> classifies expenditure by programmes or objectives, not by departments.</li></ul>

<h3>5. Budgetary control</h3>
<ul><li><b>Advantages:</b> planning, coordination, communication, control, motivation, responsibility.</li>
<li><b>Limitations:</b> based on estimates, rigidity, costly, may cause conflict or padding.</li>
<li><b>Installation steps:</b>
<ol><li>organisation chart and budget centres</li>
<li>budget manual and committee</li>
<li>budget period</li>
<li>key factor</li>
<li>prepare and approve budgets</li>
<li>compare and report</li></ol></li></ul>

<div class="box trap"><b>Traps:</b>
<ul><li>ZBB starts from zero; incremental starts from last year.</li>
<li>A flexible budget suits control when activity changes. A fixed budget doesn't.</li>
<li>The sales budget usually comes first because sales is the usual key factor.</li>
<li>A budget centre has a <b>responsible manager</b>.</li>
<li>The master budget is the summary of all functional budgets.</li></ul></div>
''')

Q('D6', """Zero-Base Budgeting is a technique in which:""",
  "Every activity must be justified afresh each period, starting from zero",
  ["The previous year's budget is taken as the base and adjusted for inflation", "Only activities with zero cost are included in the budget",
   "Budgets are prepared only when the company makes zero profit"],
  "ZBB starts each budget from zero; managers justify each decision package. Incremental budgeting uses last year's figures as the base.")

Q('D6', """A budget centre is best described as:""",
  "A section with its own budget and a manager responsible for it",
  ["The department that prepares all budgets for the organisation", "A centre where only revenue is budgeted, never costs",
   "The meeting place of the budget committee"],
  "Budget centres are responsibility areas (departments or functions) with their own budgets, which enables control by comparing actuals with budget.")

Q('D6', """At 10,000 units, budgeted costs are ₹90,000 (variable ₹5 per unit; fixed ₹40,000). Under a flexible budget, what is the cost allowance at 12,000 units?""",
  "₹1,00,000", ["₹1,08,000", "₹90,000", "₹1,20,000"],
  "Variable 12,000 × 5 = 60,000 + fixed 40,000 = ₹1,00,000. Scaling the whole budget (90,000 × 1.2 = 1,08,000) wrongly treats fixed costs as variable.")

Q('D6', """Which budget is usually prepared FIRST because sales is generally the principal budget factor?""",
  "Sales budget", ["Cash budget", "Capital expenditure budget", "Master budget"],
  "Production, materials, labour and cash budgets depend on expected sales; the master budget is compiled last.")

Q('D6', """Which statements about budgets are correct?
1. A fixed budget is designed for one level of activity.
2. A flexible budget is more useful for control when actual activity differs from budget.
3. A rolling budget is continuously updated by adding a new period as one ends.
4. Performance budgeting links expenditure to physical outputs and results.""",
  "1, 2, 3 and 4", ["1 and 2 only", "1, 2 and 3 only", "2, 3 and 4 only"],
  "All four are standard features of budget types.")

Q('D6', """The written document setting out budgeting procedures, responsibilities and the budget timetable is called the:""",
  "Budget manual", ["Master budget", "Budget centre", "Cash budget"],
  "The budget manual documents the procedures and responsibilities; the master budget is the summarised budget for the organisation.")
