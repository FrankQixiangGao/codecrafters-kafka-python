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
    correlation_id = data[8:12]
    api_version = int.from_bytes(data[6:8], "big")

    # print(data.hex())
    if api_version <= 4:
        conn.sendall(struct.pack(">i", 2) + data[8:12])
    else:
        conn.sendall(struct.pack(">i", 0) + data[8:12] + struct.pack(">h", 35))


if __name__ == "__main__":
    main()
