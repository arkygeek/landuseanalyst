# 4 Methodology Overview

## 4.1 Introduction

This chapter aims to explain the methodology used to model landuse. [cite: 1793, 1794, 1795, 1796] The goal of the modelling is to calculate the amount of land required to support a given settlement. [cite: 1796, 1797] This is achieved by creating a computer program that can calculate land requirements based on a set of input variables. [cite: 1797, 113, 114, 115, 116, 117] The input variables can be modified to reflect different scenarios, allowing the user to explore a range of possibilities.

The primary inputs for the model are:

* Population size

* Dietary requirements

* Agricultural productivity

* Animal productivity

* Landscape characteristics [cite: 113, 114, 115, 116, 117]

The model uses these inputs to calculate the amount of land needed to produce the required food and other resources. The results of the model can then be used to visualize landuse patterns and to assess the potential impact of different land management strategies.

The following sections describe the input variables and the algorithms used to calculate land requirements.

###   4.1.1 Input Variables

The model requires a number of input variables, which can be divided into two main categories:

* Settlement characteristics: These variables describe the settlement being studied, such as population size, dietary preferences, and the types of animals raised.

* Environmental characteristics: These variables describe the environment in which the settlement is located, such as soil fertility, rainfall, and topography. [cite: 113, 114, 115, 116, 117]

The specific input variables used in the model are described in more detail in the following sections.

###   4.1.2 Algorithm Development

The algorithm used to calculate land requirements is based on a series of equations that take into account the input variables. [cite: 113, 114, 115, 116, 117] The equations are designed to simulate the processes involved in food production, such as crop growth, animal reproduction, and the conversion of food into energy. The algorithm also takes into account factors such as wastage, seed stock requirements, and the need to provide feed for animals. [cite: 75, 76, 77, 78]

The algorithm is implemented in a computer program that allows the user to input different values for the input variables and to see the effect on land requirements. The program also includes features that allow the user to visualize landuse patterns and to assess the potential impact of different land management strategies.

##   4.2 Process Overview

The process used to calculate land requirements involves a number of steps, including:

1.  Defining calorie targets

2.  Calculating production targets

3.  Determining area targets

4.  Assessing land suitability

5.  Identifying land [cite: 113, 114, 115, 116, 117]

The following sections describe each of these steps in more detail.

###   4.2.1 Calorie Targets

The first step in the process is to define the calorie targets for the settlement. [cite: 55, 56, 57] This involves determining the average daily calorie intake for each person in the settlement, as well as the overall calorie needs of the settlement as a whole. The calorie targets are based on factors such as age, sex, and activity level. The model also allows for the inclusion of non-food items in the calorie targets, such as wool and dung.

The daily calorie intake is broken down into different food groups, such as:

* Domestic meat

* Dairy

* Wild meat

* Crops

* Wild plants [cite: 55, 56, 57]

The proportion of each food group in the diet can be varied to reflect different dietary preferences. [cite: 58, 59, 60]

####   4.2.1.1 Dietary Division

The model allows the user to specify the proportion of the diet that comes from animal sources and the proportion that comes from plant sources. [cite: 58, 59, 60, 61, 62, 63, 64, 65] This division can have a significant impact on the amount of land required to support the settlement. [cite: 61, 62, 63, 64, 65] A diet that is high in animal products will generally require more land than a diet that is high in plant products. The model also takes into account the different calorie densities of different food groups. [cite: 58, 59, 60, 61, 62, 63, 64, 65] For example, meat is generally more calorie-dense than plant foods, so a diet that is high in meat will require less overall food volume than a diet that is high in plant foods.

###   4.2.2 Production Targets

The next step in the process is to calculate the production targets for each food group. [cite: 75, 76, 77, 78] This involves determining the amount of each food group that needs to be produced to meet the calorie targets. The production targets are based on the calorie content of each food group and the proportion of each food group in the diet. The model also takes into account factors such as wastage and seed stock requirements. [cite: 75, 76, 77, 78] Crop production targets can be adjusted to account for wastage during harvest and storage, as well as seed stock retained for the following year's sowing. [cite: 75, 76, 77, 78]

###   4.2.3 Area Targets

The next step in the process is to determine the area targets for each food group. This involves calculating the amount of land needed to produce the required amount of each food group. The area targets are based on the productivity of the land and the production targets for each food group. The model takes into account factors such as crop yields, animal productivity, and the amount of land needed to support livestock. The model also incorporates the concept of crop rotation, which can affect the amount of land required for crop production.

