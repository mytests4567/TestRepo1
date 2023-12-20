print("Hello World2", password)

def read_file_noncompliant(filename):
    file = open(filename, 'r')
    # Noncompliant: method returns without properly closing the file.
    return file.readlines()

def read_file_noncompliant1(filename):
    file = open(filename, 'r')
    # Noncompliant: method returns without properly closing the file.
    return file.readlines()


def read_file_noncompliant2(filename):
    file = open(filename, 'r')
    # Noncompliant: method returns without properly closing the file.
    return file.readlines()
