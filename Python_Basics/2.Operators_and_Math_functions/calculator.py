#simple calculator example

a,b=0,0

print("Welcome to calculator Choose operation\n")

sel = int(input("\n1.Addition \n2.Substruction \n3.Multipication \n4.Division \n5.modulo \n6.power of (x,y) \n7.div2(round floor)\n\n"))

match sel:
    case 1:
        print("\nEnter two number = ")
        a=int(input())
        b=int(input("+\n"))
        print("=",(a+b))
        pass
    case 2:
        print("\nEnter two number = ")
        a=int(input())
        b=int(input("-\n"))
        print("=",(a-b))
        pass
    case 3:
        print("\nEnter two number = ")
        a=int(input())
        b=int(input("*\n"))
        print("=",(a*b))
        pass
    case 4:
        print("\nEnter two number = ")
        a=int(input())
        b=int(input("/\n"))
        print("=",(a/b))
        pass
    case 5:
        print("\nEnter two number = ")
        a=int(input())
        b=int(input("%\n"))
        print("=",(a%b))
        pass
    case 6:
        print("\nEnter two number = ")
        a=int(input())
        b=int(input("**\n"))
        print("=",(a**b))
        pass
    case 7:
        print("\nEnter two number = ")
        a=int(input())
        b=int(input("//\n"))
        print("=",(a//b))
        pass
    