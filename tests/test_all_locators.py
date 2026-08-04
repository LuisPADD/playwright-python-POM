from playwright.sync_api import Page, expect

def test_all_locators(page: Page):
    page.goto("https://leogcarvalho.github.io/test-automation-practice/playwright-locators.html")

    #get_by_role
    expect (page.get_by_role("button", name="Explicit Role Button")).to_be_visible()
    expect (page.get_by_role("link", name="Explicit Role link")).to_be_visible()
    expect (page.get_by_role("img", name="robot icon")).to_be_visible()
    expect (page.get_by_role("button", name="Implicit Button")).to_be_visible()
    expect (page.get_by_role("link", name="Implicit Link")).to_be_visible()

    
    

    