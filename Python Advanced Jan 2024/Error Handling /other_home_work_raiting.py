class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


while True:
    email = input()
    if email == "End":
        break

    try:
        at_index = email.index("@")
    except ValueError:
        raise MustContainAtSymbolError("Email must contain @")

    if len(email[:at_index]) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    dot_index = email.index(".") + 1

    if email[dot_index:] not in ["com", "bg", "org", "net"]:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
