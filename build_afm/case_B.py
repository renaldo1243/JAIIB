from qb import S

# ===================== B1 Final accounts =====================
S('B1', """Extracts of Vertex Traders for FY 2025-26 (₹ crore):
• Opening stock 1.80; Purchases 9.60; Purchase returns 0.40
• Wages 1.20; Carriage inward 0.30; Carriage outward 0.25
• Sales 15.00; Sales returns 0.50; Closing stock 2.10
The accountant reports gross profit of ₹3.85 crore. The auditor disagrees. What is the correct gross profit?""",
  "₹4.10 crore", ["₹3.85 crore", "₹4.60 crore", "₹3.70 crore"],
  "COGS = 1.80 + 9.60 − 0.40 + 1.20 + 0.30 − 2.10 = 10.40. Net sales = 14.50. GP = 4.10. The accountant's 3.85 wrongly includes carriage outward (a P&L selling expense).")

S('B1', """M/s Vertex Traders sent goods costing ₹32 lakh to a customer on approval on 28 March 2026, invoiced at ₹40 lakh and recorded as a sale. By 31 March the customer had neither approved nor rejected them. The Accounts Manager argues that since the goods left the warehouse they should not be in closing stock. Which treatment is correct?""",
  "Reverse the ₹40 lakh sale and include the goods in closing stock at ₹32 lakh, since risks and rewards have not passed",
  ["Keep the sale, because physical dispatch decides whether goods are inventory",
   "Reverse the sale and include the goods in closing stock at the invoice value of ₹40 lakh",
   "Keep the sale but create a provision of ₹8 lakh for unrealised profit"],
  "Goods on approval remain the seller's until approved (or the return period lapses). They are valued at cost or NRV, never at sale price.")

S('B1', """A partnership's net profit (before any partner items) is ₹6,00,000. Partner A has lent ₹5,00,000 to the firm at 6%. Interest on capital at 10%: A ₹20 lakh, B ₹10 lakh. B gets a salary of ₹60,000. Interest on drawings: A ₹6,000, B ₹4,000. The trainee debits interest on A's loan to the Appropriation Account. What is the correct divisible profit?""",
  "₹2,20,000", ["₹2,50,000", "₹2,00,000", "₹1,90,000"],
  "Interest on a partner's loan (₹30,000) is a charge in the P&L: profit = 5,70,000. Appropriation: less interest on capital 3,00,000 and salary 60,000, plus interest on drawings 10,000 = 2,20,000. Debiting the loan interest in appropriation gives the same arithmetic total, but it is a charge payable even if there is a loss, so it must go to P&L.")

S('B1', """Delta Manufacturing has at 31 March: debtors ₹8,00,000 (including a ₹20,000 debt now known to be bad); existing provision for doubtful debts ₹30,000; new provision to be 5% of good debtors; bad debts already in the TB ₹12,000. The accountant charges ₹71,000 to P&L. What is the correct charge, and the debtors' figure in the Balance Sheet?""",
  "₹41,000 charged; debtors shown at ₹7,41,000", ["₹71,000 charged; debtors shown at ₹7,41,000",
   "₹41,000 charged; debtors shown at ₹7,60,000", "₹32,000 charged; debtors shown at ₹7,80,000"],
  "New provision = 5% × 7,80,000 = 39,000. Charge = 12,000 + 20,000 + 39,000 − 30,000 = 41,000 (the accountant forgot to deduct the old provision). Debtors = 7,80,000 − 39,000 = 7,41,000.")

S('B1', """Consider the following year-end adjustments of a trader:
1. Rent ₹72,000 paid on 1 October for one year (year ends 31 March).
2. Commission of ₹15,000 received for April services.
3. Interest of ₹8,000 on investments due but not received.
4. Goods costing ₹10,000 taken by the proprietor, not recorded.
Which statement is correct?""",
  "Prepaid rent ₹36,000 and accrued interest ₹8,000 are assets; ₹15,000 is a liability; purchases fall and drawings rise by ₹10,000",
  ["Rent expense is ₹72,000 and commission income is ₹15,000 for the year",
   "Accrued interest is a liability and commission received in advance is an asset",
   "Goods taken by the proprietor increase sales by ₹10,000"],
  "Six months' rent (₹36,000) is prepaid; advance commission is unearned (liability); accrued interest is a receivable; goods for personal use reduce purchases and add to drawings.")

