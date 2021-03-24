from django.db import models

class product_model(models.Model):
    product_status_choice = (
        ('sold','sold'),
        ('unsold','unsold')
    )
    product_name = models.CharField(max_length=255)
    product_base_price = models.DecimalField(max_digits=20,decimal_places=8)
    product_description = models.TextField()
    product_start_time = models.DateTimeField(blank=False)
    product_end_time = models.DateTimeField(blank=False)
    product_updated_at = models.DateField()
    product_updated_at = models.DateField()
    product_status = models.CharField(choices=product_status_choice,default='unsold', max_length=20)
    product_sold_to = models.IntegerField(blank=False)
    product_image = models.ImageField(upload_to = 'media/product/%Y/%m')
    product_created_at = models.DateField(editable=False,auto_now_add=True)

    def __str__(self):
        return self.product_name
