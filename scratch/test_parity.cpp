#include <QCoreApplication>
#include <QDebug>
#include <QString>
#include <QMap>
#include "lamodel.h"
#include "la.h"
#include "ladietlabels.h"
#include <iostream>

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    LaModel myModel;
    myModel.setName("Test Model");
    myModel.setPopulation(100); // 100 people
    myModel.setCaloriesPerPersonDaily(2500); // 2500 kcal
    myModel.setDietPercent(50); // 50% animal, 50% plant? Wait, dietPercent is plant percent?
    
    // We need to set up animals and crops maps.
    // In C++, mAnimalsMap maps Animal GUID to AnimalParameter GUID
    // But to work properly, LaUtils::getAnimal() needs to return a valid animal.
    // That means we need to populate the data directory or provide mock data.
    
    return 0;
}
