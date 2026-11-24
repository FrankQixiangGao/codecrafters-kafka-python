import socket  # noqa: F401
import struct

def main():
    # You can use print statements as follows for debugging,
    # they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # TODO: Uncomment the code below to pass the first stage
    server = socket.create_server(("localhost", 9092), reuse_port=True)
    conn, _ = server.accept()
    data = conn.recv(256)
    # print(data.hex())


    conn.sendall(struct.pack(">i", 0) + data[8:12])


if __name__ == "__main__":
    main()
