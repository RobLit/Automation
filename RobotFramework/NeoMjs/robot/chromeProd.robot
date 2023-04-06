*** Settings ***
Library  SeleniumLibrary
Library  String
Library  commons/data_generator.py
Resource    commons/keywords.robot

*** Variables ***
${browser}  edge
${browser2}  chrome
${browser3}  firefox
${url}  http://localhost:8080/
${url1}  http://localhost:8080/apps/realworld/index.html
${url2}  http://localhost:8080/dist/development/apps/realworld/index.html
${url3}  http://localhost:8080/dist/production/apps/realworld/index.html
${url4}  http://localhost:8080/dist/development/docs/index.html
${url5}  http://localhost:8080/test/siesta/realworld/index.html
${url6}  https://neomjs.github.io/pages/node_modules/neo.mjs/dist/production/apps/website/index.html#mainview=blog
${email}    qw23@foo.bar
${password}  password

*** Test Cases ***
RunBrowser1
    open browser  ${url}    ${browser2}
    Click Element   xpath://*[@id="content"]/ul[1]/li/a
    Switch Window   title=Conduit
    Location Should Be    ${url1}
    Run Keyword And Ignore Error    Close Window

RunBrowser2
    open browser  ${url}    ${browser2}
    Click Element   xpath://*[@id="content"]/ul[2]/li[1]/a
    Switch Window   title=Conduit
    Location Should Be    ${url2}
    Run Keyword And Ignore Error    Close Window

RunBrowser3
    open browser  ${url}    ${browser2}
    Click Element   xpath://*[@id="content"]/ul[2]/li[2]/a
    Switch Window   title=Conduit
    Location Should Be    ${url3}
    Run Keyword And Ignore Error    Close Window

RunBrowser4
    open browser  ${url}    ${browser2}
    Click Element   xpath://*[@id="content"]/ul[3]/li/a
    Switch Window   title=Neo Docs
    Location Should Be    ${url4}
    Run Keyword And Ignore Error    Close Window

RunBrowser5
    open browser  ${url}    ${browser2}
    Click Element   xpath://*[@id="content"]/ul[4]/li/a
    Switch Window   title=Neo test suite
    Location Should Be    ${url5}
    Run Keyword And Ignore Error    Close Window

RunBrowser6
    open browser  ${url}    ${browser2}
    Click Element   xpath://*[@id="content"]/ul[5]/li/a
    Switch Window   title=neo.mjs - Website
    Location Should Be    ${url6}
    Run Keyword And Ignore Error    Close Window

SignUpSession
    Open Browser    ${url3}    ${browser2}
    Wait Until Page Contains Element    id:neo-vnode-6
    Click Element    id:neo-vnode-6
    Wait Until Page Contains Element    name:email
    Press Keys   name:username   TestSession
    Press Keys    name:email      ${email}
    Press Keys    name:password     ${password}
    Click Button    class:btn-primary
    Wait Until Page Contains Element    class:user-pic
    Run Keyword And Ignore Error    Close Window

SignInGen
    Open Browser    ${url3}    ${browser2}
    SignInGen
    Run Keyword And Ignore Error    Close Window

Log_out
    Open Browser    ${url3}    ${browser2}
    #SignIn
    SignInGen
    Wait Until Page Contains Element    id:neo-vnode-233
    Click Button    id:neo-vnode-233
    Click Button    id:ne-vnode-324
    Run Keyword And Ignore Error    Close Window

Should_Title_Match
    Open Browser    ${url3}    ${browser2}
    Wait Until Page Contains Element    id:neo-vnode-35
    ${get_title1}=      Get Text    id:neo-vnode-35
    Click Element    id:neo-vnode-35
    ${get_title2}=      Get Text    xpath://*[@id="neo-vnode-10"]
    Should Be Equal    ${get_title2}    ${get_title1}
    #problem didnt appear only on production version -- id:neo-vnode-10
    Run Keyword And Ignore Error    Close Window

Rating_should_+1
    Open Browser    ${url3}    ${browser2}
    Wait Until Page Contains Element    id:neo-vnode-20
    ${RatingBefore}  Get Text    id:neo-vnode-33
    ${RatingBefore}  Convert To Number    ${RatingBefore}
    Click Element    id:neo-vnode-33
    ${ratingAfter}  Get Text    id:neo-vnode-33
    ${ratingAfter}  Convert To Number    ${ratingAfter}
    Should Be Equal    ${ratingAfter}    ${RatingBefore+1}
    Click Element    id:neo-vnode-33
    Run Keyword And Ignore Error    Close Window

