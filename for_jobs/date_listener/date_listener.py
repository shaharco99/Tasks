import datetime
import socket

# Get today date
curr_date = datetime.date.today()
# Get the title of the day from the current date
day_of_week = curr_date.strftime("%A")

def get_file(conn, filename, replacements):
    with open(filename, 'r') as file:
        content = file.read()
        for placeholder, value in replacements.items():
            content = content.replace(placeholder, str(value))
        # Send the content of the file changed with the replacements,
        # sendall used for automatically try to send any remaining data if the connection is interrupted
        conn.sendall(content.encode())
        # For tests uncomment next line
        # print(content)

# Run the socket on port 8080 on localhost
def main():
    host = ''
    port = 8080

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)

    print(f"Listening on port {port}...")


    while True:
        conn, addr = s.accept()
        print(f"Connection from {addr}")
        # Read the file and create replacements
        filename = 'dates'
        replacements = {'[DAY_OF_WEEK]': day_of_week, '[CURRENT_DATE]': curr_date}
        get_file(conn, filename, replacements)

        conn.close()

if __name__ == '__main__':
    main()
