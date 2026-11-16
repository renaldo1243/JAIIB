from qb import note, Q

note('A8', r'''
<p class="small">Syllabus: Instruments of credit, term and due date, important terms, accounting entries, accommodation bill, bill books. <b>Asked: 2–5 questions every session</b> (terms plus entries). Favourites:</p>
<ul class="small"><li>Due-date calculation with days of grace and a holiday</li>
<li>Accommodation bill</li>
<li>Entries for discounting, endorsement, collection and dishonour</li>
<li>Rebate on retiring a bill</li>
<li>Bill vs promissory note statements</li></ul>

<h3>1. Instruments (Negotiable Instruments Act, 1881)</h3>
<table><tr><th></th><th>Bill of exchange (Sec 5)</th><th>Promissory note (Sec 4)</th><th>Cheque (Sec 6)</th></tr>
<tr><td>Nature</td><td>Unconditional <b>order</b></td><td>Unconditional <b>promise</b></td><td>Bill drawn on a specified <b>banker</b>, payable on demand (includes electronic cheques and truncated cheque images)</td></tr>
<tr><td>Parties</td><td>3: drawer, drawee (acceptor), payee (drawer and payee may be the same)</td><td>2: maker, payee</td><td>3: drawer, bank (drawee), payee</td></tr>
<tr><td>Acceptance</td><td>Needed (for time bills)</td><td>Not needed</td><td>Not needed</td></tr>
<tr><td>Days of grace</td><td>3 days for time bills</td><td>3 days (if payable after time)</td><td>None (always on demand)</td></tr>
<tr><td>Noting / protest</td><td>Possible on dishonour</td><td>Possible</td><td>Not needed</td></tr>
<tr><td>Payable to bearer on demand?</td><td>Not allowed</td><td>Cannot be made payable to bearer (only RBI/Govt may issue such notes, Sec 31 RBI Act)</td><td>Allowed</td></tr></table>

<h3>2. Key terms</h3>
<ul><li><b>Drawer</b>: the creditor who draws the bill. <b>Drawee</b>: the debtor on whom it is drawn; after accepting, the <b>acceptor</b>.</li>
<li><b>Payee</b>: the person to be paid.</li>
<li><b>Holder</b>: entitled in his own name to possession and to receive payment.</li>
<li><b>Holder in due course</b>: took it for consideration, before maturity, in good faith.</li>
<li><b>Tenor / usance</b>: the period of the bill.</li>
<li><b>Sight / demand bill</b>: payable on presentation, no grace days.</li>
<li><b>After-date bill</b>: period counted from the date of drawing. <b>After-sight bill</b>: counted from the date of <b>acceptance</b>.</li>
<li><b>Endorsement</b>: signing on the back to transfer. Endorser → endorsee.</li>
<li><b>Discounting</b>: selling the bill to a bank before maturity for less than face value.</li>
<li><b>Dishonour</b>: by non-acceptance or non-payment.</li>
<li><b>Noting</b>: a notary public records the fact of dishonour. <b>Noting charges</b> are paid by the holder and recovered from the drawee.</li>
<li><b>Protest</b>: a formal certificate of dishonour by a notary.</li>
<li><b>Retiring a bill</b>: the acceptor pays <b>before</b> the due date and the holder allows a <b>rebate</b>, i.e. a discount for the unexpired period.</li>
<li><b>Renewal</b>: the old bill is cancelled and a new bill is drawn, usually with interest, when the acceptor can't pay.</li>
<li><b>Trade bill</b>: backed by a genuine sale of goods.</li>
<li><b>Accommodation bill</b>: drawn and accepted <b>without consideration</b>, only to raise funds by discounting. It is legally enforceable by a holder in due course, but there is no underlying trade, so credit risk is higher. Banks are told to avoid discounting accommodation bills. Sec 43: the accommodating party is not liable to the party accommodated.</li></ul>

<h3>3. Due date (maturity)</h3>
<div class="box key">
<ul><li><b>Due date = date of drawing (or acceptance, for after-sight bills) + tenor + 3 days of grace.</b></li>
<li><b>Months:</b> calendar months. If the due month has no corresponding date, use its <b>last day</b>.</li>
<li><b>Days:</b> exclude the day of drawing.</li>
<li>If the due date is a <b>public holiday</b>, the bill is due on the <b>preceding business day</b> (Sec 25).</li></ul></div>
<table><tr><th>Bill</th><th>Working</th><th>Due date</th></tr>
<tr><td>Drawn 13 May 2023, 1 month</td><td>13 Jun + 3</td><td><b>16 June 2023</b></td></tr>
<tr><td>Drawn 23 Nov 2024, 2 months</td><td>23 Jan + 3 = 26 Jan 2025, Republic Day → preceding day</td><td><b>25 January 2025</b></td></tr>
<tr><td>Drawn 31 Jan 2026, 1 month</td><td>Feb has no 31st → 28 Feb + 3</td><td><b>3 March 2026</b></td></tr>
<tr><td>Drawn 10 Jan 2026, 90 days after date</td><td>Jan 21 days + Feb 28 + Mar 31 = 80 → 10 more days = 10 Apr; + 3</td><td><b>13 April 2026</b></td></tr>
<tr><td>Accepted 5 Mar 2026, 2 months after <b>sight</b></td><td>5 May + 3</td><td><b>8 May 2026</b></td></tr></table>

<h3>4. Entries (drawer's books = holder)</h3>
<table><tr><th>Event</th><th>Drawer / holder</th><th>Drawee / acceptor</th></tr>
<tr><td>Bill drawn and accepted</td><td>Bills Receivable Dr; To Debtor</td><td>Creditor Dr; To Bills Payable</td></tr>
<tr><td>(a) Held till maturity, paid</td><td>Cash Dr; To B/R</td><td>B/P Dr; To Cash</td></tr>
<tr><td>(b) Discounted with bank</td><td>Bank Dr + Discount Dr; To B/R</td><td>No entry</td></tr>
<tr><td>(c) Endorsed to a creditor</td><td>Creditor Dr; To B/R</td><td>No entry</td></tr>
<tr><td>(d) Sent to bank for collection</td><td>Bills sent for collection Dr; To B/R. On collection: Bank Dr; To BSFC</td><td>No entry</td></tr>
<tr><td>Dishonour (bill with holder)</td><td>Debtor Dr; To B/R (+ noting charges: Debtor Dr; To Cash)</td><td>B/P Dr + Noting charges Dr; To Creditor</td></tr>
<tr><td>Dishonour (bill discounted)</td><td>Debtor Dr; To Bank (bank recovers from drawer)</td><td>same as above</td></tr>
<tr><td>Dishonour (bill endorsed)</td><td>Debtor Dr; To Creditor (endorsee)</td><td>same as above</td></tr>
<tr><td>Retired early</td><td>Cash Dr + Rebate on bills Dr; To B/R</td><td>B/P Dr; To Cash + Rebate on bills (income)</td></tr></table>
<ul><li>Discount on a discounted bill = face value × rate × unexpired period. It is a <b>finance cost</b> for the drawer. Sales were already recorded when the goods were sold.</li>
<li><b>Bill books:</b> the Bills Receivable Book and Bills Payable Book (subsidiary books).</li></ul>

<div class="box trap"><b>Traps:</b>
<ul><li>No days of grace for demand/sight bills and cheques.</li>
<li>"Legal acceptance makes it a genuine trade bill": wrong. Acceptance makes it enforceable, not genuine.</li>
<li>An after-sight bill counts from <b>acceptance</b>.</li>
<li>When a <b>discounted</b> bill is dishonoured, the drawer credits <b>Bank</b>, not B/R.</li>
<li>Rebate on retiring a bill is an <b>expense for the holder</b> and <b>income for the acceptor</b>.</li></ul></div>
''')

