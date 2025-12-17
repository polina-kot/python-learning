# TODO Найдите количество книг, которое можно разместить на дискете
disk_Size = 1.44 * 1024 * 1024  # Объем дискеты в байтах

pageCount = 100  # Количество страниц в книге
rowPerPage = 50  # Число строк на странице
charCountInString = 25  # Количество символов в строке
charSize = 4  # Размер символа

bookSize = pageCount * rowPerPage * charCountInString * charSize # Размер одной книги

countBookOnDisk = disk_Size // bookSize # Используется целочисленное деление



print("Количество книг, помещающихся на дискету:", int(countBookOnDisk))
