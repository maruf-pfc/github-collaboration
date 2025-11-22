from django.shortcuts import render
import math

def index(request):
    result = None
    section = None

    if request.method == "POST":
        section = request.POST.get("section")

        # ---------------- BASIC CALCULATOR ----------------
        if section == "basic":
            num1 = float(request.POST.get("num1"))
            num2 = float(request.POST.get("num2"))
            operation = request.POST.get("operation")

            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                result = num1 / num2 if num2 != 0 else "Cannot divide by zero!"

        # ---------------- BMI CALCULATOR ----------------
        elif section == "bmi":
            weight = float(request.POST.get("weight"))
            height = float(request.POST.get("height")) / 100  # cm → meters
            bmi = weight / (height * height)
            result = round(bmi, 2)

        # ---------------- MEASUREMENT CONVERSION ----------------
        elif section == "measure":
            value = float(request.POST.get("value"))
            from_unit = request.POST.get("from_unit")
            to_unit = request.POST.get("to_unit")

            conversions = {
                "m": 1,
                "km": 1000,
                "mile": 1609.34,
                "ft": 0.3048,
                "kg": 1,
                "g": 0.001,
                "lb": 0.453592,
            }

            # Temperature special case
            if from_unit == "c" and to_unit == "f":
                result = (value * 9/5) + 32
            elif from_unit == "f" and to_unit == "c":
                result = (value - 32) * 5/9
            elif from_unit == "c" and to_unit == "k":
                result = value + 273.15
            elif from_unit == "k" and to_unit == "c":
                result = value - 273.15
            elif from_unit in conversions and to_unit in conversions:
                result = value * conversions[from_unit] / conversions[to_unit]
            else:
                result = "Invalid conversion"

        # ---------------- NUMBER SYSTEM ----------------
        elif section == "numbersys":
            num = request.POST.get("num")
            system = request.POST.get("system")

            if system == "bin":
                result = bin(int(num))[2:]
            elif system == "oct":
                result = oct(int(num))[2:]
            elif system == "hex":
                result = hex(int(num))[2:].upper()
            elif system == "dec_from_bin":
                result = int(num, 2)
            elif system == "dec_from_oct":
                result = int(num, 8)
            elif system == "dec_from_hex":
                result = int(num, 16)

        # ---------------- SCIENTIFIC CALCULATOR ----------------
        elif section == "sci":
            op = request.POST.get("op")
            value = float(request.POST.get("sci_value"))

            if op == "sin":
                result = math.sin(math.radians(value))
            elif op == "cos":
                result = math.cos(math.radians(value))
            elif op == "tan":
                result = math.tan(math.radians(value))
            elif op == "log":
                result = math.log10(value)
            elif op == "ln":
                result = math.log(value)
            elif op == "sqrt":
                result = math.sqrt(value)
            elif op == "exp":
                result = math.exp(value)
            elif op == "factorial":
                result = math.factorial(int(value))

    return render(request, "calculator/index.html", {"result": result, "section": section})
