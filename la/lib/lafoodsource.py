# lafoodsource.py
class LaFoodSource:
    def __init__(self):
        self.mGrain = 0
        self.mFodder = 0
        self.mDays = 0
        self.mUsed = False
        self.mCropGuid = ""

    def __del__(self):
        pass

    # accessors
    def grain(self):
        return self.mGrain

    def fodder(self):
        return self.mFodder

    def days(self):
        return self.mDays

    def used(self):
        return self.mUsed

    def cropGuid(self):
        return self.mCropGuid

    # mutators
    def setGrain(self, theValue):
        self.mGrain = theValue

    def setFodder(self, theValue):
        self.mFodder = theValue

    def setDays(self, theValue):
        self.mDays = theValue

    def setUsed(self, theBool):
        self.mUsed = theBool

    def setCropGuid(self, theCropGuid):
        self.mCropGuid = theCropGuid