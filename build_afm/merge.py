"""Build bank_afm.json + notes_afm.json for the prep app."""
import json, importlib, sys, os, re
from collections import Counter
sys.path.insert(0, os.path.dirname(__file__))
import qb

CHAPTERS = ['A1','A2','A3','A4','A5','A6','A7','A8','A9',
            'B1','B2','B3','B4','B5','B6',
            'C1','C2','C3','C4','C5','C6','C7','C8','C9','C10',
            'D1','D2','D3','D4','D5','D6']
built = []
for c in CHAPTERS:
    if os.path.exists(os.path.join(os.path.dirname(__file__), f'ch_{c}.py')):
        importlib.import_module(f'ch_{c}')
        built.append(c)
import pyq_may26  # adds PYQs

out_dir = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/JAIIB'
# keep only questions for chapters whose notes exist (release in batches)
bank = [q for q in qb.QS if q['ch'] in built]
ids = [q['id'] for q in bank]
assert len(ids) == len(set(ids)), 'duplicate ids'
for q in bank:
    assert len(q['o']) == 4 and 0 <= q['a'] < 4 and q['s'] and q['w'], q['id']
    assert len(set(q['o'])) == 4, ('duplicate options', q['id'])
    # explanations must not reference option letters
    assert not re.search(r'\b(option|Option) [A-D]\b|\(?[A-D]\) is', q['w']), ('letter ref', q['id'], q['w'][:80])
notes = {c: qb.NOTES[c] for c in built}
json.dump(bank, open(os.path.join(out_dir, 'bank_afm.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
json.dump(notes, open(os.path.join(out_dir, 'notes_afm.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
cnt = Counter(q['ch'] for q in bank)
print('chapters:', built)
print('questions:', len(bank), ' PYQ:', sum(1 for q in bank if q['id'].startswith('AF-May26')), ' practice:', sum(1 for q in bank if q['id'].startswith('AF-X')))
print(' '.join(f'{c}:{cnt[c]}' for c in built))
print('answer spread', Counter(q['a'] for q in bank))
