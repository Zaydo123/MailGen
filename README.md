# MailGen: Random Email Generator

## Overview
MailGen is a Python-based random email generator. It creates random email addresses by combining first names, last names, and domain names from predefined lists. The generator also includes options for adding numbers and special characters to the email addresses.

## Features
- Generate random email addresses
- Generate a list of random email addresses
- Save generated email addresses to a file
- Generate domain-specific email addresses
- Save domain-specific email addresses to a file

## How to Use
1. Prepare three text files: `first-names.txt`, `last-names.txt`, and `domains.txt`. Each file should contain a list of names or domains, one per line.
2. Instantiate the `MailGen` class.
3. Call the appropriate method to generate and retrieve or save email addresses.

## Example Usage
```python
mailgen = MailGen()
mailgen.generate_list_file(1000, "emails.txt")
mailgen.generate_list_file_domain_specific(1000, "gmail.com", "gmail.txt")
```
## Methods
- generate(): Generates a single random email address.
- generate_list(n): Generates a list of n random email addresses.
- generate_list_file(n, filename): Generates a list of n random email addresses and saves them to a file with the specified filename.
- generate_list_domain_specific(n, domain): Generates a list of n domain-specific email addresses.
- generate_list_file_domain_specific(n, domain, filename): Generates a list of n domain-specific email addresses and saves them to a file with the specified filename.

## Requirements
Python 3.x

## License
[MIT License](LICENSE.md)

[Learn more about the MIT License](https://license.md/licenses/mit-license/)