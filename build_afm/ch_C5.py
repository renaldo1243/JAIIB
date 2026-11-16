from qb import note, Q

note('C5', r'''
<p class="small">Syllabus: Fundamentals of foreign exchange, Indian forex market, direct and indirect quotes, basic exchange-rate arithmetic, forward rates. <b>Asked: 2–3 questions every session since Nov 2025.</b> May 2026 asked:</p>
<ul class="small"><li>exporter → buying rate</li>
<li>importer → selling rate</li>
<li>exporter and importer quoted forward rates from the same margins</li>
<li>a forward contract with a 3-month premium</li>
<li>a rupee amount for a USD purchase</li></ul>

<h3>1. Quotes</h3>
<ul><li><b>Direct quote:</b> units of home currency per unit of foreign currency, e.g. USD/INR 83.25. India has used <b>direct quotes since 2 August 1993</b>.
<br><b>Indirect quote:</b> foreign currency per unit of home currency, e.g. 1 INR = 0.01201 USD.</li>
<li>A two-way quote <b>83.25 / 83.33</b> is from the bank's side:
<ul><li>83.25 = <b>bid = the bank's buying rate</b></li>
<li>83.33 = <b>ask/offer = the bank's selling rate</b></li></ul>
<b>Buy low, sell high</b>; the gap is the spread (the bank's margin).</li>
<li><b>Exporter or inward remittance:</b> the customer sells USD to the bank → <b>bank's buying rate</b> (the lower one).
<br><b>Importer or outward remittance:</b> the customer buys USD from the bank → <b>bank's selling rate</b> (the higher one).</li>
<li>Whether the deal is spot or forward does <b>not</b> change who is buying.</li></ul>

<h3>2. Merchant rates (FEDAI)</h3>
<table><tr><th>Rate</th><th>Used for</th><th>Level</th></tr>
<tr><td>TT buying</td><td>Clean inward remittances, export proceeds already credited to nostro</td><td>Highest of the buying rates</td></tr>
<tr><td>Bill buying</td><td>Purchase or discount of export bills (bank pays before it receives)</td><td>Lower than TT buying</td></tr>
<tr><td>TT selling</td><td>Outward remittances (not involving bills)</td><td>Lowest of the selling rates</td></tr>
<tr><td>Bill selling</td><td>Import bills retired by the importer</td><td>Higher than TT selling (extra handling)</td></tr></table>
<p><b>Value dates:</b> cash/ready = same day; TOM = next working day; <b>spot = 2 working days (T+2)</b>; forward = beyond spot.</p>
<p><b>Nostro</b> = our account with them (in foreign currency). <b>Vostro</b> = their account with us (in INR). <b>Loro</b> = their account with a third bank.</p>

<h3>3. Forward rates</h3>
<ul><li>Forward rate = spot ± forward margin (swap points).</li>
<li><b>Margins in ascending order</b> (e.g. 18/22) → foreign currency at a <b>premium</b> → <b>add</b>.
<br><b>Descending</b> (e.g. 22/18) → <b>discount</b> → <b>subtract</b>.</li>
<li><b>Example:</b> spot 83.42/83.48 with a 3-month margin of +18/+22 paise.
<ul><li>Forward buying (exporter) = 83.42 + 0.18 = <b>83.60</b>.</li>
<li>Forward selling (importer) = 83.48 + 0.22 = <b>83.70</b>.</li>
<li>The two customers are quoted different rates.</li></ul></li>
<li><b>Annualised premium %</b> = (Forward − Spot) ÷ Spot × (12 ÷ months) × 100. With spot 83.00 and a 3-month forward of 83.60 → 0.60 ÷ 83 × 4 × 100 = <b>2.89% p.a.</b></li>
<li><b>Interest rate parity:</b> the currency with the higher interest rate trades at a <b>forward discount</b>.
<br>F = S × (1 + r<sub>INR</sub> × t) ÷ (1 + r<sub>USD</sub> × t). With S = 83, r<sub>INR</sub> = 7%, r<sub>USD</sub> = 5%, 3 months → F ≈ <b>83.41</b>. The USD is at a premium because rupee rates are higher.</li></ul>

<h3>4. Cross rates</h3>
<ul><li>USD/INR 83.20/83.30 and GBP/USD 1.2600/1.2610:
<ul><li>GBP/INR bid = 83.20 × 1.2600 = <b>104.83</b></li>
<li>GBP/INR ask = 83.30 × 1.2610 = <b>105.04</b></li></ul></li>
<li>Rule: for bid, multiply the bids; for ask, multiply the asks. When dividing, cross them.</li></ul>

<h3>5. Indian market basics</h3>
<ul><li>Governed by <b>FEMA 1999</b>. RBI regulates. <b>FEDAI</b> (Foreign Exchange Dealers' Association of India) sets the rules for interbank dealing.</li>
<li>Authorised Dealers:
<ul><li>Category I: banks</li>
<li>Category II: e.g. full-fledged money changers upgraded</li>
<li>Category III</li></ul></li>
<li>Rupee is fully convertible on the <b>current account</b>, partially on the capital account.</li>
<li>FBIL publishes reference rates.</li></ul>

<div class="box trap"><b>Traps:</b>
<ul><li>"Selling rate whenever foreign currency is involved": wrong. Ask <b>who is buying</b>.</li>
<li>For the exporter use the <b>lower</b> rate (bank buys); for the importer the <b>higher</b> rate.</li>
<li>Ascending margin = premium (add). Descending = discount (subtract).</li>
<li>Spot settles <b>T+2</b>, not same day.</li>
<li>Bill buying rate &lt; TT buying rate; bill selling rate &gt; TT selling rate.</li></ul></div>
''')

