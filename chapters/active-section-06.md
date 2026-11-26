# 7.6 Self-adaptive and learning metasurfaces

Instructor booklet, pages 195–199.

The reconfigurable metasurfaces studied so far depended on external computation or on continued intervention by an operator. In field applications such as interference protection, high-speed radio links to moving objects, or biosensing, the electromagnetic environment can change rapidly.

If every change requires external measurements, transmission to a central computer, heavy processing, and new control codes, processing latency can undermine real-time performance. The proposed approach integrates physical sensing and onboard processors into self-adaptive or cognitive metasurfaces.

## 7.6.1 An autonomous metasurface and its physical closed loop

A self-adaptive metasurface should sense local changes without an external command. It can observe incidence angle, polarization, frequency, power level, and even physical changes such as bending. It then makes a decision and changes its electromagnetic configuration.

A three-stage closed loop implements this:

1. **Sense.** Embed electromagnetic sensors such as RF Schottky power detectors, angle sensors that use local phase difference, polarization sensors, and near-field sampling probes.
2. **Decide.** Process the sensor signals with an embedded processor. Examples include a compact neural network on an FPGA, a low-power microcontroller, or analog neuromorphic circuitry.
3. **Act.** Generate new bias voltages for PIN diodes, varactors, graphene, or phase-change films to shape the beam. The booklet describes submicrosecond actuation as an example. Actual timing depends on loading the codes and settling the devices.

## 7.6.2 Sensor-integrated meta-atoms

A major challenge is integrating a sensor with a reflective or transmissive patch without detuning the resonance or reducing radiation gain. Two principal approaches are described:

- **Sparse sensing array.** Equip only a small fraction of cells, for example 1–5%, with RF detectors. Reconstruct the field from measurements at those points using interpolation or a statistical model.
- **Weakly coupled probing.** A small microstrip line or coupling aperture behind the radiating patch samples a small fraction of incident power, below 1% or below $-20\,\mathrm{dB}$, and delivers it to a Schottky detector under the dielectric. In an ideal system without loss, transmission, or other scattering channels, the remaining power may be reflected. A probe fraction below 1% does not by itself establish above 99% reflection.

## 7.6.3 Machine-learning architectures for intelligent metasurfaces

Optimization methods such as genetic algorithms and particle swarm optimization (PSO) may converge too slowly for a real-time deadline. A pretrained model can produce an answer in one pass, without an iterative search during operation. The booklet's $O(1)$ description applies only to the fixed number of passes for a fixed model. Inference time depends on model size and hardware.

### 1. Feedforward deep neural networks (DNN)

Train the network with an inverse mapping:

- **Input:** sensed field conditions, such as input power $P_{\rm in}$, estimated incidence angle $\theta_{\rm inc}$, and target direction $\theta_{\rm target}$.
- **Output:** the array of surface control codes, $\Gamma=[C_1,C_2,\ldots,C_N]$.

Lightweight processing cores can perform the inference. The nanosecond-to-microsecond times discussed in the booklet depend on the network, hardware, and type of computation. Whole-surface adjustment includes sensing, writing, and settling.

### 2. Deep reinforcement learning (DRL)

When a precise model of the environment is unavailable, for example after a room layout changes or an unexpected obstacle enters, define the following:

- The metasurface acts as the **agent**.
- Its **state** or observation includes received signal power.
- An **action** changes the cell phases.
- The **reward** is an improvement in SNR or data rate.

The agent can search for useful patterns through trial and error without a prior channel model. Learning does not guarantee a global optimum, convergence, or performance in a new environment.

## 7.6.4 Applications of self-adaptive metasurfaces

1. **Adaptive electromagnetic camouflage.** This proposed application senses illumination conditions and changes the scattering pattern to modify radar cross section. Performance depends on angle, frequency band, and testing of the actual device.
2. **Deformation self-compensation.** Mechanical changes alter phases on a flexible metasurface mounted on an aircraft or smart clothing. Strain gauges report the deformation to the controller, which adjusts phases to recover the focused beam.
3. **Smart radio walls.** When people or vehicles block a radio path, a metasurface wall can redirect its reflected beam toward the user. Continuity of the link must be tested under actual conditions.

## Problem statement

::::{admonition} Try it first
:class: book-exercise

