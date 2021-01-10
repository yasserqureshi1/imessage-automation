# Sending Texts using iMessage

Please note that these scripts will only work on Mac with iMessage enabled.

## Installation

Please ensure you have Python and pip installed. To install the dependencies needed for this project, use the command in Terminal or Command Prompt:
`pip install -r requirements.txt`

## Usage

The `main.py` script will need to be edited to contain the right reciever phone number, message and the path to the javascript file. The javascript file `send_message.js` will execute when you run the Python file with the details entered. Below are the variables that need to be set in the `main.py` script:

`PHONE_NUMBER` - This contains the phone number of the reciever
`MESSAGE` - This is the message that will be sent
`DIR_PATH` - This is the path to the location of the javascript file

To run the script, you can use the following command in Terminal or Command Prompt:
`python main.py`

Currently the script will send the message 100 times. The script can be editted and modified, but I am not responisible to the consequences of this script. Use this script at your own risk. 