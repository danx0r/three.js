from testlib import main
try:
    from browser import document, window
    plat = "brython"
except:
    plat = "pyscript"

if plat == "brython":
    THREE = window.THREE
    renderer = THREE.WebGLRenderer.new()
    document <= renderer.domElement
    def create_proxy(p):
        return p
    main(THREE, plat, renderer, window, create_proxy)
else:
    from pyodide import create_proxy
    from js import THREE, document, window
    renderer = THREE.WebGLRenderer.new()
    container = document.querySelector('#container')
    container.append(renderer.domElement)
    main(THREE, plat, renderer, window, create_proxy)
