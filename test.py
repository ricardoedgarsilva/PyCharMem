import subprocess, os

# Determine the current platform
if os.name == 'nt':  # for Windows
    # Launch a new console window and run another Python script in it
    process = subprocess.Popen(['start', 'cmd', '/k', 'python'], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
else:  # for Linux, macOS, and other platforms
    # Launch a new terminal window and run another Python script in it
    process = subprocess.Popen(['osascript' ], stdin=subprocess.PIPE, stdout=subprocess.PIPE)



# Send data to the second script
process.stdin.write(b"Value 1: 10\n")
process.stdin.write(b"Value 2: 20\n")
process.stdin.flush()
