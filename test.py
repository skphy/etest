# Import classes from your brand new package
from xxx_code import Mammals
from xxx_code import Birds
 
# Create an object of Mammals class & call a method of it
myMammal = Mammals()
myMammal.printMembers()
 
# Create an object of Birds class & call a method of it
myBird = Birds()
myBird.printMembers()


from xxx_code.subdir1 import sd1
from xxx_code.subdir1.sd1 import World
from xxx_code.subdir2 import sd2

x = World('india')
print x.yourname
x.india()
x.occupation()

