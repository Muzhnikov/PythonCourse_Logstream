class CardDeck:
    def __init__(self):
        self.card_suits = ["Черви", "Пики", "Бубны", "Крести"]
        self.card_value = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Валет", "Дама", "Король", "Туз"]
        self.deck = [f"{value} {suit}" for value in self.card_value for suit in self.card_suits]
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.deck):
            card = self.deck[self.counter]
            self.counter += 1
            return card
        raise StopIteration

card_deck = CardDeck()
for card in card_deck:
    print(card)
