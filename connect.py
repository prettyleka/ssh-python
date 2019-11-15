import paramiko

key = paramiko.RSAKey.from_private_key_file("./elevation-student.pem")
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print("Connecting")
client.connect(hostname="ec2-52-59-204-217.eu-central-1.compute.amazonaws.com", username="ubuntu", pkey=key)
print("Connected")
stdin, stdout, stderr = client.exec_command(the_command)
print(stdout.read())

client.close()