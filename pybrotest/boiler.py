from testlib import main
try:
    from browser import document, window
    THREE = window.THREE
    renderer = THREE.WebGLRenderer.new()
    document <= renderer.domElement
    def create_proxy(p):
        return p
    plat = "brython"
    main(THREE, plat, renderer, window, create_proxy)
except:
    from pyodide import create_proxy
    from js import THREE, document, window
    renderer = THREE.WebGLRenderer.new()
    container = document.querySelector('#container')
    container.append(renderer.domElement)
    plat = "pyscript"
    main(THREE, plat, renderer, window, create_proxy)