S('B1', """Which items appear on the debit side of the Trading Account of a manufacturer?
1. Royalty on production
2. Carriage outward
3. Factory power and fuel
4. Import duty on raw materials
5. Office salaries""",
  "1, 3 and 4 only", ["1, 2, 3 and 4 only", "2, 3 and 5 only", "3 and 4 only"],
  "Direct expenses of making or bringing goods (royalty on production, factory power, import duty) go to Trading. Carriage outward and office salaries are P&L items.")

S('B1', """Stock costing ₹40 lakh was destroyed by fire on 20 March; the insurer admitted ₹28 lakh, received in April. The accountant credits ₹28 lakh to Trading Account and ignores the rest "since the claim is not received yet". Which treatment is correct?""",
  "Credit Trading with ₹40 lakh; debit P&L with the ₹12 lakh uninsured loss; show ₹28 lakh as a claim receivable",
  ["The accountant's treatment is correct, as only admitted amounts are recorded",
   "Debit P&L with ₹40 lakh and record the claim only when cash is received",
   "Add ₹28 lakh to closing stock because the insurer will pay it"],
  "The whole cost of goods lost is removed from Trading; the admitted claim is an asset under accrual; the uninsured part is a loss.")

S('B1', """A proprietor's opening capital is ₹8 lakh. Net profit as per the draft P&L is ₹2.4 lakh BEFORE these adjustments:
• Interest on capital at 10% to be allowed
• Interest on drawings of ₹9,000 to be charged
• Goods costing ₹30,000 taken by the proprietor, not yet recorded
Cash drawings during the year were ₹1.5 lakh. The accountant reports closing capital of ₹9.70 lakh. What is the correct closing capital?""",
  "₹8.90 lakh", ["₹9.70 lakh", "₹8.51 lakh", "₹9.29 lakh"],
  "Adjusted profit = 2.40 − 0.80 + 0.09 + 0.30 (purchases reduced) = 1.99. Capital = 8.00 + 0.80 (interest on capital) + 1.99 − 1.50 − 0.30 (goods) − 0.09 (interest on drawings) = 8.90. Interest on capital, interest on drawings and goods taken each hit profit and capital equally, so they cancel: 8 + 2.4 − 1.5 = 8.90.")

S('B1', """A business's Trial Balance shows 'Adjusted Purchases' of ₹42 lakh and 'Closing Stock' of ₹6 lakh. The accountant also credits ₹6 lakh closing stock to the Trading Account. The effect is:""",
  "Gross profit is overstated by ₹6 lakh, because closing stock is already deducted in adjusted purchases",
  ["The treatment is correct, because closing stock always goes to the Trading Account",
   "Gross profit is understated by ₹6 lakh",
   "Only the Balance Sheet is overstated; profit is unaffected"],
  "When closing stock appears inside the TB (via adjusted purchases), it goes only to the Balance Sheet; crediting Trading again double-counts it.")

S('B1', """GP is 20% on cost. Sales ₹30 lakh; opening stock ₹4 lakh; purchases ₹26 lakh. The accountant computes closing stock as ₹6 lakh. What is the correct closing stock?""",
  "₹5 lakh", ["₹6 lakh", "₹4 lakh", "₹7 lakh"],
  "20% on cost = 1/6 of sales: GP = 5, COGS = 25. Closing stock = 4 + 26 − 25 = 5. Taking 20% of sales (GP 6, COGS 24) gives 6 lakh, which is the trap.")

S('B1', """A firm's cash book shows opening cash ₹50,000; receipts from sales ₹2,50,000; cash expenses ₹1,80,000; cash drawings ₹40,000; deposit into bank ₹1,00,000. The accountant reports closing cash of ₹80,000. Which is correct?""",
  "The figure is impossible: cash would be −₹20,000, so some receipt or payment is wrongly recorded",
  ["₹80,000 is correct", "Closing cash is ₹1,80,000", "Closing cash is −₹20,000, shown as a liability"],
  "50,000 + 2,50,000 − 1,80,000 − 40,000 − 1,00,000 = −20,000. A cash account can never have a credit balance, so an error exists.")

S('B1', """Which items are NOT debited to the Profit & Loss Appropriation Account of a partnership?
1. Interest on partners' capital
2. Rent paid to a partner for the firm's premises
3. Commission to a working partner
4. Interest on a partner's loan
5. Transfer to General Reserve""",
  "2 and 4 only", ["4 only", "2, 3 and 4 only", "1 and 5 only"],
  "Rent to a partner and interest on a partner's loan are charges against profit (P&L). Interest on capital, commission and transfer to reserve are appropriations.")

