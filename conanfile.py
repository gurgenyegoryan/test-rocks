import os

from conan import ConanFile
from conan.errors import ConanInvalidConfiguration
from conan.tools.build import check_min_cppstd, cross_building
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout
from conan.tools.files import apply_conandata_patches, copy, export_conandata_patches, get, rmdir
from conan.tools.microsoft import is_msvc, is_msvc_static_runtime
from conan.tools.scm import Version


# class ConanUStore(ConanFile):
#     exports = 'VERSION', 'LICENSE', 'README.md'
#     exports_sources = 'CMakeLists.txt', 'src/*', 'include/*', 'cmake/*', 'VERSION'
    name = 'ustore_deps'
    version = "0.1.1"

    # Complete list of possible settings:
    # https://docs.conan.io/en/latest/extending/custom_settings.html
    settings = {
        # https://docs.conan.io/en/latest/introduction.html#all-platforms-all-build-systems-and-compilers
        'os': ['Linux'],
        # https://docs.conan.io/en/latest/integrations/compilers.html
        'compiler': [
            'gcc', 'clang', 'intel',
            # Not fully supported yet:
            # 'intel-cc'
        ],
        # https://github.com/conan-io/conan/issues/2500
        'build_type': ['Release'],
        'arch': ['x86', 'x86_64', 'armv8', 'armv8_32', 'armv8.3'],
    }
    generators = 'CMakeDeps', 'deploy'
    options = {'with_arrow': [True, False]}
    default_options = {
        'with_arrow': False,
    }

    def layout(self):
        cmake_layout(self)

    def generate(self):
      pass

    def configure(self):
      self.options["rocksdb"].shared = False
      self.options["rocksdb"].fPIC = True
      self.options["rocksdb"].use_rtti = True

    def requirements(self):
      self.requires('rocksdb/6.29.5')

    def build(self):
      pass


    def package(self):
        self.copy(pattern="*.a", dst="lib", keep_path=False)
        self.copy(pattern="*.h", dst="lib", keep_path=False)
        self.copy(pattern="*.hpp", dst="lib", keep_path=False)
