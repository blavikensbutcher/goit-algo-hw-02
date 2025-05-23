import datetime
from queue import Queue

queue = Queue()


def generate_request():
    zayavka = f'New zayavka: {datetime.datetime.timestamp(datetime.datetime.now())}'
    queue.put(zayavka)
    print(f'Generated: {zayavka}')


def process_request():
    if not queue.empty():
        zayavka = queue.get()
        print(f'Processed: {zayavka}')
    else:
        print('Yaay, Queue is empty!')


if __name__ == '__main__':
    try:
        while True:
            generate_request()
            process_request()
    except KeyboardInterrupt:
        print('Wow you exit that program')

