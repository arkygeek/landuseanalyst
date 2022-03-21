/****************************************************************************
** Meta object code from reading C++ file 'lacropparametermanager.h'
**
** Created: Mon Mar 16 19:50:21 2009
**      by: The Qt Meta Object Compiler version 59 (Qt 4.4.3)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../../../src/gui/lacropparametermanager.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'lacropparametermanager.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 59
#error "This file was generated using the moc from 4.4.3. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_LaCropParameterManager[] = {

 // content:
       1,       // revision
       0,       // classname
       0,    0, // classinfo
       8,   10, // methods
       0,    0, // properties
       0,    0, // enums/sets

 // slots: signature, parameters, type, tag, flags
      41,   24,   23,   23, 0x08,
      71,   62,   23,   23, 0x08,
      95,   23,   23,   23, 0x08,
     115,   23,   23,   23, 0x08,
     137,   23,   23,   23, 0x08,
     158,   23,   23,   23, 0x08,
     182,   23,   23,   23, 0x08,
     204,   23,   23,   23, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_LaCropParameterManager[] = {
    "LaCropParameterManager\0\0theRow,theColumn\0"
    "cellClicked(int,int)\0theIndex\0"
    "on_cboCrop_changed(int)\0showCropParameter()\0"
    "on_toolCopy_clicked()\0on_toolNew_clicked()\0"
    "on_toolDelete_clicked()\0on_pbnApply_clicked()\0"
    "resizeEvent(QResizeEvent*)\0"
};

const QMetaObject LaCropParameterManager::staticMetaObject = {
    { &QDialog::staticMetaObject, qt_meta_stringdata_LaCropParameterManager,
      qt_meta_data_LaCropParameterManager, 0 }
};

const QMetaObject *LaCropParameterManager::metaObject() const
{
    return &staticMetaObject;
}

void *LaCropParameterManager::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_LaCropParameterManager))
        return static_cast<void*>(const_cast< LaCropParameterManager*>(this));
    return QDialog::qt_metacast(_clname);
}

int LaCropParameterManager::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QDialog::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: cellClicked((*reinterpret_cast< int(*)>(_a[1])),(*reinterpret_cast< int(*)>(_a[2]))); break;
        case 1: on_cboCrop_changed((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 2: showCropParameter(); break;
        case 3: on_toolCopy_clicked(); break;
        case 4: on_toolNew_clicked(); break;
        case 5: on_toolDelete_clicked(); break;
        case 6: on_pbnApply_clicked(); break;
        case 7: resizeEvent((*reinterpret_cast< QResizeEvent*(*)>(_a[1]))); break;
        }
        _id -= 8;
    }
    return _id;
}
QT_END_MOC_NAMESPACE
