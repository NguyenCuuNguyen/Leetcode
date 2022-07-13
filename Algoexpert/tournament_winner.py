def tournamentWinner(competitions, results):
    # Write your code here.
    scores = {}
    winner = ""
    scores[winner] = 0
    #max = ""
    for i, r in enumerate(results):
        # if max == "": 
            # max = competitions[0][0]
        if r == 1: #home wins
            if competitions[i][0] not in scores:
                scores[competitions[i][0]] = 0
            scores[competitions[i][0]] += 3
            if scores[competitions[i][0]] > scores[winner]:
                winner = competitions[i][0]
        else:
            if competitions[i][1] not in scores:
                scores[competitions[i][1]] = 0
            scores[competitions[i][1]] += 3
            if scores[competitions[i][1]] > scores[winner]:
                winner = competitions[i][1]
    #Solution 1: Brute force
    # max =0
    # winner = ""
    # for w, s in scores.items():
    #     if s > max: 
    #         max = s
    #         winner = w

    #Solution 2: Built-in func
    # winner = max(scores, key=scores.get)

    #Solution 3: Built-in max() with key function
    # winner = max(scores, key=lambda x: scores[x])
    return winner