# ===================== B2 Companies & share capital =====================
S('B2', """Galaxy Ltd. offered 1,50,000 shares. Applications were received for 2,40,000; applications for 40,000 shares were rejected and money refunded; the rest got pro-rata allotment. Mr Sharma applied for 6,000 shares, paying ₹3 per share on application; ₹5 is due on allotment. How many shares does he get and how much does he pay on allotment?""",
  "4,500 shares; ₹18,000 on allotment", ["3,750 shares; ₹18,750 on allotment",
   "4,500 shares; ₹22,500 on allotment", "6,000 shares; ₹30,000 on allotment"],
  "Accepted applications 2,00,000 for 1,50,000 → 3:4. 6,000 × 3/4 = 4,500. Application money paid 18,000; needed 13,500; excess 4,500 adjusted. Allotment due 4,500 × 5 = 22,500 − 4,500 = ₹18,000.")

S('B2', """2,000 shares of ₹10 each were issued at a premium of ₹3. Application ₹2; allotment ₹5 (including the ₹3 premium); first call ₹3; final call ₹3. A shareholder paid application and allotment but not the first call; the shares were forfeited after the first call. Which entry is correct?""",
  "Share Capital Dr ₹14,000; To First Call ₹6,000; To Share Forfeiture ₹8,000",
  ["Share Capital Dr ₹14,000; Securities Premium Dr ₹6,000; To First Call ₹6,000; To Share Forfeiture ₹14,000",
   "Share Capital Dr ₹20,000; To First Call ₹6,000; To Share Forfeiture ₹14,000",
   "Share Capital Dr ₹8,000; To Share Forfeiture ₹8,000"],
  "Called-up capital = 2 + 2 + 3 = ₹7 per share → 14,000. The premium was received with allotment, so Securities Premium is untouched. Capital received = (2 + 2) × 2,000 = 8,000 → forfeiture.")

S('B2', """Those 2,000 forfeited shares (Share Forfeiture balance ₹8,000) are reissued as fully paid at ₹8 per share. The accountant transfers ₹8,000 to Capital Reserve. What is correct?""",
  "Use ₹4,000 to cover the discount on reissue; transfer the balance ₹4,000 to Capital Reserve",
  ["Transfer ₹8,000 to Capital Reserve, as proposed", "Transfer nil to Capital Reserve, as the shares were reissued at a discount",
   "Transfer ₹6,000 to Capital Reserve"],
  "Reissue as fully paid ₹10 for ₹8: discount ₹2 × 2,000 = 4,000, met from forfeiture. The remaining forfeiture on reissued shares (₹4,000) is a capital profit.")

S('B2', """Zenith Industries proposes to use its Securities Premium of ₹18 crore for:
1. Writing off preliminary expenses of ₹40 lakh.
2. Paying an interim cash dividend of ₹5 crore.
3. Issuing fully paid bonus shares of ₹10 crore.
4. Writing off underwriting commission of ₹1 crore on a share issue.
5. Buy-back of shares worth ₹2 crore.
Which uses are permitted under the Companies Act, 2013?""",
  "1, 3, 4 and 5 only", ["1, 2, 3, 4 and 5", "1, 3 and 4 only", "3 and 5 only"],
  "Sec 52 permits bonus issue, preliminary expenses, issue expenses/commission/discount, premium on redemption, and buy-back (Sec 68). Cash dividend is not permitted.")

S('B2', """Delta Infrastructure has 9% cumulative preference capital of ₹20 crore. No dividend was paid in FY 2023-24 and FY 2024-25. In FY 2025-26 profits are adequate. The directors make these statements:
1. Arrears of ₹3.6 crore must be paid before any equity dividend.
2. Preference holders have become entitled to vote on all resolutions.
3. Preference shares have automatically converted into equity.
4. Arrears were shown as a contingent liability in the notes of earlier years.
Which are correct?""",
  "1, 2 and 4 only", ["1 and 3 only", "1, 2, 3 and 4", "2 and 4 only"],
  "Two years' arrears at 9% on 20 crore = 3.6 crore, paid before equity dividend. Dividend unpaid for two years gives voting rights on all resolutions. Arrears are disclosed as a contingent liability. There is no automatic conversion.")

S('B2', """InnovateX Ltd. wants to issue shares to its Chief Scientist at a 20% discount to market price in exchange for a patented process, and separately issue shares to the public at a 10% discount to face value. Which statement is correct?""",
  "The first is a sweat equity issue permitted under Section 54; the issue to the public at a discount to face value is void under Section 53",
  ["Both are permitted with a special resolution", "Both are void because no shares can be issued at a discount",
   "The public issue is permitted with SEBI approval, but sweat equity is not"],
  "Sec 53 bars issue of shares at a discount to face value except sweat equity under Sec 54 (for know-how or IPR, to employees or directors).")

