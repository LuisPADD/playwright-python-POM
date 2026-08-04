from playwright.sync_api import Page, expect
import time

def test_all_locators(page: Page):
    page.goto("https://leogcarvalho.github.io/test-automation-practice/playwright-locators.html")

    #get_by_role
    expect (page.get_by_role("button", name="Explicit Role Button")).to_be_visible()
    expect (page.get_by_role("link", name="Explicit Role link")).to_be_visible()
    expect (page.get_by_role("img", name="robot icon")).to_be_visible()
    expect (page.get_by_role("button", name="Implicit Button")).to_be_visible()
    expect (page.get_by_role("link", name="Implicit Link")).to_be_visible()

    #get_by_text
    expect(page.get_by_text("Locate elements by their visible text content.",exact=True)).to_be_visible()
    
    #get_by_label
    expect(page.get_by_label("Email Address", exact=True)).to_be_visible()
    page.get_by_label("Email").fill("teste@gmail.com")
    expect(page.get_by_label("Accept Terms and Conditions")).to_be_visible()
    page.get_by_label("Accept").click()

    #get_by_placeholder
    page.get_by_placeholder("Search For Items...").click()
    page.get_by_placeholder("Enter your password").fill("MinhaSenha")

    time.sleep(3)


    