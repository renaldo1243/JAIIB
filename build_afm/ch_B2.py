from qb import note, Q

note('B2', r'''
<p class="small">Syllabus: Definition and types of companies, partnership vs LLP vs company, classes of share capital, issue of shares, non-voting shares. <b>Asked: 3 questions on types of companies plus 3–4 on share capital every session.</b> May 2026 asked:</p>
<ul class="small"><li>pro-rata allotment (twice)</li>
<li>forfeiture with premium unpaid</li>
<li>forfeiture entry</li>
<li>paid-up vs issued capital</li>
<li>cumulative preference arrears</li>
<li>uses of securities premium</li>
<li>sweat equity</li>
<li>authorised capital</li>
<li>over-subscription</li>
<li>preference-share statements</li>
<li>a private company definition</li>
<li>the Food Corporation of India</li></ul>

<h3>1. Types of companies (Companies Act 2013)</h3>
<table><tr><th>Type</th><th>Key test</th></tr>
<tr><td><b>Private company</b> (Sec 2(68))</td><td>Its Articles:
<ul><li>restrict the right to transfer shares</li>
<li>limit members to <b>200</b> (excluding employee-members)</li>
<li>prohibit invitations to the public to subscribe</li></ul>
Minimum 2 members, 2 directors.</td></tr>
<tr><td><b>Public company</b> (Sec 2(71))</td><td>Not private. Minimum <b>7</b> members, 3 directors. A subsidiary of a public company is deemed public.</td></tr>
<tr><td><b>One Person Company</b></td><td>Single member, a natural person who is an Indian citizen. Must name a nominee.</td></tr>
<tr><td><b>Holding / subsidiary</b> (Sec 2(87))</td><td>The holding company controls the composition of the board <b>or</b> holds/controls <b>more than one-half of total voting power</b>.</td></tr>
<tr><td>Associate</td><td>Significant influence: ≥ <b>20%</b> of voting power or business decisions under agreement.</td></tr>
<tr><td><b>Government company</b> (Sec 2(45))</td><td>≥ <b>51%</b> of paid-up capital held by the Central and/or State Governments (e.g. Coal India).</td></tr>
<tr><td><b>Statutory corporation</b></td><td>Created by a special Act of Parliament (e.g. LIC; <b>Food Corporation of India</b>, formed under the Food Corporations Act 1964; RBI).</td></tr>
<tr><td>Section 8 company</td><td>Not-for-profit (charity, education). Profits are not distributed.</td></tr>
<tr><td>Limited by shares / by guarantee / unlimited</td><td>Liability limited to unpaid share value / to the guaranteed amount / unlimited.</td></tr></table>

<h3>2. Share capital layers</h3>
<div class="box key"><b>Authorised (nominal)</b> = maximum per the Memorandum of Association.<br>
≥ <b>Issued</b> = offered to the public.<br>
≥ <b>Subscribed</b> = taken up.<br>
≥ <b>Called-up</b> = demanded so far.<br>
≥ <b>Paid-up</b> = called-up − calls in arrears.<br>
Forfeiture reduces paid-up capital (the forfeited amount is shown separately). It does not change authorised capital.</div>
<ul><li><b>Equity shares:</b> with voting rights, or with <b>differential rights (DVR)</b>. DVR shares can be up to <b>74%</b> of total post-issue paid-up equity capital (2019 amendment raised it from 26%).</li>
<li><b>Preference shares</b> (Sec 43, 55):
<ul><li>preference as to <b>dividend and repayment of capital</b></li>
<li>vote only on resolutions affecting their rights, <b>or on all resolutions if their dividend is unpaid for 2 years or more</b></li>
<li><b>no irredeemable preference shares</b></li>
<li>maximum tenure <b>20 years</b> (up to 30 years for infrastructure projects, with 10% redeemed yearly from the 21st year)</li>
<li>types: cumulative / non-cumulative, participating / non-participating, convertible / non-convertible</li></ul></li>
<li><b>Cumulative arrears:</b> must be cleared before any equity dividend. They don't make preference holders equity holders and don't reduce paid-up capital. Arrears are disclosed as a contingent liability (not provided for).</li></ul>

<h3>3. Issue of shares</h3>
<ul><li>Shares can be issued at par or at a <b>premium</b>. Issue at a discount is <b>void</b> (Sec 53), except sweat equity.</li>
<li><b>Entries:</b>
<ul><li>Bank Dr; To Share Application</li>
<li>Share Application Dr; To Share Capital (+ To Securities Premium if premium is on application)</li>
<li>Allotment and calls follow the same pattern</li></ul></li>
<li><b>Calls in arrears:</b> interest up to 10%. <b>Calls in advance:</b> interest up to 12% (Table F defaults).</li>
<li><b>Over-subscription</b> (applications exceed shares offered), handled by:
<ul><li>rejecting some applications (money refunded)</li>
<li>full allotment to some</li>
<li><b>pro-rata</b> allotment, where excess application money is adjusted against allotment</li></ul></li>
<li><b>Pro-rata example:</b> offered 2,40,000; applied 3,60,000; 40,000 rejected → 3,20,000 get 2,40,000 = 3 : 4. An applicant for 18,000 gets <b>13,500</b>.</li>
<li><b>Minimum subscription:</b> 90% of the issue for a public issue, else money is refunded.</li></ul>

<h3>4. Forfeiture and reissue</h3>
<ul><li><b>Forfeiture entry:</b>
<br>Share Capital Dr (amount <b>called up</b>);
<br>Securities Premium Dr (only if the premium was <b>not received</b>);
<br>To Calls in arrears / unpaid allotment;
<br>To Share Forfeiture (amount <b>received</b>).</li>
<li><b>Example:</b> 1,000 shares of ₹10 at a ₹2 premium. Application ₹3; allotment ₹5 (including the premium); call ₹4. The holder paid only the application money.
<ul><li>Share Capital Dr 10,000</li>
<li>Securities Premium Dr 2,000</li>
<li>To Allotment 5,000; To Call 4,000; To Share Forfeiture 3,000</li></ul></li>
<li><b>Reissue</b> at ₹8 fully paid: Bank 8,000 + Forfeiture 2,000 Dr; To Share Capital 10,000. The remaining forfeiture balance of ₹1,000 → <b>Capital Reserve</b>.</li>
<li>If the premium <b>was received</b> before forfeiture, Securities Premium is <b>not</b> debited.</li></ul>

<h3>5. Securities premium (Sec 52) — permitted uses only</h3>
<ul><li>issue of fully paid <b>bonus shares</b></li>
<li>writing off <b>preliminary expenses</b></li>
<li>writing off expenses, commission or discount on issue of shares or debentures</li>
<li>premium on redemption of preference shares or debentures</li>
<li><b>buy-back</b> of own shares (Sec 68)</li></ul>
<p><b>Never</b> for cash dividends.</p>

<h3>6. Sweat equity and ESOP</h3>
<ul><li><b>Sweat equity</b> (Sec 54): shares to employees or directors at a discount or for non-cash consideration (know-how, IPR, value addition). Needs a special resolution.
<ul><li>No fresh cash comes in.</li>
<li>Existing holders are diluted.</li>
<li>It helps retain talent.</li>
<li>Lock-in of 3 years.</li></ul></li>
<li><b>ESOP</b> (Sec 62(1)(b)): an option to buy shares at a set price after a minimum vesting period of 1 year. Accounting is in chapter B3.</li></ul>

<div class="box trap"><b>Traps:</b>
<ul><li>Pro-rata ratio = shares offered ÷ applications <b>accepted</b> (after rejections).</li>
<li>Share Capital is debited with the <b>called-up</b> amount on forfeiture, not the paid amount.</li>
<li>FCI is a statutory corporation (special Act), not a company registered under the Companies Act.</li>
<li>Preference shares can't be irredeemable. Maximum tenure is 20 years.</li>
<li>Authorised capital is the ceiling: issued capital can't exceed it.</li></ul></div>
''')