People walking through a corridor sometimes block the direct path between an access point and a user terminal. A wall-mounted $16\times16$ reflecting metasurface supplies an alternative path. The operating frequency is $10\,\mathrm{GHz}$, the cell pitch is $d=\lambda_0/2$, and each cell permits $0^\circ$, $90^\circ$, $180^\circ$, and $270^\circ$. Assume equal reflection amplitude for all four states.

Only 8 of the 256 cells have sensors. Two adjacent sensors along $x$ use a coherent receiver to measure the incident phase difference. At one instant the right sensor reads $-90^\circ$ relative to the left. Assume a plane wave in the $xz$ plane. The initial aim is to reflect at broadside to the wall.

- Each probe samples $0.5\%$ of local power. Local incident power is $-30\,\mathrm{dBm}$ and the sensing receiver's minimum detectable power is $-58\,\mathrm{dBm}$.
- Sensing and feature extraction take $8\,\mathrm{\mu s}$, neural-network inference on the FPGA takes $4\,\mathrm{\mu s}$, and bias settling takes $1.6\,\mathrm{\mu s}$. Four parallel lines send data without overhead at $20\,\mathrm{Mbit/s}$ each. The characteristic channel variation time is $1\,\mathrm{ms}$.
- After the initial setting, an obstacle changes the corridor multipath. The user terminal can report SNR. To study bending, assume one cell moves $4\,\mathrm{mm}$ normal to the wall toward the space in front of it.

Find the incident angle and initial phase code. Evaluate the probe power budget and loop latency. Compare pretrained inference with learning from receiver feedback. Find a phase correction for the displaced cell.

