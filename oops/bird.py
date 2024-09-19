class Bird:
    def fly(self):
        return 'bird is flying..'
class crow(Bird):
    def fly(self):
        return 'crow is flying'

class parrot(Bird):
    def fly(self):
        return 'parrot is flying'
    
class Eagle(Bird):
    def fly(self):
        return 'parrot is flying'
    






def test_fly(bird):
    print(bird.fly())


crow1 = crow()
parrot1 =parrot()
parrot2 = parrot()
eagle1 = Eagle()
test_fly(crow1)
test_fly(parrot1)
test_fly(parrot2)
test_fly(eagle1)