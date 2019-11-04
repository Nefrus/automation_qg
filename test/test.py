import uiautomator2 as u2


def connect():
    # d = u2.connect("4fd2a842")  # connect to device
    d = u2.connect()  # connect to device 一台设备有线连接时，默认
    print(d.info)
    print(d.window_size())


if __name__ == "__main__":
    connect()
