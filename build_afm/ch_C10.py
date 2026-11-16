from qb import note, Q

note('C10', r'''
<p class="small">Syllabus: Derivatives: characteristics and functions, users, futures, FRA, swaps, options. <b>Asked: about 1 question on types per session.</b> May 2026 asked about exchange-traded derivatives (ETDs) and a statement on derivatives and forward contracts in India. The theory of characteristics and functions (asked only in 2024) is kept to a few lines.</p>

<h3>1. Meaning and users</h3>
<ul><li>A <b>derivative</b> is a contract whose value comes from an underlying: a currency, interest rate, share, index or commodity.</li>
<li><b>Users:</b>
<ul><li><b>Hedgers</b> reduce risk.</li>
<li><b>Speculators</b> take risk for profit.</li>
<li><b>Arbitrageurs</b> profit from price differences between markets, without risk.</li></ul></li>
<li><b>Regulation in India:</b>
<ul><li><b>Exchange-traded derivatives</b> (equity, currency and interest-rate futures and options on NSE/BSE): <b>SEBI</b>.</li>
<li><b>OTC</b> interest-rate and forex derivatives (forwards, swaps, FRAs): <b>RBI</b>.</li>
<li>Commodity derivatives: SEBI (since the FMC merger in 2015).</li></ul></li></ul>

<h3>2. Types</h3>
<table><tr><th>Instrument</th><th>Features</th></tr>
<tr><td><b>Forward</b></td><td>OTC, customised (amount and date). Settled at maturity. <b>Counterparty (default) risk</b>. No margin, not marked to market. Both parties are obliged.</td></tr>
<tr><td><b>Futures</b></td><td><b>Exchange-traded, standardised</b> (lot size, expiry). The clearing corporation is the counterparty, so there is <b>no counterparty risk</b>. <b>Initial margin + daily mark-to-market</b>. Highly liquid and can be squared off anytime.</td></tr>
<tr><td><b>Options</b></td><td>The buyer (holder) pays a <b>premium</b> and gets a <b>right but not an obligation</b>. The seller (writer) has the obligation.
<ul><li><b>Call</b> = right to buy. <b>Put</b> = right to sell.</li>
<li><b>American</b> = exercise any time up to expiry. <b>European</b> = only on expiry.</li>
<li>Call is in the money when spot &gt; strike; put when spot &lt; strike.</li>
<li>The buyer's maximum loss = premium. The writer's loss can be unlimited (for a call).</li></ul></td></tr>
<tr><td><b>Swaps</b></td><td>Exchange of cash flows.
<ul><li><b>Interest rate swap:</b> fixed vs floating in one currency. <b>Notional principal is not exchanged.</b></li>
<li><b>Currency swap:</b> principal and interest in two currencies. <b>Principal is exchanged</b> at the start and the end.</li></ul></td></tr>
<tr><td><b>FRA</b> (Forward Rate Agreement)</td><td>OTC contract fixing an interest rate today for a future period on a <b>notional</b> amount. Only the <b>difference</b> is settled (discounted, at the start of the period). Quoted as "3×6": starts in 3 months, ends in 6. A buyer of an FRA is protected against rising rates.</td></tr>
<tr><td>Credit default swap</td><td>Protection buyer pays a premium; the seller pays if the reference entity defaults.</td></tr></table>

<h3>3. ETD vs OTC</h3>
<table><tr><th>Exchange-traded</th><th>OTC</th></tr>
<tr><td>Standardised contracts</td><td>Customised</td></tr>
<tr><td>Clearing corporation guarantees (novation)</td><td>Counterparty credit risk</td></tr>
<tr><td>Margins and daily MTM</td><td>Usually no daily margin (collateral may be agreed)</td></tr>
<tr><td>Transparent prices, liquid</td><td>Less transparent; reported to the trade repository (CCIL)</td></tr>
<tr><td>e.g. currency futures and options, index futures</td><td>e.g. forex forwards, IRS, FRA, currency swaps</td></tr></table>

<div class="box trap"><b>Traps:</b>
<ul><li>A forward obliges both sides. An option obliges only the writer.</li>
<li>Futures carry no counterparty risk because the clearing house guarantees them. Forwards do.</li>
<li>IRS: notional is never exchanged. Currency swap: principal is exchanged.</li>
<li>FRA settles only the interest difference, not the principal.</li>
<li>American options can be exercised early; European only at expiry.</li></ul></div>
''')

Q('C10', """Which statement about exchange-traded derivatives (ETDs) is TRUE?""",
  "They are standardised contracts where the clearing corporation becomes the counterparty, so counterparty risk is minimal",
  ["They are customised to each client's amount and date and settled bilaterally at maturity", "They are not subject to any margins or daily mark-to-market settlement by the exchange",
   "They are regulated in India by RBI, while OTC derivatives are regulated by SEBI"],
  "ETDs are standardised and margined daily with the clearing house as central counterparty. ETDs are regulated by SEBI; OTC interest-rate and forex derivatives by RBI.")

Q('C10', """Which statements are correct?
1. The buyer of a call option has the right but not the obligation to buy the underlying.
2. The writer of an option receives the premium and takes on the obligation.
3. A European option can be exercised on any day up to expiry.
4. In an interest rate swap, the notional principal is exchanged at the start and the end.""",
  "1 and 2 only", ["1, 2 and 3 only", "1, 2 and 4 only", "2, 3 and 4 only"],
  "A European option can be exercised only on expiry (American any time). IRS exchanges only interest flows on a notional amount; principal is exchanged in a currency swap.")

Q('C10', """Compared with a currency futures contract, a forex forward contract:""",
  "Is customised and carries counterparty risk, with no daily mark-to-market",
  ["Is standardised and traded on a stock exchange with daily margins", "Gives the holder a right but no obligation to exchange currency",
   "Is guaranteed by a clearing corporation and freely tradable"],
  "Forwards are OTC, bilateral and customised, settled at maturity, with default risk. Futures are exchange-traded, standardised and margined.")

Q('C10', """A company borrows at a floating rate and fears rates will rise. Which derivative converts its floating-rate liability into a fixed-rate one?""",
  "An interest rate swap in which it pays fixed and receives floating", ["An interest rate swap in which it pays floating and receives fixed",
   "Buying a put option on foreign currency", "Selling a forward rate agreement for the same period"],
  "Paying fixed / receiving floating offsets its floating payments, leaving a fixed cost. Selling an FRA would benefit from falling rates, the opposite of what it needs.")

Q('C10', """A '3 × 6 FRA' means a forward rate agreement:""",
  "That fixes the interest rate for a 3-month period starting 3 months from today, settling only the rate difference",
  ["Under which principal is exchanged after 3 months and repaid after 6 months", "With a 3% fixed rate payable against a 6% floating rate on the notional",
   "That is traded on the stock exchange in standard lots of 3 and 6 contracts"],
  "The FRA covers the period from month 3 to month 6. Only the difference between the agreed and the reference rate on the notional amount is settled.")

Q('C10', """The maximum loss for the BUYER of an option is:""",
  "The premium paid", ["Unlimited", "The strike price", "The full notional value of the underlying"],
  "The buyer can simply let the option lapse, losing only the premium. The writer of a call faces potentially unlimited loss.")

Q('C10', """Which user enters derivatives to lock in a riskless profit from price differences between two markets?""",
  "Arbitrageur", ["Hedger", "Speculator", "Market regulator"],
  "Arbitrageurs exploit mispricing across markets without risk; hedgers reduce existing risk; speculators take risk hoping to profit.")
