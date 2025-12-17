salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

current_spend = spend
money_capital = 0

for month in range(months):
    needed = current_spend - salary
    if needed > 0:
        money_capital += needed

    current_spend *= (1 + increase)


money_capital = round(money_capital)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
