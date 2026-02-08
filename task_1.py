from abc import ABC, abstractmethod
from typing import Any
import doctest


class Device(ABC):
    """
    Абстрактный класс, описывающий электронное устройство.

    :param name: Название устройства
    :param power: Потребляемая мощность в ваттах

    >>> phone = Smartphone("Phone", 15, "Android")
    >>> phone.name
    'Phone'
    >>> phone.power
    15
    """

    def __init__(self, name: str, power: int) -> None:
        if not name:
            raise ValueError("Name must not be empty")
        if power <= 0:
            raise ValueError("Power must be positive")

        self.name: str = name
        self.power: int = power

    @abstractmethod
    def turn_on(self) -> None:
        """Включить устройство"""
        ...

    @abstractmethod
    def turn_off(self) -> None:
        """Выключить устройство"""
        ...


class Vehicle(ABC):
    """
    Абстрактный класс, описывающий транспортное средство.

    :param brand: Производитель
    :param max_speed: Максимальная скорость (км/ч)

    >>> car = Car("Tesla", 250, 4)
    >>> car.max_speed
    250
    """

    def __init__(self, brand: str, max_speed: int) -> None:
        if max_speed <= 0:
            raise ValueError("Max speed must be positive")

        self.brand: str = brand
        self.max_speed: int = max_speed

    @abstractmethod
    def move(self) -> None:
        """Начать движение"""
        ...

    @abstractmethod
    def stop(self) -> None:
        """Остановиться"""
        ...


class Account(ABC):
    """
    Абстрактный класс, описывающий пользовательский аккаунт.

    :param username: Имя пользователя
    :param balance: Баланс аккаунта

    >>> acc = BankAccount("user1", 1000.0)
    >>> acc.balance
    1000.0
    """

    def __init__(self, username: str, balance: float) -> None:
        if balance < 0:
            raise ValueError("Balance cannot be negative")

        self.username: str = username
        self.balance: float = balance

    @abstractmethod
    def deposit(self, amount: float) -> None:
        """Пополнить баланс"""
        ...

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        """Списать средства"""
        ...


# Простейшие реализации для doctest


class Smartphone(Device):
    """Конкретная реализация Device"""

    def __init__(self, name: str, power: int, os: str) -> None:
        super().__init__(name, power)
        self.os: str = os

    def turn_on(self) -> None:
        ...

    def turn_off(self) -> None:
        ...


class Car(Vehicle):
    """Конкретная реализация Vehicle"""

    def __init__(self, brand: str, max_speed: int, doors: int) -> None:
        super().__init__(brand, max_speed)
        self.doors: int = doors

    def move(self) -> None:
        ...

    def stop(self) -> None:
        ...


class BankAccount(Account):
    """Конкретная реализация Account"""

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        self.balance -= amount


if __name__ == "__main__":
    doctest.testmod()
