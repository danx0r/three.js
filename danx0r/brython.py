from browser import document, window

THREE = window.THREE

camera = THREE.PerspectiveCamera.new(70, 1, .01, 10)
camera.position.z = 1.5
scene = THREE.Scene.new()
geometry = THREE.CubeGeometry.new(0.1, 0.4, 0.9)
material = THREE.MeshNormalMaterial.new({"color": "#ffffff"})
mesh = THREE.Mesh.new(geometry, material)
scene.add(mesh)

renderer = THREE.WebGLRenderer.new()
renderer.setSize(1000, 800)

document <= renderer.domElement
renderer.render(scene, camera)

def animate(i):
    # note: three.js includes requestAnimationFrame shim
    window.requestAnimationFrame(animate)

    mesh.rotation.x += 0.01
    mesh.rotation.y += 0.005

    renderer.render(scene, camera)

animate(0)
