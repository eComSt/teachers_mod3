CC = gcc
TEST_LIB = simple_calc
TESTFILE = test
GCOV_FLAG = -fprofile-arcs -ftest-coverage
LIBS_FOR_CHECK_PCKG = -lcheck -lm -lpthread
D_OS = -D __My_APPLE__




all: clean so prepare install dist

prepare:
	/usr/bin/python3 -m pip install --upgrade pip
	/usr/bin/python3 -m pip install py2app

install:
	~/Library/Python/3.8/bin/py2applet calc.py
	cp simple_calc.so calc.app/Contents/Resources/

uninstall:
	rm -rf calc.app
	rm calc.tgz

dvi:
	open manual.txt

clean:
	@find . -type f -name "*.a" -delete
	@find . -type f -name "*.o" -delete
	@find . -type f -name "*.out" -delete
	@find . -type f -name "*.info" -delete
	@rm -rf test *.html *.gcda *.gcno gcov_report *.css
	@find . -type f -name "*.out" -delete

so:
	gcc -fPIC -shared -o simple_calc.so simple_calc.c

dist:
	tar -czf calc.tgz calc.app

c.a:
	@echo "=== simple_calc compile ==="
	$(CC) $(D_OS) -c $(FLAGS) $(TEST_LIB).c -o $(TEST_LIB).a

test: c.a
	@echo "=========== test ==========="
	$(CC) $(FLAGS) -o a.out test.c $(TEST_LIB).a $(LIBS_FOR_CHECK_PCKG) $(GCOV_FLAG)
	./a.out
gcov_report:
	$(CC) $(D_OS) -c $(FLAGS) $(GCOV_FLAG) $(TEST_LIB).c -o $(TEST_LIB).a
	$(CC) $(FLAGS) $(GCOV_FLAG) $(TEST_LIB).a $(TESTFILE).c $(LIBS_FOR_CHECK_PCKG) -o a2.out
	./a2.out
	@echo "=== gcov start ==="
	gcov a2.out
	lcov -o test.info -c -d .
	genhtml -o report test.info

ifeq ($($(shell uname -s)), Linux)
	LIBS_FOR_CHECK_PCKG = -lcheck -lsubunit -lm -lpthread -lrt
	D_OS = -D __My_Linux__
else
	LIBS_FOR_CHECK_PCKG = -lcheck -lm -lpthread
	D_OS = -D __My_APPLE__
endif


proper: uninstall clean