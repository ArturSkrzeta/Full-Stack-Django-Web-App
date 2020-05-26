from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

status_choice = (
    ('Open','Open'),
    ('Pending','Pending'),
    ('Approval','Approval'),
    ('On Hold','On Hold'),
    ('Closed','Closed')
)

category_choice = (
    ('Construction', 'Construction'),
    ('Consulting','Consulting'),
    ('Facility Management', 'Facility Management'),
    ('General Goods and Sevices','General Goods and Sevices'),
    ('Inormation Technology','Information Technlogy'),
    ('Office Supplies','Office Supplies')
)

class PR(models.Model):
    pr_number = models.CharField(max_length=100, unique=True)
    total = models.FloatField(max_length=100,default=0.00)
    status = models.CharField(max_length=100, choices=status_choice, default='Open')
    category = models.CharField(max_length=100, choices=category_choice, default='Choose Category')
    description = models.TextField(blank=True, default='')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # one user can have many prs

    def __str__(self):
        return self.pr_number

    def get_absolute_url(self):
        return reverse('pr-detail', kwargs={'pk': self.pk})
