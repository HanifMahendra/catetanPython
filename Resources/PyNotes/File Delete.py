import os
import shutil

path = "tenang aja filenya ga ada kok.txt" # Kalo beda folder, pake path yang lengkap

try:
    os.remove(path)     # Remove file
    os.rmdir(path)      # Remove empty directory (folder)
    shutil.rmtree(path) # Remove directory with all contents (DANGER!)
except FileNotFoundError:
    print("File Not Found Error!")
except PermissionError:
    print("You do not have the permission to delete that!")
except OSError:
    print("You cannot delete that using that function!")
else:
    print(f"{path} was deleted!")