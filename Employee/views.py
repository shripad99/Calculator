from django.shortcuts import render
# from django.http import HttpResponse
# from django.views import View


# Create your views here.
def home(request):
    return render(request, "home.html")


class Calculator:
    template_name = "home.html"

    def __init__(self, data):
        self.res = []
        self.num1 = int(data)
        self.temp = self.num1
        self.rem = 0
        self.rev = 0
        self.sum = 0
        self.digit = 0
        self.even = 0
        self.odd = 0

    def even_odd(self):
        while self.num1 > 0:
            if self.num1 % 2 == 0:
                self.even = self.even + 1
            else:
                self.odd = self.odd + 1
            self.digit = self.digit + 1
            self.num1 = self.num1 // 10
        return [self.digit, self.even, self.odd]

    def reverse(self):
        self.num1 = self.temp
        while self.num1 > 0:
            self.rem = self.num1 % 10
            self.rev = self.rev * 10 + self.rem
            self.num1 = self.num1 // 10
        return self.rev

    def palindrome(self):
        if self.temp == self.rev:
            self.pal = 'YES'
        else:
            self.pal = 'NO'
        return self.pal

    def armstrong(self):
        while self.num1 > 0:
            self.rem = self.num1 % 10
            self.sum = self.sum + self.rem * self.rem * self.rem
            self.rev = self.rev * 10 + self.rem
            self.num1 = int(self.num1 / 10)

        if self.temp == self.num1:
            self.res2 = 'YES'
        else:
            self.res2 = 'NO'
        return self.res2


def fibonnaci(request):
    result = []
    obj = Calculator(request.POST['num'])
    result.append(obj.even_odd())
    result.append(obj.reverse())
    result.append(obj.palindrome())
    result.append(obj.armstrong)
    return render(request, "result.html", {"result": result})
