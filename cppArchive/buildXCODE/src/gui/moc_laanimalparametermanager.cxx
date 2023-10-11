/****************************************************************************
** Meta object code from reading C++ file 'laanimalparametermanager.h'
**
** Created: Mon Mar 16 19:50:21 2009
**      by: The Qt Meta Object Compiler version 59 (Qt 4.4.3)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../../../src/gui/laanimalparametermanager.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'laanimalparametermanager.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 59
#error "This file was generated using the moc from 4.4.3. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_LaAnimalParameterManager[] = {

 // content:
       1,       // revision
       0,       // classname
       0,    0, // classinfo
      10,   10, // methods
       0,    0, // properties
       0,    0, // enums/sets

 // slots: signature, parameters, type, tag, flags
      46,   26,   25,   25, 0x0a,
      96,   79,   25,   25, 0x08,
     126,  117,   25,   25, 0x08,
     152,   25,   25,   25, 0x08,
     174,   25,   25,   25, 0x08,
     196,   25,   25,   25, 0x08,
     217,   25,   25,   25, 0x08,
     241,   25,   25,   25, 0x08,
     263,   25,   25,   25, 0x08,
     284,   25,   25,   25, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_LaAnimalParameterManager[] = {
    "LaAnimalParameterManager\0\0theSelectedCropsMap\0"
    "setSelectedCropsMap(LaTripleMap)\0"
    "theRow,theColumn\0cellClicked(int,int)\0"
    "theValue\0on_cboAnimal_changed(int)\0"
    "showAnimalParameter()\0on_toolCopy_clicked()\0"
    "on_toolNew_clicked()\0on_toolDelete_clicked()\0"
    "on_pbnApply_clicked()\0on_pbnMore_clicked()\0"
    "resizeEvent(QResizeEvent*)\0"
};

const QMetaObject LaAnimalParameterManager::staticMetaObject = {
    { &QDialog::staticMetaObject, qt_meta_stringdata_LaAnimalParameterManager,
      qt_meta_data_LaAnimalParameterManager, 0 }
};

const QMetaObject *LaAnimalParameterManager::metaObject() const
{
    return &staticMetaObject;
}

void *LaAnimalParameterManager::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_LaAnimalParameterManager))
        return static_cast<void*>(const_cast< LaAnimalParameterManager*>(this));
    return QDialog::qt_metacast(_clname);
}

int LaAnimalParameterManager::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QDialog::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: setSelectedCropsMap((*reinterpret_cast< LaTripleMap(*)>(_a[1]))); break;
        case 1: cellClicked((*reinterpret_cast< int(*)>(_a[1])),(*reinterpret_cast< int(*)>(_a[2]))); break;
        case 2: on_cboAnimal_changed((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 3: showAnimalParameter(); break;
        case 4: on_toolCopy_clicked(); break;
        case 5: on_toolNew_clicked(); break;
        case 6: on_toolDelete_clicked(); break;
        case 7: on_pbnApply_clicked(); break;
        case 8: on_pbnMore_clicked(); break;
        case 9: resizeEvent((*reinterpret_cast< QResizeEvent*(*)>(_a[1]))); break;
        }
        _id -= 10;
    }
    return _id;
}
QT_END_MOC_NAMESPACE
