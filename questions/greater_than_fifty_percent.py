import pprint


values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = sum(values)
threshold = total / 2

values.sort(reverse=True)

results = []
for i in range(len(values)):
    for k in range(i, len(values)):
        if sum(values[i:k]) >= threshold:
            results.append(['total: %s' % sum(values[i:k]), values[i:k]])

print('total: %s\n50%%: %s\n' % (total, threshold))
pprint.pprint(results)