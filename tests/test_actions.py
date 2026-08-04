from playwright.sync_api import Page, expect

def test_actions(page: Page) -> None:
    page.goto("https://leogcarvalho.github.io/test-automation-practice/")
    #page.get_by_role("textbox", name="Username: (admin)").fill("admin")
    #page.get_by_role("textbox", name="Password: (1234)").fill("1234")


    #Press_sequentially
    page.get_by_role("textbox", name="Username: (admin)").press_sequentially("admin",delay=500)
    page.get_by_role("textbox", name="Password: (1234)").press_sequentially("1234",delay=500)
    page.get_by_role("textbox", name="Select a date:").press_sequentially("10102000",delay=500)

    # check
    page.get_by_role("checkbox",name="Feature 1").check()
    expect(page.get_by_role("checkbox",name="Feature 1")).to_be_checked()
    page.get_by_role("radio",name="Option B").check()
    expect(page.get_by_role("radio",name="Option B")).to_be_checked()

    # select_option
    page.get_by_label("Choose an option:").select_option(value="option3")