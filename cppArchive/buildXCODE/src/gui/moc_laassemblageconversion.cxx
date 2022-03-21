/****************************************************************************
** Meta object code from reading C++ file 'laassemblageconversion.h'
**
** Created: Mon Mar 16 19:50:21 2009
**      by: The Qt Meta Object Compiler version 59 (Qt 4.4.3)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../../../src/gui/laassemblageconversion.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'laassemblageconversion.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 59
#error "This file was generated using the moc from 4.4.3. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_LaAssemblageConversion[] = {

 // content:
       1,       // revision
       0,       // classname
       0,    0, // classinfo
       5,   10, // methods
       0,    0, // properties
       0,    0, // enums/sets

 // slots: signature, parameters, type, tag, flags
      24,   23,   23,   23, 0x0a,
      47,   23,   23,   23, 0x0a,
      73,   23,   23,   23, 0x0a,
     100,   23,   23,   23, 0x0a,
     121,   23,   23,   23, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_LaAssemblageConversion[] = {
    "LaAssemblageConversion\0\0on_pbnInsert_clicked()\0"
    "on_pbnCalculate_clicked()\0"
    "on_pbnClearTable_clicked()\0"
    "on_pbnSave_clicked()\0resizeEvent(QResizeEvent*)\0"
};

const QMetaObject LaAssemblageConversion::staticMetaObject = {
    { &QDialog::staticMetaObject, qt_meta_stringdata_LaAssemblageConversion,
      qt_meta_data_LaAssemblageConversion, 0 }
};

const QMetaObject *LaAssemblageConversion::metaObject() const
{
    return &staticMetaObject;
}

void *LaAssemblageConversion::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_LaAssemblageConversion))
        return static_cast<void*>(const_cast< LaAssemblageConversion*>(this));
    return QDialog::qt_metacast(_clname);
}

int LaAssemblageConversion::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QDialog::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: on_pbnInsert_clicked(); break;
        case 1: on_pbnCalculate_clicked(); break;
        case 2: on_pbnClearTable_clicked(); break;
        case 3: on_pbnSave_clicked(); break;
        case 4: resizeEvent((*reinterpret_cast< QResizeEvent*(*)>(_a[1]))); break;
        }
        _id -= 5;
    }
    return _id;
}
QT_END_MOC_NAMESPACE
