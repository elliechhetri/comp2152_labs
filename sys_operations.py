import platform
import socket
import os
import sys

# Displays the machine type, CPU
print(f"- Machine type: {platform.machine()}\n")
print(f"- CPU Architecture: {platform.architecture()}\n")

socket.setdefaulttimeout(50)
print(f"- Current default socket time out: {socket.getdefaulttimeout()}\n")

print(f"- OS Type: {os.name}\n")
print(f"- OS Name: {platform.system()}\n")

print(f"- Current process ID (PID): {os.getpid()}")



file_name = "fdpractice.txt"

file_handle = os.open(file_name, os.O_RDWR | os.O_CREAT)
print(f"- [PID: {os.getpid()}] Opened the file_handle: {file_handle}\n")

file_object_TextIO = os.fdopen(file_handle, "w+")
file_object_TextIO.write("Some string to write to the file")
file_object_TextIO.flush()

print(f"- [PID: {os.getpid()}] Forking now...\n")
pid = os.fork()
# pid = 0

if pid == 0:
    print(f"- [Child PID: {os.getpid()}], Parent PID: {os.getppid()}]\n")
    os.lseek(file_handle, 0, 0)
    print(f"- [Child PID: {os.getpid()}] File Content: {os.read(file_handle, 100).decode()}\n")
    os.close(file_handle)
    sys.exit(0)

else:
    print(f"- [Child PID: {os.getpid()}], Parent PID: {os.getppid()}]\n")
    print("Wait for child")
    os.wait()
    print("Child finished")
    file_object_TextIO.close()
    sys.exit(0)