from app import app, socket_io

if __name__ == '__main__':
        socket_io.run(app, host='0.0.0.0')