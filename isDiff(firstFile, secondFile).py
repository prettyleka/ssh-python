import sys
import paramiko
import subprocess
import os
import difflib

key = paramiko.RSAKey.from_private_key_file("./elevation-student.pem")
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print("Connecting")
client.connect(hostname="ec2-52-59-204-217.eu-central-1.compute.amazonaws.com", username="ubuntu", pkey=key)
print("Connected")

def isDiff(firstFile, secondFile):
    firstFile = '/home/ubuntu/firstFile.txt'
    secondFile = '/home/ubuntu/secondFile/secondFile'
    d = difflib.Differ()
    diff = d.compare(firstFile, secondFile)
    if firstFile == secondFile:
        print(True)
    else:
        print(False)

    #
    # firstFile = '/home/ubuntu/firstFile.txt'
    # secondFile = '/home/ubuntu/secondFile/secondFile.txt'
    # out = client.exec_command('cat, firstFile, secondFile')
    # print(out)

if __name__ == "__main__":
    isDiff('/home/ubuntu/firstFile.txt', '/home/ubuntu/secondFile/secondFile.txt')