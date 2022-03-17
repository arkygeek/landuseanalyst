# Landuse Analyst

##  How we will collaborate

Please submit a pull request from your private branch to the developer branch.

## Project Authors

Jason Jorgenson
Tim Sutton

## Build Notes (QMAKE)

```BASH
export QTDIR=/usr/local/Trolltech/Qt-4.2.2/
export PATH=$QTDIR/bin/:$PATH
qmake
make
```

To Run:

```BASH
LanduseAnalyst-release/bin/landuseanalyst-release
```

Build Notes (CMAKE)

```BASH
mkdir build
cd build
cmake -D CMAKE_INSTALL_PREFIX=/home/timlinux/apps/ ..
make
make install
```

Making a kdevelop project with cmake

```BASH
mkdir build
cmake -G KDevelop3 -D CMAKE_INSTALL_PREFIX=/home/timlinux/apps/..
```

Then open the generated project using kdevelop
