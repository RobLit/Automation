*** Settings ***
Library  SeleniumLibrary
Library  String
Library  commons/data_generator.py

*** Variables ***
${email}    qw23@foo.bar
${password}  password

*** Keywords ***
SignIn
    Wait Until Page Contains Element    id:neo-vnode-6
    Click Element    id:neo-vnode-4
    Wait Until Page Contains Element    name:email
    Press Keys    name:email    ${email}
    Press Keys    name:password    ${password}
    Click Button    class:btn-primary
    Wait Until Page Contains Element    class:user-pic

SignInGen
    Wait Until Page Contains Element    id:neo-vnode-6
    Click Element    id:neo-vnode-6
    Wait Until Page Contains Element    name:email
    ${random_username}=    Name Gen
    ${random_email}=    Email Gen
    ${random_password}=    Password Gen
    Press Keys   name:username   ${random_username}
    Press Keys    name:email      ${random_email}
    Press Keys    name:password     ${random_password}
    Click Button    class:btn-primary
    Sleep    2
    ${check_name}=  Get Text    id:neo-vnode-47
    Should Be Equal As Strings    ${check_name.strip()}    ${random_username.strip()}