####   4.2.3.1 Crop Rotation

Crop rotation is the practice of growing different crops in the same area in a recurring sequence. [cite: 66, 67, 68, 69] This can help to improve soil fertility and reduce the buildup of pests and diseases. [cite: 66, 67, 68, 69] The model takes into account the effects of crop rotation on land requirements.

####   4.2.3.2 Animal Herd Size

The model calculates the required herd size based on the dietary needs of the settlement and the productivity of the animals. [cite: 68, 69, 70, 71, 72, 73, 74] This calculation takes into account factors such as the amount of meat and dairy produced by each animal, as well as the feed requirements of the animals. [cite: 68, 69, 70, 71, 72, 73, 74] The model also considers the impact of secondary animal products, such as wool and dung, on the overall land requirements.

###   4.2.4 Land Suitability

The next step in the process is to assess land suitability. [cite: 74, 75, 76, 77, 78, 79] This involves determining which areas of land are most suitable for different types of landuse, such as crop production and animal grazing. The assessment of land suitability is based on factors such as soil type, slope, and access to water. The model uses this information to create land suitability masks, which are used to guide the allocation of land for different purposes.

####   4.2.4.1 Land Suitability Masks

Land suitability masks are used to identify areas of land that are suitable for different types of landuse. [cite: 74, 75, 76, 77, 78, 79] These masks are created based on factors such as soil type, slope, and access to water. The model uses these masks to guide the allocation of land for different purposes.

####   4.2.4.2 Cost Surfaces

Cost surfaces are used to represent the cost of traveling across different areas of land. [cite: 75, 76, 77, 78] The cost of travel can be affected by factors such as slope, vegetation, and the presence of obstacles. The model uses cost surfaces to calculate the travel time between different locations.

####   4.2.4.3 Walking Time

The model calculates walking time based on the distance between different locations and the cost of traveling across the intervening land. [cite: 76, 186, 187, 188, 189, 190, 191] The model takes into account the fact that travel time can be affected by factors such as slope and terrain. [cite: 186, 187, 188, 189, 190, 191]

#####   4.2.4.3.1 Path Distance

Path distance is a measure of the distance between two locations that takes into account the cost of traveling across the intervening land. [cite: 77, 186, 187, 188, 189, 190, 191] This is in contrast to Euclidean distance, which is a simple straight-line measure of distance.

#####   4.2.4.3.2 Euclidean

Euclidean distance is a simple straight-line measure of the distance between two locations. [cite: 78]

###   4.2.5 Land Identification

The final step in the process is to identify the specific areas of land that will be used for different purposes. [cite: 78, 79] This involves using the results of the land suitability assessment to allocate land for different uses, such as crop production and animal grazing. The model uses two different methods for land identification:

1.  Incremental method

2.  Binary method [cite: 78, 79]

####   4.2.5.1 Incremental Method

The incremental method involves gradually adding land until the production targets are met. [cite: 79]

####   4.2.5.2 Binary Method

The binary method involves selecting or rejecting land parcels based on their suitability for a particular use. [cite: 79]

##   4.3 Landuse Analyst

The methodology described in this chapter has been implemented in a software program called Landuse Analyst. [cite: 113, 114, 115, 116, 117] This program allows users to input the variables described above and to calculate the amount of land required to support a given settlement. The program also includes features that allow users to visualize landuse patterns and to assess the potential impact of different land management strategies.

Landuse Analyst is a user-friendly application that can be used to model landuse in any part of the world, for any post-agriculture period. [cite: 116, 117] The software is flexible enough to be used without modification for a variety of sites. [cite: 113, 114, 115, 116, 117] The program allows for the input of various factors, such as crop types, animal types, and settlement characteristics. [cite: 113, 114, 115, 116, 117]

The software uses TrollTech’s Qt libraries to create a user-friendly graphical user interface (GUI). [cite: 112, 113, 114, 115, 116, 117]

The main screen in Landuse Analyst is shown in Figure 4.15. [cite: 83]

###   4.3.1 LA’s Opening Screen

The opening screen in Landuse Analyst allows the user to input basic information about the settlement being studied, such as:

* Settlement name

* Population size

* Dietary preferences

