import socket  # noqa: F401
import struck

def main():
    # You can use print statements as follows for debugging,
    # they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # TODO: Uncomment the code below to pass the first stage
    server = socket.create_server(("localhost", 9092), reuse_port=True)
    conn, _ = server.accept()
    conn.recv(256)
    conn.sendall(struct.pack(">ii", 0, 7))


if __name__ == "__main__":
    main()
