from conan import ConanFile
class T(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    generators = "CMakeDeps" , "CMakeToolchain"

    def requirements(self):
        self.requires("uwebsockets/20.57.0")