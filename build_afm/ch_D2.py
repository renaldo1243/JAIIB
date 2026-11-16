from qb import note, Q

note('D2', r'''
<p class="small">Syllabus: Meaning of direct and indirect tax; introduction to GST. <b>Asked: 3 questions per session since Nov 2025.</b> May 2026 asked:</p>
<ul class="small"><li>ITC blocked credits</li>
<li>registration on aggregate turnover</li>
<li>credit note</li>
<li>types of GST</li>
<li>registration threshold</li>
<li>which return summarises supplies</li>
<li>CGST/SGST/IGST</li>
<li>time of supply</li>
<li>interest at 18%</li>
<li>TCS under GST</li></ul>

<h3>1. Basics</h3>
<ul><li><b>Direct tax:</b> the burden falls on the person who pays it (income tax). <b>Indirect tax:</b> collected from someone else, the burden is shifted (GST).</li>
<li><b>GST</b> came in from <b>1 July 2017</b> through the <b>101st Constitutional Amendment (2016)</b>. The <b>GST Council</b> is under <b>Article 279A</b>, chaired by the Union Finance Minister. It is a destination-based tax on supply.</li>
<li><b>Types:</b>
<ul><li><b>Intra-State</b> supply: CGST + SGST (or UTGST in UTs without a legislature).</li>
<li><b>Inter-State</b> supply, <b>imports</b>, and supplies to SEZs: <b>IGST</b>.</li></ul></li>
<li><b>Rates (from 22 Sept 2025, "GST 2.0"):</b> main slabs <b>5% and 18%</b>, a <b>40%</b> rate for sin and luxury goods, plus nil and special rates (e.g. 3% on gold).</li>
<li><b>GSTIN</b> = 15 characters: state code (2) + PAN (10) + entity number + Z + check digit.
<br>Goods are classified by <b>HSN</b>; services by <b>SAC</b>.</li></ul>

<h3>2. Registration</h3>
<ul><li>Based on <b>aggregate turnover</b>: all-India, same PAN, covering taxable + <b>exempt</b> + export + inter-State supplies, excluding the taxes themselves and inward supplies under reverse charge.</li>
<li><b>Thresholds:</b>
<ul><li>Exclusive suppliers of <b>goods</b>: <b>₹40 lakh</b> (₹20 lakh in some special-category States).</li>
<li><b>Services</b>: <b>₹20 lakh</b> (₹10 lakh in some special-category States).</li></ul></li>
<li><b>Compulsory registration regardless of turnover:</b>
<ul><li>inter-State taxable suppliers of goods</li>
<li>casual taxable persons</li>
<li>persons liable under reverse charge</li>
<li>e-commerce operators and sellers through them (with exceptions)</li>
<li>non-resident taxable persons</li>
<li>persons deducting TDS or collecting TCS under GST</li></ul></li>
<li><b>Composition scheme:</b>
<ul><li>turnover up to ₹1.5 crore (goods)</li>
<li>pays at a low rate (1% traders and manufacturers, 5% restaurants, 6% services up to ₹50 lakh)</li>
<li>cannot collect tax from customers or claim ITC</li>
<li>no inter-State outward supply</li></ul></li></ul>

<h3>3. Time of supply</h3>
<ul><li><b>Goods</b> (Sec 12): the <b>earlier</b> of the <b>date of invoice</b> or the <b>last date by which the invoice should have been issued</b> (i.e. the date of removal or delivery). GST is not payable on advances for goods.
<br><b>Example:</b> goods removed 15 July, delivered 16 July, invoice 18 July (late), paid 28 July → time of supply = <b>15 July</b>.</li>
<li><b>Services</b> (Sec 13): earlier of the invoice date (if issued within 30 days of service) or the date of receipt of payment.</li>
<li>If the invoice is issued <b>before</b> supply (invoice 16 June, supply 13 July) → time of supply = <b>16 June</b>, so the liability falls in June, payable in the June GSTR-3B by <b>20 July</b>.</li></ul>

<h3>4. Input Tax Credit (ITC)</h3>
<ul><li><b>Conditions</b> (Sec 16):
<ul><li>possession of a tax invoice</li>
<li>goods or services received</li>
<li>tax actually paid by the supplier</li>
<li>return filed</li>
<li>invoice appears in GSTR-2B</li></ul>
Time limit: by <b>30 November</b> following the end of the FY (or the annual return, if earlier).</li>
<li><b>Blocked credits</b> (Sec 17(5)), with no ITC even though GST was paid:
<ul><li>motor vehicles for transporting persons (seating ≤ 13), except for further supply, passenger transport or driving training</li>
<li>food and beverages, outdoor catering, beauty treatment, health services, club membership, rent-a-cab, life and health insurance (unless obligatory by law)</li>
<li>travel benefits to employees on vacation (LTC)</li>
<li><b>works contract or goods/services for constructing immovable property on own account</b> (e.g. steel and cement for a factory building). <b>Plant and machinery is excluded from this block</b>, so ITC is available on it.</li>
<li>tax paid under composition</li>
<li>goods lost, stolen, destroyed, written off, or given as <b>free samples or gifts</b></li>
<li>personal consumption</li></ul></li>
<li><b>Allowed:</b> raw materials used in taxable supplies, office laptops and capital goods used in business.</li></ul>

<h3>5. Documents and returns</h3>
<table><tr><th>Document / return</th><th>Use</th></tr>
<tr><td><b>Credit note</b> (Sec 34)</td><td>Issued by the supplier to <b>reduce</b> taxable value or tax (sales return, post-sale discount, excess charge)</td></tr>
<tr><td><b>Debit note</b></td><td>Issued to <b>increase</b> value or tax</td></tr>
<tr><td><b>GSTR-1</b></td><td>Details of <b>outward supplies</b> (invoice-wise). Monthly by the 11th (quarterly under QRMP)</td></tr>
<tr><td><b>GSTR-3B</b></td><td>Monthly <b>summary return</b> of outward and inward supplies, ITC and <b>payment of tax</b>. Due by the <b>20th</b> of the next month (22nd/24th for quarterly QRMP filers)</td></tr>
<tr><td>GSTR-2B</td><td>Auto-drafted ITC statement (read-only)</td></tr>
<tr><td>CMP-08 / GSTR-4</td><td>Composition dealers: quarterly payment / annual return</td></tr>
<tr><td>GSTR-7 / GSTR-8</td><td>TDS deductors / e-commerce TCS collectors</td></tr>
<tr><td>GSTR-9</td><td>Annual return (by 31 December)</td></tr></table>
<ul><li><b>Interest</b> on late payment of tax: <b>18% p.a.</b> (Sec 50).</li>
<li><b>TCS under GST</b> (Sec 52): collected by the <b>e-commerce operator</b> on net taxable supplies made through it. 0.5% total (0.25% CGST + 0.25% SGST, or 0.5% IGST) from 10 July 2024.</li>
<li><b>TDS under GST</b> (Sec 51): by Government departments and notified bodies, 2% on contracts above ₹2.5 lakh.</li></ul>

<div class="box trap"><b>Traps:</b>
<ul><li>"Below threshold on taxable turnover alone": wrong. Use <b>aggregate</b> turnover, which includes exempt supplies.</li>
<li>Imports attract <b>IGST</b>, even though the goods land in one State.</li>
<li>Sales return or discount → <b>credit note</b>, not a payment voucher.</li>
<li>ITC is blocked on a factory building and on an MD's car, but allowed on plant and machinery and laptops.</li>
<li>GSTR-3B = summary + payment; GSTR-1 = invoice-level outward supplies.</li>
<li>TCS under GST is collected by the e-commerce operator, not the seller.</li></ul></div>
''')

