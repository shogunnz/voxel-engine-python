from settings import *
import moderngl as mgl
import pygame as pg
import sys

class VoxelEngine: # The VoxelEngine class initializes the game engine, handles updates, rendering, and events.
    def __init__(self): # class constructer
        pg.init()
        # Initializes Pygame
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        pg.display.gl_set_attribute(pg.GL_DEPTH_SIZE, 24) # depth buffer. set to 24-bit for proper 3D rendering

        pg.display.set_mode(WIN_RES, flags=pg.OPENGL | pg.DOUBLEBUF) # Creates an OpenGL-enabled Pygame window using WIN_RES (resolution from settings.py).
        # uses double buffering (pg.doublebuf) to prevent flickering
        self.ctx = mgl.create_context() # Creates an OpenGL context using ModernGL.

        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE | mgl.BLEND)
        self.ctx.gc_mode = 'auto'
        # Enables:
        # Depth Testing (mgl.DEPTH_TEST) for correct 3D rendering.
        # Face Culling (mgl.CULL_FACE) to avoid rendering hidden faces of objects.
        # Blending (mgl.BLEND) for transparency effects.
        # Sets automatic garbage collection mode for OpenGL resources.

        self.clock = pg.time.Clock() # Initializes Pygame’s Clock to regulate the frame rate.
        self.delta_time = 0 # delta_time tracks frame duration.
        self.time = 0 # time stores elapsed time.
        self.is_running = True # is_running controls the game loop.
        
    # Game Loop Methods:
    def update(self): # for updating the state of objects
        self.delta_time = self.clock.tick() # Limits the frame rate and calculates time between frames (delta_time).
        self.time = pg.time.get_ticks() * 0.001 # Updates the elapsed time in seconds (time).
        pg.display.set_caption(f'{self.clock.get_fps() :.0f}') # Updates the window title bar with the current FPS.

    def render(self): # for rendering objects
        self.ctx.clear() # Clears the OpenGL frame buffer.
        pg.display.flip() # Swaps buffers (pg.display.flip()) to display the render time

    def handle_events(self): # for handling events and calling the main application
        for event in pg.event.get(): # Checks for window close (pg.quit) or escape key press (pg.K_ESCAPE) to exit the game loop
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.is_running = False

    def run (self): # Main Game Loop
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()
        pg.quit()
        sys.exit()
        # Runs a game loop that:
        # Handles events (e.g., quitting).
        # Updates the game state.
        # Renders the frame.
        # Exits the program when is_running is False.

# Running the Engine
if __name__ == '__main__':
    app = VoxelEngine()
    app.run()
    # If the script is run directly (not imported), it creates an instance of VoxelEngine and starts the main loop.