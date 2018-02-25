from collections import defaultdict

user_ids_by_interest = defaultdict(list)
user_ids_by_interest[0].append(1)
print user_ids_by_interest.items()