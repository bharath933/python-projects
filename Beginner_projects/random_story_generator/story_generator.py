import random


name = ["bharat","kishore","srinivas","lakshmi","mike","konrad"]
place = ["germany","india","france","italy","spain","poland","netherlands"]
when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 20th Jan']
went = ['cinema', 'university','seminar', 'school', 'laundry']
happened = ['made a lot of friends','Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']

print(random.choice(when)+" " + random.choice(name) + " "+ "that lived in" +" "+ random.choice(place)+" "+ "went to" + " " + random.choice(went) +" and "+ random.choice(happened))
