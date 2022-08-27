# from browser import timer
import asyncio

async def main(THREE, plat, renderer, window, create_proxy):
    camera = THREE.PerspectiveCamera.new(70, 1, .01, 10)
    camera.position.z = 1.5
    scene = THREE.Scene.new()
    geometry = THREE.CylinderGeometry.new(0.03, 0.03, 1)
    args = {'color': "#888888", 'emissive': "#555555"}
    if plat=="brython":
        #brython wants a dict
        material = THREE.MeshLambertMaterial.new(args)
    else:
        #pyscript expects keywords
        # material = THREE.MeshLambertMaterial.new(color="#888888", emissive="#555555")
        material = THREE.MeshLambertMaterial.new(**args)
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
        mesh.rotation.z += 0.005
        renderer.render(scene, camera)

    # animate(0)
    renderer.render(scene, camera)
    await asyncio.sleep(1)
    mesh.rotation.x += 1
    mesh.rotation.z += 2
    renderer.render(scene, camera)
