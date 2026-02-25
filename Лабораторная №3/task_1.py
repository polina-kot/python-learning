class Book:
    """
    Базовый класс книги.
    """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """Геттер для названия книги (только для чтения)."""
        return self._name

    @property
    def author(self) -> str:
        """Геттер для автора книги (только для чтения)."""
        return self._author

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """
    Класс для бумажной книги (наследуется от Book).
    """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        """Геттер для количества страниц."""
        return self._pages

    @pages.setter
    def pages(self, value: int) -> None:
        """
        Сеттер для количества страниц с проверкой:
        - должно быть целым числом
        - должно быть положительным
        """
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = value

class AudioBook(Book):
    """
    Класс для аудиокниги (наследуется от Book).
    """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration
    @property
    def duration(self) -> float:
        """Геттер для продолжительности."""
        return self._duration

    @duration.setter
    def duration(self, value: float) -> None:
        """
        Сеттер для продолжительности с проверкой:
        - должно быть числом (int или float)
        - должно быть положительным
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность должна быть числом")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self._duration = float(value)

    def __str__(self) -> str:
        """
        Переопределяем __str__ для отображения специфичной информации.
        """
        return f"Аудиокнига {self.name}. Автор {self.author}. Длительность: {self.duration} ч."

if __name__ == "__main__":
    paper_book = PaperBook("Война и мир", "Лев Толстой", 1300)
    audio_book = AudioBook("1984", "Джордж Оруэлл", 11.5)


    print(paper_book)
    print(repr(paper_book))

    print(audio_book)
    print(repr(audio_book))


    try:
        paper_book.pages = -100
    except ValueError as e:
        print(f"Ошибка: {e}")

    try:
        audio_book.duration = "десять"
    except TypeError as e:
        print(f"Ошибка: {e}")