Q('B2', """Galaxy Ltd. offered 2,40,000 shares; applications were received for 3,60,000. Applications for 40,000 shares were rejected and the rest got pro-rata allotment. Mr Arjun applied for 18,000 shares. How many does he get?""",
  "13,500 shares", ["12,000 shares", "14,400 shares", "15,000 shares"],
  "Accepted applications = 3,60,000 − 40,000 = 3,20,000 for 2,40,000 shares → 3 : 4. 18,000 × 3/4 = 13,500. Using all 3,60,000 (ratio 2/3) gives 12,000, the trap.")

Q('B2', """In the same allotment (application money ₹4 per share), how much excess application money from Mr Arjun is available to adjust against allotment?""",
  "₹18,000", ["₹72,000", "₹54,000", "₹13,500"],
  "He paid 18,000 × ₹4 = 72,000 but needed only 13,500 × ₹4 = 54,000 on application. The excess ₹18,000 is adjusted towards allotment money due.")

Q('B2', """1,000 equity shares of ₹10 issued at a premium of ₹2 (payable on allotment). Application ₹3, allotment ₹5 (incl. premium), final call ₹4. A shareholder paid only the application money and the shares were forfeited after the final call. The forfeiture entry credits Share Forfeiture with:""",
  "₹3,000, after debiting Share Capital ₹10,000 and Securities Premium ₹2,000", ["₹3,000, after debiting Share Capital ₹12,000",
   "₹5,000, after debiting Share Capital ₹10,000 only", "₹3,000, after debiting Share Capital ₹3,000 only"],
  "Share Capital is debited with the called-up ₹10,000; Securities Premium ₹2,000 is debited because the premium was never received; allotment (₹5,000) and call (₹4,000) unpaid are credited; Share Forfeiture gets the amount received, ₹3,000.")

