"""May 2026 memory-based AFM paper (Oliveboard PDF) -> app questions, keys checked."""
import json, re, os
from qb import QS

D = json.load(open(os.path.join(os.path.dirname(__file__), 'may26_raw.json')))

CH = {1:'A4',2:'A9',3:'B3',4:'D3',5:'B3',6:'B5',7:'A4',8:'B2',9:'B3',10:'C4',11:'B3',12:'A8',13:'C6',14:'A7',15:'C1',
16:'A3',17:'B2',18:'C1',19:'B2',20:'A6',21:'A7',22:'C6',23:'D2',24:'B4',25:'C7',26:'B3',27:'C4',28:'D4',29:'C3',30:'B3',
31:'B5',32:'C2',33:'A1',34:'A2',35:'C8',36:'B3',37:'A2',38:'D1',39:'B4',40:'B4',41:'A1',42:'A1',43:'A1',44:'C2',45:'C2',
46:'B2',47:'A8',48:'C5',49:'A5',50:'A1',51:'D2',52:'C4',53:'C1',54:'D2',55:'D1',56:'A7',57:'A6',58:'D5',59:'A6',60:'B5',
61:'B1',62:'C4',63:'D4',64:'A5',65:'B2',66:'B2',67:'C5',68:'A4',69:'B1',70:'A3',71:'C3',72:'D1',73:'D4',74:'B2',75:'B3',
76:'B6',77:'D1',78:'A1',79:'A3',80:'C2',81:'C3',82:'B6',83:'B5',84:'C3',85:'C3',86:'C5',87:'A6',88:'D2',89:'D3',90:'C2',
91:'C4',92:'C3',93:'B3',94:'C3',95:'B2',96:'D3',97:'A1',98:'A6',99:'A6',100:'C4',101:'A6',102:'C3',103:'C6',104:'B4',
105:'D5',106:'A8',107:'A1',108:'A2',109:'A5',110:'C2',111:'A4',112:'B6',113:'A6',114:'A6',115:'A4',116:'C2',117:'D1',118:'C3'}

# Text fixes for garbled recall (exponents lost in the PDF)
STEM_FIX = {
 84: [('(Use 1.0G⁴ = 1.4116)', '(Use 1.09⁴ = 1.4116)')],
 92: [('(Use 1.0G⁶ = 1.6771)', '(Use 1.09⁶ = 1.6771)')],
 102: [('*(Given: 1.115=1.C8511.11\\^5 = 1.C8511.115=1.C851)*', '(Given: 1.11⁵ = 1.6851)')],
}

OPT_FIX = {25: ['Every project earning more than WACC should automatically be accepted regardless of risk.',
                'WACC is only one decision criterion; project-specific risk, cash-flow certainty and strategic considerations must also be evaluated.',
                'WACC is relevant only for debt-financed projects.',
                'Project A should always be rejected because its return is lower than Project B.']}

NOTE = {}
KEY = {}

# Q13: recalled figures give NO positive alpha (P 11 vs 12.4; Q 15 vs 15.6; R 17 vs 18.8). Adjust Q's return to 16%.
STEM_FIX.setdefault(13, []).append(('Q | 1.20 | 15%', 'Q | 1.20 | 16%'))
NOTE[13] = 'Recalled figures corrected: with Q at 15% no company has positive alpha, so Q is set to 16% (required 15.6%).'
# Q65: 1,80,000 applied, 20,000 rejected -> 1,60,000 get 1,20,000 = 3/4. 9,000 x 3/4 = 6,750 (the PDF key 9,000 is wrong).
OPT_FIX[65] = ['6,000 shares', '6,750 shares', '8,000 shares', '9,000 shares']
KEY[65] = 'B'
NOTE[65] = 'The coaching key (9,000) is wrong; options corrected so the right answer, 6,750, is present.'
# Q88: recalled stem had no clear question. Reframed to what it tests: where IGST applies.
STEM_FIX.setdefault(88, []).append(('Which combination correctly identifies the applicable GST treatment?',
                                    'In which of the above transactions is IGST levied?'))
OPT_FIX[88] = ['1 and 2 only', '3 and 4 only', '2 and 3 only', '2, 3 and 4 only']
KEY[88] = 'C'
NOTE[88] = 'Recalled question was incomplete; reframed to the point it tests (IGST = inter-State supply and imports).'