* Animal types [cite: 83, 84]

####   4.3.1.1 Basic Input

The basic input screen allows the user to define the settlement name, population size, dietary preferences, and animal types. [cite: 83, 84]

####   4.3.1.2 Catchment Creation Methods

Landuse Analyst provides several methods for creating catchments, which are the areas of land that are used to support the settlement. [cite: 84]

####   4.3.1.3 GRASS Data

Landuse Analyst can import data from the Geographic Resources Analysis Support System (GRASS) GIS software. [cite: 84]

###   4.3.2 LA’s Diet Screen

The diet screen in Landuse Analyst allows the user to specify the dietary preferences of the settlement. [cite: 85] The user can specify the proportion of the diet that comes from different food groups, such as domestic meat, dairy, wild meat, crops, and wild plants. The diet screen is shown in Figure 4.16. [cite: 85]

###   4.3.3 LA’s Crops Screen

The crops screen in Landuse Analyst allows the user to specify the types of crops grown by the settlement. [cite: 86, 87, 88, 89, 90, 91] The user can also specify the characteristics of each crop, such as its yield, calorie content, and water requirements. The crops screen is shown in Figure 4.17. [cite: 86, 87, 88, 89, 90, 91]

###   4.3.4 LA Crop Manager

The Crop Manager in Landuse Analyst allows the user to define and manage the crops used in the model. [cite: 87, 88, 89, 90, 91]

####   4.3.4.1 Defining the Plants

The user can define various characteristics of the plants, such as their calorie content, yield, and water requirements. [cite: 87, 88, 89, 90, 91]

###   4.3.5 LA’s Crop Parameters

The Crop Parameters screen allows the user to specify additional parameters for each crop, such as crop rotation requirements and required surplus production. [cite: 88, 89, 90, 91]

####   4.3.5.1 Crop Rotation

The user can specify the crop rotation requirements for each crop. [cite: 88, 89, 90, 91]

####   4.3.5.2 Required Surplus Production

The user can specify the required surplus production for each crop. [cite: 88, 89, 90, 91] This parameter allows the user to account for factors such as wastage and seed stock requirements.

###   4.3.6 LA’s Animal Screen

The Animal screen in Landuse Analyst allows the user to specify the types of animals raised by the settlement. [cite: 92, 93, 94, 95, 96, 97, 98, 99, 100, 101] The user can also specify the characteristics of each animal, such as its meat and dairy production, feed requirements, and reproductive rate. The Animal screen is shown in Figure 4.20. [cite: 92, 93, 94, 95, 96, 97, 98, 99, 100, 101]

###   4.3.7 LA’s Animal Manager

The Animal Manager in Landuse Analyst allows the user to define and manage the animals used in the model. [cite: 93, 94, 95, 96, 97, 98, 99, 100, 101, 151, 152, 153, 154]

####   4.3.7.1 Animal Description

The user can define various characteristics of the animals, such as their species, breed, and sex. [cite: 93, 94, 95, 96, 97, 98, 99, 100, 101]

####   4.3.7.2 Daily Feed Requirements

The user can specify the daily feed requirements for each animal. [cite: 95, 96, 97, 98, 99, 100, 101]

####   4.3.7.3 By-Products

The user can specify the by-products produced by each animal, such as wool, dung, and hides. [cite: 96, 97, 98, 99, 100, 101]

###   4.3.8 LA’s Animal Parameters

The Animal Parameters screen allows the user to specify additional parameters for each animal, such as details and land suitability selection. [cite: 96, 97, 98, 99, 100, 101]

####   4.3.8.1 Details

The user can specify various details about each animal, such as its age, weight, and reproductive status. [cite: 97, 98, 99, 100, 101]

####   4.3.8.2 Land Suitability Selection

The user can specify the land suitability requirements for each animal. [cite: 98, 99, 100, 101]

####   4.3.8.3 Portion of Domestic Meat Diet

The user can specify the portion of the domestic meat diet that comes from each animal. [cite: 98, 99, 100, 101]

###   4.3.9 LA’s Assemblage Conversion Utility

Landuse Analyst includes an Assemblage Conversion Utility, which allows the user to convert archaeological assemblage data into a format that can be used by the model. [cite: 98, 99, 100, 101, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484]

####   4.3.9.1 Automatic Entry