Q('A8', """A bill was drawn on 23 November 2024 payable two months after date. 26 January is a public holiday. What is the due date?""",
  "25 January 2025", ["26 January 2025", "24 January 2025", "27 January 2025"],
  "23 Jan 2025 + 3 days of grace = 26 Jan 2025, a public holiday. Under Section 25 of the NI Act the bill is payable on the preceding business day, 25 January 2025.")

Q('A8', """A bill dated 31 January 2026 is payable one month after date. Its due date is:""",
  "3 March 2026", ["28 February 2026", "2 March 2026", "4 March 2026"],
  "One calendar month from 31 Jan: February has no 31st, so take 28 Feb 2026. Add 3 days of grace = 3 March 2026.")

Q('A8', """Vertex Engineering drew a bill on 10 January 2026 payable 90 days after date. Ignoring holidays, the due date is:""",
  "13 April 2026", ["10 April 2026", "11 April 2026", "12 April 2026"],
  "Exclude the date of drawing: Jan 11–31 = 21 days, Feb = 28 (total 49), Mar = 31 (total 80), plus 10 days of April = 90 → 10 April. Add 3 days of grace → 13 April 2026.")

Q('A8', """A bill payable 'two months after sight' is drawn on 20 February 2026 and accepted on 5 March 2026. Its due date is:""",
  "8 May 2026", ["23 April 2026", "5 May 2026", "20 April 2026"],
  "For after-sight bills, time runs from the date of acceptance (sight): 5 March + 2 months = 5 May + 3 days of grace = 8 May 2026.")

