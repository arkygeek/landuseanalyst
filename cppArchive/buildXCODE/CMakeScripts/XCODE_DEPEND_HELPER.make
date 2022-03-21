# DO NOT EDIT
# This makefile makes sure all linkable targets are
# up-to-date with anything they link to, avoiding a bug in XCode 1.5
all.Debug: \
	/Users/arkygeek/devel/landuseanalyst/buildXCODE/src/lib/Debug/libla_core.dylib\
	/Users/arkygeek/devel/landuseanalyst/buildXCODE/src/gui/Debug/landuseanalyst.app/Contents/MacOS/landuseanalyst

all.Release: \
	/Users/arkygeek/devel/landuseanalyst/buildXCODE/src/lib/Release/libla_core.dylib\
	/Users/arkygeek/devel/landuseanalyst/buildXCODE/src/gui/Release/landuseanalyst.app/Contents/MacOS/landuseanalyst

all.MinSizeRel: \
	/Users/arkygeek/devel/landuseanalyst/buildXCODE/src/lib/MinSizeRel/libla_core.dylib\
	/Users/arkygeek/devel/landuseanalyst/buildXCODE/src/gui/MinSizeRel/landuseanalyst.app/Contents/MacOS/landuseanalyst

all.RelWithDebInfo: \
	/Users/arkygeek/devel/landuseanalyst/buildXCODE/src/lib/RelWithDebInfo/libla_core.dylib\
	/Users/arkygeek/devel/landuseanalyst/buildXCODE/src/gui/RelWithDebInfo/landuseanalyst.app/Contents/MacOS/landuseanalyst

# For each target create a dummy rule so the target does not have to exist
/usr/lib/libz.dylib:
/Users/arkygeek/devel/landuseanalyst/buildXCODE/src/lib/Debug/libla_core.dylib:
/Users/arkygeek/devel/landuseanalyst/buildXCODE/src/lib/MinSizeRel/libla_core.dylib:
/Users/arkygeek/devel/landuseanalyst/buildXCODE/src/lib/RelWithDebInfo/libla_core.dylib:
/Users/arkygeek/devel/landuseanalyst/buildXCODE/src/lib/Release/libla_core.dylib:


# Rules to remove targets that are older than anything to which they
# link.  This forces Xcode to relink the targets from scratch.  It
# does not seem to check these dependencies itself.
/Users/arkygeek/devel/landuseanalyst/buildXCODE/src/lib/Debug/libla_core.dylib:\
	/usr/lib/libz.dylib
	/bin/rm -f /Users/arkygeek/devel/landuseanalyst/buildXCODE/src/lib/Debug/libla_core.dylib
	/bin/rm -f /Users/arkygeek/devel/landuseanalyst/buildXCODE/src/lib/landuseanalyst.build/Debug/libla_core.dylib.build/Objects-normal/ppc/libla_core.dylib
	/bin/rm -f /Users/arkygeek/devel/landuseanalyst/buildXCODE/src/lib/landuseanalyst.build/Debug/libla_core.dylib.build/Objects-normal/i386/libla_core.dylib


/Users/arkygeek/devel/landuseanalyst/buildXCODE/src/gui/Debug/landuseanalyst.app/Contents/MacOS/landuseanalyst:\
	/usr/lib/libz.dylib\
	/Users/arkygeek/devel/landuseanalyst/buildXCODE/src/lib/Debug/libla_core.dylib\
	/usr/lib/libz.dylib
	/bin/rm -f /Users/arkygeek/devel/landuseanalyst/buildXCODE/src/gui/Debug/landuseanalyst.app/Contents/MacOS/landuseanalyst
	/bin/rm -f /Users/arkygeek/devel/landuseanalyst/buildXCODE/src/gui/landuseanalyst.build/Debug/landuseanalyst.build/Objects-normal/ppc/landuseanalyst
	/bin/rm -f /Users/arkygeek/devel/landuseanalyst/buildXCODE/src/gui/landuseanalyst.build/Debug/landuseanalyst.build/Objects-normal/i386/landuseanalyst


/Users/arkygeek/devel/landuseanalyst/buildXCODE/src/lib/Release/libla_core.dylib:\
	/usr/lib/libz.dylib
	/bin/rm -f /Users/arkygeek/devel/landuseanalyst/buildXCODE/src/lib/Release/libla_core.dylib
	/bin/rm -f /Users/arkygeek/devel/landuseanalyst/buildXCODE/src/lib/landuseanalyst.build/Release/libla_core.dylib.build/Objects-normal/ppc/libla_core.dylib
	/bin/rm -f /Users/arkygeek/devel/landuseanalyst/buildXCODE/src/lib/landuseanalyst.build/Release/libla_core.dylib.build/Objects-normal/i386/libla_core.dylib


