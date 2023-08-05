def vielfache3oder5():
    totalSum = 0
    for i in range(1000):
        if(i % 5 == 0 or i % 3 == 0):
            print(i)
            totalSum += i

    print(totalSum)


def geradeFibonacciZahlen():
    temp = 1
    fibo = 1
    totalSum = 0
    while (totalSum + fibo + temp) < 4000000:
        temp2 = fibo
        fibo = fibo + temp
        temp = temp2
        if fibo % 2 == 0:
            totalSum+=fibo
        
        print("fibo " + str(fibo))
    
    print("totalSum " + str(totalSum))

def primeFactorsOf(n = 48):
    
    primfaktoren = []
    def isPrime(n):
        if n < 2:
            return False
        if n==2:
            return True
        i = 2
        while i < n:
            
            if n % i == 0:
                return False
            i+=1
        return True


    m = n        
    for i in range (m - 1):
        if(n==1):
            break
        if isPrime(i):
            while n % i == 0:
               
                n = n / i
                primfaktoren.append(i)
        
    print((primfaktoren))
                
        
    
    
def biggestPalindromProduct():
    palindromList = []
    for i in range (999, 0, -1):
        for k in range(999, i, -1):
            if str(k * i) == str(k * i)[::-1]:
                palindromList.append(k*i)
    
                
    print(max(palindromList))

def smallestMultiple(n=20):
    
    k = 20
    while True:
        isMultiple = True
        k+=1
        for i in range(1, n +1):
            if k % i != 0:
                #print("nicht teilbar: k: "+str(k) + " i: " + str(i))
                isMultiple = False
                break
        if isMultiple:
            break
            
       
    return k


def largestProduct():
    longNumber = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
    product = 1
    counter = 0
    i = 0
    productList = []
    while i < len(longNumber):
        for k in range(i, i+13):
            if k < len(longNumber):
                product *= int(longNumber[k])
                #print(longNumber[k])
        productList.append(product)
        product = 1
            
        i+=1
    
    return max(productList)

primeFactorsOf()

    


    
