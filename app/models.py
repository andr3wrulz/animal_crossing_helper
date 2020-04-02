from django.db import models

class Creature(models.Model):
  name = models.CharField(max_length=256)
  creature_type = models.CharField(max_length=64)
  location = models.CharField(max_length=256)
  time = models.CharField(max_length=64)
  price = models.IntegerField()
  january = models.BooleanField()
  february  = models.BooleanField()
  march = models.BooleanField()
  april = models.BooleanField()
  may = models.BooleanField()
  june = models.BooleanField()
  july = models.BooleanField()
  august = models.BooleanField()
  september = models.BooleanField()
  october = models.BooleanField()
  november = models.BooleanField()
  december = models.BooleanField()
  seasonality = models.CharField(max_length=256)

  def get_seasonality(self):
    month_variable_list = [
      "january", "february", "march", "april",
      "may", "june", "july", "august",
      "september", "october", "november", "december"
    ]
    month_list = [
      "Jan", "Feb", "Mar", "Apr",
      "May", "Jun", "Jul", "Aug",
      "Sep", "Oct", "Nov", "Dec"
    ]

    all_months = True
    months = []
    # Loop through month indexes
    for i in range(0, 12):
      # If the creature is not available in the i-th month
      if (not getattr(self, month_variable_list[i])):
        all_months = False
      else:
        months.append(month_list[i])
    
    if (all_months):
      seasonality = "All year"
    else:
      seasonality = ', '.join(months)

    return seasonality


  def __str__(self):
    return self.name
  
  def save(self, *args, **kwargs):
    self.seasonality = self.get_seasonality()
    super(Creature, self).save(*args, **kwargs)
