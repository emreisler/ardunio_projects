from kivy.clock import mainthread
import threading
import jnius

def get_socket_stream(self, name):
    paired_devices =  self.BluetoothAdapter.getDefaultAdapter().getBondedDevices().toArray()
    socket = None
    for device in paired_devices:
        if device.getName() == name:
            socket = device.createRfcommSocketToServiceRecord(
            self.UUID.fromString("00001101-0000-1000-8000-00805F9B34FB"))
            reader = self.InputStreamReader(socket.getInputStream(), 'US-ASCII')
            recv_stream = self.BufferedReader(reader)
            send_stream = socket.getOutputStream()
            break
    socket.connect()
    return recv_stream, send_stream

def connect(self, *args):
    device = self.config.get('bluetooth', 'bt_name')
    try:
        self.recv_stream, self.send_stream = self.get_socket_stream(device)
    except AttributeError as e:
        print e.message
        return False
    except jnius.JavaException as e:
        print e.message
        return False
    except:
        print sys.exc_info()[0]
        return False

    threading.Thread(target=self.stream_reader).start()
