class DeckOfCards():
    deck = [None] * 36

    def __init__(self):
        x = 0
        for i in range(1, 4 + 1):
            for j in range(6, 14 + 1):
                self.deck[x] = Card(i, j)
                x += 1

    def get(self, i):
        try:
            answer = {
                11: "Валет",
                12: "Дама",
                13: "Король",
                14: "Туз",
            }[self.deck[i].Num]
        except:
            answer = str(self.deck[i].Num)
        answer += " "
        answer += {
            1: "червей",
            2: "бубей",
            3: "крестей",
            4: "пик",
        }[self.deck[i].Mastb]
        return answer


class Card():
    def __init__(self, i, j):
        self.Mastb = i
        self.Num = j


if __name__ == '__main__':
    deck = DeckOfCards()
    for i in range(36):
        print(deck.get(i))
