from collections import defaultdict
from pprint import pprint

### frozenset版
fushi_fset1 = frozenset(["フシギダネ", "フシギソウ", "フシギバナ"])
fushi_fset2 = frozenset(["フシギバナ", "フシギソウ", "フシギダネ"])

dct_fset = defaultdict(int)
dct_fset[fushi_fset1] += 1
dct_fset[fushi_fset2] += 1
pprint(dct_fset)


### tuple版
fushi_tpl1 = tuple(["フシギダネ", "フシギソウ", "フシギバナ"])
fushi_tpl2 = tuple(["フシギバナ", "フシギソウ", "フシギダネ"])

dct_tpl = defaultdict(int)
dct_tpl[fushi_tpl1] += 1
dct_tpl[fushi_tpl2] += 1
pprint(dct_tpl)


### set版
fushi_set1  = set(["フシギダネ", "フシギソウ", "フシギバナ"])
fushi_set2  = set(["フシギバナ", "フシギソウ", "フシギダネ"])

dct_set = defaultdict(int)
dct_set[fushi_set1] += 1
dct_set[fushi_set2] += 1
pprint(dct_set)