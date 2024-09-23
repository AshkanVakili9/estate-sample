from django.db import models
# from django.contrib.gis.db import models as gis_models
from django.contrib.auth.models import User

# Model for Employee Card
class Cartext(models.Model):
    file_code = models.CharField(max_length=100, verbose_name="کد فایل")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد فایل")
    last_modified_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ آخرین ویرایش")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    creator = models.CharField(max_length=100, verbose_name="ثبت کننده")
    user_code = models.CharField(max_length=100, verbose_name='کد کاربر')

    def __str__(self):
        return f'{self.file_code} - {self.user.username}'

    class Meta:
        verbose_name = "کارتکس"
        verbose_name_plural = "کارتکس‌ها"

# Model for Property Specification
class PropertySpecification(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('building', 'ساختمان'),
        ('apartment', 'آپارتمان'),
        ('villa', 'ویلایی'),
        ('land', 'زمین'),
        ('garden', 'باغ'),
        ('old_building', 'کلنگی'),
    ]

    USAGE_CHOICES = [
        ('residential', 'مسکونی'),
        ('commercial', 'تجاری'),
        ('administrative', 'اداری'),
        ('educational', 'آموزشی'),
        ('industrial', 'صنعتی'),
        # Add more options as needed
    ]

    POSITION_CHOICES = [
        ('north', 'شمالی'),
        ('south', 'جنوبی'),
        ('east', 'شرقی'),
        ('west', 'غربی'),
    ]

    CORNER_POSITION_CHOICES = [
        ('one_corner', 'یک کله'),
        ('two_corners', 'دو کله'),
        ('two_side', 'دو نبش'),
        ('three_side', 'سه نبش'),
        ('four_side', 'چهار نبش'),
    ]

    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES, verbose_name="نوع ملک")
    floor_number = models.IntegerField(null=True, blank=True, verbose_name="شماره طبقه")  # Only for apartments
    units_per_floor = models.IntegerField(null=True, blank=True, verbose_name="تعداد واحدهای هر طبقه")  # Only for apartments
    usage = models.CharField(max_length=200, choices=USAGE_CHOICES, verbose_name="کاربری", blank=True)
    area = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="مساحت (مترمربع)")
    position = models.CharField(max_length=20, choices=POSITION_CHOICES, verbose_name="موقعیت")
    corner_position = models.CharField(max_length=20, choices=CORNER_POSITION_CHOICES, verbose_name="موقعیت نبش")

    def __str__(self):
        return f"{self.property_type} - {self.area} m²"

    class Meta:
        verbose_name = "مشخصات "
        verbose_name_plural = "مشخصات"

# Model for Property Location
class PropertyLocation(models.Model):
    address = models.TextField(verbose_name="آدرس")
    postal_code = models.CharField(max_length=20, verbose_name="کد پستی")
    # gis_location = gis_models.PointField(verbose_name="موقعیت جغرافیایی", blank=True, null=True)  # For storing geographic location
    images = models.ManyToManyField('PropertyImage', verbose_name="تصاویر", blank=True)  # For uploading multiple images

    def __str__(self):
        return f"موقعیت برای {self.address}"

    class Meta:
        verbose_name = "موقعیت ملک"
        verbose_name_plural = "موقعیت‌های ملک"

# Model for Property Image
class PropertyImage(models.Model):
    image = models.ImageField(upload_to='property_images/', verbose_name="تصویر")

    def __str__(self):
        return f"تصویر {self.id}"

    class Meta:
        verbose_name = "تصویر ملک"
        verbose_name_plural = "تصاویر ملک"

# Model for Registration Information
class RegistrationInfo(models.Model):
    employee_card = models.OneToOneField(Cartext, on_delete=models.CASCADE, verbose_name="کارتکس")
    registration_number = models.CharField(max_length=100, verbose_name="شماره ثبت")
    registration_date = models.DateField(verbose_name="تاریخ ثبت")
    registration_authority = models.CharField(max_length=200, verbose_name="مرجع ثبت")

    def __str__(self):
        return f"ثبت برای {self.employee_card} - {self.registration_number}"

    class Meta:
        verbose_name = "اطلاعات ثبتی"
        verbose_name_plural = "اطلاعات ثبتی"

# Model for Ownership
class Ownership(models.Model):
    PERSON_TYPE_CHOICES = [
        ('real', 'حقیقی'),
        ('legal', 'حقوقی'),
    ]

    owner_name = models.CharField(max_length=200, verbose_name="نام مالک")
    person_type = models.CharField(max_length=10, choices=PERSON_TYPE_CHOICES, verbose_name="نوع شخصیت")
    national_id = models.CharField(max_length=10, verbose_name="کد ملی / شناسه ملی")
    ownership_start_date = models.DateField(verbose_name="تاریخ شروع مالکیت")
    ownership_end_date = models.DateField(null=True, blank=True, verbose_name="تاریخ پایان مالکیت")
    share_percentage = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="سهم از ملک (دانگ)")
    contact_number = models.CharField(max_length=15, verbose_name="شماره تماس")
    mobile_number = models.CharField(max_length=15, verbose_name="شماره همراه")

    def __str__(self):
        return f"مالکیت {self.owner_name} ({self.get_person_type_display()})"

    class Meta:
        verbose_name = "مالکیت"
        verbose_name_plural = "مالکیت‌ها"


# Model for Utilities
class Utility(models.Model):
    employee_card = models.OneToOneField(Cartext, on_delete=models.CASCADE, verbose_name="کارتکس")
    utility_type = models.CharField(max_length=100, verbose_name="نوع انشعاب")
    utility_details = models.CharField(max_length=200, verbose_name="جزئیات انشعاب")

    def __str__(self):
        return f"{self.employee_card} - {self.utility_type}"

    class Meta:
        verbose_name = "انشعاب"
        verbose_name_plural = "انشعابات"

# Model for Transactions
class Transaction(models.Model):
    employee_card = models.ForeignKey(Cartext, on_delete=models.CASCADE, verbose_name="کارتکس")
    transaction_type = models.CharField(max_length=100, verbose_name="نوع معامله")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="مبلغ")
    transaction_date = models.DateField(verbose_name="تاریخ معامله")

    def __str__(self):
        return f"{self.transaction_type} - {self.amount} برای {self.employee_card}"

    class Meta:
        verbose_name = "معامله"
        verbose_name_plural = "معاملات"

# Model for Technical Information
class TechnicalInfo(models.Model):
    employee_card = models.OneToOneField(Cartext, on_delete=models.CASCADE, verbose_name="کارتکس")
    skills = models.TextField(verbose_name="مهارت‌ها")
    certifications = models.TextField(verbose_name="گواهی‌نامه‌ها")
    technical_experience = models.TextField(verbose_name="تجربه فنی")

    def __str__(self):
        return f"اطلاعات فنی برای {self.employee_card}"

    class Meta:
        verbose_name = "اطلاعات فنی"
        verbose_name_plural = "اطلاعات فنی"
