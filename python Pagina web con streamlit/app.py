import streamlit as st
from PIL import Image
import requests #Nos permitira hacer una solicitud a una pagina para incluir el lottie file#
from streamlit_lottie import st_lottie


email_adress = "otsendiaz@gmail.com"


#config
st.set_page_config(page_title="Transapp", page_icon="🤼", layout="wide")


def css_load(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
  
url = "https://lottie.host/0cd49214-bdfd-47e9-8778-8dddb007da7f/qNnhNo3uau.json"  
url2 = "https://lottie.host/f1f35783-0dc7-4061-b9a8-053c843ce641/uMua7DzUoc.json"    
url3 = "https://lottie.host/74d65901-1fa7-4865-a4e1-ac0824613556/idd7IpLzbt.json"  

def load_lottie(url):
    r = requests.get(url)
    if r.status_code !=200:
         return None
    return r.json()

lottie = load_lottie(url)

def load_lottie(url2):
    r = requests.get(url2)
    if r.status_code !=200:
         return None
    return r.json()

lottie2 = load_lottie(url2)

def load_lottie(url3):
    r = requests.get(url3)
    if r.status_code !=200:
         return None
    return r.json()

lottie3 = load_lottie(url3)

css_load("style/style.css")

#image_column, text_column = st.columns((1,2))
#with image_column:
 #   image = Image.open(".imagenes/vdd.jpg")
  #  st.image(image, use_column_width=True)
        
with st.container():
    st_lottie(lottie3, height=800, width=800)
    st.header("                   :wave: i Hola, Somos tu solucion ! :wave:")
    #st.subheader(":wave: i Hola, Somos tu solucion ! :wave:")
    st.title("Creamos soluciones para acelerar tu negocio")
    st.write(
        "Somos unos apasionados de la tecnología y la innovación, especializados en el sector de la digitalización y automatización de negocios. Nos gusta crear soluciones para resolver problemas y mejorar procesos."
    )
    st.write("[Saber más >](https://wa.me/18496385795?text=Estoy%20interesteresado%20en%20onocer%20mas%20sobre%20el%20negocio.%20cuando%20puedas%20contestame%20gracias.)")



# sobre nosotros
with st.container():
    st.write("---")
    left_column, right_column= st.columns((2))
    with left_column:
        st.header("Sobre nosotros")
        st_lottie(lottie, height=300)
        st.write(
            """
            Nuestro objetivo es poder aportar valor a los negocios ayudandoles a ahorrar tiempo y dinero a través de la implantación de nuevas tecnologías como la inteligencia artifical, analisis de datos o implantación de software de automatización.
            Seguramente te vamos a poder ayudar si:

            - Tienes un negocio y quieres mejorar tus procesos de trabajo para ahorrar tiempo y dinero
            - Tienes trabajadores que emplean parte de su jornada a realizar tareas repetitivas sin valor añadido para tu negocio
            - No tienes claras las métricas de tu negocio y quieres tomar decisiones basadas en datos
            - Quieres mejorar la experiencia de tus clientes
            - Usas herramientas de software antiguas o poco eficientes o procesos en los que usas papel y bolígrafo

            ***Si esto suena interesante para ti puedes contactarnos a través del formulario que encontrarás al final de la página*** 
            """
        )
        with right_column:  
         st.header("Continuamos")
         st.write(
            """
            Nuestro objetivo es poder aportar valor a los negocios ayudandoles a ahorrar tiempo y dinero a través de la implantación de nuevas tecnologías como la inteligencia artifical, analisis de datos o implantación de software de automatización.
            Seguramente te vamos a poder ayudar si:

            - Tienes un negocio y quieres mejorar tus procesos de trabajo para ahorrar tiempo y dinero
            - Tienes trabajadores que emplean parte de su jornada a realizar tareas repetitivas sin valor añadido para tu negocio
            - No tienes claras las métricas de tu negocio y quieres tomar decisiones basadas en datos
            - Quieres mejorar la experiencia de tus clientes
            - Usas herramientas de software antiguas o poco eficientes o procesos en los que usas papel y bolígrafo

            ***Si esto suena interesante para ti puedes contactarnos a través del formulario que encontrarás al final de la página*** 
            """)
         st_lottie(lottie2, height=300)
        
        st.write("[Más sobre nosotros>](https://valerapp.com/about/)")
    #with right_column:
     #   st_lottie(load_lottieurl(lottie_file), height=400)

    # servicios
with st.container():
    st.write("---")
    st.header("Nuestros servicios")
    st.write("---")
    #st.write("##")
    
    image_column, text_column = st.columns((1,2))
    
    with image_column:
        image = Image.open(".imagenes/dda.png")
        st.image(image, use_column_width=True)
        
    with text_column:
        st.subheader("Diseño de aplicaciones")
        st.write(
            """
            Si en tus procesos diarios tienes que introducir información en diferentes fuentes de datos o bien tienes que trabajar con documentación en papel, es hora de pensar en implementar una aplicación en tu negocio para potenciar y optimizar el funcionamiento de los procesos diarios.    
            """
        )
        st.write("[Ver servicios >](https://valerapp.com/services/)")

    with st.container():
        st.write("---")
        image_column, text_column = st.columns((1,2))
    with image_column:
        image = Image.open(".imagenes/appinst.png")
        st.image(image, use_column_width=True)
    with text_column:
        st.subheader("Automatización de procesos")
        st.write(
            """
            Si realizas cualquier tipo de tarea repetitiva como por ejemplo introducir datos en excel u otras aplicaciones, gestión de facturas, envío de emails a proveedores etc Lo que quizás necesitas es una automatización de tareas para poder liberar recursos de esas actividades y poder emplearlos en otras tareas más productivas.
            """
        )
        st.write("[Ver servicios >](https://valerapp.com/services/)")

with st.container():
    st.write("---")
    #st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        image = Image.open(".imagenes/vdd.jpg")
        st.image(image, use_column_width=True)
    with text_column:
        st.subheader("Visualización de datos")
        st.write(
            """
            Si sientes que no tienes una visión clara de datos de tu negocio lo que necesitas es una aplicación en la que puedas tener toda la información de interes de tu empresa.
            """
        )
        st.write("[Ver servicios >](https://valerapp.com/services/)")

with st.container():
    st.write("---")
    st.header("Ponte en contacto con nosotros! 💌")
    contact_form = f""" <form action="https://formsubmit.co/{email_adress}" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Tu nombre" required>
        <input type="email" name="email" placeholder="Tu email" required>
        <textarea name="message" placeholder="Tu mensaje aquí" required></textarea>
        <button type="submit">Enviar</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()