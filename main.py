from calculadora import Calculadora
from cadenatxt import cadenatxt

calc = Calculadora()
cadenatxt1 = cadenatxt("Hola")
cadenatxt2 = cadenatxt("Chau")

result_sum = calc.sum(1, 2)
result_resta = calc.rest(5, 3)
result_por = calc.mult(2, 5)
result_div = calc.div(10, 2)

cadenatxt1.check_text()
cadenatxt2.check_text()

print("Suma:", result_sum)
print("Resta:", result_resta)
print("Multiplicación:", result_por)
print("División:", result_div)
print(cadenatxt1.text)
print(cadenatxt2.text)