S('B2', """Consider these statements about Galaxy Ltd. (authorised capital ₹20 crore; issued 1.5 crore shares of ₹10; calls unpaid on 2 lakh shares; 1 lakh shares forfeited, not reissued):
1. Issued capital can exceed authorised capital with Board approval.
2. Calls in arrears reduce paid-up capital.
3. Forfeited shares reduce paid-up capital, and the amount received on them is shown as Share Forfeiture.
4. Authorised capital falls when shares are forfeited.
Which are correct?""",
  "2 and 3 only", ["1, 2 and 3 only", "2, 3 and 4 only", "3 only"],
  "Issued capital can't exceed authorised capital (the MoA ceiling) without altering the MoA; forfeiture doesn't change authorised capital.")

S('B2', """Five professionals compare structures. A private company is proposed with 220 members, free transferability of shares and an invitation to the public to subscribe to debentures. Which statement is correct?""",
  "It cannot be a private company: a private company restricts transfer, limits members to 200 and cannot invite the public",
  ["It can be a private company because debentures are not shares", "It can be a private company if it has at least 2 directors",
   "It is a One Person Company because only five professionals promote it"],
  "Sec 2(68): restrictions on transfer, maximum 200 members (excluding employee-members) and no public invitation to subscribe for securities.")

S('B2', """Which statement on preference shares under the Companies Act, 2013 is NOT correct?""",
  "A company may issue preference shares redeemable after 25 years for any business",
  ["Irredeemable preference shares cannot be issued", "Infrastructure companies may issue preference shares up to 30 years, with annual partial redemption from the 21st year",
   "Redemption can be out of profits or out of a fresh issue of shares"],
  "Ordinary tenure is capped at 20 years; only infrastructure projects get up to 30 years (with 10% redemption from year 21).")

S('B2', """Food Corporation of India, Coal India Ltd. and a company in which a State Government holds 26% are being classified. Which is correct?""",
  "FCI is a statutory corporation; Coal India is a Government company; the third is neither (Government holding below 51%)",
  ["All three are Government companies", "FCI and Coal India are statutory corporations; the third is a Government company",
   "FCI is a Government company; Coal India is a statutory corporation"],
  "Statutory corporations are created by special Acts (FCI under the Food Corporations Act 1964). A Government company needs at least 51% Government holding (Sec 2(45)).")

S('B2', """A company issues 1 lakh shares of ₹10 at par. The holder of 1,000 shares paid ₹3 (application) and ₹4 (allotment) but not the final call of ₹3. The accountant debits Share Capital with ₹7,000 on forfeiture. The auditor objects. Why?""",
  "Share Capital must be debited with the called-up amount of ₹10,000; ₹3,000 goes to Calls in Arrears and ₹7,000 to Share Forfeiture",
  ["Share Capital should be debited with only ₹3,000, the unpaid amount",
   "Securities Premium must also be debited because the call is unpaid",
   "No entry is needed until the shares are reissued"],
  "On forfeiture the whole called-up amount is cancelled; the received part is credited to forfeiture and the unpaid part to calls.")

# ===================== B3 Schedule III, EPS, deferred tax =====================
S('B3', """Sun Pharma Ltd.: PAT ₹90 lakh; preference dividend ₹10 lakh; 40 lakh equity shares at the start; 10 lakh fresh shares issued at full market price on 1 July. The CFO computes EPS as ₹1.60 using year-end shares. What is the correct basic EPS?""",
  "₹1.68", ["₹1.60", "₹2.00", "₹1.80"],
  "Weighted shares = 40 + 10 × 9/12 = 47.5 lakh. Earnings for equity = 90 − 10 = 80 lakh. EPS = 80/47.5 = ₹1.68. Using year-end shares (50 lakh) ignores weighting.")

S('B3', """If, instead, the 10 lakh shares were BONUS shares issued on 1 July, what would basic EPS be (PAT ₹90 lakh; preference dividend ₹10 lakh; 40 lakh shares before)?""",
  "₹1.60", ["₹1.68", "₹2.00", "₹1.80"],
  "Bonus shares bring in no resources, so they are treated as outstanding from the start of the period: 50 lakh shares → 80/50 = ₹1.60 (and last year's EPS is restated).")

