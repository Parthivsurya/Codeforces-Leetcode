n, k = map(int, input().split())
 
if n >= k:
    scores = list(map(int, input().split()))
 
    threshold_score = scores[k - 1]
 
    advancing_count = 0
    for score in scores:
        if score >= threshold_score and score > 0:
            advancing_count += 1
    print(advancing_count)