EX = {
 1: "The machine was debited to Purchases instead of Machinery: an error of principle. Purchases is overstated by ₹18 lakh, so profit is understated; Machinery is missing, so fixed assets are understated. Depreciation for Jan–Mar (₹18 lakh × 10% × 3/12 = ₹45,000) was also not charged, which partly offsets, but net profit is still understated by ₹17.55 lakh. Both debit and credit were made, so the Trial Balance agrees.",
 5: "Bonus shares only move reserves into share capital. Ownership % is unchanged (1) and total shareholders' funds stay the same while paid-up capital rises (3). More shares with the same profit lowers EPS (4). No cash comes in, so liquidity does not improve (2 is wrong).",
 6: "Unsecured portion (₹5 crore) of a doubtful asset needs 100% provision (1 correct). The secured portion also needs provision by age in doubtful category (D2, 1–3 years: 40%), so 'only secured' is wrong (2). Interest on NPAs is not taken to income on accrual; unrealised interest already credited is reversed (4 correct, 3 wrong).",
 13: "Required return (CAPM) = Rf + β(Rm − Rf) = 6 + β × 8. P: 12.4% vs 11% → alpha −1.4. Q: 15.6% vs 16% → alpha +0.4. R: 18.8% vs 17% → alpha −1.8. Only Q has positive alpha.",
 26: "Bonus issue capitalises free reserves (1) and leaves each holder's proportion unchanged (2). More shares in issue usually improves market liquidity (4). No cash is received (3 wrong).",
 28: "Fixed costs are already covered and capacity is idle, so only variable cost matters. Contribution per unit = 410 − 360 = ₹50 > 0, and existing sales are unaffected, so accept. Comparing with total cost is the trap.",
 29: "FV = 8,00,000 × 1.10⁵ = 8,00,000 × 1.61051 = 12,88,408 ≈ 12.88 lakh.",
 45: "Average inventory = (90 + 120)/2 = 105. Inventory turnover = COGS / average inventory = 840/105 = 8 times. A higher closing stock alone may mean slow-moving stock, not better management.",
 46: "Section 52 permits Securities Premium to be used for: fully paid bonus shares, writing off preliminary expenses, writing off expenses/commission/discount on issue of shares or debentures, premium on redemption of preference shares/debentures, and buy-back. It cannot be used to pay cash dividend.",
 51: "GST registration is tested on aggregate turnover (all-India, same PAN): taxable + exempt + export + inter-State supplies, excluding GST itself and inward supplies on reverse charge. Exempt supplies and sale of office furniture (a supply) count, so taxable turnover alone is the wrong test.",
 57: "Depreciable amount = cost incl. installation − residual = (48 + 2) − 5 = ₹45 lakh. Annual SLM = 45/9 = ₹5 lakh. After 3 years: 50 − 15 = ₹35 lakh.",
 65: "Valid applications = 1,80,000 − 20,000 = 1,60,000 for 1,20,000 shares → ratio 3 : 4. Mr Sharma gets 9,000 × 3/4 = 6,750 shares.",
 72: "Section 80C (overall ₹1.5 lakh) covers LIC premium, employee's PF contribution and tuition fees for up to two children. Medical insurance premium is under Section 80D; donations to approved funds under Section 80G.",
 84: "Compound: 8,00,000 × 1.09⁴ = 8,00,000 × 1.4116 = ₹11,29,280. Simple at 10%: 8,00,000 + 8,00,000 × 10% × 4 = ₹11,20,000. Compound is higher.",
 88: "Intra-State supply (Jaipur→Kota, service within Rajasthan) attracts CGST + SGST. Inter-State supply (Jaipur→Ahmedabad) and imports attract IGST. So IGST applies to 2 and 3.",
 92: "FV = 25 lakh × 1.09⁶ = 25 × 1.6771 = ₹41.93 lakh.",
 93: "Current tax is on taxable profit (1). Different depreciation methods create a timing (temporary) difference that reverses over the asset's life, so deferred tax is recognised (2). It is not a permanent difference (3 wrong) and does not depend on extra tax being payable now (4 wrong).",
 94: "EAR = (1 + r/m)^m − 1. Bank B: (1 + 0.117/12)¹² − 1 ≈ 12.35%, which is higher than Bank A's 12%. So Bank B is actually costlier, although its quoted rate is lower.",
 102: "FV = 18 lakh × 1.11⁵ = 18 × 1.6851 = ₹30.33 lakh, so the estimate is correct.",
 113: "A sinking fund sets aside fixed amounts each year and invests them, so the redemption burden is spread (1) and investment income adds to the fund (2); its purpose is to have cash ready at redemption (4). It does not remove the legal obligation to redeem (3 wrong).",
 117: "TCS is governed by the Income-tax Act and GST by the CGST/IGST Acts. Charging GST on an invoice does not remove an Income-tax TCS obligation; each is tested under its own law.",
 11: "Books use SLM over 10 years (₹12 lakh a year); tax uses WDV at 40% (₹48 lakh in year 1). Taxable profit is lower now and will be higher later when tax depreciation falls below book depreciation. This timing difference creates a deferred tax liability under AS 22 (₹36 lakh × 30% = ₹10.8 lakh at the end of year 1).",
 48: "Quotes are from the bank's side: the lower rate (83.25) is the bank's buying rate, the higher (83.33) its selling rate. An exporter sells foreign currency to the bank, so the bank's buying rate applies (TT buying for a clean inward remittance; bill buying if a bill is purchased). 'Buy low, sell high' always favours the bank.",
 81: "Bank B's lower EMI saves (99,640 − 98,890) × 60 = ₹45,000 over 5 years, but its ₹1,20,000 processing fee is paid upfront. The effective cost of borrowing (all-in cost / IRR of the cash flows) is what must be compared, not EMI alone.",
 99: "WDV at 20%: 25 × 0.8³ = ₹12.8 lakh after 3 years. SLM gives a lower book value only if life is short (e.g. life under about 6 years). For normal lives WDV writes off more in early years, so Machine B is likely to have the lower carrying amount.",
 74: "Forfeiture reduces paid-up capital (the forfeited amount is shown separately as Share Forfeiture until reissue). Issued capital is the nominal value of shares issued and authorised capital is the ceiling in the MoA; neither changes just because of forfeiture.",
}

