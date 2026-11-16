from qb import note, Q

note('A5', r'''
<p class="small">Syllabus: Cash book vs pass book, causes of difference, preparing a BRS, adjusting the cash book balance, advantages. <b>Asked: 2 questions every session since June 2024.</b> May 2026 asked:</p>
<ul class="small"><li>which items need a cash-book entry vs which are timing differences</li>
<li>starting from an overdraft</li>
<li>CB ₹20,000 vs PB ₹28,000</li>
<li>a posting error vs an unpresented cheque</li></ul>

<h3>1. Mirror image</h3>
<ul><li>Your <b>cash book</b> (bank column) and the bank's <b>pass book / statement</b> record the same account from opposite sides.</li>
<li>A <b>debit</b> balance in the cash book = <b>credit</b> balance in the pass book = money in the bank (favourable).</li>
<li>An <b>overdraft</b> = <b>credit</b> balance in the cash book = <b>debit</b> balance in the pass book.</li>
<li>So the pass book is a mirror image only when there are no timing differences or errors, which is rare.</li></ul>

<h3>2. Causes of difference — sort them into three boxes</h3>
<table><tr><th>Box</th><th>Items</th><th>Cash book entry needed?</th></tr>
<tr><td><b>A. Timing differences</b> (in the CB, not yet in the bank)</td><td>
<ul><li>Cheques issued but <b>not yet presented</b></li>
<li>Cheques deposited but <b>not yet collected/credited</b></li></ul></td><td><b>No.</b> They clear by themselves; show them only in the BRS.</td></tr>
<tr><td><b>B. Bank-originated items</b> (in the bank, not yet in the CB)</td><td>
<ul><li>Bank charges and commission</li>
<li>Interest credited or debited by the bank</li>
<li><b>Direct deposits</b> by customers / NEFT received</li>
<li>Dividend or interest collected by the bank</li>
<li>Payments under <b>standing instructions</b> (insurance, EMI)</li>
<li><b>Dishonoured</b> cheques</li></ul></td><td><b>Yes.</b> Update the cash book (adjusted cash book).</td></tr>
<tr><td><b>C. Errors</b></td><td>
<ul><li>By the firm (wrong amount or side in the CB, casting errors): <b>correct the CB</b>.</li>
<li>By the bank (wrong debit or credit): <b>show in the BRS</b> and ask the bank to correct.</li></ul></td><td>Firm's errors: Yes. Bank's errors: No.</td></tr></table>

<h3>3. Direction rules (starting from a favourable cash-book balance)</h3>
<table><tr><th>Item</th><th>Start: CB debit balance → find PB</th></tr>
<tr><td>Cheques issued, not presented</td><td><b>Add</b> (the bank hasn't reduced the balance yet)</td></tr>
<tr><td>Cheques deposited, not credited</td><td><b>Less</b></td></tr>
<tr><td>Interest / dividend / direct deposit credited by bank</td><td><b>Add</b></td></tr>
<tr><td>Bank charges, SI payment, interest on OD, dishonoured cheque</td><td><b>Less</b></td></tr></table>
<p><b>Shortcut:</b> ask "is the bank's balance higher or lower than mine because of this item?"</p>
<ul><li>Starting from the PB, reverse every sign.</li>
<li>Starting from an <b>overdraft</b>, treat it as a negative number and apply the same logic. Or use the rule: <b>add what reduces the overdraft, subtract what increases it</b>, and remember that items which raise a favourable balance reduce an overdraft.</li></ul>

<h3>4. Worked examples</h3>
<p><b>(a)</b> CB debit ₹40,000; cheques issued not presented ₹12,000; cheques deposited not cleared ₹8,000; bank charges ₹1,000 not in CB; interest credited ₹600.<br>
PB = 40,000 + 12,000 − 8,000 − 1,000 + 600 = <b>₹43,600 (credit)</b>.</p>
<p><b>(b)</b> CB overdraft ₹80,000; cheques issued not presented ₹15,000; cheques deposited not credited ₹22,000; bank charges ₹500; OD interest ₹2,500; direct deposit ₹12,000.<br>
Treat as −80,000: −80,000 + 15,000 − 22,000 − 500 − 2,500 + 12,000 = −78,000 → <b>overdraft ₹78,000 as per PB</b>.</p>
<p><b>(c) Adjusted cash book first.</b> CB ₹24.80 lakh. Dishonoured cheque ₹1.10 lakh, bank charges ₹12,500, dividend credited ₹95,000, SI insurance ₹48,000:<br>
Adjusted CB = 24,80,000 − 1,10,000 − 12,500 + 95,000 − 48,000 = <b>₹23,04,500</b>.<br>
Then the BRS shows only the timing item: + unpresented cheques ₹4.20 lakh → PB ₹27,24,500.</p>
<p><b>(d) Error.</b> A cheque deposited of ₹1,80,000 was entered in the CB as ₹18,000. The CB is understated by ₹1,62,000, so correct the cash book (it is not a timing difference).</p>

<h3>5. Need and advantages</h3>
<ul><li>Detects errors and frauds.</li>
<li>Shows the true bank balance for the Balance Sheet (the <b>adjusted cash-book balance</b> goes to the Balance Sheet, not the pass-book balance).</li>
<li>Reveals stale or undelivered cheques and keeps a check on bank charges.</li>
<li>Prepared periodically (monthly). Banks reconcile their own nostro and inter-branch accounts similarly (chapter A9).</li></ul>

<div class="box trap"><b>Traps:</b>
<ul><li>"All items only in the BRS, no CB entry": wrong. Bank-originated items need CB entries.</li>
<li>An unpresented cheque is the <b>only</b> classic item that never needs a CB entry.</li>
<li>In the Balance Sheet, show the <b>adjusted CB balance</b>.</li>
<li>Overdraft questions reverse your instinct: an unpresented cheque <b>reduces</b> the overdraft per pass book.</li>
<li>A cheque recorded in the CB but deposited late = timing (deposited, not credited).</li></ul></div>
''')

