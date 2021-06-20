from django.db import models

class Tokens(models.Model):
    tok_name = models.CharField(max_length=50)
    tok_symbol = models.CharField(max_length=50)
    init_supply = models.DecimalField(max_digits=1000,decimal_places=1,default='0')
    tok_addr = models.CharField(max_length=50)
    dev_addr = models.CharField(max_length=50)
    dep_time = models.DateTimeField(default='2021-06-19 14:26:03+00')
    eip_score = models.SmallIntegerField(default='1')