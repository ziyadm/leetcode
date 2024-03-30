# Mock Interview 03/29/24
# Design an in-memory file system to simulate the following functions: 
# create: Given a file path and value that does not exist, you should create that file containing given content. 
# If the middle directories in the path don‘t exist, you should create them as well, and assign empty string as the value. This function has a void return type.
# get: Given a file path, return its content in string format.
# listDir: Given a path in string format. Return the list of sub directory names in this dir

# Each file will have a path and associated contents in the form of a string

from collections import defaultdict

class InMemoryFileSystem:
    def __init__(self):
        self.paths_to_contents = defaultdict(None)
        
    def create(self, file_path: str, contents: str) -> None:
        sub_directories = file_path.split("/")       
        current_file_path = ""

        for index, sub_directory in enumerate(sub_directories):
            if index == 0:
                current_file_path += f"{sub_directory}"        
            else:
                current_file_path += f"/{sub_directory}"

            if current_file_path not in self.paths_to_contents:
                self.paths_to_contents[current_file_path] = ""
            if index == len(sub_directories) - 1:
                self.paths_to_contents[current_file_path] = contents

    def get(self, file_path: str) -> str:
        return self.paths_to_contents.get(file_path)

    #def listDir(self, file_path: str) -> List[str]:





testFileSystem = InMemoryFileSystem()

testFileSystem.create("desktop/documents/ziyad.py", "1 2 3 4 5")
assert("desktop/documents" in testFileSystem.paths_to_contents)
assert(testFileSystem.paths_to_contents["desktop/documents"] == "")
assert(testFileSystem.paths_to_contents["desktop/documents/ziyad.py"] == "1 2 3 4 5")
testFileSystem.create("desktop/documents/zain.py", "1 2 3 4 5")

assert(testFileSystem.paths_to_contents["desktop/documents/zain.py"] == "1 2 3 4 5")
assert(testFileSystem.get("desktop/documents/zain.py") == "1 2 3 4 5")

assert(testFileSystem.get("bspath") == None)
                

