/****************************************************************************
** Meta object code from reading C++ file 'lacropmanager.h'
**
** Created: Mon Mar 16 19:50:21 2009
**      by: The Qt Meta Object Compiler version 59 (Qt 4.4.3)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../../../src/gui/lacropmanager.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'lacropmanager.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 59
#error "This file was generated using the moc from 4.4.3. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_LaCropManager[] = {

 // content:
       1,       // revision
       0,       // classname
       0,    0, // classinfo
      10,   10, // methods
       0,    0, // properties
       0,    0, // enums/sets

 // slots: signature, parameters, type, tag, flags
      15,   14,   14,   14, 0x0a,
      43,   14,   14,   14, 0x0a,
      71,   14,   14,   14, 0x0a,
     112,   95,   14,   14, 0x08,
     133,   14,   14,   14, 0x08,
     144,   14,   14,   14, 0x08,
     166,   14,   14,   14, 0x08,
     187,   14,   14,   14, 0x08,
     211,   14,   14,   14, 0x08,
     233,   14,   14,   14, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_LaCropManager[] = {
    "LaCropManager\0\0on_pushButtonLoad_clicked()\0"
    "on_pushButtonSave_clicked()\0"
    "on_pbnCropPic_clicked()\0theRow,theColumn\0"
    "cellClicked(int,int)\0showCrop()\0"
    "on_toolCopy_clicked()\0on_toolNew_clicked()\0"
    "on_toolDelete_clicked()\0on_pbnApply_clicked()\0"
    "resizeEvent(QResizeEvent*)\0"
};

const QMetaObject LaCropManager::staticMetaObject = {
    { &QDialog::staticMetaObject, qt_meta_stringdata_LaCropManager,
      qt_meta_data_LaCropManager, 0 }
};

const QMetaObject *LaCropManager::metaObject() const
{
    return &staticMetaObject;
}

void *LaCropManager::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_LaCropManager))
        return static_cast<void*>(const_cast< LaCropManager*>(this));
    return QDialog::qt_metacast(_clname);
}

int LaCropManager::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QDialog::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: on_pushButtonLoad_clicked(); break;
        case 1: on_pushButtonSave_clicked(); break;
        case 2: on_pbnCropPic_clicked(); break;
        case 3: cellClicked((*reinterpret_cast< int(*)>(_a[1])),(*reinterpret_cast< int(*)>(_a[2]))); break;
        case 4: showCrop(); break;
        case 5: on_toolCopy_clicked(); break;
        case 6: on_toolNew_clicked(); break;
        case 7: on_toolDelete_clicked(); break;
        case 8: on_pbnApply_clicked(); break;
        case 9: resizeEvent((*reinterpret_cast< QResizeEvent*(*)>(_a[1]))); break;
        }
        _id -= 10;
    }
    return _id;
}
QT_END_MOC_NAMESPACE
