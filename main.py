def on_chat():
    mobs.kill(mobs.entities_by_type(mobs.monster(WITCH)))
    blocks.fill(AIR,
        world(120, 70, -609),
        world(146, 97, -591),
        FillOperation.REPLACE)
    blocks.replace(AIR, FIRE, world(120, 68, -609), world(146, 97, -591))
    blocks.replace(AIR, NETHERRACK, world(120, 68, -609), world(146, 97, -591))
    loops.pause(500)
    for index in range(40):
        blocks.place(CAKE, randpos(world(123, 70, -610), world(139, 70, -591)))
player.on_chat("witch-hunters", on_chat)