# lafoodsource.py
class LaFoodSource:
    def __init__(self):
        self._grain = 0
        self._fodder = 0
        self._days = 0
        self._used = False
        self._cropGuid = ""

    def __del__(self):
        pass

    # accessors
    @property
    def grain(self):
        return self.mGrain

    def fodder(self):
        return self._fodder

    def days(self):
        return self._days

    def used(self):
        return self._used

    def cropGuid(self):
        return self._cropGuid

    # mutators
    @grain.setter
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