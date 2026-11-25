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
    supported_apis = [
    (18),
    ]
    message_size = 0
    correlation_id = data[8:12]
    api_version = int.from_bytes(data[6:8], "big")
    err_code = 0 if api_version <= 4 else 35
    api_keys = data[4:6]
    api_keys_len = len(supported_apis) + 1
    api_key_size = 0
    min_version = 0
    max_version = 4
    tag_buffer = data[23:23]
    throttle_time_ms = 0
    tag_buffer = 0
    # b = 1, h = 2, i = 4, q = 8
    body = (
        struct.pack(">h", err_code)
        + struct.pack(">b", api_keys_len)
        + api_keys
        + struct.pack(">h", min_version)
        + struct.pack(">h", max_version)
        + struct.pack(">b", tag_buffer)
        + struct.pack(">i", throttle_time_ms)
        + struct.pack(">b", tag_buffer)
    )

    payload = correlation_id + body
    response = struct.pack(">i", len(payload)) + payload
    conn.sendall(response)
    # print(data.hex())


if __name__ == "__main__":
    main()
