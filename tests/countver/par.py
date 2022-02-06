import os
import sys


fails = open("fails.out","w+")

def inc_state(state):
    acc = 1
    for i in range(len(state)):
        tmp = acc
        acc = (acc + state[i]) // 2    
        state[i] = (tmp + state[i]) % 2    

def test(number, count):
    state = number*[0]
    for _ in range (2**number):
        f = open("constraints.bul2","w+")
        f.write("#ground num [" + str(number) + "].\n") 
        f.write("#ground count [" + str(count) + "].\n") 
        f.writelines(["~"*state[i] + "var(" + str(i + 1) + ").\n" for i in range(number)])
        f.close()
        #os.system("cat constraints.bul2")
        os.system("bule2 --solve ../../encod/par/fixprepar.bul2 constraints.bul2 clauses.bul2 | grep UNSAT | wc -l > results.out")
        #os.system("cat results.out")
        #os.system("bule2 --facts ../../encod/seq/seq.bul2 constraints.bul2 clauses.bul2 ")
        res = open("results.out","r")
        unsat = int(res.read())
        if(number - sum(state) <= count):
            if(unsat == 1):
                fails.write("Test case failed: expected SAT\n")
                fails.write("Num = " + str(number) + " Count = " + str(count) + "\n")
                fails.write(str(state) + "\n")
        elif(unsat == 0):
            fails.write("Test case failed: expected UNSAT\n")
            fails.write("Num = " + str(number) + " Count = " + str(count) + "\n")
            fails.write(str(state) + "\n")
        inc_state(state)
        res.close()

if __name__ == "__main__":
    fails.write("Start Fails: \n")
    num = 10
    if(len(sys.argv) > 1):
        num = int(sys.argv[1])
    for n in range(num):
        for k in range(n):
            test(n,k)   
    fails.close()
    os.system("cat fails.out")
