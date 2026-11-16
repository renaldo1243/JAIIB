"""Shared helpers for the AFM question bank and notes."""
import random, re, json

NOTES = {}
QS = []
_count = {}

FIXED_PAT = re.compile(r'^(all of the above|none of the above|both|neither|all the above|all four|all three|all of these|none of these)', re.I)


def note(ch, html):
    NOTES[ch] = html.strip()


def Q(ch, stem, correct, wrongs, expl, fixed=False, src='Practice · exam-level (original)', pre='AF-X'):
    """correct = right option text; wrongs = list of 3 distractors.
    Options are shuffled per question (seeded by id) unless fixed=True or an option is
    an 'all/none/both' type, which then stays last."""
    assert len(wrongs) == 3, (ch, stem[:60])
    key = pre + ch
    _count[key] = _count.get(key, 0) + 1
    qid = f"{pre}-{ch}-{_count[key]:02d}"
    opts = [correct] + list(wrongs)
    if fixed:
        order = list(range(4))
    else:
        rnd = random.Random(qid)
        tail = [i for i, o in enumerate(opts) if FIXED_PAT.match(o.strip())]
        head = [i for i in range(4) if i not in tail]
        rnd.shuffle(head)
        order = head + tail
    o = [opts[i] for i in order]
    a = order.index(0)
    QS.append({"id": qid, "ch": ch, "s": stem.strip(), "o": o, "a": a, "w": expl.strip(), "src": src})
    return qid


def money(x, d=0):
    """Indian digit grouping, e.g. 1234567 -> 12,34,567"""
    neg = x < 0
    x = abs(x)
    s = f"{x:.{d}f}"
    if '.' in s:
        i, f = s.split('.')
    else:
        i, f = s, ''
    if len(i) > 3:
        head, tail = i[:-3], i[-3:]
        parts = []
        while len(head) > 2:
            parts.insert(0, head[-2:])
            head = head[:-2]
        if head:
            parts.insert(0, head)
        i = ','.join(parts + [tail])
    r = i + ('.' + f if f else '')
    return ('-' if neg else '') + r


def T(ch, stem, correct, wrongs, expl, fixed=False):
    """Trap-drill question: wrong options are the classic exam traps."""
    return Q(ch, stem, correct, wrongs, expl, fixed=fixed, src='Trap drill · exam trap (original)', pre='AF-G')
