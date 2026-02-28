import os

os.system("python .\clear.py")

for i in range(100):
    os.system("python .\create-example.py")
    os.system("organize run .\example\ ")
    print(i)