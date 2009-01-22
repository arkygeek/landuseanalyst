#ifndef __LAMODEL_INTERFACE_H
#define __LAMODEL_INTERFACE_H

class LaModelInterface
{
public:
    LaModelInterface() {}
    virtual ~LaModelInterface() {}


private:
    LaModelInterface( const LaModelInterface& source );
    void operator = ( const LaModelInterface& source );
};


#endif   // __LAMODEL_INTERFACE_H
