# Python Server Checker

A simple script to create IPv4 sockets, in order to establish a connection and see if the address is online.

## Usage

To use this script you will need `python3`

A virtual environment is recommended for testing this script. You can use `venv` of `pipenv`.

Once you have created the virtual environment, install the packages specified in the "requirements.txt" file, using:

```bash
python -m pip install -r requirements.txt

# or

pipenv install -r requirements.txt
```

Finally, you can run the script with:

```bash
python server_checker.py google.com
```