Q('A5', """On 31 March, Nova Enterprises' cash book shows ₹24,80,000 (debit). Items found: outstanding cheques ₹4,20,000; a dishonoured cheque not recorded ₹1,10,000; bank charges ₹12,500; dividend credited directly ₹95,000; insurance premium paid under standing instruction ₹48,000. What is the adjusted cash-book balance to be shown in the Balance Sheet?""",
  "₹23,04,500", ["₹27,24,500", "₹24,80,000", "₹19,04,500"],
  "Only bank-originated items adjust the cash book: 24,80,000 − 1,10,000 − 12,500 + 95,000 − 48,000 = ₹23,04,500. Outstanding cheques are a timing difference shown only in the BRS. (Balance as per pass book would be 23,04,500 + 4,20,000 = ₹27,24,500.)")

Q('A5', """Cash book shows a debit balance of ₹40,000. Cheques issued but not presented ₹12,000; cheques deposited but not collected ₹8,000; bank charges ₹1,000 not recorded in the cash book; interest credited by bank ₹600. What is the balance as per pass book?""",
  "₹43,600 credit", ["₹36,400 credit", "₹45,600 credit", "₹42,400 credit"],
  "40,000 + 12,000 (unpresented, bank not yet reduced) − 8,000 (deposit not yet credited) − 1,000 (charges) + 600 (interest) = ₹43,600 (a credit balance in the pass book means money with the bank).")

Q('A5', """Cash book shows an overdraft of ₹80,000. Cheques issued not presented ₹15,000; cheques deposited not credited ₹22,000; bank charges ₹500 and interest on overdraft ₹2,500 debited by bank; a customer deposited ₹12,000 directly. What is the overdraft as per pass book?""",
  "₹78,000", ["₹82,000", "₹1,02,000", "₹58,000"],
  "Treat the overdraft as −80,000. Unpresented cheques +15,000 (bank hasn't paid yet), uncredited deposits −22,000, charges −500, interest −2,500, direct deposit +12,000 → −78,000, i.e. overdraft ₹78,000 per pass book.")

