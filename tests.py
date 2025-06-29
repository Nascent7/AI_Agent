from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

#def test_get_info():
    #result = get_files_info("calculator", ".")
    #print("Result for current directory:")
    #print(result)
    #rint("")

    #result = get_files_info("calculator", "pkg")
    #print("Result for 'pkg' directory:")
    #print(result)
    #print("")

    #result = get_files_info("calculator", "/bin")
    #print("Result for '/bin' directory:")
    #print(result)
    #print("")    

    #result = get_files_info("calculator", "../")
    #print("Result for '../' directory:")
    #print(result)
    #print("")
    
#if __name__ == "__main__":    
    #test_get_info()

'''
def test_get_content():
    result = get_file_content("calculator", "lorem.txt")
    print (result)

    result = get_file_content("calculator", "main.py")
    print (result)

    result = get_file_content("calculator", "pkg/calculator.py")
    print (result)

    result = get_file_content("calculator", "/bin/cat")
    print (result)
if __name__ == "__main__":
    test_get_content()
'''

'''
def test_write_file():
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(result)

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result)

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(result)

if __name__ == "__main__":
    test_write_file()
'''

def test_run_python_file():
    result = run_python_file("calculator", "main.py")
    print(result)

    result = run_python_file("calculator", "tests.py")
    print(result)

    result = run_python_file("calculator", "../main.py")
    print(result)

    result = run_python_file("calculator", "nonexistent.py")
    print(result)

if __name__ == "__main__":
    test_run_python_file()