Q('D2', """ABC Constructions buys: (1) steel to construct its factory building, (2) office laptops, (3) a motor car for the MD, (4) raw materials used in taxable supplies. The executive wants ITC on all because GST was paid. ITC is available on:""",
  "Office laptops and raw materials only", ["All four, since GST was paid on every purchase", "Raw materials only",
   "Steel, laptops and raw materials, but not the car"],
  "Sec 17(5) blocks ITC on goods and services used to construct immovable property on own account (other than plant and machinery) and on motor vehicles for transport of persons. Laptops and raw materials used in business are eligible.")

Q('D2', """Aarav Handicrafts (Rajasthan only) has taxable intra-State supplies of ₹31 lakh, exempt supplies of ₹6 lakh and sale of old office furniture of ₹3 lakh. The owner says registration is not needed because taxable turnover is below the threshold. Which is correct?""",
  "Test aggregate turnover, which includes exempt supplies and the furniture sale",
  ["Registration depends only on taxable turnover, so it is not required", "Registration becomes compulsory only when an inter-State supply is made",
   "Sale of office furniture automatically makes registration compulsory"],
  "Aggregate turnover covers taxable, exempt, export and inter-State supplies of the same PAN. Here it is about ₹40 lakh, right at the goods threshold, so it must be tested on aggregate turnover.")

