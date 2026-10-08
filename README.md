# Nappulapeli: Chaotic Party Game

An overengineered autobattling party drinking game built for a friend group trip. Players control characters from an Android app while battles play out live on a shared host screen.

Developed over six months, with a Python/Pygame host and a Kotlin Android client built in Android Studio. This repository contains the Python host.

Forked from the actual repo, with some content removed. Partly in finnish.

## Highlights

- Optimized pathfinding, rendering, and game state ticking.
- A custom socket server for real-time state synchronization across concurrent clients.
- An AI avatar pipeline using background removal and facial recognition to turn player selfies into in-game character cutouts.
- A spatial audio engine written from scratch, supporting 100+ simultaneous sound sources with low-pass filtering and reverb to simulate distance. Released separately as [immersive-audio on PyPI](https://pypi.org/project/immersive-audio/).

Built for chaos.

