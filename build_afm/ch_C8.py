from qb import note, Q

note('C8', r'''
<p class="small">Syllabus: Meaning, features and types of leases, rationale, lease agreement, legal aspects, finance vs operating lease, lease accounting, leasing as a financing decision. <b>Asked: 1–2 questions on types and features per session since Nov 2025.</b> May 2026 asked:</p>
<ul class="small"><li>Ind AS 116 right-of-use asset</li>
<li>wet vs dry lease</li>
<li>lease-vs-buy by present value (three numericals)</li></ul>
<p class="small">Detailed lessor/lessee journal entries were asked only in 2024, so they are left out.</p>

<h3>1. Parties and features</h3>
<ul><li><b>Lessor</b> (owner) gives the <b>lessee</b> the right to use an asset for a period in return for <b>lease rentals</b>. Ownership stays with the lessor.</li>
<li>Leasing is governed by general law: the Indian Contract Act (<b>bailment</b>). There is no separate leasing Act. Stamp duty applies on the agreement.</li></ul>

<h3>2. Types</h3>
<table><tr><th>Type</th><th>Meaning</th></tr>
<tr><td><b>Finance lease</b></td><td>Transfers <b>substantially all risks and rewards</b> of ownership.
<ul><li>Lease term covers most of the asset's life.</li>
<li>PV of rentals ≈ fair value.</li>
<li>Non-cancellable.</li>
<li>The lessee bears maintenance and insurance.</li>
<li>Often has a bargain purchase option.</li>
<li>"Full pay-out": the lessor recovers its whole investment plus return.</li></ul></td></tr>
<tr><td><b>Operating lease</b></td><td>Does not transfer substantially all risks and rewards.
<ul><li>Short-term and cancellable.</li>
<li>The lessor maintains the asset and bears obsolescence.</li>
<li>Rentals don't recover the full cost ("non-pay-out").</li>
<li>Examples: computers, aircraft hired for a season.</li></ul></td></tr>
<tr><td>Sale and leaseback</td><td>The owner sells the asset to a lessor and leases it back. Releases cash while keeping use of the asset.</td></tr>
<tr><td>Direct lease</td><td>The lessor buys from the supplier and leases to the lessee (two-party or three-party).</td></tr>
<tr><td>Leveraged lease</td><td>Three parties: lessor, lessee and <b>lender</b>. The lessor funds most of the cost by borrowing.</td></tr>
<tr><td>Cross-border lease</td><td>Lessor and lessee are in different countries.</td></tr>
<tr><td><b>Wet lease</b></td><td>Aircraft leased <b>with crew, maintenance and insurance</b> (ACMI) provided by the lessor. Short-term.</td></tr>
<tr><td><b>Dry lease</b></td><td>Aircraft <b>only</b>. The lessee provides crew, maintenance and insurance. Usually longer-term, financing-type.</td></tr></table>

<h3>3. Accounting standards</h3>
<ul><li><b>AS 19</b> (non-Ind AS companies): the lessee capitalises a finance lease (asset + liability) and expenses operating-lease rentals. Land leases are excluded.</li>
<li><b>Ind AS 116</b> (lessee):
<ul><li>The finance/operating split is removed.</li>
<li>For almost every lease the lessee recognises a <b>right-of-use (ROU) asset</b> and a <b>lease liability</b> (PV of payments).</li>
<li>It depreciates the ROU asset and charges interest on the liability.</li>
<li><b>Exemptions:</b> short-term leases (≤ 12 months) and low-value assets.</li>
<li>Legal ownership doesn't matter; control of an identified asset does.</li></ul></li>
<li><b>Lessor</b> under Ind AS 116 still classifies leases as finance or operating.</li>
<li>Lease vs <b>hire purchase</b>: in hire purchase, ownership passes to the hirer on paying the last instalment, and the hirer claims depreciation. In a lease, ownership stays with the lessor.</li></ul>

<h3>4. Lease vs buy (financing decision)</h3>
<ul><li>Compare the <b>PV of lease rentals</b> (after tax, discounted at the after-tax cost of borrowing) with the <b>PV of the cost of buying</b>: price − PV of the depreciation tax shield − PV of salvage.</li>
<li>The simple exam version: PV of rentals vs cash price.
<ul><li>₹12 lakh × PVAF(10%, 5) 3.7908 = ₹45.49 lakh vs price ₹47.5 lakh → <b>lease</b>.</li>
<li>₹10 lakh × PVAF(12%, 3) 2.4018 = ₹24.02 lakh vs price ₹24.5 lakh → lease.</li>
<li>₹36 lakh × 3.7908 = ₹136.47 lakh vs price ₹152 lakh → lease.</li></ul></li>
<li>If rentals are paid <b>in advance</b>, use annuity due: PVAF × (1 + r).</li></ul>
<p><b>Rationale for leasing:</b> 100% financing, preserves credit lines and working capital, tax benefits, protection from obsolescence (operating lease), quick and flexible.</p>

<div class="box trap"><b>Traps:</b>
<ul><li>"Rent is an expense because ownership hasn't passed": wrong under Ind AS 116 (ROU asset + liability).</li>
<li>Wet = with crew; dry = aircraft only.</li>
<li>Operating lease: the lessor bears obsolescence. Finance lease: the lessee bears the risks.</li>
<li>Leveraged lease has a third party, the lender.</li>
<li>Compare <b>PVs</b>, never total rentals.</li></ul></div>
''')

