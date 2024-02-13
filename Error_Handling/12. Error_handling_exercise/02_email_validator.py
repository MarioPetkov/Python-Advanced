import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


EMAIL_MIN_LENGTH = 5
VALID_DOMAINS = ['com', 'bg', 'net', 'org']

command = input()
while command != 'End':
    pattern = r'([A-Za-z0-9._%+-]*)(@*)([A-Za-z0-9._%+-]*)\.([a-zA-Z]*)'
    matches = re.findall(pattern, command)
    for match in matches:

        if len(match[0]) < EMAIL_MIN_LENGTH:
            raise NameTooShortError('Name must be more than 4 characters')

        if match[1] != '@':
            raise MustContainAtSymbolError('Email must contain @')

        if match[3] not in VALID_DOMAINS:
            raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')

    print('Email is valid')
    command = input()

