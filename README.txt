Project Authors:

Jason Jorgenson
Tim Sutton


Build Notes (QMAKE):
-----------------------------------------------
export QTDIR=/usr/local/Trolltech/Qt-4.2.2/
export PATH=$QTDIR/bin/:$PATH
qmake
make


To Run:

LanduseAnalyst-release/bin/landuseanalyst-release

Build Notes (CMAKE)
-----------------------------------------------
mkdir build
cd build
cmake -D CMAKE_INSTALL_PREFIX=/home/timlinux/apps/ ..
make
make install
