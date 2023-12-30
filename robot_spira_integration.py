import requests
import json
import datetime
import time
import configparser
from robot.api import ExecutionResult, ResultVisitor
import sys

'''
The config is only retrieved once
'''
config = None

def getConfig():
    global config
    # Only retrieve config once
    if config is None:
        # Model of config object:
        config = {
            "url": "",
            "username": "",
            "token": "",
            "project_id": -1,
            "release_id": -1,
            "test_set_id": -1
        }
        # Parse the config file
        parser = configparser.ConfigParser()
        parser.read("spira.cfg")

        sections = parser.sections()

        # Process Configs
        for section in sections:
            # Handle credentials
            if section == "credentials":
                for (key, value) in parser.items(section):
                    config[key] = value
    return config


# Name of this extension
RUNNER_NAME = "Robot-Framework"


class SpiraTestRun:
    # The URL snippet used after the Spira URL
    REST_SERVICE_URL = "/Services/v6_0/RestService.svc/"
    # The URL spippet used to post an automated test run. Needs the project ID to work
    POST_TEST_RUN = "projects/%s/test-runs/record"
    '''
    A TestRun object model for Spira
    '''
    project_id = -1
    test_case_id = -1
    test_name = ""
    stack_trace = ""
    status_id = -1
    start_time = -1
    end_time = -1
    message = ""
    release_id = -1
    test_set_id = -1

    def __init__(self, project_id, test_case_id, test_name, stack_trace, status_id, start_time, end_time, message='', release_id=-1, test_set_id=-1):
        self.project_id = project_id
        self.test_case_id = test_case_id
        self.test_name = test_name
        self.stack_trace = stack_trace
        self.status_id = status_id
        self.start_time = start_time
        self.end_time = end_time
        self.message = message
        self.release_id = release_id
        self.test_set_id = test_set_id

    def post(self, spira_url, spira_username, spira_token):
        """
        Post the test run to Spira with the given credentials
        """
        url = spira_url + self.REST_SERVICE_URL + \
            (self.POST_TEST_RUN % self.project_id)
        # The credentials we need
        params = {
            'username': spira_username,
            'api-key': spira_token
        }

        # The headers we are sending to the server
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'User-Agent': RUNNER_NAME
        }

        # The body we are sending
        body = {
            # Constant for plain text
            'TestRunFormatId': 1,
            'StartDate': self.start_time.isoformat(),
            'EndDate': self.end_time.isoformat(),
            'RunnerName': RUNNER_NAME,
            'RunnerTestName': self.test_name,
            'RunnerMessage': self.message,
            'RunnerStackTrace': self.stack_trace,
            'TestCaseId': self.test_case_id,
            # Passes (2) if the stack trace length is 0
            'ExecutionStatusId': self.status_id
        }

        # Releases and Test Sets are optional
        if(self.release_id != -1):
            body["ReleaseId"] = int(self.release_id)
        if(self.test_set_id != -1):
            body["TestSetId"] = int(self.test_set_id)

        dumps = json.dumps(body)

        request = requests.post(url, data=json.dumps(
            body), params=params, headers=headers)

class SpiraResultVisitor(ResultVisitor):
    def __init__(self, markdown_file='report.md'):
        self.failed_tests = []
        self.passed_tests = []
        self.markdown_file = markdown_file

    def visit_test(self, test):
        if test.status == 'FAIL':
            self.failed_tests.append(test.name)
        elif test.status == 'PASS':
            self.passed_tests.append(test.name)

    def end_result(self, result):
        # Create a new markdown file
        with open(self.markdown_file, "w") as f:
            f.write("# Robot Framework Report\n")
            f.write("|Test|Status|\n")
            f.write("|---|---|\n")
            for test in self.passed_tests:
                f.write(f"|{test}|PASS|\n")
            for test in self.failed_tests:
                f.write(f"|{test}|FAIL|\n")
        
        # Report to the console
        print("Successfully reported {} test cases to Spira.\n".format(2))
                
if __name__ == '__main__':
    try:
        output_file = sys.argv[1]
    except IndexError:
        output_file = "output.xml"
    try:
        markdown_file = sys.argv[2]
    except IndexError:
        markdown_file = "report.md"
    result = ExecutionResult(output_file)
    result.visit(SpiraResultVisitor())
