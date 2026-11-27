class Fan:
    def _init_(self):
        self.brand="usha"
        self.cost="2000"
        self.color="black"
        self.wings=3
    def on(self):
        print("Fan is on")
    def rotate(self):
        print("Fan is rotating")
    def off(self):
        print("Fan is off")

f1=Fan()
print(f1.brand)
print(f1.cost)
print(f1.color)
print(f1.wings)
f1.on()
f1.rotate()
f1.off()

# Output:
# usha
# 2000
# black
# 3
# Fan is on
# Fan is rotating
# Fan is off
