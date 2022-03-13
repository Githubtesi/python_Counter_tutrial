import random

from collections import Counter

obj_list = ['A', 'B', 'C', 'D', 'E']

# ランダムのリスト生成
random_list = random.choices(obj_list, k=5)

# 出現回数
counter = Counter(random_list)

# 出現回数
print(random_list.count('A'))
print(counter['A'])

# ソートして上位データ取得
top_3 = counter.most_common()[:3]
print(top_3)


