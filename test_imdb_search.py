def test_imdb_search(driver):
  imdb_search_page = IMDBSearchPage(driver)
  imdb_search_page.open()
  imdb_search_page.fill_search_form(
      name="Vijay",
      searchby="BIRTH_PLACE"
  )
  imdb_search_page.click_search()
  # driver.quit()
