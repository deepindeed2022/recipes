# -*- coding:UTF-8 -*-
import sys
import time

from xmltestcase import  XmlTestCase, XmlTestCases, testcase2xml
reload(sys)
sys.setdefaultencoding('utf8')
import testenv

def read_txt_file(filename, sep="&&"):
    result = list()
    name = ""
    nameset = set()
    summary = ""
    product_req = dict()
    flag = False
    precondition = ""

    def get_step(lines, i, sep):
        l = lines[i]
        while l.rfind(sep) == -1 and i < len(lines):
            i += 1
            l = "<p>%s</p>\n<p>%s</p>" % (l , lines[i])
        kv = l.rstrip().split(sep)
        excepted = map(lambda x: x.encode("utf8"), kv[1:])
        result.append((kv[0].encode("utf8"), ";".join(excepted)))
        return i

    with open(filename, "r") as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            l = lines[i]
            if l.startswith("##"):
                summary = l.lstrip("##").rstrip()
            elif l.startswith("#"):
                flag = True
                name = l.lstrip("#").strip()
                if name not in nameset:
                    nameset.add(name)
                else:
                    print "测试用例名重复: `%s`, 换一个重新生成好不" % (name, )
                result, product_req = list(), dict()
                summary, precondition  = "", ""
            elif l.startswith("@@"):
                precondition = l.lstrip("@@").strip()
            elif l.startswith("@"):
                tmp  = l.lstrip("@").split(":")
                product_req[tmp[0].upper()] = ":".join(tmp[1:]).encode("utf8")
            elif len(l.strip()) is 0:
                if flag:
                    flag = False
                    yield name, summary, precondition, result, product_req
            else:
                i = get_step(lines, i, sep)
            i += 1
        yield name, summary, precondition, result, product_req

def generator(file, target=None):
    """Generate TestCase from RawText
    """
    cases = XmlTestCases()
    for name, summary, precondition, steps, product_req in read_txt_file(file):

        tcase = XmlTestCase(name=name, summary=summary, 
                        precondition=precondition,
                        steps=steps, excutetype=testenv.EXCUTION_TYPE, 
                        custom_fields=testenv.custom_fields,
                        req_spec_title=testenv.req_spec_title,
                        requirements=product_req)
        cases.append(tcase)
    target = "%s.xml" % (file,) if target == None else target
    testcase2xml(cases, target)

if __name__ == '__main__':
    sys.argv.append("testcase.txt")
    if len(sys.argv) < 2:
        print "Please input a testcase raw data file"
        generator("testcase.txt")
    else:
        generator(sys.argv[1])


