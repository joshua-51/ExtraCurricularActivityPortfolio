from ursina import *

app = Ursina()

# --- Window & Environment ---
window.title = 'PolyTrack Python Edition'
window.borderless = False
window.exit_button.visible = False
window.color = color.black

Sky()
sun = DirectionalLight()
sun.look_at(Vec3(1, -1, 1))

# --- Track Building System ---
# We define a helper to make track pieces quickly
def track_piece(pos, scale, rot=(0,0,0), col=color.gray):
    return Entity(model='cube', position=pos, scale=scale, rotation=rot, 
                  color=col, collider='box', texture='white_cube')

# Create the Course Layout
track_parts = [
    # Start Straight
    track_piece((0, 0, 0), (20, 1, 60), col=color.dark_gray),
    # First Ramp Up
    track_piece((0, 5, 50), (20, 1, 40), rot=(-20, 0, 0), col=color.gray),
    # High Platform
    track_piece((0, 12, 100), (20, 1, 60), col=color.dark_gray),
    # The Big Jump Gap (Empty space here)
    # Landing Zone
    track_piece((0, 0, 200), (30, 1, 80), col=color.dark_gray),
    # Banked Left Turn
    track_piece((40, 0, 240), (60, 1, 30), rot=(0, 45, 10), col=color.blue),
    # Return Straight
    track_piece((100, 0, 240), (100, 1, 20), rot=(0, 90, 0), col=color.dark_gray),
    # Finish Line / Obstacle
    track_piece((150, 2, 240), (5, 10, 20), col=color.red),
]

# --- Car Class ---
class PolyCar(Entity):
    def __init__(self):
        super().__init__(
            model='cube', color=color.orange, scale=(1.5, 0.7, 3),
            position=(0, 2, 0), collider='box'
        )
        self.speed = 0
        self.velocity_y = 0
        self.max_speed = 60
        self.accel = 40
        self.friction = 0.96

    def update(self):
        # 1. Advanced Gravity (Raycasting for Slopes)
        # We check slightly ahead of the car to stick to ramps better
        ray = raycast(self.world_position + (0,2,0), self.down, distance=3, ignore=(self,))
        
        if ray.hit:
            self.velocity_y = 0
            # Alignment to slope (The "Poly" feel)
            self.y = lerp(self.y, ray.world_point.y + 0.5, time.dt * 15)
            # Tilt car to match the surface normal
            self.rotation_x = lerp(self.rotation_x, ray.entity.rotation_x, time.dt * 10)
        else:
            self.velocity_y -= 40 * time.dt # Heavy gravity for jumps
            self.rotation_x = lerp(self.rotation_x, 0, time.dt * 2) # Level out in air
        
        self.y += self.velocity_y * time.dt

        # 2. Controls
        move = held_keys['w'] - held_keys['s']
        self.speed += move * self.accel * time.dt
        self.speed *= self.friction
        self.speed = clamp(self.speed, -20, self.max_speed)

        # 3. Steering (Sharper at speed)
        if abs(self.speed) > 1:
            steer = held_keys['d'] - held_keys['a']
            self.rotation_y += steer * 100 * time.dt * (self.speed / 40)

        # 4. Movement
        self.position += self.forward * self.speed * time.dt

        # 5. Camera (Dynamic Zoom)
        cam_target = self.position + self.back * 15 + self.up * 7
        camera.position = lerp(camera.position, cam_target, time.dt * 5)
        camera.look_at(self.position + self.forward * 5)

car = PolyCar()

# --- UI & Restart ---
speed_label = Text(text='0', position=(-0.8, -0.4), scale=4, color=color.white)

def update():
    speed_label.text = f"{round(abs(car.speed))} KM/H"
    
    # Check if we fell off the track
    if car.y < -50:
        reset_car()

def reset_car():
    car.position = (0, 2, 0)
    car.rotation = (0, 0, 0)
    car.speed = 0

def input(key):
    if key == 'r': reset_car()
    if key == 'escape': quit()

app.run()