S('B3', """Kaveri Ltd.'s book profit is ₹200 crore. Differences: tax depreciation exceeds book depreciation by ₹30 crore; bonus of ₹10 crore provided but allowable only on payment next year; a penalty of ₹5 crore is disallowed. Tax rate 25%. What is the total tax expense in the P&L?""",
  "₹51.25 crore", ["₹46.25 crore", "₹50.00 crore", "₹56.25 crore"],
  "Taxable = 200 − 30 + 10 + 5 = 185 → current tax 46.25. DTL on 30 = 7.5; DTA on 10 = 2.5. Penalty is a permanent difference (no deferred tax). Total = 46.25 + 7.5 − 2.5 = 51.25.")

S('B3', """Omega Ltd. follows SLM in its books and WDV for tax. The accounts executive says:
1. Current tax should be based on taxable profit.
2. Deferred tax arises because depreciation differences reverse over time.
3. Deferred tax is a permanent difference.
4. Deferred tax is recognised only if additional tax is payable this year.
Which are correct?""",
  "1 and 2 only", ["2, 3 and 4 only", "1, 3 and 4 only", "1, 2, 3 and 4"],
  "Deferred tax arises only on timing differences; it doesn't depend on whether tax is payable now.")

S('B3', """Sigma Ltd. issues bonus shares 1 : 1 out of general reserve. Analysts say: (1) debt-equity worsens; (2) EPS halves if profits are unchanged; (3) book value per share halves; (4) each holder's percentage ownership falls; (5) the share price is likely to adjust downwards. Which are correct?""",
  "2, 3 and 5 only", ["1, 2 and 3 only", "2, 3, 4 and 5", "1, 4 and 5 only"],
  "Net worth is unchanged, so D/E is unchanged and ownership % is unchanged. Doubling the share count halves EPS and book value per share, and the market price adjusts.")

S('B3', """A company issues rights 1 for 3 at ₹120 when the market price is ₹200. Mr A holds 3,000 shares and lets his rights lapse without selling them. What is his approximate economic loss?""",
  "₹60,000", ["₹80,000", "₹2,40,000", "Nil, as he still holds 3,000 shares"],
  "TERP = (3 × 200 + 120)/4 = 180. His 3,000 shares fall from ₹200 to ₹180: loss ₹60,000. The value of his 1,000 rights (₹60 each) was lost by not exercising or renouncing them.")

S('B3', """TechNova grants 2,00,000 ESOPs vesting in 4 years; fair value per option at grant ₹60. The HR head says no expense arises until exercise. What expense is recognised in Year 1 (assuming all options are expected to vest)?""",
  "₹30 lakh, credited to Employee Stock Options Outstanding in equity", ["Nil, until the options are exercised",
   "₹1.20 crore in Year 1, as all options were granted in that year", "₹30 lakh, credited to a provision under liabilities"],
  "Total fair value = 2,00,000 × 60 = 1.2 crore, spread over the 4-year vesting period = 30 lakh a year; the credit is to equity.")

S('B3', """Nova Industries' draft Schedule III balance sheet shows:
1. Current maturities of long-term debt under non-current liabilities.
2. A security deposit recoverable after 4 years under current assets.
3. Trade receivables without an ageing schedule.
4. Deferred tax liability (net) under non-current liabilities.
Which items are WRONGLY presented?""",
  "1, 2 and 3 only", ["1 and 2 only", "All four", "2 and 4 only"],
  "Current maturities go to short-term borrowings; deposits recoverable after 12 months are non-current; receivables need ageing. DTL (net) is correctly a non-current liability.")

S('B3', """Which reserves can Bharat Ltd. legally use for (a) dividend and (b) fully paid bonus shares?
Reserves: General Reserve, Revaluation Reserve, Securities Premium, Capital Redemption Reserve.""",
  "(a) General Reserve only; (b) General Reserve, Securities Premium and CRR",
  ["(a) General Reserve and Securities Premium; (b) all four", "(a) All four; (b) General Reserve only",
   "(a) General Reserve and Revaluation Reserve; (b) Securities Premium and CRR"],
  "Dividend: profits or free reserves only. Bonus: free reserves, securities premium and CRR; never revaluation reserve.")

S('B3', """ABC Technologies converted ₹20 crore of debentures into 20 lakh shares on 1 October. The CFO says diluted EPS will equal basic EPS because conversion happened within the year. How should the auditor respond?""",
  "Incorrect: diluted EPS treats the debentures as converted from the start of the year, adjusting both post-tax interest and weighted shares",
  ["Correct: instruments converted during the year are ignored for diluted EPS",
   "Correct: interest saving is considered only for conversions at year-end",
   "Incorrect: only the number of shares changes; earnings are never adjusted"],
  "Potential equity shares outstanding for part of the year are included in diluted EPS from the start of the year (or issue date); earnings add back the post-tax interest for that period.")

