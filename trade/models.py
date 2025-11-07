from django.db import models


class Contact(models.Model):
    """Модель контактов звена сети"""

    email = models.EmailField(unique=True, verbose_name="Email")
    country = models.CharField(max_length=100, verbose_name="Страна")
    city = models.CharField(max_length=100, verbose_name="Город")
    street = models.CharField(max_length=255, verbose_name="Улица")
    house_number = models.CharField(max_length=20, verbose_name="Номер дома")

    def __str__(self):
        return f"{self.email}, ({self.city})"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"


class Product(models.Model):
    """Модель продукт"""

    name = models.CharField(max_length=255, verbose_name="Название продукта")
    model = models.CharField(max_length=255, verbose_name="Модель")
    release_date = models.DateField(verbose_name="Дата выхода продукта на рынок")

    def __str__(self):
        return f"{self.name}, ({self.model})"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class LinkNetwork(models.Model):
    """Модель звена сети"""

    name = models.CharField(max_length=255, verbose_name="Название")
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE, related_name='network_link')
    products = models.ManyToManyField(Product, verbose_name="Продукт", related_name='network_links')
    supplier = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Поставщик")
    debt = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Задолженность перед поставщиком")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    @property
    def get_level(self):
        if self.supplier is None:
            return 0  # Завод без поставщика — уровень 0
        level = 0
        supplier = self.supplier
        while supplier:
            level += 1
            supplier = supplier.supplier
        return level

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Звено сети"
        verbose_name_plural = "Звенья сети"