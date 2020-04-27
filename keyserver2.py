import asyncio
import ssl
import socket
import json

import keyring
import pymysql
from ecies import encrypt, decrypt
from binascii import b2a_hex, a2b_hex
db = pymysql.connect("localhost", "root", "123456", "shamir_key_two")
cursor = db.cursor()

async def handle_request(reader, writer):
    data = await reader.read(1024)
    addr = writer.get_extra_info('peername')
    print(f"Received task from {addr!r}")
    msg = json.loads(data.decode())
    print(msg)
    send_msg = {'status': 'no'}
    productId = msg['productId']
    public =msg['public']
    sql = "SELECT * FROM apps_key_db_two WHERE productId = %s" % (int(productId))
    cursor.execute(sql)
    data = cursor.fetchone()
    encrypt_key = b2a_hex(encrypt(public, decrypt(keyring.get_password("DRMDEMO", "keyManagerTwoPrivate"), a2b_hex(data[2])))).decode()
    print(encrypt_key)
    send_msg['status'] ='ok'
    send_msg['key'] = encrypt_key
    send_data = json.dumps(send_msg)

    writer.write(send_data.encode())
    await writer.drain()

    print(f"finsh {addr!r} work")
    writer.close()


async def main(sock, context):
    server = await asyncio.start_server(
        handle_request, sock=sock, ssl=context)

    print(f'Serving on {server.sockets}')

    async with server:
        await server.serve_forever()

# def main_run():
if __name__ == '__main__':
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    server_sock.bind(('127.0.0.1', 7778))
    server_sock.listen(5)
    server_sock.setblocking(False)
    CA_FILE ="ca.crt"
    KEY_FILE = "client.key"
    CERT_FILE = "client.crt"
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)
    context.load_verify_locations(CA_FILE)
    context.verify_mode = ssl.CERT_REQUIRED
    asyncio.run(main(server_sock, context))