Q('C5', """An exporter will receive USD 5,00,000. The bank's quote is USD/INR 83.25 / 83.33. A new officer suggests applying the selling rate because foreign currency is involved. Which is correct?""",
  "The exporter sells USD to the bank, so the bank's buying rate of 83.25 applies",
  ["The selling rate of 83.33 applies whenever foreign currency is involved", "The mid-rate of 83.29 must be applied to all customer deals",
   "The buying rate applies only to cash transactions; for remittances the selling rate applies"],
  "Quotes are from the bank's side: bid (lower) is what the bank pays to buy USD. An exporter brings USD in, so the bank buys at 83.25.")

Q('C5', """An importer must remit USD 5,00,000 immediately. Spot USD/INR is 83.48 / 83.56. What rupee amount will be debited?""",
  "₹4,17,80,000", ["₹4,17,40,000", "₹4,17,60,000", "₹4,18,00,000"],
  "The importer buys USD from the bank at the bank's selling rate, 83.56: 5,00,000 × 83.56 = ₹4,17,80,000.")

Q('C5', """Spot USD/INR 83.42 / 83.48; 3-month forward margin +18 / +22 paise. An exporter will receive and an importer will pay USD in 3 months. What forward rates apply?""",
  "Exporter 83.60; importer 83.70", ["Both 83.65, the forward mid-rate", "Exporter 83.66; importer 83.64", "Exporter 83.24; importer 83.26"],
  "Ascending margins mean the USD is at a premium, so add: buying 83.42 + 0.18 = 83.60 (exporter); selling 83.48 + 0.22 = 83.70 (importer).")

Q('C5', """A 3-month forward quote shows margins of 25/20 paise against spot 83.10/83.16. What is the forward selling rate?""",
  "82.96", ["83.36", "83.41", "82.85"],
  "Descending margins mean a discount, so subtract: selling = 83.16 − 0.20 = 82.96 (buying = 83.10 − 0.25 = 82.85).")

Q('C5', """Spot USD/INR is 83.00 and the 3-month forward rate is 83.60. The annualised forward premium is about:""",
  "2.89%", ["0.72%", "7.23%", "1.45%"], "(83.60 − 83.00)/83.00 × 12/3 × 100 = 0.7229% × 4 = 2.89% p.a.")

Q('C5', """Spot USD/INR is 83.00, 3-month rupee interest 7% p.a. and USD interest 5% p.a. By interest rate parity, the 3-month forward rate is about:""",
  "83.41, with the USD at a forward premium", ["82.59, with the USD at a forward discount", "83.00, as forward and spot rates are always equal",
   "84.66, with the USD at a forward premium"],
  "F = 83 × (1 + 0.07/4)/(1 + 0.05/4) = 83 × 1.0175/1.0125 = 83.41. The currency with lower interest (USD) trades at a forward premium.")

Q('C5', """USD/INR 83.20/83.30 and GBP/USD 1.2600/1.2610. What is the GBP/INR quote?""",
  "104.83 / 105.04", ["104.94 / 104.93", "66.03 / 66.06", "105.04 / 104.83"],
  "Bid = 83.20 × 1.2600 = 104.83; ask = 83.30 × 1.2610 = 105.04. Multiply bid × bid and ask × ask.")

Q('C5', """Which statements about the Indian forex market are correct?
1. India follows the direct method of quotation.
2. A spot transaction is settled on the second working day after the deal date.
3. The bill buying rate is higher than the TT buying rate.
4. FEDAI frames rules for interbank forex dealing.""",
  "1, 2 and 4 only", ["1, 2, 3 and 4", "1 and 3 only", "2, 3 and 4 only"],
  "Direct quotes since 1993; spot = T+2; FEDAI sets dealing rules. Bill buying is LOWER than TT buying because the bank pays out before it is reimbursed.")

Q('C5', """An Indian exporter books a forward contract to sell USD 10,000 at ₹83.00. On maturity, spot is ₹84.20. What is the effect?""",
  "He receives ₹8,30,000 as contracted, forgoing a ₹12,000 gain he would have made at spot",
  ["He receives ₹8,42,000 because forward contracts settle at the spot rate on maturity", "He can cancel the contract free of cost and sell at the spot rate",
   "He receives ₹8,30,000 and the bank also pays him the ₹12,000 difference"],
  "A forward contract fixes the rate: he must deliver at 83.00, getting ₹8,30,000. The hedge removed both downside risk and upside gain.")

Q('C5', """'Nostro account' of an Indian bank means:""",
  "The Indian bank's account maintained with a foreign bank abroad, in foreign currency",
  ["A foreign bank's rupee account maintained with the Indian bank", "An account of one foreign bank with another foreign bank",
   "The Indian bank's rupee account with the Reserve Bank of India"],
  "Nostro = 'ours with you' (in foreign currency, abroad). Vostro = 'yours with us' (in INR, in India). Loro = a third party's account.")
