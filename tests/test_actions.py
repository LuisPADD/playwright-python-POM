from playwright.sync_api import Page, expect

def test_actions(page: Page) -> None:
    page.goto("https://leogcarvalho.github.io/test-automation-practice/")
    # page.get_by_role("textbox", name="Username: (admin)").fill("admin")
    # page.get_by_role("textbox", name="Password: (1234)").fill("1234")
    page.get_by_role("textbox", name="Username: (admin)").press_sequentially("admin",delay=500)
    page.get_by_role("textbox", name="Password: (1234)").press_sequentially("1234",delay=500)
    page.get_by_role("textbox", name="Select a date:").press_sequentially("10102000",delay=500)
    page.get_by_role("button", name="Login").click()
    page.get_by_text("Login successful!").click()
