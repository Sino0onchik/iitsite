from ckeditor.fields import RichTextField
from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=123, verbose_name='Имя')
    description = models.TextField(blank=True, default='', verbose_name='Описание')
    profession = models.CharField(max_length=123, verbose_name='Профессия')
    image = models.ImageField(upload_to='images/teachers/', blank=True, null=True, verbose_name='Изоюражение')
    phone = models.CharField(max_length=134, blank=True, null=True, verbose_name='Номер Телефона')
    email = models.CharField(max_length=134, blank=True, null=True, verbose_name='Почта')
    exp = models.CharField(max_length=123, blank=True, null=True, verbose_name='Опыт в годах')
    education = models.TextField(blank=True, null=True, verbose_name='Образование')
    created_at = models.DateTimeField(auto_now_add=True)
    is_manage = models.BooleanField(blank=True, default=False, verbose_name='Директорат')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class Category(models.Model):
    title = models.CharField(max_length=123)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-created_at']


class News(models.Model):
    title = models.CharField(max_length=123, verbose_name='Название')
    description = RichTextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(verbose_name='Изображение')
    views = models.IntegerField(blank=True, null=True, verbose_name='Колличество просмотров')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='all_news', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modifited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Cafedra(models.Model):
    title = models.CharField(max_length=123, verbose_name='Название')
    description = RichTextField(blank=True, null=True, verbose_name='Описание')
    teachers = models.ManyToManyField(Teacher, blank=True, verbose_name='Преподаватели')
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/cafedras/', verbose_name='Изображение')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Кафедра'
        verbose_name_plural = 'Кафедры'
        ordering = ['title']


class SingletonModel(models.Model):
    """
    Модель, которая всегда имеет только один экземпляр.
    """

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        # Если модель уже существует, удалите ее
        self.__class__.objects.exclude(id=self.id).delete()
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        # Если модель еще не существует, создайте ее
        if not cls.objects.exists():
            cls.objects.create()
        return cls.objects.get()


class SiteContent(models.Model):
    original_text = models.TextField(verbose_name="Оригинальный текст",
                                     help_text="Оригинальный текст, который отображается на сайте.",
                                     max_length=20000
                                     )
    current_text = models.TextField(
        verbose_name="Текущий текст",
        help_text="Измененный или текущий текст, который отображается на сайте.",
        max_length=20000
    )

    class Meta:
        verbose_name = "Контент сайта"
        verbose_name_plural = "Контент сайта"


class SiteSetting(SingletonModel):
    dictors = models.ManyToManyField(Teacher, blank=True, verbose_name='Директорат')
    contacts = models.TextField(blank=True, verbose_name='Контакт')
    emails = models.TextField(blank=True, verbose_name='Почта')
    address = models.CharField(max_length=123, verbose_name="Адрес")

    class Meta:
        verbose_name = 'Настройка сайта'
        verbose_name_plural = 'Настройки сайта'


class Brands(models.Model):
    image = models.ImageField(upload_to='images/brands/')

    class Meta:
        verbose_name = 'Логотип'
        verbose_name_plural = 'Логотипы'
