# Blocking vs Non Blocking Sockets
# Blocking Stops
# Non Blocking runs in the background

"""
ready_to_read, ready_to_write, in_error =
select.select(potential_readers,potential_writers,potential_errs,timeout)
"""

import logging
import socket
import select

logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)


def create_blocking(host, ip):
    logging.info('Blocking - Creating Socket')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    logging.info('Blocking - connecting')
    s.connect((host, ip))
    logging.info('Blocking - connected')
    logging.info('Blocking - sending...')
    s.send(b'hello\r\n')

    logging.info('Blocking - waiting')
    data = s.recv(1024)
    logging.info(f'Blocking - data = {len(data)}')
    logging.info('Blocking - closing...')
    s.close()

def create_nonblocking(host,port):
    logging.info('Non blocking - creating socket')
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    logging.info('Non blocking - connecting')
    ret = s.connect_ex((host,port)) # Blocking
    if ret !=0:
        logging.info('Non Blocking - failed to connect')
        return

    logging.info('Non blocking - connected')
    s.setblocking(False)

    inputs = [s]
    outputs = [s]
    while inputs:
        logging.info('Non Blocking - waiting')
        readable,writable,errors = select.select(inputs,outputs,inputs,0.5)

        for s in writable:
            logging.info('Non Blocking - sending ...')
            data = s.send(b'hello\r\n')
            logging.info(f'Non Blocking - sent :{data}')
            outputs.remove(s)
        for s in readable:
            logging.info(f'Non Blocking - reading...')
            data = s.recv(1024)
            logging.info(f'Non Blocking - data:{len(data)}')
            logging.info(f'Non Blocking - closing...')
            s.close()
            inputs.remove(s)
            break
        for s in errors:
            logging.info(f'Non Blocking - error')
            inputs.remove(s)
            outputs.remove(s)
            break

def main():
    # create_blocking('voidrealms.com',80)
    create_nonblocking('voidrealms.com',80)


if __name__ == "__main__":
    main()
