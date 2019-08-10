"""
try:
    with open('myfile.txt') as fh:
        file_data = fh.read()
    print(file_data)
except FileNotFoundError:
    print('The File is missing')
except PermissionError:
    print('This is not allowed')
except:
    print('Some other error occurred')

"""

try:
    with open('myfile.txt') as fh:
        file_data = fh.read()
    print(file_data)
except FileNotFoundError:
    print('The File is missing')
except PermissionError:
    print('This is not allowed')
except Exception as err:
    print('Some other error occurred', str(err))

