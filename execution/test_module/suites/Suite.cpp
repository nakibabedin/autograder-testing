#include "../external/doctest.h"
#include "../util.hpp"
#include "../../submission_module/submission_module.hpp"


TEST_SUITE_BEGIN("Helloworld");

TEST_CASE("Helloworld") {

    REQUIRE_EQ("helloworld", Test::helloworld());
}

TEST_SUITE_END();
