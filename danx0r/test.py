from browser import document, window

THREE = window.THREE

camera = THREE.PerspectiveCamera.new(70, 1, .01, 10)
camera.position.z = 1
scene = THREE.Scene.new()
geometry = THREE.CubeGeometry.new(0.2, 0.2, 0.2)
material = THREE.MeshBasicMaterial.new({"color": "#ffffff", "wireframe": True})
mesh = THREE.Mesh.new(geometry, material)
scene.add(mesh)

renderer = THREE.WebGLRenderer.new()
renderer.setSize(600, 600)

document <= renderer.domElement
renderer.render(scene, camera)

def animate(i):
    # note: three.js includes requestAnimationFrame shim
    window.requestAnimationFrame(animate)

    mesh.rotation.x += 0.01
    mesh.rotation.y += 0.02

    renderer.render(scene, camera)

animate(0)
