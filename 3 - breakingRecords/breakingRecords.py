# Exercício -> https://www.hackerrank.com/challenges/breaking-best-and-worst-record/


# Scores = Vetor das Pontuações Por Jogo

scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]


def breakingRecords(scores):
    countMin = 0
    countMax = 0
    scoreMax = scores[0]
    scoreMin = scores[0]

    for value in scores[1:]:
        if value > scoreMax:
            scoreMax = value
            countMax += 1
        elif value < scoreMin:
            scoreMin = value
            countMin +=1
    return countMax,countMin

if __name__ == '__main__':
    print(breakingRecords(scores))