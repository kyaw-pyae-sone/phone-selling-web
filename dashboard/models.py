from django.db import models

# Create your models here.

class Phone(models.Model):

    ram_sizes = [
        ("2 gb","2 GB"),
        ("3 gb","3 GB"),
        ("4 gb","4 GB"),
        ("6 gb","6 GB"),
        ("8 gb","8 GB"),
        ("12 gb","12 GB"),
        ("16 gb","16 GB"),
        ("18 gb","18 GB"),
        ("24 gb","24 GB"),
    ]

    storage_sizes = [
        ("8 gb","8 GB"),
        ("16 gb","16 GB"),
        ("32 gb","32 GB"),
        ("64 gb","64 GB"),
        ("128 gb","128 GB"),
        ("256 gb","256 GB"),
        ("512 gb","512 GB"),
        ("1 tb","1 TB"),
        ("2 tb","2 TB"),
    ]

    brand_names = [
            ("iphone", "IPhone"),
            ("samsung", "Samsung"),
            ("oppo", "Oppo"),
            ("vivo", "Vivo"),
            ("infinix", "Infinix"),
            ("redmi", "Redmi"),
            ("one plus", "One plus"),
    ]

    banner = models.ImageField(default="fallback.png", blank=True)
    model_name = models.CharField(max_length=100, primary_key=True)
    instock = models.IntegerField()
    brand = models.CharField(
        max_length=50,
        choices = brand_names
    )
    release_date = models.DateField()
    price = models.FloatField()
    os = models.CharField(max_length=100)
    cpu = models.TextField()
    ram = models.CharField(
        max_length=10,
        choices = ram_sizes
    )
    storage = models.CharField(
        max_length=10,
        choices=storage_sizes
    )
    battery = models.TextField()
    dimension = models.TextField()
    resolution = models.TextField()
    screen = models.TextField()
    network = models.CharField(max_length=100)
    wifi = models.CharField(max_length=100)
    sim_type = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    
    def __str__(self):
        return self.model_name