# ===================== B4 Cash flow =====================
S('B4', """Delta Ltd. (a manufacturer) reports: NPBT ₹48 crore; depreciation ₹6 crore; amortisation ₹1 crore; loss on sale of machinery ₹1.5 crore; interest expense ₹4 crore; dividend received ₹2 crore; inventory decreased ₹3 crore; debtors increased ₹5 crore; creditors decreased ₹2 crore; income tax paid ₹12 crore. Net cash from operating activities is:""",
  "₹42.5 crore", ["₹54.5 crore", "₹46.5 crore", "₹38.5 crore"],
  "48 + 6 + 1 + 1.5 + 4 (interest is financing) − 2 (dividend is investing) + 3 − 5 − 2 = 54.5 cash generated; − 12 tax = 42.5.")

S('B4', """A trainee classifies these flows of a manufacturing company as operating:
1. Interest paid on term loans
2. Sale of old machinery
3. Dividend received on investments
4. Proceeds from issue of shares
5. Income tax paid on business profits
Which are actually operating activities under AS 3?""",
  "5 only", ["1, 3 and 5 only", "1 and 5 only", "All five"],
  "For a non-financial enterprise: interest paid → financing; sale of machinery and dividend received → investing; share issue → financing; income tax → operating (unless specifically identifiable otherwise).")

S('B4', """For the same five items, which classification would change if the entity were a commercial bank?""",
  "Interest paid and dividend received would become operating activities", ["Sale of machinery would become operating",
   "Issue of shares would become operating", "Nothing would change"],
  "For financial enterprises, interest paid, interest received and dividends received are operating, since lending and borrowing are their main business.")

S('B4', """During the year Bharat Ltd.: bought land worth ₹10 crore by issuing shares to the seller; converted ₹5 crore debentures into equity; issued bonus shares of ₹2 crore; bought machinery for ₹3 crore cash. How much appears as cash outflow under investing activities?""",
  "₹3 crore", ["₹13 crore", "₹18 crore", "₹20 crore"],
  "Non-cash transactions (land for shares, conversion, bonus) are excluded from the statement and disclosed separately. Only the cash purchase of machinery is an outflow.")

S('B4', """A company reports net profit of ₹50 crore but negative operating cash flow of ₹10 crore for the third year running, with receivables doubling. A credit officer's best conclusion is:""",
  "Profits may not be converting into cash (e.g. aggressive credit sales); repayment capacity needs deeper scrutiny",
  ["Profit is what matters for repayment, so the cash flow can be ignored",
   "Negative operating cash flow is normal for every profitable company",
   "Depreciation must have been charged twice"],
  "Persistent negative operating cash flow with rising receivables is a classic warning sign.")

S('B4', """Which of the following are cash equivalents for a company preparing a cash flow statement on 31 March 2026?
1. Treasury bills bought on 15 February 2026 maturing 15 May 2026.
2. Fixed deposit made on 1 April 2025 maturing 31 March 2027.
3. Listed equity shares held for trading.
4. Bank overdraft repayable on demand that fluctuates between positive and negative balances.""",
  "1 and 4 only", ["1, 2 and 3 only", "1 and 3 only", "2 and 4 only"],
  "Cash equivalents mature within about 3 months of acquisition (T-bills qualify). Long FDs and equity shares don't. A demand overdraft that is part of cash management can be included.")

S('B4', """A company sold a machine (book value ₹8 lakh) for ₹11 lakh. Under the indirect method, the accountant adds ₹11 lakh to net profit in operating activities. Which is correct?""",
  "Deduct ₹3 lakh profit from operating activities and show ₹11 lakh as an investing inflow",
  ["Add ₹11 lakh to operating activities", "Add ₹3 lakh to operating activities and ₹8 lakh to investing",
   "Show ₹11 lakh under financing activities"],
  "The profit is non-operating, so it is removed from net profit; the whole sale proceeds are an investing inflow.")

S('B4', """In the indirect method, a trainee: (i) deducts depreciation; (ii) adds an increase in trade receivables; (iii) adds an increase in trade payables; (iv) adds back provision for gratuity created but not paid. Which treatments are correct?""",
  "(iii) and (iv) only", ["(i) and (ii) only", "(ii), (iii) and (iv) only", "All four"],
  "Depreciation and non-cash provisions are added back; an increase in receivables is deducted; an increase in payables is added.")

