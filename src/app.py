import sys
import os


def prime(s): 
    s = int(s)
    if s > 1:
        for i in range(2, s):
            if (s % i) == 0:
                print(s, "is a not a prime number")
                break
            else:
                print(s, "is a prime number")     
    else:
        print("not prime")
    
   
def solution(s):
    return prime(s)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argument required"))

    print(solution(sys.argv[1]))
