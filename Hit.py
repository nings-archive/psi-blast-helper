class Hit:
    XPATH_DESCRIPTION = ".//a[@class='deflnDesc']"
    XPATH_CHECKBOX = ".//input[@name='checked_GI']"
    XPATH_CHECKMARK = ".//img"

    def __init__(self, web_element):
        self.web_element = web_element
        self.update_attributes()

    def select(self): self.select_for_PSI_BLAST()

    def deselect(self): self.deselect_for_PSI_BLAST()

    def update_attributes(self):
        self.description = (
            self.web_element.
                find_element_by_xpath(self.XPATH_DESCRIPTION)
                .text
        )
        self.accession = (
            self.web_element
                .find_element_by_xpath(self.XPATH_DESCRIPTION)
                .get_attribute('accs')
        )
        self.will_use_for_PSI_BLAST = (
            self.web_element
                .find_element_by_xpath(self.XPATH_CHECKBOX)
                .get_attribute('checked') is not None
        )
        self.was_used_for_PSSM = (
            not 'hidden' in
            self.web_element
                .find_element_by_xpath(self.XPATH_CHECKMARK)
                .get_attribute('class')
        )

    def select_for_PSI_BLAST(self):
        self.update_attributes()
        if not self.will_use_for_PSI_BLAST:
            self.toggle_will_use_for_PSI_BLAST()

    def deselect_for_PSI_BLAST(self):
        self.update_attributes()
        if self.will_use_for_PSI_BLAST:
            self.toggle_will_use_for_PSI_BLAST()

    def toggle_will_use_for_PSI_BLAST(self):
        checkbox = self.web_element.find_element_by_xpath(self.XPATH_CHECKBOX)
        # scroll to element, otherwise error
        checkbox.location_once_scrolled_into_view
        checkbox.click()
