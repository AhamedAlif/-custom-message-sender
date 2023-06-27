# Custom Message Sender

This is a custom message sender script that allows you to send custom messages to multiple recipients using an SMS API. It utilizes the `requests` library to send HTTP GET requests to the API endpoint.

## Prerequisites

- Python installed on your system. You can download it from the official Python website: https://www.python.org/downloads/
- The `requests` library. Install it using the following command:

    ```
    pip install requests
    ```

## How to Run

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Open the `custom_message_sender.py` file in a text editor.

4. Locate the `base_url` variable and replace it with the appropriate base URL of your SMS API.

5. Save the changes to the `custom_message_sender.py` file.

6. In the terminal or command prompt, run the following command:

    ```
    python custom_message_sender.py
    ```

7. The script will prompt you to enter the number of recipients you want to send messages to.

8. For each recipient, enter the mobile number and message as prompted by the script.

9. The script will construct the API URL with the provided details and send an HTTP GET request to the API endpoint.

10. The response status code will be checked to determine the success or failure of each SMS sent.

11. The script will provide feedback on the status of each SMS sent.

12. You can repeat the process to send messages to additional recipients.

Note: Make sure you comply with the terms and conditions of the SMS API provider and have the necessary permissions to send messages to the recipients.

