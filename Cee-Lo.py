import random


class Ceelo1:
    def diceroll1(self):
        self.name1 = input("Enter Player 1 Name: ")
        self.ceelo1 = random.randint(1, 6)
        self.ceelo2 = random.randint(1, 6)
        self.ceelo3 = random.randint(1, 6)
        self.ce1 = [self.ceelo1, self.ceelo2, self.ceelo3]
        self.index = 0
        while self.index < len(self.ce1):
            self.ce1[self.index] = int(self.ce1[self.index])
            self.index += 1
        self.ce1.sort()
        print(self.name1, 'rolled', self.ce1)
        self.calcwinner1()
        self.autowin1 = [4, 5, 6]
        self.autolose1 = [1, 2, 3]
        self.checkautowinlose1()
        self.reroll1()

    def calcwinner1(self):
        if self.ce1[0] == self.ce1[1] and self.ce1[0] != self.ce1[2]:
            print(self.name1, 'rolled', self.ce1[2])
        elif self.ce1[0] == self.ce1[1] and self.ce1[0] == self.ce1[2]:
            print(self.name1, 'rolled trip', self.ce1[2], 's')
        elif self.ce1[1] == self.ce1[2] and self.ce1[0] != self.ce1[2]:
            print(self.name1, 'Rolled', self.ce1[0])

    def checkautowinlose1(self):
        if self.ce1 == self.autowin1:
            print(' autowins')
        elif self.ce1 == self.autolose1:
            print('autoloses')
        return self.ce1

    def reroll1(self):
        while self.ce1[0] != self.ce1[1] and self.ce1[1] != self.ce1[
            2] and self.ce1 != self.autowin1 and self.ce1 != self.autolose1:
            print('re-rolling')
            self.ceelo1 = random.randint(1, 6)
            self.ceelo2 = random.randint(1, 6)
            self.ceelo3 = random.randint(1, 6)
            self.ce1 = [self.ceelo1, self.ceelo2, self.ceelo3]
            self.index = 0
            while self.index < len(self.ce1):
                self.ce1[self.index] = int(self.ce1[self.index])
                self.index += 1
            self.ce1.sort()
            print(self.name1, 'rolled', self.ce1)
            if self.ce1 == self.autowin1:
                print("autowins")
            elif self.ce1 == self.autolose1:
                print(self.name1, 'Autoloses')
            self.calcwinner1()


class Ceelo2():
    def diceroll2(self):
        self.name2 = input("Enter Player 2 Name: ")
        self.ceelo4 = random.randint(1, 6)
        self.ceelo5 = random.randint(1, 6)
        self.ceelo6 = random.randint(1, 6)
        self.ce2 = [self.ceelo4, self.ceelo5, self.ceelo6]
        self.index = 0
        while self.index < len(self.ce2):
            self.ce2[self.index] = int(self.ce2[self.index])
            self.index += 1
        self.ce2.sort()
        print(self.name2, 'rolled', self.ce2)
        self.calcwinner2()
        self.autowin2 = [4, 5, 6]
        self.autolose2 = [1, 2, 3]
        self.checkautowinlose2()
        self.reroll2()

    def calcwinner2(self):
        if self.ce2[0] == self.ce2[1] and self.ce2[0] != self.ce2[2]:
            print(self.name2, 'rolled', self.ce2[2])
        elif self.ce2[0] == self.ce2[1] and self.ce2[0] == self.ce2[2]:
            print(self.name2, 'rolled trip', self.ce2[2], 's')
        elif self.ce2[1] == self.ce2[2] and self.ce2[0] != self.ce2[2]:
            print(self.name2, 'rolled', self.ce2[0])

    def checkautowinlose2(self):
        if self.ce2 == self.autowin2:
            print('autowins')
        elif self.ce2 == self.autolose2:
            print('autoloses')
        return self.ce2

    def reroll2(self):
        while self.ce2[0] != self.ce2[1] and self.ce2[1] != self.ce2[
            2] and self.ce2 != self.autowin2 and self.ce2 != self.autolose2:
            print('re-rolling')
            self.ceelo4 = random.randint(1, 6)
            self.ceelo5 = random.randint(1, 6)
            self.ceelo6 = random.randint(1, 6)
            self.ce2 = [self.ceelo4, self.ceelo5, self.ceelo6]
            self.index = 0
            while self.index < len(self.ce2):
                self.ce2[self.index] = int(self.ce2[self.index])
                self.index += 1
            self.ce2.sort()
            print(self.name2, 'rolled', self.ce2)
            if self.ce2 == self.autowin2:
                print("autowins")
            elif self.ce2 == self.autolose2:
                print(self.name2, 'autoloses')
            self.calcwinner2()

class Ceelo3():
    def diceroll3(self):
        self.name3 = input("Enter Player 3 Name: ")
        self.ceelo7 = random.randint(1, 6)
        self.ceelo8 = random.randint(1, 6)
        self.ceelo9 = random.randint(1, 6)
        self.ce3 = [self.ceelo7, self.ceelo8, self.ceelo9]
        self.index = 0
        while self.index < len(self.ce3):
            self.ce3[self.index] = int(self.ce3[self.index])
            self.index += 1
        self.ce3.sort()
        print('rolled',self.ce3)
        self.calcwinner3()
        self.autowin3 = [4, 5, 6]
        self.autolose3 = [1, 2, 3]
        self.checkautowinlose3()
        self.reroll3()


    def calcwinner3(self):
        if self.ce3[0] == self.ce3[1] and self.ce3[0] != self.ce3[2]:
            print(self.name3,'rolled', self.ce3[2])
        elif self.ce3[0] == self.ce3[1] and self.ce3[0] == self.ce3[2]:
            print(self.name3,'trip', self.ce3[2], 's')
        elif self.ce3[1] == self.ce3[2] and self.ce3[0] != self.ce3[2]:
            print(self.name3,'rolled', self.ce3[0])


    def checkautowinlose3(self):
        if self.ce3 == self.autowin3:
            print(self.name3,'autowins')
        elif self.ce3 == self.autolose3:
            print(self.name3,'autoloses')
        return self.ce3


    def reroll3(self):
        while self.ce3[0] != self.ce3[1] and self.ce3[1] != self.ce3[
            2] and self.ce3 != self.autowin3 and self.ce3 != self.autolose3:
            print('re-rolling')
            self.ceelo7 = random.randint(1, 6)
            self.ceelo8 = random.randint(1, 6)
            self.ceelo9 = random.randint(1, 6)
            self.ce3 = [self.ceelo7, self.ceelo8, self.ceelo9]
            self.index = 0
            while self.index < len(self.ce3):
                self.ce3[self.index] = int(self.ce3[self.index])
                self.index += 1
            self.ce3.sort()
            print(self.name3,"rolled", (self.ce3))
            if self.ce3 == self.autowin3:
                print(self.name3, "autowins")
            elif self.ce3 == self.autolose3:
                print(self.name3,'autoloses')
            self.calcwinner3()



A = Ceelo1()
A.diceroll1()

B = Ceelo2()
B.diceroll2()