# ===================== B5 Bank final accounts =====================
S('B5', """A term loan of ₹50 lakh became NPA on 1 April 2023. On 31 March 2026, the realisable value of security is ₹30 lakh. The branch proposes a provision of 15% of the outstanding. What provision is required?""",
  "₹32 lakh: 40% on the secured ₹30 lakh (D2) plus 100% on the unsecured ₹20 lakh", ["₹7.5 lakh: 15% as a sub-standard asset",
   "₹50 lakh: 100% since it is NPA for three years", "₹27.5 lakh: 25% on the secured portion plus 100% on the unsecured portion"],
  "Sub-standard for the first 12 months (to 31-3-2024), then doubtful; on 31-3-2026 it has been doubtful for 2 years → D2: 40% of secured + 100% of unsecured = 12 + 20 = 32 lakh.")

S('B5', """A bank's draft balance sheet shows:
1. Bills purchased and discounted under Investments.
2. Housing loans to staff (interest-bearing) under Other Assets.
3. Letters of credit opened for customers under Other Liabilities.
4. Refinance from NABARD deducted from agricultural advances.
How many items are correctly classified?""",
  "None", ["One", "Two", "All four"],
  "Bills purchased/discounted → Advances; interest-bearing staff loans → Advances; LCs → Contingent Liabilities; refinance → Borrowings with advances shown gross.")

S('B5', """From the following, compute the bank's 'Interest Earned' (Schedule 13): interest on advances ₹840 crore; discount on bills ₹60 crore; income on investments ₹410 crore; interest on balances with RBI ₹15 crore; commission on LCs and guarantees ₹45 crore; profit on sale of investments ₹30 crore.""",
  "₹1,325 crore", ["₹1,400 crore", "₹1,370 crore", "₹1,250 crore"],
  "Interest earned = 840 + 60 + 410 + 15 = 1,325. Commission and profit on sale of investments go to Other Income (Schedule 14).")

S('B5', """A loan account turned NPA on 31 December. Interest of ₹3 lakh for Oct–Dec had been credited to income but not realised; interest for Jan–Mar would be ₹3.2 lakh. The branch keeps the ₹3 lakh and accrues ₹3.2 lakh, arguing security is ample. Which is correct?""",
  "Reverse the unrealised ₹3 lakh and do not accrue the ₹3.2 lakh; recognise interest only when realised",
  ["Keep both, since the account is fully secured", "Keep the ₹3 lakh but stop accrual from January",
   "Reverse the ₹3 lakh but accrue the ₹3.2 lakh"],
  "Income recognition norms: no accrual on NPAs, and unrealised income booked earlier is reversed, regardless of security.")

S('B5', """Consider these statements about bank accounts:
1. The BR Act requires transfer of at least 20% of profit to the Statutory Reserve; RBI requires scheduled commercial banks to transfer 25%.
2. Bills for collection are shown as contingent liabilities.
3. Non-banking assets acquired in satisfaction of claims are shown under Other Assets.
4. Schedule 18 contains notes to accounts, including Basel III capital disclosures.
Which are correct?""",
  "1, 3 and 4 only", ["1, 2, 3 and 4", "2 and 3 only", "1 and 4 only"],
  "Bills for collection are shown below the balance sheet as a memorandum item; the bank is only an agent (2 wrong).")

S('B5', """A borrower with a cash-credit limit of ₹2 crore has an outstanding of ₹2.3 crore continuously for 95 days, with drawing power of ₹1.8 crore. Interest has been fully serviced. The branch manager says it is standard because interest is paid. Which is correct?""",
  "It is an NPA, since the account has stayed out of order (outstanding above limit/drawing power) for more than 90 days",
  ["It is standard, as interest is regularly serviced", "It becomes NPA only after 180 days of being out of order",
   "It is a special mention account (SMA-2) and not an NPA"],
  "A CC/OD account is 'out of order' if the outstanding stays above the sanctioned limit or drawing power continuously for 90 days; such an account is NPA even if interest is paid.")

S('B5', """A bank's loan of ₹10 crore is classified sub-standard; it is unsecured from the outset (no security). The provision required is:""",
  "25%, i.e. ₹2.5 crore", ["15%, i.e. ₹1.5 crore", "100%, i.e. ₹10 crore", "0.40%, i.e. ₹4 lakh"],
  "Sub-standard assets carry 15%; unsecured exposures classified sub-standard carry an additional 10%, i.e. 25% in total.")

S('B5', """Which item does a bank show under 'Balances with banks and money at call and short notice' (Schedule 7)?""",
  "Funds lent in the inter-bank call money market", ["Cash reserve maintained with RBI", "Treasury bills held as investments",
   "Bills purchased from customers"],
  "Call money lent and balances with other banks go to Schedule 7; CRR balance with RBI is in Schedule 6; T-bills in Schedule 8; bills purchased in Schedule 9.")

