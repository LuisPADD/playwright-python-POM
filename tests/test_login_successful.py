
from playwright.sync_api import Page, expect
import time

def test_login_successful(page: Page) -> None:
    #page.set_viewport_size({"width":800,"height":600})
    #pytest --device="iPhone 15" https://leogcarvalho.github.io/test-automation-practice/ - Colocar em Device especifico
    page.goto("https://leogcarvalho.github.io/test-automation-practice/")
    page.get_by_role("textbox", name="Username: (admin)").click()
    page.get_by_role("textbox", name="Username: (admin)").fill("admin")
    page.get_by_role("textbox", name="Password: (1234)").click()
    page.get_by_role("textbox", name="Password: (1234)").fill("1234")
    page.get_by_role("button", name="Login").click()
    page.get_by_text("Login successful!").click()
    expect(page.get_by_text("Login successful!")).to_be_visible()