Q('C8', """Zen Motors takes a 7-year lease of an identified factory; it gets the right to use and direct the asset, but legal title stays with the lessor. The executive wants to book rentals as rent expense. Under Ind AS 116 the lessee should generally:""",
  "Recognise a right-of-use asset and a lease liability, unless the short-term or low-value exemption applies",
  ["Expense the rentals as rent, because legal ownership never passes to the lessee", "Capitalise the asset only if ownership will transfer to it at the end of the lease",
   "Disclose the lease only as a contingent liability in the notes until it expires"],
  "Ind AS 116 removed the operating/finance split for lessees: control of an identified asset for a period leads to an ROU asset and a lease liability. Exemptions: leases of 12 months or less and low-value assets.")

Q('C8', """An airline hires an aircraft along with the lessor's crew, maintenance and insurance for the peak season. This is a:""",
  "Wet lease", ["Dry lease", "Leveraged lease", "Sale and leaseback"],
  "A wet lease (ACMI) includes aircraft, crew, maintenance and insurance from the lessor. In a dry lease the lessee arranges crew and maintenance.")

Q('C8', """Which feature is most closely associated with a finance lease?""",
  "Substantially all risks and rewards of ownership pass to the lessee over a non-cancellable term covering most of the asset's life",
  ["The lessor bears obsolescence risk and maintains the asset, and the lease can be cancelled at short notice",
   "The lease term is short and rentals recover only a small part of the asset's cost",
   "The aircraft is supplied together with crew and insurance by the lessor"],
  "A finance lease is in substance a financing arrangement: full pay-out, non-cancellable, lessee bears risks. The other descriptions fit an operating or wet lease.")

Q('C8', """A company can buy a warehouse for ₹24.50 lakh or lease it for ₹10 lakh at the end of each year for 3 years. Required return 12%; PVAF (12%, 3) = 2.4018. Which is preferable?""",
  "Lease, because the PV of rentals (about ₹24.02 lakh) is lower than the purchase price",
  ["Buy, because total rentals of ₹30 lakh exceed the purchase price of ₹24.50 lakh", "They are financially identical, because the rentals are fixed in amount",
   "Buy, because time value of money does not apply when acquiring fixed assets"],
  "PV = 10 × 2.4018 = ₹24.02 lakh < ₹24.50 lakh. Comparing undiscounted totals (₹30 lakh) is the trap.")

Q('C8', """If the same lease rentals of ₹10 lakh for 3 years at 12% were payable at the BEGINNING of each year, their present value would be about:""",
  "₹26.90 lakh", ["₹24.02 lakh", "₹30.00 lakh", "₹21.45 lakh"],
  "Annuity due PV = 2.4018 × 1.12 × 10 = ₹26.90 lakh; now buying (₹24.50 lakh) becomes cheaper.")

Q('C8', """A company sells its office building to a leasing company and immediately takes it back on lease. This is called:""",
  "Sale and leaseback", ["Leveraged lease", "Cross-border lease", "Hire purchase"],
  "Sale and leaseback releases funds locked in the asset while the seller keeps using it.")

Q('C8', """Which statements are correct?
1. In a leveraged lease, a lender finances a large part of the asset's cost.
2. In an operating lease, the lessor generally bears the risk of obsolescence.
3. In hire purchase, ownership stays permanently with the hire vendor.
4. There is no separate Act in India governing leasing; general contract law applies.""",
  "1, 2 and 4 only", ["1, 2, 3 and 4", "2 and 3 only", "1 and 3 only"],
  "In hire purchase, ownership passes to the hirer on payment of the last instalment (3 wrong). Leasing is a contract of bailment under the Indian Contract Act.")

Q('C8', """Under Ind AS 116, which leases may a lessee keep off the balance sheet by choosing the recognition exemption?""",
  "Leases of 12 months or less and leases of low-value assets",
  ["All leases where legal ownership does not pass at the end", "All leases of land and buildings",
   "Leases where rentals are paid in advance"],
  "Only short-term (≤12 months) and low-value asset leases can be expensed on a straight-line basis; others create an ROU asset and lease liability.")
