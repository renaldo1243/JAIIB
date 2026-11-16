from qb import note, Q

note('D3', r'''
<p class="small">Syllabus: Cost &amp; management accounting overview (concepts, classification, elements, cost centre and unit, methods and techniques); costing methods: unit, job, batch, contract, process (normal and abnormal loss, equivalent units, joint and by-products), service, multiple. <b>Asked: 3–4 questions on methods and techniques plus 2 on job/contract every session.</b> May 2026 asked:</p>
<ul class="small"><li>multiple costing for an AC maker</li>
<li>job costing for pressure vessels</li>
<li>a method for pipes, kitchens and fasteners</li>
<li>features of multiple costing</li>
<li>batch cost of tyres</li>
<li>management-accounting match</li>
<li>direct cost definition</li>
<li>normal loss treatment</li></ul>
<p class="small">Cost accounting standards and the evolution of management accounting are left out (not asked).</p>

<h3>1. Basics</h3>
<ul><li><b>Elements of cost:</b>
<ul><li>direct material + direct labour + direct expenses = <b>prime cost</b></li>
<li>+ factory overheads = <b>works/factory cost</b></li>
<li>+ office and administration overheads = <b>cost of production</b></li>
<li>+ selling and distribution overheads = <b>cost of sales</b></li>
<li>+ profit = selling price</li></ul></li>
<li><b>Direct cost:</b> traceable to a specific cost unit economically (e.g. wood for a table). <b>Indirect cost (overhead):</b> shared, so it is apportioned (factory rent).</li>
<li><b>By behaviour:</b>
<ul><li>fixed: total constant, per-unit falls as output rises</li>
<li>variable: per-unit constant, total varies</li>
<li>semi-variable</li></ul></li>
<li><b>Cost centre:</b> a location, person or equipment for which costs are collected. <b>Cost unit:</b> the unit of output costed: per tonne, per km, per passenger-km, per batch, per job, per kWh.</li>
<li><b>Methods vs techniques:</b>
<ul><li><b>Methods</b> fit the type of production: job, batch, contract, process, operating/service, unit/output, multiple.</li>
<li><b>Techniques</b> are tools used with any method: marginal costing, standard costing, budgetary control, uniform costing, absorption costing.</li></ul></li>
<li><b>Cost vs financial vs management accounting:</b>
<ul><li>financial: external reporting, historical, legally required</li>
<li>cost: ascertaining and controlling cost</li>
<li>management accounting: wider, for decisions and planning, using cost and financial data</li></ul></li></ul>

<h3>2. Which method fits which industry</h3>
<table><tr><th>Method</th><th>Production type</th><th>Examples</th></tr>
<tr><td><b>Job costing</b></td><td>Each order is unique, to customer specification; a job cost card per job</td><td>Printing press, custom pressure vessels, repair shops, modular kitchens, furniture to order</td></tr>
<tr><td><b>Batch costing</b></td><td>Identical units in lots; cost per batch ÷ units in the batch</td><td>Fasteners, medicines, biscuits, tyres in a lot, toys, garments</td></tr>
<tr><td><b>Contract costing</b></td><td>Large, long-duration job at a site; each contract is a cost unit</td><td>Construction, shipbuilding, bridges</td></tr>
<tr><td><b>Process costing</b></td><td>Continuous mass production through sequential processes; the output of one process is the input of the next</td><td><b>Chemicals, oil refining, paper</b>, sugar, cement, textiles, steel pipes</td></tr>
<tr><td><b>Service (operating) costing</b></td><td>Services; composite cost units</td><td>Transport (passenger-km), hospitals (patient-day), power, hotels</td></tr>
<tr><td><b>Unit / output costing</b></td><td>Single product, uniform units</td><td>Bricks, mining, dairy</td></tr>
<tr><td><b>Multiple (composite) costing</b></td><td><b>Combination</b> of methods for a product with many components made differently, assembled into one product</td><td>Cars, aircraft, AC systems, radios</td></tr></table>
<p>One company can and should use <b>different methods for different stages</b>: process for compressors, batch for coils, job for each installation, and contract-wise for AMCs. Forcing one uniform method distorts cost.</p>

<h3>3. Job vs contract costing</h3>
<table><tr><th>Job</th><th>Contract</th></tr>
<tr><td>Small, short duration, usually in the factory</td><td>Large, long duration (often over a year), at the customer's site</td></tr>
<tr><td>Overheads apportioned on a basis</td><td>Most costs are direct (site rent, plant, supervisor)</td></tr>
<tr><td>Profit taken on completion</td><td>Profit on <b>incomplete contracts</b> taken by stage of completion (AS 7)</td></tr></table>
<p><b>Contract terms:</b></p>
<ul><li><b>Progress payments</b> on architect's certificates, less <b>retention money</b> (a % kept back as security for defects).</li>
<li><b>Escalation clause:</b> the price is raised if input costs rise.</li>
<li><b>Work certified</b> vs uncertified.</li>
<li>Plant at site: depreciated, or charged at a usage rate.</li>
<li>Notional profit = value of work certified − cost of work certified. The traditional rule takes a fraction of notional profit (e.g. 2/3 × cash received ÷ work certified), adjusted for the stage of completion.</li></ul>

<h3>4. Process costing</h3>
<ul><li><b>Normal loss:</b> expected and unavoidable (evaporation, shrinkage). Its cost is <b>absorbed by good units</b>: it raises their cost per unit. Any scrap value is credited to the process.</li>
<li><b>Abnormal loss:</b> loss beyond normal (accident, carelessness). It is valued <b>like good output</b> and transferred to <b>Costing P&amp;L</b>.</li>
<li><b>Abnormal gain:</b> actual loss is less than normal. Debit the process at the good-unit rate; the net amount (less the scrap value forgone) is credited to Costing P&amp;L.</li>
<li><b>Example:</b> input 1,000 units, total cost ₹92,000, normal loss 10% (scrap ₹20 a unit), output 850.
<ul><li>Cost per unit = (92,000 − 2,000) ÷ 900 = <b>₹100</b>.</li>
<li>Abnormal loss = 50 units = <b>₹5,000</b>.</li>
<li>Good output = ₹85,000.</li></ul></li>
<li><b>Equivalent units:</b> convert WIP into complete units (e.g. 200 units 60% done = 120 EU).</li>
<li><b>Joint products:</b> equally important (petrol and diesel). <b>By-products:</b> minor value (molasses from sugar).</li>
<li><b>Inter-process profit:</b> transfer at a price above cost; the unrealised profit in stock is eliminated.</li></ul>

<div class="box trap"><b>Traps:</b>
<ul><li>Unique customer orders → <b>job</b>, not process.</li>
<li>Many components assembled → <b>multiple</b> costing.</li>
<li>Normal loss → absorbed by good units. Abnormal loss → Costing P&amp;L at full cost.</li>
<li>Marginal and standard costing are <b>techniques</b>, not methods; they don't replace job or process costing.</li>
<li>Retention money is held back by the contractee, not paid to the contractor yet.</li></ul></div>
''')

