import copy
from django.shortcuts import render
from django.http import HttpResponse


# Load the database objects
from .models import Creature


# Index page is list of all creatures in the db
def all(request):
  # Grab all creatures
  bug_list = Creature.objects.order_by('name').filter(creature_type='bug')
  fish_list = Creature.objects.order_by('name').filter(creature_type='fish')

  # Data structure to pass to the template renderer
  context = {
    'bug_list' : bug_list,
    'fish_list' : fish_list
  }

  # Return the rendered template
  return render(request, 'all.html', context)


# This page will show creatures available and highlight ones
# that are new or going away in the specified month
def month(request, month_name):
  month_list = [
    "january", "february", "march", "april",
    "may", "june", "july", "august",
    "september", "october", "november", "december"
  ]

  # Validate the month and get the index
  try:
    month_index = month_list.index(month_name)
  except:
    # Invalid month
    context = {
      'error_msg': 'Invalid month'
    }
    return render(request, 'error.html', context)

  # Get the previous and next months
  prev_month = month_list[(month_index - 1) % 12]
  next_month = month_list[(month_index + 1) % 12]

  # I don't think there is a good way in Django to to do this so I
  # loaded everything and processed it serverside, probably bad but
  # I think the database should be small enough?

  # Grab all creatures available this month
  creature_list = Creature.objects.order_by('name')

  bug_list = []
  fish_list = []

  for c in creature_list:
    # If we can't catch this creature this month, skip it
    if (not getattr(c, month_name)):
      continue

    # Copy the basic info
    formatted = {
      'name' : c.name,
      'creature_type' : c.creature_type,
      'location' : c.location,
      'time' : c.time,
      'price' : c.price,
      'seasonality' : c.seasonality,
      'new' : False,
      'leaving' : False
    }

    # Check if it is new this month
    if (not getattr(c, prev_month)):
      formatted['new'] = True
    
    # Check if it is leaving this month
    if (not getattr(c, next_month)):
      formatted['leaving'] = True
    
    # Add our formatted creature to the list
    if (c.creature_type == "bug"):
      bug_list.append(formatted)
    elif (c.creature_type == "fish"):
      fish_list.append(formatted)

  # Data structure to pass to the template renderer
  context = {
    'month' : month_name.capitalize(),
    'bug_list' : bug_list,
    'fish_list' : fish_list
  }

  # Return the rendered template
  return render(request, 'month.html', context)