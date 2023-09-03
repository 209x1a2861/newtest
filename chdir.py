import os
os.chdir(r"C:\Users\bharg\OneDrive\Desktop\practice\faces")
name="dkgjdfsg"
if name not in os.listdir():
    os.mkdir(name)
path=os.getcwd()
path=path+"\\"+name
print(path)
print(os.listdir())
