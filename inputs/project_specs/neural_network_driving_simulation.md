# Project Spec: Neural Network Driving Simulation

## Resume Title

Neural Network Driving Simulation

## Repositories / Links

- https://github.com/ObaidaKandakji/Neural-Network-Driving-Simulation.git

## Project Type

ML simulation prototype (browser-based autonomous driving demo)

## Problem It Solves

Demonstrates how autonomous driving behavior can be simulated in-browser without external AI/game libraries.  
Combines sensing, control, scoring, and visualization to make neural-network-driven decisions inspectable in real time.

## What Was Actually Built

- Browser simulation with road rendering, traffic vehicles, and car movement/collision logic.
- AI-controlled cars using sensor rays and a hand-built feed-forward neural network.
- Generation loop that scores cars, ranks parents, mutates offspring, and restarts runs.
- Live neural-network visualizer on a separate canvas.
- UI controls and status panel for save/reset, generation count, active cars, fitness, and passes.
- Persistence of the best compatible brain using `localStorage`.

## Tech Stack (Verified)

- Vanilla JavaScript
- HTML5
- CSS3
- HTML Canvas API
- Browser `localStorage` (Web Storage API)

## Allowed Keywords (With Evidence)

- `vanilla JavaScript`: `README.md` (states vanilla JS), `main.js`, `car.js`, `network.js`
- `HTML Canvas`: `index.html` (`carCanvas`, `networkCanvas`), `main.js` (`getContext("2d")`)
- `neural network`: `network.js` (`NeuralNetwork`, `Level`), `car.js` (`new NeuralNetwork([this.sensor.rayCount,8,4])`)
- `evolutionary mutation`: `main.js` (`breedNextGeneration`, parent selection), `network.js` (`NeuralNetwork.mutate`)
- `ray-casting sensors`: `sensor.js` (`rayCount=7`, ray casting and nearest intersection reading)
- `collision detection`: `car.js` (`#assessDamage`), `utils.js` (`polysIntersect`, `getIntersection`)
- `real-time visualization`: `main.js` (`requestAnimationFrame(animate)`), `visualizer.js` (network drawing)
- `localStorage persistence`: `main.js` (`save`, `discard`, `loadSavedBrain`, compatibility checks)

## Do Not Claim

- Reinforcement learning (Q-learning, policy gradients, PPO, DQN).
- Backpropagation or gradient-based training.
- TensorFlow, PyTorch, scikit-learn, or any external ML framework usage.
- Computer vision/camera input processing.
- Backend services, APIs, databases, or cloud deployment.
- Distributed training or multi-node compute.
- Production autonomous driving/ADAS safety claims.
- Measured model accuracy, precision/recall, or benchmark speedups.

## Metrics / Outcomes

- Configured population size: `100` AI cars per generation.
- Configured network shape: `7 -> 8 -> 4`.
- Configured generation cutoff: `1800` frames max or all cars inactive.
- Selection setup: top `5` parents with mutation rate `0.12`.
- Quantified improvement across generations (for example pass-rate gain over time): `UNVERIFIED`.
- Runtime/FPS benchmarks across devices: `UNVERIFIED`.

## Quantification Candidates

- User-confirmed estimate: `100x` increase in experiment throughput versus testing one car at a time
  - Basis: the simulation evaluates 100 AI cars in a generation instead of a single-car run.
- User-confirmed estimate: `~23%` reduction in debugging or tuning time after adding live visualization and saved-brain workflow
  - Basis: visualization and persistence made behavior easier to inspect across runs.

## Best-Fit Job Signals

- Browser-based simulation engineering
- Applied ML prototyping (without external frameworks)
- Algorithmic geometry and collision logic
- Real-time Canvas visualization
- Evolutionary optimization fundamentals
- Frontend state persistence and interactive controls

## Bullet Bank (Truthful Variants)

- Built a browser-based autonomous driving simulation in vanilla JavaScript, implementing road geometry, vehicle physics, and collision checks, enabling 100 concurrent AI cars to run per generation client-side.
- Implemented a 7-ray sensing system with intersection-based obstacle detection, feeding normalized inputs into a custom neural network, which enabled real-time steering and throttle decisions each frame.
- Wrote a hand-built `7 -> 8 -> 4` feed-forward network and mutation routine, avoiding external ML libraries, so behavior updates could be generated directly in the browser.
- Designed a generation pipeline that scores cars by passes plus penalties, ranks candidates, and seeds top-parent mutations, ensuring selection favors overtaking progress over simple survival.
- Added dual-canvas rendering for both driving scene and network state, making weights/activations visible during execution and improving model decision transparency.
- Implemented save/reset controls with `localStorage` compatibility checks, preserving the best-performing brain across sessions for repeatable experimentation.
