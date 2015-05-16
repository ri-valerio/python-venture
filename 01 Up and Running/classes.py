#
# Example file for working with classes
#

class MyClass():
  def method1(self):
    print("MyClass method1")

  def method2(self, someString):
    print("MyClass method2: " + someString)


class AnotherClass(MyClass):
  def method1(self):
    super(AnotherClass, self).method1()
    # MyClass.method1(self);
    print("AnotherClass method1")

  def method2(self):
    print("AnotherClass method2")


def main():
  c = MyClass()
  c.method1()
  c.method2( someString = "This is a string")
  c2 = AnotherClass()
  c2.method1()

if __name__ == "__main__":
  main()
