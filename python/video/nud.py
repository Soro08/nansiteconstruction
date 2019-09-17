import nude
from nude import Nude

print(nude.is_nude('images.jpg'))
m = Nude('img.webp')

m.parse()
print("damita_1 :", m.result, m.inspect())
n = Nude('images2.jpg')
n.parse()
print("damita_2 :", n.result, n.inspect())