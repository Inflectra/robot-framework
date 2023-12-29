*** Settings ***
Documentation     This .robot file is a sample test suite for demonstrating the Spira integration
...
...               Keywords are imported from the resource file
Resource          keywords.resource
Library           DateTime


*** Test Cases ***
Simple Test Case
    [Documentation]    Shows some assertion keywords
    [Tags]    TC:23
    Should Be Title Case    Robot Framework
    Should Be Equal    Text123    Text123
    Should Be True    5 + 5 == 10

Test with Keywords
    [Tags]    TC:24
    Store Text    Hail Our Robot
    Add Text To Stored Text     Overlords!
    Verify Stored Text Length    25
    ${current_text}=    Get Stored Text
    Should Be Equal    ${current_text}    Hail Our Robot Overlords!

Test for the year 2022
    [Documentation]    Tests if it is still 2022...
    [Tags]    TC:25
    ${date}=    Get Current Date    result_format=datetime
    Log    ${date}
    Should Be Equal As Strings    ${date.year}    2022

Test Case that fails
    [Tags]    TC:26
    Check Correct Greeting    Hail Our Robot Overlords!
    Check Correct Greeting    Hello World!