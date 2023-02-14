# _*_ coding: utf-8 _*_
# @Time : 2022/2/7 18:13
# @Author : 进击的大饼
# @File : looklook 
# @Project : hw06

class Number:
    def __add__(self, other):
        return self.add(other)

    def __mul__(self, other):
        return self.mul(other)


class Complex(Number):
    def add(self, other):
        return ComplexRI(self.real + other.real, self.imag + other.imag)

    def mul(self, other):
        magnitude = self.magnitude * other.magnitude
        return ComplexMA(magnitude, self.angle + other.angle)


class ComplexRI(Complex):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def magnitude(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5

    def angle(self):
        return (self.imag, self.real)

    def __repr__(self):
        return 'ComplexRI({0:g}, {1:g})'.format(self.real, self.imag)


def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


def count(f):
    def counted(n):
        counted.call_count += 1
        return f(n)
    counted.call_count = 0
    return counted

class A:
    def f(self):
        return 2
    def g(self, obj, x):
        if x == 0:
            return A.f(obj)
        return obj.f() + self.g(self, x - 1)
class B(A):
    def f(self):
        return 4

class Yolo:
    def __init__(self, n):
        self.n = n

    def g(self, m):
        return self.n + m

    @property
    def motto(self):
        return

    @motto.setter
    def motto(self, amount):
        self.n = amount


class Yolo2:
    def __init__(self, motto=0):
        self.motto = motto

    def g(self, amount):
        return amount + self.motto



class Instructor:
    degree = "PhD(Magic)"

    def __init__(self, name):
        self.name = name


class Email:
    def __init__(self, msg, sender_name, recipient_name):
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name


class Mailman:
    def __init__(self):
        self.clients = {}

    def send(self, email):
        self.clients[email.recipient_name].receive(Email(email.msg, email.sender_name, email.recipient_name))

    def register_client(self, client, client_name):
        self.clients[client_name] = client

class Client:
    def __init__(self, mailman, name):
        self.inbox = []
        self.mailman = mailman
        self.name = name

    def compose(self, msg, recipient_name):
        self.mailman.clients[recipient_name].recive(Email(msg, self.name, recipient_name)) # 前面的recipient应该是obj

    def receive(self, email):
        self.inbox.append(email)


