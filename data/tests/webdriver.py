## Eigentümer: Hüseyin Sümer

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

class BasicUploadTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chromedriver_path = os.path.abspath('chromedriver.exe')
        cls.service = Service(chromedriver_path)
        cls.driver = webdriver.Chrome(service=cls.service)
        cls.driver.implicitly_wait(10)
        cls.base_url = 'http://127.0.0.1:5000/'

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # Testen ob die Problembeschreibung als PDF erfolgreich hochgeladen werden kann

    def test_problembeschreibung_upload(self):
        driver = self.driver
        driver.get(self.base_url)

        file_path = r'C:\Users\49176\OneDrive\Dokumente\24_SoSe_StoryGenerator\datasets\Persona mit Problembeschreibung.pdf' # In dem Fall wird die Problembeschreibung PDF hochgeladen.

        assert os.path.exists(file_path), f"File not found: {file_path}"

        file_input = driver.find_element(By.NAME, 'file')
        submit_button = driver.find_element(By.XPATH, '//form[@action="/input/upload"]//input[@type="submit"]')

        file_input.send_keys(file_path)
        submit_button.click()

        time.sleep(30)

    # Testen ob die Persona Alex Müller PDF Datei hochgeladen werden kann
    def test_persona_upload(self):
        driver = self.driver
        driver.get(self.base_url)#

        file_path = r'C:\Users\49176\OneDrive\Dokumente\24_SoSe_StoryGenerator\generator-llm\artefacts\Persona Alex Mueller\Persona_ Alex Müller.pdf'  # In dem Fall wird die Persona Alex Müller hochgeladen.


        assert os.path.exists(file_path), f"File not found: {file_path}"

        file_input = driver.find_element(By.NAME, 'file')
        submit_button = driver.find_element(By.XPATH, '//form[@action="/input/upload"]//input[@type="submit"]')

        file_input.send_keys(file_path)
        submit_button.click()

        time.sleep(20)



    def test_click_button_generate(self):
        driver = self.driver
        driver.get(self.base_url)

        file_path = r'C:\Users\49176\OneDrive\Dokumente\24_SoSe_StoryGenerator\generator-llm\artefacts\Persona Alex Mueller\Persona_ Alex Müller.pdf'
        assert os.path.exists(file_path), f"File not found: {file_path}"

        file_input = driver.find_element(By.NAME, 'file')
        submit_button = driver.find_element(By.XPATH, '//form[@action="/input/upload"]//input[@type="submit"]')

        file_input.send_keys(file_path)
        submit_button.click()

        time.sleep(30)

        generate_button = driver.find_element(By.XPATH,'//form[@action="/backend/llm/generate_text"]//button[text()="Generieren"]')
        generate_button.click()

    def test_uploaded_files_display(self):
        driver = self.driver
        driver.get(self.base_url)

        file_path = r'C:\Users\49176\OneDrive\Dokumente\24_SoSe_StoryGenerator\generator-llm\artefacts\Persona Alex Mueller\Persona_ Alex Müller.pdf'
        assert os.path.exists(file_path), f"File not found: {file_path}"

        file_input = driver.find_element(By.NAME, 'file')
        submit_button = driver.find_element(By.XPATH, '//form[@action="/input/upload"]//input[@type="submit"]')

        file_input.send_keys(file_path)
        submit_button.click()

        time.sleep(10)


    # Das File Alex Müller.pdf löschen
    def test_delete_uploaded_file(self):
        driver = self.driver
        driver.get(self.base_url)

        file_path = r'C:\Users\49176\OneDrive\Dokumente\24_SoSe_StoryGenerator\generator-llm\artefacts\Persona Alex Mueller\Persona_ Alex Müller.pdf'
        assert os.path.exists(file_path), f"File not found: {file_path}"

        file_input = driver.find_element(By.NAME, 'file')
        submit_button = driver.find_element(By.XPATH, '//form[@action="/input/upload"]//input[@type="submit"]')

        file_input.send_keys(file_path)
        submit_button.click()

        time.sleep(40)

        delete_button = driver.find_element(By.XPATH, '//form[@action="/backend/manage/files"]//button[@name="filenamesSelection" and @value="deleteFile"]')
        delete_button.click()

        time.sleep(20)

        uploaded_files = driver.find_elements(By.XPATH, '//section[@class="file_management"]//input[@type="checkbox"]')
        uploaded_file_names = [file.get_attribute('value') for file in uploaded_files]

        self.assertNotIn("Persona_ Alex Müller.pdf", uploaded_file_names)


    #Überprüfen ob die Beschreibung auf der Website vorhanden ist.
    def test_project_info_display(self):
        driver = self.driver
        driver.get(self.base_url)

        project_info_section = driver.find_element(By.CLASS_NAME, 'project_info')
        self.assertIsNotNone(project_info_section)

        project_info_text = project_info_section.text
        self.assertIn("Data Science Project Sommersemester 2024", project_info_text)
        self.assertIn("Hochschule Neu-Ulm", project_info_text)


if __name__ == "__main__":
    unittest.main()