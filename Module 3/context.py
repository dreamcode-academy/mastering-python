
import tempfile
import shutil

class TemporaryDirectoryManager:
    def __enter__(self):

        self.temp_dir = tempfile.mkdtemp()

        return self.temp_dir
    
    def __exit__(self, exc_type, exc_value, traceback):

        shutil.rmtree(self.temp_dir)

with TemporaryDirectoryManager() as tmp_dir:
    print(tmp_dir)
    f = open(f"{tmp_dir}/test.txt", "w")
    f.write("Test content") 
    f.close()
    
    print("Temporary file created")

