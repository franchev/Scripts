my_name = 'francesca koulikov'
my_age = 31
my_height = 62 # inches
my_weight = 120 # lbs
my_eyes = 'brown'
my_teeth = 'Wite'
my_hair = 'Black'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s yeyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# This line is tricky, try to get it exactly right
print "if I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)