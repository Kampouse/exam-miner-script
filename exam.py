import subprocess
import random


def pathandler(number):
    output = subprocess.run(['ls',"./exams/0" + str(number) ],capture_output=True, text=True)
    return(output)
 ##working now 
def subjecthandle(output,number):
    lst = output.stdout.split("\n")
    rdm = random.randrange(len(lst ) - 1)
    string = "exams/0" + str(number) + "/" + lst[rdm] + "/" + "subject.en.txt"
    print(rdm)
    return(string)

def addpath(path):
    output.stdout = subprocess.run(['cat',path ],capture_output=True, text=True)
    return (output.stdout)
location = random.randrange(0,5)
output = pathandler(location)
print(location)
print(  addpath(subjecthandle(pathandler(location),location)).stdout)
