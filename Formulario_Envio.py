from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium import webdriver
import time
import unittest


#llenado de formulario y envio de formmulario
class inicio(unittest.TestCase):
    
    #ruta de web driver con chrome
    def setUp(self):                 
        self.driver = webdriver.Chrome(executable_path=r"")#ingresar la ruta de de webdriver
    
    #inicializar sitio web, y entrando al formulario de contacto para llenar y enviar 
    def test_busqueda_envio_formulario(self):
        self.driver.get('')
        time.sleep(4)
        inicio = self.driver.find_element_by_xpath('')
        nosotros = self.driver.find_element_by_xpath('')
        portafolio = self.driver.find_element_by_xpath('')
        contacto = self.driver.find_element_by_xpath('')
        
        
        #recorrido de pestañas hasta llegar al form 
        seleccionar = ActionChains(self.driver)
        seleccionar.move_to_element(inicio).move_to_element(nosotros).move_to_element(portafolio).move_to_element(contacto).click().perform()
        time.sleep(3)
        
                
        #declaracion de variables    
        nombre = ""
        correo = ""
        telefono = ""
        asunto = ""
        mensaje = ""
        
        #llenado de informacion de elementos 
        boton_name =  self.driver.find_element_by_xpath('')
        boton_name.send_keys(nombre)
        boton2_mail = self.driver.find_element_by_xpath('')
        boton2_mail.send_keys(correo)
        boton3_telefono = self.driver.find_element_by_xpath('')
        boton3_telefono.send_keys(telefono)
        boton4_asunto = self.driver.find_element_by_xpath('')
        boton4_asunto.send_keys(asunto) 
        boton5_mensaje = self.driver.find_element_by_xpath('')
        boton5_mensaje.send_keys(mensaje)
        time.sleep(3)
        enviar = self.driver.find_element_by_xpath('')
        enviar.click()

    
    
    def tearDown(self):
        self.driver.quit()
        time.sleep(3)
        
        
if __name__ == '__main__':
    unittest.main()