Q('A8', """Three group companies face a cash crunch. X draws a bill on Y; Y accepts though no goods are sold; X discounts it with a bank and shares the proceeds with Y. The credit officer says 'Y legally accepted it, so it is a genuine trade bill.' Which is correct?""",
  "It is an accommodation bill: enforceable by a holder in due course, but with no trade behind it and higher credit risk",
  ["It is a genuine trade bill, because acceptance by the drawee is conclusive proof of an underlying sale", "It automatically becomes a demand bill, because no goods were supplied and so no credit period exists",
   "It is void for want of consideration and cannot be enforced by anyone, including the discounting bank"],
  "An accommodation bill is drawn and accepted without consideration to raise funds. It can be enforced by a holder in due course for value, but there is no self-liquidating trade transaction behind it. Banks are advised not to discount accommodation bills.")

Q('A8', """Horizon Traders discounted a ₹1,00,000, 90-day bill receivable with its bank at 12% p.a. with 60 days to run. Which entry does Horizon pass?""",
  "Bank A/c Dr ₹98,027; Discount A/c Dr ₹1,973; To Bills Receivable A/c ₹1,00,000",
  ["Bank A/c Dr ₹1,00,000; To Bills Receivable A/c ₹1,00,000", "Bank A/c Dr ₹97,041; Discount A/c Dr ₹2,959; To Sales A/c ₹1,00,000",
   "Bills Receivable A/c Dr ₹1,00,000; To Bank A/c ₹98,027; To Discount A/c ₹1,973"],
  "Discount = 1,00,000 × 12% × 60/365 = ₹1,973 (rounded). Bank receives ₹98,027. The bill (asset) is replaced by cash; discount is a finance cost. Sales were recorded when the goods were sold.")

Q('A8', """A bill receivable that had been discounted with the bank is dishonoured on maturity; the bank pays noting charges of ₹100. In the drawer's books the entry is:""",
  "Drawee's A/c Dr (bill amount + ₹100); To Bank A/c", ["Drawee's A/c Dr; To Bills Receivable A/c", "Bills Receivable A/c Dr; To Bank A/c",
   "Bank A/c Dr; To Drawee's A/c"],
  "The bill is no longer in the drawer's B/R account (it was discounted). The bank recovers the amount plus noting charges from the drawer, and the drawer in turn charges the drawee.")

Q('A8', """The acceptor of a ₹50,000 bill pays it one month before maturity, and the holder allows a rebate of ₹500. In the holder's books the entry is:""",
  "Cash Dr ₹49,500; Rebate on Bills Dr ₹500; To Bills Receivable ₹50,000", ["Cash Dr ₹50,000; To Bills Receivable ₹49,500; To Rebate ₹500",
   "Bills Payable Dr ₹50,000; To Cash ₹49,500; To Rebate ₹500", "Cash Dr ₹49,500; To Bills Receivable ₹49,500"],
  "This is retiring a bill. The holder allows a rebate (expense to him); the acceptor records the rebate as income.")

Q('A8', """Consider the following statements:
1. A promissory note contains an unconditional promise; a bill contains an unconditional order.
2. A bill must be accepted by the drawee before it binds him; a promissory note needs no acceptance.
3. A cheque is entitled to three days of grace.
4. A promissory note can be made payable to bearer on demand by any trader.
Which are correct?""",
  "1 and 2 only", ["1, 2 and 3 only", "1, 2 and 4 only", "2 and 3 only"],
  "Cheques are always payable on demand, with no grace days (3 wrong). Section 31 of the RBI Act bars anyone other than RBI (and the Government in specified cases) from issuing promissory notes payable to bearer on demand (4 wrong).")

Q('A8', """When a bill of exchange is sent to the bank for collection, the drawer passes:""",
  "Bills Sent for Collection A/c Dr; To Bills Receivable A/c", ["Bank A/c Dr; To Bills Receivable A/c (as if already collected)", "Bills Receivable A/c Dr; To Bank A/c (on handing over)",
   "No entry at all until the bank actually collects the amount"],
  "The bill moves from 'in hand' to 'with bank for collection'. When the bank collects: Bank A/c Dr; To Bills Sent for Collection A/c.")

Q('A8', """Which of the following is correct about noting of a dishonoured bill?""",
  "It is done by a notary public, and noting charges paid by the holder are ultimately recoverable from the drawee",
  ["It is done by the drawer himself, and the noting charges are a loss to the drawer", "It is done by the bank, and the noting charges are always borne by the collecting bank", "It is compulsory for every dishonoured cheque before a complaint can be filed"],
  "A notary public records the dishonour (noting); a protest is the formal certificate. Noting charges are paid by the holder and charged to the party liable.")
