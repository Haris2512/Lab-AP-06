n = int(input("Masukkan nilai n: "))
if n <= 2:
    print("Bilangan yang anda input tidak dapat dijalankan.")
else:
    tengah = n//2
    for i in range(1,tengah+1+(n%2)):
        print("  "*(tengah-i+1) + " *"*(2*i-1))
    for i in range(tengah,0,-1):
        print("  "*(tengah-i+1)+ " *"*(2*i-1))

