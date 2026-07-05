"""bill"""

def main():
    """bill"""
    x = int(input())
    y = x * 0.1
    if y < 50:
        y = 50
    elif y >= 1000:
        y = 1000
    z = (x + y) * 0.07
    a = x + y + z
    print(f"{a:.2f}")
main()
