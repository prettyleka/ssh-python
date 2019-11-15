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

def print_is():
        stdin, stdout, stderr = client.exec_command('grep  "is" /home/ubuntu/a/b/c/d/secretFile.txt')
        out=stdout.read().decode('ascii').split('\n')[:-1]
        print(out)





if __name__ == "__main__":
    print_is()