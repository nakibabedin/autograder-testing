CXX = g++
CXXFLAGS = -std=c++17 -g -Wall -O2 

PROG ?= main

# Source directories
SUBMISSION_DIR = submission_module
TEST_DIR = test_module
TEST_SUITE_DIR = test_module/suites

# Core game objects
CORE_OBJS = \
	# $(SUBMISSION_DIR)/something.o

# Test library objects
TEST_OBJS = \
	$(TEST_DIR)/util.o \
	$(TEST_SUITE_DIR)/Suite.o \

# Main program objects
MAIN_OBJS = main.o

OBJS = $(MAIN_OBJS) $(CORE_OBJS) $(TEST_OBJS)

mainprog: $(PROG)

.cpp.o:
	$(CXX) $(CXXFLAGS) -c -o $@ $<

$(PROG): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $@ $(OBJS)

clean:
	rm -rf $(PROG) *.o *.out \
		$(TEST_DIR)/*.o \
		$(TEST_DIR)/*/*.o \
		$(SUBMISSION_DIR)/*.o \
		$(SUBMISSION_DIR)/*/*.o 

rebuild: clean main