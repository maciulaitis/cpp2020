import check50

@check50.check()
def exists():
    """caesar.cpp exists."""
    check50.exists("caesar.cpp")
    check50.include("input.txt")
    check50.include("expected_output1.txt", "expected_output2.txt", "expected_output3.txt", "expected_output4.txt", "expected_output5.txt", "expected_output6.txt")

@check50.check(exists)
def compiles():
    """caesar.cpp compiles."""
    check50.run("g++ caesar.cpp -lcrypt -lcs50 -lm -o caesar").exit(0)

@check50.check(compiles)
def encrypts_a_as_b():
    """encrypts "a" as "b" using 1 as key"""
    generate_input("a")
    check50.run("./caesar 1").exit(0)
    check_output(open("output.txt").read(), open("expected_output1.txt").read())

@check50.check(compiles)
def encrypts_barfoo_as_yxocll():
    """encrypts "barfoo" as "yxocll" using 23 as key"""
    generate_input("barfoo")
    check50.run("./caesar 23").exit(0)
    check_output(open("output.txt").read(), open("expected_output2.txt").read())

@check50.check(compiles)
def encrypts_BARFOO_as_EDUIRR():
    """encrypts "BARFOO" as "EDUIRR" using 3 as key"""
    generate_input("BARFOO")
    check50.run("./caesar 3").exit(0)
    check_output(open("output.txt").read(), open("expected_output3.txt").read())

@check50.check(compiles)
def encrypts_BaRFoo_FeVJss():
    """encrypts "BaRFoo" as "FeVJss" using 4 as key"""
    generate_input("BaRFoo")
    check50.run("./caesar 4").exit(0)
    check_output(open("output.txt").read(), open("expected_output4.txt").read())

@check50.check(compiles)
def encrypts_barfoo_as_onesbb():
    """encrypts "barfoo" as "onesbb" using 65 as key"""
    generate_input("barfoo")
    check50.run("./caesar 65").exit(0)
    check_output(open("output.txt").read(), open("expected_output5.txt").read())

@check50.check(compiles)
def checks_for_handling_non_alpha():
    """encrypts "world, say hello!" as "iadxp, emk tqxxa!" using 12 as key"""
    generate_input("world, say hello!")
    check50.run("./caesar 12").exit(0)
    check_output(open("output.txt").read(), open("expected_output6.txt").read())

@check50.check(compiles)
def handles_no_argv():
    """handles lack of argv[1]"""
    check50.run("./caesar").exit(1)
    
    
def generate_input(input):
    open("input.txt", "w").write(input)
