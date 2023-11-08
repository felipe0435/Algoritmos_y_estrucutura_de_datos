from os import system
"""
system("ls")
system("git clone https://github.com/intel/isa-l.git")
system("cd isa-l")
system("./autogen.sh")
system("./configure --prefix=/usr --libdir=/usr/lib64")
system("make")
system("sudo make install")
system("git clone https://github.com/ebiggers/libdeflate.git")
system("cd libdeflate")
system("cmake -B build")
system("cmake --build build")
system("cmake --install build")
# get source (you can also use browser to download from master or releases)
system("git clone https://github.com/OpenGene/fastp.git")

# build
system("cd fastp")
system("make")

# Install
system("sudo make install")
"""
# download the latest build
system("wget http://opengene.org/fastp/fastp")
system("chmod a+x ./fastp")

# or download specified version, i.e. fastp v0.23.4
"""system("wget http://opengene.org/fastp/fastp.0.23.4")
system("mv fastp.0.23.4 fastp")
system("chmod a+x ./fastp")"""