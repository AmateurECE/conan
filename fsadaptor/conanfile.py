from conans import ConanFile, CMake, tools
import shutil
import glob


class ConanFsadaptor(ConanFile):
    name = "fsadaptor"
    version = "0.1.2"
    license = "MIT"
    author = "Ethan D. Twardy <ethan.twardy@gmail.com>"
    url = "https://github.com/AmateurECE/conan"
    description = """An Object-Oriented Adaptor for the Standard C++ Library
    that performs filesystem operations."""
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake_find_package"

    def source(self):
        self.run("git clone https://github.com/AmateurECE/fsadaptor.git")
        self.run("git --git-dir=fsadaptor/.git --work-tree=fsadaptor checkout v{}"
                 .format(self.version))

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="fsadaptor", build_folder="build")
        cmake.build()
        cmake.test()

    def package(self):
        self.copy("*.h", dst="include/fsadaptor", src="fsadaptor/include")
        self.copy("*fsadaptor.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False, excludes=("*test*"))
        self.copy("*.so", dst="lib", keep_path=False, excludes=("*test*"))
        self.copy("*.dylib", dst="lib", keep_path=False, excludes=("*test*"))
        self.copy("*.a", dst="lib", keep_path=False, excludes=("*test*"))

    def package_info(self):
        self.cpp_info.libs = ["fsadaptor"]

