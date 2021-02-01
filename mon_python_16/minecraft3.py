from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()


pos = mc.player.getTilePos()
block = 56

mc.setBlocks(pos.x, pos.y, pos.z, 
			pos.x + 10, pos.y, pos.z + 15, block)
