from conans import ConanFile, CMake

class PlumaConan(ConanFile):
    name = "Pluma"
    version = "1.1"
    url = "https://github.com/monsdar/pluma-cmake"
    license = "GNU LESSER GENERAL PUBLIC LICENSE Version 3"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports = "*"

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake %s %s' % (self.conanfile_directory, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.hpp", dst="include/Pluma", src="Pluma-1.1/include/Pluma")
        self.copy("*.inl", dst="include/Pluma", src="Pluma-1.1/include/Pluma")
        self.copy("*.lib", dst="lib", src="Release")
        self.copy("*.a", dst="lib", src="Release")

    def package_info(self):
        self.cpp_info.libs = ["Pluma"]
        