Q('D3', """Omega Engineering makes AC systems: compressors in continuous processing, copper coils in batches, installation separately for each customer, and AMCs tracked customer-wise. The Finance Director wants one uniform costing method. The cost accountant objects because:""",
  "Stages use resources differently, so process, batch and job costing together work better",
  ["Process costing alone is accurate because everything becomes one system", "Marginal costing removes the need for any product-costing method",
   "Uniform costing is prohibited by Cost Accounting Standards for installation work"],
  "The method should match the nature of each activity: continuous → process; lots → batch; customer-specific → job/contract. Using several methods for one final product is multiple costing.")

Q('D3', """Precision Fabricators makes customised pressure vessels; each order differs in design, material, engineering hours and testing. The production head suggests process costing because it is simpler. The right method is:""",
  "Job costing, because each customer order is a separate, identifiable cost unit", ["Process costing, because similar raw materials are used in every order",
   "Standard costing, because it replaces job costing for engineering products", "Marginal costing, because it eliminates job-wise costing"],
  "Job costing collects costs per job on a job cost card; it suits unique orders. Process costing suits continuous identical output.")

Q('D3', """Alpha Engineering makes steel pipes in continuous production, modular kitchens to customer specification and industrial fasteners in lots. Which combination of methods is appropriate?""",
  "Process for pipes, job for kitchens, batch for fasteners", ["Process costing uniformly for all three products",
   "Batch for pipes, process for kitchens, job for fasteners", "Marginal costing for all three, as required for inventory valuation"],
  "Continuous homogeneous output → process; customer-specific → job; identical units in lots → batch.")

