# Nappulapeli: Chaotic Party Game

An overengineered autobattling party game originally built for a trip with friends. Players customize their characters through an Android companion app while AI-controlled battles unfold on a shared screen.

Developed over six months using **Python/Pygame** for the game host and **Kotlin/Android Studio** for the companion app.

This repository contains the Python host. It is a stripped-down fork of the original project, with some private content removed. Parts of the game is in Finnish.

## Technical Highlights

- Game AI and performance: Optimized pathfinding, rendering, and game-state simulation to squeeze every last frame out of poor old Pygame.
- **Multiplayer networking:** Custom WebSocket server handling concurrent Android clients and real-time game-state synchronization.
- **AI avatar generation:** Automated image-processing pipeline using background removal and face detection to turn player selfies into in-game characters.
- **Spatial audio:** Custom audio engine supporting 100+ simultaneous sound sources, with positional panning, distance-based low-pass filtering, and reverb since Pygames audio sucks. Released separately as [immersive-audio on PyPI](https://pypi.org/project/immersive-audio/).

The Android app can be found [here](https://github.com/vsalli12/nappulapeli-app)

## About This Repository

This project was designed specifically for a small group of friends, rather than public distribution. The repository is provided primarily as a technical showcase and is not intended as a ready-to-run release.

Built for chaos.
