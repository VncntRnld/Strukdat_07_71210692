class PrefixConverter:

    def __init__(self):
        self.stackList = ["?"]
    
    def push(self,data):
        self.stackList.append(data)

    def peek(self):
        if self.stackList:
            return self.stackList[-1]
        else:
            return "Isi Stack Kosong"

    def pop(self):
        if self.stackList:
            data = self.stackList.pop(-1)
            return data
        else:
            return "Isi Stack Kosong"
    
    def cekValidExpression(self, expression):
        for i in expression:
            if i.isalpha() or i == "(":
                return False
        return True
        
    
    def infixToPrefix(self, expression):

        if " " in expression:
            expression = expression.split()

        if not self.cekValidExpression(expression):
            return "Expresi Infix yang anda masukkan tidak valid !!"
        
        op = []
        angka = []

        for i in expression:
            if i.isdigit():
                angka.append(i)
            # elif i == "*" or i == "/":
            #     op.append()


        return "Expresi Prefix-nya Adalah : "
        # for i in reversed(expression):
        #     if i.isdigit():
        #         self.push(i)
            


if __name__ == "__main__":
    ex = PrefixConverter()

    print(ex.infixToPrefix("1+2+3*4/2-1"))
    print(ex.infixToPrefix("A * (B + C) / D"))
    print(ex.infixToPrefix("(1+2)*3"))
    print(ex.infixToPrefix("20 * 3 - 10 + 289"))
    print(ex.infixToPrefix("100 * 30 / 600 - 30 + 100 * 777"))