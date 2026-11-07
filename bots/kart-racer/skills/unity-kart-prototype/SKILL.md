---
name: unity-kart-prototype
description: Build the drivable core of a kart racer in Unity, handling first.
version: 1.0.0
author: Apex
license: MIT
metadata:
  hermes:
    tags: [unity, kart, physics, gamepad, csharp]
---

# Unity kart prototype

The first milestone is one kart, one flat track, and a drift that feels good.
Content comes after handling, never before.

## Procedure

1. **Project**: Unity 6 LTS, URP, new 3D (URP) template, Linear color, 60 fps target.
   `Assets/Scripts/Kart/` for code, `Assets/Data/` for ScriptableObjects.
2. **Rig**: a `Rigidbody` (mass 180, drag 0.2, angular drag 4), four invisible
   wheel colliders or sphere casts, a visual mesh child that is never collided with.
3. **Input**: one `KartInput` struct fed by the new Input System, with a gamepad
   deadzone of 0.15 and separate analog triggers. Never read `Input.GetAxis` ad hoc.
4. **Drive**: forward force from throttle, speed-scaled steer, and a lateral grip
   term that is high normally and low while drifting:
   ```csharp
   var grip = drifting ? driftGrip : normalGrip;      // 8.0 vs 22.0 m/s^2
   rb.AddForce(-transform.right * Vector3.Dot(rb.velocity, transform.right) * grip);
   ```
5. **Drift**: hop on press (0.12 s), charge while holding + steering, release into
   mini-turbo. Tiers by charge seconds: 0.8 → blue (+8 m/s), 1.6 → orange (+12),
   2.6 → purple (+17). Tune these numbers, do not ship them unmeasured.
6. **Camera**: spring arm behind the kart, FOV 60→72 with speed, slight look-ahead
   along velocity, hard clamp so it never clips track walls.
7. **Track test**: a 200 m oval with a 3 m wall ring and a single checkpoint.
   Time a full lap; under 25 s means the layout is too short to tune on.
8. **Acceptance**: keyboard and gamepad both drive; drift charge is visible;
   reversing does not flip the kart; a 90° wall hit stops it without spinning.

## Anti-patterns

- Wheel colliders tuned for realism. This is arcade; use sphere casts and grip math.
- Building tracks before drift feels right — every track then needs re-tuning.
- Copying Nintendo track geometry or music. Feel is fair; assets are not.