Q('D2', """A supplier invoiced ₹12,00,000 plus GST; goods worth ₹1,50,000 were later returned, so both value and GST must be reduced. Which document should be issued?""",
  "Credit note", ["Debit note", "Revised tax invoice", "Payment voucher"],
  "A credit note (Sec 34) reduces taxable value or tax charged in an earlier invoice; a debit note increases it.")

Q('D2', """Mr Rajesh removes goods for delivery on 15 July, they are delivered on 16 July, the invoice is issued on 18 July and payment is received on 28 July. What is the time of supply?""",
  "15 July", ["16 July", "18 July", "28 July"],
  "For goods, time of supply = earlier of the invoice date or the last date by which the invoice should have been issued (at or before removal). The invoice was due by 15 July, so 15 July.")

Q('D2', """An invoice is issued on 16 June 2024 but supply of goods is completed on 13 July 2024. When is GSTR-3B for this liability due (monthly filer)?""",
  "20 July 2024", ["20 August 2024", "16 July 2024", "13 August 2024"],
  "Time of supply = earlier of invoice (16 June) and supply → June. June's GSTR-3B (summary return with payment) is due by the 20th of the next month: 20 July 2024.")

Q('D2', """Which return is used by a registered taxpayer to give a summary of outward and inward supplies, claim ITC and pay tax?""",
  "GSTR-3B", ["GSTR-1", "GSTR-2B", "GSTR-9"],
  "GSTR-3B is the summary return with tax payment. GSTR-1 gives invoice-wise outward supplies; GSTR-2B is an auto-generated ITC statement; GSTR-9 is the annual return.")

Q('D2', """Under GST, interest at 18% per annum is chargeable mainly for:""",
  "Delay in payment of tax after the due date", ["Delay in filing GSTR-1", "Issuing a credit note after the due date",
   "Delay in obtaining registration when turnover crosses the threshold"],
  "Section 50 levies interest at 18% p.a. on tax paid late (for the period of delay). Late filing of returns attracts late fees, not this interest.")

Q('D2', """TCS (Tax Collected at Source) under GST is collected by:""",
  "The e-commerce operator on supplies made through its platform", ["The supplier from every customer on all taxable sales",
   "Government departments when paying their contractors", "The bank through which the GST payment is made"],
  "Sec 52: e-commerce operators collect TCS (0.5% from 10 July 2024). Government departments deduct TDS under Sec 51.")

Q('D2', """What is the GST registration threshold for a supplier exclusively of goods in a normal category State such as Rajasthan?""",
  "Aggregate turnover of ₹40 lakh", ["Aggregate turnover of ₹20 lakh", "Aggregate turnover of ₹10 lakh", "Taxable turnover of ₹1.5 crore"],
  "Exclusive suppliers of goods: ₹40 lakh (₹20 lakh in some special-category States). Service providers: ₹20 lakh (₹10 lakh). ₹1.5 crore is the composition-scheme limit.")

Q('D2', """Which statements are correct?
1. GST was introduced through the 101st Constitutional Amendment and came into force on 1 July 2017.
2. The GST Council is constituted under Article 279A and is chaired by the Union Finance Minister.
3. A composition dealer can claim ITC and collect tax from customers.
4. GSTIN is a 15-character number based on the PAN.""",
  "1, 2 and 4 only", ["1, 2, 3 and 4", "2 and 3 only", "1 and 3 only"],
  "Composition dealers pay a low flat rate but cannot claim ITC or collect GST from buyers (3 wrong).")

Q('D2', """Income tax is a direct tax while GST is an indirect tax because:""",
  "GST's burden is shifted to the consumer; income tax is borne by the taxpayer",
  ["GST is levied by States only, while income tax is levied by the Centre", "Income tax is paid monthly while GST is paid annually",
   "GST applies only to companies, while income tax applies to individuals"],
  "In an indirect tax the person who pays it to the government (supplier) recovers it from someone else (buyer); a direct tax's impact and incidence fall on the same person.")
