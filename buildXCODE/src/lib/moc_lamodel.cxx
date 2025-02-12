/****************************************************************************
** Meta object code from reading C++ file 'lamodel.h'
**
** Created: Sun Mar 29 14:40:28 2009
**      by: The Qt Meta Object Compiler version 59 (Qt 4.4.3)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../../../src/lib/lamodel.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'lamodel.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 59
#error "This file was generated using the moc from 4.4.3. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_LaModel[] = {

 // content:
       1,       // revision
       0,       // classname
       0,    0, // classinfo
       1,   10, // methods
       0,    0, // properties
       0,    0, // enums/sets

 // signals: signature, parameters, type, tag, flags
      20,    9,    8,    8, 0x05,

       0        // eod
};

static const char qt_meta_stringdata_LaModel[] = {
    "LaModel\0\0theMessage\0message(QString)\0"
};

const QMetaObject LaModel::staticMetaObject = {
    { &QObject::staticMetaObject, qt_meta_stringdata_LaModel,
      qt_meta_data_LaModel, 0 }
};

const QMetaObject *LaModel::metaObject() const
{
    return &staticMetaObject;
}

void *LaModel::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_LaModel))
        return static_cast<void*>(const_cast< LaModel*>(this));
    if (!strcmp(_clname, "LaSerialisable"))
        return static_cast< LaSerialisable*>(const_cast< LaModel*>(this));
    if (!strcmp(_clname, "LaGuid"))
        return static_cast< LaGuid*>(const_cast< LaModel*>(this));
    return QObject::qt_metacast(_clname);
}

int LaModel::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: message((*reinterpret_cast< QString(*)>(_a[1]))); break;
        }
        _id -= 1;
    }
    return _id;
}

// SIGNAL 0
void LaModel::message(QString _t1)
{
    void *_a[] = { 0, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}
QT_END_MOC_NAMESPACE
