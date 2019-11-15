import sys
import paramiko

key = paramiko.RSAKey.from_private_key_file("./elevation-student.pem")
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print("Connecting")
client.connect(hostname="ec2-52-59-204-217.eu-central-1.compute.amazonaws.com", username="ubuntu", pkey=key)
print("Connected")

def dirs_fiIes():
    dir_num = 8
    file_num = 9

    dir = sys.argv[1]
    file = sys.argv[2]
    commands = []
    commands.append("mkdir {}".format(dir))
    for i in range(0, dir_num + 1):
        commands.append("cd {}; mkdir {}{}".format(dir,dir,i))
        for z in range(0, file_num + 1):
            commands.append("cd {}; touch {}{}/{}{}.txt".format(dir,dir,i,file,z))

    for command in commands:
        client.exec_command(command)

    client.close()





if __name__ == "__main__":
    dirs_fiIes()