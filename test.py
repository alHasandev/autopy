import internet


def ping():
    # Test internet connection
    print("connected" if internet.ping() else "no internet!")


def ip():
    print(internet.defaultGateway())  # Check default ip address gateway


def echo():
    print('test')