Q('A5', """While preparing a BRS, which of these require a correcting entry in the cash book itself?
1. Cheque deposited ₹1,80,000 recorded in the cash book as ₹18,000.
2. Bank charges debited by the bank, not yet recorded.
3. A cheque issued that is still unpresented.
4. Interest credited by the bank, not entered in the cash book.
5. A cheque wrongly debited by the bank to our account (belongs to another customer).""",
  "1, 2 and 4 only", ["1, 2, 4 and 5 only", "2 and 4 only", "1, 2, 3 and 4"],
  "The firm's own error (1) and bank-originated items (2, 4) are corrected in the cash book. An unpresented cheque (3) is a timing difference. A bank's error (5) is shown in the BRS and the bank is asked to reverse it; our cash book is correct.")

Q('A5', """Balance as per cash book is ₹20,000 and as per pass book ₹28,000 (both favourable). If there is no other difference, which single item explains it?""",
  "Cheques of ₹8,000 issued but not yet presented for payment",
  ["Cheques of ₹8,000 deposited but not yet credited by the bank", "Bank charges of ₹8,000 not yet recorded in the cash book",
   "A cheque of ₹8,000 deposited and dishonoured, not yet recorded in the cash book"],
  "The pass book is higher by ₹8,000. Unpresented cheques have reduced the cash book but not yet the bank balance. The other three items would make the pass book lower than the cash book.")

Q('A5', """Starting from the balance as per pass book (credit ₹50,000), how should 'cheques deposited but not yet collected ₹6,000' be treated to arrive at the cash-book balance?""",
  "Added, giving ₹56,000", ["Deducted, giving ₹44,000", "Ignored, as it is a timing difference", "Deducted, giving ₹44,000 overdraft"],
  "The cash book already includes the deposit; the bank does not. So the cash book is higher: start at 50,000 and add 6,000 = ₹56,000.")

Q('A5', """Which balance of bank is shown in the Balance Sheet after preparing the BRS?""",
  "The cash-book balance after recording bank charges, direct credits and other omitted items (adjusted cash book)",
  ["The pass-book balance, because it is prepared independently by the bank and is therefore reliable", "The average of the cash-book and pass-book balances, to spread the timing differences",
   "The unadjusted cash-book balance, because the BRS is only a statement and needs no entries"],
  "After all bank-originated items and the firm's errors are entered, the adjusted cash book shows the true balance from the firm's side. Timing differences don't change the firm's true position.")

Q('A5', """Which statement about the pass book being a 'mirror image' of the cash book is correct?""",
  "A debit in the cash book bank column appears as a credit in the pass book, but timing differences and errors make the balances differ",
  ["The pass book always shows exactly the same balance as the cash book on any given date", "An overdraft appears as a debit balance in the cash book and a credit balance in the pass book",
   "A favourable cash-book balance appears as a debit balance in the pass book prepared by the bank"],
  "The customer's asset (debit in cash book) is the bank's liability (credit in pass book). Overdraft = credit in cash book, debit in pass book. Balances match only if no timing differences or errors exist.")

Q('A5', """A trainee argues: "Since the bank statement is correct, we should just copy its closing balance into the books and skip the BRS." Which is the strongest objection?""",
  "The bank statement omits timing items and may itself contain errors; a BRS identifies these and protects against errors and fraud",
  ["The bank statement is not admissible in court as evidence, so the firm's own records must prevail", "A BRS is required only for overdraft accounts, where interest is charged on daily balances",
   "Bank balances are not shown in the Balance Sheet, so the closing balance has no use in the books"],
  "The bank doesn't yet know about unpresented and uncleared cheques, and banks do make errors. Reconciliation is a key internal control against errors and frauds.")

Q('A5', """A cheque of ₹15,000 received from a debtor was recorded in the cash book and deposited, but the bank returned it dishonoured; this is not yet recorded. Starting from the cash-book balance, how is it treated?""",
  "Deducted to find the pass-book balance, and a cash-book entry 'Debtor Dr; To Bank' must be passed",
  ["Added to find the pass-book balance with no cash-book entry", "Ignored because the debtor will pay later",
   "Deducted in the BRS only, no cash-book entry because it is a timing difference"],
  "The bank has already reversed the credit, so its balance is lower. A dishonour is a real event: the debtor owes again, so the cash book must be corrected.")
