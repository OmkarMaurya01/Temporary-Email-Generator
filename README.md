# Temporary Email Generator

This Python project generates temporary email addresses using the `MailTM` service and retrieves verification links or OTPs sent to the generated email. It is helpful for website registration or verification without exposing your personal email address.

## Features

- **Generate Temporary Email**: Automatically creates a random temporary email address.
- **Receive Verification Emails**: Retrieves verification links or OTPs sent to the temporary email address.
- **Disposable**: The generated email addresses are disposable and can be discarded after use.

## Requirements

- Python 3.x
- `mailtm` (for creating temporary email addresses)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/temporary-email-generator.git
    ```

2. Navigate to the project directory:

    ```bash
    cd temporary-email-generator
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:

    ```bash
    python temp_email_generator.py
    ```

2. The script will generate a random temporary email address and print it on the screen. You can use this email for website registrations or verifications.

3. Once an email is received with the verification link or OTP, the script will display the link.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Python’s `mailtm` library for generating temporary emails.
