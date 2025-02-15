#pragma once

#include <iostream>
#include <sstream>
#include <memory>
#include <stdexcept>

struct RedirectFixture {
    std::streambuf* coutBuffer;
    std::stringstream newBuffer;

    RedirectFixture();
    ~RedirectFixture();

    std::string currentCoutOutput() const;
};