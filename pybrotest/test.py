try:
    from pyodide import create_proxy
    from js import THREE, document, window
    renderer = THREE.WebGLRenderer.new()
    container = document.querySelector('#container')
    container.append(renderer.domElement)
    plat = "pyscript"
except:
    from browser import document, window
    THREE = window.THREE
    renderer = THREE.WebGLRenderer.new()
    document <= renderer.domElement
    def create_proxy(p):
        return p
    plat = "brython"


camera = THREE.PerspectiveCamera.new(70, 1, .01, 10)
camera.position.z = 1.5
scene = THREE.Scene.new()
geometry = THREE.CubeGeometry.new(0.1, 0.4, 0.9)
material = THREE.MeshNormalMaterial.new({"color": "#ffffff"})
mesh = THREE.Mesh.new(geometry, material)
scene.add(mesh)
renderer.setSize(1000, 800)
renderer.render(scene, camera)

def animate(i):
    # note: three.js includes requestAnimationFrame shim
    window.requestAnimationFrame(create_proxy(animate))
    mesh.rotation.x += 0.01
    mesh.rotation.y += 0.005
    renderer.render(scene, camera)

animate(0)
