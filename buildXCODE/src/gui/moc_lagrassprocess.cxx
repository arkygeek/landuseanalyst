/****************************************************************************
** Meta object code from reading C++ file 'lagrassprocess.h'
**
** Created: Mon Mar 30 14:30:51 2009
**      by: The Qt Meta Object Compiler version 59 (Qt 4.4.3)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../../../src/gui/lagrassprocess.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'lagrassprocess.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 59
#error "This file was generated using the moc from 4.4.3. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_LaGrassProcess[] = {

 // content:
       1,       // revision
       0,       // classname
       0,    0, // classinfo
      12,   10, // methods
       0,    0, // properties
       0,    0, // enums/sets

 // slots: signature, parameters, type, tag, flags
      16,   15,   15,   15, 0x0a,
      35,   25,   15,   15, 0x0a,
      70,   59,   15,   15, 0x0a,
     103,   95,   15,   15, 0x0a,
     138,  130,   15,   15, 0x0a,
     181,  165,   15,   15, 0x0a,
     223,  208,   15,   15, 0x0a,
     261,  246,   15,   15, 0x0a,
     294,  284,   15,   15, 0x0a,
     364,  328,  322,   15, 0x0a,
     461,  408,  398,   15, 0x0a,
     534,  498,  490,   15, 0x0a,

       0        // eod
};

static const char qt_meta_stringdata_LaGrassProcess[] = {
    "LaGrassProcess\0\0accept()\0theTarget\0"
    "setPbarTargetRange(int)\0theOverall\0"
    "setPbarOverallRange(int)\0theArea\0"
    "updateCurrentProgress(int)\0theStep\0"
    "updateOverallProgress(int)\0theGrassMessage\0"
    "writeGrassMessage(QString)\0thePreviewFile\0"
    "updatePreview(QString)\0theGraphicFile\0"
    "updateGraphic(QString)\0theStatus\0"
    "toggleBusyProgressBar(bool)\0float\0"
    "theItem,theRasterMask,theAreaTarget\0"
    "analyseModel(QString,QString,int)\0"
    "LandFound\0"
    "theCurrentlyContainedArea,theAreaTarget,thePrecision\0"
    "getSearchStatus(int,int,int)\0QString\0"
    "theItemName,theExtent,theAreaTarget\0"
    "generateFilename(QString,float,int)\0"
};

const QMetaObject LaGrassProcess::staticMetaObject = {
    { &QDialog::staticMetaObject, qt_meta_stringdata_LaGrassProcess,
      qt_meta_data_LaGrassProcess, 0 }
};

const QMetaObject *LaGrassProcess::metaObject() const
{
    return &staticMetaObject;
}

void *LaGrassProcess::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_LaGrassProcess))
        return static_cast<void*>(const_cast< LaGrassProcess*>(this));
    return QDialog::qt_metacast(_clname);
}

int LaGrassProcess::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QDialog::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: accept(); break;
        case 1: setPbarTargetRange((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 2: setPbarOverallRange((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 3: updateCurrentProgress((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 4: updateOverallProgress((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 5: writeGrassMessage((*reinterpret_cast< QString(*)>(_a[1]))); break;
        case 6: updatePreview((*reinterpret_cast< QString(*)>(_a[1]))); break;
        case 7: updateGraphic((*reinterpret_cast< QString(*)>(_a[1]))); break;
        case 8: toggleBusyProgressBar((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 9: { float _r = analyseModel((*reinterpret_cast< QString(*)>(_a[1])),(*reinterpret_cast< QString(*)>(_a[2])),(*reinterpret_cast< int(*)>(_a[3])));
            if (_a[0]) *reinterpret_cast< float*>(_a[0]) = _r; }  break;
        case 10: { LandFound _r = getSearchStatus((*reinterpret_cast< int(*)>(_a[1])),(*reinterpret_cast< int(*)>(_a[2])),(*reinterpret_cast< int(*)>(_a[3])));
            if (_a[0]) *reinterpret_cast< LandFound*>(_a[0]) = _r; }  break;
        case 11: { QString _r = generateFilename((*reinterpret_cast< QString(*)>(_a[1])),(*reinterpret_cast< float(*)>(_a[2])),(*reinterpret_cast< int(*)>(_a[3])));
            if (_a[0]) *reinterpret_cast< QString*>(_a[0]) = _r; }  break;
        }
        _id -= 12;
    }
    return _id;
}
QT_END_MOC_NAMESPACE
