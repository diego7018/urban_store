import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from fastapi.responses import HTMLResponse 
import uvicorn


app = FastAPI()

# Definir la carpeta de imágenes en el directorio del proyecto
image_dir = "images"

# Crear la carpeta si no existe
if not os.path.exists(image_dir):
    os.makedirs(image_dir)

# Montar la carpeta para servir archivos estáticos
app.mount("/images", StaticFiles(directory=image_dir), name="images")

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Tienda de Ropa</title>
        <link rel="icon" type="image/png" href="/images/logo.jpg">
        <style>
            body {
                background-color: #ffffff;
                color: #333;
                font-family: 'Arial', sans-serif;
                text-align: center;
                margin: 0;
                padding: 0;
                overflow-x: hidden;
            }
            .menu {
                background-color: transparent;
                padding: 15px;
                position: fixed;
                left: 0;
                top: 0;
                width: 100%;
                display: flex;
                align-items: center;
                transition: background 0.3s;
                z-index: 1000;
            }
            .menu-items {
                display: none;
                flex-direction: column;
                position: absolute;
                top: 50px;
                left: 10px;
                background: white;
                padding: 10px;
                border-radius: 5px;
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
            }
            .menu a {
                text-decoration: none;
                color: black;
                font-size: 18px;
                padding: 10px;
                display: block;
            }
            .menu-icon {
                font-size: 30px;
                cursor: pointer;
                display: block;
                color: black;
                margin-left: 20px;
            }
            .banner-container {
                width: 100%;
                height: 600px; /* Aumentamos la altura del banner principal */
                display: flex;
                align-items: center;
                justify-content: center;
                position: relative;
                background: url(/images/banner1.png) no-repeat center center; /* Banner común */
                background-size: cover; /* La imagen cubrirá toda la área del banner */
            }
            .banner-text {
                font-size: 50px; /* Aumentamos el tamaño del texto */
                font-weight: bold;
                color: white;
                text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.7);
                text-align: center;
            }
            .products {
                display: flex;
                justify-content: center;
                gap: 20px;
                flex-wrap: wrap;
                margin-top: 80px; /* Aumentamos el espacio entre el banner principal y los productos */
            }
            .product {
                background-color: #f4f4f4;
                border-radius: 10px;
                width: 300px;
                text-align: center;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
                margin: 20px;
                position: relative;
            }
            .product-banner {
                width: 100%;
                height: 150px; /* El banner de cada producto será más bajo (horizontal) */
                background-size: cover;
                background-position: center;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
            }
            .product img {
                width: 200px;
                height: 200px;
                object-fit: cover;
                border-radius: 10px;
                margin-top: -40px; /* Alineamos la imagen por encima del borde del banner */
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
            }
            .product p {
                margin-top: 10px;
                font-size: 18px;
                font-weight: bold;
            }
            .buy-button {
                background-color: #25D366;
                color: white;
                border: none;
                padding: 15px;
                margin-top: 10px;
                cursor: pointer;
                font-size: 18px;
                border-radius: 5px;
                transition: background 0.3s;
                width: 100%;
                font-weight: bold;
            }
            .buy-button:hover {
                background-color: #128C7E;
            }
            .whatsapp-button {
                position: fixed;
                bottom: 20px;
                right: 20px;
                width: 60px;
                height: 60px;
                cursor: pointer;
                z-index: 1000;
            }
            .marquee-container {
                position: fixed;
                bottom: 0;
                width: 100%;
                background: black;
                color: white;
                padding: 10px 0;
                overflow: hidden;
                white-space: nowrap;
            }
            .marquee-text {
                display: inline-block;
                font-size: 20px;
                font-weight: bold;
                animation: marquee 10s linear infinite;
            }
            @keyframes marquee {
                from { transform: translateX(100%); }
                to { transform: translateX(-100%); }
            }
        </style>
        <script>
            document.addEventListener("DOMContentLoaded", function() {
                const menuIcon = document.querySelector(".menu-icon");
                const menuItems = document.querySelector(".menu-items");
                menuIcon.addEventListener("click", function() {
                    if (menuItems.style.display === "none" || menuItems.style.display === "") {
                        menuItems.style.display = "block";
                    } else {
                        menuItems.style.display = "none";
                    }
                });
            });
        </script>
    </head>
    <body>
        <div class="menu">
            <span class="menu-icon">☰</span>
            <div class="menu-items">
                <a href="/">Ropa</a>
                <a href="/sobre-nosotros">Sobre Nosotros</a>
                <a href="/contacto">Contáctanos</a>
            </div>
        </div>
        <div class="banner-container">
            <span class="banner-text">¡Bienvenido a Urban Store ™!</span>
        </div>
        <div class="products">
            <!-- 🔹 Productos -->
            """ + "".join([
                f'<div class="product">'
                f'<div class="product-banner" style="background-image: url(/images/product-banner{i}.jpg);"></div>'  # Banner horizontal de cada producto
                f'<img src="/images/ropa{i}.jpg" alt="Producto {i}">'  # Imagen del producto
                f'<p>{"Título Especial del Producto 1" if i == 1 else f"Producto {i}"}</p>'
                f'<button class="buy-button" onclick="window.location.href=\'https://wa.me/1234567890\'">Comprar</button>'
                f'</div>'
                for i in range(1, 15)
            ]) + """
        </div>
        <img src="/images/whatsapp.png" alt="WhatsApp" class="whatsapp-button" onclick="window.location.href='https://wa.me/1234567890'">
        <div class="marquee-container"><span class="marquee-text"> Urban Store ™ - Las mejores prendas para ti 🔥 Envío GRATIS por compras mayores a S/150 🔥 • </span></div>
    </body>
    </html>
    """

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
