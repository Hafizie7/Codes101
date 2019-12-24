from django.db import models

# Create your models here.
class Rooms(models.Model):

    no = models.IntegerField()
    price = models.IntegerField()

    choices = (
        ('AVAILABLE', 'Room is available'),
        ('RESERVED', 'Room already reserved'),
    )
    status = models.CharField(max_length=10, choices=choices, default='Available')
    issues = models.CharField(max_length=50, default="No Issues")

    class Meta:
        abstract = True

    def __str__(self):
        return 'no: {0} price: {1}'.format(self.no, self.price)

class SingleBed(Rooms):
    pass

class Double_bed(Rooms):
    pass

class Customer(models.Model):

    CustomerName = models.CharField(max_length=50)
    RoomNo = models.IntegerField()

    def __str__(self):
        return 'CustomerName: {0} RoomNo: {1}'.format(self.CustomerName, self.RoomNo)
