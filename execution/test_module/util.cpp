#include "util.hpp"

RedirectFixture::RedirectFixture() {
    coutBuffer = std::cout.rdbuf();
    newBuffer = std::stringstream();
    std::cout.rdbuf(newBuffer.rdbuf());
}

RedirectFixture::~RedirectFixture() {
    if (coutBuffer) { std::cout.rdbuf(coutBuffer); }
    else { std::cerr << "Unable to restore cout buffer" << std::endl; }

    std::cout << newBuffer.str() << std::endl;
}

std::string RedirectFixture::currentCoutOutput() const {
    return newBuffer.str();
}