Q('B2', """Those 1,000 forfeited shares (forfeiture balance ₹3,000) are reissued as fully paid at ₹8 each. What is transferred to Capital Reserve?""",
  "₹1,000", ["₹3,000", "₹2,000", "Nil"],
  "Discount on reissue = ₹2 × 1,000 = ₹2,000, met from the forfeiture account. The balance ₹1,000 is a capital profit, transferred to Capital Reserve.")

Q('B2', """Zenstar Ltd. forfeited shares of ₹10 each (issued at ₹12) after the holder paid application and allotment (including the premium) but not the final call. Which treatment is correct?""",
  "Share Capital is debited with the called-up amount; Securities Premium is not touched",
  ["Share Capital is debited only with the amount actually received from the holder", "Securities Premium is always debited on forfeiture whether or not it was received",
   "Calls in arrears never appear in a forfeiture entry"],
  "Premium already received stays in Securities Premium. Share Capital is debited with the called-up value; unpaid calls are credited; the amount received goes to Share Forfeiture.")

Q('B2', """Delta Infrastructure has 10% cumulative preference capital of ₹15 crore; no dividend was paid for two years due to losses. Profits are now adequate. Which statements are correct?
1. Preference holders automatically become equity holders after two years of unpaid dividend.
2. Arrears must ordinarily be paid before any equity dividend.
3. Arrears represent accumulated contractual preference rights.
4. Non-payment reduces the paid-up preference capital.""",
  "2 and 3 only", ["1, 2 and 4 only", "2, 3 and 4 only", "1 and 3 only"],
  "Cumulative dividend accumulates and ranks ahead of equity dividend. Non-payment for 2 years gives preference holders voting rights on all resolutions, not conversion to equity; capital is unaffected.")

