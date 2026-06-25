import math

def calculate_trigonometry():
    angle = float(input("Enter the angle in degrees: "))

    # Convert degrees to radians
    radians = math.radians(angle)

    # Calculate trigonometric values
    sine = math.sin(radians)
    cosine = math.cos(radians)
    tangent = math.tan(radians)

    print(f"\nAngle: {angle}°")
    print(f"sin({angle}) = {sine:.4f}")
    print(f"cos({angle}) = {cosine:.4f}")
    print(f"tan({angle}) = {tangent:.4f}")

calculate_trigonometry()