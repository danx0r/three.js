def main(THREE, plat, renderer, window, create_proxy):
    camera = THREE.PerspectiveCamera.new(70, 1, .01, 10)
    camera.position.z = 1.5
    scene = THREE.Scene.new()
    geometry = THREE.CubeGeometry.new(0.1, 0.4, 0.9)
    if plat=="brython":
        material = THREE.MeshLambertMaterial.new({'color': "#ffffff", 'emissive': "#555555"})
    else:
        material = THREE.MeshLambertMaterial.new(emissive="#555555")
    # material.wireframe=True
    mesh = THREE.Mesh.new(geometry, material)
    scene.add(mesh)
    light = THREE.PointLight.new(0xffffff, 1, 0, 2)
    light.position.set(2, 2, 2)
    scene.add(light)
    renderer.setSize(1000, 800)
    renderer.render(scene, camera)

    def animate(i):
        # note: three.js includes requestAnimationFrame shim
        window.requestAnimationFrame(create_proxy(animate))
        mesh.rotation.x += 0.01
        mesh.rotation.y += 0.005
        renderer.render(scene, camera)

    animate(0)
