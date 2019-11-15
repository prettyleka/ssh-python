import sys
import paramiko
import subprocess
import os

key = paramiko.RSAKey.from_private_key_file("./elevation-student.pem")
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print("Connecting")
client.connect(hostname="ec2-52-59-204-217.eu-central-1.compute.amazonaws.com", username="ubuntu", pkey=key)
print("Connected")



def printDirsNamesAlphabetical():
    stdin, stdout, stderr = client.exec_command('ls /home/ubuntu')
    out = stdout.read().decode('ascii').lower()
    sorted(out)
    with open('dirsNames.txt', 'w') as f:
        f.write(out)
        f.close()




if __name__ == "__main__":
    printDirsNamesAlphabetical()