NOTE[31] = 'RBI rule: interest-bearing staff loans (vehicle, housing) → Advances (Sch 9); non-interest-bearing ones (e.g. festival advance) → Other Assets (Sch 11).'
EX[31] = "Loans to staff are part of a bank's lending, so the interest-bearing ones (vehicle ₹9.5 lakh, housing ₹42 lakh) go under Advances (Schedule 9), as RBI's balance-sheet instructions require. Non-interest-bearing staff advances, such as a festival advance, are shown under Other Assets (Schedule 11). They are never fixed assets or adjusted against staff welfare expense."
LET = 'ABCD'
import random
TABLE_FIX = {81: "ABC Manufacturing Ltd. plans to purchase a CNC machine costing ₹48 lakh. Two banks offer the following loans:\nParticulars | Bank A | Bank B\nLoan Amount | ₹48 lakh | ₹48 lakh\nInterest Rate | 9.00% | 8.60%\nTenure | 5 Years | 5 Years\nEMI | ₹99,640 | ₹98,890\nProcessing Fee | Nil | ₹1,20,000\nThe Finance Manager recommends Bank B solely because its EMI is lower. The CFO disagrees.\nWhich financial principle should primarily guide the decision?"}
for o in D:
    n = o['n']
    title = o['title']
    stem = o['stem_nl']
    if stem.startswith(title):
        stem = stem[len(title):].strip()
    for t in ['Balance Sheet -- Classification of Accounts ', 'AS 10 -- Capital vs Revenue Expenditure ', 'Paid-up Capital ',
              'Rules of Debit and Credit (Integrated Journal Analysis) ', 'Standard Costing vs Marginal Costing ']:
        if stem.startswith(t):
            stem = stem[len(t):].strip()
    stem = TABLE_FIX.get(n, stem)
    for a, b in STEM_FIX.get(n, []):
        assert a in stem, (n, a)
        stem = stem.replace(a, b)
    stem = re.sub(r'(?<=[a-z,])\n(?=(Alternative|Bank B|Bond|Option))', ' ', stem)
    stem = re.sub(r'\s+(?=(The investment analyst|The analyst makes|The Head of Treasury|The CFO makes|The Accounts Executive makes))', '\n', stem)
    stem = stem.replace('2025--26', '2025-26').replace('2023--24','2023-24').replace('2024--25','2024-25').replace('--', '–').replace('*', '').strip()
    opts = OPT_FIX.get(n, o['opts'])
    assert len(opts) == 4, n
    key = KEY.get(n, o['key'])
    ex = EX.get(n) or o['ex']
    assert ex, n
    qid = f"AF-May26-Q{n}"
    rnd = random.Random(qid)
    order = list(range(4)); rnd.shuffle(order)
    q = {"id": qid, "ch": CH[n], "s": stem, "o": [opts[i] for i in order], "a": order.index(LET.index(key)), "w": ex,
         "src": "PYQ · May 2026 (recalled)"}
    if n in NOTE:
        q['note'] = NOTE[n]
    QS.append(q)
