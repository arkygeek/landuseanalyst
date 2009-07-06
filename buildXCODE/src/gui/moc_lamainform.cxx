/****************************************************************************
** Meta object code from reading C++ file 'lamainform.h'
**
** Created: Mon Mar 23 07:01:50 2009
**      by: The Qt Meta Object Compiler version 59 (Qt 4.4.3)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../../../src/gui/lamainform.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'lamainform.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 59
#error "This file was generated using the moc from 4.4.3. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_LaMainForm[] = {

 // content:
       1,       // revision
       0,       // classname
       0,    0, // classinfo
      39,   10, // methods
       0,    0, // properties
       0,    0, // enums/sets

 // slots: signature, parameters, type, tag, flags
      47,   19,   12,   11, 0x0a,
      97,   88,   11,   11, 0x0a,
     137,  129,   11,   11, 0x0a,
     171,  129,   11,   11, 0x0a,
     203,  129,   11,   11, 0x0a,
     237,   88,   11,   11, 0x0a,
     278,   88,   11,   11, 0x0a,
     310,   88,   11,   11, 0x0a,
     350,   88,   11,   11, 0x0a,
     404,   11,  382,   11, 0x0a,
     438,   11,  423,   11, 0x0a,
     471,   11,  459,   11, 0x0a,
     511,  499,  491,   11, 0x0a,
     563,  549,  491,   11, 0x0a,
     603,   11,  491,   11, 0x0a,
     612,   11,   11,   11, 0x0a,
     639,   11,   11,   11, 0x0a,
     667,   11,   11,   11, 0x0a,
     695,   11,   11,   11, 0x0a,
     719,   11,   11,   11, 0x0a,
     745,   11,   11,   11, 0x0a,
     778,   11,   11,   11, 0x0a,
     813,   88,   11,   11, 0x0a,
     850,   11,   11,   11, 0x0a,
     873,   11,   11,   11, 0x0a,
     894,   11,   11,   11, 0x0a,
     929,   11,   11,   11, 0x0a,
     943,   11,   11,   11, 0x0a,
     955,   11,   11,   11, 0x0a,
     981,  971,   11,   11, 0x0a,
    1001,   11,   11,   11, 0x0a,
    1040, 1012,   11,   11, 0x08,
    1099, 1091,   11,   11, 0x08,
    1121, 1012,   11,   11, 0x08,
    1172, 1012,   11,   11, 0x08,
    1242, 1225,   11,   11, 0x08,
    1269, 1225,   11,   11, 0x08,
    1305, 1225,   11,   11, 0x08,
    1330, 1225,   11,   11, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_LaMainForm[] = {
    "LaMainForm\0\0double\0theDaysToGain,theGainPerDay\0"
    "totalWeightFromLinearGrowth(float,float)\0"
    "theValue\0on_sliderMeat_valueChanged(int)\0"
    "theBool\0on_cboxIncludeDairy_clicked(bool)\0"
    "on_cboxLimitDairy_clicked(bool)\0"
    "on_cboxBaseOnPlants_clicked(bool)\0"
    "on_sbLimitDairyPercent_valueChanged(int)\0"
    "on_sliderDiet_valueChanged(int)\0"
    "on_sbDairyUtilisation_valueChanged(int)\0"
    "on_sliderCrop_valueChanged(int)\0"
    "QMap<QString,QString>\0getSelectedCrops()\0"
    "QPair<int,int>\0getSiteCoordinates()\0"
    "LaTripleMap\0getAvailableCrops()\0QString\0"
    "theCropGuid\0getMatchingCropParameterGuid(QString)\0"
    "theAnimalGuid\0getMatchingAnimalParameterGuid(QString)\0"
    "getDEM()\0on_pushButtonRun_clicked()\0"
    "on_pushButtonLoad_clicked()\0"
    "on_pushButtonSave_clicked()\0"
    "on_pbnNewCrop_clicked()\0"
    "on_pbnNewAnimal_clicked()\0"
    "on_pbnNewCropParameter_clicked()\0"
    "on_pbnNewAnimalParameter_clicked()\0"
    "on_sbDailyCalories_valueChanged(int)\0"
    "on_pbnFallow_clicked()\0on_cbDebug_clicked()\0"
    "on_cboMapSet_currentIndexChanged()\0"
    "loadAnimals()\0loadCrops()\0setDietLabels()\0"
    "theString\0logMessage(QString)\0setModel()\0"
    "thepCurrentItem,thepOldItem\0"
    "helpItemClicked(QTreeWidgetItem*,QTreeWidgetItem*)\0"
    "theText\0writeResults(QString)\0"
    "cropCalcClicked(QListWidgetItem*,QListWidgetItem*)\0"
    "animalCalcClicked(QListWidgetItem*,QListWidgetItem*)\0"
    "theRow,theColumn\0animalCellClicked(int,int)\0"
    "animalCalcSelectionChanged(int,int)\0"
    "cropCellClicked(int,int)\0"
    "cropCalcSelectionChanged(int,int)\0"
};

const QMetaObject LaMainForm::staticMetaObject = {
    { &QDialog::staticMetaObject, qt_meta_stringdata_LaMainForm,
      qt_meta_data_LaMainForm, 0 }
};

const QMetaObject *LaMainForm::metaObject() const
{
    return &staticMetaObject;
}

void *LaMainForm::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_LaMainForm))
        return static_cast<void*>(const_cast< LaMainForm*>(this));
    return QDialog::qt_metacast(_clname);
}

int LaMainForm::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QDialog::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: { double _r = totalWeightFromLinearGrowth((*reinterpret_cast< float(*)>(_a[1])),(*reinterpret_cast< float(*)>(_a[2])));
            if (_a[0]) *reinterpret_cast< double*>(_a[0]) = _r; }  break;
        case 1: on_sliderMeat_valueChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 2: on_cboxIncludeDairy_clicked((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 3: on_cboxLimitDairy_clicked((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 4: on_cboxBaseOnPlants_clicked((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 5: on_sbLimitDairyPercent_valueChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 6: on_sliderDiet_valueChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 7: on_sbDairyUtilisation_valueChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 8: on_sliderCrop_valueChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 9: { QMap<QString,QString> _r = getSelectedCrops();
            if (_a[0]) *reinterpret_cast< QMap<QString,QString>*>(_a[0]) = _r; }  break;
        case 10: { QPair<int,int> _r = getSiteCoordinates();
            if (_a[0]) *reinterpret_cast< QPair<int,int>*>(_a[0]) = _r; }  break;
        case 11: { LaTripleMap _r = getAvailableCrops();
            if (_a[0]) *reinterpret_cast< LaTripleMap*>(_a[0]) = _r; }  break;
        case 12: { QString _r = getMatchingCropParameterGuid((*reinterpret_cast< QString(*)>(_a[1])));
            if (_a[0]) *reinterpret_cast< QString*>(_a[0]) = _r; }  break;
        case 13: { QString _r = getMatchingAnimalParameterGuid((*reinterpret_cast< QString(*)>(_a[1])));
            if (_a[0]) *reinterpret_cast< QString*>(_a[0]) = _r; }  break;
        case 14: { QString _r = getDEM();
            if (_a[0]) *reinterpret_cast< QString*>(_a[0]) = _r; }  break;
        case 15: on_pushButtonRun_clicked(); break;
        case 16: on_pushButtonLoad_clicked(); break;
        case 17: on_pushButtonSave_clicked(); break;
        case 18: on_pbnNewCrop_clicked(); break;
        case 19: on_pbnNewAnimal_clicked(); break;
        case 20: on_pbnNewCropParameter_clicked(); break;
        case 21: on_pbnNewAnimalParameter_clicked(); break;
        case 22: on_sbDailyCalories_valueChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 23: on_pbnFallow_clicked(); break;
        case 24: on_cbDebug_clicked(); break;
        case 25: on_cboMapSet_currentIndexChanged(); break;
        case 26: loadAnimals(); break;
        case 27: loadCrops(); break;
        case 28: setDietLabels(); break;
        case 29: logMessage((*reinterpret_cast< QString(*)>(_a[1]))); break;
        case 30: setModel(); break;
        case 31: helpItemClicked((*reinterpret_cast< QTreeWidgetItem*(*)>(_a[1])),(*reinterpret_cast< QTreeWidgetItem*(*)>(_a[2]))); break;
        case 32: writeResults((*reinterpret_cast< QString(*)>(_a[1]))); break;
        case 33: cropCalcClicked((*reinterpret_cast< QListWidgetItem*(*)>(_a[1])),(*reinterpret_cast< QListWidgetItem*(*)>(_a[2]))); break;
        case 34: animalCalcClicked((*reinterpret_cast< QListWidgetItem*(*)>(_a[1])),(*reinterpret_cast< QListWidgetItem*(*)>(_a[2]))); break;
        case 35: animalCellClicked((*reinterpret_cast< int(*)>(_a[1])),(*reinterpret_cast< int(*)>(_a[2]))); break;
        case 36: animalCalcSelectionChanged((*reinterpret_cast< int(*)>(_a[1])),(*reinterpret_cast< int(*)>(_a[2]))); break;
        case 37: cropCellClicked((*reinterpret_cast< int(*)>(_a[1])),(*reinterpret_cast< int(*)>(_a[2]))); break;
        case 38: cropCalcSelectionChanged((*reinterpret_cast< int(*)>(_a[1])),(*reinterpret_cast< int(*)>(_a[2]))); break;
        }
        _id -= 39;
    }
    return _id;
}
QT_END_MOC_NAMESPACE
