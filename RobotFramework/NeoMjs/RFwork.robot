*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  edge
${url}  http://www.google.com

*** Test Cases ***
TestRF
    Open Browser    ${url}     ${browser}
    Click Element   id:L2AGLb