///////////////////////////////////////////////////////////////////////////////
// NAME:            fsadaptortest.cpp
//
// AUTHOR:          Ethan D. Twardy <ethan.twardy@gmail.com>
//
// DESCRIPTION:     Test for the fsadaptor Conan package
//
// CREATED:         09/20/2022
//
// LAST EDITED:     09/20/2022
////

#include <functional>
#include <iostream>
#include <list>
#include <FSAdaptor/namespace.h>
#include <FSAdaptor/Path.h>
#include <FSAdaptor/PathWalker.h>
#include <FSAdaptor/StandardFilesystemAdaptor.h>

int main() {
    FSAdaptor::StandardFilesystemAdaptor stdAdaptor;
    FSAdaptor::PathWalker<std::list> pathWalker;
    static const std::string path = ".";
    stdAdaptor.walk(pathWalker, stdAdaptor.absolute(FSAdaptor::Path{path}));

    std::list<FSAdaptor::Path> files{pathWalker.getContainer()};
    std::for_each(files.cbegin(), files.cend(), [](const auto& element) {
        std::cout << element << "\n";
    });
}

///////////////////////////////////////////////////////////////////////////////
