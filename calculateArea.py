import matplotlib.pyplot as plt
from sympy import *
c = float(input("Enter the form of Parabola>>"))
P = input("Axis of Parabola>>")
T = input("Respective Axis of region>> ")
while T == 'x' or T == 'y' and P == 'x' or P == 'y':
    if P == 'x':
        x1 = []
        y1 = []
        for x in range(1001):
            exp_1 = c*x
            for y in range(1001):
                exp_2 = y**2
                if exp_1 == exp_2:
                    x1.append(x)
                    y1.append(y)

        if T == 'x':
            x1.append(x1[-1])
            y1.append(y1[0])
            t1 = int(input("Enter lower limit value>>"))
            t2 = int(input("Enter upper  limit value>>"))
            x2 = [t1, t1]
            y2 = [0, (t1*c)**0.5]
            x3 = [t2, t2]
            y3 = [0, (t2*c)**0.5]
            x1.append(x1[0])
            y1.append(y1[0])
            x = symbols('x ')
            fy = [0, (t1*c)**0.5]
            o = round((t1*c)**0.5)
            while o < (t2*c)**0.5:
                fy.append(o)
                o += 1
            fx = [t1, t1]
            for o1 in range(len(fy) - 2):
                o2 = ((fy[2 + o1])**2)/c
                fx.append(o2)
            fy.append((t2*c)**0.5)
            fy.append(0)
            fx.append(t2)
            fx.append(t2)
            print(fx, fy)
            res = integrate((c**0.5)*(x**0.5), (x, t1, t2))
            plt.plot(x1, y1, x2, y2, x3, y3, color='k')
            plt.fill_between(fx, fy, color='#cccccc')
            plt.title("Area bounded by this region>>" + str(res))
            plt.show()
            break

        elif T == 'y':
            x1.append(x1[0])
            y1.append(y1[-1])
            t1 = int(input("Enter lower limit value>>"))
            t2 = int(input("Enter upper  limit value>>"))
            x2 = [0, (t1**2)/c]
            y2 = [t1, t1]
            x3 = [0, (t2**2)/c]
            y3 = [t2, t2]
            x1.append(x1[0])
            y1.append(y1[0])
            y = symbols('y')
            fx = [0, float((t1**2)/c)]
            o = round((t1**2)/c)
            while o < (t2**2)/c:
                fx.append(o)
                o += 1
            fy = [t1, t1]
            for o1 in range(len(fx)-2):
                o2 = ((fx[2+o1])*c)**0.5
                fy.append(o2)

            res = integrate((y**2)/c, (y, t1, t2))
            plt.plot(x1, y1, x2, y2, x3, y3, color='k')
            plt.fill_between(fx, fy, t2, color='#cccccc')
            plt.title("Area bounded by this region>>" + str(res))
            plt.show()
            break
    else:
        x1 = []
        y1 = []
        for x in range(1001):
            exp_1 = c*x**2
            for y in range(1001):
                exp_2 = y
                if exp_1 == exp_2:
                    x1.append(x)
                    y1.append(y)

        if T == 'x':
            x1.append(x1[-1])
            y1.append(y1[0])
            t1 = int(input("Enter lower limit value>>"))
            t2 = int(input("Enter upper  limit value>>"))
            x2 = [t1, t1]
            y2 = [0, c*t1**2]
            x3 = [t2, t2]
            y3 = [0, c*t2**2]
            x1.append(x1[0])
            y1.append(y1[0])
            fy = [0, c*t1**2]
            o = round(c*t1**2)
            while o < c*t2**2:
                fy.append(o)
                o += 1
            fx = [t1, t1]
            for o1 in range(len(fy) - 2):
                o2 = ((fy[2 + o1])/c)**0.5
                fx.append(o2)
            print(fx, fy)
            fy.append(c*t2**2)
            fy.append(0)
            fx.append(t2)
            fx.append(t2)
            x = symbols('x ')
            res = integrate(c*x**2, (x, t1, t2))
            plt.plot(x1, y1, x2, y2, x3, y3, color='k')
            plt.fill_between(fx, fy, color='#cccccc')
            plt.title("Area bounded by this region>>" + str(res))
            plt.show()
            break

        elif T == 'y':
            x1.append(x1[0])
            y1.append(y1[-1])
            t1 = int(input("Enter lower limit value>>"))
            t2 = int(input("Enter upper  limit value>>"))
            x2 = [0, float((t1/c)**0.5)]
            y2 = [t1, t1]
            x3 = [0, float((t2/c)**0.5)]
            y3 = [t2, t2]
            x1.append(x1[0])
            y1.append(y1[0])
            print(x1, y1)
            y = symbols('y')
            f1 = [0, float((t1/c)**0.5)]
            o = round((t1/c)**0.5)
            while o < (t2/c)**0.5:
                f1.append(o)
                o += 1
            f2 = [t1, t1]
            for o1 in range(len(f1)-2):
                o2 = ((f1[2+o1])**2)*c
                f2.append(o2)
            f1.append(float((t2/c)**0.5))
            f2.append(t2)
            print(f1, f2)
            res = integrate((y**0.5)/(c**0.5), (y, t1, t2))
            plt.plot(x1, y1, x2, y2, x3, y3, color='k')
            plt.fill_between(f1, f2, t2, color='#cccccc')
            plt.title("Area bounded by this region>>" + str(res))
            plt.show()
            break
else:
    print("Enter for x axis<x> and y axis<y> //>")
