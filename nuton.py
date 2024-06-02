def calculate_force(mass, acceleration):
    if mass < 0:
        raise ValueError("Масса должна быть неотрицательной величиной.")
    if acceleration < 0:
        raise ValueError("Acceleration must be a non-negative value.")

    force = mass * acceleration
    return force


mass = float(input("Введите массу тела (в kg): "))
acceleration = float(input("Введите ускорение (в m/s^2): "))


try:
    force = calculate_force(mass, acceleration)
    print(f"Сила, необходимая для ускорения объекта, равна {force:.2f} Н.")
except ValueError as e:
    print(e)
