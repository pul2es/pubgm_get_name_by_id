import re
from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(channel="chrome", headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.midasbuy.com/midasbuy/uz/buy/pubgm")
    page.locator("div").filter(has_text=re.compile(r"^ВОЙДИТЕ, ЧТОБЫ НАСЛАЖДАТЬСЯ VIP-ПРИВИЛЕГИЯМИ!VIP получают очки опыта\.$")).locator("i").click(no_wait_after=True)
    page.get_by_text("Введите свой идентификатор игрока сейчас").click(no_wait_after=True)
    page.get_by_placeholder("Введите ID игрока").click(no_wait_after=True)
    # ID kiritiladigan maydon!
    page.get_by_placeholder("Введите ID игрока").fill("51725881929", no_wait_after=True) # bu yerga id kiritiladi
    page.get_by_text("Окей").click(no_wait_after=True)
    name = page.locator('span.UserTabBox_name__4ogGM')
    name.click(no_wait_after=True)
    name_text = name.inner_text()
    print(name_text)
    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)