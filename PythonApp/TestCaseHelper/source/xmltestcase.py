from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element

class mElement(Element):
    def __init__(self, tag, text=""):
        super(mElement, self).__init__(tag=tag)
        self.text = text
        self.tail = "\n"

class Summary(mElement):
    def __init__(self, text=""):
        super(Summary, self).__init__(tag="summary", text=text)

class Preconditions(mElement):
    def __init__(self, text=""):
        super(Preconditions, self).__init__(tag="preconditions", text=text)


class StepNumber(mElement):
    def __init__(self, text=""):
        super(StepNumber, self).__init__(tag="step_number", text=text)


class Actions(mElement):
    def __init__(self, text=""):
        super(Actions, self).__init__(tag="actions", text=text)


class ExceptedResults(mElement):
    def __init__(self, text=""):
        super(ExceptedResults, self).__init__(tag="expectedresults", text=text)


class ExceutionType(mElement):

    def __init__(self, text=""):
        super(ExceutionType, self).__init__(tag="execution_type", text=text)



ExceutionType.MANUAL = "1"
ExceutionType.AUTOEXEC = "2"


class Step(mElement):
    def __init__(self, nstep, actions, excepted,
            excutetype, tag="step"):
        super(Step, self).__init__(tag)
        self.append(StepNumber(nstep))
        self.append(Actions(actions))
        self.append(ExceptedResults(excepted))
        self.append(ExceutionType(excutetype))


class Steps(mElement):
    def __init__(self):
        super(Steps, self).__init__(tag="steps")


class CustomField(mElement):
    def __init__(self, name, value):
        super(CustomField, self).__init__(tag="custom_field")
        self.append(mElement(tag="name", text=name))
        self.append(mElement(tag="value", text=value))


class CustomFields(mElement):
    def __init__(self):
        super(CustomFields, self).__init__(tag="custom_fields")


class Requirement(mElement):
    def __init__(self, req_spec_title, doc_id, title):
        super(Requirement, self).__init__(tag="requirement")
        self.append(mElement(tag="req_spec_title", text=req_spec_title))
        self.append(mElement(tag="doc_id", text=doc_id))
        self.append(mElement(tag="title", text=title))



class Requirements(mElement):
    def __init__(self):
        super(Requirements, self).__init__(tag="requirements")

def create_steps(steps=dict(), excutetype = ExceutionType.MANUAL):
    if isinstance(steps, dict):
        result = Steps()
        i = 1
        for key, value in steps.items():
            result.append(Step(nstep=str(i), actions=key, excepted=value, excutetype=excutetype))
            i += 1
        return result
    elif isinstance(steps, list):
        result = Steps()
        i = 1
        for key, value in steps:
            result.append(Step(nstep=str(i), actions=key, excepted=value, excutetype=excutetype))
            i += 1
        return result
    elif isinstance(Steps, steps):
        return steps
    else:
        raise TypeError("Input Parameter Error")


def create_custom_fileds(fileds=dict()):
    if isinstance(fileds, dict):
        result = CustomFields()
        for name, value in fileds.items():
            result.append(CustomField(name, value))
        return result
    elif isinstance(fileds, CustomFields):
        return fileds
    else:
        raise TypeError("Input Custom Fileds Parameter Error")

def create_requirements(req_spec_title, requirements=dict()):
    if isinstance(requirements, dict):
        reqs = Requirements()
        for _doc_id, _title in requirements.items():
            reqs.append(Requirement(req_spec_title=req_spec_title,
                                     doc_id=_doc_id, title=_title))
        return reqs
    elif isinstance(requirements, Requirements):
        return requirements
    else:
        raise TypeError("Input Requirement Parameter Error")


class XmlTestCase(mElement):
    def __init__(self, name, summary, precondition, steps, excutetype, custom_fields, req_spec_title, requirements):
        super(XmlTestCase, self).__init__(tag="testcase")
        self.attrib["name"] = name
        self.append(Summary(summary))
        self.append(Preconditions(precondition))
        self.append(create_steps(steps, excutetype))
        self.append(create_custom_fileds(custom_fields))
        self.append(create_requirements(req_spec_title, requirements))

class XmlTestCases(mElement):
    def __init__(self):
        super(XmlTestCases, self).__init__(tag="testcases")


class TestCase2Xml(ElementTree):
    def __init__(self, element=None, file=None):
        super(TestCase2Xml, self).__init__(element, file)

def testcase2xml(cases, target):
    tree = TestCase2Xml(cases)
    tree.write(target, encoding="utf8",
            xml_declaration=True, default_namespace=None, method="xml")