Rating_should_back
    Open Browser    ${url3}    ${browser2}
    Wait Until Page Contains Element    id:neo-vnode-20
    ${RatingBefore}  Get Text    id:neo-vnode-33
    ${RatingBefore}  Convert To Number    ${RatingBefore}
    Click Element    id:neo-vnode-33
    Click Element    id:neo-vnode-33
    ${ratingFinal}  Get Text    id:neo-vnode-33
    ${ratingFinal}  Convert To Number    ${ratingFinal}
    Should Be Equal     ${ratingFinal}    ${RatingBefore}
    Run Keyword And Ignore Error    Close Window

Tags_should_not_be_empty
    Open Browser    ${url3}    ${browser2}
    Wait Until Page Contains Element    id:neo-vnode-20
    Should Not Be Empty    class:tag-list
    Run Keyword And Ignore Error    Close Window

Article_title_on_a_list
    Open Browser    ${url3}    ${browser2}
    Wait Until Page Contains Element    id:neo-vnode-20
    Should Not Be Empty    id:neo-vnode-35
    Run Keyword And Ignore Error    Close Window

Article_description_on_a_list
    Open Browser    ${url3}    ${browser2}
    Wait Until Page Contains Element    id:neo-vnode-20
    Should Not Be Empty    id:neo-vnode-36
    Run Keyword And Ignore Error    Close Window

Article_author_on_a_list
    Open Browser    ${url3}    ${browser2}
    Wait Until Page Contains Element    id:neo-vnode-20
    Should Not Be Empty    id:neo-vnode-29
    Run Keyword And Ignore Error    Close Window

Article_tags_on_a_list
    Open Browser    ${url3}    ${browser2}
    Wait Until Page Contains Element    id:neo-vnode-20
    Should Not Be Empty    id:neo-vnode-42
    Run Keyword And Ignore Error    Close Window

Adding_comment_unlog
    Open Browser    ${url3}    ${browser2}
    Wait Until Page Contains Element    id:neo-vnode-20
    Click Element    id:neo-vnode-136
    Wait Until Page Contains Element    id:neo-vnode-247
    Press Keys    id:neo-component-16__input    test_test
    Click Element    id:neo-vnode-247
    #something should happen
    Run Keyword And Ignore Error    Close Window

Adding_empty_comment_unlog
    Open Browser    ${url3}    ${browser2}
    Wait Until Page Contains Element    id:neo-vnode-20
    Click Element    id:neo-vnode-136
    Wait Until Page Contains Element    id:neo-vnode-20
    Click Element    id:neo-vnode-247
    #something should happen
    Run Keyword And Ignore Error    Close Window

Log_in
    Open Browser    ${url3}    ${browser2}
    #SignIn
    SignInGen

Adding_favPost_log_list
    Open Browser    ${url3}    ${browser2}
    #SignIn
    SignInGen
    Click Element    id:neo-vnode-167
    Click Element    class:user-pic
    Click Element    id:neo-vnode-293
    #should appear list
    Should Not Be Empty    id:neo-vnode-293
    Run Keyword And Ignore Error    Close Window

Adding_favPost_log
    Open Browser    ${url3}    ${browser2}
    #SignIn
    SignInGen
    Click Element    id:neo-vnode-186
    Click Element    id:neo-vnode-264
    Click Element    class:user-pic
    Click Element    id:neo-vnode-293
    #should appear list
    Should Not Be Empty    id:neo-vnode-293
    Run Keyword And Ignore Error    Close Window

Write_art
    Open Browser    ${url3}    ${browser2}
    #SignIn
    SignInGen
    Click Element    id:neo-vnode-230
    Press Keys    name:title    TestTitle
    Press Keys    name:description    TestDescription
    Press Keys    name:body    TestBody
    Press Keys    name:tags    TestTag
    Click Element    id:neo-vnode-352
    Click Element    class:user-pic
    Click Element    id:neo-vnode-291
    Should Not Be Empty    id:neo-vnode-291
    #should appear list
    Run Keyword And Ignore Error    Close Window