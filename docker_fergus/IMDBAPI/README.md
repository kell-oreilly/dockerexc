# Flask Demo



Then, set up your environment using either of the following methods (using the CLI or with PyCharm).

### CLI
In the terminal, run the following commands.
```shell
# Navigate to the project folder
cd dockerPython
# Create and activate a virtual environment:
python -m venv venv
./venv/Scripts/activate
# Install dependencies:
pip install -r requirements.txt
# To leave the virtual environment:
deactivate
```

### PyCharm

After cloning the code:

- Open PyCharm
- Select `File` > `Open...`
- Navigate to the cloned project folder and click `Open`
- PyCharm should automatically detect that the project has dependencies.
  - Keep the default values and click "OK"

## Running the API
If you're not already in the virtual environment, run `./venv/Scripts/activate`.
Run `deactivate` to leave the virtual environment when you're done.

To start the server, run **ONE** of the following in the Terminal:

```shell
flask run
python -m flask run
python app.py
```

### Note:
By default, the application will run in production mode. To use development or testing configurations, set the `ENV` environment to `DEV` or `TEST` respectively. This can be done through the command line, or in your PyCharm Run/Debug Configurations menu.
