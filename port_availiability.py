import logging
import socket

logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)


# Check one port

def check_port(ip, port, timeout):
    ret = False
    logging.debug(f'Checking {ip}:{port}')
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        con = s.connect_ex((ip, port))
        logging.debug(f'Connection {ip}:{port} ={con}')
        s.close()
        if con == 0:
            ret = False
            logging.debug(f'In use {ip}:{port}')
        else:
            ret = True
            logging.debug((f'Usable {ip}:{port}'))
    except Exception as ex:
        logging.debug(f'Error {ip}:{port} ={ex.msg}')
    finally:
        logging.debug(f'Returning {ip}:{port} = {ret}')
        return ret


def check_range(ip, scope):
    ret = {}
    for p in scope:
        r = check_port(ip, p, 1.0)
        ret[p] = r
    return ret


def main():
    p = check_port("localhost", 8085, 2.0)
    logging.info(f'Port 2594 usable :{p}')

    ports = check_range('localhost',range(3300,3309))
    for k,v in ports.items():
        logging.info(f'Port {k} usable {v}')


if __name__ == "__main__":
    main()
