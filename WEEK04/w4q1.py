def avg(a, b, c, d, e):
    return (a + b + c + d + e) / 5

def f_tmp(c_tmp):
    return (c_tmp * 9/5) + 32

def peri(len, wid):
    return 2 * (len + wid)

if __name__ == "__main__":
    average = avg(10, 20, 30, 40, 50)
    print(f"avg: {average}")

    fah = f_tmp(25)
    print(f"temp: {fah}")

    pmtr = peri(5, 10)
    print(f"peri: {pmtr}")