The Assemblage Conversion Utility allows for automatic entry of assemblage data. [cite: 99, 151, 152, 153, 154]

####   4.3.9.2 Manual Entry

The Assemblage Conversion Utility also allows for manual entry of assemblage data. [cite: 99, 151, 152, 153, 154]

###   4.3.10 LA’s Calculations Screen

The Calculations screen in Landuse Analyst displays the results of the model calculations. [cite: 99, 100, 101, 567, 568, 569, 570, 571, 572]

###   4.3.11 LA’s Results Screen

The Results screen in Landuse Analyst presents the results of the model in a user-friendly format. [cite: 99, 100, 101, 616, 617, 618]

###   4.3.12 LA’s Log Screen

The Log screen in Landuse Analyst displays a log of the model calculations. [cite: 99, 106]

###   4.3.13 LA’s Help Screen

The Help screen in Landuse Analyst provides help and documentation for the software. [cite: 106, 47, 48, 49]

###   4.3.14 Future development

Landuse Analyst is a powerful tool that can be used to model landuse in a variety of contexts. The software is constantly being updated and improved, and future development efforts will focus on adding new features and improving the user interface.

###   D Landuse Analyst Source Code

The source code for Landuse Analyst is provided in Appendix D. The source code is written in C++ and uses the Qt library. The following files are included in the source code:

* `laanimalmanager.h` [cite: 389, 390]

* `laanimalmanager.cpp` [cite: 389, 390]

* `laanimalparametermanager.h` [cite: 396, 397]

* `laanimalparametermanager.cpp` [cite: 396, 397]

* `laassemblageconversion.h` [cite: 407, 408]

* `laassemblageconversion.cpp` [cite: 407, 408]

* `lacropmanager.h` [cite: 413, 414]

* `lacropmanager.cpp` [cite: 413, 414]

* `lacropparametermanager.h` [cite: 419, 420]

* `lacropparametermanager.cpp` [cite: 419, 420]

* `lagrassprocess.h` [cite: 426, 427]

* `lagrassprocess.cpp` [cite: 426, 427]

* `lamainform.h` [cite: 435, 436, 437]

* `lamainform.cpp` [cite: 435, 436, 437]

* `main.cpp` [cite: 465]

* `la.h` [cite: 467]

* `laanimal.h` [cite: 468, 473]

* `laanimal.cpp` [cite: 468, 473]

* `laanimalparameter.h` [cite: 483, 485]

* `laanimalparameter.cpp` [cite: 483, 485]

* `lacrop.h` [cite: 494, 496]

* `lacrop.cpp` [cite: 494, 496]

* `lacropparameter.h` [cite: 501, 503]

* `lacropparameter.cpp` [cite: 501, 503, 972, 973, 974, 975, 976, 977, 978]

* `ladietlabels.h` [cite: 509, 510]

* `ladietlabels.cpp` [cite: 509, 510, 614, 615, 616, 617]

* `lafoodsource.h` [cite: 514, 515]

* `lafoodsource.cpp` [cite: 514, 515, 863, 864, 865, 866, 867]

* `lagrass.h` [cite: 517, 519]

* `lagrass.cpp` [cite: 517, 519, 1036, 1037, 1038, 1039, 1040, 1041]

* `lagrassprocesslib.h` [cite: 526, 527]

* `lagrassprocesslib.cpp` [cite: 526, 527]

* `laguid.h` [cite: 529, 530]

* `laguid.cpp` [cite: 529, 530]

* `lamodel.h` [cite: 531, 539]

* `lamodel.cpp` [cite: 531, 539, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121]

* `laserialisable.h` [cite: 576, 577]

* `laserialisable.cpp` [cite: 576, 577]

* `lautils.h` [cite: 482, 579, 582]

* `lautils.cpp` [cite: 482, 579, 582, 868, 869, 870, 972, 1635, 1636, 1637, 1638, 1639, 1640, 1641, 1684, 1685, 1686, 1687, 1688, 1689]

These files contain the source code for the various classes and functions used in Landuse Analyst. The source code is well-documented and can be used to understand how the program works.

###   E Crop Characteristics

Appendix E provides a table of crop characteristics used in the model. The table includes information on the calorie content, yield, and water requirements for each crop.

###   F Animal Characteristics

Appendix F provides a table of animal characteristics used in the model. The table includes information on the meat and dairy production, feed requirements, and reproductive rate for each animal.