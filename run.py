from application import app


def parse_command_line():
    """
    :return: None. Loads data into the API / evrythng , adds and updates it based on command-line input.
    """
    var = raw_input("Please enter something: ")

if __name__ == '__main__':
    # Start app
    app.run(threaded=True)