Q('D3', """Process costing is ideal for which industries?
I. Chemical industry  II. Oil refinery  III. Paper industry""",
  "I, II and III", ["I and II only", "II and III only", "I and III only"],
  "All three are continuous-process industries with homogeneous output passing through successive processes.")

Q('D3', """1,000 units are introduced into a process at a total cost of ₹92,000. Normal loss is 10% of input, saleable as scrap at ₹20 per unit. Actual output is 850 units. What is the value of the abnormal loss?""",
  "₹5,000", ["₹4,600", "₹3,500", "₹15,000"],
  "Normal cost per unit = (92,000 − 100 × 20)/(1,000 − 100) = 90,000/900 = ₹100. Abnormal loss = 900 − 850 = 50 units × ₹100 = ₹5,000, transferred to Costing P&L.")

Q('D3', """In process costing, the cost of NORMAL loss is treated by:""",
  "Absorbing it into the cost of good units produced, after crediting any scrap value",
  ["Transferring it to the Costing Profit and Loss Account as a loss", "Charging it to the Abnormal Loss Account at full cost",
   "Ignoring it, as it has no effect on cost per unit"],
  "Normal loss is an unavoidable cost of production, so good units bear it (raising their unit cost). Only abnormal loss goes to Costing P&L.")

Q('D3', """Which of the following is generally treated as normal loss in process costing?""",
  "Evaporation and shrinkage inherent in the production process", ["Loss due to a machine breakdown caused by poor maintenance",
   "Loss due to theft from the factory store", "Loss from a fire in the processing plant"],
  "Normal loss is expected under normal conditions (evaporation, chemical change, shrinkage). Breakdowns, theft and fire are abnormal.")

Q('D3', """An Indian unit produces 1,000 tyres in a single lot; each needs 3 kg of rubber at ₹80/kg. Labour and overheads for the lot are ₹60,000 and packing is ₹10 per tyre. What is the cost per tyre under batch costing?""",
  "₹310", ["₹240", "₹300", "₹250"],
  "Material = 1,000 × 3 × 80 = 2,40,000; labour & OH 60,000; packing 10,000. Batch cost = 3,10,000 ÷ 1,000 = ₹310 per tyre.")

Q('D3', """Which statements about multiple costing are correct?
1. It combines two or more costing methods.
2. It suits products made of many separately produced components, such as cars and aircraft.
3. It is a costing technique like standard costing.
4. It is used where one method alone cannot ascertain cost properly.""",
  "1, 2 and 4 only", ["1, 2, 3 and 4", "2 and 3 only", "1 and 3 only"],
  "Multiple (composite) costing is a method, not a technique like standard or marginal costing.")

Q('D3', """A direct cost is best defined as a cost that:""",
  "Can be traced economically to a specific cost unit",
  ["Varies directly with the volume of production in every case", "Is incurred directly by the head office",
   "Is paid directly in cash rather than on credit"],
  "Direct means traceable to the cost unit (e.g. raw material in a product). A variable cost may still be indirect (e.g. power for the whole factory).")

Q('D3', """In contract costing, 'retention money' means:""",
  "The part of certified value held back by the contractee against defects",
  ["The amount the contractor keeps aside as a reserve for future losses", "The advance paid by the contractee before work starts",
   "The escalation amount payable when input prices rise"],
  "Progress payments are made on certified work less a retention percentage, released after the defect-liability period.")

Q('D3', """Which of the following is a costing TECHNIQUE rather than a costing METHOD?""",
  "Marginal costing", ["Job costing", "Process costing", "Contract costing"],
  "Methods (job, batch, contract, process, service, multiple) depend on the type of production. Techniques (marginal, standard, absorption, uniform costing, budgetary control) can be used with any method.")
