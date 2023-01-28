import logging
import socket

logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)


# TCP Server
def server(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (ip, port)
    s.bind(address)
    logging.info('Listening')
    s.listen(1)
    con, addr = s.accept()
    logging.info(f'Connected:{addr}')
    while True:
        data = con.recv(1024)
        if len(data) == 0:
            logging.info(f'Exiting')
            con.close()
            break
        logging.info(f'Data:{data}')
    logging.info('Closing the server')
    s.close()


if __name__ == "__main__":
    server("localhost", 7000)
