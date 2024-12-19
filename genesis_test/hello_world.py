import genesis as gs

def main():
    ########################## init ##########################
    gs.init(backend=gs.metal)

    ########################## create a scene ##########################
    scene = gs.Scene(
        show_viewer=True,
        viewer_options=gs.options.ViewerOptions(
            camera_pos=(3.5, 0.0, 2.5),
            camera_lookat=(0.0, 0.0, 0.5),
            camera_fov=40,
            res=(1280, 720)
        )
    )

    ########################## entities ##########################
    plane = scene.add_entity(gs.morphs.Plane())
    franka = scene.add_entity(
        gs.morphs.MJCF(file='xml/franka_emika_panda/panda.xml'),
    )

    ########################## build ##########################
    scene.build()

    # Run simulation in another thread
    gs.tools.run_in_another_thread(fn=run_sim, args=(scene,))
    scene.viewer.start()

def run_sim(scene):
    for i in range(1000):
        scene.step()

if __name__ == "__main__":
    main()