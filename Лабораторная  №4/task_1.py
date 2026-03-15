class BuildingElement:
    """
    Базовый класс для всех строительных элементов.

    Содержит общие атрибуты и методы, характерные для любых элементов здания.
    Некоторые атрибуты сделаны защищёнными, так как их изменение напрямую может
    нарушить целостность данных об элементе.
    """

    def __init__(self, element_id: str, name: str, material: str) -> None:
        """
        Инициализация базового строительного элемента.

        Args:
            element_id: Уникальный идентификатор элемента (защищённый атрибут)
            name: Наименование элемента
            material: Материал элемента
        """
        self._id = element_id
        self.name = name
        self.material = material
        self._volume = 0.0

    @property
    def id(self) -> str:
        """Геттер для идентификатора (только для чтения)."""
        return self._id

    def calculate_volume(self) -> float:
        """
        Базовый метод расчёта объёма.

        В базовом классе возвращает 0, так как для разных элементов
        формула расчёта объёма может отличаться.

        Returns:
            float: Объём элемента
        """
        return self._volume

    def get_info(self) -> str:
        """
        Получение базовой информации об элементе.

        Returns:
            str: Информационная строка
        """
        return f"Элемент {self.name} (ID: {self._id}) из материала {self.material}"

    def __str__(self) -> str:
        """Строковое представление для пользователя."""
        return f"{self.name} [{self.material}]"

    def __repr__(self) -> str:
        """Официальное строковое представление для разработчика."""
        return f"{self.__class__.__name__}(id='{self._id}', name='{self.name}', material='{self.material}')"


class Wall(BuildingElement):
    """
    Класс стены (дочерний от BuildingElement).

    Стена имеет дополнительные параметры: длина, высота, толщина.
    Метод расчёта объёма переопределён, так как для стены формула отличается.
    """

    def __init__(self, element_id: str, name: str, material: str,
                 length: float, height: float, thickness: float) -> None:
        """
        Инициализация стены. Расширяет конструктор базового класса.

        Args:
            element_id: Уникальный идентификатор
            name: Наименование стены
            material: Материал
            length: Длина стены (м)
            height: Высота стены (м)
            thickness: Толщина стены (м)
        """
        super().__init__(element_id, name, material)
        self.length = length
        self.height = height
        self.thickness = thickness
        self._fire_rating = None

    @property
    def fire_rating(self) -> str | None:
        """Геттер для класса пожарной безопасности."""
        return self._fire_rating

    @fire_rating.setter
    def fire_rating(self, value: str) -> None:
        """
        Сеттер для класса пожарной безопасности с проверкой формата.

        Args:
            value: Класс пожарной безопасности (например, "REI 120")

        Raises:
            ValueError: Если формат не соответствует ожидаемому
        """
        if value and not value.startswith(("REI", "R", "EI")):
            raise ValueError("Некорректный формат класса пожарной безопасности")
        self._fire_rating = value

    def calculate_volume(self) -> float:
        """
        Переопределённый метод расчёта объёма для стены.

        Причина перегрузки: для стены объём вычисляется как произведение
        длины, высоты и толщины, что отличается от базовой реализации.

        Returns:
            float: Объём стены в кубических метрах
        """
        self._volume = self.length * self.height * self.thickness
        return self._volume

    def get_info(self) -> str:
        """
        Расширенный метод получения информации (перегрузка).

        Добавляет информацию о геометрических параметрах стены.

        Returns:
            str: Расширенная информация о стене
        """
        base_info = super().get_info()
        return (f"{base_info}, Размеры: {self.length}x{self.height}x{self.thickness} м, "
                f"Объём: {self.calculate_volume():.2f} м³")

    def __str__(self) -> str:
        """Перегруженное строковое представление для стены."""
        return f"Стена: {self.name} ({self.length}x{self.height}x{self.thickness} м)"


class Column(BuildingElement):
    """
    Класс колонны (дочерний от BuildingElement).

    Колонна может быть круглого или прямоугольного сечения.
    Метод расчёта объёма переопределён в зависимости от типа сечения.
    """


    SECTION_TYPES = {
        'rect': 'прямоугольное',
        'circle': 'круглое'
    }

    def __init__(self, element_id: str, name: str, material: str,
                 section_type: str, height: float, width: float = None) -> None:
        """
        Инициализация колонны.

        Args:
            element_id: Уникальный идентификатор
            name: Наименование колонны
            material: Материал
            section_type: Тип сечения ('rect' или 'circle')
            height: Высота колонны (м)
            width: Для прямоугольного сечения - вторая сторона (м),
                  для круглого - диаметр (если не указан, используется radius)

        Raises:
            ValueError: При некорректном типе сечения
        """
        super().__init__(element_id, name, material)

        if section_type not in self.SECTION_TYPES:
            raise ValueError(f"Тип сечения должен быть один из: {list(self.SECTION_TYPES.keys())}")

        self.section_type = section_type
        self.height = height
        self._width = width
        self._radius = None

    @property
    def width(self) -> float | None:
        """Геттер для ширины/диаметра сечения."""
        return self._width

    @width.setter
    def width(self, value: float) -> None:
        """
        Сеттер для ширины с проверкой положительности.

        Args:
            value: Ширина/диаметр сечения

        Raises:
            ValueError: При отрицательном значении
        """
        if value <= 0:
            raise ValueError("Размер сечения должен быть положительным числом")
        self._width = value

        if self.section_type == 'circle':
            self._radius = value / 2

    def calculate_volume(self) -> float:
        """
        Переопределённый метод расчёта объёма для колонны.

        Причина перегрузки: объём колонны зависит от формы сечения,
        что требует разного подхода к расчёту.

        Returns:
            float: Объём колонны в кубических метрах
        """
        if self.section_type == 'rect':

            if self._width is None:
                raise ValueError("Для прямоугольной колонны необходима ширина")
            base_area = self._width * self._width
        else:

            if self._radius is None and self._width is not None:
                self._radius = self._width / 2
            elif self._radius is None:
                raise ValueError("Для круглой колонны необходим диаметр или радиус")
            base_area = 3.14159 * (self._radius ** 2)

        self._volume = base_area * self.height
        return self._volume

    def get_info(self) -> str:
        """
        Расширенный метод получения информации (перегрузка).

        Добавляет информацию о типе сечения и высоте колонны.

        Returns:
            str: Расширенная информация о колонне
        """
        base_info = super().get_info()
        section_name = self.SECTION_TYPES.get(self.section_type, 'неизвестный тип')
        return (f"{base_info}, {section_name} сечение, "
                f"высота: {self.height} м, объём: {self.calculate_volume():.2f} м³")

    def __str__(self) -> str:
        """Перегруженное строковое представление для колонны."""
        return f"Колонна: {self.name}, тип сечения: {self.SECTION_TYPES[self.section_type]}"



if __name__ == "__main__":

    wall = Wall("W001", "Наружная стена", "Бетон", 5.0, 3.0, 0.4)
    print(wall)
    print(wall.get_info())

    wall.fire_rating = "REI 120"
    print(f"Класс пожарной безопасности: {wall.fire_rating}")

    print("-" * 50)

    column1 = Column("C001", "Колонна 1", "Сталь", "circle", 4.5, 0.3)
    print(column1)
    print(column1.get_info())

    print("-" * 50)

    column2 = Column("C002", "Колонна 2", "Железобетон", "rect", 3.0, 0.4)
    print(column2)
    print(column2.get_info())


    print(repr(wall))
    print(repr(column1))