```{dropdown} Show the full worked answer

### 1. Sparse sensing: from phase difference to incidence angle

First find the fraction of instrumented cells:

$$
\frac{8}{256}\times100=3.125\%.
$$

The sensing array is sparse. In the single-plane-wave model we need not measure the field at all 256 cells to find the $x$ slope. Define the incident angle by $k_{x,\rm inc}=k_0\sin\theta_{\rm inc}$, so a positive angle means positive tangential wave number. The right-minus-left phase is

$$
\Delta\phi_{\rm sense}=-k_{x,\rm inc}d=-k_0d\sin\theta_{\rm inc}.
$$

With $d=\lambda_0/2$, $k_0d=\pi$, hence

$$
-\pi/2=-\pi\sin\theta_{\rm inc}
\quad\Rightarrow\quad \theta_{\rm inc}=+30^\circ.
$$

The calculation uses **coherent phase measurement**. A power detector alone cannot measure relative phase. With several simultaneous incident waves, one pair's phase difference may not identify the direction of any one wave. More sensors and a suitable estimation model are then needed.

### 2. Weakly coupled probe: is the sample measurable?

Power coupling is $0.005$:

$$
10\log_{10}(0.005)\simeq-23.0\,\mathrm{dB},\qquad
P_{\rm sample}=-30-23.0=-53.0\,\mathrm{dBm}.
$$

Ignoring extra path loss, this is about $5\,\mathrm{dB}$ above the stated threshold. The power budget permits sampling. Precise angle estimation also requires phase accuracy and calibration of the two channels.

Weak coupling does not guarantee $99.5\%$ reflected power. The $0.5\%$ describes only the probe's share. Material loss, bias circuitry, and other scattering channels are excluded. **Sparse sensing** reduces the number of instrumented cells; **weak coupling** limits the power sampled at each instrumented cell.

### 3. Decide and act: how is the beam redirected to broadside?

At $x_m=md$, the incident wave has phase $-k_{x,\rm inc}x_m$. The surface compensates the incident slope so that the columns add coherently at broadside:

$$
\Delta\phi_{\rm act}=k_{x,\rm inc}d=\pi\sin30^\circ=\pi/2.
$$

Set the first column to zero, then repeat $[0^\circ,90^\circ,180^\circ,270^\circ]$ four times over sixteen columns. No $y$ gradient is needed, so use the sequence in all sixteen rows. In this case there is no phase-rounding loss, because all required phases already belong to the two-bit codebook. Other angles do not necessarily share this property.

This simple geometry gives an analytical code without a neural network. The response can be a **benchmark for the pretrained network**: from estimated angle, sensed power, and target direction, it should produce a code with similar performance. Calibration data can help because actual cell phases and mutual interactions may differ from the ideal model. Inference avoids an iterative run-time search, but its cost depends on model size and hardware. The $4\,\mathrm{\mu s}$ figure is an assumption for this implementation.

### 4. Loop latency: network speed versus system speed

Four states require two bits per cell, or 512 bits. The aggregate line rate is $80\,\mathrm{Mbit/s}$:

$$
t_{\rm load}=\frac{512}{80\times10^6}=6.4\,\mathrm{\mu s}.
$$

With sequential stages, time from sensing to a settled surface is

$$
\begin{aligned}
t_{\rm loop}&=t_{\rm sense}+t_{\rm decide}+t_{\rm load}+t_{\rm settle}\\
&=(8+4+6.4+1.6)\,\mathrm{\mu s}=20\,\mathrm{\mu s}.
\end{aligned}
$$

This is 2% of the $1\,\mathrm{ms}$ channel timescale, so local adjustment is faster than the changes specified. Periodic sensing adds the wait until the next sample. If decisions depend on a user report, include report transmission and reception time separately. A $20\,\mathrm{\mu s}$ local loop does not guarantee uninterrupted communication.

### 5. Learning from feedback: when the incident angle is insufficient

After blockage, the wave reaching the wall may still arrive at about $30^\circ$, while the wall-to-user path changes. A controller that observes only the incident angle might retain the old code despite falling SNR. This is why receiver feedback matters.

Suppose the controller can try three preselected codes. The **action** is choosing a code, and the **observation** can include estimated angle and latest reported SNR. Define reward as SNR improvement over the reference code under the same channel conditions.

| Tested code | Reported SNR | Reward relative to reference |
| --- | --- | --- |
| A: reference | $8\,\mathrm{dB}$ | $0\,\mathrm{dB}$ |
| B: first alternative | $12\,\mathrm{dB}$ | $+4\,\mathrm{dB}$ |
| C: second alternative | $7\,\mathrm{dB}$ | $-1\,\mathrm{dB}$ |

If the channel remains approximately constant during the trials, B is the best **among the tested options**. Update estimated scores as new rewards arrive so one noisy observation does not determine the decision. If B's previous score was 2 and update rate $\alpha=0.5$,

$$
Q_{\rm new}(B)=Q_{\rm old}(B)+\alpha[r_B-Q_{\rm old}(B)]
=2+0.5(4-2)=3.
$$

This is a simple selection and feedback-learning exercise. In a larger problem a network can estimate code values or a selection policy from observations. A **pretrained network** proposes a code from sensed conditions. **Feedback learning** measures what the code actually did to the current link. The controller still decides, and the reported SNR is a measurement rather than a surface command.

### 6. Bending compensation: from measured displacement to phase correction

At $10\,\mathrm{GHz}$ the wavelength is about $30\,\mathrm{mm}$. Suppose strain sensors and a calibrated mechanical model estimate $\delta z=+4\,\mathrm{mm}$. Displacement outward shortens both the incident and outgoing paths. A shorter path increases the received phase:

$$
\begin{aligned}
\Delta\phi_{\rm geom}
&=k_0\delta z(\cos\theta_{\rm inc}+\cos\theta_{\rm out})\\
&=\frac{360^\circ}{30\,\mathrm{mm}}(4\,\mathrm{mm})(\cos30^\circ+\cos0^\circ)
\simeq+89.6^\circ.
\end{aligned}
$$

Add about $-89.6^\circ$ to the original cell phase. The nearest two-bit correction is $-90^\circ$, one state backward. For example, $180^\circ$ becomes $90^\circ$. The residual phase error is about $0.4^\circ$. This calculation treats only the **geometrical displacement**. Phase correction alone is insufficient if bending also rotates the patch, detunes resonance, or changes reflection amplitude.

**Summary.** Surface sensors estimated the incident direction. The controller applied a reflection code in time. User feedback revealed whether the code improved the link. The same architecture can convert mechanical sensor data into phase corrections. Its success depends on observability, whole-loop speed, and an appropriate feedback criterion.
```
::::

[Computational reading](active-computational.md) · [Lab](../labs/07-tunable-lab.md)
