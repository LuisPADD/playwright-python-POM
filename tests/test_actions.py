from playwright.sync_api import Page, expect

def test_actions(page: Page) -> None:
    page.set_viewport_size({"width":1920,"height":1080})
    page.goto("https://leogcarvalho.github.io/test-automation-practice/")
    
    #page.get_by_role("textbox", name="Username: (admin)").fill("admin")
    #page.get_by_role("textbox", name="Password: (1234)").fill("1234")
    
    # fill & keys
    page.get_by_role("textbox", name="Username: (admin)").fill("admin")
    page.get_by_role("textbox", name="Username: (admin)").press("Tab")
    page.get_by_role("textbox", name="Password: (1234)").fill("1234")
    page.get_by_role("textbox", name="Password: (1234)").press("Enter")
    expect(page.get_by_text("Login successful!")).to_be_visible()


    #Press_sequentially
    # page.get_by_role("textbox", name="Username: (admin)").press_sequentially("admin",delay=100)
    # page.get_by_role("textbox", name="Password: (1234)").press_sequentially("1234",delay=100)
    # page.get_by_role("textbox", name="Select a date:").press_sequentially("10102000",delay=100)

    # check
    page.get_by_role("checkbox",name="Feature 1").check()
    expect(page.get_by_role("checkbox",name="Feature 1")).to_be_checked()
    page.get_by_role("radio",name="Option B").check()
    expect(page.get_by_role("radio",name="Option B")).to_be_checked()

    # select_option
    page.get_by_label("Choose an option:").select_option(value="option3")

    # mouse actions
    page.get_by_text("single Click").click()
    expect(page.get_by_text("Single Click button clicked successfully!")).to_be_visible()
    page.get_by_text("Double Click").dblclick()
    expect(page.get_by_text("Double Click button clicked successfully!")).to_be_visible()
    page.get_by_text("Right Click").click(button="right")
    expect(page.get_by_text("Right click button clicked successfully!")).to_be_visible()
    page.get_by_text("Shift + Click").click(modifiers=["Shift"])
    expect(page.get_by_text("Shift + click button clicked successfully!")).to_be_visible()
    page.get_by_text("Hover Menu").hover()
    page.locator('//*[@class="dropdown-content"]/*[text()="Option 1"]').click()
    expect(page).to_have_url("https://leogcarvalho.github.io/test-automation-practice/#option1")

    # file upload
    page.get_by_role("button", name="Choose File").set_input_files("files/sample1.pdf")
    expect(page.get_by_text("Selected File: sample1.pdf")).to_be_visible()

    #clear uploaded files
    page.get_by_role("button", name="Choose File").set_input_files([])

    #drag n drop
    page.get_by_text("Drag me").drag_to(page.get_by_text("Drop here"))
    expect(page.get_by_text("Drop here")).to_be_visible()
