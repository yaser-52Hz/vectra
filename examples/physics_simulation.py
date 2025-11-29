"""
Physics Simulation Example using the Vector Library

This script demonstrates how the vector library can be used for
physics simulations, including forces, velocities, and accelerations.
"""

import math
from vectors import Vector, add, normalize, magnitude


class Particle:
    """Simple particle class for physics simulation."""
    
    def __init__(self, position, velocity, mass=1.0):
        self.position = position
        self.velocity = velocity
        self.mass = mass
    
    def update(self, force, dt):
        """Update particle state based on applied force and time step."""
        # F = ma, so a = F/m
        acceleration = force / self.mass
        
        # v = v0 + a*dt
        self.velocity = self.velocity + (acceleration * dt)
        
        # x = x0 + v*dt
        self.position = self.position + (self.velocity * dt)
        
        return self.position, self.velocity
    
    def __repr__(self):
        return f"Particle(pos={self.position}, vel={self.velocity})"


def simulate_projectile():
    """Simulate projectile motion."""
    print("=" * 60)
    print("Projectile Motion Simulation")
    print("=" * 60)
    
    # Initial conditions
    initial_position = Vector(0, 0, 0)
    initial_velocity = Vector(10, 15, 0)  # 10 m/s horizontal, 15 m/s vertical
    gravity = Vector(0, -9.8, 0)  # Gravity acceleration
    
    particle = Particle(initial_position, initial_velocity, mass=1.0)
    
    print(f"Initial position: {particle.position}")
    print(f"Initial velocity: {particle.velocity}")
    print(f"Gravity: {gravity}")
    print()
    
    dt = 0.1  # Time step
    time = 0
    max_height = 0
    
    print("Time  |  Position        |  Velocity        |  Height")
    print("-" * 60)
    
    for step in range(50):
        # Apply gravity
        force = gravity * particle.mass
        pos, vel = particle.update(force, dt)
        
        height = pos.y
        if height > max_height:
            max_height = height
        
        time += dt
        
        if step % 10 == 0:
            print(f"{time:4.1f}  |  {pos}  |  {vel}  |  {height:.2f}")
        
        # Stop if hit ground
        if pos.y < 0:
            print(f"\nProjectile hit ground at t = {time:.2f}s")
            print(f"Maximum height = {max_height:.2f}m")
            break


def simulate_orbital_motion():
    """Simulate orbital motion around a planet."""
    print("\n\n" + "=" * 60)
    print("Orbital Motion Simulation")
    print("=" * 60)
    
    # Planet at origin
    planet_position = Vector(0, 0, 0)
    
    # Satellite initial conditions
    initial_position = Vector(10, 0, 0)  # 10 units away
    initial_velocity = Vector(0, 2, 0)  # Tangential velocity
    
    particle = Particle(initial_position, initial_velocity, mass=1.0)
    
    print(f"Planet position: {planet_position}")
    print(f"Satellite initial position: {particle.position}")
    print(f"Satellite initial velocity: {particle.velocity}")
    print()
    
    dt = 0.01
    time = 0
    
    print("Time  |  Satellite Position  |  Distance from Planet")
    print("-" * 60)
    
    for step in range(100):
        # Calculate gravitational force (simplified)
        direction = particle.position - planet_position
        distance = magnitude(direction)
        
        if distance > 0.1:  # Avoid division by zero
            normalized_dir = direction / distance
            
            # F = -GMm/r² * direction
            gravitational_constant = 10  # Simplified constant
            force_magnitude = -gravitational_constant / (distance * distance)
            force = normalized_dir * force_magnitude
        else:
            force = Vector(0, 0, 0)
        
        pos, vel = particle.update(force, dt)
        time += dt
        
        if step % 20 == 0:
            print(f"{time:4.2f}  |  {pos}  |  {distance:.3f}")
    
    print("\nNote: This is a simplified orbital simulation for demonstration.")


def calculate_center_of_mass():
    """Calculate center of mass for a system of particles."""
    print("\n\n" + "=" * 60)
    print("Center of Mass Calculation")
    print("=" * 60)
    
    particles = [
        Particle(Vector(0, 0, 0), Vector(0, 0, 0), mass=1.0),
        Particle(Vector(2, 0, 0), Vector(0, 0, 0), mass=2.0),
        Particle(Vector(0, 2, 0), Vector(0, 0, 0), mass=3.0),
    ]
    
    print("Particles:")
    total_mass = 0
    weighted_position_sum = Vector(0, 0, 0)
    
    for i, particle in enumerate(particles):
        print(f"  Particle {i+1}: mass={particle.mass}, position={particle.position}")
        total_mass += particle.mass
        weighted_position_sum = weighted_position_sum + (particle.position * particle.mass)
    
    center_of_mass = weighted_position_sum / total_mass
    print(f"\nTotal mass: {total_mass}")
    print(f"Center of mass: {center_of_mass}")


def main():
    """Run all simulation examples."""
    simulate_projectile()
    simulate_orbital_motion()
    calculate_center_of_mass()
    
    print("\n" + "=" * 60)
    print("All simulations completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

