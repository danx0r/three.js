try:
    from browser import document, window
    import browser.aio as aio

    plat = "brython"
except:
    plat = "pyscript"

from testlib import main

if plat == "brython":
    THREE = window.THREE
    renderer = THREE.WebGLRenderer.new()
    document <= renderer.domElement
    def create_proxy(p):
        return p
    aio.run(main(THREE, plat, renderer, window, create_proxy))
# else:
#     from pyodide import create_proxy
#     from js import THREE, document, window
#     renderer = THREE.WebGLRenderer.new()
#     container = document.querySelector('#container')
#     container.append(renderer.domElement)
#     await main(THREE, plat, renderer, window, create_proxy)