S('B5', """A bank's operating expenses schedule lists: payments to employees, rent and lighting, depreciation, directors' fees and 'provision for NPAs'. The auditor objects to one item. Which one and why?""",
  "Provision for NPAs, which is shown under 'Provisions and contingencies', not under operating expenses",
  ["Depreciation, which is shown under Other Liabilities", "Directors' fees, which are shown under Interest expended",
   "Rent and lighting, which is shown under Other Income as net rent"],
  "NPA provisions, investment depreciation and tax are 'provisions and contingencies'; Schedule 16 covers operating costs.")

S('B5', """In a bank's balance sheet, which of these is a contingent liability?
1. Guarantees given on behalf of constituents.
2. Liability on account of outstanding forward exchange contracts.
3. Interest accrued on deposits.
4. Claims against the bank not acknowledged as debts.""",
  "1, 2 and 4 only", ["1, 2, 3 and 4", "1 and 3 only", "3 and 4 only"],
  "Interest accrued on deposits is an actual liability (Other Liabilities, Schedule 5).")

# ===================== B6 Computerised accounting & CBS =====================
S('B6', """After moving to computerised accounting, the CFO of Kaveri Ltd. claims: "Our Trial Balance always tallies now, so our accounts are error-free." Which response is correct?""",
  "Software prevents arithmetical and posting errors, but wrong entries and errors of principle still flow into the accounts",
  ["Correct: computerised accounting eliminates all types of errors", "Incorrect: computerised accounting cannot follow double entry",
   "Correct: an audit is no longer needed once accounts are computerised"],
  "'Garbage in, garbage out': data-entry mistakes and wrong classifications are not detected by the trial balance.")

S('B6', """A fintech markets a 'Neo Bank' app offering instant accounts, virtual cards and expense analytics to a large company. The CFO asks whether the platform can itself accept deposits, lend and maintain CRR/SLR. Which answer is correct?""",
  "No; Indian neo banks run digital front-ends for licensed partner banks, which hold deposits and perform regulated functions",
  ["Yes; neo banks receive a banking licence automatically after three years", "Yes; neo banks function exactly like scheduled commercial banks",
   "No; but they may issue their own digital currency instead"],
  "Neo banks in India do not hold banking licences; the partner bank remains responsible to RBI.")

S('B6', """A power station uses a device that continuously measures voltage, temperature and pressure and shows readings as continuously varying signals. A trainee calls it digital "because it shows numbers". Which classification is correct?""",
  "Analog computer", ["Digital computer", "Hybrid computer", "Supercomputer"],
  "Analog machines work on continuously varying physical quantities; digital ones on discrete binary data.")

S('B6', """A bank posts every ATM withdrawal to the customer's account instantly but runs interest application for all savings accounts once a quarter. Which statement is correct?""",
  "ATM postings use online real-time processing; quarterly interest is batch processing",
  ["Both are batch processing", "Both are online real-time processing", "ATM postings are batch; interest is real-time"],
  "Real-time updates each transaction at once; batch collects transactions and processes them together.")

S('B6', """Under a bank's CBS, a teller both enters and authorises a ₹9 lakh cash withdrawal because the officer is busy. The auditor objects mainly on which ground?""",
  "It breaches maker–checker dual control, a key information-security and fraud control",
  ["CBS does not allow cash withdrawals above ₹5 lakh", "Only the branch manager can enter cash transactions",
   "The withdrawal should have been processed as a batch at day-end"],
  "Segregation (one enters, another verifies) protects integrity and prevents unauthorised transactions.")

S('B6', """Consider these statements about Core Banking Solutions:
1. All branches access a centralised database at the data centre, enabling anywhere banking.
2. A disaster recovery site is maintained for business continuity.
3. Each branch maintains its own separate customer database linked directly to every other branch.
4. Confidentiality, integrity and availability are the core security objectives.
Which are correct?""",
  "1, 2 and 4 only", ["1, 2, 3 and 4", "3 and 4 only", "1 and 3 only"],
  "Under CBS, branch servers connect to the central server; branches don't keep separate databases linked to each other.")

S('B6', """Which is NOT a disadvantage or risk of computerised accounting?""",
  "Automatic preparation of ledgers and statements from entered data", ["Dependence on power, hardware and software",
   "Risk of data loss without regular backups", "Exposure to unauthorised access and cyber attacks"],
  "Automatic posting and reporting is the main advantage; the others are risks needing controls.")
