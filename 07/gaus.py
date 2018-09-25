import math
def f(x):
    return math.log(x) + 2 * x**2 - 6

def f_prime(x):
    return 1/x + 4*x

def newton_method(x0, tol, max_iter):
    x = x0
    for i in range(max_iter):
        x_next = x - f(x) / f_prime(x)
        if abs(x_next - x) < tol:
            return x_next
        x = x_next
    return None  # Если не сошлось
# Начальное приближение, точность и максимальное количество итераций
x0_newton = 2.0
tolerance_newton = 1e-3
max_iterations_newton = 100

root_newton = newton_method(x0_newton, tolerance_newton, max_iterations_newton)
if root_newton is not None:
    print(f"Приближенный корень методом Ньютона: {root_newton}")
else:
    print("Метод Ньютона не сошелся.")
