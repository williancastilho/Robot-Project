*** Settings ***
Library           RPA.Browser.Selenium
Library           ../resources/page_objects/yahoo_finance_page.py

*** Test Cases ***
Create Yahoo Finance Account
    Yahoo Finance Page.Open Yahoo Finance
    Yahoo Finance Page.Click Sign Up
    Yahoo Finance Page.Fill Registration Form    mynewuser    mynewuser@example.com    MySecurePassword123
    Yahoo Finance Page.Submit Registration Form
    Yahoo Finance Page.Wait For Confirmation
    [Teardown]    Close Browser