Q('B2', """For which purposes can Securities Premium be used under Section 52?
1. Writing off preliminary expenses.
2. Paying cash dividend.
3. Issuing fully paid bonus shares.
4. Writing off commission paid on issue of shares.
5. Buy-back of the company's own shares.""",
  "1, 3, 4 and 5 only", ["1, 2, 3 and 4 only", "2, 3 and 5 only", "All five"],
  "Sec 52 lists bonus issue, preliminary expenses, issue expenses/commission/discount, premium on redemption, and buy-back (Sec 68). It cannot be used for cash dividends.")

Q('B2', """InnovateX issues equity shares to its Chief Scientist in exchange for a patented technology instead of cash. Which statements are correct?
1. Existing shareholders' percentage may be diluted.
2. The issue brings fresh cash into the company.
3. The shares are issued for intellectual property (sweat equity).
4. Such issues can help retain skilled employees.""",
  "1, 3 and 4 only", ["2 and 4 only", "1 and 2 only", "1, 2, 3 and 4"],
  "Sweat equity is issued for know-how or IPR, so no cash comes in. It increases the number of shares (dilution) and is used to reward and retain talent.")

Q('B2', """Which statement on preference shares under the Companies Act, 2013 is NOT correct?""",
  "A company may issue irredeemable preference shares with Board approval",
  ["Preference shares carry preferential rights as to dividend and repayment of capital", "Preference shares must normally be redeemed within 20 years of issue",
   "Preference holders can vote on all resolutions if their dividend remains unpaid for two years or more"],
  "Sec 55 prohibits irredeemable preference shares. Maximum tenure is 20 years (30 for infrastructure).")

Q('B2', """Galaxy Ltd. has authorised capital ₹20 crore, issued capital of 1.5 crore shares of ₹10, some calls unpaid and some shares forfeited but not reissued. A trainee wants to cut 'issued capital' because of forfeiture. Which is correct?""",
  "Paid-up capital falls on forfeiture; issued capital does not change merely because of it",
  ["Issued capital automatically falls once any shares are forfeited by the Board", "Authorised capital always equals paid-up capital at the year-end",
   "Forfeiture affects only the Securities Premium Account and nothing else"],
  "Paid-up = called-up less arrears (forfeited amounts move to Share Forfeiture). Authorised is the MoA ceiling; issued is what was offered.")

Q('B2', """The maximum amount of share capital a company is authorised to issue, as stated in its Memorandum of Association, is called:""",
  "Authorised (nominal) capital", ["Issued capital", "Subscribed capital", "Called-up capital"],
  "Authorised capital is the ceiling in the MoA; issued, subscribed, called-up and paid-up capital cannot exceed it.")

Q('B2', """The Food Corporation of India is an example of a:""",
  "Statutory corporation created by a special Act of Parliament", ["Private company limited by shares", "Government company registered under the Companies Act, 2013",
   "Section 8 non-profit company"],
  "FCI was set up under the Food Corporations Act, 1964, a special statute, like LIC (LIC Act 1956).")

Q('B2', """Under the Companies Act, 2013, a company becomes a subsidiary of another when the other company:""",
  "Controls its board composition or more than half of its total voting power",
  ["Holds at least 20% of its voting power", "Has at least one common director on its Board", "Supplies more than half of its raw materials"],
  "Sec 2(87): control of board composition or more than half the total voting power (alone or with subsidiaries). 20% is the associate (significant influence) test.")

Q('B2', """Equity shares with differential voting rights (DVR) can be issued up to what limit under the Companies (Share Capital and Debentures) Rules?""",
  "74% of total post-issue paid-up equity share capital", ["26% of total post-issue paid-up equity share capital",
   "50% of authorised capital", "10% of net worth"],
  "The 2019 amendment raised the DVR limit from 26% to 74% of total post-issue paid-up equity capital (including DVRs).")

Q('B2', """A public issue is 'over-subscribed' when:""",
  "Applications received exceed the number of shares offered", ["Applications received are less than the minimum subscription",
   "The issue price is above the face value of the shares", "The shares are listed at a premium on the first day"],
  "Over-subscription means demand exceeds the issue size; the company may reject some, allot fully to some, or allot pro-rata.")
