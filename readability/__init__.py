import check50

@check50.check()
def exists():
    """readability.cpp exists"""
    check50.exists("readability.cpp")
    check50.include("input1.txt", "input2.txt")
    check50.include("expected_output1.txt", "expected_output2.txt")

@check50.check(exists)
def compiles():
    """readability.cpp compiles"""
    check50.run("g++ readability.cpp -lcrypt -lcs50 -lm -o readability").exit(0)

@check50.check(compiles)
def single_sentence_fileRead():
    """handles single sentence with multiple words"""
    check50.run("./readability").stdin("input1.txt").exit(0)
    check_output(open("output.txt").read(), open("expected_output1.txt").read())
    
@check50.check(compiles)
def single_sentence_other_punctuation_fileRead():
    """handles punctuation within a single sentence"""
    check50.run("./readability").stdin("input2.txt").exit(0)
    check_output(open("output.txt").read(), open("expected_output2.txt").read())
            
def check_output(out, expected_out):
    if (out != expected_out):
        raise check50.Failure("Calculated result does not match with expected result\nOutput: " + out + "\nExpected output: " + expected_out)