/Users/arkygeek/devel/landuseanalyst/buildXCODE/src/gui/Release/landuseanalyst.app/Contents/MacOS/landuseanalyst:\
	/usr/lib/libz.dylib\
	/Users/arkygeek/devel/landuseanalyst/buildXCODE/src/lib/Release/libla_core.dylib\
	/usr/lib/libz.dylib
	/bin/rm -f /Users/arkygeek/devel/landuseanalyst/buildXCODE/src/gui/Release/landuseanalyst.app/Contents/MacOS/landuseanalyst
	/bin/rm -f /Users/arkygeek/devel/landuseanalyst/buildXCODE/src/gui/landuseanalyst.build/Release/landuseanalyst.build/Objects-normal/ppc/landuseanalyst
	/bin/rm -f /Users/arkygeek/devel/landuseanalyst/buildXCODE/src/gui/landuseanalyst.build/Release/landuseanalyst.build/Objects-normal/i386/landuseanalyst


/Users/arkygeek/devel/landuseanalyst/buildXCODE/src/lib/MinSizeRel/libla_core.dylib:\
	/usr/lib/libz.dylib
	/bin/rm -f /Users/arkygeek/devel/landuseanalyst/buildXCODE/src/lib/MinSizeRel/libla_core.dylib
	/bin/rm -f /Users/arkygeek/devel/landuseanalyst/buildXCODE/src/lib/landuseanalyst.build/MinSizeRel/libla_core.dylib.build/Objects-normal/ppc/libla_core.dylib
	/bin/rm -f /Users/arkygeek/devel/landuseanalyst/buildXCODE/src/lib/landuseanalyst.build/MinSizeRel/libla_core.dylib.build/Objects-normal/i386/libla_core.dylib


/Users/arkygeek/devel/landuseanalyst/buildXCODE/src/gui/MinSizeRel/landuseanalyst.app/Contents/MacOS/landuseanalyst:\
	/usr/lib/libz.dylib\
	/Users/arkygeek/devel/landuseanalyst/buildXCODE/src/lib/MinSizeRel/libla_core.dylib\
	/usr/lib/libz.dylib
	/bin/rm -f /Users/arkygeek/devel/landuseanalyst/buildXCODE/src/gui/MinSizeRel/landuseanalyst.app/Contents/MacOS/landuseanalyst
	/bin/rm -f /Users/arkygeek/devel/landuseanalyst/buildXCODE/src/gui/landuseanalyst.build/MinSizeRel/landuseanalyst.build/Objects-normal/ppc/landuseanalyst
	/bin/rm -f /Users/arkygeek/devel/landuseanalyst/buildXCODE/src/gui/landuseanalyst.build/MinSizeRel/landuseanalyst.build/Objects-normal/i386/landuseanalyst


/Users/arkygeek/devel/landuseanalyst/buildXCODE/src/lib/RelWithDebInfo/libla_core.dylib:\
	/usr/lib/libz.dylib
	/bin/rm -f /Users/arkygeek/devel/landuseanalyst/buildXCODE/src/lib/RelWithDebInfo/libla_core.dylib
	/bin/rm -f /Users/arkygeek/devel/landuseanalyst/buildXCODE/src/lib/landuseanalyst.build/RelWithDebInfo/libla_core.dylib.build/Objects-normal/ppc/libla_core.dylib
	/bin/rm -f /Users/arkygeek/devel/landuseanalyst/buildXCODE/src/lib/landuseanalyst.build/RelWithDebInfo/libla_core.dylib.build/Objects-normal/i386/libla_core.dylib


/Users/arkygeek/devel/landuseanalyst/buildXCODE/src/gui/RelWithDebInfo/landuseanalyst.app/Contents/MacOS/landuseanalyst:\
	/usr/lib/libz.dylib\
	/Users/arkygeek/devel/landuseanalyst/buildXCODE/src/lib/RelWithDebInfo/libla_core.dylib\
	/usr/lib/libz.dylib
	/bin/rm -f /Users/arkygeek/devel/landuseanalyst/buildXCODE/src/gui/RelWithDebInfo/landuseanalyst.app/Contents/MacOS/landuseanalyst
	/bin/rm -f /Users/arkygeek/devel/landuseanalyst/buildXCODE/src/gui/landuseanalyst.build/RelWithDebInfo/landuseanalyst.build/Objects-normal/ppc/landuseanalyst
	/bin/rm -f /Users/arkygeek/devel/landuseanalyst/buildXCODE/src/gui/landuseanalyst.build/RelWithDebInfo/landuseanalyst.build/Objects-normal/i386/landuseanalyst


