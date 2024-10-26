class Wallet:
    payment_system = "МИР"

    def __init__(self, name: str, currency: str):
        if currency not in ("RUB", "USD", "EUR", "AED"):
            raise ValueError("Доступны только следующие валюты: RUB, USD, EUR, AED")
        self._balance = 0
        self.name = name
        self.currency =  currency

    def top_up_balance(self, amount: float) -> None:
        if amount > 0:
            self._balance += amount
            print(f"{amount} {self.currency} добавлено на баланс.")
        else:
            print("Сумма пополнения должна быть положительной.")

    def pay(self, amount: float) -> None:
        if amount > self._balance:
            print("Недостаточно средств.")
        elif amount <= 0:
            print("Сумма списания должна быть положительной.")
        else:
            self._balance -= amount
            print(f"Оплата в рамзере {amount} {self.currency} успешно списана с Вашего баланса.")

    def show_info(self) -> str:
        info = f'Баланс кошелька "{self.name}" составляет {self._balance} {self.currency}.'
        print(info)
        return info

    def delete_account(self) -> None:
        self._balance = 0
        print(f'Кошелек "{self.name}" закрыт.')

class CryptoWallet(Wallet):
    def __init__(self, name: str, currency: str, coin: str):
        super().__init__(name, currency)
        if coin not in ("ETH", "BTC"):
            raise ValueError("Доступны только следующие коины: BTC, ETH")
        self.coin = coin

    def top_up_balance(self, amount: float) -> None:
        if amount > 0:
            self._balance += amount
            print(f"{amount} {self.coin} добавлено на баланс.")
        else:
            print("Сумма пополнения должна быть положительной.")

    def pay(self, amount: float) -> None:
        if amount > self._balance:
            print("Недостаточно средств.")
        elif amount <= 0:
            print("Сумма списания должна быть положительной.")
        else:
            self._balance -= amount
            print(f"Оплата в рамзере {amount} {self.coin} успешно списана с Вашего баланса.")

    def show_info(self) -> str:
        info = f'Баланс кошелька "{self.name}" составляет {self._balance} {self.coin}.'
        print(info)
        return info

    def show_usd_info(self) -> str:
        coin_rates = {"BTC": 72000, "ETH": 3500}
        total_dollars = self._balance * coin_rates[self.coin]
        info = f'Баланс кошелька "{self.name}" составляет {total_dollars} USD'
        print(info)
        return info

wallet = Wallet("Мой кошелек", "RUB")
wallet.top_up_balance(1000)
wallet.pay(500)
wallet.show_info()
wallet.delete_account()
print()

crypto_wallet = CryptoWallet("Мой крипто кошелек", "USD", "BTC")
crypto_wallet.top_up_balance(0.5)
crypto_wallet.pay(50)
crypto_wallet.pay(0.25)
crypto_wallet.show_info()
crypto_wallet.show_usd_info()
crypto_wallet.delete_account()
