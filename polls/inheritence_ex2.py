class A(object):
    def go(self):
        print("go A go!")

    def stop(self):
        print("stop A stop!")

    def pause(self):
        raise Exception("Not Implemented")


class B(A):
    def go(self):
        super(B, self).go()
        print("go B go!")


class C(A):
    def go(self):
        super(C, self).go()
        print("go C go!")

    def stop(self):
        super(C, self).stop()
        print("stop C stop!")


class D(B,C):
    def go(self):
        super(D, self).go()
        print("go D go!")

    def stop(self):
        super(D, self).stop()
        print("stop D stop!")

    def pause(self):
        print("wait D wait!")


class E(B, C): pass

a = A()
b = B()
c = C()
d = D()
e = E()

# specify output from here onwards

a.go()
b.go()
c.go()
d.go()
e.go()

a.stop()
b.stop()
c.stop()
d.stop()
e.stop()

a.pause()
b.pause()
c.pause()
d.pause()
e.pause()





1. Indentation
2. Interpreted
3. Dynamic typing
4. Open sourced
5. Library
6. OOPs
7. Easy to learn


1. Python 2.* Vs 3.*

Python slower compared to C/C++
Multi thereading
GIL - Global Interpreted Lock
    - One thread at a time



Garbage Collector
    - Refernce Count



OOPs, MRO

Function overloading, overriding


Signals

DB Migration tools - south







